# =============================================================================
# ########## Visualization of Cosine Distance between Experiments #############
# =============================================================================
import seaborn as sns
import pandas as pd
import numpy as np
from CosDist import cos_dist_df

### TOTAL (number of investments for all investment possibilities)
# NB max distance value = 0.3613807473319133
total_v_count = pd.concat([vv,lv])
# Calculate the cosine distances
distance_matrix_total_count = cos_dist_df(total_v_count)
# Mask the upper half of the matrix
mask = np.zeros_like(distance_matrix_total_count)
mask[np.triu_indices_from(mask)] = True
# Visualize the distances with color differences
sns.heatmap(distance_matrix_total_count, mask=mask, cmap='viridis',
            vmin=0,
            square=True, yticklabels=False, xticklabels=False).\
            collections[0].colorbar.set_label("Cosine distance")
            
### Type aggregation (total number of investments for all experiments ...
#... per techology unit (summation of all locations and time periods))
# max distance value = 0.1277794295904222
type_v_count = pd.concat([count_type,count_type_line])
distance_matrix_type_count = cos_dist_df(type_v_count)
mask = np.zeros_like(distance_matrix_type_count)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(distance_matrix_type_count, mask=mask, cmap='viridis',
            vmin=0,
            square=True, yticklabels=False, xticklabels=False).\
            collections[0].colorbar.set_label("Cosine distance")
            
### Location aggregation (total number of investments for all experiments ...
#... per location (summation of all technology units and time periods))
# max distance value = 0.19790257944723078
loc_v_count = pd.concat([count_loc,count_edge_line])
loc_v_count = loc_v_count.drop(0)
distance_matrix_loc_count = cos_dist_df(loc_v_count)
mask = np.zeros_like(distance_matrix_loc_count)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(distance_matrix_loc_count, mask=mask, cmap='viridis',
            vmin=0,#vmax=0.37, 
            square=True, yticklabels=False, xticklabels=False).\
            collections[0].colorbar.set_label("Cosine distance")
            
### Year aggregation (total number of investments for all experiments ...
#... per time period (summation of all technology units and locations))
# Add up the non-network and network outcomes here to prevent...
#... two entire time periods. 
# max distance value = 0.9398124576806194 WITHOUT 2018 
year_v_count = count_year+count_year_line 
# Drop 2018 to prevent distortion
year_v_count = year_v_count.drop(labels=2018)
distance_matrix_year_count = cos_dist_df(year_v_count)
mask = np.zeros_like(distance_matrix_year_count)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(distance_matrix_year_count, mask=mask, cmap='viridis',
            vmin=0,vmax=1, square=True, yticklabels=False, xticklabels=False).\
            collections[0].colorbar.set_label("Cosine distance")
