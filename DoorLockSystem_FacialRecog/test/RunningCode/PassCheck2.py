#for keypad
import RPi.GPIO as GPIO
import time

#for lcd
import digitalio
import board
import adafruit_character_lcd.character_lcd as characterlcd

#Pin setup for keypad
L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
Lock = 21

Password = '6969'

CurrPass = ""

#LCD setup

lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D23)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D8)
lcd_d6 = digitalio.DigitalInOut(board.D7)
lcd_d7 = digitalio.DigitalInOut(board.D1)


lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                       lcd_d7, lcd_columns, lcd_rows)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Lock, GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(Lock, GPIO.HIGH)

#displaying input message
lcd.clear()
lcd.message = "Welcome, \nEnter password:"
time.sleep(3)
lcd.clear()

def check(Code):
    global Password
    if Password == Code:
        lcd.clear()
        lcd.message = 'Khul jaa sim sim'
        GPIO.output(Lock, GPIO.LOW)
        time.sleep(10)
        GPIO.output(Lock, GPIO.HIGH)
        lcd.clear()
    else:
        lcd.clear()
        lcd.message = 'GND MRA'
    

def readLine(line, characters):
    global CurrPass
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
        if characters[0] == '*':
            CurrPass = CurrPass[:-1]
            lcd.clear()
            lcd.message = CurrPass
        elif characters[0] == '#':
            check(CurrPass)
        else:
            CurrPass = CurrPass + characters[0]
            print(CurrPass)        
            lcd.message=CurrPass
       
    if(GPIO.input(C2) == 1):
        print(characters[1])        
        if characters[1] == '*':
            CurrPass = CurrPass[:-1]
            lcd.clear()
            lcd.message = CurrPass
        elif characters[1] == '#':
            check(CurrPass)
        else:
            CurrPass = CurrPass + characters[1]
            print(CurrPass)        
            lcd.message=CurrPass
    if(GPIO.input(C3) == 1):
        print(characters[2])
        if characters[2] == '*':
            CurrPass = CurrPass[:-1]
            lcd.clear()
            lcd.message = CurrPass
        elif characters[2] == '#':
            check(CurrPass)
        else:
            CurrPass = CurrPass + characters[2]
            print(CurrPass)        
            lcd.message=CurrPass
   
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(L1, ["1","2","3"])
        readLine(L2, ["4","5","6"])
        readLine(L3, ["7","8","9"])
        readLine(L4, ["*","0","#"])
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\nApplication stopped!")
    GPIO.cleanup()