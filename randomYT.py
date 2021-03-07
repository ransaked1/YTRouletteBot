import requests
import os
import discord
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from stayup import keep_alive

# Starting a server to keep the repl.it VM on
keep_alive()

# Adding a header identifier to the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

# Getting the Discord Token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Loading the client
client = discord.Client()

# Setting up the tag
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!ythelp'))
    print(f'{client.user} has connected to Discord!')

# Function to watch the messages in Discord chat
@client.event
async def on_message(message):
    # Check that it's a valid user
    if message.author == client.user:
        return

    # !ytroll command
    if message.content == '!ytroll':
        result = None

        # Request YouTube videos until a valid one is loaded without errors
        while result is None:
            try:
                # Request a video and parse the first link from the HTML
                url = "https://random-ize.com/random-youtube"
                html_text = requests.get(url, headers=headers).text
                soup = BeautifulSoup(html_text, 'html.parser')
                url2 = soup.find(id='Container').find('iframe').attrs['src']
                
                # Follow the link and parse the clean YT video link
                html_text = requests.get(url2, headers=headers).text
                soup = BeautifulSoup(html_text, 'html.parser')
                yt_url = soup.find('a').attrs['href']

                print(url2) # Debug print
                print(yt_url) #Debug print
                
                await message.channel.send(yt_url) # Output link to chat and stop
                break
            except:
                pass

    # !ythelp command
    if message.content == "!ythelp":
        await message.channel.send(
            "Commands available:\n!ytroll - spit out a random YouTube video"
        )

client.run(TOKEN) # Run the bot client
