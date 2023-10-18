import RPi.GPIO as GPIO
from time import sleep
from time import time
from matplotlib import pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troykaV = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troykaV, GPIO.OUT)


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
    currency = []
    times = []
    current = 0
    GPIO.output(troykaV, GPIO.HIGH)
    start = time()
    while current <= 187:
        current = adc()
        currency.append(current / 255 * 3.3)
        times.append(time() - start)
        print(current)
    GPIO.output(troykaV, GPIO.LOW)
    while current >= 170:
        current = adc()
        currency.append(current / 255 * 3.3)
        times.append(time() - start)
        print(current)
    print("время эксперимента: ", times[-1] - times[0], "c\n",
          "период измерения: ", (times[-1] - times[0]) / len(times), "раз\n",
          "частота дискретизации: ", 1 / ((times[-1] - times[0]) / len(times)), "Гц\n",
          "шаг квантования: ", 3.3 / 255, "B\n")
    with open('/home/b03-301/Desktop/Scripts/get_1semester/data.txt', 'w') as f:
        for i in currency:
            f.write(str(i / 255 * 3.3) + "\n")
        f.write("время эксперимента: " + str(times[-1] - times[0]) + "c\n" + 
          "период измерения: " + str((times[-1] - times[0]) / len(times)) + "раз\n" +
          "частота дискретизации: " + str(1 / ((times[-1] - times[0]) / len(times))) +  "Гц\n" +
          "шаг квантования: " + str(3.3 / 255) + "B\n")
    plt.plot(times, currency)
    plt.show()
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
