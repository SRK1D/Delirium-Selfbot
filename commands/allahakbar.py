import settings
import os
import time

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def allahakbarCommand(event):
    """Detonates

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    bot.editMessage(channelID, messageID, "Detonating in...")
    
    
    for i in range(5):
        time.sleep(1)
        bot.editMessage(channelID, messageID, "Detonating in... " + str(5 - i))
        
    time.sleep(1)
    bot.editMessage(channelID, messageID, "https://i.giphy.com/media/XUFPGrX5Zis6Y/giphy.webp")
    
settings.commands[fileName] = allahakbarCommand
settings.commandsInfo[fileName] = ";allahakbar <no settings> - Does funni explosion"