import re, yaml
from pathlib import Path

compiled = []

def addln(addln: str):
    global compiled
    compiled.append(addln)

# paths
web_path = Path.home() / 'software' / 'web'
config = web_path / 'config.yaml'
html_template = web_path / 'template.html'
html_output = web_path / 'homepage.html'

    # read in config
with open(config, 'r') as file:
    config_data = yaml.safe_load(file)

# compile title
compiled_title = ""
if config_data['title']:
    compiled_title += ("%s" % config_data['title'])

# combile blocks
compiled_blocks = ""
if config_data['blocks']:
    compiled_blocks += "\n" + "<div class=\"block-grid\">"
    for block in config_data['blocks']:
        # block title
        compiled_blocks += "\n" + ("<div class=\"inset block\">")
        compiled_blocks += "\n" + ("<h3>%s</h3>" % block)
        compiled_blocks += "\n" + ("<ul>")
        for block_item in config_data['blocks'][block]:
            # block item
            compiled_blocks += "\n" + ("<li><a href=\"%s\">%s</a></li>" \
                    % (r'https:\\' + block_item[1], block_item[0]))
        compiled_blocks += "\n" + ("</ul>")
        compiled_blocks += "\n" + ("</div>")
    compiled_blocks += "\n" + "</div>"

# read in html template
with open(html_template, 'r') as file:
    input_string = file.read()

# replace template elements
compiled = re.sub("\{\{\s*title\s*\}\}",
                  compiled_title,
                  input_string)

compiled = re.sub("\{\{\s*blocks\s*\}\}",
                  compiled_blocks,
                  compiled)

# write to output file
with open(html_output, "w") as outfile:
    outfile.writelines(compiled)
