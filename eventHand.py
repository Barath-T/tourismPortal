from PyQt5 import QtWidgets
import socket
import pickle

PACKAGE = ' '

HEADER = 64
HEADER_SIZE = 16
HEADER_TYPES = ['LOGIN', 'REGISTER', 'BOOK NOW', 'REQUEST', 'DISCONNECT']

PORT = 2020
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

def connectToServer():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    return client

def send(client:socket.socket, msg, type:int):
    message = pickle.dumps(msg)
    print(len(message))
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE-len(send_length))

    send_header = send_length + HEADER_TYPES[type].encode(FORMAT) + (b' ' * ((HEADER-HEADER_SIZE)-len(HEADER_TYPES[type])))

    client.send(send_header)
    client.send(message)

##############################################################################################################################################
def login(username, password, stacked: QtWidgets.QStackedWidget, client:socket.socket):
    try:
        send(client, [username, password], 0)
        if int(client.recv(1).decode(FORMAT)):
            stacked.setCurrentIndex(3)
            return username
        else:
            print('try again!')
    except:
        print('try logging again!')
        stacked.setCurrentIndex(0)
    
    

def signup(username, phone, password, stacked: QtWidgets.QStackedWidget, client:socket.socket):
    try:
        send(client, [username, phone, password], 1)
        stacked.setCurrentIndex(1)
    except Exception as ex:
        print('try registering again')
        stacked.setCurrentIndex(0)
        

def gotoBooking(index:int , stacked:QtWidgets.QStackedWidget):
    PACKAGE = index
    stacked.setCurrentIndex(4)

def book(name, address, count, phone, stacked:QtWidgets.QStackedWidget, client:socket.socket):
    try:
        send(client, [name, address, count, phone, PACKAGE], 2)
        print('Booked!')
        stacked.setCurrentIndex(3)

    except Exception as ex:
        print('tryagain!', ex)
        stacked.setCurrentIndex(3)

def request(source, destination, start, end, count, client:socket.socket):
    try:
        send(client, [source, destination, start, end, count], 3)
        print('Requested!')

    except Exception as ex:
        print('tryagain!', ex)