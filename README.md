# Multi-Messenger
In this Project I created a Multi-Messenger(web Application) through that multiple user can chat with each other at same time. Using Python Programming Language 

# Introduction
Teleconferencing or Chatting, is a method of using technology to bring
people and ideas “together” despite of the geographical barriers. The
technology has been available for year’s butte acceptance it was quit
recent. Our project is an example of a chat server. It is made up of 2
applications the client application, which runs on the user’s Pc and
server application, which runs on any Pc on the network. To start
chatting client should get connected to server where they can practice
two kinds of chatting, public one(message is broadcasted to all
connected users) and private one(between any 2 users only)and during
the last one security measures were taken
Basically our project is ‘One Server Multiple Clients’ program,which is
more like to the real world chat apps we use every day.To run the program,execute the ‘server.py’( after changing the bind()
address to the address of the server on which it is supposed to run.),
then execute the ‘client.py’(guess what? Samething here .But you will
have to add the server address in the connect() function here).
Of course you can have all of them running on the same system. 

# BACKGROUND
Our project is a simple Chat Room server and allow multiple clients to
connect to it using a client side script. The code uses the concept of
sockets and threading.
# Socket programming
Sockets can be thought of as end points in a communication channel
that is bi directional, and establishes communication between a server
and one or more clients. Here, we setup a socket on each end and allow
a client to interact with other clients via the server. The socket on the
server side associates itself with some hardware port on the server side.
Any client that has a socket associated with the same port can
communicate with the server socket .
# Multi Threading
A thread is sub process that runs a set of commands individually of any
other thread. So, every time a user connects to the server, a separate
thread is created for that user and communication from server to client
takes place along individual threads based on socket objects created for
the sake of identity of each client.
We will require two scripts to establish this chat room. One to keep the
server running, and another that every client should run in order to
connect to the server 
