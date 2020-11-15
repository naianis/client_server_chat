# encoding: utf-8
import sys
import socket

#SERVER_ADDRESS = '127.0.0.1'     # Endereco IP do Servidor
#print 'Argument List:', str(sys.argv)
#print sys.argv[0], sys.argv[1],sys.argv[2], sys.argv[3]

CLIENT_NAME = sys.argv[1]           # Nome do cliente
SERVER_ADDRESS = sys.argv[2]        # Endereco IP do Servidor
SERVER_PORT = int(sys.argv[3])      # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER_ADDRESS, SERVER_PORT)

tcp.connect(dest)
tcp.send (CLIENT_NAME)

print 'Para sair use CTRL+X\n'
msg = raw_input()

while msg <> '\x18':
    tcp.send (msg)
    
    if msg == 'WHO' or msg == 'HELP':
        #tcp.send (msg)
        server_response = tcp.recv(1024)
        print server_response
        msg = raw_input()

    else:
        print('Mensagem nao suportada. Digite HELP para mais informações.')
        msg = raw_input()





    
tcp.close()
