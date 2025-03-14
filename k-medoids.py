# Importação das bibliotecas
from sklearn import datasets
from sklearn.metrics import confusion_matrix
import numpy as np
# importa o algoritmo K-Medoids, que é uma alternativa ao K-Means. 
# Ele funciona escolhendo pontos reais como centros dos clusters (medoids) 
# em vez de calcular médias. Isso torna o algoritmo mais robusto a outliers.
from pyclustering.cluster.kmedoids import kmedoids
#gerar gráficos e visualizar os agrupamentos formados pelo K-Medoids 
from pyclustering.cluster import cluster_visualizer

# Carregamento da base de dados
iris = datasets.load_iris()

# Configuração dos parâmetros do k-medoids, utilizando somente as duas primeiras colunas da base de dados por causa da visualização apenas
# 3, 12 e 20 são índices aleatórios de registros da base de dados (inicialização)
cluster = kmedoids(iris.data[:, 0:2], [50, 6, 40])
# Visualização dos pontos escolhidos (3, 12 e 20)
cluster.get_medoids()


# Aplicação do algoritmo para o agrupamento, obtenção da previsões (grupo de cada registro) e visualização dos medoides
# Ele processa os dados fornecidos e encontra os clusters com base na lógica do algoritmo escolhido
cluster.process()
previsoes = cluster.get_clusters()
medoides = cluster.get_medoids()
#lista de 3 elementos, com os indices dos registros do cluster
print(previsoes)
print(medoides)



# Visualização do agrupamento
# Cria uma instância do cluster_visualizer
v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:,0:2])
#marker = '*': usa um asterisco para representar os medoids.
#markersize = 20: define o tamanho do marcador maior para facilitar a visualização.
v.append_cluster(medoides, data = iris.data[:,0:2], marker = '*', markersize = 20)
#Gera o grafico
v.show()

# Código para criar duas listas, uma com os grupos reais da base de dados e outra com os valores dos grupos
# Utilizado posteriormente para visualização da matriz de contingência
lista_previsoes = []
lista_real = []
for i in range(len(previsoes)):
     for j in range(len(previsoes[i])):
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])
        
        
# Geração da matriz de contingência, comparando os grupos reais com os grupos previstos
lista_previsoes = np.asarray(lista_previsoes)
lista_real = np.asarray(lista_real)
resultados = confusion_matrix(lista_real, lista_previsoes)
print(resultados)