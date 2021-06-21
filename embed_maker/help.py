import discord
from discord.colour import Color
def normal_help():
    embed = discord.Embed(title='Basic Help', color= discord.Color.blue() )
    embed.add_field(name="Color help", value="Just type **!help color**")
    embed.add_field(name="help for syntax", value="check [syntax](https://bit.ly/embed_syntax)")
    return embed
def color_help():
    embed = discord.Embed(title='Color Help', color= discord.Color.blue() )
    color_dict={"embed":"teal (default color)", "embed-red":"red", 
    "embed-blue":"blue", "embed-dark-gold":"dark blue", 
    "embed-dark-green":"dark green", "embed-dark-gray":"dark gray",
    "embed-dark-magenta":"dark magenta", "embed-dark-orange":"dark orange",
    "embed-dark-purple":"dark purple", "embed-dark-teal":"dark teal",
    "embed-darker-grey":"darker grey", "embed-gold":"gold", 
    "embed-green":"green", "embed-light-grey":"light grey", 
    "embed-magenta":"magenta", "embed-orange":"orange", 
    "embed-purple":"purple", "embed-teal":"teal"}
    for i, j in color_dict.items():
        embed.add_field(name="!"+i, value="color it gives - "+j)
    return embed