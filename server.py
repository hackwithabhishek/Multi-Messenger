from socket import *
from _thread import *








s=socket((AF_INET),SOCK_STREAM)
host="127.0.0.1"
port=888
s.bind((host,port))
s.listen(50)

sessions=[]

def recvThread(c,ad):
    while True:
        messege= str(ad[1]) + " : " + c.recv(1048).decode('utf-8')
        for session in sessions:
            if session !=c:
                session.send(messege.encode('utf-8'))
                

while True:
    c,ad= s.accept()
    messege= "new connection from "+ str(ad[1])
    for session in sessions:
        session.send(messege.encode('utf-8'))
    sessions.append(c)
    start_new_thread(recvThread,(c,ad))
        