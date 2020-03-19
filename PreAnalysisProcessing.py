#################CREATE OUTPUT VECTOR FOR ANALYSIS#############################
import numpy as np
import pandas as pd

# NB outcomes is a dictionary type with within the decision_vector
# decision_vector should be a dataframe to be easily accessible
# Outcome is processed to be used in calculations

# Get number of investments per non-network investment possibility
vv = outcomes['value_vector'] 
# Get number of investments per network investment possibility
lv = outcomes['line_value']
# COSTS treated separately
vv_costs = outcomes['cost_vector']
lv_costs = outcomes['line_cost_vector']

# Convert the four to arrays for processing
vv = np.array(vv) # Non-network number of investments
lv = np.array(lv) # Network number of investments
vv_costs = np.array(vv_costs) # Non-network costs of investments
lv_costs = np.array(lv_costs) # Network costs of investments

# Transpose these to retrieve column-orientation for each experiment
vv = vv.T 
lv = lv.T 
vv_costs = vv_costs.T
lv_costs = lv_costs.T

# Transform all into dataframes
vv = pd.DataFrame.from_records(vv) 
lv = pd.DataFrame.from_records(lv) 
vv_costs = pd.DataFrame.from_records(vv_costs)
lv_costs = pd.DataFrame.from_records(lv_costs)


# To be able to draw conclusions on the data, merge the 'key' with investment..
#... possibilities again with the value dataframes. 

dl = pd.read_excel('./key_vector.xlsx')
# Now merge the two dataframes to create one big decision vector
dv = pd.concat([dl,vv],axis=1) # 'Type','Loc','Year','0','1',..'n-experiments'
dv_costs = pd.concat([dl,vv_costs],axis=1) #'Type','Loc','Year','0',..'n-exp'

# Line investments treated separately due to the edges with two locations.
ll = pd.read_excel('./linekey_vector.xlsx')
# Now merge the two dataframes to create one big decision vector
linedv = pd.concat([ll,lv],axis=1)
linedv_costs = pd.concat([ll,lv_costs],axis=1)

# Construct Edge column based on loc1-loc2 combination
linedv['Edge'] = 0
linedv.loc[((linedv.Loc1 == 'Node_1') & (linedv.Loc2 == 'Node_2')) | \
           ((linedv.Loc1 == 'Node_2') & (linedv.Loc2 == 'Node_1')),'Edge'] \
           = 'Edge_1_2'
linedv.loc[((linedv.Loc1 == 'Node_1') & (linedv.Loc2 == 'Node_3')) | \
           ((linedv.Loc1 == 'Node_3') & (linedv.Loc2 == 'Node_1')),'Edge'] \
           = 'Edge_1_3'
linedv.loc[((linedv.Loc1 == 'Node_1') & (linedv.Loc2 == 'Node_4')) | \
           ((linedv.Loc1 == 'Node_4') & (linedv.Loc2 == 'Node_1')),'Edge'] \
           = 'Edge_1_4'      
linedv.loc[((linedv.Loc1 == 'Node_1') & (linedv.Loc2 == 'Node_5')) | \
           ((linedv.Loc1 == 'Node_5') & (linedv.Loc2 == 'Node_1')),'Edge'] \
           = 'Edge_1_5'  
linedv.loc[((linedv.Loc1 == 'Node_1') & (linedv.Loc2 == 'Node_6')) | \
           ((linedv.Loc1 == 'Node_6') & (linedv.Loc2 == 'Node_1')),'Edge'] \
           = 'Edge_1_6'           
linedv.loc[((linedv.Loc1 == 'Node_1') & (linedv.Loc2 == 'Node_7')) | \
           ((linedv.Loc1 == 'Node_7') & (linedv.Loc2 == 'Node_1')),'Edge'] \
           = 'Edge_1_7'
linedv.loc[((linedv.Loc1 == 'Node_3') & (linedv.Loc2 == 'Node_2')) | \
           ((linedv.Loc1 == 'Node_2') & (linedv.Loc2 == 'Node_3')),'Edge'] \
           = 'Edge_2_3'  
