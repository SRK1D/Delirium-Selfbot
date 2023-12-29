import random
import time

class Randomizer:
    def __init__(self, tbl) -> None:
        random.seed(time.time())
        self._mTable = tbl
        
    def returnRandomWithOffset(self):
        return random.choice(self._mTable)