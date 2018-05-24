import tkinter
import random
from math import floor

class UI:

    def __init__(self):
        """self.ID = floor(float(random.randint(1,999999)/29189) * 10000000000)
        if len(str(self.ID)) < 12:
            self.ID = self.ID * 10 ** (12-len(str(self.ID)))
        print(self.ID)"""
        self.title = "Can Do Flow"
        self.createUI()

    def createUI(self):

        self.f = tkinter.Canvas