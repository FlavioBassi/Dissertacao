# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 03:10:18 2021

@author: flavi
"""

import numpy as np
import pandas as pd

# Diable the warnings
import warnings
warnings.filterwarnings('ignore')

#Import Model Packages 
from sklearn.cluster import KMeans, AgglomerativeClustering,AffinityPropagation, DBSCAN
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
from sklearn.metrics import adjusted_mutual_info_score
from sklearn import cluster, covariance, manifold

dataset = pd.read_excel('C:/Users/flavi/Desktop/Dissertação/Cruzamento_Medias_TC.xlsx')
dataset

returns = dataset.mean()*252
returns = pd.DataFrame(returns)
returns.columns = ['Returns']
returns['Volatility'] = dataset.std() * np.sqrt(252)
data=returns

escala = StandardScaler().fit(data)
reescalando = pd.DataFrame(escala.fit_transform(data),
                           columns = data.columns,
                           index = data.index)

X = reescalando
X.head(5)

# Formação e avaliação do modelo
## Affinity Propagation

ap = AffinityPropagation()
ap.fit(X)
clust_labels = ap.predict(X)


cluster_centers_indices = ap.cluster_centers_indices_
labels = ap.labels_

no_clusters = len(cluster_centers_indices)
print(no_clusters)








