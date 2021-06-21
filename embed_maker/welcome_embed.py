# Created by Manoj Paramsetti

import discord

def welcome_msg():
    embed=discord.Embed(title = "Hello everyone!", description = "This bot will embed your messsage to make it prettier than normal message", color = discord.Color.teal())
    embed.add_field(name = "Thanks for adding me here!", value = "You can check my help commands to use me", inline =False)
    embed.add_field(name = "Basic", value="Send a message **!help**", inline = True)
    embed.add_field(name = "Help to change embed colour", value="Send a message **!help color**", inline = True)
    embed.add_field(name = "Check the syntax to send the message", value="https://github.com/Manoj-Paramsetti/Embed-Discord-Bot/wiki", inline = True)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/1c/54/f7/1c54f7b06d7723c21afc5035bf88a5ef.png")
    embed.set_image(url="https://media.giphy.com/media/krkrHAEodHgzP72rTI/giphy.gif")
    embed.set_footer(text="Enjoy with embed message :heart: ", icon_url="https://i.pinimg.com/originals/1c/54/f7/1c54f7b06d7723c21afc5035bf88a5ef.png")
    embed.set_author(name="Baby Yoda", icon_url="https://media.giphy.com/media/krkrHAEodHgzP72rTI/giphy.gif")
    return embed
