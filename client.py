import socket
import threading
import os

HEADER  = 64
PORT = 5050
cmd = 'curl ifconfig.me'
SERVER=os.system(cmd)

hostname=socket.gethostname()
FORMAT ='utf-8'
ADDR = (SERVER,PORT)
DISCONNECT_message="!Disconnect"

# # setup socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


    
    
print("Client side testing")
    
    

