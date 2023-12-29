import settings
import os
import ressources.utils.redditParser as rP


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def thighCommand(event):
    """Sends a thigh image from r/thighzone on deddit

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.editMessage(channelID, messageID, "Searching...")
    
    thighSub = rP.subreddit("r/thighzone")
    
    thighImage = thighSub.getRandomImage(headers)
    
    bot.editMessage(channelID, messageID, thighImage)
    
    
    
    
settings.commands[fileName] = thighCommand
settings.commandsInfo[fileName] = ";thigh <no settings> - [SEMI-NSFW] gives a random result of thigh picture from reddit"