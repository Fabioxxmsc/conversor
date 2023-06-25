import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datamodule.connectionDataBase import ConnectionDataBase

class Estatistics:
    def __init__(self):
        self.__conn = ConnectionDataBase()

    def Show(self):
        self.__ShowHistplot()

    def __ShowHistplot(self):
        query = """  select cast (case  
                                  when e.acerto between 00 and 09.9999 then '00'
                                  when e.acerto between 10 and 19.9999 then '10'
                                  when e.acerto between 20 and 29.9999 then '20'
                                  when e.acerto between 30 and 39.9999 then '30'
                                  when e.acerto between 40 and 49.9999 then '40'
                                  when e.acerto between 50 and 59.9999 then '50'
                                  when e.acerto between 60 and 69.9999 then '60'
                                  when e.acerto between 70 and 79.9999 then '70'
                                  when e.acerto between 80 and 89.9999 then '80'
                                  when e.acerto between 90 and 99.9999 then '90'
                                  when e.acerto = 100 then '100'
                                end as integer) as intervalo
                              , count(*) as quantidade
                            from estatistica e
                        group by intervalo
                        order by intervalo
                """
        
        results = self.__Dados(query)

        # Converter os dados em listas separadas
        intervalos = [str(d[0]) + "%" for d in results]
        quantidades = [d[1] for d in results]

        # Plotar o gráfico de barras
        sns.barplot(x=intervalos, y=quantidades)
        plt.xlabel("Acurácia")
        plt.ylabel("Qtd. Registros")
        plt.title("Contagem de registros por intervalo")

        for i in range(len(quantidades)):
          plt.text(i, quantidades[i], str(quantidades[i]), ha='center', va='bottom')

        plt.show()

        # Plotar o gráfico de pizza
        colors = ['red', 'yellow', 'orange', 'cyan', 'blue', 'purple', 'pink', 'gray', 'brown', 'black', 'green']
        plt.figure(figsize=(10, 10))
        plt.pie(quantidades, colors=colors, autopct='%1.1f%%', startangle=90)

        # Definir a legenda
        legend = plt.legend(intervalos, title='Acurácia', loc='best')
        # Definir título para a legenda
        legend.set_title('Acurácia', prop={'size': 12})

        plt.axis('equal') # Para tornar o gráfico circular
        plt.title('Distribuição da acurácia em relação ao total de registros')
        plt.show()

        # Plotar o gráfico de dispersão
        query = "select e.acerto, count(*) as quantidade from estatistica e group by e.acerto order by e.acerto"
        results = self.__Dados(query)
        df = pd.DataFrame(results, columns=["acerto", "quantidade"])
        sns.scatterplot(data=df, x='acerto', y='quantidade')
        plt.title('Gráfico de dispersão com regressão linear')
        plt.show()

    def __Dados(self, query):
      results = None
      connection = self.__conn.Connection()
      connection.autocommit = False

      cursor = connection.cursor()
      try:
          cursor.execute(query)
          results = cursor.fetchall()            
          connection.commit()
      except (Exception) as error:
          connection.rollback()
          print('error in query: ' + query, error)
          raise

      finally:
          if cursor is not None:
              if not cursor.closed:
                  cursor.close()
      return results

if __name__ == '__main__':
    estatistics = Estatistics()
    estatistics.Show()