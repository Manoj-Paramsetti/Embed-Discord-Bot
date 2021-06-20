# Created by Manoj Paramsetti

import discord, os
from discord.ext import commands
import dotenv

from embed_maker.welcome_embed import welcome_msg

dotenv.load_dotenv()
client = commands.Bot(command_prefix="!", help_command=None)

# print when bot is live
@client.event
async def on_ready():
    print("Bot is now on ride")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help'))
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(embed=welcome_msg())
            break
# loading commands from cog
client.load_extension('cogs.commands')
# initalizing the bot
client.run(os.getenv('DISCORD_BOT_TOKEN'))
