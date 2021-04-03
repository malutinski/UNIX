#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
print('Запуск сервера.')
sock.bind(('', 9091))
print('Начало прослушивания порта.')
sock.listen(1)
conn, addr = sock.accept()
print('Подключение клиента и прием данных от клиента.')
print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print('Отправка данных клиенту.')
    conn.send(data.upper())
print('Остановка сервера.')
conn.close()