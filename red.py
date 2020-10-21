import main as red
import socket
import threading

RED_SENT_PORT = 5050
RED_RECEIVE_PORT = 4040
RED_RECEIVE =  socket.gethostbyname(socket.gethostname())
RED_SEND = "192.168.0.114"
RED_SEND_ADDR = (RED_SEND,RED_SENT_PORT)
RED_RECEIVE_ADDR = (RED_RECEIVE,RED_RECEIVE_PORT)
red_connect = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
red_send = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def Handle_Requests(conn,adr):
    while True:
        message = conn.recv(100).decode()
        if len(message)==1:
            col = int(message)
            red.board[col][red.row[col]] = 2
            red.row[col]-=1
            red.turn = True
def establish_connection():
    global red_connect,red_send
    print("Wating for player")
    red_connect.bind(RED_RECEIVE_ADDR)
    red_connect.listen()
    (conn,addr) = red_connect.accept()
    red_send.connect(RED_SEND_ADDR)
    t = threading.Thread(target=Handle_Requests, args=(conn, addr))
    t.start()
establish_connection()
print("CONNECTED")
red.turn = True
red.game(0,red_send)