import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def cumCommand(event):
    """Post a cum picture / video

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    channelID = str(messageInfo["channel_id"])
    cumImage = json.loads(requests.get("http://api.nekos.fun:8080/api/cum").content.decode())["image"]
    bot.editMessage(channelID, messageID, cumImage)
    
settings.commands[fileName] = cumCommand
settings.commandsInfo[fileName] = ";cum <no settings> - [NSFW] generates an image which has cum in it"