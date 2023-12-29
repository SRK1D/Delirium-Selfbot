import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def catFactCommand(event):
    """Sends a cat fact (YAY)

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    catfact = json.loads(requests.get("https://catfact.ninja/fact").content.decode())
    
    bot.editMessage(channelID, messageID, catfact["fact"])
    
    
    
settings.commands[fileName] = catFactCommand
settings.commandsInfo[fileName] = ";catfact <no settings> - Generates a random and funni cat fact"