# =============================================================================
# ################# Specify characteristics OUTCOMES OF INTEREST ##############
# =============================================================================
import pandas as pd
import numpy as np

# Output is dataframe, which is written to excel, containing per OoI the ...
# ... median, standard deviation and variance. 
ooi_characteristics = pd.DataFrame(columns=['Median','25% quantile',
                                            '75% quantile','IQR','Min'],
                                   index=dict.keys(outcomes_PJ_separate))

for key in outcomes_PJ_separate:
    ooi_characteristics.loc[key] = pd.Series\
        ({'Median':np.median(outcomes_PJ_separate[key]), 
          '25% quantile':np.quantile(outcomes_PJ_separate[key],0.25), 
          '75% quantile':np.quantile(outcomes_PJ_separate[key],0.75),
          'IQR':(np.quantile(outcomes_PJ_separate[key],0.75)-\
                 np.quantile(outcomes_PJ_separate[key],0.25)),
          'Min':np.min(outcomes_PJ_separate[key])})

ooi_characteristics.to_excel('./results/OoI_Characteristics.xlsx')

# Give the unique values, and the count of these, for input. 
np.unique(np.array(wind_PJ.loc[2050]),return_counts=True)

# =============================================================================
# ################# DETERMINE THRESHOLDS OUTCOMES OF INTEREST #################
# =============================================================================
# Use these as thresholds to make such analysis provide relevant insights
np.quantile(total_costs_array,0.1) # < this is the 10% lowest costs
np.quantile(total_costs_array,0.9) # > this is the 10% highest costs
np.quantile(total_costs_array,0.75) # between 0.25 & 0.75 is the median+-25% 
np.quantile(total_costs_array,0.25) 
