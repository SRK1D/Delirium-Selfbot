import threading
import _thread

def timeoutWrapper(seconds, task):
    def functionWrapper(func):
        def quitFunction():
            print(f"\n\n\nERROR TIMEOUT: COULD NOT FINISH {task}\n\n\n")
            _thread.interrupt_main()
        def argumentWrapper(*args, **kwargs):
            timerHandler = threading.Timer(seconds, quitFunction)
            timerHandler.start()
            try:
                result = func(*args, **kwargs)
            finally:
                timerHandler.cancel()
            return result
            
        return argumentWrapper
    return functionWrapper