import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def isinstance(self):
        node = HTMLNode()
        self.assertIsInstance(node, htmlnode.HTMLNode, "it is")

    def is_empty(self):
        node = HTMLNode()
        self.assertIs(node.tag, None, "okay")

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()
