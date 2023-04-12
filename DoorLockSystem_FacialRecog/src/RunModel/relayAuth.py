import RPi.GPIO as GPIO
import time

import digitalio
import board
import adafruit_character_lcd.character_lcd as characterlcd

# LCD setup
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


relay_pin = 21


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.HIGH)


class relay:
    def authenticator(faceAuth, auth_token, safe):
        if faceAuth and auth_token:
            lcd.clear()
            lcd.message = "Welcome !!\nDoor Opened !!"
            GPIO.output(relay_pin, GPIO.LOW)
            time.sleep(5)
            GPIO.output(relay_pin, GPIO.HIGH)
            lcd.clear()

        if safe == True:
            lcd.clear()
            lcd.message = 'Door Opened.'
            GPIO.output(relay_pin, GPIO.LOW)
            time.sleep(5)
            GPIO.output(relay_pin, GPIO.HIGH)
            lcd.clear()
            time.sleep(1)