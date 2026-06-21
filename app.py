# This example requires the 'message_content' intent.

import discord, random
from dotenv import load_dotenv
from os import getenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="Rating your queerness"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("&oldgay"):
        percent = random.randrange(0, 102)
        if percent == 50:
            await message.reply("You are bisexual!", mention_author=True)
        elif percent == 101:
            await message.reply(f"You are ULTRA-GAY! (101%)", mention_author=True)
        elif percent == 0:
            await message.reply("You are scary (0% gay)", mention_author=True)
        else:
            await message.reply(f"You are {str(percent)}% gay! 🏳️‍🌈")

    if message.content.startswith("&gay"):
        percent = random.randrange(0, 110)
        if percent == 50:
            await message.reply("You are bisexual!", mention_author=True)
        elif percent > 100:
            await message.reply(f"You are ULTRA-GAY! ({str(percent)}%)", mention_author=True)
        elif percent == 0:
            await message.reply("You are scary (0% gay)", mention_author=True)
        else:
            await message.reply(f"You are {str(percent)}% gay! 🏳️‍🌈")

    if message.content.startswith("&lesbian"):
        percent = random.randrange(0, 110)
        if percent == 50:
            await message.reply("You are bisexual!", mention_author=True)
        elif percent > 100:
            await message.reply(f"You are ULTRA-LESBIAN! ({str(percent)}%)", mention_author=True)
        elif percent == 0:
            await message.reply("You are scary (0% lesbian)", mention_author=True)
        else:
            await message.reply(f"You are {str(percent)}% lesbian! 🏳️‍🌈")

    if message.content.startswith("&trans"):
        percent = random.randrange(0, 110)
        if percent == 50:
            await message.reply("You are genderfluid!", mention_author=True)
        elif percent > 100:
            await message.reply(f"You are ULTRA-TRANS! ({str(percent)}%)", mention_author=True)
        elif percent == 0:
            await message.reply("You are scary (0% trans)", mention_author=True)
        else:
            await message.reply(f"You are {str(percent)}% trans! 🏳️‍⚧️")
    
    if message.content.startswith("&bisexual"):
        await message.reply("You are 50% gay! (what did you think would happen?)")

client.run(getenv("TOKEN"))
