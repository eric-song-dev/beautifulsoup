import unittest
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

class TestSoupReplacer(unittest.TestCase):
    """Test the SoupReplacer API."""

    # M2 Tests

    def test_basic_replacement(self):
        """Test that <b> is replaced by <blockquote>."""
        markup = "<p>Here is <b>bold text</b>.</p>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNone(soup.find("b"))
        self.assertIsNotNone(soup.find("blockquote"))
        self.assertEqual(
            str(soup.p),
            "<p>Here is <blockquote>bold text</blockquote>.</p>"
        )

    def test_no_replacement(self):
        """Test that <i> is not replaced."""
        markup = "<p>Here is <i>italic text</i>.</p>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNone(soup.find("b"))
        self.assertIsNone(soup.find("blockquote"))
        self.assertIsNotNone(soup.find("i"))
        self.assertEqual(
            str(soup.p),
            "<p>Here is <i>italic text</i>.</p>"
        )

    def test_multiple_and_nested_replacements(self):
        """Test that multiple and nested <b> tags are replaced."""
        markup = "<b>One</b> <b>Two</b> <b>Three</b>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNone(soup.find("b"))
        self.assertEqual(len(soup.find_all("blockquote")), 3)
        self.assertEqual(
            str(soup),
            "<blockquote>One</blockquote> <blockquote>Two</blockquote> <blockquote>Three</blockquote>"
        )

    # M3 Tests

    def test_name_xformer(self):
        """Test name_xformer"""
        markup = "<p>Here is <b>bold text</b>.</p>"
        replacer = SoupReplacer(
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
        )
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNone(soup.find("b"))
        self.assertIsNotNone(soup.find("blockquote"))
        self.assertEqual(
            str(soup.p),
            "<p>Here is <blockquote>bold text</blockquote>.</p>"
        )

    def test_attrs_xformer(self):
        """Test attrs_xformer."""
        markup = '<p class="old">Here is <i>italic</i>.</p>'

        def attrs_transformer(tag):
            if tag.name == 'p':
                attrs = tag.attrs.copy()
                attrs['class'] = 'test'
                attrs['data'] = 'true'
                return attrs
            return tag.attrs

        replacer = SoupReplacer(attrs_xformer=attrs_transformer)
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNotNone(soup.find("p"))
        self.assertEqual(soup.p['class'], 'test')
        self.assertEqual(soup.p['data'], 'true')
        self.assertEqual(
            str(soup.p),
            '<p class="test" data="true">Here is <i>italic</i>.</p>'
        )

    def test_xformer(self):
        """Test xformer."""
        markup = '<p class="old">Here is <i class="delete">italic</i>.</p>'

        def side_effect_transformer(tag):
            if tag.name == 'p':
                tag.attrs['class'] = 'test'
                tag.attrs['data'] = 'true'
            if tag.name == 'i':
                del tag.attrs['class']

        replacer = SoupReplacer(xformer=side_effect_transformer)
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNotNone(soup.find("p"))
        self.assertEqual(soup.p['class'], 'test')
        self.assertEqual(soup.p['data'], 'true')
        self.assertNotIn('class', soup.i.attrs)
        a = str(soup.p)
        self.assertEqual(
            str(soup.p),
            '<p class="test" data="true">Here is <i>italic</i>.</p>'
        )

    def test_priority_name_xformer_over_og_tag_and_alt_tag(self):
        """Test that name_xformer has priority over og_tag/alt_tag."""
        markup = "<b>bold</b>"
        replacer = SoupReplacer(
            og_tag="b", alt_tag="should-be-ignored",
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
        )
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)
        self.assertEqual(str(soup), "<blockquote>bold</blockquote>")

    def test_og_tag_and_alt_tag_compatibility_with_xformer(self):
        """Test og_tag/alt_tag replacer still works alongside xformer."""
        markup = "<b>bold</b> <i>italic</i>"

        def add_id(tag):
            tag.attrs['id'] = 'id-' + tag.name

        replacer = SoupReplacer(
            og_tag="b", alt_tag="blockquote",
            xformer=add_id
        )
        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertEqual(
            str(soup),
            '<blockquote id="id-blockquote">bold</blockquote> <i id="id-i">italic</i>'
        )

    def test_all_parameters_priority(self):
        """
        Test priority when all parameters are provided.
        Expected order:
        1. name_xformer (overrides og_tag/alt_tag)
        2. attrs_xformer (runs first on the tag object)
        3. xformer (runs second, can override attrs_xformer)
        """
        markup = '<b class="original">bold</b>'

        replacer = SoupReplacer(
            # og_tag/alt_tag (should be ignored by name_xformer)
            og_tag="b",
            alt_tag="i",

            # name_xformer (should run)
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name,

            # attrs_xformer (should run first)
            attrs_xformer=lambda tag: {'class': ['from-attrs-xformer']} if tag.name == 'blockquote' else tag.attrs,

            # xformer (should run second and override class)
            xformer=lambda tag: tag.attrs.update(
                {'class': ['from-xformer'], 'id': 'final'}) if tag.name == 'blockquote' else None
        )

        soup = BeautifulSoup(markup, "html.parser", replacer=replacer)

        self.assertIsNone(soup.find('b'))
        self.assertIsNone(soup.find('i'))
        self.assertIsNotNone(soup.find('blockquote'))

        tag = soup.find('blockquote')
        self.assertEqual(tag.name, 'blockquote')
        self.assertEqual(tag['class'], ['from-xformer'])
        self.assertEqual(tag['id'], 'final')
        self.assertEqual(
            str(soup),
            '<blockquote class="from-xformer" id="final">bold</blockquote>'
        )