# pico-morse-code
Morse code 'pico' on the Raspberry Pi Pico LED

Prerequesite:
Raspberry Pi Pico, set up to receive MicroPython code via another computer and USB to micro USB *data* cable.

Short summary of setup (full details and example at: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) 


Enable boot loading (first time use of Pico): 

 - While the BOOTSEL button is pressed, insert USB to computer.
 
 - Use software Thonny Python IDE, and allow MicroPython firmware install.
 
Write MicroPython code with Thonny Python IDE and save and flash across to Pico.


<br>
<br>

The example files, when flashed to a Raspberry Pi Pico: 

**main.py**   outputs 'pico' in morse code using the Pico LED

**morse.py**  converts any string (as set within code) of letters/numbers/words you put in, and outputs in morse code using the Pico LED. 


<br>
<br>

### Notes:

To make a file run on Pico, plug it into your computer using a **data** cable, then use Thonny software to connect to the Pico and run your file. 

To run your file remotely, i.e. when the Pico is plugged into any battery/power source, you will need to 'Save As' your file from Thonny to the Pico; save it with the filename *main.py* so that it will be read on startup. When you next plug the Pico into power, your file should be running. Therefore, from the above examples, the *morse.py* should be renamed *main.py* when written onto the Pico. 

Problems with the Pico? see https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html which has links to various UF2 files, that can clear the memory etc.



