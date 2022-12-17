import discord
import os
import youtube_dl
from music import Music
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

# Load the Discord token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.add_cog(Music(bot))


async def on_message(self, message):
        # Only respond to messages from other users (not the bot itself)
        if message.author != self.user:
            # Print the message to the console
            print(message.content)


# Create an instance of the bot and the Music cog
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
bot.add_listener(on_ready)
bot.run(TOKEN)

