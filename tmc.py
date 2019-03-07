import socket
import pickle
from PIL import Image
import numpy


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
        if cmd == 'notm':
            print("NO TELECOMMAND PROSSED DATA OVER SASTELLITE...........")
            continue
        elif  cmd[2][2]=="3A326910":
            tas = "THREE AXIS STABLIZE"
            print("The Command has been received from the ground station...TAS")
            mess = "--->>Received Telemetry THREE AXIS STABLIZE <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="8789AC43":
            spd = "SOLAR PANEL DEPLOYMENT"

            print("The Command has been received from the ground station... SPD")
            mess = "--->>Received Telemetry SOLAR PANEL DEPLOYMENT <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="69984ACD":
            ea = "EARTH ACQUSITION "
            print("The Command has been received from the ground station...EA")
            mess = "--->>Received Telemetry EARTH ACQUSITION <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="ACD1437DF":
            sa = "SUN ACQUSITION"
            print("The Command has been received from the ground station...SA")
            mess = "--->>Received Telemetry SUN ACQUSITION <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="0A010ECD":
            pit = "PCS_INIT_TERM"

            print("The Command has been received from the ground station...PIT")
            mess = "--->>Received Telemetry PCS_INIT_TERM <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="ADCFE1235":
            sud = "SS_UPDATE_DISABLE"

            print("The Command has been received from the ground station...SUD")
            mess = "--->>Received Telemetry SS_UPDATE_DISABLE <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="987ADC344":
            ton = "TRANSMITTER ON"

            print("The Command has been received from the ground station...TON")
            mess = "--->>Received Telemetry TRANSMITTER ON <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="0A14CD13":
            opon = "PAYLOAD ON"

            print("The Command has been received from the ground station...OPON")
            img = Image.open("./earth.jpg")
            print("READING IMAGE FROM THE SATELLITE...")
            arr = numpy.array(img)
            print("CONVERTING ARRAY BACK TO IMAGE...")
            img1 = Image.fromarray(arr)
            print("Image converted....")
            img1.show()
            print("PAYLAOD ACK")
            #NOT WORKING THEN
            # img.show()
            mess = "--->>Received Telemetry ORIGAMI PAYLOAD ON <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="876ADEF5":
            sue = "SS UPDATE ENABLE"

            print("The Command has been received from the ground station...SUE")
            mess = "--->>Received Telemetry SS UPDATE ENABLE <<---"
            client_socket.send(mess.encode())
            pass

        elif cmd[2][2] =="68AECD120":
            thk = "TRANSMIT HK"

            print("The Command has been received from the ground station...THK")
            mess = "--->>Received Telemetry TRANSMIT HK <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="AFFEC34A":
            thk = "SAT STAT"

            print("The status of the satellite...SATSTAT")
            mess = "--->>Received Telemetry SAT STAT <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="BA53A980":
            thk = "BAT STAT"

            print("The status of the satellite...BATSTAT")
            mess = "--->>Received Telemetry BAT STAT <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="231876A7":
            thk = "HLTH"

            print("The status of the satellite...HLTH")
            mess = "--->>Received Telemetry HLTH <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] =="C4579850":
            thk = "CHRG"

            print("The status of the satellite...CHRG")
            mess = "--->>Received Telemetry CHRG <<---"
            client_socket.send(mess.encode())
            pass
        elif cmd[2][2] == "00000000":
            null = "00000000"
            print("Null packets for conn estab.....")
            mess = "-->> NUL PACKETS <<--"
            client_socket.send(mess.encode())
            pass
        else:
            print("NO COMMAND TO BE RECOG BY THE SAT.....")
            break
    client_socket.close() 


if __name__ == '__main__':
    client_program()
