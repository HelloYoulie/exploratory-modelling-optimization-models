# =============================================================================
# ################# Kernel Density Estimates Plots ############################
# =============================================================================
import seaborn as sns
import matplotlib as plt

for ooi in outcomes:
    plt.figure()
    kdeplot = sns.distplot(outcomes[ooi])
    plt.xlabel(ooi)
    plt.ylabel('Probability density')
    plt.ylim(0,3)
    plt.savefig('./results/ProbabDens_'+outcomes_nospaces_dict[ooi]+'.png',
                bbox_inches='tight')
    