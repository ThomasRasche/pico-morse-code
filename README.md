# pico-morse-code
Morse code 'pico' on the Raspberry Pi Pico LED

Prerequesite:
Raspberry Pi Pico, set up to receive MicroPython code via another computer and USB cable.

Short summary of setup (full details and example at: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) 


Enable boot loading (first time use of Pico): 

 - While the BOOTSEL button is pressed, insert USB to computer.
 
 - Use software Thonny Python IDE, and allow MicroPython firmware install.
 
Write MicroPython code with Thonny Python IDE and save and flash across to Pico.




The example files, when flashed to a Raspberry Pi Pico:

main.py   outputs 'pico' in morse code using the Pico LED

morse.py  converts any string (as set within code) of letters/numbers/words you put in, and outputs in morse code using the Pico LED
