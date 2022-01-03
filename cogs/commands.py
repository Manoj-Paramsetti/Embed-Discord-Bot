# Created by Manoj Paramsetti

import discord
from discord import message
from discord.ext import commands

from embed_maker.help import color_help, normal_help, code_help
from embed_maker import converter

class commander(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command("ping")
    async def ping(self, ctx, *, arg=""):
        await ctx.channel.send("Hloo watt?")
    
    @commands.command("embed")
    async def embed(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.teal))
        
    @commands.command("embed-announce")
    async def embed_announce(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send("@everyone",embed=converter.embed(arg, ctx, discord.Color.dark_magenta))
    
    
    @commands.command("embed-code-announce")
    async def embed_announce_code(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send("@everyone",embed=converter.embedCode(arg, ctx, discord.Color.teal))
    
    @commands.command("embed-code")
    async def embed_code(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embedCode(arg, ctx, discord.Color.red))
    
    @commands.command("embed-code-use")
    async def embed_code_use(self, ctx, arg1, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embedCodeUse(arg, arg1, ctx, discord.Color.red))
        
    @commands.command("embed-red")
    async def embed_red(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.red))
    
    @commands.command("embed-clear")
    @commands.bot_has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 1):
        perms= ctx.message.author.permissions_in(ctx.message.channel)
        if (getattr(perms, "manage_messages")):
            await ctx.channel.purge(limit=amount+1)
            embed=discord.Embed(description = f"I deleted {amount} message(s)", color = discord.Color.red())
            await ctx.channel.send(embed=embed)
        else:
            embed=discord.Embed(description = f"You are not having **manage messages** permission in this channel", color = discord.Color.red())
            await ctx.channel.send(embed=embed)
    
    @commands.command("spam-embed")
    async def spam_embed(self, ctx, amount = 1, *, text=""):
        for i in range(0, amount):      
            embed=discord.Embed(description = f"{text}", color = discord.Color.red())
            await ctx.channel.send(embed=embed)

    @commands.command("spam")
    async def spam(self, ctx, amount = 1, *, text=""):
        for i in range(0, amount):      
            await ctx.channel.send(text)

    @commands.command("cal")
    async def calculate(self, ctx, *, text=""):
        a = {'1','2','3','4','5','6','7','8','9','0','*','/','+','-', '(', ')'}
        findchar = set(text)-set(a)
        try:
            message = eval(text)
        except:
            message = 'I can\'t calculate that'
        if(len(findchar)==0):
            await ctx.channel.send(message)
            pass
        else:
            await ctx.channel.send('What are you trying to do actually?')

    @commands.command("embed-blue")
    async def embed_blue(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.blue))

    @commands.command("embed-dark-gold")
    async def embed_dark_gold(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_blue))
    
    @commands.command("embed-dark-green")
    async def embed_dark_green(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_green))
    
    @commands.command("embed-dark-gray")
    async def embed_dark_gray(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_gray))
    
    @commands.command("embed-dark-magenta")
    async def embed_dark_magenta(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_magenta))
    
    @commands.command("embed-dark-orange")
    async def embed_dark_orange(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_orange))
    
    @commands.command("embed-dark-purple")
    async def embed_dark_purple(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_purple))
    
    @commands.command("embed-dark-teal")
    async def embed_dark_teal(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_teal))
    
    @commands.command("embed-darker-grey")
    async def embed_darker_gray(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.darker_grey))
    
    @commands.command("embed-gold")
    async def embed_gold(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.gold))
    
    @commands.command("embed-green")
    async def embed_green(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.green))
    
    @commands.command("embed-light-grey")
    async def embed_light_grey(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.light_grey))
    
    @commands.command("embed-magenta")
    async def embed_magenta(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.magenta))

    @commands.command("embed-orange")
    async def embed_orange(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.orange))
    
    @commands.command("embed-purple")
    async def embed_purple(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.purple))
    
    @commands.command("embed-teal")
    async def embed_teal(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.teal))
    
    @commands.command("profile")
    async def profile(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.profile(ctx, discord.Color.teal))
    
    @commands.command("help")
    async def help(self, ctx, *arg):
        # Here we are just checking whether the argument is passed with command
        if arg == ():
            await ctx.channel.send(embed=normal_help())
        # Here we are sending help for embed colors
        elif arg[0] == "color":
            await ctx.channel.send(embed=color_help())
        elif arg[0] == "syntax":
            await ctx.channel.send(embed=color_help())
        elif arg[0] == "code":
            await ctx.channel.send(embed=code_help())

def setup(bot):
    # pushing cogs to main runner
    bot.add_cog(commander(bot))
