from __future__ import annotations
from typing import Iterable
import amas_IOiCGS
import amas_projection
import transducer
from utils import T, T_str as Ts, T_str_help as Tts


class AMASagent:
    """
    A class to represent an AMAS agent.

    Attributes
    ----------
    name : str
        Name of the agent.
    number : int
        Enumeration of agent.
    L : set[T]
        Set of local states for the agent.
    i : T
        Starting location of agent (among its local states). It always holds that 'self.i in self.L'.
    Evt : set[str]
        Non-empty set of events (transition labels) for agent.
    R : dict[T, set[frozenset[str]]]
        The repertoire of choices for the agent. It is a function from the local states (L) to a list of subsets
        of Evt (choices). That is, all elements e inside the innermost structure must fulfill 'e in Evt'. Said
        choices are non-empty, as is R[l] for all l in L. 
    T : set[tuple[T, str, T]]
        Local transition relation. The tuple (l,e,l'), with 'l,l' in L' and 'e in U R(l)' represents that the local
        state changes from l to l' by event e.
    PV : set[str]
        List of local propositional variables (boolean flags), it contains the names of said propositional variables
    V : dict[T, set[str]]
        Evaluation function of the agent. It maps local agent states to a mapping of labels of propositional variables 
        (elements of PV). A proposition p appears in a value associated with l iff p is true in l.
    
    Methods
    -------
    print:
        Prints this agent to the console by default, displaying all of its components. It is possible to make
        this method to instead write this to a file.
    to_tikz_picture:
        Returns a graph representation of this agent meant for creating a tikz picture in LaTeX.
    
    
    """
    def __init__(
        self, 
        name: str, 
        number: int, 
        L: Iterable[T], 
        i: T, 
        Evt: Iterable[str], 
        R: dict[T, Iterable[Iterable[str]]], 
        T: Iterable[tuple[T, str, T]], 
        PV: Iterable[str], 
        V: dict[T, Iterable[str]]
    ):
        """Constructs an AMAS agent and makes checks to ensure that the constructed AMAS agent is valid."""
        # Descriptive info
        self.name = name
        self.number = number
        # Locations
        i: "T" = i
        L: set["T"] = set(L)
        try:
            assert L
        except AssertionError:
            print("InputError: Problem defining L, the input location list is empty.")
            return
        try:
            assert i in L
        except AssertionError:
            print("InputError: Problem defining i, initial state is not inside the given list of the agent's local states L.")
            return
        self.i = i
        self.L = L
        # Events
        Evt: set[str] = set(Evt)
        try: 
            assert Evt
        except AssertionError:
            print("InputError: Problem defining Evt, input event list is empty.")
            return
        self.Evt = Evt
        # Repertoire
        R: dict["T", set[frozenset[str]]] = R
        for l in R.keys():
            try:
                assert R[l]
            except AssertionError:
                print("InputError: Problem defining R, the list of choices at state", Ts(l), "is empty.")
                return
            for choices in R[l]:
                try:
                    assert choices
                except AssertionError:
                    print("InputError: Error defining R, a choice for the repetorire at", Ts(l) , "is empty.")
                for event in choices:
                    try:
                        assert event in Evt
                    except AssertionError:
                        print("InputError: Option", event, "for this agent at a choice in local state", Ts(l), "is not in the list of events for the agent")
                        return
            R[l] = set(map(frozenset, R[l]))
        self.R = R
        # Transition relation
        T: set[tuple["T",str,"T"]] = set(T)
        for (l, a, r) in T:
            R_l = self.R[l]
            R_union = set()
            for choices in R_l: R_union = R_union.union(choices)
            try:
                assert l in L
            except:
                print("InputError: Problem defining T,", Ts(l), "in", Tts((l,a,r)), "is not a local state.")
                return
            try:
                assert r in L
            except:
                print("InputError: Problem defining T,", Ts(r), "in", Tts((l,a,r)), "is not a local state.")
                return
            try:
                assert a in R_union
            except:
                print("InputError: Problem defining T,", a, "in", Tts((l,a,r)), "is not among the repetoire of choices of the agent at local state", str(l), ".")
                return
        self.T = T
        # Evaluation, Local propositions
        V: dict["T", set[str]] = V
        for l in V.keys():
            try:
                assert l in L
            except AssertionError:
                print("InputError: Problem defining V,", Ts(l), "is not a local state.")
            for val in V[l]:
                try: 
                    assert val in PV
                except AssertionError:
                    print("InputError: Problem defining V,", val, "is not a local proposition of the agent.")
                    return
        self.PV = set(PV)
        self.V = V

    def expand(self, M: amas_IOiCGS.AMASIOiCGS, P: amas_projection.AgentProjection, name: str = None) -> "AMASagent":
        """Construct the MKBSC expansion for this AMAS agent whose projection on I/O iCGS **M** is **P**.

        Attributes
        ----------
        M : amas_IOiCGS.AMASIOiCGS
            The I/O iCGS that was induced on the AMAS this agent is part of.
        P : amas_projection.AgentProjection
            The projection of this agent on **M**.
            
        """
        if name == None: name = self.name
        # Inherited from P
        Evt: set[str] = P.Evt
        PV: set[str] = P.PV
        # Initialize R_i^K, V_i^K 
        R: dict[frozenset[tuple["T"]], set[frozenset[str]]] = {}
        V: dict[frozenset[tuple["T"]], set[str]]= {}
        # Compute St_i^K, i_i^K, T_i^K
        # Step 1
        i: frozenset[tuple["T"]] = P.eps_closure({P.i})
        St: set[frozenset[tuple["T"]]] = set()
        T: set[tuple[frozenset[tuple["T"]], str, frozenset[tuple["T"]]]] = set()
        # Steps 2, 3
        stack: list[frozenset[tuple["T"]]] = [i]
        while stack:
            sk: frozenset[tuple["T"]] = stack.pop()
            St.add(sk)
            R[sk] = self.R[list(sk)[0][self.number]]
            V[sk] = self.V[list(sk)[0][self.number]]
            for E in R[sk]:
                Succ: set[frozenset[tuple["T"]]] = set()
                for q in sk:
                    for (g, g_in, _, gp) in P.T:
                        if g == q and g_in == E:
                            Succ.add(gp)
                Succp = P.eps_closure(Succ)
                SuccK: set[frozenset[tuple["T"]]] = set()
                equiv_part: dict["T", list[tuple["T"]]] = {}
                for q in Succp:
                    if q[self.number] not in equiv_part.keys(): equiv_part[q[self.number]] = [q]
                    else: equiv_part[q[self.number]].append(q)
                for v in equiv_part.values(): SuccK.add(frozenset(v))
                for q in SuccK:
                    if q not in St: stack.append(q)
                St.update(SuccK)
                for sk_succ in SuccK:
                    for q in sk:
                        for qp in sk_succ:
                            for a in Evt:
                                if (q, E, a, qp) in P.T:
                                    T.add((sk, a, sk_succ))
        return AMASagent(
            self.name,
            self.number,
            St,
            i,
            Evt,
            R,
            T,
            PV,
            V
        )

    def create_iF_strategy_transducer(self, ir_strategy: dict[frozenset[tuple["T"]], set[str]], SK: amas_IOiCGS.AMASIOiCGS):
        """Construct an iF-strategy transducer for this agents out of a local ir-strategy and a expanded game for this
        agent."""
        # Ensure that this Agent is one from an expanded game.
        if type(self.i) == 'str':
            print("InputError: Cannot create iF-strategy transducer from a non-expanded agent (the current type of this agent's states is 'str').")
            return
        # TODO??: Ensure that SK is a valid I/O iCGS in this context (it is a expanded game, not a 'regular' game).

        memory_update_function: dict[tuple[tuple[frozenset[tuple[T]]]], frozenset[tuple[T]]] = {}
        # TODO: Construct the memory update function
        return transducer.Transducer(SK.St, SK.i, self.L, self.Evt, memory_update_function, ir_strategy)

    def to_tikz_picture(self) -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
        """Return a representation of a LaTeX tikz picture for the agent in the form of nodes and edges."""
        nodes = []
        edges = []
        for l in self.L:
            node_type = ["state"]
            if l == self.i: node_type.append("initial")
            node_name = self.name.replace(" ", "") + "\\_" + l
            label = "$" + l + "$"
            nodes.append((node_type, node_name, label))
        for (t_from, t_label, t_to) in self.T:
            edges.append((self.name.replace(" ", "") + "\\_" + t_from, t_label, self.name.replace(" ", "") + "\\_" + t_to))
        return (nodes, edges)
    
    def __str__(self):
        s = "Agent: " + self.name + " | Enumeration: " + str(self.number) + "\n"
        s += "Locations: " + ",\n".join(map(Ts, self.L)) + "\nInitial location: " + Ts(self.i) + "\n"
        s += "Events: " + str(self.Evt) + "\nRepertoire of Choices:\n"
        for k in self.R.keys():
            s += Ts(k) + " -> " + "{" + ", ".join(map(lambda x: str(set(x)), self.R[k])) + "}\n"
        s += "Transitions:\n" 
        for (fr, a, to) in self.T:
            s += "("+ Ts(fr) + ", " + a + ", " + Ts(to) + "),\n"
        s += "Local Propositions: " + str(self.PV) + "\nProposition Evaluations:\n"
        for k in self.V.keys():
            s += Ts(k) + " -> " + str(self.V[k]) + "\n"
        return s
    
    def print(self, write_to = '', mode = 'w'): 
        if write_to:
            with open("./outputs/" + write_to, mode) as handle:
                handle.write(self.__str__())
        else:
            print(self)

