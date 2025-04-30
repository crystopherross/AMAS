from typing import Callable, Iterable, Union, Tuple, FrozenSet


T = Union[str, FrozenSet[Tuple["T", ...]]]
"""The type of an AMAS agent's locations. It is recursive, either a string, or a frozenset of tuples of this type.
This recursion comes from the fact that the AMAS can be expanded arbitrarily many times, each time a type wrapping
frozenset(tuple()) occurs by the nature of the projection and expansion procedures."""

def card_prod(sets : list[set]) -> set[tuple]:
    """Given a list of sets, return the cardinal product of the sets in the same order as they appear in the input list."""
    if not sets: return set()
    cp: set[tuple] = set(map(lambda x: (x,), sets[0]))
    for s in sets[1:]:
        cp_new = set()
        for e in s:
            for p in cp:
                cp_new.add(p + (e,))
        cp = cp_new
    return cp

def power_set(s : set) -> set[frozenset]:
    """Given a set **s** return its power set"""
    P = set()
    ls = len(s)
    s = list(s)
    for i in range(2**(ls)):
        bin_str = bin(i)[2:]
        bin_str = ('0' * (ls - len(bin_str))) + bin_str
        subset = set()
        for i in range(len(s)):
            if bin_str[i] == '1': subset.add(s[i])
        P.add(frozenset(subset))
    return P


def for_all(coll: Iterable[object], b_lambda : Callable[[object], bool]) -> bool:
    """Given a collection (iterable) and a function that returns a boolean, determine whether all
    elements in **coll** give True when passed to **b_lambda**."""
    for e in coll:
        if not b_lambda(e): return False
    return True

def exists(coll: Iterable[object], b_lambda : Callable[[object], bool]) -> bool:
    """Given a collection (iterable) and a function that returns a boolean, determine whether there is some
    element in **coll** that evaluate to True when passed to **b_lambda**."""
    for e in coll:
        if b_lambda(e): return True
    return False

def union_all(iterables: list[Iterable]) -> set[frozenset]:
    """Given a list of iterables return their set union."""
    union = set()
    for it in iterables:
        union.update(frozenset(it))
    return union

def T_str(t: T):
    if isinstance(t, str):
        return t
    else: 
        return "{" + ", ".join(map(T_str_help, t)) + "}"

def T_str_help(t: tuple[T]):
    return "(" + ", ".join(map(T_str, t)) + ")"    


def frozenset_str(frset: frozenset):
    def frozenset_str_rec(item):
        if isinstance(item, frozenset):
            return f"{{{', '.join(map(str, item))}}}"
        return str(item)
    return f"{{{', '.join(frozenset_str_rec(item) for item in frset)}}}"


def write_tikz_picture(tikz_pict: tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]], file_name: str = "tikz.txt", fig_caption: str = "caption", fig_label: str = "label"):
    """Take a list of nodes and a list of edges to write a tikz picture to a file, sparing most effort in writting it down in LaTeX.
    Still, the placement and customization is to be made manually.
    
    TODO: Use NetworkX library or similar to find a good layout for the graph.
    """
    with open(file_name, 'w') as handle:
        (nodes, edges) = tikz_pict
        handle.write("\\begin{ figure }[H]\n\t\\centering\n\t\\begin{ tikzpicture } [->, >=stealth, shorten >=1pt, auto, node distance=4cm, semithick]\n")
        handle.write("\t\t% States\n")
        for (node_type, node_name, label) in nodes:
            handle.write("\t\t\\node[" + ", ".join(node_type) + "] (" + node_name + ") {" + label + "};\n")
        handle.write("\n\t\t% Edges\n\t\t\\path")
        for (t_from, t_label, t_to) in edges:
            handle.write("\n\t\t(" + t_from + ") edge node {" + t_label + "} (" + t_to + ")")
        handle.write(";\n\t\\end{ tikzpicture }\n\t\\caption{" + fig_caption + "}\n\t\\label{" + fig_label + "}\n\\end{ figure }")

