# Work with Python 3.6
import random
import asyncio
import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

TOKEN = "NDg5MjgwMzk4MDAyNjE4MzY4.DnpJOA.raZMwvSvTHCr5BiB0PB-mN310YA"

client = commands.Bot(command_prefix="!")  #when the bot should read chat input


@client.event
async def on_ready():
    print("Logged in as:")         #terminal information
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=Game(name="King's Raid"))  # bot is playing a game


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!hello"):  #says hello to the person that says !hello
        await client.send_message(message.channel,
                                  "Hello {0.author.mention}!".format(message))
    elif "rude" in message.content:      #calls people who say rude....rude
        await client.send_message(message.channel,
                                  "NO! {0.author.mention} is rude, don\'t listen to them!".format(message))
    await client.process_commands(message)


@client.event
async def on_message_delete(message):  #chat log of messages that got deleted
    author = message.author
    content = message.content
    channel = message.channel
    if content.startswith(".prune"):
        return
    else:
        await client.send_message(channel, '{}\'s message, "{}" was deleted :frowning:'.format(author, content))


@client.command()
async def echo(*args):  #repeats what is said
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)


@client.command(pass_context=True)    #welcomes new users
async def welcome(ctx):
    await client.say("Welcome to the server, {}".format(ctx.message.server.name))


@client.command()
async def spam(times: int):   # spams a custom server emote x amount of times,x < 26 to prevent slow down
    for x in client.get_all_emojis():
        if x.id == "347265536448659467":
            break
        pass
    if times > 26:
        await client.say("Thats too many times....no")
        return
    for i in range(times):
        await asyncio.sleep(1)
        await client.say(x)


client.run(TOKEN)
