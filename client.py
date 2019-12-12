from socket import *
from _thread import *
from tkinter import *








s=socket((AF_INET),SOCK_STREAM)
host="127.0.0.1"
port=888
s.connect((host,port))

window=Tk()
window.title("chat client")
window.geometry("400x400")

label=Label(window)
label.grid(row=3,column=3)

entry=Entry(window,width="40")
entry.grid(row=1,column=3)

def clicked():
    messege=entry.get()
    s.send(messege.encode('utf-8'))
    entry.delete(0,END)

btn=Button(window,text="send",bg="green",fg="white",width=8,height=1,command=clicked)
btn.grid(row=1,column=4)

def recvThread(s):
    while True:
        label['text'] += "\n" + s.recv(1024).decode('utf-8')
        
start_new_thread(recvThread,(s,))

window.mainloop()