from tkinter import *



class Calculator():
    def __init__(self, laptime, fuelxlap):
        self.laptime = sum(x * int(t) for x, t in zip([3600, 60, 1], laptime.split(":")))                 #lap time in seconds
        self.fuelxlap = int(float(fuelxlap))                                                              #fuel for one lap i liters


    def time_based(self, time):
        self.time = sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))                       #race time in seconds
        self.lapsamount = self.time / self.laptime
        self.fuel = self.lapsamount * self.fuelxlap
        self.myLabel = Label(text=str(self.fuel))
        self.myLabel.pack()

    def laps_based(self, laps):
        self.laps = int(laps)                                                                               #Number of laps
        self.fuel = self.laps * self.fuelxlap
        self.myLabel = Label(text=str(self.fuel))
        self.myLabel.pack()


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Is your race based on time duration or on number of laps?").pack(side="top", fill="x", pady=10)
        Button(self, text="TIME",
                  command=lambda: master.switch_frame(PageOne)).pack()
        Button(self, text="LAPS",
                  command=lambda: master.switch_frame(PageTwo)).pack()



class PageOne (Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        L1 = Label(self, text="Fuel calculator: please enter data")
        L1.pack()

        input1 = Entry(self, width=30)
        input1.pack()
        input1.insert(0, "Enter your lap time")

        input2 = Entry(self, width=30)
        input2.pack()
        input2.insert(0, "Enter the fuel per lap")

        input3 = Entry(self, width=30)
        input3.pack()
        input3.insert(0, "Enter the race time")


        printButton = Button(self, text="Calculate", command=lambda: Calculator.time_based(Calculator(input1.get(),input2.get()),input3.get()))

        printButton.pack(side=LEFT)

        Button(self, text="Return to start page",
            command=lambda: master.switch_frame(StartPage)).pack()


class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        L1 = Label(self, text="Fuel calculator: please enter data")
        L1.pack()

        input1 = Entry(self, width=30)
        input1.pack()
        input1.insert(0, "Enter the fuel per lap")

        input2 = Entry(self, width=30)
        input2.pack()
        input2.insert(0, "Enter the race time")

        input3 = Entry(self, width=30)
        input3.pack()
        input3.insert(0, "Enter the amount of laps")

        printButton1 = Button(self, text="Calculate", command=lambda: Calculator.laps_based(Calculator(input1.get(),input2.get()),input3.get()))

        printButton1.pack(side=LEFT)

        Button(self, text="Return to start page",
            command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()