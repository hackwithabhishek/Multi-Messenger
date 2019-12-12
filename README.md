# Multi-Messenger
In this Project I created a Multi-Messenger(web Application) through that multiple user can chat with each other at same time. Using Python Programming Language 

# Introduction
Teleconferencing or Chatting, is a method of using technology to bring people and ideas “together” despite of the geographical barriers. The
technology has been available for year’s butte acceptance it was quit recent. Our project is an example of a chat server. It is made up of 2
applications the client application, which runs on the user’s Pc and server application, which runs on any Pc on the network. To start
chatting client should get connected to server where they can practice two kinds of chatting, public one(message is broadcasted to all
connected users) and private one(between any 2 users only)and during the last one security measures were taken
Basically our project is ‘One Server Multiple Clients’ program,which is more like to the real world chat apps we use every day.To run the program,execute the ‘server.py’( after changing the bind()
address to the address of the server on which it is supposed to run.), then execute the ‘client.py’(guess what? Samething here .But you will
have to add the server address in the connect() function here). Of course you can have all of them running on the same system. 

# BACKGROUND
Our project is a simple Chat Room server and allow multiple clients to connect toi tusi ngacl i ent si descr i pt .Thecodeusest heconceptof
socket sandt hr eadi ng.
Socketpr ogr ammi ng
Socket scanbet houghtofasendpoi nt si nacommuni cat i onchannel
t hati sbi di r ect i onal ,andest abl i shescommuni cat i onbet weenaser v er
andoneormor ecl i ent s.Her e, wesetupasocketoneachendandal l ow
acl i entt oi nt er actwi t hot hercl i ent sv i at heser v er .Thesocketont he
ser v ersi deassoci at esi t sel fwi t hsomehar dwar epor tont heser v ersi de.
Anycl i entt hathasasocketassoci at ed wi t h t hesamepor tcan
communi cat ewi t ht heser v ersocket .
Mul t i Thr eadi ng
At hr eadi ssubpr ocesst hatr unsasetofcommandsi ndi v i dual l yofany
ot hert hr ead.So,ev er yt i meauserconnect st ot heser v er ,asepar at e
t hr eadi scr eat edf ort hatuserandcommuni cat i onf r om ser v ert ocl i ent
t akespl aceal ongi ndi v i dualt hr eadsbasedonsocketobj ect scr eat edf or
t hesakeofi dent i t yofeachcl i ent .
Wewi l lr equi r et woscr i pt st oest abl i sht hi schatr oom.Onet okeept he
ser v err unni ng,andanot hert hatev er ycl i entshoul dr uni nor dert o
connectt ot heser v e
