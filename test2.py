from CMNI import network
import time

client = network.Client()
client.Setup("192.168.137.1", 8787)

client.Connect()
