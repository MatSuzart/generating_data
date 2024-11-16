import plotly.express as px
from die import Die

# Cria um D6 e um D10
die_1 = Die(6)
die_2 = Die(10)

# Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

# Analisando os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_result = range(2, max_result + 1)
for value in poss_result:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados 
title = "Results of Rolling Two Dice 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_result, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
