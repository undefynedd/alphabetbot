### VARIABLES ###                                         ---

TOKEN = ""   # token
autorole = 900561278542696468                             # id of automatic role
welcomechannel = 901213480256962610                       # id of welcome channel

### IMPORTS   ###                                         ---

import json                                               # for dictionary

import discord                                            # for bot functionality
from discord.ext import commands
from discord.utils import get

import urllib                                             # for youtube links
import urllib.request
from urllib.parse import parse_qs, urlparse
import pprint

import random                                             # for random

### INIT      ###                                         ---

version = "1.2.0"

intents=intents=discord.Intents.all()                     # makes bots work
client = commands.Bot(command_prefix="!", intents=intents)

with open('letters.json', encoding="utf-8") as file:      # letters.json to dict
    letters = json.load(file)
    print("Loaded letters.json!")

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"{message.author} sent {message.content} in #{message.channel.name}!")
    
    if len(message.channel.name) == 1:
        good = check(message, letters)

        if good == 0:
            print(f"I deleted {message.content}!")
            await message.delete()
            await message.channel.send(f"<@{message.author.id}> no", delete_after = 5)

    if message.content.startswith("!"):
        if message.content.lower().strip("!").startswith("ping"):
            ping = round(client.latency * 1000)
            await message.channel.send(f"Pong! `{ping}ms`")
            
        elif message.content.lower().strip("!").startswith("pong"):
            await message.channel.send(f"Ping! <@{message.author.id}>")
                
        elif message.content.lower().strip("!").startswith("rl"):
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            letter = alphabet[random.randrange(26)]
            await message.channel.send(f"Your letter is `{letter}`!")
    
@client.event
async def on_message_edit(before, after):
    print(f"{after.author} edited {before.content} to {after.content}!")
    
    if len(after.channel.name) == 1:
        good = check(after, letters)
        
        if good == 0:
            print(f"I deleted {after.content}!")
            await after.delete()
            await after.channel.send(f"<@{after.author.id}> lol imagine editing", delete_after = 5)


@client.event
async def on_member_join(member):
    channel = client.get_channel(welcomechannel)
    await channel.send(f"Welcome! <@{member.id}> just learnt the alphabet!")
    print(f"{member} joined")
    
    role = get(member.guild.roles, id = autorole)
    await member.add_roles(role)
    print(f"I added role {role} to {member}!")
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel(welcomechannel)
    await channel.send(f"RIP! <@{member.id}> forgot their ABC's.")
    print(f"RIP {member}, they forgot their ABC's.")

client.run(TOKEN)