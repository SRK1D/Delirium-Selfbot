import settings
import os
import ressources.utils.redditParser as rP


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def pussyCommand(event):
    """Sends a puss image from r/pussy on deddit

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.editMessage(channelID, messageID, "Searching...")
    
    pussySub = rP.subreddit("r/pussy")
    
    pussyImage = pussySub.getRandomImage(headers)
    
    bot.editMessage(channelID, messageID, pussyImage)
    
    
    
    
settings.commands[fileName] = pussyCommand
settings.commandsInfo[fileName] = ";pussy <no settings> - [SEMI-NSFW] gives a random result of pussy picture from reddit"