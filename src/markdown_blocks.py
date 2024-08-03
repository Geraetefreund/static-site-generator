def markdown_to_blocks(markdown):
    blocks = []
    split = markdown.split('\n\n')
    for item in split:
        if item == "":
            continue
        blocks.append(item.strip())
    return blocks


