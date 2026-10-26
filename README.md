# Malavika Kashireddy — Engineering Portfolio

A static HTML/CSS/JavaScript portfolio for 2027 new graduate software engineering roles. It presents UIC education, selected source repositories, professional experience, and direct contact links.

## Local preview

Requires Python 3; there is no build step or package installation.

```bash
python3 -m http.server 8080 --bind 127.0.0.1
# Open http://127.0.0.1:8080
python3 -m unittest discover -s tests -v
```

`index.html` is the canonical page; `styles.css` controls the responsive layout and `script.js` progressively updates the footer year. All core content/navigation works without JavaScript. System fonts avoid third-party font requests. The older standalone HTML URL redirects to the canonical page.

## Review status and content policy

These changes are prepared on a review branch. They do not publish a deployment. Project status labels distinguish existing prototypes from work in review; update those labels after the corresponding project PRs merge and their checks succeed.

Unsupported project benchmark numbers and the inaccessible job-processing project have been removed from the proposed page. Experience descriptions are based on candidate-provided history; they are not independently verified by public employer code. The original `resume.pdf` remains unchanged, but its download links are removed because its project bullets still include unverified metrics. Replace/review that PDF before restoring a resume download. Email remains available for resume requests.

The website is served from `main` by GitHub Pages. Merging this branch may publish the website automatically, so merge/publish requires the owner’s explicit approval. The CI workflow performs checks only; it does not deploy.

## Accessibility and maintenance

- Semantic sections, heading hierarchy, descriptive source links, keyboard focus, and a skip link.
- Navigation remains visible on small screens, responsive grids, and reduced-motion support.
- Canonical/Open Graph metadata, `robots.txt`, and `sitemap.xml`.
- Local validation checks asset/anchor integrity, external-link safety, essential metadata, and retired claims.

[Validation evidence](docs/VALIDATION.md) records checks that actually ran. A real assistive-technology review and current external-site content verification remain separate tasks. [The profile README](docs/github-profile/README.md) is ready to use in the special `malavikakashireddy/malavikakashireddy` repository, which is not currently present in the connected account.
