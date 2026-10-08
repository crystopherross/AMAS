# AMAS
## Introduction
This repository contains an implementation of AMAS and its structures defined by Gurov et al. [1], relevant for our bachelor's thesis [2]. This README file will contain information about the usage of the tool.

## Usage
To use this tool import the contents of `amas.py`, `amas_IOiCGS.py`, `amas_projection.py`, `utils.py`, and optionally `read_input.py` in the source file. Construct an AMAS by using the constructors from `amas.py`, or using the function defined in `read_input.py` to construct an AMAS from a `.json` file in the `inputs` folder. The rest of the classes are used to construct I/O iCGSs and applying the MKBSC algorithm on the AMAS. The classes have methods to print the structures into files, some of the constructors have the choice to record a construction trace into a `.trace` file, these are saved in the `outputs` folder. 

## Input
The inputs of this tool are `.json` files located in the `./inputs/` directory. More information on the format of these `.json` files is found in the `README.md` file in the `./inputs/` directory. The file `read_input.py` contains the function that reads a `.json` file located in `./inputs/` and constructs an AMAS object with it. JSON files were chosen due to their standard use in structured data, it being enough to encode all that an AMAS requires for its construction, and to decouple the input from the program. Alternatively, the users can import the `AMAS` class in `amas.py` and call its constructor with correct arguments.

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
## Minimal example
In the `inputs` directory there are 2 examples in `.json` format, which were studied in the paper [2], these are read and used in `main.py`, showcasing the usage of the constructors and methods implemented.
## Extra files
The `utils.py` file contains utility functions, and more importantly, the `T` type, representing an AMAS's state, `read_input.py` contains the function that reads a `.json` file in the `inputs` folder and constructs an AMAS.
## References
[1]. Dilian Gurov, Filip Jamroga, Wojciech Jamroga, Mateusz Kaminski, Damian
Kurpiewski, Wojciech Penczek, and Teofil Sidoruk. “Asynchronous Agents
with Perfect Recall: Model Reductions, Knowledge-Based Construction,
and Model Checking for Coalitional Strategies”. In: CoRR abs/2412.06706
(2024). doi: 10 . 48550 / ARXIV . 2412 . 06706. arXiv: 2412 .
06706. url: https://doi.org/10.48550/arXiv.2412.
06706.

[2]. Crystopher W. Mariño Ross, Alexander Widén. “Modeling and Knowledge-based Strategy Synthesis for Asynchronous Multi-Agent Systems” (Dissertation). (2025). url: https://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-367566.
