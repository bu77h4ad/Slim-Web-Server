# Slim Web Server on MicroPython for ESP32

Легкий веб сервер для ESP-32. 
---
Написан на MicroPython 1.9.4. В коде нет ООП специально, дабы обеспечить меньше занимаемой памяти в контроллере. Код работает и на Python 3.6 без изменений.

* По умолчанию выводит страницы с каталога "www".
* Умеет работать только с GET запросами.

**Пример запуска для MicroPython 1.9.4**
 
```python
import server2
```
**Пример запуска для Python 3.6**
```python
python server2.py
```
**Настройка**
```python
addr = socket.getaddrinfo('192.168.1.194', 80)[0][-1]
patch = "www\\"
```
http://micropython.org/download#esp32

<img align="left" width="50%" height="50%" src="cover.png">
<img align="left" width="50%" height="50%" src="image.png">
