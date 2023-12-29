import settings
import os
import ressources.utils.rule34Parser as r34P

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def pointersCommand(event):
    """It gets image from R34

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    messageContent = messageInfo["content"].split(" ")
    if (len(messageContent) >= 2):
        messagesTags = messageContent[1:]
        fTags = r34P.tagParser(messagesTags)
        bot.editMessage(channelID, messageID, r34P.r34(fTags).getRandomImage())
    else:
        bot.deleteMessage(channelID, messageID)
    
settings.commands[fileName] = pointersCommand
settings.commandsInfo[fileName] = ";r34 <tags> <tags> ... - [NSFW] Gets image from da beautiful rule34.xxx"