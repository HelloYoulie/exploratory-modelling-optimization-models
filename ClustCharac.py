# =============================================================================
######## Cosine Distance-based Agglomerative Clusters Characterization ########
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# Return the number of clusters and the in-cluster-experiment counts. 
np.unique(clustering_total,return_counts=True)

#### Work from the ID'd clusters column-indices to the count input
# Create new count dataframes to prevent overwriting
type_v_count_cluster = type_v_count
loc_v_count_cluster = loc_v_count
year_v_count_cluster = year_v_count
#### Rename the columns of the aggregations to the identified cluster-indices
type_v_count_cluster.columns = clustering_total
loc_v_count_cluster.columns = clustering_total
year_v_count_cluster.columns = clustering_total

# Create empty dataframes to fill with the median and IQR characteristics...
#... per aggregation of the total design clusters. 
type_median = pd.DataFrame()
type_IQR = pd.DataFrame()
loc_median = pd.DataFrame()
loc_IQR = pd.DataFrame()
year_median = pd.DataFrame()
year_IQR = pd.DataFrame()

# The first column of the characteristics dataframes contains the ...
#... NON-CLUSTERED total design characteristics. 
type_median = pd.concat([type_median,
                         pd.DataFrame(np.median(type_v_count,axis=1))],axis=1)
type_IQR = pd.concat([type_IQR,
                      pd.DataFrame(np.quantile(type_v_count,0.75,axis=1)-\
                                   np.quantile(type_v_count,0.25,axis=1))],
                                   axis=1)
loc_median = pd.concat([loc_median,
                        pd.DataFrame(np.median(loc_v_count,axis=1))],axis=1)
loc_IQR = pd.concat([loc_IQR,
                     pd.DataFrame(np.quantile(loc_v_count,0.75,axis=1)-\
                                  np.quantile(loc_v_count,0.25,axis=1))],
                                  axis=1)
year_median = pd.concat([year_median,
                         pd.DataFrame(np.median(year_v_count,axis=1))],axis=1)
year_IQR = pd.concat([year_IQR,
                      pd.DataFrame(np.quantile(year_v_count,0.75,axis=1)-\
                                   np.quantile(year_v_count,0.25,axis=1))],
                                   axis=1)

# The other columns of the characteristics dataframes contain the ...
#... CLUSTERED total design characteristics. 
 # Only analyse the clusters with n_exp >=1% ...
 #... (number of in-cluster experiments >= 8)                      
for x in [0,1,2,3,4,8]:
    type_med = pd.DataFrame(np.median(type_v_count_cluster.loc[:,x],axis=1))
    type_median = pd.concat([type_median,type_med],axis=1)
    
    type_IQR_n = pd.DataFrame(np.quantile(type_v_count_cluster.loc[:,x],
                                          0.75,axis=1)-\
                              np.quantile(type_v_count_cluster.loc[:,x],
                                          0.25,axis=1))   
    type_IQR = pd.concat([type_IQR,type_IQR_n],axis=1)            
    
    loc_med = pd.DataFrame(np.median(loc_v_count_cluster.loc[:,x],axis=1))
    loc_median = pd.concat([loc_median,loc_med],axis=1)
    
    loc_IQR_n = pd.DataFrame(np.quantile(loc_v_count_cluster.loc[:,x],
                                         0.75,axis=1)-\
                 np.quantile(loc_v_count_cluster.loc[:,x],0.25,axis=1))   
    loc_IQR = pd.concat([loc_IQR,loc_IQR_n],axis=1)  
    
    year_med = pd.DataFrame(np.median(year_v_count_cluster.loc[:,x],axis=1))
    year_median = pd.concat([year_median,year_med],axis=1)
    
    year_IQR_n = pd.DataFrame(np.quantile(year_v_count_cluster.loc[:,x],
                                          0.75,axis=1)-\
                 np.quantile(year_v_count_cluster.loc[:,x],0.25,axis=1))   
    year_IQR = pd.concat([year_IQR,year_IQR_n],axis=1)
    
