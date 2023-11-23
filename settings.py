import discum # For selfbot purpose

def defaultInit():
    """Generates the default variables needed
    """
    
    global log
    
    def log(state, message):
        print(f"[{state} - Delirium] {message}")

def settingsInit(prefx, token):
    """Generates the commands list and starts the bot with a prefix + token

    Args:
        prefx (string): the bot prefix
        token (string): the discord token to use (its got to be a user token)
    """
    
    global prefix, commands, bot, commandsInfo
    
    bot = discum.Client(token=token, log=False)
    prefix = prefx
    commands = {}
    commandsInfo = {}