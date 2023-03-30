import numpy as np

def generate_od_xml(od_rand, config, sim_setup, prefix_run):
    """
    The tazRelation format defines the demand per OD pair in time slices for 
    every a given vehicle type as follows:

        <data xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/datamode_file.xsd">
            <interval id="car" begin="0" end="1:0:0">
            <tazRelation count="2000" from="1" to="2"/>
            <tazRelation count="500" from="1" to="3"/>
            ...
            </interval>
            <interval ...>
            ...
        </data>

    See: https://sumo.dlr.de/docs/Demand/Importing_O/D_Matrices.html#tazrelation_format
    """
    # print od in xml file

    od_xml_str = (
        f"<?xml version=\"1.0\" encoding=\"UTF-8\"?> \n"
        f"<data xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"http://sumo.dlr.de/xsd/datamode_file.xsd\">\n"
        f"<interval id=\"CarA\" begin=\"54000\" end=\"57600.0\">\n"
        f"<tazRelation from=\"taz91\" to=\"taz93\" count=\"{int(np.floor(od_rand[0]))}\"/>\n"
        f"<tazRelation from=\"taz91\" to=\"taz94\" count=\"{int(np.floor(od_rand[1]))}\"/>\n"
        f"<tazRelation from=\"taz92\" to=\"taz93\" count=\"{int(np.floor(od_rand[2]))}\"/>\n"
        f"<tazRelation from=\"taz92\" to=\"taz94\" count=\"{int(np.floor(od_rand[3]))}\"/>\n"
        f"</interval>\n"
        f"</data>"
    )

    file_name = f"{config['NETWORK']}/{prefix_run}_{sim_setup['current_od']}"
    print('printing '+file_name)
    f = open(file_name,'w')
    f.write(od_xml_str) 
    f.close()
