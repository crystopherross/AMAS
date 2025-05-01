class Transducer:
    """Representation of a transducer for a local iF strategy for an AMAS agent"""
    def __init__(self, memory_states, init_memory_state, input_alphabet, output_alphabet, mem_upd, output):
        """Create a transducer from the inputs. 
        TODO: Make checks to ensure that the transducer is valid."""
        self.memory_states = memory_states
        self.init_memory_state = init_memory_state
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.mem_upd = mem_upd
        self.output = output

