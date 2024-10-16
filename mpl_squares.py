import matplotlib.pyplot as plt
plt.style.available

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaboarn')

fig, ax = plt.subplots()
ax.plot(input_values,squares,linewidth=3)
ax.plot(squares, linewidth=3)

#Define o Título do gráfico e os eixos do rótulo
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

#Define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

ax.plot(squares)
plt.show()