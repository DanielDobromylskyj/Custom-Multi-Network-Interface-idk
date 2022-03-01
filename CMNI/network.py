import time
import socket
import threading
import sys



class Server():
    def __init__(self):
        pass


    def Setup(self, port):

        self.Close = False
        self.CONNECTIONLIST = []
        self.PORT = port
        self.HOST = socket.gethostbyname(socket.gethostname())

        print("Setup Complete | Host:", self.HOST, ", On Port", self.PORT)

        self.send = False
        self.recv = False
        self.send_data = []
        self.recv_data = []

        self.connections = [] # (addr, conn)
        self.Binded = False





    def Run(self, functionname):
        if self.Binded == False:
            func = functionname
            functionname = str(functionname).split(" ")
            functionname = functionname[1]

            filename = sys.argv[0]
            filename = filename.split("/")
            filename = filename[filename.__len__() - 1]
            filename = filename.split(".")

            x = threading.Thread(target=self.Init_Network_Thread, args=[functionname, filename[0], func])
            x.start()
            self.Binded = True
            time.sleep(1)
        else:
            print("Script Already Binded")

    def Shutdown(self):
        self.s.close()
        self.Close = True

    def Send(self, socketNO , message, encoding_type = "utf-8"):       # Add Encoding / Encryption
        conn = self.CONNECTIONLIST[int(socketNO)]
        conn.sendall(message.encode(encoding_type))

    def Recv(self, socketNO, encoding_type = "utf-8", buffersize = 1024):
        conn = self.CONNECTIONLIST[int(socketNO)]
        binary = conn.recv(buffersize)
        message = binary.decode(encoding_type)
        return message

    def Get_Connected(self):
        return self.connections


    def Init_Network_Thread(self, function, file_name, func):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))

        while True:
            try:
                if self.Close == True:
                    break

                self.s.listen()
                conn, addr = self.s.accept()
                self.connections.append((addr, conn))
                self.CONNECTIONLIST.append(conn)


                try:
                    try:
                        exec("from " + file_name + " import " + function)
                    except SyntaxError:
                        pass


                    socket_number = self.CONNECTIONLIST.__len__() - 1
                    client = threading.Thread(target=func, args=[self, socket_number])
                    client.start()

                except Exception as e:
                    print("Function Call Error: ", e)


                #eval(function + "()")


            except Exception as e:
                print(e)




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
            time.sleep(1)
        else:
            print("Script Already Binded")

    def Send(self, message, encoding_type = "utf-8"): # Add Encoding / Encryption
        binary = message.encode(encoding_type)
        self.s.sendall(binary)

    def Recv(self, ReturnIp = False, encoding_type = "utf-8", buffersize = 1024):
        binary = self.s.recv(1024)# buffersize
        message = binary.decode(encoding_type)
        if ReturnIp == False:
            return message
        elif ReturnIp == True:
            return message


    def Init_Network_Thread(self, Print = True):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            if self.connected == False:
                self.s.connect((self.Client_HOST, self.Client_PORT))
                self.connected = True
                print("Connection Made")
