import settings
import os
import json
import time

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def purgeCommand(event):
    """Delete x amount of messages

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    
    channelID = str(messageInfo["channel_id"])
    bot.deleteMessage(channelID, messageInfo["id"])
    
    # Gets how many messages to delete :yay:
    messageContent = messageInfo["content"].split(" ")
    if len(messageContent) == 2 and messageContent[1].isnumeric():
        nmbOfMessages = int(messageContent[1])
        if nmbOfMessages < 100:
            settings.log("Purge", f"Deleting {str(nmbOfMessages)} message(s)...")
            
            lastMessages = json.loads(bot.getMessages(channelID, nmbOfMessages).content.decode())
            for idx, message in enumerate(lastMessages):
                if ((idx + 1) % 5 == 0):
                    time.sleep(2)
                bot.deleteMessage(channelID, message["id"])
    
settings.commands[fileName] = purgeCommand
settings.commandsInfo[fileName] = ";purge <amount of message> - it deletes the <amount> messages it has permission to"