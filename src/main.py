import os
import shutil
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import *

def rem_public():
    path = 'public'
    if not os.path.exists(path):
        raise Exception(f'error: path ./{path} does not exist')
    shutil.rmtree(path)
    print(f'path: ./{path} successfully removed')

def copy_from_to(source, destination):
    if not os.path.exists(destination):
        print(f'creating folder: {destination}')
        os.mkdir(destination)
    items = os.listdir(source)
    for item in items:
        src = os.path.join(source, item)
        dest = os.path.join(destination, item)
        if not os.path.isfile(src):
            if not os.path.exists(dest):
                print(f'creating dir: {dest}')
                os.mkdir(dest)
            copy_from_to(src, dest)
        else:
            print(f'copying file: {dest}')
            shutil.copy(os.path.join(source, item), os.path.join(destination, item))
    
def generate_page(from_path, template_path, dest_path):
    with open(from_path, 'r') as file:
        src_file = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    html_node = markdown_to_html_node(src_file)
    html_string = html_node.to_html()
    title = extract_title(src_file)
    result = template.replace('{{ Title }}', title).replace('{{ Content }}', html_string)
    with open(dest_path, 'w') as file:
        file.write(result)
    #print(f'Generating page from {from_path} to {dest_path} using {template_path}.')

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        src_path = os.path.join(dir_path_content, item) 
        dest_path = os.path.join(dest_dir_path, item) 
        if os.path.isdir(src_path):
            print(f'creating directory: {dest_path}')
            os.mkdir(dest_path)
            generate_pages_recursive(src_path, template_path, dest_path)
        else:
            dest_path = dest_path.replace('.md', '.html')
            generate_page(src_path, template_path, dest_path)


def main():
    try:
        rem_public()
    except:
        print('folder public does not exist')

    copy_from_to('static', 'public')
    #generate_page('./content/index.md', './template.html', './public/index.html')
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == '__main__':
    main()

