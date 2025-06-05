from __future__ import annotations
import amas_IOiCGS
import amas
from typing import Iterable
import logging
from utils import T, T_str as Ts, T_str_help as Tts

class AgentProjection:
    """
        A class to represent the projection of an AMAS agent on an I/O iCGS.
        
        Attributes
        ----------
        name : str
            The name of the agent this projection belongs to.
        number : int
            The number of the agent this projection belongs to.
        St : set[tuple[T]]
            The set of global states for the induced CGS reachable from its initial state by its transition relation.
        i : tuple[T]
            The initial global state of the CGS.
        Evt : set[str]
            The set of all events for the agent projected on.
        PV : set[str]
            The set of propositions for the projected agent.
        V : dict[tuple[T], set[str]]
            Projected global valuation function for the agent. For a location 'g' it is defined as the local 
            valuation functions for the projected agent.
        R : dict[T, set[frozenset[str]]]
            Repertoire of choices for this agent.
        T : set[tuple[tuple[T], frozenset[str], str, tuple[T]]]
            Projected global transition relation. See the paper for more info on the conditions for an element to be in this set.  
        iR : set[tuple[tuple[T],tuple[T]]]
            Indistiguishability relations of projected agents. The pair **(a,b)** of states in **St**
            lies in this relation for agent **i** iff **i**'s component in **a** is the same as in **b**.  
    """
    def __init__(self, S: amas.AMAS, i: int, M: amas_IOiCGS.AMASIOiCGS = None, trace_file = ''):
        """
        Parameters
        ----------
        S : amas.AMAS
            The AMAS where the agent **i** is
        i : int
            The enumeration of the agent to be projected on **M**.
        M : amas_IOiCGS.AMASIOiCGS
            Optional: The I/O iCGS to project on the agent given by **i**. By default the constructor will call
            S.joint_game(), creating M in the process, to avoid recomputing this CGS it is recommended to have a
            suitable value here
        """

        # Initialize Logging
        logger = logging.getLogger(f'proj_construct.{trace_file}')

        if trace_file and not logger.handlers:
            file_handler = logging.FileHandler('./outputs/' + trace_file, mode='w')
            formatter = logging.Formatter('%(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)
            logger.propagate = False
        def log(message): 
            """Log message only if the file name is valid (and thus the logger is initialized)."""
            if trace_file: logger.info(message)
            else: return

        if M == None:
            M = S.joint_game()
        # Inherited from M
        self.St = M.St
        self.i = M.i
        self.iR = M.ind_rel[i]
        # Inherited from S
        self.name = S.agents[i].name
        self.number = S.agents[i].number
        self.Evt = S.agents[i].Evt
        self.PV = S.agents[i].PV
        self.R = S.agents[i].R
        # Computed
        
        V : dict[tuple["T"], set[str]] = {}
        for g in self.St:
            V[g] = S.agents[i].V[g[i]]
        self.V = V
        del V

        # Go through all transitions in M, if out in the choices made by the agent, add
        # proper transition, else add epsilon-transition.
        log("Constructing transitions.\n")
        T: set[tuple[tuple["T"], frozenset[str], str, tuple["T"]]] = set()
        for (g, g_in, g_out, gp) in M.T:
            log(f"Transition: ({Tts(g)}, {{{", ".join(map(str,map(set, g_in)))}}}, {g_out}, {Tts(gp)})")
            log(f"Agent's (number {self.number+1}, index {self.number}) choice: {set(g_in[self.number])}")
            if g_out in g_in[i]:
                log(f"{g_out} in {set(g_in[self.number])}, add proper transition ({Tts(g)}, {set(g_in[self.number])}, {g_out}, {Tts(gp)}) to the projection's transition set.\n")
                T.add((g,g_in[i],g_out,gp))
            if g_out not in g_in[i]:
                log(f"{g_out} not in {set(g_in[self.number])}, add epsilon-transition ({Tts(g)}, {set(g_in[self.number])}, eps, {Tts(gp)}) to the projection's transitions.\n")
                T.add((g,g_in[i],'eps',gp))
        self.T = T
        del T

        # Shut down logger
        if trace_file:
            for handler in logger.handlers:
                handler.close()
                logger.removeHandler(handler)
    
    def __str__(self):
        ret = ""
        # ret = "Agents: " + " ".join([a.name for a in self.S.agents]) + "\n"
        ret += f"Agent: {self.name} | Number: {self.number}\n"
        ret += "Global states (St):\n" + ",\n".join(map(Tts, self.St)) + "\n"
        ret += "Initial state (i): " + Tts(self.i) + "\n"
        ret += "Events (Evt): " + str(self.Evt) + "\n"
        ret += "Propositions (PV): " + str(self.PV) + "\n"
        ret += "Global valuation of propositions (V):\n"
        for k in self.V.keys():
            ret += Tts(k) + " -> " + str(self.V[k]) + "\n"
        ret += "Global Transitions (T):\n"
        for (g, g_in, g_out, gp) in self.T:
            ret += Tts(g) + ", " + str(set(g_in)) + ", " + g_out + ", " + Tts(gp) + "\n"
        ret += "Indistinguishability relation:\n"
        for (g, gp) in self.iR:
            ret += Tts(g) + ", " + Tts(gp) + ",\n"
        return ret
    
    def print(self): print(self)
    def print(self, write_to = '', mode = 'w'): 
        if write_to:
            with open("./outputs/" + write_to, mode) as handle:
                handle.write(self.__str__())
        else:
            print(self)

    def eps_closure(self, G: Iterable[tuple[T]]) -> frozenset[tuple[T]]:
        """Given a collection of global states **G**, find the epsilon-closure of G in this projection."""
        closure = set()
        stack = list(G)
        while stack:
            curr = stack.pop()
            closure.add(curr)
            for (g, _, g_out, gp) in self.T:
                if g == curr and g_out == 'eps' and gp not in closure: 
                    stack.append(gp)
        return frozenset(closure)
        
class MKBSC_AMAS_Projection:
    def __init__(self, projections: list[AgentProjection]):
        self.projections = projections
    
    def print(self, write_to='', mode = 'a'):
        if write_to:
                # Clear the file
                with open("./outputs/" + write_to, 'w'):
                    pass
                # Write to the file
                for p in self.projections:
                    p.print(write_to, mode)
        else:
            for p in self.projections:
                p.print()

    
    