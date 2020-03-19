# =============================================================================
################ Cluster-based Subspace Partitioning with CART ################
# =============================================================================
import matplotlib.pyplot as plt 
from ema_workbench.analysis import (cart, RuleInductionType)

# Choose the aggregation level of the clustering --> cluster-indices for ...
#... total design.
clustering = clustering_total

# Load the uncertainty input per experiment. 
x = experiments
x = experiments.drop(['policy','model'],axis=1)
# Load the cluster-indices per experiment. 
y = clustering

# Perform CLASSIFICATION based clustering, due to the cluster-indices.
cart_alg = cart.CART(x,y,mode=RuleInductionType.CLASSIFICATION)
cart_alg.build_tree()

# visualize
cart_alg.show_boxes(together=False)
pp = cart_alg.show_tree(mplfig=True)

fig = plt.gcf()
fig.set_size_inches(36,36)
pp.savefig('./CARTTree9.png')
plt.show()