### Visualize the result in heatmaps. 
### TYPE aggregation
fig = plt.figure()
fig.set_size_inches(10,10)
sns.set(font_scale=1.8)  
xx = sns.heatmap(type_median,cmap='viridis',square=True,annot=True,cbar=False,
            xticklabels=['Non-clustered','1','2','3','4','5','6'],
            yticklabels=['CHP','E storage','G storage','HP','H storage',
                         'P2G','PV supply','Wind supply','E network',
                         'G network','H network'])
xx.figure.savefig('./analysis/Clusters_Median_HM_Type.png')

fig = plt.figure()
fig.set_size_inches(10,10)
sns.set(font_scale=1.8)
xx = sns.heatmap(type_IQR,cmap='viridis',square=True,annot=True,cbar=False,
            xticklabels=['Non-clustered','1','2','3','4','5','6'],
            yticklabels=['CHP','E storage','G storage','HP','H storage',
                         'P2G','PV supply','Wind supply','E network',
                         'G network','H network'])
xx.figure.savefig('./analysis/Clusters_IQR_HM_Type.png')   

### LOCATION aggregation
fig = plt.figure()
fig.set_size_inches(20,20)
sns.set(font_scale=1.8)
xx = sns.heatmap(loc_median,cmap='viridis',square=True,annot=True,cbar=False,
            xticklabels=['Non-clustered','1','2','3','4','5','6'],
            yticklabels=['Node_1','Node_2','Node_3','Node_4','Node_5',
                         'Node_6','Node_7','Edge_1_2','Edge_1_3','Edge_1_4',
                         'Edge_1_5','Edge_1_6','Edge_1_7','Edge_2_3',
                         'Edge_2_4','Edge_2_5','Edge_2_6','Edge_2_7',
                         'Edge_3_4','Edge_3_5','Edge_3_6','Edge_3_7',
                         'Edge_4_5','Edge_4_6','Edge_4_7','Edge_5_6',
                         'Edge_5_7','Edge_6_7'])
xx.figure.savefig('./analysis/Clusters_Median_HM_Loc.png')

fig = plt.figure()
fig.set_size_inches(20,20)
sns.set(font_scale=1.8)
xx = sns.heatmap(loc_IQR,cmap='viridis',square=True,annot=True,cbar=False,
            xticklabels=['Non-clustered','1','2','3','4','5','6'],
            yticklabels=['Node_1','Node_2','Node_3','Node_4','Node_5',
                         'Node_6','Node_7','Edge_1_2','Edge_1_3','Edge_1_4',
                         'Edge_1_5','Edge_1_6','Edge_1_7','Edge_2_3',
                         'Edge_2_4','Edge_2_5','Edge_2_6','Edge_2_7',
                         'Edge_3_4','Edge_3_5','Edge_3_6','Edge_3_7',
                         'Edge_4_5','Edge_4_6','Edge_4_7','Edge_5_6',
                         'Edge_5_7','Edge_6_7'])
xx.figure.savefig('./analysis/Clusters_IQR_HM_Loc.png')

### TIME PERIOD aggregation 
fig = plt.figure()
fig.set_size_inches(10,10)
sns.set(font_scale=1.8)
xx = sns.heatmap(year_median,cmap='viridis',square=True,annot=True,cbar=False,
            xticklabels=['Non-clustered','1','2','3','4','5','6'],
            yticklabels=['2020','2022','2024','2026','2028','2030','2032',
                         '2034','2036','2038','2040','2042','2044','2046',
                         '2048','2050'])
xx.figure.savefig('./analysis/Clusters_Median_HM_Year.png')

fig = plt.figure()
fig.set_size_inches(10,10)
sns.set(font_scale=1.8)
xx = sns.heatmap(year_IQR,cmap='viridis',square=True,annot=True,cbar=False,
            xticklabels=['Non-clustered','1','2','3','4','5','6'],
            yticklabels=['2020','2022','2024','2026','2028','2030','2032',
                         '2034','2036','2038','2040','2042','2044','2046',
                         '2048','2050'])
xx.figure.savefig('./analysis/Clusters_IQR_HM_Year.png')
