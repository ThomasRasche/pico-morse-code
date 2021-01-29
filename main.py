from machine import Pin
import time

led = Pin(25, Pin.OUT)

def dot():
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.5)
    
def dash():    
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(0.5)
    
while True:
    time.sleep(1.5)
    dot()  #p
    dash()
    dash()
    dot()
    time.sleep(0.7)
    dot()  #i
    dot()
    time.sleep(0.7)
    dash() #c
    dot()
    dash()
    dot()
    time.sleep(0.7)
    dash() #o
    dash()
    dash()
    


        
    