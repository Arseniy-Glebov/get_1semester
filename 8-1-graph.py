import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

f = open('/home/b03-301/Desktop/Scripts/get_1semester/data.txt', 'r')
data = f.read().split("\n")
f.close()
data = [float(i) * 100 for i in data]

f = open('/home/b03-301/Desktop/Scripts/get_1semester/settings.txt', 'r')
raw = f.read().split("\n")[1]
step = ""
f.close()
for i in raw:
    if i.isdigit() or i == ".":
        step += i
step = float(step)
time = [i * step for i in range(len(data))] 

fig, ax = plt.subplots()
plt.plot(time, data, linewidth='0.5', label='V(t)', marker='.', markevery=20)

plt.title(label='Зависимость напряжения на конденсаторе\n от времени', loc='center')
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))
ax.tick_params(which='major')
plt.grid(which='minor', linewidth='0.2', linestyle='dashed', color='black')
plt.grid(which='major', linewidth='1')
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.legend()
plt.text(7, 1.5, "Время зарядки - 9 с")
plt.text(7, 1, "Время разрядки - 3.8 с")

plt.show()
