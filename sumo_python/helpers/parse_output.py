import os
import pandas as pd
import numpy as np

def parse_loop_data(config: dict,loop_file: dict):
    """Read the Loop Detectors Data: Each SUMO run produces a file with the
    traffic counts. This function reads the corresponding traffic counts file
    averages across simulation replications
    """        

    output_file =(config["NETWORK"] / "loopOutputs.csv")
    data2csv = (
        f"python {config['SUMO']}/tools/xml/xml2csv.py "
        f"{config['NETWORK']/loop_file} "
        f"--x {config['SUMO']}/data/xsd/det_e1_file.xsd " 
        f"-o {output_file}"
        )

    os.system(data2csv)

    df_trips = pd.read_csv(output_file, sep=";", header=0)
    df_trips["EdgeID"] = [elem.split("_")[1] for elem in df_trips["interval_id"]]
    df_trips_grouped = df_trips\
            .groupby(by=['EdgeID','interval_begin','interval_end'], as_index=False)\
            .agg({
                'interval_nVehContrib':np.sum,
                'interval_harmonicMeanSpeed':np.mean
                }
            )

    return df_trips_grouped