import assert from "node:assert/strict";
import { chromium } from "playwright";
const base = process.env.TEST_BASE_URL ?? "http://127.0.0.1:8080";
for (let attempt = 0; attempt < 60; attempt += 1) {
  try { if ((await fetch(base)).ok) break; } catch { /* preview server is starting */ }
  if (attempt === 59) throw new Error("Preview server did not become ready");
  await new Promise(resolve => setTimeout(resolve, 500));
}
const browser = await chromium.launch({ headless: true });
try {
  for (const width of [320, 375, 768, 1440]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: "reduce" });
    const page = await context.newPage();
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.goto(base);
    assert.equal(await page.locator("h1").count(), 1);
    for (const name of ["Projects", "Experience", "About", "Contact"]) {
      assert.ok(await page.getByRole("navigation").getByRole("link", { name, exact: true }).isVisible());
    }
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `overflow at ${width}`);
    await page.keyboard.press("Tab");
    assert.equal(await page.locator(":focus").textContent(), "Skip to main content");
    await page.keyboard.press("Enter");
    assert.equal(await page.locator(":focus").getAttribute("id"), "main");
    assert.deepEqual(errors, []);
    await context.close();
  }
  const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 375, height: 900 } });
  const page = await context.newPage();
  await page.goto(base);
  assert.ok(await page.getByRole("heading", { name: "Machinery Find", exact: true }).isVisible());
  assert.ok(await page.getByRole("link", { name: "Explore DevDocs AI source →", exact: true }).isVisible());
  await context.close();
  console.log("Portfolio browser checks passed: four viewport widths, visible navigation, skip-link focus, no page errors, and JavaScript-disabled content.");
} finally { await browser.close(); }