linedv.loc[((linedv.Loc1 == 'Node_4') & (linedv.Loc2 == 'Node_2')) | \
           ((linedv.Loc1 == 'Node_2') & (linedv.Loc2 == 'Node_4')),'Edge'] \
           = 'Edge_2_4'
linedv.loc[((linedv.Loc1 == 'Node_5') & (linedv.Loc2 == 'Node_2')) | \
           ((linedv.Loc1 == 'Node_2') & (linedv.Loc2 == 'Node_5')),'Edge'] \
           = 'Edge_2_5'
linedv.loc[((linedv.Loc1 == 'Node_6') & (linedv.Loc2 == 'Node_2')) | \
           ((linedv.Loc1 == 'Node_2') & (linedv.Loc2 == 'Node_6')),'Edge'] \
           = 'Edge_2_6'           
linedv.loc[((linedv.Loc1 == 'Node_7') & (linedv.Loc2 == 'Node_2')) | \
           ((linedv.Loc1 == 'Node_2') & (linedv.Loc2 == 'Node_7')),'Edge'] \
           = 'Edge_2_7'           
linedv.loc[((linedv.Loc1 == 'Node_3') & (linedv.Loc2 == 'Node_4')) | \
           ((linedv.Loc1 == 'Node_4') & (linedv.Loc2 == 'Node_3')),'Edge'] \
           = 'Edge_3_4'   
linedv.loc[((linedv.Loc1 == 'Node_3') & (linedv.Loc2 == 'Node_5')) | \
           ((linedv.Loc1 == 'Node_5') & (linedv.Loc2 == 'Node_3')),'Edge'] \
           = 'Edge_3_5'     
linedv.loc[((linedv.Loc1 == 'Node_3') & (linedv.Loc2 == 'Node_6')) | \
           ((linedv.Loc1 == 'Node_6') & (linedv.Loc2 == 'Node_3')),'Edge'] \
           = 'Edge_3_6'            
linedv.loc[((linedv.Loc1 == 'Node_3') & (linedv.Loc2 == 'Node_7')) | \
           ((linedv.Loc1 == 'Node_7') & (linedv.Loc2 == 'Node_3')),'Edge'] \
           = 'Edge_3_7'            
linedv.loc[((linedv.Loc1 == 'Node_5') & (linedv.Loc2 == 'Node_4')) | \
           ((linedv.Loc1 == 'Node_4') & (linedv.Loc2 == 'Node_5')),'Edge'] \
           = 'Edge_4_5'
linedv.loc[((linedv.Loc1 == 'Node_6') & (linedv.Loc2 == 'Node_4')) | \
           ((linedv.Loc1 == 'Node_4') & (linedv.Loc2 == 'Node_6')),'Edge'] \
           = 'Edge_4_6'             
linedv.loc[((linedv.Loc1 == 'Node_7') & (linedv.Loc2 == 'Node_4')) | \
           ((linedv.Loc1 == 'Node_4') & (linedv.Loc2 == 'Node_7')),'Edge'] \
           = 'Edge_4_7'          
linedv.loc[((linedv.Loc1 == 'Node_5') & (linedv.Loc2 == 'Node_6')) | \
           ((linedv.Loc1 == 'Node_6') & (linedv.Loc2 == 'Node_5')),'Edge'] \
           = 'Edge_5_6'
linedv.loc[((linedv.Loc1 == 'Node_5') & (linedv.Loc2 == 'Node_7')) | \
           ((linedv.Loc1 == 'Node_7') & (linedv.Loc2 == 'Node_5')),'Edge'] \
           = 'Edge_5_7'           
linedv.loc[((linedv.Loc1 == 'Node_7') & (linedv.Loc2 == 'Node_6')) | \
           ((linedv.Loc1 == 'Node_6') & (linedv.Loc2 == 'Node_7')),'Edge'] \
           = 'Edge_6_7'
# These dataframes consist of the exact same ordering, so copy Edge column           
linedv_costs['Edge'] = linedv['Edge']