# =============================================================================
######################## Cosine Distance Clustering ###########################
# =============================================================================
### DENDROGRAM (based on the agglomerative hierarchical clustering - linkage)
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt

# distance_matrix_total_count is cosine distance matrix of the total design.
dists = squareform(distance_matrix_total_count)
linkage_matrix = linkage(dists, "complete")
fig = plt.figure(figsize=(25, 10))
dendrogram(linkage_matrix,no_labels=True)
plt.show()

# Agglomerative clustering on the cosine distance matrices for the total...
#... energy system design. 
# Outcome is the cluster label per experiment. 
# 'Complete' linkage method. 
from sklearn.cluster import AgglomerativeClustering
clustering_total = AgglomerativeClustering(affinity='precomputed',
                                           linkage='complete',
                        n_clusters=9).fit_predict(distance_matrix_total_count)

