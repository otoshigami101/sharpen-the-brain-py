from Tkinter import *
from threading import Timer
import tkMessageBox

'''
    TRAFFIC LIGHT SIMULATOR BY OTOSHIGAMI
'''
class App(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, root)
        self.initWindow(root)
        self.createWidgets()
        self.pack(anchor=N, fill=BOTH, expand=True)

    def initWindow(self, root, width=800, height=600):
        root.title('Traffic Light')

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_coordinate = int(screen_width / 2) - (width / 2)
        y_coordinate = int(screen_height / 2) - (height / 2)

        root.geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))

    def numberOnly(self, value):
        if str.isdigit(value) or value == "":
            return True
        else:
            return False

    def createWidgets(self):
        m1 = PanedWindow(self)
        m1.pack(fill=X)

        numberOnly = (self.register(self.numberOnly))

        Label(m1, text="interval red lamp").grid(row=0, sticky=W)
        self.interval_red = Entry(m1, validate='all', validatecommand=(numberOnly, '%P'))
        self.interval_red.grid(row=0, column=1)

        Label(m1, text="interval yellow lamp").grid(row=1, sticky=W)
        self.interval_yellow = Entry(m1, validate='all', validatecommand=(numberOnly, '%P'))
        self.interval_yellow.grid(row=1, column=1)

        Label(m1, text="interval green lamp").grid(row=2, sticky=W)
        self.interval_green = Entry(m1, validate='all', validatecommand=(numberOnly, '%P'))
        self.interval_green.grid(row=2, column=1)

        m2 = PanedWindow(self)
        m2.pack()

        lampWidth = 10
        lampHeight = 5

        self.startBtn = Button(m2, text="Start", command=self.start)
        self.startBtn.grid(row=0, padx=5, pady=5)

        self.redLamp = {
            "shape": Label(m2, text="0", fg="black", bg="gray", width=lampWidth, height=lampHeight),
            "name": "redLamp"
        }
        self.redLamp["shape"].grid(row=1, pady=10)

        self.yellowLamp = {
            "shape": Label(m2, text="0", fg="black", bg="gray", width=lampWidth, height=lampHeight),
            "name": "yellowLamp"
        }
        self.yellowLamp["shape"].grid(row=2, pady=10)

        self.greenLamp = {
            "shape": Label(m2, text="0", fg="black", bg="gray", width=lampWidth, height=lampHeight),
            "name": "greenLamp"
        }
        self.greenLamp["shape"].grid(row=3, pady=10)

    def setInterval(self, handler):
        self.timer = Timer(1, handler)
        self.timer.start()

    def handler(self):
        self.setInterval(self.handler)
        try:
            self.second -= 1
            self.current_lamp['shape']['text'] = self.second

            if self.second == 0:

                if self.current_lamp['name'] == 'redLamp':
                    self.current_lamp['shape']['bg'] = 'gray'

                    self.current_lamp = self.yellowLamp
                    self.current_lamp['shape']['bg'] = 'yellow'
                    self.second = int(self.interval_yellow.get())
                    self.current_lamp['shape']['text'] = self.second

                elif self.current_lamp['name'] == 'yellowLamp':
                    self.current_lamp['shape']['bg'] = 'gray'

                    self.current_lamp = self.greenLamp
                    self.current_lamp['shape']['bg'] = 'green'
                    self.second = int(self.interval_green.get())
                    self.current_lamp['shape']['text'] = self.second

                elif self.current_lamp['name'] == 'greenLamp':
                    self.current_lamp['shape']['bg'] = 'gray'

                    self.current_lamp = self.redLamp
                    self.current_lamp['shape']['bg'] = 'red'
                    self.second = int(self.interval_red.get())
                    self.current_lamp['shape']['text'] = self.second

        except AttributeError:
            self.current_lamp = self.redLamp
            self.current_lamp['shape']['bg'] = 'red'
            self.second = int(self.interval_red.get())
            self.current_lamp['shape']['text'] = self.second

    def start(self):
        if (self.interval_red.get() and self.interval_yellow.get() and self.interval_green.get()):
            self.interval_red['state'] = 'disabled'
            self.interval_yellow['state'] = 'disabled'
            self.interval_green['state'] = 'disabled'

            self.startBtn['text'] = 'stop'
            self.startBtn['command'] = self.stop

            self.handler()
        else:
            tkMessageBox.showerror("Error", "set interval for all lamp first.")

    def stop(self):
        self.startBtn['text'] =  'start'
        self.startBtn['command'] = self.start
        self.interval_red['state'] = 'normal'
        self.interval_yellow['state'] = 'normal'
        self.interval_green['state'] = 'normal'
        self.timer.cancel()

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    app.mainloop()
    try:
        app.timer.cancel()
    except AttributeError:
        pass