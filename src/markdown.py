import re 

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text):
    old_node = TextNode(text, text_type_text)

    new_node = split_nodes_delimiter([old_node], '**', text_type_bold)
    new_node = split_nodes_delimiter(new_node, '*', text_type_italic)
    new_node = split_nodes_delimiter(new_node, '`', text_type_code)
    new_node = split_nodes_image(new_node)
    new_node = split_nodes_link(new_node)
    
    return new_node


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        node_text = old_node.text
        extracted_links = extract_markdown_images(node_text)

        if len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue

        for image_alt, image_link in extracted_links:
            parts = node_text.split(f"![{image_alt}]({image_link})", 1)
            
            if len(parts) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))

            new_nodes.append(TextNode(image_alt, text_type_image, image_link))

            node_text = parts[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        node_text = old_node.text
        extracted_links = extract_markdown_links(node_text)

        if len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue

        for alt_text, url in extracted_links:
            parts = node_text.split(f"[{alt_text}]({url})", 1)

            if len(parts) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))

            new_nodes.append(TextNode(alt_text, text_type_link, url))

            node_text = parts[1]

        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError('Invalid markdown, formatted section not closed')
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
