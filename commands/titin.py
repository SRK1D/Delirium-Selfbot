import settings
import os
import time

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def titinCommand(event):
    """Sends the full titin name in chat because it is indeed funny AF

    Args:
        event (response event): the event that calls this function
    """
    
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.deleteMessage(channelID, messageID)
    
    titinName = open("ressources/titin_name.txt", "r").read()
    splitTitinName = [titinName[i : i + 2000] for i  in range(0, len(titinName), 2000)]
    settings.log("Titin", "Finished processing the titin protein name")
    for splitted in splitTitinName:
        bot.sendMessage(channelID, splitted)
        time.sleep(2)
    
settings.commands[fileName] = titinCommand
settings.commandsInfo[fileName] = ";titin <no settings> - gives the whole 189k letters word, separated in message of 2k characters"