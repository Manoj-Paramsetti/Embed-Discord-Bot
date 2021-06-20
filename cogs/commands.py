# Created by Manoj Paramsetti

import discord
from discord.ext import commands
from embed_maker import converter

class commander(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command("embed")
    async def embed(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.red()))
    
    @commands.command("embed-red")
    async def embed_red(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.red()))
    
    @commands.command("embed-blue")
    async def embed_blue(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.blue()))
    
    @commands.command("embed-dark-gold")
    async def embed_dark_gold(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.dark_blue()))
    
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

    @commands.command("embed-mro")
    async def embed_mro(self, ctx, *, arg=""):
        await ctx.message.delete()
        await ctx.channel.send(embed=converter.embed(arg, ctx, discord.Color.mro))
    
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
    
    @commands.command("help")
    async def help(self, ctx, *arg):
        # Here we are just checking whether the argument is passed with command
        if arg == ():
            await ctx.channel.send("Sorry, It is under work. so, this bot will not show any help")
        # Here we are sending help for embed colors
        elif arg[0] == "color":
            await ctx.channel.send("Here, I'll show all the embed commands with colour")


def setup(bot):
    # pushing cogs to main runner
    bot.add_cog(commander(bot))