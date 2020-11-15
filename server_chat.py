# encoding: utf-8
import socket
import thread
import datetime

class Server():
    def __init__(self):
        HOST = ''              # Endereco IP do Servidor
        PORT = 5000            # Porta que o Servidor esta
        self.client_list = []

        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (HOST, PORT)

        tcp_socket.bind(orig)
        tcp_socket.listen(1)


        while True:
            connection_socket, client = tcp_socket.accept()        
            thread.start_new_thread(self.new_client,(connection_socket, client, tcp_socket))



    def new_client(self,connection_socket, client, tcp_socket):
        count = 0  
 
        while True:
            current_time = datetime.datetime.now()
            msg = connection_socket.recv(1024)
            if not msg: break
            print client, msg
            
            if count == 0:      # A primeira mensagem é sempre o nome do cliente.
                client_info = client[1], msg 
                self.client_list.append((client[1],msg))
                print 'client list:::::::', self.client_list
                print ("") + str(current_time.hour) + (":") + str(current_time.minute) + ("     ") + str(client_info[1]) + ("      Conectado")
            count = 1
            
            if msg == 'WHO':
                print msg
                connection_socket.send(str(self.client_list))
            
            elif msg == 'HELP':
                print msg
                help_message = 'Comando: SEND <MESSAGE>     Envia <CLIENTS_NAME>:<MESSAGE> para todos os clientes conectados (menos o cliente emissor) \n Comando: SENDTO <CLIENT_NAME> <MESSAGE> Idêntico com SEND, porém envia a mensagem apenas para o cliente especificado pelo <CLIENT_NAME> \n Comando: WHO    Retorna a lista dos clientes conectados ao servidor\n'
                connection_socket.send(help_message)

            '''
            if 'SEND ' in msg:
                msg_backup = msg
                msg_backup.split()
                print msg_backup[1]
            '''


                


          
            
        current_time = datetime.datetime.now()
        print '', current_time.hour, ':', current_time.minute, '    ', client_info[1], '   Desconectado.'
        self.client_list.remove((client[1],client_info[1]))
        print 'NEW client list:::::::', self.client_list

        connection_socket.close()





if __name__ == '__main__':
    HOST = ''              # Endereco IP do Servidor
    PORT = 5000            # Porta que o Servidor esta
    Server()

    


'''   
    while True:
        msg = connection_socket.recv(1024)
        if not msg: break
        print client, msg

    current_time = datetime.datetime.now()
    print '', current_time.hour, ':', current_time.minute, '    ', client, '   Desconectado.'
    connection_socket.close()
'''