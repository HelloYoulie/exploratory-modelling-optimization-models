###########################Specify Outcomes of Interest #######################
import numpy as np

# Dictionary consisting of numpy arrays and keys of the outcomes of interest.
outcomes_costs = {'Total costs': total_costs_array, 
                  'Total # investments': total_number_investments_array,
                  '% of investment costs by wind': share_wind,
                  '% of investment costs by PV': share_solar,
                  '% of investment costs by HP': share_HP,
                  '% of investment costs by CHP': share_CHP,
                  '% of investment costs by P2G': share_P2G,
                  '% of investment costs by elec storage': share_elec_storage,
                  '% of investment costs by gas storage': share_gas_storage,
                  '% of investment costs by heat storage': share_heat_storage,
                  '% of investment costs by elec line': share_elec_line,
                  '% of investment costs by gas line': share_gas_line,
                  '% of investment costs by heat line': share_heat_line}
                  
outcomes_count = {'Total costs': total_costs_array,
                  'Total # investments': total_number_investments_array,
                  '% of # non-line investments at node 1': share_node_1,
                  '% of # non-line investments at node 2': share_node_2,
                  '% of # non-line investments at node 3': share_node_3,
                  '% of # non-line investments at node 4': share_node_4,
                  '% of # non-line investments at node 5': share_node_5,
                  '% of # non-line investments at node 6': share_node_6,
                  '% of # non-line investments at node 7': share_node_7}
                  
outcomes_PJ = {'Total costs (MEur)': total_costs_array,
               'Total # investments': total_number_investments_array,
               'Total supply capacity (PJ)': \
               np.array(total_supply_PJ.loc[2050]),
               'Total storage capacity (PJ)': \
               np.array(total_storage_PJ.loc[2050]),
               'Total conversion capacity (PJ)': \
               np.array(total_conversion_PJ.loc[2050]),
               'Total network capacity (PJ)': np.array(total_line_PJ.loc[2050])}

outcomes_PJ_separate = {'Total costs (MEur)': total_costs_array,
                        'Total # investments': total_number_investments_array,
                        'Total wind capacity (PJ)': np.array(wind_PJ.loc[2050]),
                        'Total PV capacity (PJ)': np.array(solar_PJ.loc[2050]),
                        'Total gas storage capacity (PJ)': \
                        np.array(gas_PJ.loc[2050]),
                        'Total heat storage capacity (PJ)': \
                        np.array(heat_PJ.loc[2050]),
                        'Total CHP capacity (PJ)': np.array(chp_PJ.loc[2050]),
                        'Total HP capacity (PJ)': np.array(hp_PJ.loc[2050]),
                        'Total P2G capacity (PJ)': np.array(p2g_PJ.loc[2050]),
                        'Total network capacity (PJ)': \
                        np.array(total_line_PJ.loc[2050])}

outcomes_nospaces_dict = {'Total costs (MEur)': 'costs',
                        'Total # investments': 'number_investments',
                        'Total wind capacity (PJ)': 'wind_PJ',
                        'Total PV capacity (PJ)': 'solar_PJ',
                        'Total gas storage capacity (PJ)': 'gas_PJ',
                        'Total heat storage capacity (PJ)': 'heat_PJ',
                        'Total CHP capacity (PJ)': 'chp_PJ',
                        'Total HP capacity (PJ)': 'hp_PJ',
                        'Total P2G capacity (PJ)': 'p2g_PJ',
                        'Total network capacity (PJ)': 'network_PJ'}

results = (experiments,outcomes)

###### SPECIFY which OutcomesOfInterest-vector to be used in results analysis
outcomes = outcomes_PJ_separate