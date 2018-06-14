import socket
html = """
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""
addr = socket.getaddrinfo('192.168.4.1', 80)[0][-1]
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(addr)
serv.listen(10)

print('listening on', addr)

while True:
    client_sock, client_addr = serv.accept()
    client_sock_file = client_sock.makefile('rwb', 0)
    line = client_sock_file.readline()
    print ("CLIENT ADDRESS : ",client_addr)
    while True:
        line = client_sock_file.readline()
        if not line or line == b'\r\n':
            break
    client_sock.send("HTTP/1.0 200 OK\r\n")    
    client_sock.send("Content-Type: text/html\r\n")
    client_sock.send("\r\n")
    client_sock.send(html)
    client_sock.close()