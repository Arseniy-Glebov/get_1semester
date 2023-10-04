import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10 , 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
GPIO.output(leds, 0)
sleep(2)


while True:
    for j in range(8):

        GPIO.output(leds[j], GPIO.input(aux[j]))

