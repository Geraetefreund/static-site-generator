import re
from textnode import TextNode, text_type_text, text_type_image, text_type_link


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

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
            
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], text_type_text))

            new_nodes.append(TextNode(image_alt, text_type_image, image_link))

            node_text = parts[1]
    return new_nodes




def split_nodes_link(old_nodes):
    pass



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
