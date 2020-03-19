# ####################### Counter ##############################################
# This function returns the number of investments per type, location and year.
# =============================================================================
import numpy as np

# Non-Network investment options
# Count the number of investments per non-network unit per experiment
count_type = dv.groupby('Type').agg('sum')
# Drop the time periods, as the algorithm perceives the years as integers.
count_type = count_type.drop(columns='TIME')
# Count the costs of investments per technology unit per experiment
count_type_costs = dv_costs.groupby('Type').agg('sum')
count_type_costs = count_type_costs.drop(columns='TIME')

# The number of investments & costs per technology unit and year. 
count_type_year = dv.groupby(['Type','TIME']).agg('sum')
count_type_year_costs = dv_costs.groupby(['Type','TIME']).agg('sum')

# Count the number and costs of investments per location per experiment
count_loc = dv.groupby('Loc').agg('sum')
count_loc = count_loc.drop(columns='TIME')
count_loc_costs = dv_costs.groupby('Loc').agg('sum')
count_loc_costs = count_loc_costs.drop(columns='TIME')

# Count the number and costs of investments per location & year per experiment.
count_loc_year = dv.groupby(['Loc','TIME']).agg('sum')
count_loc_year_costs = dv_costs.groupby(['Loc','TIME']).agg('sum')

# Count the number and costs of investments per year per experiment
count_year = dv.groupby('TIME').agg('sum')
count_year_costs = dv_costs.groupby('TIME').agg('sum')

# Now simply sum the number of investments per non-network technology unit.
count_supply = count_type.loc["Solar"] + count_type.loc["Wind"]
count_converter = count_type.loc["P2G"] + count_type.loc["HP"]  \
                                        + count_type.loc["CHP"]
count_storage = count_type.loc["Electricity"] + count_type.loc["Gas"] \
                                        + count_type.loc["Heat"]
count_supply_costs = count_type_costs.loc["Solar"] \
                        + count_type_costs.loc["Wind"]
count_converter_costs = count_type_costs.loc["P2G"] \
                        + count_type_costs.loc["HP"]  \
                        + count_type.loc["CHP"]
count_storage_costs = count_type_costs.loc["Electricity"] \
                        + count_type_costs.loc["Gas"] \
                        + count_type_costs.loc["Heat"]

# Network investment options
# Count the number of investments per non-network unit per experiment
count_type_line = linedv.groupby('Type').agg('sum')
# Drop the time periods, as the algorithm perceives the years as integers.
count_type_line = count_type_line.drop(columns='TIME')
# Count the costs of investments per non-network unit per experiment
count_type_line_costs = linedv_costs.groupby('Type').agg('sum')
count_type_line_costs = count_type_line_costs.drop(columns='TIME')

# The number of investments & costs per network unit and year. 
count_type_year_line = linedv.groupby(['Type','TIME']).agg('sum')
count_type_year_line_costs = linedv_costs.groupby(['Type','TIME']).agg('sum')

# Count the number and costs of network investments per year per experiment
count_year_line = linedv.groupby('TIME').agg('sum')
count_year_line_costs = linedv_costs.groupby('TIME').agg('sum')

# Count the number and costs of network investments per edge per experiment
count_edge_line = linedv.groupby('Edge').agg('sum')
count_edge_line = count_edge_line.drop(columns='TIME')
count_edge_line_costs = linedv_costs.groupby('Edge').agg('sum')
count_edge_line_costs = count_edge_line_costs.drop(columns='TIME')

# Count the number and costs of network investments per edge & year per exp.
count_edge_year_line = linedv.groupby(['Edge','TIME']).agg('sum')
count_edge_year_line_costs = linedv_costs.groupby(['Edge','TIME']).agg('sum')


# ####################### Counter to % Share ##################################
# This function returns the share of investment possibilities to the total. 
# The share is returned in percentages, which should be taken into account...
#... if used in further analysis. 
# =============================================================================

#### The outcomes of interest should be one value per experiment!!
# Create numpy array of the total sum of investments of non-network and network.
total_number_investments_array = np.array(vv.sum()) + np.array(lv.sum())
# Create numpy array of the total sum of the non-network and network costs.
total_costs_array = np.array(vv_costs.sum()) + np.array(lv_costs.sum())

# Create numpy array of the % share of total number of NON-NETWORK ...
#... investments per location.
share_node_1 = np.array(count_loc.loc['Node_1',:]/count_loc.sum()*100)
share_node_2 = np.array(count_loc.loc['Node_2',:]/count_loc.sum()*100)
share_node_3 = np.array(count_loc.loc['Node_3',:]/count_loc.sum()*100)
share_node_4 = np.array(count_loc.loc['Node_4',:]/count_loc.sum()*100)
share_node_5 = np.array(count_loc.loc['Node_5',:]/count_loc.sum()*100)
share_node_6 = np.array(count_loc.loc['Node_6',:]/count_loc.sum()*100)
share_node_7 = np.array(count_loc.loc['Node_7',:]/count_loc.sum()*100)
# Create numpy array of the share of each investment unit to total costs 
share_wind = np.array(count_type_costs.loc['Wind',:])/total_costs_array*100
share_solar = np.array(count_type_costs.loc['Solar',:])/total_costs_array*100
share_HP = np.array(count_type_costs.loc['HP',:])/total_costs_array*100
share_CHP = np.array(count_type_costs.loc['CHP',:])/total_costs_array*100
share_P2G = np.array(count_type_costs.loc['P2G',:])/total_costs_array*100
share_elec_storage = np.array(count_type_costs.loc['Electricity',:])/\
                        total_costs_array*100
share_gas_storage = np.array(count_type_costs.loc['Gas',:])/\
                        total_costs_array*100
share_heat_storage = np.array(count_type_costs.loc['Heat',:])/\
                        total_costs_array*100
share_elec_line = np.array(count_type_line_costs.loc['Electricity',:])/\
                        total_costs_array*100
share_gas_line = np.array(count_type_line_costs.loc['Gas',:])/\
                        total_costs_array*100
share_heat_line = np.array(count_type_line_costs.loc['Heat',:])/\
                        total_costs_array*100