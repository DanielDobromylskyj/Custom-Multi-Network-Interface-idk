from CMNI import network


def test(server, socket_number):
    print("Test Function Called")
    server.Send(socket_number, "123")
    data = server.Recv(socket_number)
    print("Recved: ", data)


if __name__ == "__main__":
    server = network.Server()
    server.Setup(8776)

    server.Run(test)
