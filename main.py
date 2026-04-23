import discord
from discord import app_commands
from datetime import datetime
import pytz
import os
from flask import Flask
from threading import Thread

# Configurazione Web Server per Render
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    # Render assegna automaticamente la porta, ma la 10000 è lo standard
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# Configurazione Bot Discord
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
    risposta = "Sì, è casa GOGOGO" if oggi in giorni_si else "No, oggi si lavora e si fattura"
    await interaction.response.send_message(risposta)

if __name__ == "__main__":
    # Avviamo il server Flask in un thread separato prima del bot
    keep_alive()
    
    token = os.getenv("DISCORD_TOKEN")
    if token:
        client.run(token)
    else:
        print("Errore: DISCORD_TOKEN non trovato nelle variabili d'ambiente!")
