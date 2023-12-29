import settings
import time
import os
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def ghostCommand(event):
    """Pings <userid> secretly :sus:

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    # Sends a message and delete it after 0.1 seconds (as well as doing some checks for the funni)
    messageContent = messageInfo["content"].split(" ")
    if len(messageContent) == 2 and messageContent[1].isnumeric():
        pingID = json.loads(bot.editMessage(channelID, messageID, f"<@{messageContent[1]}>").content.decode())["id"]
        time.sleep(0.5)
        bot.deleteMessage(channelID, pingID)
    else:
        bot.deleteMessage(channelID, messageInfo["id"])
    
settings.commands[fileName] = ghostCommand
settings.commandsInfo[fileName] = ";ghostping <user id> - ghostpings the user id once"