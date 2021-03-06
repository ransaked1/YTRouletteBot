import requests
import os
import discord
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from stayup import keep_alive

keep_alive()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!ythelp'))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!ytroll':
        result = None
        while result is None:
            try:
                url = "https://random-ize.com/random-youtube"
                html_text = requests.get(url, headers=headers).text
                soup = BeautifulSoup(html_text, 'html.parser')

                url2 = soup.find(id='Container').find('iframe').attrs['src']
                html_text = requests.get(url2, headers=headers).text
                soup = BeautifulSoup(html_text, 'html.parser')

                print(url2)

                yt_url = soup.find('a').attrs['href']
                print(yt_url)
                await message.channel.send(yt_url)
                break
            except:
                pass

    if message.content == "!ythelp":
        await message.channel.send(
            "Commands available:\n!ytroll - spit out a random YouTube video"
        )

client.run(TOKEN)
