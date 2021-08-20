import random
import matplotlib.pyplot as plt

#Generar un número aleatorio
print(random.randrange(10, 100, 2))

#Reacomodar una lista la azar
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Lista Original', list)

random.shuffle(list)
print('Lista remix', list)

campana = [random.gauss(1,0.5) for i in range (1000)]
plt.hist(campana, bins=15)
plt.show()