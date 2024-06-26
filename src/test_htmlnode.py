import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "click me", "", { "href": "https://thundron.dev", "target": "_blank" } )
        self.assertEqual(node.props_to_html(), 'href="https://thundron.dev" target="_blank"')


if __name__ == "__main__":
    unittest.main()
