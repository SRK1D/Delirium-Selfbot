import settings
import os

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def nwordCommand(event):
    """Responds with a eeeeaa

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    bot.editMessage(channelID, messageID, "Why u used the ;nword command?\nHere it is: nig||ht||")
    
settings.commands[fileName] = nwordCommand
settings.commandsInfo[fileName] = ";nword <no settings> - big secret"