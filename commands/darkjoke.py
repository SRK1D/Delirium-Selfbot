import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def darkJokeCommand(event):
    """Sends a random dark joke cause again, funni

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    joke = json.loads(requests.get("https://v2.jokeapi.dev/joke/Dark").content.decode())
    
    if joke["type"] == "single":
        bot.editMessage(channelID, messageID, f"{joke['joke']}")
    else:
        bot.editMessage(channelID, messageID, f"{joke['setup']}\n\n||{joke['delivery']}||")
    
    # bot.editMessage(channelID, messageID, f"{joke['setup']}\n\n||{joke['punchline']}||")
    
settings.commands[fileName] = darkJokeCommand
settings.commandsInfo[fileName] = ";darkjoke <no settings> - [SENSITIVE] Gives a random darkjoke"