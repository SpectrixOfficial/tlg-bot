import discord
import asyncio
import random
from discord.ext import commands
bot = commands.Bot(command_prefix='!!',
                   description='A bot that greets the user back.')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="TLG-Bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="TheEntertainmentLord")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?client_id=438663807993118730&scope=bot&permissions=0")
    embed.add_field(name="Language", value="Python")
    embed.add_field(name="Support", value="https://discord.gg/ZP2VGDd")
    embed.add_field(name="Members I can see", value=f"len(bot.get_all_members)")
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="TLG-Bot", description="A completely rewritten version of TLG-bot. List of commands are:", color=0xeee657)

    embed.add_field(name="!!add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="!!multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="!!divide X Y", value="Gives the division of **X** and **Y**", inline=False)
    embed.add_field(name="!!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="!!cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="!!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="!!help", value="Gives this message", inline=False)
    embed.add_field(name="!!ping", value="Pings the bot and records it in seconds", inline=False)
    embed.add_field(name="!!argsct", value="Counts how many arguments you used", inline=False)
    embed.add_field(name="!!slap <reason>", value="Slap a random user!", inline=True) 
    await ctx.send(embed=embed)
@bot.command()
async def ping(ctx):
    '''
    Ping the bot
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
@bot.command()
async def argsct(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
@bot.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because **{2}**'.format(ctx, to_slap, argument)

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)
@bot.command
async def math(ctx): #gotta get this working somehow
    async def add(ctx, a: int, b: int):
        await ctx.send(a + b)
    async def subtract(ctx, a: int, b: int):
        await ctx.send(a - b)
    async def multiply(ctx, a: int, b: int):
        await ctx.send(a * b)
    async def divide(ctx, a: int, b: int):
        await ctx.send(a / b)
bot.run(token)
