#################PERCENTAGE SOLVED TO OPTIMALITY###############################
import numpy as np
# Stopping_condition has value 1 for experiments solved to optimality ...
#... and value 0 for experiment stopped due to time constraints and did ...
#... not reach optimality. 
percentage_optimal = (np.count_nonzero(outcomes['stopping_condition'])/ \
                        len(outcomes['stopping_condition']))*100
                        