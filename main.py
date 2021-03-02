from tkinter import *



class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title('Fuel Calculator')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()




class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Label1 = Label(self, text="Is your race based on time duration or on number of laps?")
        Label1.configure(font=("Courier", 14, "italic"))
        Label1.grid(row=0, column=1,columnspan=4, padx=20, pady=20)

        Button1 = Button(self, text="TIME",
                  command=lambda: master.switch_frame(PageOne), height=3, width=20, padx=20, pady=10)
        Button1.grid(row=1, column=1)

        Button2 = Button(self, text="LAPS",
                  command=lambda: master.switch_frame(PageTwo), height=3, width =20, padx=20, pady=10)
        Button2.grid(row=1, column=3)



class PageOne (Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Description1 = Label(self, text="Fuel calculator: please enter data")
        Description1.configure(font=("Courier", 10, "italic"))
        Description1.grid(row=0, column=0,columnspan=2, padx=20, pady=20)

        input1 = Entry(self, width=30)
        input1.grid(row=1, column=0, padx=5, pady=5)
        input1.insert(0, "Enter your lap time")

        input2 = Entry(self, width=30)
        input2.grid(row=2, column=0, padx=5, pady=5)
        input2.insert(0, "Enter the fuel per lap")

        input3 = Entry(self, width=30)
        input3.grid(row=3, column=0, padx=5, pady=5)
        input3.insert(0, "Enter the race time")

        result1 = Entry(self, width=30)
        result1.grid(row=4, column=0, padx=40, pady=20)
        result1.insert(0, "Result in liters")


        Button1 = Button(self, text="Calculate", command=lambda: calculate())
        Button1.grid(row=5, column=0, padx=5, pady=5)

        Button2 = Button(self, text="Return to start page",command=lambda: master.switch_frame(StartPage))
        Button2.grid(row=5, column=1, padx=5, pady=5)

        def calculate():
            laptime = sum(x * int(t) for x, t in zip([3600, 60, 1], input1.get().split(":")))                           # lap time in seconds
            fuelxlap = int(float(input2.get()))
            time = sum(x * int(t) for x, t in zip([3600, 60, 1], input3.get().split(":")))                              # race time in seconds
            lapsamount = time / laptime
            fuel = lapsamount * fuelxlap
            result1.delete(0, END)
            result1.insert(0, str(fuel) + " [L]")

class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Description2 = Label(self, text="Fuel calculator: please enter data")
        Description2.configure(font=("Courier", 10, "italic"))
        Description2.grid(row=0, column=0,columnspan=2, padx=20, pady=20)

        input1 = Entry(self, width=30)
        input1.grid(row=1, column=0, padx=5, pady=5)
        input1.insert(0, "Enter the fuel per lap")

        input2 = Entry(self, width=30)
        input2.grid(row=2, column=0, padx=5, pady=5)
        input2.insert(0, "Enter the race time")

        input3 = Entry(self, width=30)
        input3.grid(row=3, column=0, padx=5, pady=5)
        input3.insert(0, "Enter the amount of laps")


        result2 = Entry(self, width=30)
        result2.grid(row=4, column=0, padx=40, pady=20)
        result2.insert(0, "Result in liters")

        Button1 = Button(self, text="Calculate", command=lambda: calculate())
        Button1.grid(row=5, column=0, padx=5, pady=5)

        Button2 = Button(self, text="Return to start page",command=lambda: master.switch_frame(StartPage))
        Button2.grid(row=5, column=1, padx=5, pady=5)




        def calculate():
            fuelxlap = int(float(input2.get()))
            laps = int(input3.get())                                                                                    # Number of laps
            fuel = laps * fuelxlap
            result2.delete(0, END)
            result2.insert(0, str(fuel) + " [L]")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()