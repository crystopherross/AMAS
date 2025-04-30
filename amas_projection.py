from __future__ import annotations
import amas_IOiCGS
import amas
from typing import Iterable
from utils import T

class AgentProjection:
    """
        A class to represent the projection of an AMAS agent on an I/O iCGS.
        
        Attributes
        ----------
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
    def __init__(self, S: amas.AMAS, i: int, M: amas_IOiCGS.AMASIOiCGS = None):
        """
        Attributes
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
        if M == None:
            M = S.joint_game()
        # Inherited from M
        self.St = M.St
        self.i = M.i
        self.iR = M.ind_rel[i]
        # Inherited from S
        self.Evt = S.agents[i].Evt
        self.PV = S.agents[i].PV
        self.R = S.agents[i].R
        # Computed
        
        V : dict[tuple["T"], set[str]] = {}
        for g in self.St:
            V[g] = S.agents[i].V[g[i]]
        self.V = V
        del V

        T: set[tuple[tuple["T"], frozenset[str], str, tuple["T"]]] = set()
        for (g, g_in, g_out, gp) in M.T:
            if g_out in g_in[i]:
                T.add((g,g_in[i],g_out,gp))
            if g_out not in g_in[i]:
                T.add((g,g_in[i],'eps',gp))
        self.T = T
        del T
    
    def __str__(self):
        ret = ""
        # ret = "Agents: " + " ".join([a.name for a in self.S.agents]) + "\n"
        ret += "Global states (St): " + str(self.St) + "\n"
        ret += "Initial state (i): " + str(self.i) + "\n"
        ret += "Events (Evt): " + str(self.Evt) + "\n"
        ret += "Propositions (PV): " + str(self.PV) + "\n"
        ret += "Global valuation of propositions (V):\n"
        for k in self.V.keys():
            ret += str(k) + " -> " + str(self.V[k]) + "\n"
        ret += "Global Transitions (T):\n"
        for (g, g_in, g_out, gp) in self.T:
            ret += str(g) + ", " + str(g_in) + ", " + g_out + ", " + str(gp) + "\n"
        ret += "Indistinguishability relation:\n"
        ret += str(self.iR) + "\n"
        return ret
    
    def print(self): print(self)

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
    
    def print(self):
        for proj in self.projections:
            proj.print()
    

    
    