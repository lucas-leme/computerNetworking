import socket

HOST = 'localhost' 
PORT = 9090

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destiny = (HOST, PORT)

message = bytes('Início da comunicação', 'utf-8')

END_VALUE = bytes('termina', 'utf-8')

while message != END_VALUE:
    udp_client.sendto (message, destiny)
    text = input('Insira uma nova messagem')
    message = bytes(text, 'utf-8')
    
udp_client.close()