import discord
from discord import app_commands
from datetime import datetime
import pytz
import os

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyBot()

@client.tree.command(name="oggiclemmy", description="Oggi è il giorno di Clemmy?")
async def oggiclemmy(interaction: discord.Interaction):
    tz = pytz.timezone('Europe/Rome')
    oggi = datetime.now(tz).weekday()
    giorni_si = [0, 3, 5] # 0=Lun, 3=Gio, 5=Sab
    risposta = "Sì" if oggi in giorni_si else "No"
    await interaction.response.send_message(risposta)

token = os.getenv("DISCORD_TOKEN")
client.run(token)
