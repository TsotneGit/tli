from tkinter import *
from tkinter import filedialog
from image_serializer import dumps
from sockets import Client_IPV4

root = Tk()
filetypes = (("Pictures", ("*.png", "*.jpg")), ("All Files", "*.*"))
root.geometry("400x400")


def open():
    client = Client_IPV4(ip="127.0.0.1", header_size=16384)
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/Tsotne/Pictures",
        title="Select a file",
        filetypes=filetypes,
    )
    client.send(dumps(root.filename))
    client.disconnect()


btn = Button(root, text="Open Image", command=open)
btn.pack()


root.mainloop()
