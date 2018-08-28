# Slim Web Server on MicroPython for ESP32

Легкий веб сервер для ESP-32. 
---
Написан на MicroPython 1.9.4. Легкий и простой веб сервер. В коде нет ООП специально, дабы обеспечить меньше занимаемой памяти в контроллере. Исходники работает и на Python 3.6 без изменений.

* По умолчанию выводит страницы с каталога "www".
* Умеет работать только с GET запросами.

**Пример запуска для MicroPython 1.9.4**
 
```python
import slimWebServ
```
**Пример запуска для Python 3.6**
```python
python slimWebServ.py
```
**Настройка**
```python
addr = socket.getaddrinfo('192.168.1.194', 80)[0][-1]
patch = "www\\"
```
http://micropython.org/download#esp32

<img align="left" src="cover.png">
<img align="left" src="image.png">

инструкция
http://andreyapanasenko.ru/prostoy-web-server-na-python
