# This example requires the 'message_content' intent.

import discord, random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("&gay"):
        percent = random.randrange(1, 101)
        if percent == 50:
            await message.reply("You are bisexual!", mention_author=True)
        elif percent == 101:
            await message.reply("You are ULTRA-GAY! (101%)", mention_author=True)
        else:
            await message.reply(f"You are {str(percent)}% gay!")

client.run('MTUxODA1NTAwMDA1ODg4ODM5MQ.G_9sfg.L9CRtqtAe-OKkEZUr6WcGQZUeN2p5f377b-b4I')
