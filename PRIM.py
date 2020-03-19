# =============================================================================
################# PRIM Subspace Partitioning on Outcomes of Interest ##########
# =============================================================================
# Find an (orthogonal) subspace in the model input space, which has a high ...
#... concentration of cases of interest (by specifying the outcome constraint).
from ema_workbench.analysis import prim
from Fontsize import change_fontsize
import matplotlib.pyplot as plt
import numpy as np

# Load the uncertainty input for each experiment
x = experiments
# Classify the output space per experiment as True/False based on the ...
#... specified conditions.
y = ((outcomes['Total PV capacity (PJ)'] > \
                np.quantile(np.array(solar_PJ.loc[2050]),0.75))&\
                (outcomes['Total PV capacity (PJ)'] <= 12.5))

# Perform PRIM
# Threshold should be 0.8 for more accurate analysis.
# Mass_min can be reduced for OoIs with a low number of 'True' experiments.
prim_alg = prim.Prim(x, y, threshold=0.8, peel_alpha=0.05, mass_min=0.05) 
box1 = prim_alg.find_box()

# Coverage = fraction of cases of interest within the box
# Density = fraction of cases in the box which are of interest
# Quasi p-values (qp) = one sided binomial test, proxy for statistical ...
# significance of each uncertainty in isolation (>=0.05).
# The algorithm automatically selects the 'best' datapoint for analysis. 
box1.show_tradeoff()
plt.show()
box1.inspect()
ax = box1.inspect(style='graph')
change_fontsize(ax, fs=17)
plt.show()
box1.show_pairs_scatter()
plt.show()