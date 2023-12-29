import settings
import os
import re
import requests
import json


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def ipLookupCommand(event):
    """Gets information from an IP address

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    messageContent = messageInfo["content"]
    
    ipAddress = re.findall(r"((?:(?:25[0-5]|(?:2[0-4]|1\d|[1-9]|)\d)\.?\b){4})", messageContent)
    
    if ipAddress != None and len(ipAddress) > 0:
        bot.editMessage(channelID, messageID, "Searching...")
        response = json.loads(requests.get(f"http://ip-api.com/json/{ipAddress[0]}").content.decode())
        if response["status"] == "success":
            bot.editMessage(channelID, messageID, f"""{response['query']}:```
Country: {response['country']}
Country Code: {response['countryCode']}
Region: {response['region']}
Region Name: {response['regionName']}
City: {response['city']}
Latitude: {response['lat']}
Longitude: {response['lon']}
ISP: {response['isp']}
ORG: {response['org']}
AS: {response['as']}```""")
        else:
            bot.editMessage(channelID, messageID, f"{response['query']}:```Error: {response['message']}```")
    else:
        print(ipAddress)
        bot.editMessage(channelID, messageID, "Invalid IP address (Must be IPv4)")

settings.commands[fileName] = ipLookupCommand
settings.commandsInfo[fileName] = ";iplookup <ip address> - Will find details of an IP"