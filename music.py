from discord.ext import commands
import discord
import youtube_dl
import os

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url: str):
        channel = ctx.author.voice.channel
        if channel is not None:
            voice = await channel.connect()

            # Use youtube-dl to download and play the audio from the YouTube video
            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
                "keep_original_extension": True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([url])
                    info = ydl.extract_info(url, download=False)
                    audio_filename = ydl.prepare_filename(info)
                    voice.play(discord.FFmpegPCMAudio(audio_filename))
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.5
                except Exception as e:
                    print(f'Error: {e}')