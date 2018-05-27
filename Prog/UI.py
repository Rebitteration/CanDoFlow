import tkinter
#import random
#from math import floor

class UI:

    def __init__(self, master):
        """self.ID = floor(float(random.randint(1,999999)/29189) * 10000000000)
        if len(str(self.ID)) < 12:
            self.ID = self.ID * 10 ** (12-len(str(self.ID)))
        print(self.ID)"""
        self.title = "Can Do Flow"
        self.createUI()
        

    def createUI(self):
        print("Nothing")


root = tkinter()

UI(root)

root.mainloop()

"""
Animations are optional,
however I'm not sure as to wether these will work anyway.
But functionality is more important than eyecandy at this stage.
"""
