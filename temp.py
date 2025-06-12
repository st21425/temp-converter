"""
convert temps
v1: convert
"""
from tkinter import *
class Temp():
    def __init__(self):
        self.root = Tk()
        self.root.title("Temp converter")
        self.root.resizable(0,0)

        self.container = Frame(self.root)
        self.container.grid(row= 0, column=0, sticky = "nsew")

        self.frames = {}
        self.frames["MenuFrame"] = self.menu()
        self.frames["toCelFrame"] = self.toCel()
        self.frames["toFarFrame"] = self.toFar()

        self.show_frames("MenuFrame")

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def menu(self):
        frame = Frame(self.container)
        frame.grid(row=0,column=0)

        self.tempLabel = Label(frame, font = ("Verdana 16 bold"), text = "Temperature Converter")
        self.tempLabel.grid(row=0, columnspan=2,padx=10,pady=10, sticky="nsew")

        self.toCelButton = Button(frame, text = "To Celcius", bg = "yellow", font = "Verdana 12 bold", command = lambda: self.show_frames("toCelFrame"))
        self.toFarButton = Button(frame, text = "To Fahrenhiet", bg = "orange", font = "Verdana 12 bold", command = lambda: self.show_frames("toFarFrame"))

        self.toCelButton.grid(row=1, column=0,padx=10,pady=10, sticky="nsew")
        self.toFarButton.grid(row=1, column=1,padx=10,pady=10, sticky="nsew")

        frame.grid(row=0, column=0, sticky="nswe")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        for i in range(2):
            frame.grid_columnconfigure(0, weight=1)
        for i in range(2):
            frame.grid_rowconfigure(0, weight=1)

        return frame

    def toFar(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nswe")
        Label(frame, text="Convert to Fahrenheit").grid(row=0, column=1)
        
        
        self.temp_entry_c=Entry(frame, justify=CENTER)
        self.temp_entry_c.grid(row=1,column=1) 

        self.result_label_c = Label(frame, text="Result: ")
        self.result_label_c.grid(row=3, column=0, columnspan=2, pady=10)


        self.calc_button = Button(frame, text="Calculate", bg="#dda6aa",font="Arial 12",command=self.toC)
        self.calc_button.grid(row=2,column=1, padx=10,pady=10)

        self.back_button = Button(frame, text="Go Back", bg="#dda6aa", font="Arial 12 ",command=lambda: self.show_frames("MenuFrame"))
        self.back_button.grid(row=2, column=0, padx=10, pady=10)

        self.reset_button=Button(frame, text="Reset", bg="#dda6aa", font="Arial 12",command=self.reset)
        self.reset_button.grid(row=2,column=2,padx=10,pady=10)

        return frame
    def toCel(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nswe")
        Label(frame, text="Convert to Celcius").grid(row=0, column=1)
            
            
        self.temp_entry_f=Entry(frame, justify=CENTER)
        self.temp_entry_f.grid(row=1,column=1) 

        self.result_label_f = Label(frame, text="Result: ")
        self.result_label_f.grid(row=3, column=0, columnspan=2, pady=10)


        self.calc_button = Button(frame, text="Calculate", bg="#dda6aa",font="Arial 12",command=self.toF)
        self.calc_button.grid(row=2,column=1, padx=10,pady=10)

        self.back_button = Button(frame, text="Go Back", bg="#dda6aa", font="Arial 12 ",command=lambda: self.show_frames("MenuFrame"))
        self.back_button.grid(row=2, column=0, padx=10, pady=10)

        self.reset_button=Button(frame, text="Reset", bg="#dda6aa", font="Arial 12",command=self.reset)
        self.reset_button.grid(row=2,column=2,padx=10,pady=10)

        return frame

    def run(self):
        self.root.mainloop()
    def toF(self):
        try:
            temp = float(self.temp_entry_f.get())
            farenhright=(temp-32)*5/9
            self.result_label_f.config(text=f"Result: {farenhright:.2f}°C")
        except ValueError:
            self.result_label_f.config(text="Invalid input! Enter a number.")
    def toC(self):
        try:
            temp = float(self.temp_entry_c.get())
            farenhright=(temp*9/5)+32
            self.result_label_c.config(text=f"Result: {farenhright:.2f}°F")
        except ValueError:
            self.result_label_c.config(text="Invalid input! Enter a number.")
    def reset(self):
        self.temp_entry_c.delete(0, END) 
        self.temp_entry_f.delete(0, END)  
        self.result_label_c.config(text="Result: ") 
        self.result_label_f.config(text="Result: ")  
app = Temp()
app.run()