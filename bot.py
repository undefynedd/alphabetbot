import discord

letters = {
    "a": ["a", "🅰️", 🇦]
}


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(message.content)
        
        if message.content.lower().startswith(message.channel.name):
            await message.channel.send("good")
        else:
            await message.channel.send("bad")

client = MyClient()
client.run("token")