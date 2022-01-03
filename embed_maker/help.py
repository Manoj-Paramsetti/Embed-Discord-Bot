import discord
from discord.colour import Color

def normal_help():
    embed = discord.Embed(title='Basic Help', color= discord.Color.blue() )
    embed.add_field(name="$embed\n`EMBED CODE`", value="Display this message", inline=False)
    embed.add_field(name="$ping", value="For presence testing", inline=False)
    embed.add_field(name="$cal `EXP`", value="A basic calculator", inline=False)
    embed.add_field(name="$profile", value="Displays your profile picture", inline=False)
    embed.add_field(name="$help", value="Display this message", inline=False)
    embed.add_field(name="$help color", value="To get all embed color colors", inline=False)
    embed.add_field(name="$help code", value="Gives another help for embed code", inline=False)
    embed.add_field(name="Help for embed code syntax", value="[Read Here](https://bit.ly/embed_syntax)", inline=False)

    return embed

def color_help():
    embed = discord.Embed(title='Color Help', color= discord.Color.blue() )
    color_dict={"embed":"teal", "embed-red":"red", 
    "embed-blue":"blue", "embed-dark-gold":"dark blue", 
    "embed-dark-green":"dark green", "embed-dark-gray":"dark gray",
    "embed-dark-magenta":"dark magenta", "embed-dark-orange":"dark orange",
    "embed-dark-purple":"dark purple", "embed-dark-teal":"dark teal",
    "embed-darker-grey":"darker grey", "embed-gold":"gold", 
    "embed-green":"green", "embed-light-grey":"light grey", 
    "embed-magenta":"magenta", "embed-orange":"orange", 
    "embed-purple":"purple", "embed-teal":"teal"}
    for i, j in color_dict.items():
        embed.add_field(name="!"+i, value="Embed color: "+j)
    return embed

def code_help():
    embed = discord.Embed(title='Code Help', color= discord.Color.blue() )
    embed.add_field(name="$embed-code", value="""First line after $embed-code is heading 1 and then remaining lines are treated as code
```ps
$embed-code
Heading 1
CODE
CODE
...
```
    """, inline=False)
    
    embed.add_field(name="$embed-code-use LANGUAGE_NAME", value="""Add language name after $embed-code-use. 
The second line is heading 1 and then remaining lines are treated as code
```ps
$embed-code-use REPLACE_LANGUAGE_NAME_HERE
Heading 1
CODE
CODE
...
```
    """, inline=False)
    return embed
