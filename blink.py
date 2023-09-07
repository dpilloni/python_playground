from machine import Pin, ADC
from time import sleep
from gpio_lcd import GpioLcd

class Board:
    running = "on"
    button1 = "up"
    button2 = "up"
    speed = 0
    
#Buttons
btn1 = Pin(4, Pin.IN)
btn2 = Pin(0, Pin.IN)

#LEDS
led1 = Pin(26, Pin.OUT) 
led2 = Pin(12, Pin.OUT) 
led3 = Pin(13, Pin.OUT)

#Init
c =  0
pot = ADC(Pin(34))
led3.on()
led1.on()    
Board.button1 == "up"
Board.button2 == "up"

def lcd_board():

    lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                  d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22),
                  num_lines=4, num_columns=20)
    lcd.clear()
    lcd.putstr("BLINKY PRG")

    lcd.move_to(0, 1)
    lcd.putstr("SPEED: " + str(Board.speed))

    lcd.move_to(0, 2)
    lcd.putstr("STATUS: " + Board.running)


Board.speed = pot.read() 
lcd_board()

while True:
    t = pot.read()
    if int(t/200) != int(Board.speed/200):
        Board.speed = t
        lcd_board()
        
    if btn1.value() == 0 and Board.button1 == "up":
        Board.button1 = "down"
        Board.button2 = "up"
        Board.running = "off"
        lcd_board()    

    if btn2.value() == 0 and Board.button2 == "up":
        Board.button2 = "down"
        Board.button1 = "up"
        Board.running = "on"
        lcd_board()    

    if Board.running == "on":
        c = c + 1

    if c < t:
        led1.on()
        led2.on()
        led3.off()    

    if c >= t:
        led1.off()
        led2.off()
        led3.off()    

    if c >= (t * 2):
        led1.off()
        led2.on()
        led3.on()    

    if c >= (t * 3):
        c = 0
 