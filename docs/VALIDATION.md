# Validation evidence — 2026-10-26

These results document the tested implementation. The featured project changes have since been merged into their main branches. Website publication has been approved; its hosting workflow records the deployment result.

| Check | Actual result |
| --- | --- |
| Python static-site checks | **5 passed** |
| JavaScript syntax | `node --check script.js` passed |
| Local HTML anchors and assets | Checked by tests; all resolve |
| Heading/metadata/source-link policy | Checked by tests |
| Legacy page alias/sitemap | Checked by tests |
| Original homepage at audit start | HTTP 200, 8,559-byte HTML; matched the audited original index content |
| Existing `resume.pdf` | Parsed; contains unsupported project metrics. Preserved but no longer prominently linked by the page |
| LinkedIn destination | URL matches existing site/resume; current ownership/content not independently verified |
| Email delivery | Address matches source/profile; no email sent and delivery not tested |
| Browser/mobile visual QA | [Passed in GitHub CI: run 40401372470](https://github.com/malavikakashireddy/malavikakashireddy.github.io/actions/runs/40401372470); local browser runtime unavailable |
| Keyboard/screen-reader testing | Skip-link focus verified in Chromium CI; human screen-reader review remains open |
| Remote CI / deployment | [Check-only workflow passed](https://github.com/malavikakashireddy/malavikakashireddy.github.io/actions/runs/40401372470); site publication uses the existing GitHub Pages workflow |

The new page uses semantic sections, a skip link, visible focus, persistent mobile navigation, responsive grids, and system fonts. All primary content exists in HTML and the script only updates the footer year; no JavaScript-driven reveal can hide project content. Chromium CI confirmed visible navigation, no horizontal overflow at 320/375/768/1440 px, skip-link focus, no page errors, and project content with JavaScript disabled. This is not a WCAG conformance claim. Core Web Vitals, human assistive-technology review, and additional browser engines remain unverified.

The profile README is a draft file under `docs/github-profile`; the special profile repository does not exist and the README has not been activated on the account.
