# encoding: utf-8
import sys
import socket


CLIENT_NAME = sys.argv[1]           # Nome do cliente
SERVER_ADDRESS = sys.argv[2]        # Endereco IP do Servidor
SERVER_PORT = int(sys.argv[3])      # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criacao do soquete
dest = (SERVER_ADDRESS, SERVER_PORT) # Encapsulamos o endereço fornecido

tcp.connect(dest)                    # Criação da conexão
tcp.send (CLIENT_NAME)               # A primeira mensagem é sempre o nome do cliente

print 'Para sair use CTRL+C\n'
msg = raw_input()                    # Input da mensagem a ser enviada

while msg <> '\x18':                # Loop responsável por enviar e receber mensagens
    tcp.send (msg)                  # Envia a requisição ao servidor
    
    if msg == 'WHO' or msg == 'HELP':
        server_response = tcp.recv(1024)    # Recebe a resposta do servidor. Problema: se não receber, trava.
        print server_response
        msg = raw_input()                   # Input da mensagem a ser enviada

    elif 'SEND' in msg:
        server_response = tcp.recv(1024)    # Recebe a resposta do servidor
        print server_response
        msg = raw_input()                   # Input da mensagem a ser enviada
    

    else:
        print('Mensagem nao suportada. Digite HELP para mais informações.')
        msg = raw_input()


    
tcp.close()         # Fecha a conexão
