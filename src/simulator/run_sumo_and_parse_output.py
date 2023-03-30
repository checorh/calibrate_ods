import pandas as pd
import numpy as np
from .sumo import run_sumo
from ..helpers.parse_output import parse_loop_data

def run_sumo_and_parse_output(config, sim_setup, prefix_sim_run): 
    """Read and parse SUMO outputs.
    
    """    
    #np.random.seed(11)
    # random_seeds = np.random.normal(0, 10000, sim_setup["n_sumo_replicate"]).astype("int32")
    for replic_counter in range(sim_setup["n_sumo_replicate"]):

        # Run simulation
        print(f'### Runing: {prefix_sim_run}')
        run_sumo(config, sim_setup, prefix_sim_run) #, random_seeds[counter])

        if sim_setup["objective"] == "counts":
            loop_file = f"{prefix_sim_run}_out.xml"
            df_agg = parse_loop_data(config, loop_file)

            if replic_counter==0:
                df_loop = df_agg.copy()
            else:
                df_loop = pd.concat([df_loop, df_agg], axis=0)
                

    if sim_setup["objective"] == "counts":
        # speeds across lanes are being averaged arithmetically not with harmonic mean
        df_output = df_loop\
            .groupby(by=['EdgeID','interval_begin','interval_end'], 
            as_index=False)\
        .agg(
            {'interval_nVehContrib':np.mean,
            'interval_harmonicMeanSpeed':np.mean
            }
        )

        return df_output