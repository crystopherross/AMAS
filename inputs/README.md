# Inputs
This folder contains the input `.json` files to be used in conjuction with the `read_amas_from_json` function defined in `../read_input.py`. This `README.md` file specifies the structure of these files. This folder also contains two examples (used in our bachelor thesis), namely `train_controller_success.json` and `train_controller_fail.json`.

## File Format
The `.json` file should specify a JSON list of objects. Each of these objects have the following attributes:
- "name": string
- "number": integer
- "L": string list
- "i": string
- "Evt": string list
- "R": an object with each element in "L" as an attribute. Each of these attributes is a list of lists of strings.
- "T": a list of lists of strings, the nested lists should more specifically have 3 elements each.
- "PV": string list
- "V": an object with each element in "L" as an attribute. Each of these attributes is a list of strings.

Each of these objects represent the definition of an AMAS agent. The description of what these attributes represent follows:

- "name": The name of the agent, for display purposes
- "number": The enumeration of the agent, starting from 0, the agents defined in the object should together have the enumerations `0, 1,..., n-1` if `n` agents are defined, in that specific order.
- "L": The list of local states of the agent.
- "i": The initial local state of the agent.
- "Evt": The events available to the agent.
- "R": The repertoire function of the agent, each attribute should be an element in "L", to which it is associated a list of lists containing elements of "Evt"
- "T": The local transition relation of the agent, it is a list of triples, 1st and 3rd components should be elements of "L", the 2nd component should be an element of "Evt". These triples are represented as JSON lists with precisely 3 elements.  
