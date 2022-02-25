from CMNI import network
import time

client = network.Client()
client.Setup("IP", 8787)

client.Connect()
data = client.Recv()
print(data)

client.Send("321")
