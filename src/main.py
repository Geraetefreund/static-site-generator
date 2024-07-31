from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode



def main():
    pass
#    node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
#    print(node.url)
#    node2 = HTMLNode("div", "Just for testing")
#    print(node2)
#    leaf = LeafNode('a', 'First LeafNode...', {"href": "https://boot.dev"})
#    print(leaf.to_html())
#    parent = ParentNode('a', ['a', 'b'], {'href': 'https://boot.dev'})
#    print(parent)
#    node5 = ParentNode( "p", [
#        LeafNode("b", "Bold text"),
#        LeafNode(None, "Normal text"),
#        LeafNode("i", "italic text"),
#        LeafNode(None, "Normal text"), 
#        ],
#    )
#    print(node5.to_html())
#
#    nested_node = ParentNode( "div", 
#            [ ParentNode( "p", 
#                [ LeafNode("b", "Nested Bold text"),
#                  LeafNode(None, "Nested Normal text"),
#                ]
#        ),
#        LeafNode("i", "Italic text outside nested p"),
#    ],
#    )
#    print(nested_node.to_html())
#
#    props_node = ParentNode( "a", [LeafNode("b", "Bold text within a link"),],
#        props={"href": "https://example.com"}
#    )
#    print(props_node.to_html())

main()
