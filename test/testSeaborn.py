import seaborn as sns
import matplotlib.pyplot as plt

#==============================================================================

# Carregar dados de exemplo
tips = sns.load_dataset('tips')

# Gráfico de dispersão com regressão linear
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Gráfico de dispersão com regressão linear')
plt.show()

#==============================================================================

# Carregar dados de exemplo
titanic = sns.load_dataset('titanic')

# Gráfico de barras com contagem de sobreviventes por classe
sns.barplot(data=titanic, x='class', y='survived')
plt.title('Gráfico de barras com contagem de sobreviventes por classe')
plt.show()

#==============================================================================

# Carregar dados de exemplo
iris = sns.load_dataset('iris')

# Gráfico de boxplot das medidas de pétalas por espécie
sns.boxplot(data=iris, x='species', y='petal_length')
plt.title('Gráfico de boxplot das medidas de pétalas por espécie')
plt.show()

#==============================================================================

# Carregar dados de exemplo
iris = sns.load_dataset('iris')

# Gráfico de violino das medidas de pétalas por espécie
sns.violinplot(data=iris, x='species', y='petal_length')
plt.title('Gráfico de violino das medidas de pétalas por espécie')
plt.show()

#==============================================================================

# Carregar dados de exemplo
tips = sns.load_dataset('tips')

# Gráfico de distribuição do valor da conta
sns.histplot(data=tips, x='total_bill', kde=True)
plt.title('Gráfico de distribuição do valor da conta')
plt.show()

#==============================================================================

# Dados de exemplo
labels = ['Maçã', 'Banana', 'Laranja', 'Pera']
sizes = [30, 25, 20, 15]
colors = ['red', 'yellow', 'orange', 'green']

# Plotar o gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Definir a legenda
plt.legend(labels, loc='best')

plt.axis('equal')  # Para tornar o gráfico circular
plt.title('Distribuição de Frutas')
plt.show()

#==============================================================================

# Dados de exemplo
labels = ['Maçã', 'Banana', 'Laranja', 'Pera']
sizes = [30, 25, 20, 15]
colors = ['red', 'yellow', 'orange', 'green']

# Plotar o gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Criar a legenda personalizada
legend_labels = [f'{label} - {size}%' for label, size in zip(labels, sizes)]
legend = plt.legend(legend_labels, title='Frutas', loc='best')

# Definir título para a legenda
legend.set_title('Legenda', prop={'size': 12})

plt.axis('equal')  # Para tornar o gráfico circular
plt.title('Distribuição de Frutas')
plt.show()