import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def dogCommand(event):
    """Sends a random dog gif/image

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.editMessage(channelID, messageID, "Dog image incoming...:")
    getImage = requests.get("https://api.thedogapi.com/v1/images/search", headers={
        "x-api-key": "DEMO_API_KEY"
    }).content.decode()

    open("ressources/funni.gif", "wb").write(requests.get(json.loads(getImage)[0]["url"]).content)
    
    bot.sendFile(channelID, "ressources/funni.gif")
    
    os.remove("ressources/funni.gif")
    
    
    
settings.commands[fileName] = dogCommand
settings.commandsInfo[fileName] = ";dog <no settings> - generates a dog gif"