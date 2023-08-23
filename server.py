import socket
import threading
import os

HEADER  = 64
PORT = 5050
hostname=socket.gethostname()
FORMAT ='utf-8'

#cmd = 'curl ifconfig.me'
cmd = "ls -l"
#cmd = 'echo "$(curl ifconfig.me)"'
SERVER=os.system(cmd)


import os

#p = os.popen('curl ifconfig.me')

#zero=float(p.read())
import uuid
 
# printing the value of unique MAC
# address using uuid and getnode() function
print(hex(uuid.getnode()))
#converted = float(zero.strip('.%'))

#SERVER=socket.gethostbyname(hostname)

ADDR = (SERVER,PORT)
DISCONNECT_message="!Disconnect"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(server)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f" [new connection] {addr} connected ")
    connected = True
    
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg  == DISCONNECT_message:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()
        
        


def start():
    server.listen()
    print(f"[Listening] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,
                                  args=(conn,addr))
        thread.start()
        print(f"[threading is active] {threading.active_count() - 1}")
        

print('sever is starting....]')
start()