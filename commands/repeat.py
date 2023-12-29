import settings
import os
import time

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def repeatCommand(event):
    """Repeat message x times
    1 - how many times to repeat
    2 - message

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    
    channelID = str(messageInfo["channel_id"])
    bot.deleteMessage(channelID, messageInfo["id"])
    
    # Gets how many messages to delete :yay:
    messageContent = messageInfo["content"].split(" ")
    if len(messageContent) >= 4 and messageContent[1].replace(".", "").isnumeric() and messageContent[2].isnumeric():
        
        message = " ".join(messageContent[3:])
        settings.log("Repeat", f"Called {message} x{messageContent[2]}")
        nmbOfMessages = int(messageContent[2])
        sleepTime = float(messageContent[1])
        for w in range(nmbOfMessages):
            time.sleep(sleepTime)
            bot.sendMessage(channelID, message)
    
settings.commands[fileName] = repeatCommand
settings.commandsInfo[fileName] = ";repeat <seconds of sleep> <amount of messages> <message> - repeats the message x amount of times with x amount of delay"