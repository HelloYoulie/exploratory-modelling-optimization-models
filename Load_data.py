from __future__ import (absolute_import, print_function, division, \
                        unicode_literals)
from ema_workbench import load_results
# ####################### IMPORT DATA #########################################
# =============================================================================

results = load_results('./800experiments_300s_7%_ForReal.tar.gz')

experiments, outcomes = results