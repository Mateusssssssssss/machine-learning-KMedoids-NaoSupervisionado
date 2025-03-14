# K-Medoids Clustering com a Base de Dados Iris

## Descrição
Este projeto implementa o algoritmo **K-Medoids** para realizar agrupamento na base de dados **Iris**. Diferente do K-Means, o K-Medoids escolhe pontos reais como centros dos clusters (medoids), tornando-se mais robusto a outliers. O projeto inclui visualização dos agrupamentos e gera uma matriz de contingência para comparar os grupos previstos com os reais.

## Estrutura do Projeto
- **Carregamento da base de dados Iris**.
- **Configuração do K-Medoids**, utilizando apenas as duas primeiras colunas para facilitar a visualização.
- **Execução do algoritmo** e obtenção dos clusters.
- **Visualização dos agrupamentos** usando `cluster_visualizer`.
- **Geração da matriz de contingência** para comparação entre os grupos reais e previstos.


## Resultados
1. Impressão dos clusters encontrados.
2. Gráfico mostrando os grupos e os medoids (representados por um '*').
3. Matriz de contingência comparando os grupos reais com os previstos.

## Exemplo de Saída (Clusters e Medoids)
```python
[[ 0  0 50]
 [12 38  0]
 [35 14  1]]
```

- Os **medoids iniciais** foram escolhidos aleatoriamente.
- Utilizado apenas as **duas primeiras colunas** da base de dados para facilitar a visualização.
