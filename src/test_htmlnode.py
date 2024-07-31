import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"},)
        self.assertEqual(
            node.__repr__(), 
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",)

    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, world!", 
                        None, {"class": "greeting", "href": "https://boot.dev"},)
        self.assertEqual(node.props_to_html(),
                         ' class="greeting" href="https://boot.dev"',)

    def test_eq(self):
        # keep in mind: needs to have def __eq__(self, other) in class declaration!
        node = HTMLNode("p", "Hello, world", None, {"class": "primary"},)
        node2 = HTMLNode("p", "Hello, world", None, {"class": "primary"},)
        self.assertEqual(node, node2)

    def test_values(self):
        node = HTMLNode("div", "I wish I could read",)
        self.assertEqual(node.tag, "div",)
        self.assertEqual(node.value, "I wish I could read",)
        self.assertEqual(node.children, None,)
        self.assertEqual(node.props, None,)

    def test_leafnode_repr(self):
        node = LeafNode("div", "Hello, world", {'class': 'beer_class'},)
        self.assertEqual(
            node.__repr__(), 
            "LeafNode(div, Hello, world, {'class': 'beer_class'})",)

    def test_leafnode_no_value(self):
        node = LeafNode('div', None)
        self.assertRaises(ValueError, node.to_html, )

    def test_leafnode_no_tag(self):
        node = LeafNode(None, "Some value", {'class': 'beer_class'},)
        self.assertEqual(node.to_html(), f"{node.value}")

    def test_leafnode_render_p(self):
        node = LeafNode("p", "This is a paragraph of text.",)
        self.assertEqual(node.to_html(), f'<p>This is a paragraph of text.</p>',)

    def test_leafnode_render_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"},)
        self.assertEqual(node.to_html(),
                f'<a href="https://www.google.com">Click me!</a>')

    def test_parentnode_repr(self):
        node = ParentNode('a', "I guess children", {"href": "https://www.google.com"})
        self.assertEqual(
            node.__repr__(), 
            "ParentNode(a, I guess children, {'href': 'https://www.google.com'})")

    def test_parentnode_to_html_no_tag(self):
        node = ParentNode(None, ['child_one', 'child_two'], 
                          {'href': "https://www.google.com"})
        self.assertRaises(ValueError, node.to_html,)


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), 
                         "<div><span><b>grandchild</b></span></div>")


    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    def test_to_html_props(self):
        node = ParentNode("a", [LeafNode("b", "Bold text within a link")],
                          props={'href': 'https://boot.dev'})
        self.assertEqual(node.to_html(),
                         '<a href="https://boot.dev"><b>Bold text within a link</b></a>')

if __name__ == "__main__":
    unittest.main()
