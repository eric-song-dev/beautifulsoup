import unittest
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

class TestSoupReplacer(unittest.TestCase):
    """Test the SoupReplacer API."""

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