import settings
import os
import math


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def humanToDogYearsCommand(event):
    """Converts human to dog years

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    messageContent = messageInfo["content"].split(" ")

    if len(messageContent) == 2 and messageContent[1].replace(".", "").isnumeric():
        try:
            outp = 16 * math.log(float(messageContent[1])) + 31
            bot.editMessage(channelID, messageID, f"{messageContent[1]} years old = {str(round(outp))} dog years old")
        except:
            bot.deleteMessage(channelID, messageID)
    else:
        bot.deleteMessage(channelID, messageID)


settings.commands[fileName] = humanToDogYearsCommand
settings.commandsInfo[fileName] = ";humantodogyears <human age> - Will return the dog equivalent of the human age mentioned"