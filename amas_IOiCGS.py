from __future__ import annotations
import amas
from utils import card_prod, T, for_all, T_str as Ts

class AMASIOiCGS:
    """
        A class to represent an AMAS I/O iCGS execution semantics.
        
        Attributes
        ----------
        St : set[tuple[T]]
            The set of global states for the induced CGS reachable from the initial state 'self.i' by 'self.T'.
        i : tuple[T]
            The initial global state, it always holds that 'self.i in self.St'
        Evt : set[str]
            The set of all events across agents, with the addition of the 'silent' event 'eps'. This
            silent event is such that 'Self.S.Agent('eps') == set()'.
        PV : set[str]
            The union of all sets of S's agents' propositions.
        V : dict[tuple[T], set[str]]
            The global valuation function. For a location 'g' it is defined as the union of the results of  the local 
            valuation functions for all agents of self.S on their corresponding component of 'g'.
        R : list[dict[T, set[frozenset[str]]]]
            The list of all repertoires of choices of all agents of self.S.
        T : set[tuple[tuple[T], tuple[frozenset[str]], str, tuple[T]]]
            Global transition relation. See the paper for more info on the conditions for an element to be in this set.  
        ind_rel : dict[int, set[tuple[tuple[T],tuple[T]]]] 
            List of all indistiguishability relations of all agents of self.S. The pair **(a,b)** of states in **St**
            lies in this relation for agent **i** iff **i**'s component in **a** is the same as in **b**.  

        Methods
        -------
        print: Prints this joint game to the console, displaying all of its components.
    """
    def __init__(self, S : amas.AMAS):
        """
        Construct an I/O iCGS for an input AMAS

        Attributes
        ----------
        name : S
            AMAS to extend. Beware that this AMAS should not have an event with name 'eps' as this name is reserved
            for the 'silent' event. Furthermore, its agents must be enumerated 0, 1, ..., in that order.
        
        """
        try:
            for agent in S.agents:
                assert 'eps' not in agent.Evt
        except AssertionError:
            print("InputError: The input AMAS has some agent (" + agent.name + ") with the event 'eps'. This event name is reserved for the construction of the CGS.")
            return

        # Initial global state
        temp_i: tuple["T"] = tuple()
        for agent in S.agents:
            temp_i += (agent.i,)
            print(temp_i)
        self.i = temp_i
        del temp_i

        # All propositions
        PV: set[str] = set()
        for agent in S.agents:
            PV.update(agent.PV)
        self.PV = PV
        del PV

        # Repertoires
        R: list[dict["T", set[frozenset[str]]]] = []
        for agent in S.agents:
            R.append(agent.R)
        self.R = R
        del R
        # Events
        Evt: set[str] = set()
        for agent in S.agents:
            Evt.update(agent.Evt)
        self.Evt = Evt
        self.Evt.add('eps')
        del Evt

        # Construct the set of global states and the transitions by
        # 'traversing' the graph from the initial state self.i and add the states and transitions
        # according to the definitions. This procedure assumes that the CGS is total (the resulting state graph
        # is connected).
        St: set[tuple["T"]] = set()
        T : set[tuple[tuple["T"], tuple[frozenset[str]], str, tuple["T"]]] = set()
        def g_i(g : tuple["T"], i : int) -> "T": return g[i]
        St_stack = [self.i]

        while St_stack:
            state = St_stack.pop()
            St.add(state)
            for out in self.Evt:
                # (*)
                if out != 'eps':
                    # Compute Agent(out), A\Agent(out)
                    A_out = S.Agent(out)
                    comp_A_out = set([i for i in range(len(S.agents))]).difference(A_out)
                    # Find valid choice lists for each agent from this global state with 'out'
                    R_list = [None for _ in range(len(S.agents))]

                    for i in range(len(S.agents)):
                        choices = S.agents[i].R[g_i(state, i)]
                        if i in A_out:
                            R_list[i] = set(map(frozenset, filter(lambda x: out in x, choices)))
                        else:
                            R_list[i] = set(map(frozenset,choices))
                    
                    # If any of the choices list in R_list is empty, continue to next out value
                    if not for_all(R_list, lambda x: x): continue

                    for prod in card_prod(R_list):
                        to = tuple()
                        for i in range(len(S.agents)):
                            if i in A_out: 
                               for t in S.agents[i].T:
                                   if t[0] == state[i] and t[1] == out:
                                       to += (t[2],)
                            else: to += (g_i(state,i),)
                        T.add((state, prod, out, to))
                        if to not in St:
                            # St.add(to)
                            St_stack.append(to)
                # (**)
                else:
                    non_silent_events = self.Evt.difference(set(['eps']))        
                    for prod in card_prod([set(map(frozenset,S.agents[i].R[g_i(state, i)])) for i in range(len(S.agents))]):
                        valid = True
                        for a in non_silent_events:
                            Ag = S.Agent(a)
                            if for_all([prod[i] for i in Ag], lambda x: a in x):
                                valid = False
                                break
                        if valid:
                            T.add((state, prod, 'eps' , state))
        self.St = St
        self.T = T
        del St 
        del T

        # {~}_{i in S.agents}
        ind_rel : dict[int, set[tuple[tuple["T"],tuple["T"]]]] = {} 
        for agent in S.agents:
            local_ind_rel = set()
            for g in self.St:
                for h in self.St:
                    if g_i(g, agent.number) == g_i(h, agent.number):
                        local_ind_rel.add((g, h))
            ind_rel[agent.number] = local_ind_rel
        self.ind_rel = ind_rel
        del ind_rel

        V : dict[tuple["T"], set[str]] = {}
        for g in self.St:
            union = set()
            for i in range(len(g)):
                union.update(S.agents[i].V[g[i]])
            V[g] = union
        self.V = V
        del V
    
    def __str__(self):
        ret = "Global states (St):\n"# + str(self.St) + "\n"
        for g in self.St:
            ret += "(" + ", ".join(map(Ts, g)) + "),\n"
        ret += "Initial state (i): (" + ", ".join(map(Ts, self.i)) + ")\n"
        ret += "Events (Evt): " + str(self.Evt) + "\n"
        ret += "Propositions (PV): " + str(self.PV) + "\n"
        ret += "Global valuation of propositions (V):\n"
        for k in self.V.keys():
            ret += "(" + ", ".join(map(Ts, k)) + ") -> " + str(self.V[k]) + "\n"
        ret += "Global Transitions (T):\n"
        for (g, g_in, g_out, gp) in self.T:
            ret += "(" + ", ".join(map(Ts, g)) + "), " + str(tuple(map(set,g_in))) + ", " + g_out + ", (" + ", ".join(map(Ts, gp)) + "),\n"
        ret += "Indistinguishability relations:\n"
        for a in self.ind_rel.keys():
            ret += "\t" + str(a) + ":\n"
            for (g, gp) in self.ind_rel[a]: ret += "(" + ", ".join(map(Ts, g)) + "), (" + ", ".join(map(Ts, gp)) + "),\n"
        return ret
    
    def print(self, write_to = '', mode = 'w'): 
        if write_to:
            with open("./outputs/" + write_to, mode) as handle:
                handle.write(self.__str__())
        else:
            print(self)


        