from CMNI import network

client = network.Client()
client.Setup("IP", 8787)

client.Connect()
data = client.Recv()
print("Recved: ", data)

client.Send("321")
