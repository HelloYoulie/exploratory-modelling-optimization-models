# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:42:07 2019

@author: JulieFr
"""



############ConnectToEMAWorkbench################

from ema_workbench import (RealParameter, ScalarOutcome, Constant,
                           ema_logging, CategoricalParameter, MultiprocessingEvaluator,
                           ArrayOutcome, SequentialEvaluator, save_results)
from ema_workbench.em_framework.model import WorkingDirectoryModel, SingleReplication
from ema_workbench.util.ema_logging import method_logger, get_module_logger

from Model_Foresight_EMA_Excel import optim_model  # @UnresolvedImport
import pandas as pd
import os


_logger = get_module_logger(__name__)

class PyomoModel(SingleReplication, WorkingDirectoryModel):
    
    @method_logger(__name__)
    def model_init(self, policy):
        super(PyomoModel, self).model_init(policy)
        
            
        ###################IMPORT DATA#################################################
        # Retrieving dataframes from MS access DB and creating dictionaries
        #db_file= './7_nodes_voorPython_with_time_2018.xlsx'
        db_file = os.path.join(self.working_directory, 
                               '7_nodes_voorPython_with_time_2018_WithScenarios.xlsx')
        db_file = pd.ExcelFile(db_file)
        
        #Read data from the excel datafiles 
        #This only needs to occur once for the entire analysis if the data are...
        #... changed manually inside these tables. 
        _logger.info("Connecting to database")
        
        self.df_conversion_efficiencies = db_file.parse('ConversionEfficiencies')
        self.df_conversion_units = db_file.parse('ConversionUnits')
        self.df_demand = db_file.parse('Demand')
        self.df_locations = db_file.parse('Locations')
        self.df_max_converted = db_file.parse('MaxConverted')
        self.df_max_flow = db_file.parse('MaxFlow')
        self.df_network = db_file.parse('Network')
        self.df_storage_units = db_file.parse('StorageUnits')
        self.df_supply = db_file.parse('Supply')
        self.df_supply_units = db_file.parse('SupplyUnits')
        # 2-year time periods
        self.df_time_periods = db_file.parse('TimePeriods')
        
        db_file.close()
        
    @method_logger(__name__)
    def run_experiment(self, experiment):
        _logger.debug("running model")
        
        output = optim_model(df_conversion_efficiencies=self.df_conversion_efficiencies,
                    df_conversion_units=self.df_conversion_units,
                    df_locations=self.df_locations,
                    df_max_converted=self.df_max_converted,
                    df_max_flow=self.df_max_flow, df_network=self.df_network,
                    df_storage_units=self.df_storage_units,
                    df_supply_units=self.df_supply_units,
                    df_time_periods=self.df_time_periods, 
                    df_demand=self.df_demand, df_supply=self.df_supply,
                    **experiment)
        
        results = {}
        for i, variable in enumerate(self.output_variables):
            try:
                value = output[variable]
            except KeyError:
                _logger.warning(variable + ' not found in model output')
                value = None
            except TypeError:
                value = output[i]
            results[variable] = value
        return results

    
if __name__ == '__main__':

    ###################IMPORT DATA#################################################
    # Retrieving dataframes from MS access DB and creating dictionaries
    #db_file= './7_nodes_voorPython_with_time_2018.xlsx'
    db_file= './data/7_nodes_voorPython_with_time_2018_WithScenarios.xlsx'
    db_file = pd.ExcelFile(db_file)
    
    #Read data from the excel datafiles 
    #This only needs to occur once for the entire analysis if the data are...
    #... changed manually inside these tables. 
    print("Connecting to database")
    df_conversion_efficiencies = db_file.parse('ConversionEfficiencies')
    df_conversion_units = db_file.parse('ConversionUnits')
    df_demand = db_file.parse('Demand')
    df_locations = db_file.parse('Locations')
    df_max_converted = db_file.parse('MaxConverted')
    df_max_flow = db_file.parse('MaxFlow')
    df_network = db_file.parse('Network')
    df_storage_units = db_file.parse('StorageUnits')
    df_supply = db_file.parse('Supply')
    df_supply_units = db_file.parse('SupplyUnits')
    df_time_periods = db_file.parse('TimePeriods')

    #model = Model('simpleModel', function=optim_model)
    ###############################################################################
    #ema_logging.LOG_FORMAT = '[%(name)s/%(levelname)s/%(processName)s] %(message)s'
    ema_logging.log_to_stderr(ema_logging.DEBUG)
    
    ##############################################################################
    model = PyomoModel('simpleModel', wd='./data')  # instantiate the model
    ##############################################################################
        
    # specify uncertainties
    model.uncertainties = [CategoricalParameter('demand_index',(3,4,5,6,7,8,9,10,
                                                                11,12,13,14)),
                           RealParameter('dev_rate_wind',0.011,0.033),#0.022 is estimated base value
                           RealParameter('dev_rate_solar',0.025,0.075),#0.05 is estimated base value
                           RealParameter("dev_rate_storage_elec",0.025,0.075),#0.05 is estimated base value
                           #RealParameter("dev_rate_storage_heat",0.0125,0.0375),#0.016 is estimated base value
                           RealParameter("dev_rate_conv_P2G",0.0395,0.1185),#0.079 is estimated base value
                           #RealParameter("dev_rate_conv_HP",0.0125,0.0375),#0.01 is estimated base value
                           RealParameter("discount_rate",0.01,0.15)] #'base value' is 0.04. 
    
    # specify outcomes    
    model.outcomes = [ArrayOutcome('value_vector'),
                      ArrayOutcome('line_value'),
                      ArrayOutcome('cost_vector'),
                      ArrayOutcome('line_cost_vector'),
                      ScalarOutcome('stopping_condition')] 

    ##############################################################################
    # Use small number of experiments to quickly test the model and EMA workbench. 
    #experiments, outcomes = perform_experiments(model, 2)
    
    #Open exploration 
    n_experiments = 800
    
    with MultiprocessingEvaluator(model) as evaluator:
        results = evaluator.perform_experiments(n_experiments)
        
    save_results(results, 
                 f'./results/{n_experiments }experiments_300s_7%.tar.gz')
    
   