class AMAS:
    """
    A class representing an AMAS

    Attributes
    ----------
    agents: list[AMASagent]
        The list of all agents in this AMAS, they are (should be) ordered by their agent number, starting from 0
        and without skipping integers.

    Methods
    -------
    print: 
        Print each agent of this AMAS to the console, displaying their components.
    Agent: 
        Given a event **a**, return the set of numbers of the agents in this AMAS that have said event locally.
    joint_game:
        Induce an I/O iCGS on this AMAS and return it.
    project:
        Project this AMAS on its induced I/O iCGS.
    expand:
        Expand this AMAS using MKBSC, yielding a new AMAS.

    """
    def __init__(self, agents: list[AMASagent]):
        self.agents = agents
        for i in range(len(agents)):
            # Ensure that the agents are ordered by index 0,1,2,...,n-1
            try:
                assert agents[i].number == i
            except AssertionError:
                print("InputError: Agent enumeration is wrong, agent " + agents[i].name + " has enumeration " + str(agents[i].number) + ", it should have enumeration " + str(i))
                return
        # Ensure that no two agents share any propositional variables. 
        # We do this by having a list and set union representation at once. At the end, the condition
        # is fulfilled iff both the list and the union have the same amount of elements.
        union = set()
        prop_list = []
        for i in range(len(agents)):
            union.update(agents[i].PV)
            prop_list.extend(list(agents[i].PV))
        try: 
            assert len(union) == len(prop_list)
        except AssertionError:
            print("InputError: A pair of agents in the input list share some propositional variable.")
            return 
    
    def Agent(self, a : str) -> set[int]:
        """Return the set of enumerations of agents of this AMAS that have the event 'a'."""
        ret = set()
        for agent in self.agents:
            if a in agent.Evt:
                ret.add(agent.number)
        return ret
    
    def joint_game(self) -> amas_IOiCGS.AMASIOiCGS:
        """Induces an I/O iCGS on this AMAS, returns said CGS."""
        return amas_IOiCGS.AMASIOiCGS(self)
    
    def project(self, M: amas_IOiCGS.AMASIOiCGS = None) -> amas_projection.MKBSC_AMAS_Projection:
        """Projects this AMAS's agents on an induced I/O iCGS. By default this method induces an I/O iCGS during
        execution, to avoid this we can provide a ready-made I/O iCGS, although there is the need of guaranteing
        that said input CGS actually extends this AMAS properly."""
        
        # Induce a CGS if none is provided
        if M == None:
            M = self.joint_game()

        projections: list[amas_projection.AgentProjection] = []
        for i in range(len(self.agents)):
            projections.append(amas_projection.AgentProjection(self, i, M))

        return amas_projection.MKBSC_AMAS_Projection(projections)

    def expand(self, M:amas_IOiCGS.AMASIOiCGS = None, P:amas_projection.MKBSC_AMAS_Projection = None) -> "AMAS":
        """Expands this AMAS using MKBSC, returning a new AMAS. By default this method induces an I/O iCGS and
        projection on it during execution, to avoid this we can provide a ready-made I/O iCGS and projection, 
        although there is the need of guaranteing that said input CGS and projection actually extends this AMAS 
        properly."""
        if M == None:
            M = self.joint_game()
        if P == None:
            P = self.project(M)
        expanded_agents: list[AMASagent] = []
        for agent in self.agents:
            expanded_agents.append(agent.expand(M, P.projections[agent.number]))
        return AMAS(expanded_agents)
        

    def print(self, write_to = '', mode = 'a'): 
        if write_to:
            # Clear the file
            with open("./outputs/" + write_to, 'w'):
                pass
            # Write to the file
            for a in self.agents:
                a.print(write_to, mode)

        else:
            for a in self.agents:
                a.print()