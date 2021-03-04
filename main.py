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

        Label1 = Label(self, text="Welcome to Fuel calcualtor")
        Label1.configure(font=("Arial", 14, "italic"))
        Label1.grid(row=0, column=1,columnspan=4, padx=20, pady=20)

        Label2 = Label(self, text="Is your race based on time duration or on number of laps?")
        Label2.configure(font=("Arial", 10, "italic"))
        Label2.grid(row=1, column=1,columnspan=4, padx=20, pady=20)

        Button1 = Button(self, text="TIME",
                  command=lambda: master.switch_frame(PageOne), height=3, width=20, padx=20, pady=10)
        Button1.grid(row=2, column=1)

        Button2 = Button(self, text="LAPS",
                  command=lambda: master.switch_frame(PageTwo), height=3, width =20, padx=20, pady=10)
        Button2.grid(row=2, column=3)



class PageOne (Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Description1 = Label(self, text="Fuel calculator: please enter data")
        Description1.configure(font=("Courier", 10, "italic"))
        Description1.grid(row=0, column=0,columnspan=2, padx=20, pady=20)

        label1 = Label(self, text="Lap time")
        label1.grid(row=1, column=0, padx=1, pady=5)

        label2 = Label(self, text="Fuel per lap")
        label2.grid(row=2, column=0, padx=1, pady=5)

        label3 = Label(self, text="Race time")
        label3.grid(row=3, column=0, padx=5, pady=5)

        label4 = Label(self, text="Minimum feul")
        label4.grid(row=4, column=0, padx=1, pady=5)

        label5 = Label(self, text="Safe fuel")
        label5.grid(row=4, column=1, padx=1, pady=5)


        input1 = Entry(self, width=20)
        input1.grid(row=1, column=1, padx=5, pady=5)
        input1.insert(0, "[MM:SS:MSMS]")

        input2 = Entry(self, width=20)
        input2.grid(row=2, column=1, padx=5, pady=5)
        input2.insert(0, "0")

        input3 = Entry(self, width=20)
        input3.grid(row=3, column=1, padx=5, pady=5)
        input3.insert(0, "[MM:SS]")

        result1 = Entry(self, width=30)
        result1.grid(row=5, column=0, padx=5, pady=5)
        result1.insert(0, "Result in liters")

        result2 = Entry(self, width=30)
        result2.grid(row=5, column=1, padx=5, pady=5)
        result2.insert(0, "Result in liters")


        Button1 = Button(self, text="Calculate", command=lambda: calculate())
        Button1.grid(row=6, column=0, padx=5, pady=5)

        Button2 = Button(self, text="Return to start page",command=lambda: master.switch_frame(StartPage))
        Button2.grid(row=6, column=1, padx=5, pady=5)

        def calculate():
            laptime = sum(x * int(t) for x, t in zip([3600, 60, 1], input1.get().split(":")))
            fuelxlap = float(input2.get())
            time = sum(x * int(t) for x, t in zip([3600, 60, 1], input3.get().split(":")))
            lapsamount = time / laptime
            fuel = lapsamount * fuelxlap
            sfuel = fuel + 2*fuelxlap
            result1.delete(0, END)
            result2.delete(0, END)
            result1.insert(0, str(round(fuel,2)) + " [L]")
            result2.insert(0, str(round(sfuel,2)) + " [L]")


class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        Description1 = Label(self, text="Fuel calculator: please enter data")
        Description1.configure(font=("Courier", 10, "italic"))
        Description1.grid(row=0, column=0,columnspan=2, padx=20, pady=20)

        label1 = Label(self, text="Fuel per lap")
        label1.grid(row=1, column=0, padx=1, pady=5)

        label2 = Label(self, text="Amount of laps")
        label2.grid(row=2, column=0, padx=1, pady=5)

        label3 = Label(self, text="Minimum feul")
        label3.grid(row=3, column=0, padx=1, pady=5)

        label4 = Label(self, text="Safe fuel")
        label4.grid(row=3, column=1, padx=1, pady=5)

        input1 = Entry(self, width=20)
        input1.grid(row=1, column=1, padx=1, pady=5)
        input1.insert(0, "0")

        input2 = Entry(self, width=20)
        input2.grid(row=2, column=1, padx=5, pady=5)
        input2.insert(0, "e.g. 12")


        result1 = Entry(self, width=30)
        result1.grid(row=4, column=0, padx=5, pady=5)
        result1.insert(0, "Result in liters")

        result2 = Entry(self, width=30)
        result2.grid(row=4, column=1, padx=5, pady=5)
        result2.insert(0, "Result in liters")

        Button1 = Button(self, text="Calculate", command=lambda: calculate())
        Button1.grid(row=5, column=0, padx=5, pady=5)

        Button2 = Button(self, text="Return to start page",command=lambda: master.switch_frame(StartPage))
        Button2.grid(row=5, column=1, padx=5, pady=5)


        def calculate():
            fuelxlap = float(input1.get())
            laps = int(input2.get())
            fuel = laps * fuelxlap
            sfuel = fuel + 2*fuelxlap
            result1.delete(0, END)
            result2.delete(0, END)
            result1.insert(0, str(round(fuel,2)) + " [L]")
            result2.insert(0, str(round(sfuel,2)) + " [L]")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()