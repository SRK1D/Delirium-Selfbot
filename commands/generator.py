import settings
import os
from random import choice


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def generatorCommand(event):
    """Get the DNS of a website :pOg:

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    messageContent = messageInfo["content"]
    
    messageSplits = messageContent.split(" ")
    if len(messageSplits) == 3 and messageSplits[2].isnumeric():
        for char in messageSplits[1]:
            if char != "X" and char != "O":
                bot.deleteMessage(channelID, messageID)
                return
        
        characters = ""
        characters += messageSplits[1][0] != "O" and "abcdefgijklmnopqrstuvwxyz" or ""
        characters += messageSplits[1][1] != "O" and "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ""
        characters += messageSplits[1][2] != "O" and "0123456789" or ""
        characters += messageSplits[1][3] != "O" and "!@#$%^&*()<>?:{}|,./;'[]\\" or ""

        output = ""
        print(characters)
        for i in range(int(messageSplits[2])):
            output += choice([i for i in characters])
        
        bot.editMessage(channelID, messageID, f"Generated output for pattern \"{messageSplits[1]}\": {output}")


settings.commands[fileName] = generatorCommand
settings.commandsInfo[fileName] = ";generator <Lowercase|Uppercase|Numbers|Special <length>  ; ex.: ;generator XOOO 5 since X = true; O = false"