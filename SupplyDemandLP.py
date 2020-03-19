# =============================================================================
# ########################### Supply / Demand  LINE PLOTS #####################
# =============================================================================        
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
           
supplydemand_composition_dict = {'Wind supply':wind_PJ,
                                 'Solar supply':solar_PJ,
                                 'Gas supply':gas_supply_PJ,
                                 'Demand':demand_PJ}
                         
supplydemand_color_dict = {'Wind supply':'b',
                           'Solar supply':'orange',
                           'Gas supply':'r',
                           'Demand':'g'}

x = [2018,2020,2022,2024,2026,2028,2030,2032,2034,2036,2038,2040,2042,2044,
     2046,2048,2050]

# Cumulative PJ demand, enveloppe plot and end state density (2050) of all...
# ... 12 demand timeseries. 
demand = df_demand.groupby('TimePeriod').agg('sum')

ymax = 25
fig7 = plt.figure(constrained_layout=True,figsize=(20,8))
gs7 = fig7.add_gridspec(nrows=1, ncols=20)
for col in demand.columns:
    fig7_sp1 = fig7.add_subplot(gs7[0,:9])
    plt.plot(x,demand[col],label=col)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Total demand (PJ)',size=16)
    plt.ylim(0,ymax)
fig7_sp2 = fig7.add_subplot(gs7[0,17])
sns.distplot(demand.loc[2050],
            vertical=True)
plt.xlabel('Density')
plt.ylim(0,ymax)
fig7_sp2 = fig7.add_subplot(gs7[0,9:17])
plt.ylim(0,ymax)
plt.plot(x,np.median(demand,axis=1),label = 'Median of experiments')
plt.fill_between(x,np.quantile(demand,0.75,axis=1),
                 np.quantile(demand,0.25,axis=1),alpha = 0.4,
                 label = 'Middle 50% of experiments')
plt.fill_between(x,demand[(np.argmin(demand.loc[2050]))],
                          demand[(np.argmax(demand.loc[2050]))], alpha = 0.3,
                          label = '100% of experiments')
plt.label()
plt.xlabel('Time')

# Plot the SUPPLY DISTRIBUTIONS over all experiments
fig7 = plt.figure(constrained_layout=True,figsize=(20,8))
gs7 = fig7.add_gridspec(nrows=1, ncols=20)
ymax = 17
for key in supplydemand_composition_dict:
    fig7_sp1 = fig7.add_subplot(gs7[0,:6])
    plt.plot(x, np.median(supplydemand_composition_dict[key],axis=1), 
            label = key,color=supplydemand_color_dict[key])
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Total capacity (PJ)',size=16)
    plt.ylim(0,ymax)
    fig7_sp2 = fig7.add_subplot(gs7[0,17])
    sns.distplot(supplydemand_composition_dict[key].loc[2050],
            vertical=True, color = supplydemand_color_dict[key])
    plt.ylim(0,ymax)
    plt.xlim(0,8)
    plt.xlabel('Density')
    fig7_sp3 = fig7.add_subplot(gs7[0,6:17])
    plt.plot(x,np.median(supplydemand_composition_dict[key],axis=1),
             supplydemand_color_dict[key],
             label = 'Median of '+ key + ' experiments')
    plt.fill_between(x,
            np.quantile(supplydemand_composition_dict[key],0.75,axis=1),
            np.quantile(supplydemand_composition_dict[key],0.25,axis=1), 
            facecolor = supplydemand_color_dict[key], alpha = 0.4,
            label = 'Middle 50% of '+ key + ' experiments')
    if(key=='Demand'):
            plt.fill_between(x,
            supplydemand_composition_dict[key]\
            [(np.argmin(supplydemand_composition_dict[key]\
                        .loc[2050]))].iloc[:,0],
            supplydemand_composition_dict[key]\
            [(np.argmax(supplydemand_composition_dict[key]\
                        .loc[2050]))].iloc[:,0],
            facecolor = supplydemand_color_dict[key], alpha = 0.3,
            label = '100% of '+ key + ' experiments')
    else:
            plt.fill_between(x,
            supplydemand_composition_dict[key]\
            [(np.argmin(supplydemand_composition_dict[key].loc[2050]))],
            supplydemand_composition_dict[key]\
            [(np.argmax(supplydemand_composition_dict[key].loc[2050]))],
            facecolor = supplydemand_color_dict[key], alpha = 0.3,
            label = '100% of '+ key + ' experiments')
    plt.xlabel('Time')
    plt.legend(loc='upper left')
    plt.ylim(0,ymax)
    