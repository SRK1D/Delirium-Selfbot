# FULLY MADE BY
# SRK1D - SRK!D

import os
import json
from ressources.utils.wrappers import *

appSettings = json.load(open("settings.json", "r"))

import settings # Manages basically everything lmfao

settings.defaultInit()

def loadCommands():
    """Load all the commands modules in ./commands/
    """

    commandPath = "./commands/"
    pythonFiles = [file.replace(".py", "")
                   for file in os.listdir(commandPath)
                   if os.path.isfile(os.path.join(commandPath, file)) and ".py" in file] # Generates a list of python
                                                                                         # files in the command path and remove the .py

    settings.log("Info", "-" * 30 + " COMMANDS")
    settings.log("Info", "Loading the commands...")

    for pythonModule in pythonFiles:
        settings.log("Info", f"Loading -> ./commands/{pythonModule}")
        __import__("commands." + pythonModule)

    settings.log("Info", "-" * 30 + " RECONNECTION")

def reloadCommands():
    """Cleans the commands list and create it once more (for some reason)
    """
    settings.commands = {}
    loadCommands()

settings.log("Info", "Checking token validity and parsing discord version...")
settings.settingsInit(";", appSettings["discordToken"]) # Starts the bot (with prefix + token) and creates the
                                                              # commands list

@settings.bot.gateway.command
def eventHandler(resp):
    if resp.event.ready_supplemental:
        settings.log("Info", "Successfully connected to gateway!")
        settings.log("Info", "-" * 30 + " LOGS")
        settings.log("Info", f"Prefix is: \"{settings.prefix}\"")
        settings.log("Info", f"Use \"{settings.prefix}listcommands\" to get a list of commands")

    """Command handler
    """
    if resp.event.message:

        try: # For some reasons, it gives some error for some reasons
            # Checks if theres a command for it
            messageInfo = resp.parsed.auto()
        except:
            return

        messageContent = str(messageInfo["content"])
        messageCommand = (messageContent.split(" ")[0]).replace(settings.prefix, "")
        if str(messageInfo["author"]["id"]) == appSettings["userID"]: # Type checking (too lazy) and checking for user
            if (messageContent.startswith(settings.prefix) == True): # Checking if commands exist
                if (messageCommand in settings.commands):
                    settings.log("Action", f"Command called: \"{messageCommand}\"")
                    settings.commands[messageCommand](resp)
                else:
                    settings.log("Warning", f"Command not found: \"{messageCommand}\"")

loadCommands()

settings.log("Info", "Loading reconnection handler for optimal connection...")
__import__("ressources.utils.reconnectionHandler")

settings.log("Info", "Loaded custom randomizer!")
settings.log("Info", "Connecting to gateway...")

settings.bot.gateway.run(auto_reconnect=True)
