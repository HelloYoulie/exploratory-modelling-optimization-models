# =============================================================================
# ###################### GENERAL LINE PLOTS ###################################
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

type_color_dict = {'CHP':'c', 
                   'Electricity':'#00f467', 
                   'Gas':'r',
                   'HP':'m',
                   'Heat':'#373a6f',
                   'P2G':'y',
                   'Solar':'g',
                   'Wind':'b'}

type_lines_color_dict = {'Electricity':'#f65f1d', 
                         'Gas':'k',
                         'Heat':'#66f61d'}
                         
type_PJ_dict = {'CHP':chp_PJ, 
                'Electricity':elec_PJ, 
                'Gas':gas_PJ,
                'HP':hp_PJ,
                'Heat':heat_PJ,
                'P2G':p2g_PJ,
                'Solar':solar_PJ,
                'Wind':wind_PJ}

type_lines_PJ_dict = {'Electricity':elec_line_PJ, 
                         'Gas':gas_line_PJ,
                         'Heat':heat_line_PJ}    


x = [2018,2020,2022,2024,2026,2028,2030,2032,2034,2036,2038,2040,2042,2044,
     2046,2048,2050]
 
# Non-network cumulative costs, enveloppe plot and end state density (2050)    
# Non-network cumulative number of investments, enveloppe plot & ...
#...end state density (2050)    
for key in type_color_dict:
    ymax = np.cumsum(count_type_year_costs.loc[key])\
            [(np.argmax(np.cumsum(count_type_year_costs.loc[key]).loc[2050]))]\
            .loc[2050] + 2
    ymax = 40
    fig7 = plt.figure(constrained_layout=True,figsize=(20,12))
    gs7 = fig7.add_gridspec(nrows=2, ncols=20)
    fig7_sp1 = fig7.add_subplot(gs7[0,:9])
    plt.plot(x,np.cumsum(count_type_year_costs.loc[key]))
    plt.ylabel('Cumulative costs of investment in '+ key,size=16)
    plt.title(key,size=16)
    plt.ylim(0,ymax)
    fig7_sp1 = fig7.add_subplot(gs7[0,17])
    sns.distplot(np.cumsum(count_type_year_costs.loc[key]).loc[2050],
                vertical=True, color = type_color_dict[key])
    plt.ylim(0,ymax)
    fig7_sp2 = fig7.add_subplot(gs7[0,9:17])
    plt.ylim(0,ymax)
    plt.plot(x,np.median(np.cumsum(count_type_year_costs.loc[key]),axis=1),
             type_color_dict[key], label = 'Median of experiments')
    plt.fill_between(x,
            np.quantile(np.cumsum(count_type_year_costs.loc[key]),0.75,axis=1),
            np.quantile(np.cumsum(count_type_year_costs.loc[key]),0.25,axis=1), 
            facecolor = type_color_dict[key], alpha = 0.4, 
            label = 'Middle 50% of experiments')
    plt.fill_between(x,
            np.cumsum(count_type_year_costs.loc[key])\
            [(np.argmin(np.cumsum(count_type_year_costs.loc[key]).loc[2050]))],
            np.cumsum(count_type_year_costs.loc[key])\
            [(np.argmax(np.cumsum(count_type_year_costs.loc[key]).loc[2050]))], 
            facecolor = type_color_dict[key], alpha = 0.3, 
            label = '100% of experiments') 
    plt.legend()        
    #######
    ymax = 25
    fig7_sp1 = fig7.add_subplot(gs7[1,:9])
    plt.plot(x,type_PJ_dict[key])
    plt.xlabel('Time')
    plt.ylabel('Cumulative capacity (PJ) of investment in '+ key,size=16)
    plt.ylim(0,ymax)
    fig7_sp1 = fig7.add_subplot(gs7[1,17])
    sns.distplot(type_PJ_dict[key].loc[2050],
                vertical=True, color = type_color_dict[key])
    plt.ylim(0,ymax)
    fig7_sp2 = fig7.add_subplot(gs7[1,9:17])
    plt.xlabel('Density')
    plt.ylim(0,ymax)
    plt.plot(x,np.median(type_PJ_dict[key],axis=1),type_color_dict[key], 
             label = 'Median of experiments')
    plt.fill_between(x,
            np.quantile(type_PJ_dict[key],0.75,axis=1),
            np.quantile(type_PJ_dict[key],0.25,axis=1), 
            facecolor = type_color_dict[key], alpha = 0.4, 
            label = 'Middle 50% of experiments')    
    plt.fill_between(x,
            type_PJ_dict[key]\
            [(np.argmin(type_PJ_dict[key].loc[2050]))],type_PJ_dict[key]\
            [(np.argmax(type_PJ_dict[key].loc[2050]))],
            facecolor = type_color_dict[key], alpha = 0.3, 
            label = '100% of experiments')
    plt.xlabel('Time')
    plt.legend()
    plt.savefig('./results/LinePlot_'+key+'.png',
                bbox_inches='tight')


