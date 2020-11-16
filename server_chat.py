# encoding: utf-8
import sys
import socket
import thread
import datetime

class Server():
    def __init__(self):
        HOST = ''              # Endereco IP do Servidor, no linux, ao não digitar, é definido como localhost        
        PORT = sys.argv[1]     # Porta que o Servidor está (argumento de entrada)
        PORT = int(PORT)       # Casting por entrar como string
        
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do soquete
        orig = (HOST, PORT)     # Encapsulamento do endereço 

        tcp_socket.bind(orig)   # Faz a ligação entre o soquete criado e o endereço fornecido
        tcp_socket.listen(1)    # Fica na escuta da porta
        self.client_list = []   # Lista de clientes para manejar 


        while True:
            connection_socket, client = tcp_socket.accept() # Aceita a conexão quando requisitada
            thread.start_new_thread(self.new_client,(connection_socket, client, tcp_socket)) # Foram usadas threads para as conexões com os clientes. Mas seria melhor usar vários soquetes.



    def new_client(self,connection_socket, client, tcp_socket): #Função que cria as threads
        count = 0           # Variável de controle para guardar nome do cliente (que é sempre a primeira mensagem)
 
        while True:
            current_time = datetime.datetime.now()
            msg = connection_socket.recv(1024)  # Recebe a mensagem/requisição do cliente
            if not msg: break
            print client, msg
            
            if count == 0:      # Atualiza a lista de clientes
                client_info = client[1], msg 
                self.client_list.append((client[1],msg))
                print ("") + str(current_time.hour) + (":") + str(current_time.minute) + ("     ") + str(client_info[1]) + ("      Conectado")
            count = 1
            
            #---------------- Tratamento das mensagens -------------------
            if msg == 'WHO':
                print msg
                connection_socket.send(str(self.client_list)) #Envia a lista de clientes conectados
            
            elif msg == 'HELP':
                print msg
                help_message = 'Comando: SEND <MESSAGE>     Envia <CLIENTS_NAME>:<MESSAGE> para todos os clientes conectados (menos o cliente emissor) \n Comando: SENDTO <CLIENT_NAME> <MESSAGE> Idêntico com SEND, porém envia a mensagem apenas para o cliente especificado pelo <CLIENT_NAME> \n Comando: WHO    Retorna a lista dos clientes conectados ao servidor\n'
                connection_socket.send(help_message) # Envia a mensagem de ajuda
                

            if 'SEND' in msg:
                msg_backup = msg.split(" ", 1)
                print msg_backup
                connection_socket.send('Função não implementada')
            

          
            
        current_time = datetime.datetime.now()
        print '', current_time.hour, ':', current_time.minute, '    ', client_info[1], '   Desconectado.'
        self.client_list.remove((client[1],client_info[1])) # Remove o cliente que fechou a conexão da lista de clientes conectados

        connection_socket.close()       # Fecha a conexão


if __name__ == '__main__':

    Server()
