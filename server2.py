import socket
import time

addr = socket.getaddrinfo('192.168.1.194', 80)[0][-1]
patch = b"www"
 
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
    print (data)    
    
    data_split = data.split(b'\r\n')
    print(data_split )
    
    #Проверяем то что запрос на сервер адекватный
    if (data == b'') or (data_split[-1] != b'' and data_split[-2] !=b''):
        conn.close()
        continue
    
    file = data_split[0].split(b' ')[1]
    
    conn.send("HTTP/1.1 200 OK\r\n")    
    conn.send("Server: MicroPython-WebServer\r\n")
    conn.send("Content-Type: text/html; charset=UTF-8\r\n")
    conn.send("\r\n")    
    
    try:
        f = open(patch+file)
        conn.send(f.read())
        f.close()
    except:
        print("file not found", patch+file)
         
    
    conn.close()
    # Делаем задержку, чтобы цикл не сильно загружал процессор
    time.sleep(0.1)