# Network cumulative costs, enveloppe plot and end state density (2050)    
# Network cumulative number of investments, enveloppe plot and &...
#... state density (2050)    
for key in type_lines_color_dict:
    ymax = np.cumsum(count_type_year_line_costs.loc[key])\
            [(np.argmax(np.cumsum(count_type_year_line_costs.loc[key]).loc[2050]))]\
            .loc[2050] + 2
    ymax = 40
    fig7 = plt.figure(constrained_layout=True,figsize=(20,12))
    gs7 = fig7.add_gridspec(nrows=2, ncols=20)
    fig7_sp1 = fig7.add_subplot(gs7[0,:9])
    plt.plot(x,np.cumsum(count_type_year_line_costs.loc[key]))
    plt.ylabel('Cumulative costs of investments ' + key + ' network',size=14)
    plt.title(key+' network',size=16)
    plt.ylim(0,ymax)
    fig7_sp2 = fig7.add_subplot(gs7[0,17])
    sns.distplot(np.cumsum(count_type_year_line_costs.loc[key]).loc[2050],
                vertical=True, color = type_lines_color_dict[key])
    plt.ylim(0,ymax)
    fig7_sp2 = fig7.add_subplot(gs7[0,9:17])
    plt.ylim(0,ymax)
    plt.plot(x,np.median(np.cumsum(count_type_year_line_costs.loc[key]),axis=1),
             type_lines_color_dict[key], label = 'Median of experiments')
    plt.fill_between(x,
            np.cumsum(count_type_year_line_costs.loc[key])\
            [(np.argmin(np.cumsum(count_type_year_line_costs.loc[key]).loc[2050]))],
            np.cumsum(count_type_year_line_costs.loc[key])\
            [(np.argmax(np.cumsum(count_type_year_line_costs.loc[key]).loc[2050]))], 
            facecolor = type_lines_color_dict[key], alpha = 0.3, 
            label = 'Middle 50% of experiments')
    plt.fill_between(x,
            np.quantile(np.cumsum(count_type_year_line_costs.loc[key]),0.75,axis=1),
            np.quantile(np.cumsum(count_type_year_line_costs.loc[key]),0.25,axis=1), 
            facecolor = type_lines_color_dict[key], alpha = 0.4, 
            label = '100% of experiments')
    plt.legend()
    #######
    ymax = 25
    fig7_sp1 = fig7.add_subplot(gs7[1,:9])
    plt.plot(x,type_lines_PJ_dict[key])
    plt.xlabel('Time')
    plt.ylabel('Cumulative capacity (PJ) of investment in '+ key + ' network',
               size=14)
    plt.ylim(0,ymax)
    fig7_sp1 = fig7.add_subplot(gs7[1,17])
    sns.distplot(type_lines_PJ_dict[key].loc[2050],
                vertical=True, color = type_lines_color_dict[key])
    plt.ylim(0,ymax)
    fig7_sp2 = fig7.add_subplot(gs7[1,9:17])
    plt.xlabel('Density')
    plt.ylim(0,ymax)
    plt.plot(x,np.median(type_lines_PJ_dict[key],axis=1),type_lines_color_dict[key], 
             label = 'Median of experiments')
    plt.fill_between(x,
            type_lines_PJ_dict[key]\
            [(np.argmin(type_lines_PJ_dict[key].loc[2050]))],
            type_lines_PJ_dict[key]\
            [(np.argmax(type_lines_PJ_dict[key].loc[2050]))],
            facecolor = type_lines_color_dict[key], alpha = 0.3, 
            label = 'Middle 50% of experiments')
    plt.fill_between(x,
            np.quantile(type_lines_PJ_dict[key],0.75,axis=1),
            np.quantile(type_lines_PJ_dict[key],0.25,axis=1), 
            facecolor = type_lines_color_dict[key], alpha = 0.4, 
            label = '100% of experiments')
    plt.xlabel('Time')
    plt.legend()
    plt.savefig('./results/LinePlot_'+key+'_network.png',
                bbox_inches='tight')
