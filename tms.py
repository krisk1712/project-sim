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


asm = "4EA36B01"
ph = "83EC"
dat1 = "AA55BB66"
dat2 = "1A0E"
fil = "3412"

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
        print("THE ABOVE IS THE READ FILE DATA")
        if pack.strip() == "THREE AXIS STABLIZE":
            sis = "3A326910"
            pack_sis = [asm,ph,[dat1,dat2,sis,fil],fil]
            sis_proc = pickle.dumps(sis)
            conn.send(sis_proc)
            pass
        elif pack.strip() == "SOLAR PANEL DEPLOYMENT":
            dsp = ["4EA36B01","83EC",["AA55BB66","1A0E","8789AC43","0101"],"1212"]
            dsp_proc = pickle.dumps(dsp)
            conn.send(dsp_proc)
            pass
        elif pack.strip() == "EARTH ACQUSITION ":
            ton = ["4EA36B01","83EC",["AA55BB66","1A0E","69984ACD","0101"],"1212"]
            ton_proc = pickle.dumps(ton)
            conn.send(ton_proc)
            pass
        elif pack.strip() == "SUN ACQUSITION":
            ea = ["4EA36B01","83EC",["AA55BB66","1A0E","ACD1437DF","0101"],"1212"] 
            ea_proc  = pickle.dumps(ea)
            conn.send(ea_proc)
            pass
        elif pack.strip() == "PCS_INIT_TERM":
            sa = ["4EA36B01","83EC",["AA55BB66","1A0E","0A010ECD","0101"],"1212"] 
            sa_proc = pickle.dumps(sa)
            conn.send(sa_proc)
            pass
        elif pack.strip() == "SS_UPDATE_DISABLE":
            t_off = ["4EA36B01","83EC",["AA55BB66","1A0E","ADCFE1235","0101"],"1212"]  
            t_off_proc   = pickle.dumps(t_off)
            conn.send(t_off_proc)
            pass
        elif pack.strip() == "TRANSMITTER ON":
            pd = ["4EA36B01","83EC",["AA55BB66","1A0E","987ADC34","0101"],"1212"] 
            pd_proc  = pickle.dumps(pd)
            conn.send(pd_proc)
            pass
        elif pack.strip() == "PAYLOAD ON":
            oson = ["4EA36B01","9A7D",["AA55BB66","1A0E","0A14CD13","0101"],"1212"]
            oson_proc = pickle.dumps(oson)
            conn.send(oson_proc)
            pass
        elif pack.strip() == "SS UPDATE ENABLE":
            hk = ["4EA36B01","83EC",["AA55BB66","1A0E","876ADEF5","0101"],"1212"] 
            hk_proc  = pickle.dumps(hk)
            conn.send(hk_proc)
            pass
        elif pack.strip() == "TRANSMIT HK":
            hk = ["4EA36B01","83EC",["AA55BB66","1A0E","68AECD120","0101"],"1212"] 
            hk_proc  = pickle.dumps(hk)
            conn.send(hk_proc)
            pass
        else:
            print("NO SUCH TELE_COMMAND")
            pass       
        red = red + 2
    except IndexError:
        print("NO TELECOMMAND SORRY.....")
        contm = "notm"
        cont = pickle.dumps(contm)
        conn.send(cont)
    s.enter(10, 3, telecmd_recv, (s,))                      # calling event scheduler at the 10th second only for the function execution

s.enter(1, 1, telemet_send, (s,))                           # 
s.enter(10, 3, telecmd_recv, (s,))                          #    Function calling on all the side to run the diffrent function 
s.run() 

