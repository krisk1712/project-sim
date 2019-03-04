import sched, time                                          # advanced libraraies
import signal                                               # advanced library
import select                                               # advanced library
import sys                                                  # advanced library
import socket                                               #the network library
import pickle                                               # the hex code factory library
import queue 
import random                                             




pac_qu = queue.LifoQueue()
s = sched.scheduler(time.time, time.sleep)                  
host = socket.gethostname()
port = 5555  
server_socket = socket.socket()  
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept() 

def telemet_send(s):
    sat_stat = ["4EA36B01","83EC",["AA55BB66","1A0E","AFFEC34A","0101"],"1212"]
    bat_stat=  ["4EA36B01","83EC",["AA55BB66","1A0E","BA53A980","0101"],"1212"]
    hlth =     ["4EA36B01","83EC",["AA55BB66","1A0E","231876A7","0101"],"1212"]
    chrg =     ["4EA36B01","83EC",["AA55BB66","1A0E","C4579850","0101"],"1212"] 
    vars = [sat_stat,bat_stat,hlth,chrg]
    counter = 0 
    while counter < 10:
        print(counter)
        packt= queue.LifoQueue()
        packt.put(random.choice(vars))
        tm = packt.get()
        telemetry = pickle.dumps(tm)
        time.sleep(1)
        conn.send(telemetry)
        time.sleep(1) 
        data = conn.recv(1024)
        print(data)
        time.sleep(1)
        counter = counter + 1
    s.enter(1, 1, telemet_send, (s,)) 
red = 0
def telecmd_recv(s):
    global red
    print("THE TELECOMMAND PART")
    newtc = "THIS IS A TELECOMMAND"
    try:
        tmdb = open("tmdb.txt",'r')
        new = tmdb.readlines()
        pack = new[red + 1]
        print(pack)
        packt= pickle.dumps(pack)
        conn.send(packt)
        tcdb = open("tcdb.txt",'a')        
        red = red + 2
    except IndexError:
        print("NO TELECOMMAND SORRY.....")
        contm = "NO TELECOMMAND IN THE SATELLITE QUE..."
        cont = pickle.dumps(contm)
        conn.send(cont)
    s.enter(10, 5, telecmd_recv, (s,))                      # calling event scheduler at the 10th second only for the function execution

s.enter(1, 1, telemet_send, (s,))                           # 
s.enter(10, 1, telecmd_recv, (s,))                          #    Function calling on all the side to run the diffrent function 
s.run() 

