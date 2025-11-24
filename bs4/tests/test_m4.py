import unittest
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment


class TestMilestone4(unittest.TestCase):
    """Test cases to verify that the BeautifulSoup object is iterable via depth-first traversal."""

    def test_iteration_yields_all_nodes(self):
        """Test 1: Verify that iteration."""
        html = "<html><body><p>Test</p></body></html>"
        soup = BeautifulSoup(html, 'html.parser')

        # Collect nodes to verify count and content
        nodes = [node for node in soup]

        # Expected nodes: html, body, p, "Test"
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].name, 'html')
        self.assertEqual(nodes[3], 'Test')

    def test_iteration_order(self):
        """Test 2: Verify that iteration follows document order (depth-first)."""
        html = "<div><a>1</a><b>2</b></div>"
        soup = BeautifulSoup(html, 'html.parser')

        expected_names = ['div', 'a', '1', 'b', '2']
        # Convert actual nodes to names
        actual_names = []
        for node in soup:
            if isinstance(node, Tag):
                actual_names.append(node.name)
            elif isinstance(node, NavigableString):
                actual_names.append(str(node))

        self.assertEqual(actual_names, expected_names)

    def test_iteration_types(self):
        """Test 3: Verify iteration yields different types of PageElements (Tags, Strings, Comments)."""
        html = "<div><!-- comment -->text</div>"
        soup = BeautifulSoup(html, 'html.parser')

        nodes = list(soup)

        self.assertTrue(isinstance(nodes[0], Tag))  # div
        self.assertTrue(isinstance(nodes[1], Comment))  # comment
        self.assertTrue(isinstance(nodes[2], NavigableString))  # text

    def test_empty_soup_iteration(self):
        """Test 4: Verify iteration on an empty soup yields nothing."""
        soup = BeautifulSoup("", 'html.parser')
        nodes = list(soup)
        self.assertEqual(len(nodes), 0)

    def test_memory_efficiency_check(self):
        """Test 5: Ensure __iter__ returns a generator/iterator, not a list."""
        html = "<root><child>1</child><child>2</child></root>"
        soup = BeautifulSoup(html, 'html.parser')

        iterator = iter(soup)

        # It should not be a list
        self.assertNotIsInstance(iterator, list)
        # It should be an iterator (has __next__)
        self.assertTrue(hasattr(iterator, '__next__') or hasattr(iterator, 'next'))

        # Consuming one item shouldn't consume all
        first_node = next(iterator)
        self.assertEqual(first_node.name, 'root')