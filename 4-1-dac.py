import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
allowed = [str(elem) for elem in range(0, 256)]


def dec2bin(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]


try:
    volt = input("Please enter an integer from 0 to 255:")
    while volt != "q":
        if (volt not in allowed):
            print("incorrect input")
        else:
            GPIO.output(dac, dec2bin(volt))
            print(float(volt) / 255 * 3.25)
        volt = input("Please enter an integer from 0 to 255:")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
