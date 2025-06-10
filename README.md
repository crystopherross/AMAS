# AMAS
## Introduction
This repository contains an implementation of AMAS and its structures defined by Gurov et al. [1], relevant for our bachelor's thesis. This README file will contain information about the usage of the tool.

## Installation
To use this tool, simply clone this repository and begin using it. As of now the tool assumes that all usage is done within the cloned repository. An example of usage can be found in `main.py`.

## Input
The inputs of this tool are `.json` files located in the `./inputs/` directory. More information on the format of these `.json` files is found in the `README.md` file in the `./inputs/` directory. The file `read_input.py` contains the function that reads a `.json` file located in `./inputs/` and constructs an AMAS object with it. JSON files were chosen due to their standard use in structured data and it being enough to encode all that an AMAS requires for its construction. Alternatively, the users can import the `AMAS` class in `amas.py` and call its constructor with correct arguments.

## Classes
The classes implemented in this tool represent the structures AMAS, I/O iCGS, and projections as defined in [1]. Each class and its attributes are documented in the code, a short summary of each follows. Each of the classes also implement a `.print()` method that prints the structure either to the console or to a file with a specified name in the `./outputs/` folder.
### AMASagent
Represents an agent in an AMAS, its attributes represent the components in an AMAS agent (local states, initial state, repertoire function, etc.). It has methods for MKBSC expansion (provided an I/O iCGS and projection on it). Upon calling the constructor of this class, it validates the input received, prompting helpful error messages if something goes wrong during the construction. The implementation of this class lies in `amas.py`.
### AMAS
Represents an AMAS structure as defined in [1], it is mainly described as a (ordered) list of `AMASagent` objects. It has methods for constructing I/O iCGS from it (`.joint_game()`), and MKBSC projection (`.project()`) and expansion (`.expand()`). The constructor makes some validations on the agents received as input. The implementation of this class lies in `amas.py`. 
### AMASIOiCGS
Represents an I/O iCGS induced on some AMAS. The constructor takes an AMAS and optionally a name for a `.trace` file where the steps of construction are recorded. The implementation of this class lies in `amas_IOiCGS.py`.
### AgentProjection
Represents the projection of an AMAS agent on an I/O iCGS. The constructor takes an AMAS, the number of the agent and optionally a an `AMASIOiCGS` and the name for a `.trace` file where the steps of construction are recorded. The implementation of this class lies in `amas_projection.py`.
### MKBSC_AMAS_Projection
Represents an AMAS's projection on an induced I/O iCGS, it is mainly described as a (ordered) list of `AgentProjection` objects. The implementation of this class lies in `amas_projection.py`. 
## References

[1]. Dilian Gurov, Filip Jamroga, Wojciech Jamroga, Mateusz Kaminski, Damian
Kurpiewski, Wojciech Penczek, and Teofil Sidoruk. “Asynchronous Agents
with Perfect Recall: Model Reductions, Knowledge-Based Construction,
and Model Checking for Coalitional Strategies”. In: CoRR abs/2412.06706
(2024). doi: 10 . 48550 / ARXIV . 2412 . 06706. arXiv: 2412 .
06706. url: https://doi.org/10.48550/arXiv.2412.
06706.
