import settings
import os
import time
import random

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def hackerCommand(event):
    """Totally 100% hacks ip no lies

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    messageContent = messageInfo["content"].split(" ")
    channelID = str(messageInfo["channel_id"])
    if len(messageContent) == 2 and messageContent[1].isnumeric():
        bot.editMessage(channelID, messageID, "[#--------] Finding users location...")
        time.sleep(random.randint(3, 5))
        bot.editMessage(channelID, messageID, "[###------] Contacting nearest FBI agent...")    
        time.sleep(random.randint(3, 5))
        bot.editMessage(channelID, messageID, "[####-----] Error... Could not find a breached database with IP in it... Skipping step")
        time.sleep(random.randint(3, 5))
        bot.editMessage(channelID, messageID, "[######---] Pinging target for a callback...")
        time.sleep(random.randint(3, 5))
        bot.editMessage(channelID, messageID, "[#######--] Bruteforcing targets computer using port 22 (SSH)")
        time.sleep(random.randint(3, 5))
        bot.editMessage(channelID, messageID, f"[$$$$$$$$$] Target IP found: {str(random.randint(100, 255))}.{str(random.randint(100, 255))}.{str(random.randint(100, 255))}.{str(random.randint(100, 255))} <@{messageContent[1]}>")

settings.commands[fileName] = hackerCommand
settings.commandsInfo[fileName] = ";hacker <user id> - Fakes a hack against the user id"