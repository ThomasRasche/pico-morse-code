# pico-morse-code
Morse code 'pico' on the Raspberry Pi Pico LED

Prerequesite:
Raspberry Pi Pico, set up to receive MicroPython code.
See https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico
In short summary: 
Enable boot loading (first time use of Pico): 
 - While the BOOTSEL button is pressed, insert USB to computer.
 - Use software Thonny Python IDE, and allow MicroPython firmware install.
Write MicroPython code with Thonny Python IDE and save to Pico; save as main.py on the Pico; this enables it to run when powered up.

Content of main.py:



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
    dash() /n
    dash()

