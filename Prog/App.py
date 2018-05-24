import Prog.UI

class App:

    i=0

    def __init__(self):

        #self.title = "Can Do Flow"

        self.version = "0.0.1-a"
        self.kRun = True
        self.key_pressed_esc = True
        self.program_closed = False
        self.App()

    def App(self):
        while self.kRun:
            # Do stuff here
            if self.key_pressed_esc or self.program_closed:
                for i in range(10):
                    print("Hello")
                    a = Prog.UI.UI()
                i=0
                break


if __name__ == "__main__":
    App()