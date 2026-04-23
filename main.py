import discord
from discord import app_commands
from datetime import datetime
import pytz
import os
from flask import Flask
from threading import Thread

--- SEZIONE WEB SERVER PER RENDER ---,
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    # Render usa la porta 10000 di default
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run_web)
    t.start()
-------------------------------------,
class MyBot(discord.Client):
    def init(self):
        intents = discord.Intents.default()
        super().init(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyBot()

@client.tree.command(name="oggiclemmy", description="Oggi è il giorno di Clemmy?")
async def oggiclemmy(interaction: discord.Interaction):
    tz = pytz.timezone('Europe/Rome')
    oggi = datetime.now(tz).weekday()
    giorni_si = [0, 3, 5]
    risposta = "Sì, è casa GOGOGO" if oggi in giorni_si else "No, oggi si lavora e si fattura"
    await interaction.response.send_message(risposta)

if name == "main":
    # Avvia il server web in un thread separato
    keep_alive()

    token = os.getenv("DISCORD_TOKEN")
    client.run(token)
