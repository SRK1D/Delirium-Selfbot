import settings
import os
import requests
import json

fileName = os.path.basename(__file__).replace(".py", "")
bot = settings.bot

def pointersCommand(event):
    """Wtf moment, pointers yes yes

    Args:
        event (response event): the event that calls this function
    """
    messageInfo = event.parsed.auto()
    messageID = messageInfo["id"]
    
    channelID = str(messageInfo["channel_id"])
    messageContent = messageInfo["content"].split(" ")
    
    bot.deleteMessage(channelID, messageID)
    if len(messageContent) == 2 and messageContent[1].isnumeric():
        loops = int(messageContent[1]) + 1
        keyWord = "coke"
        ending = f"coke" + str(loops - 1)

        phrase = f"#include <iostream>\nint main "
        phrase += "{"
        phrase += f"\n\tint {keyWord}0 = 5;"
        for lf in range(1, loops):
            phrase = f"{phrase}\n\tint{'*' * lf} coke{str(lf)} = &coke{str(lf - 1)};"

        for lf in range(loops - 1, 0, -1):
            ending = f"(*(int{'*' * (lf)})({ending}))"

        ending = f"\tint {keyWord}Result = {ending}"
        phrase = f"{phrase}\n{ending};\n\tstd::cout << \"Number of {keyWord}0 when pointed too many times is: \" << {keyWord}Result << '\\n';\n"
        phrase += "}"
        # print(phrase)
        with open("WTF.cpp", "w+") as f:
            f.write(phrase)
            f.close()
        
        bot.sendFile(channelID, "WTF.cpp")
        os.remove("WTF.cpp")
    
settings.commands[fileName] = pointersCommand
settings.commandsInfo[fileName] = ";pointersmeme <pointers to pointers amount> - gives a pointer file that is like wtf"