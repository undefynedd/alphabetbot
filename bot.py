# videos if they start with letters
# numbers if start with letters
# 

import discord

letters = {
    'a': ['a', '🅰️', '🇦'],
    'b': ['b', '🅱️', '🇧'],
    'c': ['c', '🇨'],
    'd': ['d', '🇩'],
    'e': ['e', '🇪'],
    'f': ['f', '🇫'],
    'g': ['g', '🇬'],
    'h': ['h', '🇭'],
    'i': ['i', '🇮'],
    'j': ['j', '🇯'],
    'k': ['k', '🇰'],
    'l': ['l', '🇱'],
    'm': ['m', '🇲'],
    'n': ['n', '🇳'],
    'o': ['o', '🅾️', '🇴'],
    'p': ['p', '🇵'],
    'q': ['q', '🇶'],
    'r': ['r', '🇷'],
    's': ['s', '🇸'],
    't': ['t', '🇹'],
    'u': ['u', '🇺'], 
    'v': ['v', '🇻'],
    'w': ['w', '🇼'],
    'x': ['x', '🇽'],
    'y': ['y', '🇾'],
    'z': ['z', '🇿']
}


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(message.content)
        
        if len(message.channel.name) == 1:
            good = 0
            
            for i in letters[message.channel.name]:
            
                if message.content.lower().strip("*_`~").startswith(i):
                    good = 1
                    return
                    
            if good == 0:
                await message.delete()
                await message.channel.send(f"<@{message.author.id}> no", delete_after = 5)

client = MyClient()
client.run("token")