import socket

HOST = ''
PORT = 9090

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origin = (HOST, PORT)

udp_server.bind(origin)

while True:
    message, client = udp_server.recvfrom(1024)
    
    print(client, message.decode())