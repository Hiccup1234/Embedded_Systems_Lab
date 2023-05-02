import RPi.GPIO as GPIO
PIR_Input = 29
LED = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_Input, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
while True:
    if GPIO.input(PIR_Input):
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
