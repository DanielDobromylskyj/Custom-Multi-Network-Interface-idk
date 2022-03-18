from CMNI import network

client = network.Client()
client.Setup("192.168.137.1", 8776)

client.Connect()
data = client.Recv()
print("Recved: ", data)

client.Send("321")
