# YTRouletteBot
This is a Discord bot written in Python and hosted on a [repl.it VM](https://replit.com/@ransaked1/YTRouletteBot) that is pinged by [UptimeRobot](https://uptimerobot.com/) in 5min intervals. The bot gives a random YouTube video on request. Check out [this article](https://codenoodles.com/lets-build-an-always-on-discord-bot-with-python/) on my blog to learn how it was built and set up.

## Setup
 Use this [invite link](https://discord.com/api/oauth2/authorize?client_id=817498684627353641&permissions=75776&scope=bot) to add it to you Discord server.

## Built With
* [Python-dotenv 0.15.0](https://pypi.org/project/python-dotenv/) - .env storing API keys
* [BeautifulSoup4 4.9.2](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - used for parsing the HTML
* [Discord API 1.0.0](https://discordpy.readthedocs.io/en/latest/api.html) - Discord API used to interact with Discord
* [Flask 1.1.2](https://discordpy.readthedocs.io/en/latest/api.html) - the server used to keep the repl.it VM always on
