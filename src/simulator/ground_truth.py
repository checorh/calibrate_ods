import os
import pandas as pd
import numpy as np

from calibrate_ods.src.helpers.parse_output import parse_loop_data


def run_ground_truth_and_parse(config, sim_setup):
    """Read and parse SUMO outputs.
    This function evaluates grand-truth (GT).
    """    
    # currently defined for a single simulation replication
    
    #np.random.seed(11)
    # random_seeds = np.random.normal(0, 10000, sim_setup["n_sumo_replicate"]).astype("int32")

    # Run od2trips_cmd to generate trips file
    od2trips_cmd = (
        f"od2trips --no-step-log  --spread.uniform "
        f"--taz-files {config['NETWORK']}/{sim_setup['taz']} "
        f"--tazrelation-files {config['NETWORK']}/{sim_setup['gt_od']} "
        f"-o {config['NETWORK']}/gt_od_trips.trips.xml "
        )
        # f"--seed {seed}"
        # --output-prefix {k}
    print(od2trips_cmd)
    os.system(od2trips_cmd)
    
    # Run SUMO to generate outputs
    sumo_run = (
        f"sumo --output-prefix gt_ "
        f"--ignore-route-errors=true "
        f"--net-file={config['NETWORK']/sim_setup['net']} "
        f"--routes={config['NETWORK']}/gt_od_trips.trips.xml "
        f"-b {sim_setup['start_sim_sec']} -e {sim_setup['end_sim_sec']} "
        f"--additional-files {config['NETWORK']/sim_setup['add']} "
        f"--duration-log.statistics "
        f"--xml-validation never "
        f"--vehroutes {config['NETWORK']}/gt_routes.vehroutes.xml "
        )
        # f"--seed {seed}"
    print(sumo_run)
    os.system(sumo_run)
    

    if sim_setup["objective"] == "counts":
        loop_file = "gt_out.xml"
        df1 = parse_loop_data(config, loop_file)

        df_output = df1.groupby(by=['EdgeID','interval_begin','interval_end'], as_index=False)\
            .agg(
            {
                'interval_nVehContrib':np.sum, 
                'interval_harmonicMeanSpeed':np.mean
            }
        )

        return df_output

    # speeds across lanes are being averaged arithmetically not with harmonic mean
