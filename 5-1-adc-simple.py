import RPi.GPIO as GPIO
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troykaV = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troykaV, GPIO.OUT, initial=GPIO.HIGH)



def dec2bin(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]


def adc():
    comp_inp = 0
    step = 0
    while comp_inp != 1 and step != 256:
        GPIO.output(dac, dec2bin(step))
        sleep(0.007)
        if GPIO.input(comp) == 1:
            return step
        step += 1
    return 255


try:
    while True:
        current = adc()
        print("decimal value = ", current, " real value = ", current / 255 * 3.3, " V")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
