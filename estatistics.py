import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datamodule.connectionDataBase import ConnectionDataBase
import queries.queries as qrs

class Estatistics:
    def __init__(self):
        self.__conn = ConnectionDataBase()

    def Show(self):
        results = self.__Dados(qrs.SELECT_CASE_COUNT_ESTATISTICA)
        self.__ShowBarplot(results)
        self.__ShowPieplot(results)

        results = self.__Dados(qrs.SELECT_ACERTO_QTD_EST)
        self.__ShowScatterplot(results)

        self.__ShowHistplot(results)

    def __ShowBarplot(self, results):
        intervalos = [str(d[0]) + "%" for d in results]
        quantidades = [d[1] for d in results]

        sns.barplot(x=intervalos, y=quantidades)
        plt.xlabel("Acurácia")
        plt.ylabel("Qtd. Registros")
        plt.title("Contagem de registros por intervalo")

        for i in range(len(quantidades)):
          plt.text(i, quantidades[i], str(quantidades[i]), ha='center', va='bottom')

        plt.show()

    def __ShowPieplot(self, results):
        intervalos = [str(d[0]) + "%" for d in results]
        quantidades = [d[1] for d in results]

        colors = ['red', 'yellow', 'orange', 'cyan', 'blue', 'purple', 'pink', 'gray', 'brown', 'black', 'green']
        plt.figure(figsize=(10, 10))
        plt.pie(quantidades, colors=colors, autopct='%1.1f%%', startangle=90)

        legend = plt.legend(intervalos, title='Acurácia', loc='best')
        legend.set_title('Acurácia', prop={'size': 12})

        plt.axis('equal')
        plt.title('Distribuição da acurácia em relação ao total de registros')
        plt.show()

    def __ShowScatterplot(self, results):
        df = pd.DataFrame(results, columns=["acerto", "quantidade"])
        sns.scatterplot(data=df, x='acerto', y='quantidade')
        plt.title('Gráfico de dispersão com regressão linear')
        plt.show()

    def __ShowHistplot(self, results):
      pass

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