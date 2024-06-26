import os
import shutil

from pathlib import Path
from markdown_blocks import markdown_to_html_node

static_dir_path = "./static"
public_dir_path = "./public"
content_dir_path = "./content"
template_path = "./template.html"
def main():
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    cp_recursive(static_dir_path, public_dir_path)
    print('Done!')
    generate_pages_recursive(
        content_dir_path,
        template_path,
        public_dir_path,
    )

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def cp_recursive(source, target):
    if os.path.isfile(source):
        shutil.copy(source, target)
    else:
        if not os.path.exists(target):
            os.mkdir(target)
        for item in os.listdir(source):
            new_source = os.path.join(source, item)
            new_target = os.path.join(target, item)
            cp_recursive(new_source, new_target)

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:]
    raise ValueError('No title found')

def generate_page(source_path, template_path, target_path):
    print(f'Generating page from {source_path} to {target_path} using {template_path}')
    source_file = open(source_path, 'r') # open file handler for reading
    markdown_text = source_file.read()
    source_file.close() # close file handler
    # handle template
    print(f'template_path: {template_path}')
    template_file = open(template_path, 'r')
    template_text = template_file.read()
    template_file.close()
    # generate html from markdown
    node = markdown_to_html_node(markdown_text)
    html = node.to_html()
    # replace title in template
    title = extract_title(markdown_text)
    template = template_text.replace('{{ Title }}', title)
    template = template_text.replace('{{ Content }}', html)
    # write target file
    tgt_dir_path = os.path.dirname(target_path)
    if tgt_dir_path != "":
        os.makedirs(tgt_dir_path, exist_ok=True)
    tgt_file = open(target_path, 'w') # open file handler for writing
    tgt_file.write(template)
    tgt_file.close()

main()

