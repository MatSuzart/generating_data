import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Cria um random walk
rw = RandomWalk()
rw.fill_walk()

#Plota os pontos no passeio
plt.style.use('classic')