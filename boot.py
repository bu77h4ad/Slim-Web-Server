# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import network 
# вариант 1, микроконтроллер подключается к WI FI и на ИП адресе вешает веб сервер
#sta_if = network.WLAN(network.STA_IF); 
#sta_if.active(True) 
#print(sta_if.scan())
#sta_if.connect("ASUS", "1234567890") # Connect to an AP 
#sta_if.isconnected() # Check for successful connection

# вариант 2, микроконтроллер как точка доступа 192.168.4.1
ap = network.WLAN(network.AP_IF) 
ap.active(True) 
ap.config(essid='ESP32')
ap.config(authmode=3, password='12345678')

#import webrepl
#webrepl.start()

#import machine
#machine.freq() # get the current frequency of the CPU
#machine.freq(160000000) # set the CPU frequency to 160 MHz

