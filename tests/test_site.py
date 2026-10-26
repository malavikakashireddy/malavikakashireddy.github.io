from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.elements = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / 'index.html').read_text()
        self.page = Page(self.html)

    def test_internal_links_and_assets_resolve(self):
        ids = [attrs['id'] for _, attrs in self.page.elements if 'id' in attrs]
        self.assertEqual(len(ids), len(set(ids)), 'duplicate IDs')
        for _, attrs in self.page.elements:
            for key in ('href', 'src'):
                value = attrs.get(key)
                if not value:
                    continue
                url = urlsplit(value)
                if url.scheme or url.netloc:
                    continue
                if url.path:
                    self.assertTrue((ROOT / unquote(url.path)).is_file(), value)
                if url.fragment:
                    self.assertIn(url.fragment, ids, value)

    def test_page_semantics_metadata_and_navigation(self):
        elements = self.page.elements
        self.assertEqual(sum(tag == 'h1' for tag, _ in elements), 1)
        self.assertTrue(any(tag == 'html' and attrs.get('lang') == 'en' for tag, attrs in elements))
        self.assertTrue(any(tag == 'link' and attrs.get('rel') == 'canonical' for tag, attrs in elements))
        for name in ('description', 'viewport'):
            self.assertTrue(any(tag == 'meta' and attrs.get('name') == name for tag, attrs in elements))
        links = {attrs.get('href') for tag, attrs in elements if tag == 'a'}
        self.assertTrue({'#main', '#work', '#experience', '#about', '#contact'} <= links)
        self.assertIn('class="skip-link"', self.html)

    def test_external_links_and_source_repositories(self):
        links = [attrs for tag, attrs in self.page.elements if tag == 'a']
        for attrs in links:
            if attrs.get('target') == '_blank':
                self.assertIn('noopener', attrs.get('rel', '').split())
        for repo in ('devdocs-ai', 'real-time-analytics-platform', 'machinery-find'):
            self.assertTrue(any(attrs.get('href') == 'https://github.com/malavikakashireddy/' + repo for attrs in links))

    def test_unverified_project_claims_are_not_published(self):
        for claim in ('5,000+', '~85%', 'Recall@5', '250</b>', '2,000+', 'Distributed Job Processing'):
            self.assertNotIn(claim, self.html)
        self.assertNotIn('href="resume.pdf"', self.html)
        self.assertIn('December 2026', self.html)
        self.assertIn('Mathematics minor', self.html)

    def test_alias_and_sitemap_point_to_canonical_site(self):
        self.assertIn('url=./index.html', (ROOT / 'Malavika Kashireddy _ Software Engineer.html').read_text())
        self.assertIn('https://malavikakashireddy.github.io/', (ROOT / 'sitemap.xml').read_text())


if __name__ == '__main__':
    unittest.main()
