import socket
import threading
import pickle
import time

from datas import users, bookings, packageRequests


HEADER = 64
HEADER_SIZE = 16
HEADER_TYPES = ['LOGIN', 'REGISTER', 'BOOK NOW', 'REQUEST', 'DISCONNECT']

PORT = 2020
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    CURRENT_USER = ' '
    print(f"New connection: {addr}")
    
    connected = True

    while connected:
        msg_header = conn.recv(HEADER)
        if msg_header:
            msg_length = int(msg_header[:HEADER_SIZE].decode(FORMAT))
            msg_type = msg_header[HEADER_SIZE:].decode(FORMAT).rstrip()

            if msg_type == HEADER_TYPES[-1]:
                connected = False

            elif str(msg_type) == HEADER_TYPES[0]:
                msg = conn.recv(msg_length)
                msg = pickle.loads(msg)

                matched = '0'
                for user in users:
                    if (user['username'] == msg[0]) and (user['password'] == msg[1]):
                        matched = '1'
                        CURRENT_USER = msg[0]
                        break
                    
                conn.send(matched.encode(FORMAT))
                
            elif msg_type == HEADER_TYPES[1]:
                msg = conn.recv(msg_length)
                msg = pickle.loads(msg)

                users.append(
                    {
                    'username': msg[0],
                    'phone': msg[1],
                    'password': msg[2]
                    }
                )
                
            elif msg_type == HEADER_TYPES[2]:
                
               
                msg = conn.recv(msg_length)
                msg = pickle.loads(msg)
                bookings.append(
                    {
                        'Package': msg[4],
                        'user': CURRENT_USER,
                        'name': msg[0],
                        'address': msg[1],
                        'count': msg[2],
                        'phone': msg[3],
                    }
                )
                print(bookings)

            elif msg_type == HEADER_TYPES[3]:
                msg = conn.recv(msg_length)
                msg = pickle.loads(msg)
                packageRequests.append(
                    {
                        'source': msg[0],
                        'destination': msg[1],
                        'start': msg[2],
                        'end': msg[3],
                        'count': msg[4],
                    }
                )
                print(packageRequests)

            else:
                pass


            

    conn.close()
def start():
    server.listen()
    print(f"Listening on {SERVER}")
    while True:
        conn, addr =server.accept()

        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        
        print(f"Active connections: {threading.active_count()-1}")

print("Starting server...")
start()