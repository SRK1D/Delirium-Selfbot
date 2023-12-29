import settings
import os

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def pingCommand(event):
    """Tests if the bot is alive

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    bot.editMessage(channelID, messageID, "Pong! :ping_pong: ")
    
settings.commands[fileName] = pingCommand
settings.commandsInfo[fileName] = ";ping <no settings> - pong"