from tkinter import *



class Calculator():
    def __init__(self, laptime, fuelxlap):
        self.laptime = sum(x * int(t) for x, t in zip([3600, 60, 1], laptime.split(":")))               #lap time in seconds
        self.fuelxlap = int(fuelxlap)                                                                   #fuel for one lap i liters


    def time_based(self, time):
        self.time = sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))                     #race time in seconds
        self.lapsamount = self.time / self.laptime
        self.fuel = self.lapsamount * self.fuelxlap
        self.myLabel = Label(root, text=str(self.fuel))
        self.myLabel.pack()

    def laps_based(self, laps):
        self.laps = int(laps)                                                                            #Number of laps
        self.fuel = self.laps * self.fuelxlap
        self.myLabel = Label(root, text=str(self.fuel))
        self.myLabel.pack()



class Buttons (Calculator):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


        self.L1 = Label(frame, text="Fuel calculator: please enter data")
        self.L1.pack()


        self.input1 = Entry(frame, width=30)
        self.input1.pack()
        self.input1.insert(0, "Enter your lap time")

        self.input2 = Entry(frame, width=30)
        self.input2.pack()
        self.input2.insert(0, "Enter the fuel per lap")

        self.input3 = Entry(frame, width=30)
        self.input3.pack()
        self.input3.insert(0, "Enter the race time")

        self.input4 = Entry(frame, width=30)
        self.input4.pack()
        self.input4.insert(0, "Enter the amount of laps")

        self.printButton = Button(frame, text="time based", command=lambda: Calculator.time_based(Calculator(self.input1.get(),self.input2.get()),self.input3.get()))

        self.printButton.pack(side=LEFT)

        self.printButton2 = Button(frame, text="laps based", command=lambda: Calculator.laps_based(Calculator(self.input1.get(),self.input2.get()),self.input4.get()))

        self.printButton2.pack(side=RIGHT)

    def click(self):
        print(self.input2.get())

root = Tk()
b = Buttons(root)
root.mainloop()

