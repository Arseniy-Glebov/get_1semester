import RPi.GPIO as GPIO

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
PWM_dac = GPIO.PWM(24, 1000)
PWM_led = GPIO.PWM(9, 1000)
GPIO.output(leds, 0)
allowed = [str(elem) for elem in range(0, 101)]


def dec2bin(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]


try:
    dutyCycle = input("Please enter an integer from 0 to 100(duty cycle %):")
    while dutyCycle != "q":
        if (dutyCycle not in allowed):
            print("incorrect input")
        else:
            PWM_led.start(int(dutyCycle))
            input('Press return to proceed to the standart output')
            PWM_led.stop()
            PWM_dac.start(int(dutyCycle))
            input('Press return to reenter duty cycle')
            PWM_dac.stop()
        dutyCycle = input("Please enter an integer from 0 to 100:")
finally:
    GPIO.output(leds, 0)
    GPIO.output(24, 0)
    GPIO.cleanup()
