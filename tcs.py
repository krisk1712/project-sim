import socket
import pickle


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 4448  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    a = 0
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024)
        if not data:
            # if data is not received break
            break
        
        cmd = pickle.loads(data)
        tcdb = open("tmdb.txt",'a')
        tcdb.write(str(a) + "\n")
        if   cmd[3][2]=="0C1100-0100CC":
            tas = "THREE AXIS STABLIZE"
            print("The Command has been received from the ground station...TAS")
            tcdb.write(tas + "\n")
            mess = "--->>Received command THREE AXIS STABLIZE <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A1105-010C06":
            spd = "SOLAR PANEL DEPLOYMENT"

            print("The Command has been received from the ground station... SPD")
            tcdb.write(spd + "\n")

            mess = "--->>Received command SOLAR PANEL DEPLOYMENT <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A1105-010A04":
            ea = "EARTH ACQUSITION "

            print("The Command has been received from the ground station...EA")
            tcdb.write(ea + "\n")

            mess = "--->>Received command EARTH ACQUSITION <<---"
            conn.send(mess.encode())
            pass
        elif cmd[3][2] =="0A1105-010A14":
            sa = "SUN ACQUSITION"

            print("The Command has been received from the ground station...SA")
            tcdb.write(sa + "\n")

            mess = "--->>Received command SUN ACQUSITION <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A2204-010C05":
            pit = "PCS_INIT_TERM"

            print("The Command has been received from the ground station...PIT")
            tcdb.write(pit + "\n")
            mess = "--->>Received command PCS_INIT_TERM <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A113F-0000AA":
            sud = "SS_UPDATE_DISABLE"

            print("The Command has been received from the ground station...SUD")
            tcdb.write(sud + "\n")
            mess = "--->>Received command SS_UPDATE_DISABLE <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A0001-000004":
            ton = "TRANSMITTER ON"

            print("The Command has been received from the ground station...TON")
            tcdb.write(ton + "\n")
            mess = "--->>Received command TRANSMITTER ON <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A0002-000005":
            opon = "PAYLOAD ON"

            print("The Command has been received from the ground station...OPON")
            tcdb.write(opon + "\n")
            mess = "--->>Received command PAYLOAD ON <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A113F-00009D":
            sue = "SS UPDATE ENABLE"

            print("The Command has been received from the ground station...SUE")
            tcdb.write(sue + "\n")
            mess = "--->>Received command SS UPDATE ENABLE <<---"
            conn.send(mess.encode())
            pass

        elif cmd[3][2] =="0A1100-0A00AA":
            thk = "TRANSMIT HK"

            print("The Command has been received from the ground station...THK")
            tcdb.write(thk + "\n")
            mess = "--->>Received command TRANSMIT HK <<---"
            conn.send(mess.encode())
            pass

        else:
            print("NO COMMAND TO BE RECOG BY THE SAT.....")
            pass
        a = a + 1
    tcdb.close()    
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()

