import settings
import os
import ressources.utils.redditParser as rP


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def boobCommand(event):
    """Sends a bub image from r/boobs on deddit

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.editMessage(channelID, messageID, "Searching...")
    
    boobSub = rP.subreddit("r/boobs")
    
    boobImage = boobSub.getRandomImage(headers)
    
    bot.editMessage(channelID, messageID, boobImage)
    
    
    
    
settings.commands[fileName] = boobCommand
settings.commandsInfo[fileName] = ";boob <no settings> - [SEMI-NSFW] gives a random result of boob picture from reddit"