import settings
import os
import time

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def dickStrokeCommand(event):
    """Stroken my dick

    Args:
        event (response event): the event that calls this function
    """
    
    filler = "="
    hand = ":fist:"
    top = "D"
    start = "8"
    iteration = 3
    newIteration = 1
    current = 0
    multiplier = 1
    max_filler = 8
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    while newIteration <= iteration:
        if current > (max_filler - 1):
            multiplier = -1
        elif current < 1:
            multiplier = 1
            newIteration += 1
            
            
        current += multiplier
        
        text = start + filler * current + hand + (filler * (max_filler - current)) + top
        bot.editMessage(channelID, messageID, text)
        time.sleep(0.5)
    
    bot.editMessage(channelID, messageID, text + ":sweat_drops:")
settings.commands[fileName] = dickStrokeCommand
settings.commandsInfo[fileName] = ";dickstroke <no settings> - Strokes yo dick"