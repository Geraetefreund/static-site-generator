import unittest

from markdown_blocks import (
    markdown_to_blocks,
)


class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_mine(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        text_blocks = markdown_to_blocks(text)
        self.assertEqual(
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ], 
            text_blocks
        )

    def test_m_t_b_empty_blocks(self):
        text = " # Heading with a whitespace before \n\nJust some **bold** text, really.  \n\n\n\n\n\n\nAnd some final text"
        text_blocks = markdown_to_blocks(text)
        self.assertEqual(
            [
                '# Heading with a whitespace before', 
                'Just some **bold** text, really.',
                'And some final text'
            ],
            text_blocks,
        )
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )



if __name__ == "__main__":
    unittest.main()
