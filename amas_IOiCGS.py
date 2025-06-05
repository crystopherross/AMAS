from __future__ import annotations
import logging
import amas
from utils import card_prod, T, for_all, T_str as Ts, T_str_help as Tts

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
    def __init__(self, S : amas.AMAS, trace_file = ''):
        """
        Construct an I/O iCGS for an input AMAS

        Attributes
        ----------
        name : S
            AMAS to extend. Beware that this AMAS should not have an event with name 'eps' as this name is reserved
            for the 'silent' event. Furthermore, its agents must be enumerated 0, 1, ..., in that order.
        trace_file : str
            The name of the file where the trace of the algorithm (construction of states and transitions) is recorded.
            By default no trace file is created.
        
        """
        try:
            for agent in S.agents:
                assert 'eps' not in agent.Evt
        except AssertionError:
            print("InputError: The input AMAS has some agent (" + agent.name + ") with the event 'eps'. This event name is reserved for the construction of the CGS.")
            return
        
        # Initialize Logging
        logger = logging.getLogger(f'cgs_construct.{trace_file}')

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
        
        # Inherited from the AMAS.
        temp_i: tuple["T"] = tuple() # Initial global state
        PV: set[str] = set() # All propositions
        R: list[dict["T", set[frozenset[str]]]] = [] # Repertoires
        Evt: set[str] = set() # All events
        for agent in S.agents:
            temp_i += (agent.i,)
            PV.update(agent.PV)
            R.append(agent.R)
            Evt.update(agent.Evt)
        self.i, self.PV, self.R, self.Evt = temp_i, PV, R, Evt
        self.Evt.add('eps')
        del temp_i
        del PV
        del R
        del Evt

        # Construct the set of global states and the transitions by
        # 'traversing' the graph from the initial state self.i and add the states and transitions
        # according to the definitions. This procedure assumes that the CGS is total (the resulting state graph
        # is connected).
        St: set[tuple["T"]] = set()
        T : set[tuple[tuple["T"], tuple[frozenset[str]], str, tuple["T"]]] = set()
        def g_i(g : tuple["T"], i : int) -> "T": return g[i]

        log("Starting construction of states and transitions.\n")

        St_stack = [self.i]
        while St_stack:
            log("St = " + str(list(map(Tts, St))) + ", T = " + str(set(map(lambda x: (Tts(x[0]), str(tuple(map(set, list(x[1])))), x[2], Tts(x[3])), T))) + ", stack = " + str(list(map(Tts,St_stack))))
            state = St_stack.pop()
            log("g = " + Tts(state))
            St.add(state)
            log("St = " + str(set(map(Tts, St))) + ", stack = " + str(list(map(Tts,St_stack))))
            for out in self.Evt:
                # (*)
                log("Checking out = " + str(out))
                if out != 'eps':
                    log("Adding 'proper' transitions.")
                    # Compute Agent(out), A\Agent(out)
                    A_out = S.Agent(out)
                    log(f"Agent({out}) = " + str(set(map(lambda x: x+1,A_out))))
                    # Find valid choice lists for each agent from this global state with 'out'
                    R_list = [None for _ in range(len(S.agents))]

                    for i in range(len(S.agents)):
                        choices = S.agents[i].R[g_i(state, i)]
                        if i in A_out:
                            R_list[i] = set(map(frozenset, filter(lambda x: out in x, choices)))
                        else:
                            R_list[i] = set(map(frozenset,choices))
                        log("C" + str(i+1) + " = " + str(list(map(set, list(R_list[i])))) + ",")
                    
                    # If any of the choices list in R_list is empty, continue to next out value
                    if not for_all(R_list, lambda x: x): 
                        log("Skipping this value of out, some set C is empty.")
                        continue

                    for prod in card_prod(R_list):
                        log("in = " + str(list(map(set, list(prod)))))
                        to = tuple()
                        for i in range(len(S.agents)):
                            log("Transitions in T" + str(i+1) + " with l = " + Ts(g_i(state,i)) + ", alpha = " + out + ":")
                            if i in A_out: 
                                for t in S.agents[i].T:
                                    if t[0] == state[i] and t[1] == out:
                                        to += (t[2],)
                                        log("(" + Ts(g_i(state,i)) + ", " + out + ", " + Ts(t[2]) + "), ")
                            else: 
                                to += (g_i(state,i),)
                                log("Agent " + str(i+1) + " remains unchanged.")
                        log("g' = " + Tts(to))
                        log("g' not in St; add g' to St and stack." if to not in St else "g' already in St. St and stack remain unchanged.")
                        log("Add (" + Tts(state) + ", " + str(list(map(set, list(prod)))) + ", " + out + ", " + Tts(to) + ") to T.")
                        T.add((state, prod, out, to))
                        if to not in St:
                            St_stack.append(to)
                # (**)
                else:
                    log("Adding epsilon-transitions for this state.")
                    non_silent_events = self.Evt.difference({'eps'})        
                    for prod in card_prod([set(map(frozenset,S.agents[i].R[g_i(state, i)])) for i in range(len(S.agents))]):
                        log("in = " + str(list(map(set, list(prod)))))
                        valid = True
                        for a in non_silent_events:
                            Ag = S.Agent(a)
                            if for_all([prod[i] for i in Ag], lambda x: a in x):
                                valid = False
                                log("All agents having " + a + " (agents " + ", ".join(list(map(str, map(lambda x: x+1, Ag)))) + "), made a choice containing the event, no epsilon-transition added with in.")
                                break
                        if valid:
                            log("Add (" + Tts(state) + ", " + str(list(map(set, list(prod)))) + ", epsilon, " + Tts(state) + ") to T.")
                            T.add((state, prod, 'eps' , state))
                log("")
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

        # Shut down logger
        if trace_file:
            for handler in logger.handlers:
                handler.close()
                logger.removeHandler(handler)
        
    
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


        