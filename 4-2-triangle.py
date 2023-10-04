import RPi.GPIO as GPIO
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def dec2bin(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]


try:
    volt = 0
    marker = 1
    sleepTime = float(input("Please, enter the period of your signal")) / 510

    while True:
        sleep(sleepTime)
        GPIO.output(dac, dec2bin(volt))
        if marker == 1 and volt < 255:
            volt += 1
        elif marker == -1 and volt > 0:
            volt -= 1
        else:
            marker *= -1
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
