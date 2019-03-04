import socket
import pickle


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5555  
    client_socket = socket.socket() 
    client_socket.connect((host, port))  
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # print("from connected user: " + str(data))
        cmd = pickle.loads(data)
        # if cmd == 'notm':
        #     print("NO TELECOMMAND PROSSED DATA OVER SASTELLITE...........")
        #     continue
        if  cmd[2][2]=="3A326910":
            tas = "THREE AXIS STABLIZE"
            print("The Command has been received from the ground station...TAS")
            mess = "--->>Received command THREE AXIS STABLIZE <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="8789AC43":
            spd = "SOLAR PANEL DEPLOYMENT"

            print("The Command has been received from the ground station... SPD")
            mess = "--->>Received command SOLAR PANEL DEPLOYMENT <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="69984ACD":
            ea = "EARTH ACQUSITION "
            print("The Command has been received from the ground station...EA")
            mess = "--->>Received command EARTH ACQUSITION <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="ACD1437DF":
            sa = "SUN ACQUSITION"
            print("The Command has been received from the ground station...SA")
            mess = "--->>Received command SUN ACQUSITION <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="0A010ECD":
            pit = "PCS_INIT_TERM"

            print("The Command has been received from the ground station...PIT")
            mess = "--->>Received command PCS_INIT_TERM <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="ADCFE1235":
            sud = "SS_UPDATE_DISABLE"

            print("The Command has been received from the ground station...SUD")
            mess = "--->>Received command SS_UPDATE_DISABLE <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="987ADC344":
            ton = "TRANSMITTER ON"

            print("The Command has been received from the ground station...TON")
            mess = "--->>Received command TRANSMITTER ON <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="0A14CD13":
            opon = "ORIGAMI PAYLOAD ON"

            print("The Command has been received from the ground station...OPON")
            mess = "--->>Received command ORIGAMI PAYLOAD ON <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="76AC1340":
            opoff = "ORIGAMI PAYLOAD OFF"

            print("The Command has been received from the ground station...OPOFFF")
            mess = "--->>Received command ORIGAMI PAYLOAD OFF <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="876ADEF5":
            sue = "SS UPDATE ENABLE"

            print("The Command has been received from the ground station...SUE")
            mess = "--->>Received command SS UPDATE ENABLE <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="68AECD120":
            thk = "TRANSMIT HK"

            print("The Command has been received from the ground station...THK")
            mess = "--->>Received command TRANSMIT HK <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="AFFEC34A":
            thk = "SAT STAT"

            print("The Command has been received from the ground station...SATSTAT")
            mess = "--->>Received command SAT STAT <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="BA53A980":
            thk = "BAT STAT"

            print("The Command has been received from the ground station...BATSTAT")
            mess = "--->>Received command BAT STAT <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="231876A7":
            thk = "HLTH"

            print("The Command has been received from the ground station...HLTH")
            mess = "--->>Received command HLTH <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="C4579850":
            thk = "CHRG"

            print("The Command has been received from the ground station...CHRG")
            mess = "--->>Received command CHRG <<---"
            client_socket.send(mess.encode())
            pass
        else:
            print("NO COMMAND TO BE RECOG BY THE SAT.....")
            break
    client_socket.close() 


if __name__ == '__main__':
    client_program()