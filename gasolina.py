import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina = pd.read_csv("gasolina.csv", sep=',')
display(gasolina)

grafico_linha = sns.lineplot(data = gasolina, x='dia', y='venda', color = 'red')
grafico_linha.set_title("Preço de Gasolina por Dia")
figure = grafico_linha.get_figure()
figure.savefig('gasolina.png')
plt.show(grafico_linha)