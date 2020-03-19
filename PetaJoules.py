# ####################### PetaJoules invested in ##############################
import pandas as pd
import numpy as np

# This function returns the energy capacity invested in per type,...
#... location and year.
# =============================================================================

###################IMPORT DATA#################################################
# First, the capacity data per technology unit must be imported. 
# Retrieving dataframes from MS Excel.
db_file= './7_nodes_voorPython_with_time_2018_WithScenarios.xlsx'
db_file = pd.ExcelFile(db_file)

#Read data from the excel datafiles 
# per unit the 'produced' (=converted) PJ of energy
df_conversion_efficiencies = db_file.parse('ConversionEfficiencies') 
# The energy demand in PJ
df_demand = db_file.parse('Demand')
# per unit the maximum 'consumed' (=converted) PJ of energy
df_max_converted = db_file.parse('MaxConverted') 
# per network pipeline the PJ transport capacity
df_max_flow = db_file.parse('MaxFlow') 
 # per unit the maximum storage capacity PJ of energy
df_storage_units = db_file.parse('StorageUnits')
# the PJ supplied energy in the form of natural gas
df_supply = db_file.parse('Supply') 
# per supply unit (PV and wind) the maximum supply capacity PJ of energy
df_supply_units = db_file.parse('SupplyUnits') 

# The yearly cumulative DEMAND over time
# Retrieve the demand indices for the uncertainty demand scenarios...
#... from the experiment set
demand_index = experiments['demand_index']
# Aggregate the demand (specified per location and energy carrier) ...
#... to total demand per year.
demandvalues = df_demand.groupby('TimePeriod').agg('sum')
demandvalues.insert(0,'new-col',0)
demandvalues.insert(1,'ne-col',0)
demandvalues.insert(2,'n-col',0)
# Fill the demand dataframe with the timeseries as in the experiments.
demand_PJ = demandvalues.iloc[:,demand_index]


###################CALCULATE PJs###############################################
# Now, with the number of units invested in known, and the capacity per unit...
#... known, the amount of energy capacity (PJ) invested in is calculated.

# Per supply unit the yearly cumulative supply capacity over time
solar_PJ = np.cumsum(count_type_year.loc['Solar'],axis=0)*\
    df_supply_units.loc[df_supply_units.SupplyType=='Solar','MaxSupply']\
    .reset_index(drop=True)[0]
wind_PJ = np.cumsum(count_type_year.loc['Wind'],axis=0)*\
    df_supply_units.loc[df_supply_units.SupplyType=='Wind','MaxSupply']\
    .reset_index(drop=True)[0]
gas_supply_PJ = pd.DataFrame(np.zeros((17,900)))
supplyvalues = df_supply.groupby('iTimeSlot').agg('sum').loc[:,'MaxSupply']
for x in gas_supply_PJ.columns:
    gas_supply_PJ.loc[:,x] = supplyvalues.values
gas_supply_PJ = gas_supply_PJ.set_index(supplyvalues.index)

total_supply_PJ = solar_PJ + wind_PJ #+ gas_supply_PJ 

# Per conversion unit the yearly cumulative conversion capacity over time
hp_PJ = np.cumsum(count_type_year.loc['HP'],axis=0)*\
    df_max_converted.loc[((df_max_converted.ConversionUnit=='HP')&\
                          (df_max_converted.Type=='Electricity')),
                          'MaxConverted']\
    .reset_index(drop=True)[0]
chp_PJ = np.cumsum(count_type_year.loc['CHP'],axis=0)*\
    df_max_converted.loc[((df_max_converted.ConversionUnit=='CHP') &\
                          (df_max_converted.Type=='Gas')),'MaxConverted']\
    .reset_index(drop=True)[0]
p2g_PJ = np.cumsum(count_type_year.loc['P2G'],axis=0)*\
    df_max_converted.loc[((df_max_converted.ConversionUnit=='P2G')&\
                          (df_max_converted.Type=='Electricity'))
                           ,'MaxConverted']\
    .reset_index(drop=True)[0]
    
total_conversion_PJ = hp_PJ + chp_PJ + p2g_PJ    
   
# Per storage unit the yearly cumulative storage capacity over time
elec_PJ = np.cumsum(count_type_year.loc['Electricity'],axis=0)*\
    df_storage_units.loc[df_storage_units.StorageType=='Electricity','MaxStorageLevel']\
    .reset_index(drop=True)[0]
gas_PJ = np.cumsum(count_type_year.loc['Gas'],axis=0)*\
    df_storage_units.loc[df_storage_units.StorageType=='Gas','MaxStorageLevel']\
    .reset_index(drop=True)[0]
heat_PJ = np.cumsum(count_type_year.loc['Heat'],axis=0)*\
    df_storage_units.loc[df_storage_units.StorageType=='Heat','MaxStorageLevel']\
    .reset_index(drop=True)[0]
    
total_storage_PJ = gas_PJ + elec_PJ + heat_PJ    

# Per pipelinetype the yearly cumulative network transport capacity over time
elec_line_PJ = np.cumsum(count_type_year_line.loc['Electricity'],axis=0)*\
    df_max_flow.loc[df_max_flow.Type=='Electricity','MaxFlowLine']\
    .reset_index(drop=True)[0]
gas_line_PJ = np.cumsum(count_type_year_line.loc['Gas'],axis=0)*\
    df_max_flow.loc[df_max_flow.Type=='Gas','MaxFlowLine']\
    .reset_index(drop=True)[0]
heat_line_PJ = np.cumsum(count_type_year_line.loc['Heat'],axis=0)*\
    df_max_flow.loc[df_max_flow.Type=='Heat','MaxFlowLine']\
    .reset_index(drop=True)[0]  
    
total_line_PJ = gas_line_PJ + elec_line_PJ + heat_line_PJ    
