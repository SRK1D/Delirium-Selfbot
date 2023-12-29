import settings
import os
import ressources.utils.redditParser as rP


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def loseFaithInHumanityCommand(event):
    """Sends a r/LostFaithInHumanity reddit post

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    bot.editMessage(channelID, messageID, "Searching...")
    
    faithSub = rP.subreddit("r/lostfaithinhumanity")
    
    faithPost = faithSub.getRandomPost(headers)
    
    faithContent = faithSub.getContentFromPost(headers, faithPost)
    
    if faithContent != None:
        bot.editMessage(channelID, messageID, f'```\n{faithContent["Title"]}:\n{faithContent["Description"]}\n\n```\n \- {faithPost}')
    else:
        bot.deleteMessage(channelID, messageID)
    
    
    
    
settings.commands[fileName] = loseFaithInHumanityCommand
settings.commandsInfo[fileName] = ";losefaithinhumanity <no settings> - Sends a reddit post from r/lostfaithinhumanity"