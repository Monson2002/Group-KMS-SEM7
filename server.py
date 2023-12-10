import threading
import socket
host = '192.168.0.104'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients'connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break
        
# Main function to receive the clients connection
def connection_request ():
    print('Server is running and listening ...')
    while True:
        client, address = server.accept()
        print(f'A connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        server_msg = f'The alias of this client is {alias}'.encode('utf-8')
        print(server_msg.decode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        # client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    connection_request()