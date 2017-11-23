# Клиент игры Виселица

import socket

HOST = 'localhost'
PORT = 9999

print('Клиент игры Виселица')
print('Подключение к {}:{}'.format(HOST, PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes("START", 'utf-8'))
received = sock.recv(1024).decode()

data = received.split(';')
if data[0] == 'GUESS':
    print('Попробуйте угадать число от {} до {}'.format(data[1], data[2]))
    while True:
        x = input('Ваш ответ (q - для выхода)')
        if x == 'q':
            break

        sock.sendall(bytes("TRY;{}".format(x), 'utf-8'))    
        received = sock.recv(1024).decode()
        data = received.split(';')
        if data[0] == 'TRUE':
            print('Вы угадали!')
            break
        elif data[0] == 'FAIL':
            print('Вы проиграли!')    
            break
        elif data[0] == 'FALSE':
            if data[2] == '<':
                print('Загаданное число меньше. У Вас осталось попыток: {}'.format(data[1]))
            elif data[2] == '>':
                print('Загаданное число больше. У Вас осталось попыток: {}'.format(data[1]))
        else:
            print('Неизвестный ответ сервера')        
            break

sock.sendall(bytes('GOODBYE', 'utf-8'))
sock.close()
