import time
import socket
import threading



class Server():
    def __init__(self):
        self.Close = False


    def Setup(self, port):
        self.PORT = port
        self.HOST = socket.gethostbyname(socket.gethostname())

        self.connections = [] # (addr, conn)
        self.Binded = False

        print("Setup Complete | Host:", self.HOST, ", On Port", self.PORT)

    def Run(self):
        if self.Binded == False:
            x = threading.Thread(target=self.Init_Network_Thread)
            x.start()
            self.Binded = True
        else:
            print("Script Already Binded")

    def Shutdown(self):
        self.s.close()

    def GetConnected(self):
        return self.connections

    def Send(self, addr, message, encoding_type = "utf-8"): # Add Encoding / Encryption
        binary = message.encode(encoding_type)
        self.s.sendto(binary, addr)

    def Recv(self, ReturnIp = False, encoding_type = "utf-8", buffersize = 1024):
        binary= self.s.recv(buffersize)
        message = binary.decode(encoding_type)
        if ReturnIp == False:
            return message
        elif ReturnIp == True:
            return message


    def Init_Network_Thread(self, Print = True):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
                self.s.bind((self.HOST, self.PORT))
                self.s.listen()
                conn, addr = self.s.accept()
                self.connections.append((addr, conn))
                if Print == True:
                    print("Connection From: ", addr)


class Client():
    def __init__(self):
        self.connected = False

    def Setup(self, ip, port):
        self.Client_PORT = port
        self.Client_HOST = ip

        self.Binded = False

        print("Setup Complete | Host:", self.Client_HOST, ", On Port", self.Client_PORT)

    def Connect(self):
        if self.Binded == False:
            x = threading.Thread(target=self.Init_Network_Thread)
            x.start()
            self.Binded = True
        else:
            print("Script Already Binded")

    def Send(self, message, encoding_type = "utf-8"): # Add Encoding / Encryption
        binary = message.encode(encoding_type)
        self.s.sendto(binary, (self.Client_HOST, self.Client_PORT))

    def Recv(self, ReturnIp = False, encoding_type = "utf-8", buffersize = 1024):
        binary, addr = self.s.recvfrom(buffersize)
        print(addr)
        message = binary.decode(encoding_type)
        if ReturnIp == False:
            return message
        elif ReturnIp == True:
            return message, addr


    def Init_Network_Thread(self, Print = True):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
                if self.connected == False:
                    self.s.connect((self.Client_HOST, self.Client_PORT))
                    self.connected = True
                    print("Conn Made")
                    time.sleep(0.5)

                # Loop



