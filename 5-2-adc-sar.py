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
    bin_res = [0] * 8
    decimal_res = 0
    for i in range(8):
        bin_res[i] = 1
        GPIO.output(dac, bin_res)
        sleep(0.007)
        if GPIO.input(comp) == 0:
            decimal_res += 2 ** (7 - i)
        else:
            bin_res[i] = 0
        GPIO.output(dac, GPIO.LOW)
    return decimal_res


try:
    while True:
        current = adc()
        print("decimal value = ", current, " real value = ", current / 255 * 3.3, " V")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
