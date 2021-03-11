import os, time
from tkinter import *
from tkinter import messagebox

ngrokpath = "C://Users//aliha//Desktop//Tools//ngrok.exe"

class App:

    def __init__(self, master, ngrok_path='ngrok.exe') -> None:
        
        self.command_line_call = None

        Label(master, text="ngrok GUI", font=('', 30)).pack()
        
        self.mainframe = Frame(master)
        self.mainframe.pack(side=BOTTOM)

        Label(self.mainframe, text="Enter TCP port:").grid(column = 1, row = 1)

        self.enter_port = Entry(self.mainframe)
        self.enter_port.grid(row = 1, column=2, padx = 1, pady = 10)

        start_button = Button(self.mainframe, text="Start Server", command=self.start_ngrok)
        start_button.grid(row = 3, column=2, padx = 1, pady = 10)

        end_button = Button(self.mainframe, text="End Server", command=self.end_ngrok)
        end_button.grid(row = 3, column=3, padx = 1, pady = 10)

        # self.feed = Text(self.mainframe)
        # self.feed.grid(row = 2, column = 2)


    def start_ngrok(self):

        port = self.enter_port.get()

        if port.isnumeric() and len(port) == 5:
            self.command_line_call = os.popen(f'C://Users//aliha//Desktop//Tools//ngrok.exe tcp {port}')
        
        else:
            messagebox.showinfo("Error!","Port is not in the correct format.")

    def end_ngrok(self):
        pass
        # port = self.enter_port.get()

            
    # def update(self):

    #     if self.command_line_call is not None:
    #         a = self.command_line_call.read()
    #         if len(a) > 0:
    #             self.feed.insert(1.0, a)
                # print(a)

# outputs = os.popen(f'start C://Users//aliha//Desktop//Tools//ngrok.exe tcp {33355}')


# print(outputs.read())

root = Tk()
root.title("ngrok GUI")
root.geometry("300x200")
app = App(root, ngrokpath)
root.mainloop()

# while True:
#     root.update()
#     root.update_idletasks()
#     app.update()

# while True:
#     print(outputs.readline())