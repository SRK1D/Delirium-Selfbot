import settings
import os
import ressources.utils.redditParser as rP

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot
femboyPath = "ressources/femboys/"

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def femboyCommand(event):
    """Sends a femboy image from r/femboy on deddit

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.editMessage(channelID, messageID, "Searching...")
    
    femboySub = rP.subreddit("r/traps")
    
    femboyImage = femboySub.getRandomImage(headers)
    
    bot.editMessage(channelID, messageID, femboyImage)
    
    
    
settings.commands[fileName] = femboyCommand
settings.commandsInfo[fileName] = ";traps <no settings> - [NSFW] Gives you a random trap picture from reddoot"