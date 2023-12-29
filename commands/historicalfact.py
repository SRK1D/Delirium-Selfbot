import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def historicalFactCommand(event):
    """Answers questions related to history

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    messageContent = messageInfo["content"].split(" ")
    if len(messageContent) >= 2: # Valid
        messageRelatedToEvent = " ".join(messageContent[1:])
        events = requests.get(f"https://api.api-ninjas.com/v1/historicalevents?text={messageRelatedToEvent}", headers={
            "X-Api-Key": "<PUT YOUR KEY HERE>"
        })
        
        content = []
        for event in json.loads(events.content.decode()):
            content.append(f"Year: {event['year']}, Month: {event['month']}, Day: {event['day']}\n{event['event']}")
            
        bot.editMessage(channelID, messageID, f"Facts about {messageRelatedToEvent}:```\n" + "\n\n".join(content) + "\n```")
    else:
        bot.deleteMessage(channelID, messageID)
        return
        
    
    
    
settings.commands[fileName] = historicalFactCommand
settings.commandsInfo[fileName] = ";historicalfact <event name> - Tries to find the event in history"