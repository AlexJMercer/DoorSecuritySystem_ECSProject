import RPi.GPIO as GPIO
import time

LED_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
