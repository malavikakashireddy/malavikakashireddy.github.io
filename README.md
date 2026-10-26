# Malavika Kashireddy — Engineering Portfolio

A static HTML/CSS/JavaScript portfolio for 2027 new graduate software engineering roles. It presents UIC education, selected source repositories, professional experience, and direct contact links.

## Local preview

Requires Python 3; there is no application build step or runtime package installation. Optional browser checks use a Node.js development dependency.

```bash
python3 -m http.server 8080 --bind 127.0.0.1
# Open http://127.0.0.1:8080
python3 -m unittest discover -s tests -v
```

`index.html` is the canonical page; `styles.css` controls the responsive layout and `script.js` progressively updates the footer year. All core content/navigation works without JavaScript. System fonts avoid third-party font requests. The older standalone HTML URL redirects to the canonical page.

## Project status and content policy

The three featured project improvements have been merged into their main branches after passing checks. Project labels describe the implemented scope: a catalog demo, a local event-pipeline prototype, and a lexical retrieval baseline. Keep these descriptions aligned with the source and validation evidence as the projects evolve.

Unsupported project benchmark numbers and the inaccessible job-processing project have been removed from the page. Experience descriptions are based on candidate-provided history; they are not independently verified by public employer code. The original `resume.pdf` remains unchanged, but its download links are removed because its project bullets still include unverified metrics. Replace/review that PDF before restoring a resume download. Email remains available for resume requests.

The website is served from `main` by GitHub Pages. Future merges to main may publish the website automatically and require the owner’s explicit approval. The CI workflow performs checks only; it does not deploy.

## Accessibility and maintenance

- Semantic sections, heading hierarchy, descriptive source links, keyboard focus, and a skip link.
- Navigation remains visible on small screens, responsive grids, and reduced-motion support.
- Canonical/Open Graph metadata, `robots.txt`, and `sitemap.xml`.
- Local validation checks asset/anchor integrity, external-link safety, essential metadata, and retired claims.

[Validation evidence](docs/VALIDATION.md) records checks that actually ran. A real assistive-technology review and current external-site content verification remain separate tasks. [The profile README](docs/github-profile/README.md) is ready to use in the special `malavikakashireddy/malavikakashireddy` repository, which is not currently present in the connected account.

Optional browser validation (Node.js 24 and a running local preview):

```bash
npm ci
npx playwright install chromium
npm run test:browser
```

The script checks four viewport widths, navigation visibility, skip-link focus, absence of page errors, and content with JavaScript disabled. It does not certify screen-reader conformance or Web Vitals.
