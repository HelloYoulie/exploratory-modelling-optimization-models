# =============================================================================
# ####################### CORRELATION## #######################################
# =============================================================================
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### Pairsplot ####
from ema_workbench.analysis import pairs_plotting            

# This version shows the distribution of each outcome of interest as well
pp = sns.pairplot(pd.DataFrame(outcomes),vars=list(outcomes.keys()))
plt.show()
pp.savefig('./analysis/pairplot.png')

#### Correlation matrix ####
# https://seaborn.pydata.org/examples/many_pairwise_correlations.html
# Compute the correlation matrix
corr = pd.DataFrame(outcomes).corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(20, 17))
# Draw the heatmap with the mask and correct aspect ratio
# Use diverging colormap to explicitly note negative vs positive correlations
sns.set(font_scale=0.7)
sns.heatmap(corr, mask=mask, cmap='bwr', center=0,
            square=True, cbar_kws={"shrink": .7})
