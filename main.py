import old.amas_agent as amas_agent
import amas
import amas_IOiCGS
import amas_projection
import old.amas_mkbsc_expansion as amas_mkbsc_expansion

# Sender
sender = amas_agent.AMASAgent(
    'Sender', 
    0, 
    ['s0','s1'],
    's0',
    ['send0','send1','next'],
    {'s0': [['next'],['send0']], 's1': [['next'],['send1']]},
    [('s0', 'send0', 's0'), ('s0', 'next', 's1'), ('s1', 'next', 's0'), ('s1', 'send1', 's1')],
    [],
    {'s0': set(), 's1': set()}
    )

# Receiver
receiver = amas_agent.AMASAgent(
    'Receiver', 
    1, 
    ['rb','r0','r1'],
    'rb',
    ['send0','send1','lost','dup'],
    {'rb': [['lost','send0','send1']], 'r0': [['lost','dup','send1']], 'r1': [['lost','dup','send0']]},
    [('rb', 'lost', 'rb'), ('rb', 'send0', 'r0'), ('rb', 'send1', 'r1'), 
     ('r1', 'dup', 'r1'), ('r1', 'lost', 'rb'), ('r1', 'send0', 'r0'), 
     ('r0', 'dup', 'r0'), ('r0', 'lost', 'rb'), ('r0', 'send1', 'r1'),],
    [],
    {'rb': set(), 'r0': set(), 'r1': set()}
    )

S = amas.AMAS([sender, receiver])

M = amas_IOiCGS.AMASIOiCGS(S)

P = amas_projection.MKBSC_AMAS_Projection(M)

# for proj in P.projections:
#     print(proj)

E = amas_mkbsc_expansion.MKBSC_AMAS_Expansion(M, P)

for exp in E.expansions:
    print(exp)