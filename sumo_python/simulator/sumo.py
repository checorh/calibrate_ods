import os

def run_sumo(config,
            sim_setup,
            prefix_sim_run):
    """   
    See: https://sumo.dlr.de/docs/Demand/Importing_O/D_Matrices.html

    Args:
        config (_type_): _description_
        sim_setup (_type_): _description_
        algo_iter (_type_): _description_
        replic_iter (_type_): _description_
    """
    # Run OD2Trips and SUMO simulation.

    # p_reroute = 0.1 # rerouting probability
    # Run od2trips_cmd to generate trips file
    od2trips_cmd = (
        f"od2trips --no-step-log  --spread.uniform "
        #Loads TAZ (districts)
        f"--taz-files {config['NETWORK']}/{sim_setup['taz']} " 
        # Loads O/D-matrix in tazRelation format fromFILE(s)
        f"--tazrelation-files {config['NETWORK']}/{prefix_sim_run}_{sim_setup['current_od']} "
        # Writes trip definitions into FILE
        f"-o {config['NETWORK']}/{prefix_sim_run}_od_trips.trips.xml " 
        )
        # f"--seed {seed}"
        # --output-prefix {k}

    # Run SUMO to generate outputs
    sumo_run = (
        # Prefix which is applied to all output files. 
        f"sumo --output-prefix {prefix_sim_run}_ " 
        # Do not check whether routes are connected
        f"--ignore-route-errors=true "
        # Load road network description from FILE
        f"--net-file={config['NETWORK']/sim_setup['net']} "
        # Load routes descriptions from FILE(s)
        f"--routes={config['NETWORK']}/{prefix_sim_run}_od_trips.trips.xml "
        #  -b Defines the begin time in seconds; The simulation starts at this time
        # -e Defines the end time in seconds; The simulation ends at this time
        f"-b {sim_setup['start_sim_sec']} -e {sim_setup['end_sim_sec']} "
        # Load further descriptions from FILE(s)
        f"--additional-files {config['NETWORK']/sim_setup['add']} "
        f"--duration-log.statistics "
        f"--xml-validation never "
        # Save single vehicle route info into FILE
        f"--vehroutes {config['NETWORK']}/routes.vehroutes.xml "
        )
        # f"--seed {seed}"

    try:
        print(od2trips_cmd)
        os.system(od2trips_cmd)
    except:
        print("Unable to create trips file")
    else:
        #print(sumo_run)
        os.system(sumo_run)
