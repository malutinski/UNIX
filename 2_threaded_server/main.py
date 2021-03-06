import socket
import threading

sock = socket.socket()
print('Сервер запущен.', file=open('log.txt','a'))

while True:
    try:
        port = 9090
        sock.bind(('', port))
        break
    except:
        port += 1

sock.listen(5)

def go(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Отправка данных клиенту.',file=open('log.txt','a'))
        conn.send(data.upper())
    
    conn.close()
        

while True:
    conn, addr = sock.accept()
    th = threading.Thread(target=go, args=(conn, addr))
    th.start()

    