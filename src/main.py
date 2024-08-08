import os
import shutil
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def rem_public():
    path = 'public'
    if not os.path.exists(path):
        raise Exception(f'error: path ./{path} does not exist')
    shutil.rmtree(path)
    print(f'path: ./{path} successfully removed')

def copy_from_to(source, destination):
    if not os.path.exists(destination):
        print('creating folder: public')
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
    

def main():
    try:
        rem_public()
    except:
        print('folder public does not exist')

    copy_from_to('static', 'public')
main()

