from CMNI import network
import time

server = network.Server()
server.Setup(8787)

server.Run()

while True:
    data, addr = server.Recv(ReturnIp = True)
    if data == "ping":
        server.Send(addr, "pong")