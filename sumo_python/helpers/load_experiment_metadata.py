import json
from pathlib import Path

def load_experiment_metadata(input_path: str):

    config = json.load(open(input_path + "/config.json"))
    config["NETWORK"] = Path(config["NETWORK"])
    config["SUMO"] = Path(config["SUMO"])
    
    sim_setup = json.load(open(input_path + "simulation_setups.json"))

    return config, sim_setup
