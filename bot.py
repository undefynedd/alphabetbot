# videos if they start with letters
# numbers if start with letters
# 

import json             # dictionary -----

import discord          # discord    -----

import urllib.request   # youtube    -----
from urllib.parse import parse_qs, urlparse
import json
import urllib
import pprint

with open('letters.json', encoding="utf-8") as file:
    letters = json.load(file)
    print("Loaded letters.json!")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
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
                    url = "https://www.youtube.com/oembed"   # what does this do
                    query_string = urllib.parse.urlencode(params)   # this gets the query string (id)
                    url = url + "?" + query_string   # this makes it url

                    with urllib.request.urlopen(url) as response:   # this whole thing gets the data from the yt video
                        response_text = response.read()
                        data = json.loads(response_text.decode())
                        title = data['title']
                        print(f"The title was {title}.")
                        
                        for i in letters[message.channel.name]:
                        
                            if title.lower().startswith(i):
                                print(f"The video started with {i}, so it's all good.")
                                good = 1
                                return
                
                except:
                    print("I don't think it was a youtube video. :sadge: I give up")
                    good = 0
                    
            for i in letters[message.channel.name]:
            
                if message.content.lower().strip("*_`~").startswith(i):
                    print("Success!")
                    good = 1
                    return
                        
            if good == 0:
                print(f"deleted{message.content}!")
                await message.delete()
                await message.channel.send(f"<@{message.author.id}> no", delete_after = 5)
                
        elif message.content.startswith("!"):
            if message.content.lower().strip("!").startswith("ping"):
                ping = round(client.latency * 1000)
                await message.channel.send(f"Pong! `{ping}ms`")

client = MyClient()
client.run("token")