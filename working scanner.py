import threading  # Подключаем модуль threading для работы с потоками
import socket  # Подключаем модуль socket для работы с сокетами (интерфейс для обеспечения обмена данными между процессами)

target = input('Enter host:\n\n')  # Ввод хоста для сканирования


def portscan(port):  # Создаём функцию сканирования портов

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём сокет
    s.settimeout(0.5)   # Выставляем таймаут

    try:
        connection = s.connect((target, port))  # Пытаемся приконнектиться к хосту
        print('Port :', port, "is open.")   # В случае соединения, пишем что порт открыт
        connection.close()   # Закрываем соединение
    except:
        pass   # Оператор-заглушка, в случае отсутствия соединения, ничего не выполняем


ports = [] # Список портов
for i in range(6000):
    ports.append(i)

for element in ports:   # Перебор в цикле портов
    t = threading.Thread(target=portscan, kwargs={'port': element})  # Создаём поток

    t.start()   # Запуск потока

input()