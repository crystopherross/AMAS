import amas
import json

def read_amas_from_json(file_name):
    """Read a .json file in the 'Inputs' folder of this project and build an AMAS out of its contents."""
    with open("./inputs/" + file_name + ".json", 'r') as handle:
        data = json.load(handle)
        agents: list[amas.AMASagent] = []
        for agent_data in data:
            # Convert nested json lists to tuples for the "T" attribute
            agent_data["T"] = list(map(tuple, agent_data["T"]))
            agents.append(
                amas.AMASagent(
                    agent_data["name"], 
                    agent_data["number"], 
                    agent_data["L"], 
                    agent_data["i"], 
                    agent_data["Evt"], 
                    agent_data["R"], 
                    agent_data["T"], 
                    agent_data["PV"], 
                    agent_data["V"]
                )
            )
        return amas.AMAS(agents)