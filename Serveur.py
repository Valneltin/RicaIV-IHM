import socket
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 12345))

socket.listen(5)
client, address = socket.accept()
print("{} connected".format(address))

while True:
        time.sleep(1.5)
        client.send(b"JOY_0,2_1")
        time.sleep(1.5)
        client.send(b"LT_0,3")
        time.sleep(1.5)
        response = client.recv(255)
        if response != "":
                print(response)

print("Close")
client.close()
stock.close()
