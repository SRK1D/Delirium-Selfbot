import settings
import os
import requests

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def insultCommand(event):
    """Sends a random insult cause funni

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    insult = requests.get("https://insult.mattbas.org/api/insult").content.decode()
    
    bot.editMessage(channelID, messageID, insult)
    
settings.commands[fileName] = insultCommand
settings.commandsInfo[fileName] = ";insult <no settings> - creates a creative insult to use"