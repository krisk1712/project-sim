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

        command = pickle.loads(data)
        print(command)
        print("the packet received")
        send = "The command  has been received"
        client_socket.send(send.encode())
    client_socket.close() 


if __name__ == '__main__':
    client_program()