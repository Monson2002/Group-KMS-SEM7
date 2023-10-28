import socket
import threading
import rsa
        

nickname=input("Choose a nickname: ")

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("https://0a75-223-233-81-128.ngrok-free.app",9999))
client.connect(('127.0.0.1',9999))

def receive():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break
        
def write():
    while True:
        message=f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()