from CMNI import network
import time

server = network.Server()
server.Setup(8787)
addr = "1.231.123.12.1"
server.Run()

server.Send(123, "test")

while True:
    print(server.Get_Connected())