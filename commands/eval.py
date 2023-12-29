import settings
import os


fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def evalCommand(event):
    """Get the DNS of a website :pOg:

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    
    messageContent = messageInfo["content"].split(" ")

    if len(messageContent) >= 1:
        try:
            args = " ".join(messageContent[1:])
            outp = eval(args)
            print(f"Eval command: {args} -> {str(outp)}")
            bot.editMessage(channelID, messageID, f"{args}: {str(outp)}")
        except:
            bot.deleteMessage(channelID, messageID)
    else:
        bot.deleteMessage(channelID, messageID)


settings.commands[fileName] = evalCommand
settings.commandsInfo[fileName] = ";eval <expression> - Will return expression, calculated"