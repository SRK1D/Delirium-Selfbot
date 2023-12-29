import settings
import threading
import time

bot = settings.bot


def reconnection():
    try:
        temp_ = bot.gateway.session.read()
    except Exception as e:
        reconnection()
        return
    
    
def initializeReconnection():
    while True:
        time.sleep(5)
        reconnection()
        
settings.log("Info", "Reconnection handler loaded!")
settings.log("Info", "-" * 30 + " STATUS")
threading.Thread(target=initializeReconnection).start()