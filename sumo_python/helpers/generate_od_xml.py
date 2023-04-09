import numpy as np

import xml.etree.ElementTree as ET
from pathlib import Path


def generate_od_xml(x, config, sim_setup, prefix_run):

    # check if initial 
    init_od_path = f"{config['NETWORK']}/{sim_setup['init_od']}"
    if Path(init_od_path).is_file():
        print("Reading:",init_od_path)
        tree = ET.parse(init_od_path)
        root = tree.getroot()

        for i,x in enumerate(x):
            root[0][i].attrib["count"] = str(np.round(x))
            
    file_name = f"{config['NETWORK']}/{prefix_run}_{sim_setup['current_od']}"
    print('Saving: '+file_name)
    tree.write(file_name)
