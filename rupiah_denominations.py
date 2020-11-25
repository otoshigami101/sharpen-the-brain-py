from Tkinter import *


class App(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, root)
        self.pack(fill=BOTH)
        self.initWindow()
        self.createWidgets()

    def initWindow(self, width=800, height=600):
        self._root().title('Rupiah Denominations')

        screen_width = self._root().winfo_screenwidth()
        screen_height = self._root().winfo_screenheight()

        x_coordinate = int(screen_width / 2) - (width / 2)
        y_coordinate = int(screen_height / 2) - (height / 2)

        self._root().geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))

    def numberOnly(self, value):
        if str.isdigit(value) or value == "":
            return True
        else:
            return False

    def createWidgets(self):
        m1 = PanedWindow(self)
        m1.pack(pady=25)

        Label(m1, text="amount", anchor=W).grid(row=0)
        self.amount = Entry(m1, validate="all", validatecommand=(self.register(self.numberOnly), '%P'))
        self.amount.grid(row=0, column=1)

        Button(m1, text="process", command=self.process).grid(row=1, column=1)

        m2 = PanedWindow(self)
        m2.pack(pady=50, padx=50)

        m2c1 = PanedWindow(m2)
        self.sheets = ['100.000', '50.000', '20.000', '10.000', '5.000', '2.000', '1.000']
        self.entrySheets = {}
        i = 0
        for sheet in self.sheets:
            Label(m2c1, text=sheet, anchor=N).grid(row=i, sticky=E)

            self.entrySheets[sheet] = Entry(m2c1)
            self.entrySheets[sheet].grid(row=i, column=1)

            Label(m2c1, text="sheets").grid(row=i, column=2)

            i += 1

        m2c2 = PanedWindow(m2)
        m2c1.pack()

        self.chips = ['500', '200', '100', '50', '25']
        self.entryChips = {}
        i = 0
        for chip in self.chips:
            Label(m2c2, text=chip, anchor=N).grid(row=i, sticky=E)

            self.entryChips[chip] = Entry(m2c2)
            self.entryChips[chip].grid(row=i, column=1)

            Label(m2c2, text="chips").grid(row=i, column=2)

            i += 1

        m2c1.grid(row=0, padx=25, pady=25)
        m2c2.grid(row=0, column=2, sticky=N, padx=25, pady=25)

        self.resetCount()

    def resetCount(self):
        for sheet in self.sheets:
            self.entrySheets[sheet]['state'] = NORMAL
            self.entrySheets[sheet].delete(0, END)
            self.entrySheets[sheet].insert(0, "0")
            self.entrySheets[sheet]['state'] = DISABLED


        for chip in self.chips:
            self.entryChips[chip]['state'] = NORMAL
            self.entryChips[chip].delete(0, END)
            self.entryChips[chip].insert(0, "0")
            self.entryChips[chip]['state'] = DISABLED

    def process(self):
        self.resetCount()

        amount = int(self.amount.get())

        while amount > 0:

            amount_in_sheet = False
            for sheet in self.sheets:
                num = int(sheet.replace('.', ''))
                if amount >= num:
                    amount -= num
                    self.entrySheets[sheet]['state'] = NORMAL
                    count = int(self.entrySheets[sheet].get()) + 1

                    self.entrySheets[sheet].delete(0, END)
                    self.entrySheets[sheet].insert(0, str(count))
                    self.entrySheets[sheet]['state'] = DISABLED

                    amount_in_sheet = True
                    break
                else:
                    continue

            if not amount_in_sheet:
                for chip in self.chips:
                    num = int(chip)
                    if amount >= num:
                        self.entryChips[chip]['state'] = NORMAL
                        amount -= num
                        count = int(self.entryChips[chip].get()) + 1
                        self.entryChips[chip].delete(0, END)
                        self.entryChips[chip].insert(0, str(count))

                        self.entryChips[chip]['state'] = DISABLED

                        break
                    else:
                        continue

            if amount < int(self.chips[-1]):
                break

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    app.mainloop()
