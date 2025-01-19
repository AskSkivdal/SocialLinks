from jinja2 import Environment, FileSystemLoader
import json
import os, pathlib, shutil

os.makedirs("build/icons", exist_ok=True)

env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template("page.jinja")

class SocialLink:
    def __init__(self, url: str, icon=None, title=None):
        self.url = url
        self.title = title

        if icon:
            self.iconpath = pathlib.Path(icon)
            self.icon = self.iconpath.name
        else:
            self.icon =  url.split("/")[2] + ".svg"
            self.iconpath = "./icons/" + self.icon


links = json.load(open("links.json", "r"))

socialLinks = []

for link in links["links"]:
    l = SocialLink(
        link["url"], 
        title=link["title"] if "title" in link.keys() else None,
        icon=link["icon"] if "icon" in link.keys() else None,
        )
    
    iconPath = pathlib.Path(l.iconpath)
    shutil.copy(iconPath, "build/icons")

    socialLinks.append(l)

html = template.render(socialLinks=socialLinks)

with open('build/index.html', 'w', encoding="UTF-8") as f:
    f.write(html)