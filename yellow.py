import main as yellow
import socket
import threading

YELLOW_SENT_PORT = 4040
YELLOW_RECEIVE_PORT = 5050
YELLOW_RECEIVE =  socket.gethostbyname(socket.gethostname())
YELLOW_SEND = "192.168.0.114"
YELLOW_SEND_ADDR = (YELLOW_SEND,YELLOW_SENT_PORT)
YELLOW_RECEIVE_ADDR = (YELLOW_RECEIVE,YELLOW_RECEIVE_PORT)
yellow_send = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
yellow_connect = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def Handle_Requests(conn,addr):
    while True:
        message = conn.recv(100).decode()
        if len(message)==1:
            col = int(message)
            yellow.board[col][yellow.row[col]] = 1
            yellow.row[col]-=1
            yellow.turn = True
def establish_connection():
    global yellow_send,yellow_connect
    yellow_send.connect(YELLOW_SEND_ADDR)
    yellow_connect.bind(YELLOW_RECEIVE_ADDR)
    yellow_connect.listen()
    (conn,addr) = yellow_connect.accept()
    t = threading.Thread(target=Handle_Requests,args=(conn,addr))
    t.start()
establish_connection()
print("CONNECTED")
yellow.turn = False
yellow.game(1,yellow_send)