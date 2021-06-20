# Created by  Manoj Paramsetti

import re
import discord

import requests

def embed(string, ctx, Color):
    embed=discord.Embed(color = Color())
    # setting embed color as red
    try:
        # spliting lines to check each line
        for line in string.split('\n'):
            # Checking the h1 tags using RegEx
            if re.match("^<h1>", line) and re.findall("<h1>$", line):
                text=line.split("<desc>")
                embed=discord.Embed(title = text[0][4:], description = text[1][:-4], color = Color())
            # Checking the h1 tags using RegEx
            elif re.match("^<h2>", line) and re.findall("<h2>$", line):
                text=line.split("<desc>")
                embed.add_field(name = text[0][4:], value = text[1][:-4], inline =False)
            # Checking the h1 tags using RegEx
            elif re.match("^<inline>", line) and re.findall("<inline>$", line):
                text=line.split("<desc>")
                embed.add_field(name = text[0][8:], value = text[1][:-8], inline= True)
            # Checking the h1 tags using RegEx
            elif re.match("^<img>", line) and re.findall("<img>$", line):
                if is_url_image(line[5:-5]):
                    embed.set_image(url=line[5:-5])
            # Checking the h1 tags using RegEx
            elif re.match("^<thumbnail>", line) and re.findall("<thumbnail>$", line):
                if is_url_image(line[11:-11]):
                    embed.set_thumbnail(url=line[11:-11])
            # Checking the h1 tags using RegEx
            elif re.match("^<footerImg>", line) and re.findall("<footerImg>$", line):
                text=line.split("<img>")
                if is_url_image(text[1][:-11]):
                    embed.set_footer(text = text[0][11:], icon_url = text[1][:-11])
            # Checking the h1 tags using RegEx
            elif re.match("^<footer>", line) and re.findall("<footer>$", line):
                print("footer here")
                embed.set_footer(text=line[8:-8])
        # Adding the author name and author's display picture
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        return embed
    except AttributeError:
        return "Something went wrong"

# Checking the link is image and validating it with requests module
def is_url_image(image):
    #checking content type with below options
    image_formats = ["image/png", "image/jpeg", "image/gif", "image/jpg"]
    try:
        request = requests.head(image)
        if request.headers["content-type"] in image_formats:
            return True
        return False
    except:
        return False