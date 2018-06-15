import time
import socket

html = """
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP32</h1>
        <p style="width: 100px;">%s</p>
    </body>
</html>
"""
addr = socket.getaddrinfo('192.168.1.194', 80)[0][-1]
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(addr)
serv.listen(0)

print('listening on', addr)

while True:
    try:
        client_sock, client_addr = serv.accept()    
        client_sock_file = client_sock.makefile('rwb', 0)
        client_sock.settimeout(3)
        line = client_sock_file.readline()
        print ("CLIENT ADDRESS : ",client_addr) 
        while True:
            line = client_sock_file.readline()
            print ("Client Resive ->", line)
            if line == b'' or line == b'\r\n':
                break
        client_sock.send("HTTP/1.1 200 OK\r\n")    
        client_sock.send("Server: MicroPython-WebServer\r\n")
        client_sock.send("Content-Type: text/html; charset=UTF-8\r\n")
        client_sock.send("\r\n")
        f = open('cover.txt')
        cover = f.read()
        f.close()
    
        client_sock.send(html % (cover) )              
    
    except KeyboardInterrupt:
        break
    
    except :
        print('ERROR!')

    finally:
        client_sock.close() 
        time.sleep(0.1)
