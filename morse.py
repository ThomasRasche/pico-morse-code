from machine import Pin
import time

led = Pin(25, Pin.OUT)

dictionaryofletters = {       "a": "._",    "b": "_...",  "c": "_._.",  "d": "_..",  "e": ".",
  "f": ".._.",  "g": "__.",   "h": "....",  "i": "..",    "j": ".___",  "k": "_._",  "l": "._..",
  "m": "__",    "n": "_.",    "o": "___",   "p": ".__.",  "q": "__._",  "r": "._.",  "s": "...",
  "t": "_",     "u": ".._",   "v": "..._",  "w": ".__",   "x": "_.._",  "y": "_.__", "z": "__..",
  "0": "_____", "1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....",
  "6": "_....", "7": "__...", "8": "___..", "9": "____.", " ": " "
}

def dot():
    led.value(1)
    time.sleep(0.25)
    led.value(0)
    time.sleep(0.3)
    
def dash():    
    led.value(1)
    time.sleep(0.8)
    led.value(0)
    time.sleep(0.3)
    
def gap():    
    led.value(0)
    time.sleep(0.5)
    
# each letter is converted to set of dots
def todot(dotty): 
    for i in dotty:
        if i == ".":
            dot()
        elif i == "_":
            dash()
        else:
            gap()
    #gap at the end of the word
    time.sleep(1)

# Put your text inside the apostrophies (lower case and numbers, so will match defined letters):
# eg "pico" will create morse: dot dash dash dot - dot dot - dash dot dash dot - dash dash dash
textstring = "pico"

# Code to run through the text
while True:
    time.sleep(1)
    for i in textstring:
        dotstring = dictionaryofletters.get(i)
        todot(dotstring)
    #gap at the end before starting again
    time.sleep(3)        

    

