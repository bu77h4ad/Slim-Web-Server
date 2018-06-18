import socket
import time
from libServ import *

addr = socket.getaddrinfo('192.168.1.194', 80)[0][-1]
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
    
    #Проверяем то что запрос на сервер адекватный
    if (data == b'') or (data_split[-1] != b'' and data_split[-2] !=b''):
        conn.close()
        continue

    method = data_split[0].split(b' ')[0]
    file = str(data_split[0].split(b' ')[1])
    
    print (method)
    if method == b'GET':
        header, body = requestGet (patch= patch, file = file)        
        conn.send(header)
        conn.send(body)

    
    conn.close()
    # Делаем задержку, чтобы цикл не сильно загружал процессор
    time.sleep(0.1)
