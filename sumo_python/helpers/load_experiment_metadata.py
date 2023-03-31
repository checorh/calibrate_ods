import json
from pathlib import Path
from typing import Union

def load_experiment_config(
                        config: Union[Path, str]="config.json",
                        sim_setup: Union[Path, str]="simulation_setups.json"
    ):
    """Load paths, simulation setups and algorithm setups
    

    Parameters
    ----------
    config : Union[Path, str], optional
        Paths to cache, network, and SUMO. The default is "config.json".
    sim_setup : Union[Path, str], optional
        Simulation parameters. The default is "simulation_setups.json".

    Returns
    -------
    config : Dictionary
    sim_setup : Dictionary

    """
    config = Path(config) if isinstance(config, str) else config
    config = json.load(open(config))
    for k, v in config.items():
        config[k] = Path(v)
    
    sim_setup = Path(sim_setup) if isinstance(sim_setup, str) else sim_setup
    sim_setup = json.load(open(sim_setup))
    for k, v in sim_setup.items():
        sim_setup[k] = v
            
    return config, sim_setup
