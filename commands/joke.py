import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def jokeCommand(event):
    """Sends a random joke cause again, funni

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    joke = json.loads(requests.get("https://official-joke-api.appspot.com/random_joke").content.decode())
    
    bot.editMessage(channelID, messageID, f"{joke['setup']}\n\n||{joke['punchline']}||")
    
settings.commands[fileName] = jokeCommand
settings.commandsInfo[fileName] = ";joke <no settings> - gives a dad joke"