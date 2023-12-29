import settings
import os
import time

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def listCommandsCommand(event):
    """Gives a list of commands

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    bot.editMessage(channelID, messageID, "```\n" + "\n".join(settings.commandsInfo.values()) + f"\n---> Number of commands: {len(settings.commandsInfo.values())}```")
        
    
settings.commands[fileName] = listCommandsCommand
settings.commandsInfo[fileName] = ";listcommands <no settings> - gets you a list of commands"