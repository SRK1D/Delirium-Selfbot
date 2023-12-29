import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def nekoCommand(event):
    """Post a neko picture / video

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    channelID = str(messageInfo["channel_id"])
    cumImage = json.loads(requests.get("http://api.nekos.fun:8080/api/neko").content.decode())["image"]
    bot.editMessage(channelID, messageID, cumImage)
    
settings.commands[fileName] = nekoCommand
settings.commandsInfo[fileName] = ";neko <no settings> - [NSFW, NOT FILTERED] gives an image of a neko, can be SFW or NSFW"