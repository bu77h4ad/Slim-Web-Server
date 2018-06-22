import socket
import time
from libSlimWebServ import *

#   Вешаем на текущий адрес машины на 80 порт, прослушку порта
addr = socket.getaddrinfo('192.168.1.194', 80)[0][-1]
#   Каталог - корень для веб сервера
patch = "www\\"
 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(addr)
serversocket.listen(0)

print ('Server is waiting for connections.')
while True:
    try:
        conn, addr = serversocket.accept()
        conn.settimeout(3)
        data = conn.recv(1024)    
    except:
        pass
    
    print ('Connection:', addr)
    print ('------------------------------')
    print ("Request Data from Browser")
    print ('------------------------------')
    #print (data)    
    
    data_split = data.split(b'\r\n')
    print(data_split )
    
    #   Проверяем то что запрос на сервер адекватный
    if (data == b'') or (data_split[-1] != b'' and data_split[-2] !=b''):
        conn.close()
        continue
    #   Берем параметры с запроса клиента
    method = data_split[0].split(b' ')[0]
    link = str(data_split[0].split(b' ')[1])    
    
    if method == b'GET':
        headerHtml, bodyHtml, varHtmlDict = requestGet (patch= patch, link = link)        
        conn.send(headerHtml)   #   Отправляет браузеру заголовок
        conn.send(bodyHtml)     #   Отправляет браузеру тело страницы
        print (varHtmlDict)
        if (varHtmlDict.get('login') == '1'):
            print ("login = ", varHtmlDict.get('login') )
        #   ...
        #   ...
        #   Можно добавить свои переменные 
        #   You may add yours GET date
        #
    conn.close()
    #   Делаем задержку, чтобы цикл не сильно загружал процессор
    time.sleep(0.1)