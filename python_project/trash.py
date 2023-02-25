import pandas
#import matplotlib.pyplot as plt
import numpy

dados = pandas.read_csv('python_project\\dados\\trees.csv')

print(dados['Girth'])

print(dados.iloc[:,0])

#h = numpy.histogram(dados['Girth'])
#print(h)

#x = [3, 2, 9, 3, 5, 1, 2, 5, 0, 1 , 1]
#y = [ 8.3 ,9.53, 10.76, 11.99, 13.22, 14.45, 15.68, 16.91, 18.14,19.37, 20.6 ]

#print(len(x), len(y))

#plt.hist(dados.iloc[:,1] , numpy.array(range(0,31,1)))
#plt.show()
plt.title('Gráfico de Histograma')
plt.xlabel('Girth')
plt.ylabel('Frequência')

#seaborn