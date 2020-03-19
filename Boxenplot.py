#==============================================================================
# ################################## SHOW BOXENPLOT ###########################
# =============================================================================
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(columns=['Total wind capacity (PJ)',
                        'Total PV capacity (PJ)',
                        'Total gas storage capacity (PJ)',
                        'Total heat storage capacity (PJ)',
                        'Total CHP capacity (PJ)',
                        'Total HP capacity (PJ)',
                        'Total P2G capacity (PJ)',
                        'Total network capacity (PJ)',
                        'Clustering'])
    
data['Total wind capacity (PJ)'] = np.array(wind_PJ.loc[2050])
data['Total PV capacity (PJ)'] = np.array(solar_PJ.loc[2050])
data['Total gas storage capacity (PJ)'] = np.array(gas_PJ.loc[2050])
data['Total heat storage capacity (PJ)'] = np.array(heat_PJ.loc[2050])
data['Total CHP capacity (PJ)'] = np.array(chp_PJ.loc[2050])
data['Total HP capacity (PJ)'] = np.array(hp_PJ.loc[2050])
data['Total P2G capacity (PJ)'] = np.array(p2g_PJ.loc[2050])
data['Total network capacity (PJ)'] = np.array(total_line_PJ.loc[2050])
plt.figure(figsize=(20, 10))
ax = sns.boxenplot(data=data)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, 
                   horizontalalignment='right',
                   fontweight='light',fontsize='small')