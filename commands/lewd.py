import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def lewdCommand(event):
    """Post a lewd picture / video

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    channelID = str(messageInfo["channel_id"])
    lewdImage = json.loads(requests.get("http://api.nekos.fun:8080/api/lewd").content.decode())["image"]
    bot.editMessage(channelID, messageID, lewdImage)
    
settings.commands[fileName] = lewdCommand
settings.commandsInfo[fileName] = ";lewd <no settings> - [NSFW, NOT FILTERED] gives an image that contains lewds"