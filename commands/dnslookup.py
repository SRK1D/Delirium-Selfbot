import settings
import os
import re
import requests
import json


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def ipLookupCommand(event):
    """Get the DNS of a website :pOg:

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    messageContent = messageInfo["content"]
    
    websiteAddress = re.findall(r"((?:(?!-))(?:xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(?:xn--)?(?:[a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,}))", messageContent)
    
    if websiteAddress != None and len(websiteAddress) > 0:
        bot.editMessage(channelID, messageID, "Searching...")
        events = requests.get(f"https://api.api-ninjas.com/v1/dnslookup?domain={websiteAddress[0]}", headers={
            "X-Api-Key": "<PUT YOUR KEY HERE>"
        })
        
        content = []
        DNS_s = json.loads(events.content.decode())
        for DNS in DNS_s:
            if DNS["record_type"] != "SOA":
                content.append(f"Record Type: {DNS['record_type']}\nValue: {DNS['value']}\n\n")
            else:
                content.append(f"Record Type: {DNS['record_type']}\nMName: {DNS['mname']}\nRName: {DNS['rname']}\n\n")
                
        bot.editMessage(channelID, messageID, f"{websiteAddress[0]}:```" + "".join(content) + "```")
    else:
        bot.editMessage(channelID, messageID, "Invalid website")

settings.commands[fileName] = ipLookupCommand
settings.commandsInfo[fileName] = ";dnslookup <website address> - Will find a list of DNS of a website"