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

version = "1.1.0"

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
        good = 0
        print("This was an alphabet channel.")
        
        if len(message.content) == 0:
            good = 1
            print("The message was empty, so I let it pass.")
        
        elif "youtu" in message.content:
            
            print("I think this is a youtube video.")
            
            if "youtu.be" in message.content:
                if "https://" in message.content:
                    print("It was an https:// link.")
                    id = message.content[17:].strip("/")
                    
                elif "http://" in message.content:
                    print("It was an http:// link.")
                    id = message.content[16:].strip("/")
                    
            else:
                id = parse_qs(urlparse(message.content).query).get('v')[0]   # the id comes out as a one value list for some reason
            
            print(id)
            
            try:
                params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % id}   # yeah i found this on stackoverflow
                url = "https://www.youtube.com/oembed"   # oh! this is the start of the url
                query_string = urllib.parse.urlencode(params)   # this gets the query string (id)
                url = url + "?" + query_string   # this adds the id onto the url!

                with urllib.request.urlopen(url) as response:   # this whole thing gets the data from the yt video
                    response_text = response.read()   # i think this reads the json and puts it in var
                    data = json.loads(response_text.decode())   # oh and this loads it into json
                    title = data['title']    # and this gets the title
                    print(f"The title was {title}.")   # useless debug code shut up
                    
                    for i in letters[message.channel.name]:    # i should make this a function
                    
                        if title.lower().startswith(i):
                            print(f"The video started with {i}, so it's all good.")
                            good = 1
                            return
            
            except:
                print("I don't think it was a youtube video. I give up")
                good = 0
                
        for i in letters[message.channel.name]:
        
            if message.content.lower().strip("*_`~|").startswith(i):
                print("Success!")
                good = 1
                return
            
            elif unidecode(message.content.lower().strip("*_`~|")).startswith(i):
                print("Success!")
                good = 1
                return
                    
        if good == 0:
            print(f"I deleted {message.content}!")
            await message.delete()
            await message.channel.send(f"<@{message.author.id}> no", delete_after = 5)
            
    elif message.content.startswith("!"):
        if message.content.lower().strip("!").startswith("ping"):
            ping = round(client.latency * 1000)
            await message.channel.send(f"Pong! `{ping}ms`")
            
        elif message.content.lower().strip("!").startswith("pong"):
            await message.channel.send(f"Ping! <@{message.author.id}>")
                
        elif message.content.lower().strip("!").startswith("rl"):
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            letter = letters[random.randrange(26)]
            await message.channel.send(f"Your letter is `{letter}`!")
    
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
