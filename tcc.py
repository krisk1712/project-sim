import socket
import pickle

def client_program():
    flag = "7E"
    addr = "0A1C3B49"
    cntrl = "5E9E8346"
    preamble = "10101"
    dat_flg = "0A"
    fcs = "2EA6"
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
            tas = "0C1100-0100CC"
            pack_tas = [flag,addr,cntrl,[preamble,dat_flg,tas],fcs,flag]
            sis_proc = pickle.dumps(pack_tas)
            client_socket.send(sis_proc)
            pass
        elif cmd == "spd":
            spd = "0A1105-010C06"
            pack_spd = [flag,addr,cntrl,[preamble,dat_flg,spd],fcs,flag]
            dsp_proc = pickle.dumps(pack_spd)
            client_socket.send(dsp_proc)
            pass
        elif cmd == "ea":
            ea = "0A1105-010A04"
            pack_ea = [flag,addr,cntrl,[preamble,dat_flg,ea],fcs,flag]
            ton_proc = pickle.dumps(pack_ea)
            client_socket.send(ton_proc)
            pass
        elif cmd == "sa":
            sa = "0A1105-010A14"
            pack_sa = [flag,addr,cntrl,[preamble,dat_flg,sa],fcs,flag] 
            ea_proc  = pickle.dumps(pack_sa)
            client_socket.send(ea_proc)
            pass
        elif cmd == "pit":
            pit = "0A2204-010C05"
            pack_pit = [flag,addr,cntrl,[preamble,dat_flg,pit],fcs,flag] 
            sa_proc = pickle.dumps(pack_pit)
            client_socket.send(sa_proc)
            pass
        elif cmd == "sud":
            sud = "0A113F-0000AA"
            pack_sud = [flag,addr,cntrl,[preamble,dat_flg,sud],fcs,flag] 
            t_off_proc   = pickle.dumps(pack_sud)
            client_socket.send(t_off_proc)
            pass
        elif cmd == "ton":
            ton = "0A0001-000004"
            pack_ton = [flag,addr,cntrl,[preamble,dat_flg,ton],fcs,flag] 
            pd_proc  = pickle.dumps(pack_ton)
            client_socket.send(pd_proc)
            pass
        elif cmd == "pon":
            pon = "0A0002-000005"
            pack_pon = [flag,addr,cntrl,[preamble,dat_flg,pon],fcs,flag] 
            oson_proc = pickle.dumps(pack_pon)
            client_socket.send(oson_proc)
            pass
        elif cmd == "sue":
            sue = "0A113F-00009D"
            pack_sue = [flag,addr,cntrl,[preamble,dat_flg,sue],fcs,flag] 
            hk_proc  = pickle.dumps(pack_sue)
            client_socket.send(hk_proc)
            pass
        elif cmd == "thk":
            thk = "0A1100-0A00AA"
            pack_thk = [flag,addr,cntrl,[preamble,dat_flg,thk],fcs,flag] 
            hk_proc  = pickle.dumps(pack_thk)
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


        