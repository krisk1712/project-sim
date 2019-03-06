import socket
import pickle

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 4448  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("<<------------TELECOMMAND MODULE------------>>")
    print("\n1.THREE AXIS STABLIZE(cmd--> tas)\n2.SOLAR PANEL DEPLOYMENT(cmd--> spd)\n3.EARTH ACQUSITION(cmd--> ea)\n4.SUN ACQUSITION(cmd--> sa)\n5.PCS_INIT_TERM(cmd--> pit)\n6.SS_UPDATE_DISABLE(cmd--> sud)\n7.TRANSMITTER ON(cmd--> ton)\n8.PAYLOAD ON(cmd--> pon)\n9.SS UPDATE ENABLE(cmd-->sue)\n10.TRANSMIT HK(cmd-->thk)\n")
    print("<<------------------------------------------>>")
    cmd = input("ENTER A COMMAND FORM THE MENU: ")
    while cmd.lower().strip() != 'exit':
        if cmd == "tas":
            sis = ["7E","0A1C3B49","5E9E8346",["10101","01","0C1100-0100CC"],"2EA6","7E"]
            sis_proc = pickle.dumps(sis)
            client_socket.send(sis_proc)
            pass
        elif cmd == "spd":
            dsp = ["7E","0FF1B498","1100AE64",["10101","01","0A1105-010C06"],"A13D","7E"]
            dsp_proc = pickle.dumps(dsp)
            client_socket.send(dsp_proc)
            pass
        elif cmd == "ea":
            ton = ["7E","0A1C3B49","5E9E8346",["10101","01","0A1105-010A04"],"2EA6","7E"] 
            ton_proc = pickle.dumps(ton)
            client_socket.send(ton_proc)
            pass
        elif cmd == "sa":
            ea = ["7E","0A1C3B49","1100AE64",["10101","01","0A1105-010A14"],"2EA6","7E"] 
            ea_proc  = pickle.dumps(ea)
            client_socket.send(ea_proc)
            pass
        elif cmd == "pit":
            sa = ["7E","0A1C3B49","1100AE64",["10101","01","0A2204-010C05"],"2EA6","7E"] 
            sa_proc = pickle.dumps(sa)
            client_socket.send(sa_proc)
            pass
        elif cmd == "sud":
            t_off = ["7E","0A1C3B49","1100AE64",["10101","01","0A113F-0000AA"],"2EA6","7E"] 
            t_off_proc   = pickle.dumps(t_off)
            client_socket.send(t_off_proc)
            pass
        elif cmd == "ton":
            pd = ["7E","0A1C3B49","76AE2350",["10101","01","0A0001-000004"],"2EA6","7E"] 
            pd_proc  = pickle.dumps(pd)
            client_socket.send(pd_proc)
            pass
        elif cmd == "pon":
            pon = ["7E","0A1C3B49","1100AE64",["10101","01","0A0002-000005"],"2EA6","7E"] 
            oson_proc = pickle.dumps(pon)
            client_socket.send(oson_proc)
            pass
        elif cmd == "sue":
            hk = ["7E","0A1C3B49","5E9E8346",["10101","01","0A113F-00009D"],"2EA6","7E"] 
            hk_proc  = pickle.dumps(hk)
            client_socket.send(hk_proc)
            pass
        elif cmd == "thk":
            hk = ["7E","0A1C3B49","5E9E8346",["10101","01","0A1100-0A00AA"],"2EA6","7E"] 
            hk_proc  = pickle.dumps(hk)
            client_socket.send(hk_proc)
            pass
        else:
            print("NO SUCH TELE_COMMAND")
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        cmd = input(" -> ")  # again take input
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()


        