# =============================================================================
# ####################### Sensitivity Analyses ################################
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

######### Feature scoring ##############################################################################
#### NB The standard feature scoring algorithm is extra trees! Use the ...
#... extra trees code to specify specific outcomes of interest ranges. 
from ema_workbench.analysis import feature_scoring

x = experiments
x = x.rename(columns={"demand_index": "Demand", 
                      "dev_rate_conv_P2G": "Development Rate P2G conversion",
                      "dev_rate_solar": "Development Rate PV supply",
                      "dev_rate_storage_elec": "Development Rate E Storage",
                      "dev_rate_wind": "Development Rate Wind supply",
                      "discount_rate": "Discount Rate"})
y = outcomes 

fs = feature_scoring.get_feature_scores_all(x, y)
sns.set(font_scale=1)
sns.heatmap(fs, cmap='viridis', annot=True)
plt.show()

######### Regional Sensitivity Analysis LOOP ########################################################
from ema_workbench.analysis import regional_sa

x = experiments.drop(['policy','model'],axis=1)
x = x.rename(columns={"demand_index": "Demand", 
                      "dev_rate_conv_P2G": "DevRateP2G",
                      "dev_rate_solar": "DevRatePV",
                      "dev_rate_storage_elec": "DevRateEStor",
                      "dev_rate_wind": "DevRateWind",
                      "discount_rate": "DiscRate"})
for key in outcomes_PJ_separate:
    y = outcomes[key] > np.quantile(outcomes_PJ_separate[key],0.75)
    #y = outcomes[key] < np.quantile(outcomes_PJ_separate[key],0.25)
    #y = ((outcomes[key] >= np.quantile(outcomes_PJ_separate[key],0.25))&\
    #(outcomes[key] <= np.quantile(outcomes_PJ_separate[key],0.75)))
    
    fig = regional_sa.plot_cdfs(x,y)
    sns.despine()
    
    plt.savefig('./results/RSA_'+outcomes_nospaces_dict[key]+'_Upper25.png',
                bbox_inches='tight')



######### EXTRA TREES - Global Sensitivity Loop ########################################################
from ema_workbench.analysis.feature_scoring import (get_ex_feature_scores,
                                                    RuleInductionType)

x = experiments.drop(['policy','model'],axis=1)
x = x.rename(columns={"demand_index": "Demand", 
                      "dev_rate_conv_P2G": "DevRateP2G",
                      "dev_rate_solar": "DevRatePV",
                      "dev_rate_storage_elec": "DevRateEStor",
                      "dev_rate_wind": "DevRateWind",
                      "discount_rate": "DiscRate"})
for key in outcomes_PJ_separate:
    y = outcomes[key]

    #NB the default mode is CLASSIFICATION, BUT: REGRESSION should be used.
    all_scores = []
    for i in range(800):
        scores = get_ex_feature_scores(x,y,
                                       mode=RuleInductionType.REGRESSION)[0]
        all_scores.append(scores)
        
    all_scores = pd.concat(all_scores,axis=1,sort=False)
    
    ymax = 0.7
    fig = plt.figure(constrained_layout=True,figsize=(10,10))
    gs = fig.add_gridspec(nrows=2,ncols=1)
    sp1 = fig.add_subplot(gs[0])
    sns.boxplot(data=all_scores.T)
    plt.ylim(0,ymax)
    sp2 = fig.add_subplot(gs[1])
    sns.heatmap(all_scores.T, cmap='viridis', annot=False, vmin=0,vmax=ymax, 
                yticklabels=False)
    
    plt.savefig('./results/ET_'+outcomes_nospaces_dict[key]+'.png',
                bbox_inches='tight')
