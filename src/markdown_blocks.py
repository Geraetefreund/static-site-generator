import re
from htmlnode import *
from markdown_inline import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node = [block_to_block_type(block) for block in blocks]
    return html_node
        


def block_to_html_p(block):
    text_nodes = text_to_textnodes(block)
    leaf_nodes = [text_node_to_html_node(node) for node in text_nodes]
    html_node = ParentNode('p', leaf_nodes)
    return html_node

def block_to_html_heading(block):
    if block.startswith('# '):
        value = block.lstrip('# ')
        tag = 'h1'
    if block.startswith('## '):
        value = block.lstrip('## ')
        tag = 'h2'
    if block.startswith('### '):
        value = block.lstrip('### ')
        tag = 'h3'
    if block.startswith('#### '):
        value = block.lstrip('#### ')
        tag = 'h4'
    if block.startswith('##### '):
        value = block.lstrip('##### ')
        tag = 'h5'
    if block.startswith('###### '):
        value = block.lstrip('###### ')
        tag = 'h6'
    html_node = LeafNode(tag, value)
    return html_node

def block_to_html_code(block):
    value = block.strip('```').strip('\n')
    html_node = ParentNode("pre", [LeafNode("code", value)])
    return html_node

def block_to_html_quote(block):
    tag = 'blockquote'
    lines = block.splitlines()
    text = [text.append(line.lstrip('> ')) for line in lines ]
    value = "\n".join(text)
    html_node = LeafNode(tag, value)
    return html_node

def block_to_ulist(block):
    lines = block.splitlines()
    items = [re.sub(r'(?<!\*)\* |- ', '', line) for line in lines]
    children = [LeafNode('li', item) for item in items]
    parent_node = ParentNode('ul', children)
    return parent_node

def block_to_olist(block):
    lines = block.splitlines()
    items = [re.sub(r'^\d+\.\s+', '', line) for line in lines]
    children = [LeafNode('li', item) for item in items]
    parent_node = ParentNode('ol', children)
    return parent_node

def markdown_to_blocks(markdown):
    blocks = []
    split = markdown.split('\n\n')
    for item in split:
        if item == "":
            continue
        blocks.append(item.strip())
    return blocks

def block_to_block_type(block):
    lines = block.split('\n')
    if (
        block.startswith('# ')
        or block.startswith('## ')
        or block.startswith('### ')
        or block.startswith('#### ')
        or block.startswith('##### ')
        or block.startswith('###### ')
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return block_type_code
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    if block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('-'):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph


