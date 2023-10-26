from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
led_2 = Pin(5, Pin.OUT)

while True:
    led.value(not led.value())
    led_2.value(not led_2.value())
    sleep(0.5)
