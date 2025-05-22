import amas

# # First version
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s0','s1'],
#     's0',
#     ['send0','send1','next'],
#     {'s0': [['next'],['send0']], 's1': [['next'],['send1']]},
#     [('s0', 'send0', 's0'), ('s0', 'next', 's1'), ('s1', 'next', 's0'), ('s1', 'send1', 's1')],
#     [],
#     {'s0': set(), 's1': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rb','r0','r1'],
#     'rb',
#     ['send0','send1','lost','dup'],
#     {'rb': [['lost','send0','send1']], 'r0': [['lost','dup','send1']], 'r1': [['lost','dup','send0']]},
#     [('rb', 'lost', 'rb'), ('rb', 'send0', 'r0'), ('rb', 'send1', 'r1'), 
#      ('r1', 'dup', 'r1'), ('r1', 'lost', 'rb'), ('r1', 'send0', 'r0'), 
#      ('r0', 'dup', 'r0'), ('r0', 'lost', 'rb'), ('r0', 'send1', 'r1'),],
#     [],
#     {'rb': set(), 'r0': set(), 'r1': set()}
#     )

# # Second Version
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s0b','s00', 's01', 's1b', 's10', 's11'],
#     's0b',
#     ['send0','send1','next','lostr','ack0','ack1','dupr'],
#     {'s0b': [['next'],['send0'],['lostr','ack0','ack1']], 's00': [['next'],['send0'],['lostr','dupr','ack1']],'s01': [['next'],['send0'],['lostr','ack0','dupr']],
#      's1b': [['next'],['send1'],['lostr','ack0','ack1']], 's10': [['next'],['send1'],['lostr','dupr','ack1']],'s11': [['next'],['send1'],['lostr','ack0','dupr']]},
#     [('s0b', 'send0', 's0b'), ('s0b', 'lostr', 's0b'), ('s0b', 'ack0', 's00'), ('s0b', 'ack1', 's01'), ('s0b', 'next', 's1b'),
#      ('s00', 'send0', 's00'), ('s00', 'dupr', 's00'), ('s00', 'lostr', 's0b'), ('s00', 'ack1', 's01'), ('s00', 'next', 's10'),
#      ('s01', 'send0', 's01'), ('s01', 'dupr', 's01'), ('s01', 'lostr', 's0b'), ('s01', 'ack0', 's00'), ('s01', 'next', 's11'),
#      ('s1b', 'send1', 's1b'), ('s1b', 'lostr', 's1b'), ('s1b', 'ack0', 's10'), ('s1b', 'ack1', 's11'), ('s1b', 'next', 's0b'),
#      ('s10', 'send1', 's10'), ('s10', 'dupr', 's10'), ('s10', 'lostr', 's1b'), ('s10', 'ack1', 's11'), ('s10', 'next', 's00'),
#      ('s11', 'send1', 's11'), ('s11', 'dupr', 's11'), ('s11', 'lostr', 's1b'), ('s11', 'ack0', 's10'), ('s11', 'next', 's01')],
#     [],
#     {'s0b': set(),'s00': set(),'s01': set(), 's1b': set(),'s10': set(),'s11': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rb','r0','r1'],
#     'rb',
#     ['send0','send1','losts','dups','ack0','ack1'],
#     {'rb': [['losts','send0','send1']], 'r0': [['losts','dups','send1'],['ack0']], 'r1': [['losts','dups','send0'],['ack1']]},
#     [('rb', 'losts', 'rb'), ('rb', 'send0', 'r0'), ('rb', 'send1', 'r1'), 
#      ('r1', 'dups', 'r1'), ('r1', 'losts', 'rb'), ('r1', 'send0', 'r0'), 
#      ('r0', 'dups', 'r0'), ('r0', 'losts', 'rb'), ('r0', 'send1', 'r1'),
#      ('r0', 'ack0', 'r0'), ('r1', 'ack1', 'r1')],
#     [],
#     {'rb': set(), 'r0': set(), 'r1': set()}
#     )

# # Third Version
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s0','s1'],
#     's1',
#     ['send0','send1','next','ack1','ack0'],
#     {'s0': [['next'],['send0'],['ack1','ack0']], 's1': [['next'],['send1'],['ack1','ack0']]},
#     [('s0', 'send0', 's0'), ('s0', 'next', 's1'), ('s1', 'next', 's0'), ('s1', 'send1', 's1'),
#      ('s0', 'ack0', 's0'), ('s0', 'ack1', 's0'),
#      ('s1', 'ack0', 's1'), ('s1', 'ack1', 's1')],
#     [],
#     {'s0': set(), 's1': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rb','r0','r1'],
#     'rb',
#     ['send0','send1','lost','dup','ack0','ack1'],
#     {'rb': [['lost','send0','send1']], 'r0': [['lost','dup','send1'],['ack0']], 'r1': [['lost','dup','send0'],['ack1']]},
#     [('rb', 'lost', 'rb'), ('rb', 'send0', 'r0'), ('rb', 'send1', 'r1'), 
#      ('r1', 'dup', 'r1'), ('r1', 'lost', 'rb'), ('r1', 'send0', 'r0'), 
#      ('r0', 'dup', 'r0'), ('r0', 'lost', 'rb'), ('r0', 'send1', 'r1'), ('r0', 'ack0', 'r0'), ('r1', 'ack1', 'r1')],
#     [],
#     {'rb': set(), 'r0': set(), 'r1': set()}
#     )

# # Fourth Version
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['ss', 's0','s1'],
#     'ss',
#     ['send0','send1','next','ack1','ack0','ldr'],
#     {'s0': [['next'],['send0'],['ack0','ack1','ldr']], 's1': [['next'],['send1'],['ack1','ack0','ldr']], 'ss': [['send1']]},
#     [('s0', 'send0', 's0'), ('s0', 'next', 's1'), ('s1', 'next', 's0'), ('s1', 'send1', 's1'),
#      ('s0', 'ack0', 's0'), ('s0', 'ldr', 's0'), ('s0', 'ack1', 's0'), ('s1', 'ack0', 's1'),
#     ('s1', 'ack1', 's1'), ('s1', 'ldr', 's1'), ('ss', 'send1', 's1')],
#     [],
#     {'s0': set(), 's1': set(), 'ss': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs','r0','r1'],
#     'rs',
#     ['send0','send1','lds','ack0','ack1'],
#     {'r0': [['lds','send1'],['ack0']], 'r1': [['lds','send0'],['ack1']], 'rs' : [['lds','send1']]},
#     [('rs', 'lds', 'rs'), ('rs', 'send1', 'r1'),
#      ('r1', 'lds', 'r1'), ('r1', 'send0', 'r0'), ('r1', 'ack1', 'r1'),
#      ('r0', 'lds', 'r0'), ('r0', 'send1', 'r1'), ('r0', 'ack0', 'r0')],
#     [],
#     {'r0': set(), 'r1': set(), 'rs': set()}
#     )


# # Fifth Version
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s0','s1'],
#     's1',
#     ['send0','send1','next','ack1','ack0','ldr'],
#     {'s0': [['next'],['send0'],['ack1','ack0','ldr']], 's1': [['next'],['send1'],['ack1','ack0','ldr']]},
#     [('s0', 'send0', 's0'), ('s0', 'next', 's1'), ('s1', 'next', 's0'), ('s1', 'send1', 's1'),
#      ('s0', 'ack0', 's0'), ('s0', 'ack1', 's0'), ('s0', 'ldr', 's0'),
#      ('s1', 'ack0', 's1'), ('s1', 'ack1', 's1'), ('s1', 'ldr', 's1')],
#     [],
#     {'s0': set(), 's1': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rb','r0','r1'],
#     'rb',
#     ['send0','send1','lost','dup','ack0','ack1'],
#     {'rb': [['lost','send0','send1'],['ack0'],['ack1']], 'r0': [['lost','dup','send1'],['ack0']], 'r1': [['lost','dup','send0'],['ack1']]},
#     [('rb', 'lost', 'rb'), ('rb', 'send0', 'r0'), ('rb', 'send1', 'r1'), ('rb', 'ack0', 'r0'), ('rb', 'ack1', 'r0'), 
#      ('r1', 'dup', 'r1'), ('r1', 'lost', 'rb'), ('r1', 'send0', 'r0'), 
#      ('r0', 'dup', 'r0'), ('r0', 'lost', 'rb'), ('r0', 'send1', 'r1'), ('r0', 'ack0', 'r0'), ('r1', 'ack1', 'r1')],
#     [],
#     {'rb': set(), 'r0': set(), 'r1': set()}
#     )

# # Sixth Version
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s0','d0','l0','s1','d1','l1'],
#     's1',
#     ['send0','send1','next','ack1','ack0','lostr','dupr'],
#     {
#         's0': [['next'],['send0'],['ack1','ack0','lostr','dupr']], 
#         'd0': [['next'],['send0'],['ack1','ack0','lostr','dupr']],
#         'l0': [['next'],['send0'],['ack1','ack0','lostr','dupr']],  
#         's1': [['next'],['send1'],['ack1','ack0','lostr','dupr']], 
#         'd1': [['next'],['send1'],['ack1','ack0','lostr','dupr']],
#         'l1': [['next'],['send1'],['ack1','ack0','lostr','dupr']]
#     },
#     [
#         ('s0', 'send0', 's0'), ('s0', 'next', 's1'), ('s0', 'ack0', 's0'), ('s0', 'ack1', 's0'),('s0', 'dupr', 'd0'), ('s0', 'lostr', 'l0'),
#         ('d0', 'next', 's1'), ('d0', 'dupr', 'd0'), ('d0', 'lostr', 'l0'), ('d0', 'send0', 'd0'),('d0', 'ack1', 'd0'), ('d0', 'ack0', 'd0'),
#         ('l0', 'next', 's1'), ('l0', 'dupr', 'd0'), ('l0', 'lostr', 'l0'), ('l0', 'send0', 'l0'),('l0', 'ack1', 'l0'), ('l0', 'ack0', 'l0'),
#         ('s1', 'send1', 's1'), ('s1', 'next', 's0'), ('s1', 'ack0', 's1'), ('s1', 'ack1', 's1'),('s1', 'dupr', 'd1'), ('s1', 'lostr', 'l1'),
#         ('d1', 'next', 's0'), ('d1', 'dupr', 'd1'), ('d1', 'lostr', 'l1'), ('d1', 'send1', 'd1'),('d1', 'ack1', 'd1'), ('d1', 'ack0', 'd1'),
#         ('l1', 'next', 's0'), ('l1', 'dupr', 'd1'), ('l1', 'lostr', 'l1'), ('l1', 'send1', 'l1'),('l1', 'ack1', 'l1'), ('l1', 'ack0', 'l1')
#     ],
#     [],
#     {'s0': set(), 'd0': set(), 'l0': set(), 's1': set(), 'd1': set(), 'l1': set(),}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs','r0','d0','l0','r1','d1','l1'],
#     'rs',
#     ['send0','send1','losts','dups','ack0','ack1'],
#     {
#         'rs': [['losts', 'send1']],
#         'r0': [['ack0'],['send1','losts','dups']], 
#         'd0': [['ack0'],['send1','losts','dups']],
#         'l0': [['ack0'],['send1','losts','dups']],  
#         'r1': [['ack1'],['send0','losts','dups']], 
#         'd1': [['ack1'],['send0','losts','dups']],
#         'l1': [['ack1'],['send0','losts','dups']]
#     },
#     [
#         ('rs', 'losts', 'rs'),('rs', 'send1', 'r1'),
#         ('r0', 'ack0', 'r0'),('r0', 'send1', 'r1'),('r0', 'dups', 'd0'),('r0', 'losts', 'l0'),
#         ('d0', 'send1', 'r1'),('d0', 'dups', 'd0'),('d0', 'losts', 'l0'),('d0', 'ack0', 'd0'),
#         ('l0', 'send1', 'r1'), ('l0', 'dups', 'd0'), ('l0', 'losts', 'l0'),('l0', 'ack0', 'l0'),
#         ('r1', 'ack1', 'r1'),('r1', 'send0', 'r0'),('r1', 'dups', 'd1'),('r1', 'losts', 'l1'),
#         ('d1', 'send0', 'r0'),('d1', 'dups', 'd1'),('d1', 'losts', 'l1'),('d1', 'ack1', 'd1'),
#         ('l1', 'send0', 'r0'), ('l1', 'dups', 'd1'), ('l1', 'losts', 'l1'),('l1', 'ack1', 'l1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'd0': set(), 'l0': set(), 'r1': set(), 'd1': set(), 'l1': set(),}
#     )

# # Final version
# # Full model
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['ss','s11','d11','l11','s01','d01','l01','s00','d00','l00','s10','d10','l10'],
#     'ss',
#     ['send0','send1','next','ack1','ack0','lostr','dupr'],
#     {
#         'ss': [['send1'],['lostr','ack0','ack1']],
#         's11': [['next'],['send1'],['ack0','lostr','dupr']], 
#         'd11': [['next'],['send1'],['ack0','lostr','dupr']],
#         'l11': [['next'],['send1'],['ack0','lostr','dupr']],  
#         's01': [['next'],['send0'],['ack0','lostr','dupr']], 
#         'd01': [['next'],['send0'],['ack0','lostr','dupr']],
#         'l01': [['next'],['send0'],['ack0','lostr','dupr']],
#         's00': [['next'],['send0'],['ack1','lostr','dupr']], 
#         'd00': [['next'],['send0'],['ack1','lostr','dupr']],
#         'l00': [['next'],['send0'],['ack1','lostr','dupr']],  
#         's10': [['next'],['send1'],['ack1','lostr','dupr']], 
#         'd10': [['next'],['send1'],['ack1','lostr','dupr']],
#         'l10': [['next'],['send1'],['ack1','lostr','dupr']],
#     },
#     [
#         ('ss', 'send1', 'ss'), ('ss', 'lostr', 'ss'), ('ss', 'ack0', 's10'), ('ss', 'ack1', 's11'),
        
#         ('s11', 'send1', 's11'), ('s11', 'ack0', 's10'), ('s11', 'next', 's01'), ('s11', 'dupr', 'd11'), ('s11', 'lostr', 'l11'),
#         ('d11', 'send1', 'd11'), ('d11', 'ack0', 's10'), ('d11', 'next', 'd01'), ('d11', 'dupr', 'd11'), ('d11', 'lostr', 'l11'),
#         ('l11', 'send1', 'l11'), ('l11', 'ack0', 's10'), ('l11', 'next', 'l01'), ('l11', 'dupr', 'd11'), ('l11', 'lostr', 'l11'),
#         ('s01', 'send0', 's01'), ('s01', 'ack0', 's00'), ('s01', 'next', 's11'), ('s01', 'dupr', 'd01'), ('s01', 'lostr', 'l01'),
#         ('d01', 'send0', 'd01'), ('d01', 'ack0', 's00'), ('d01', 'next', 'd11'), ('d01', 'dupr', 'd01'), ('d01', 'lostr', 'l01'),
#         ('l01', 'send0', 'l01'), ('l01', 'ack0', 's00'), ('l01', 'next', 'l11'), ('l01', 'dupr', 'd01'), ('l01', 'lostr', 'l01'),
        
#         ('s10', 'send1', 's10'), ('s10', 'ack1', 's11'), ('s10', 'next', 's00'), ('s10', 'dupr', 'd10'), ('s10', 'lostr', 'l10'),
#         ('d10', 'send1', 'd10'), ('d10', 'ack1', 's11'), ('d10', 'next', 'd00'), ('d10', 'dupr', 'd10'), ('d10', 'lostr', 'l10'),
#         ('l10', 'send1', 'l10'), ('l10', 'ack1', 's11'), ('l10', 'next', 'l00'), ('l10', 'dupr', 'd10'), ('l10', 'lostr', 'l10'),
#         ('s00', 'send0', 's00'), ('s00', 'ack1', 's01'), ('s00', 'next', 's10'), ('s00', 'dupr', 'd00'), ('s00', 'lostr', 'l00'),
#         ('d00', 'send0', 'd00'), ('d00', 'ack1', 's01'), ('d00', 'next', 'd10'), ('d00', 'dupr', 'd00'), ('d00', 'lostr', 'l00'),
#         ('l00', 'send0', 'l00'), ('l00', 'ack1', 's01'), ('l00', 'next', 'l10'), ('l00', 'dupr', 'd00'), ('l00', 'lostr', 'l00'),
#     ],
#     [],
#     {'ss': set(), 'ss': set(),'s11': set(),'d11': set(),'l11': set(),'s01': set(),'d01': set(),'l01': set(),'s00': set(),'d00': set(),'l00': set(),'s10': set(),'d10': set(),'l10': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs','r0','d0','l0','r1','d1','l1'],
#     'rs',
#     ['send0','send1','losts','dups','ack0','ack1'],
#     {
#         'rs': [['losts', 'send1']],
#         'r0': [['ack0'],['send1','losts','dups']], 
#         'd0': [['ack0'],['send1','losts','dups']],
#         'l0': [['ack0'],['send1','losts','dups']],  
#         'r1': [['ack1'],['send0','losts','dups']], 
#         'd1': [['ack1'],['send0','losts','dups']],
#         'l1': [['ack1'],['send0','losts','dups']]
#     },
#     [
#         ('rs', 'losts', 'rs'),('rs', 'send1', 'r1'),
#         ('r0', 'ack0', 'r0'),('r0', 'send1', 'r1'),('r0', 'dups', 'd0'),('r0', 'losts', 'l0'),
#         ('d0', 'send1', 'r1'),('d0', 'dups', 'd0'),('d0', 'losts', 'l0'),('d0', 'ack0', 'd0'),
#         ('l0', 'send1', 'r1'), ('l0', 'dups', 'd0'), ('l0', 'losts', 'l0'),('l0', 'ack0', 'l0'),
#         ('r1', 'ack1', 'r1'),('r1', 'send0', 'r0'),('r1', 'dups', 'd1'),('r1', 'losts', 'l1'),
#         ('d1', 'send0', 'r0'),('d1', 'dups', 'd1'),('d1', 'losts', 'l1'),('d1', 'ack1', 'd1'),
#         ('l1', 'send0', 'r0'), ('l1', 'dups', 'd1'), ('l1', 'losts', 'l1'),('l1', 'ack1', 'l1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'd0': set(), 'l0': set(), 'r1': set(), 'd1': set(), 'l1': set(),}
#     )

# # Remove lost and dup loops 
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['ss','s11','d11','l11','s01','d01','l01','s00','d00','l00','s10','d10','l10'],
#     'ss',
#     ['send0','send1','next','ack1','ack0','lostr','dupr'],
#     {
#         'ss': [['send1'],['lostr','ack0','ack1']],
#         's11': [['next'],['send1'],['ack0','lostr','dupr']], 
#         'd11': [['next'],['send1'],['ack0','lostr']],
#         'l11': [['next'],['send1'],['ack0','dupr']],  
#         's01': [['next'],['send0'],['ack0','lostr','dupr']], 
#         'd01': [['next'],['send0'],['ack0','lostr']],
#         'l01': [['next'],['send0'],['ack0','dupr']],
#         's00': [['next'],['send0'],['ack1','lostr','dupr']], 
#         'd00': [['next'],['send0'],['ack1','lostr']],
#         'l00': [['next'],['send0'],['ack1','dupr']],  
#         's10': [['next'],['send1'],['ack1','lostr','dupr']], 
#         'd10': [['next'],['send1'],['ack1','lostr']],
#         'l10': [['next'],['send1'],['ack1','dupr']],
#     },
#     [
#         ('ss', 'send1', 'ss'), ('ss', 'lostr', 'ss'), ('ss', 'ack0', 's10'), ('ss', 'ack1', 's11'),
        
#         ('s11', 'send1', 's11'), ('s11', 'ack0', 's10'), ('s11', 'next', 's01'), ('s11', 'dupr', 'd11'), ('s11', 'lostr', 'l11'),
#         ('d11', 'send1', 'd11'), ('d11', 'ack0', 's10'), ('d11', 'next', 'd01'), ('d11', 'lostr', 'l11'),
#         ('l11', 'send1', 'l11'), ('l11', 'ack0', 's10'), ('l11', 'next', 'l01'), ('l11', 'dupr', 'd11'),
#         ('s01', 'send0', 's01'), ('s01', 'ack0', 's00'), ('s01', 'next', 's11'), ('s01', 'dupr', 'd01'), ('s01', 'lostr', 'l01'),
#         ('d01', 'send0', 'd01'), ('d01', 'ack0', 's00'), ('d01', 'next', 'd11'), ('d01', 'lostr', 'l01'),
#         ('l01', 'send0', 'l01'), ('l01', 'ack0', 's00'), ('l01', 'next', 'l11'), ('l01', 'dupr', 'd01'),
        
#         ('s10', 'send1', 's10'), ('s10', 'ack1', 's11'), ('s10', 'next', 's00'), ('s10', 'dupr', 'd10'), ('s10', 'lostr', 'l10'),
#         ('d10', 'send1', 'd10'), ('d10', 'ack1', 's11'), ('d10', 'next', 'd00'), ('d10', 'lostr', 'l10'),
#         ('l10', 'send1', 'l10'), ('l10', 'ack1', 's11'), ('l10', 'next', 'l00'), ('l10', 'dupr', 'd10'),
#         ('s00', 'send0', 's00'), ('s00', 'ack1', 's01'), ('s00', 'next', 's10'), ('s00', 'dupr', 'd00'), ('s00', 'lostr', 'l00'),
#         ('d00', 'send0', 'd00'), ('d00', 'ack1', 's01'), ('d00', 'next', 'd10'), ('d00', 'lostr', 'l00'),
#         ('l00', 'send0', 'l00'), ('l00', 'ack1', 's01'), ('l00', 'next', 'l10'), ('l00', 'dupr', 'd00'),
#     ],
#     [],
#     {'ss': set(), 'ss': set(),'s11': set(),'d11': set(),'l11': set(),'s01': set(),'d01': set(),'l01': set(),'s00': set(),'d00': set(),'l00': set(),'s10': set(),'d10': set(),'l10': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs','r0','d0','l0','r1','d1','l1'],
#     'rs',
#     ['send0','send1','losts','dups','ack0','ack1'],
#     {
#         'rs': [['losts', 'send1']],
#         'r0': [['ack0'],['send1','losts','dups']], 
#         'd0': [['ack0'],['send1','losts']],
#         'l0': [['ack0'],['send1','dups']],  
#         'r1': [['ack1'],['send0','losts','dups']], 
#         'd1': [['ack1'],['send0','losts']],
#         'l1': [['ack1'],['send0','dups']]
#     },
#     [
#         ('rs', 'losts', 'rs'),('rs', 'send1', 'r1'),
#         ('r0', 'ack0', 'r0'),('r0', 'send1', 'r1'),('r0', 'dups', 'd0'),('r0', 'losts', 'l0'),
#         ('d0', 'send1', 'r1'),('d0', 'losts', 'l0'),('d0', 'ack0', 'd0'),
#         ('l0', 'send1', 'r1'), ('l0', 'dups', 'd0'),('l0', 'ack0', 'l0'),
#         ('r1', 'ack1', 'r1'),('r1', 'send0', 'r0'),('r1', 'dups', 'd1'),('r1', 'losts', 'l1'),
#         ('d1', 'send0', 'r0'),('d1', 'losts', 'l1'),('d1', 'ack1', 'd1'),
#         ('l1', 'send0', 'r0'), ('l1', 'dups', 'd1'),('l1', 'ack1', 'l1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'd0': set(), 'l0': set(), 'r1': set(), 'd1': set(), 'l1': set(),}
#     )

# # Merge lost and dup states 
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['ss','s11','ld11','s01','ld01','s00','ld00','s10','ld10'],
#     'ss',
#     ['send0','send1','next','ack1','ack0','ldr'],
#     {
#         'ss': [['send1'],['ack0','ack1']],
#         's11': [['next'],['send1'],['ack0','ldr']], 
#         'ld11': [['next'],['send1'],['ack0']],
#         's01': [['next'],['send0'],['ack0','ldr']], 
#         'ld01': [['next'],['send0'],['ack0']],
#         's00': [['next'],['send0'],['ack1','ldr']], 
#         'ld00': [['next'],['send0'],['ack1']],
#         's10': [['next'],['send1'],['ack1','ldr']], 
#         'ld10': [['next'],['send1'],['ack1']],
#     },
#     [
#         ('ss', 'send1', 'ss'), ('ss', 'ack0', 's10'), ('ss', 'ack1', 's11'),
        
#         ('s11', 'send1', 's11'), ('s11', 'ack0', 's10'), ('s11', 'next', 's01'), ('s11', 'ldr', 'ld11'),
#         ('ld11', 'send1', 'ld11'), ('ld11', 'ack0', 's10'), ('ld11', 'next', 'ld01'),
#         ('s01', 'send0', 's01'), ('s01', 'ack0', 's00'), ('s01', 'next', 's11'), ('s01', 'ldr', 'ld01'),
#         ('ld01', 'send0', 'ld01'), ('ld01', 'ack0', 's00'), ('ld01', 'next', 'ld11'),
        
#         ('s10', 'send1', 's10'), ('s10', 'ack1', 's11'), ('s10', 'next', 's00'), ('s10', 'ldr', 'ld10'),
#         ('ld10', 'send1', 'ld10'), ('ld10', 'ack1', 's11'), ('ld10', 'next', 'ld00'),
#         ('s00', 'send0', 's00'), ('s00', 'ack1', 's01'), ('s00', 'next', 's10'), ('s00', 'ldr', 'ld00'),
#         ('ld00', 'send0', 'ld00'), ('ld00', 'ack1', 's01'), ('ld00', 'next', 'ld10'),
#     ],
#     [],
#     {'ss': set(), 'ss': set(),'s11': set(),'ld11': set(),'s01': set(),'ld01': set(),'s00': set(),'ld00': set(),'s10': set(),'ld10': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs','r0','ld0','r1','ld1'],
#     'rs',
#     ['send0','send1','lds','ack0','ack1'],
#     {
#         'rs': [['send1']],
#         'r0': [['ack0'],['send1','lds']], 
#         'ld0': [['ack0'],['send1']],  
#         'r1': [['ack1'],['send0','lds']], 
#         'ld1': [['ack1'],['send0']],
#     },
#     [
#         ('rs', 'send1', 'r1'),
#         ('r0', 'ack0', 'r0'),('r0', 'send1', 'r1'),('r0', 'lds', 'ld0'),
#         ('ld0', 'send1', 'r1'),('ld0', 'ack0', 'ld0'),
#         ('r1', 'ack1', 'r1'),('r1', 'send0', 'r0'),('r1', 'lds', 'ld1'),
#         ('ld1', 'send0', 'r0'),('ld1', 'ack1', 'ld1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'ld0': set(), 'r1': set(), 'ld1': set(),}
#     )

# Merge x_i0 with x_i1 for each x in {l, s, d} for sender, now they do not store the last type of acknowledgement. 
# Remove ss as it is redundant
# Sender
sender = amas.AMASagent(
    'Sender', 
    0, 
    ['s1','ld1','s0','ld0'],
    's1',
    ['send0','send1','next','ack1','ack0','ldr'],
    {
        's1': [['next'],['send1'],['ack0','ldr','ack1']], 
        'ld1': [['next'],['send1'],['ack1','ack0']],
        's0': [['next'],['send0'],['ack0','ldr','ack1']], 
        'ld0': [['next'],['send0'],['ack0','ack1']],
    },
    [   
        ('s1', 'send1', 's1'), ('s1', 'ack0', 's1'), ('s1', 'ack1', 's1'), ('s1', 'next', 's0'), ('s1', 'ldr', 'ld1'),
        ('ld1', 'send1', 'ld1'), ('ld1', 'ack0', 's1'), ('ld1', 'ack1', 's1'), ('ld1', 'next', 'ld0'),
        ('s0', 'send0', 's0'), ('s0', 'ack0', 's0'), ('s0', 'ack1', 's0'), ('s0', 'next', 's1'), ('s0', 'ldr', 'ld0'),
        ('ld0', 'send0', 'ld0'), ('ld0', 'ack0', 's0'), ('ld0', 'ack1', 'ld0'), ('ld0', 'next', 'ld1'),
    ],
    [],
    {'s1': set(), 'ld1': set(), 's0': set(), 'ld0': set()}
    )
# Receiver
receiver = amas.AMASagent(
    'Receiver', 
    1, 
    ['rs','r0','ld0','r1','ld1'],
    'rs',
    ['send0','send1','lds','ack0','ack1'],
    {
        'rs': [['send1']],
        'r0': [['ack0'],['send1','lds']], 
        'ld0': [['ack0'],['send1']],  
        'r1': [['ack1'],['send0','lds']], 
        'ld1': [['ack1'],['send0']],
    },
    [
        ('rs', 'send1', 'r1'),
        ('r0', 'ack0', 'r0'),('r0', 'send1', 'r1'),('r0', 'lds', 'ld0'),
        ('ld0', 'send1', 'r1'),('ld0', 'ack0', 'ld0'),
        ('r1', 'ack1', 'r1'),('r1', 'send0', 'r0'),('r1', 'lds', 'ld1'),
        ('ld1', 'send0', 'r0'),('ld1', 'ack1', 'ld1'),
    ],
    [],
    {'rs': set(), 'r0': set(), 'ld0': set(), 'r1': set(), 'ld1': set(),}
    )

# # Merge send and receive events 
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['ss','s11','ld11','s01','ld01','s00','ld00','s10','ld10'],
#     'ss',
#     ['next','s0a1','s0a0','s0ldr','s1a1','s1a0','s1ldr',],
#     {
#         'ss': [['s1a0','s1a1']],
#         's11': [['next'],['s1a0','s1ldr']], 
#         'ld11': [['next'],['s1a0']],
#         's01': [['next'],['s0a0','s0ldr']], 
#         'ld01': [['next'],['s0a0']],
#         's00': [['next'],['s0a1','s0ldr']], 
#         'ld00': [['next'],['s0a1']],
#         's10': [['next'],['s1a1','s1ldr']], 
#         'ld10': [['next'],['s1a1']],
#     },
#     [
#         ('ss', 's1a0', 's10'), ('ss', 's1a1', 's11'),
        
#         ('s11', 's1a0', 's10'), ('s11', 'next', 's01'), ('s11', 's1ldr', 'ld11'),
#         ('ld11', 's1a0', 's10'), ('ld11', 'next', 'ld01'),
#         ('s01', 's0a0', 's00'), ('s01', 'next', 's11'), ('s01', 's0ldr', 'ld01'),
#         ('ld01', 's0a0', 's00'), ('ld01', 'next', 'ld11'),
        
#         ('s10', 's1a1', 's11'), ('s10', 'next', 's00'), ('s10', 's1ldr', 'ld10'),
#         ('ld10', 's1a1', 's11'), ('ld10', 'next', 'ld00'),
#         ('s00', 's0a1', 's01'), ('s00', 'next', 's10'), ('s00', 's0ldr', 'ld00'),
#         ('ld00', 's0a1', 's01'), ('ld00', 'next', 'ld10'),
#     ],
#     [],
#     {'ss': set(), 'ss': set(),'s11': set(),'ld11': set(),'s01': set(),'ld01': set(),'s00': set(),'ld00': set(),'s10': set(),'ld10': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs','r0','ld0','r1','ld1'],
#     'rs',
#     ['s1a1','s1a0','ldsa0','s0a1','ldsa1'],
#     {
#         'rs': [['s1a1']],
#         'r0': [['s1a0','ldsa0']], 
#         'ld0': [['s1a0']],  
#         'r1': [['s0a1','ldsa1']], 
#         'ld1': [['s0a1']],
#     },
#     [
#         ('rs', 's1a1', 'r1'),
#         ('r0', 's1a0', 'r1'),('r0', 'ldsa0', 'ld0'),
#         ('ld0', 's1a0', 'ld0'),
#         ('r1', 's0a1', 'r0'),('r1', 'ldsa1', 'ld1'),
#         ('ld1', 's0a1', 'ld1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'ld0': set(), 'r1': set(), 'ld1': set(),}
#     )

# # Remove unecessary starting states ss, replace by s11 
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s11','ld11','s01','ld01','s00','ld00','s10','ld10'],
#     's11',
#     ['next','s0a1','s0a0','s0ldr','s1a1','s1a0','s1ldr',],
#     {
#         's11': [['next'],['s1a0','s1ldr']], 
#         'ld11': [['next'],['s1a0']],
#         's01': [['next'],['s0a0','s0ldr']], 
#         'ld01': [['next'],['s0a0']],
#         's00': [['next'],['s0a1','s0ldr']], 
#         'ld00': [['next'],['s0a1']],
#         's10': [['next'],['s1a1','s1ldr']], 
#         'ld10': [['next'],['s1a1']],
#     },
#     [   
#         ('s11', 's1a0', 's10'), ('s11', 'next', 's01'), ('s11', 's1ldr', 'ld11'),
#         ('ld11', 's1a0', 's10'), ('ld11', 'next', 'ld01'),
#         ('s01', 's0a0', 's00'), ('s01', 'next', 's11'), ('s01', 's0ldr', 'ld01'),
#         ('ld01', 's0a0', 's00'), ('ld01', 'next', 'ld11'),
        
#         ('s10', 's1a1', 's11'), ('s10', 'next', 's00'), ('s10', 's1ldr', 'ld10'),
#         ('ld10', 's1a1', 's11'), ('ld10', 'next', 'ld00'),
#         ('s00', 's0a1', 's01'), ('s00', 'next', 's10'), ('s00', 's0ldr', 'ld00'),
#         ('ld00', 's0a1', 's01'), ('ld00', 'next', 'ld10'),
#     ],
#     [],
#     {'s11': set(),'ld11': set(),'s01': set(),'ld01': set(),'s00': set(),'ld00': set(),'s10': set(),'ld10': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs', 'r0','ld0','r1','ld1'],
#     'rs',
#     ['s1a1','s1a0','ldsa0','s0a1','ldsa1'],
#     {
#         'rs': [['s1a1']],
#         'r0': [['s1a0','ldsa0']], 
#         'ld0': [['s1a0']],  
#         'r1': [['s0a1','ldsa1']], 
#         'ld1': [['s0a1']],
#     },
#     [
#         ('rs', 's1a1', 'r1'),
#         ('r0', 's1a0', 'r1'),('r0', 'ldsa0', 'ld0'),
#         ('ld0', 's1a0', 'ld0'),
#         ('r1', 's0a1', 'r0'),('r1', 'ldsa1', 'ld1'),
#         ('ld1', 's0a1', 'ld1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'ld0': set(), 'r1': set(), 'ld1': set(),}
#     )

# # Merge x_i0 with x_i1 for each x in {l, s, d} for sender, now they do not store the last type of acknowledgement. 
# # Sender
# sender = amas.AMASagent(
#     'Sender', 
#     0, 
#     ['s1','ld1','s0','ld0'],
#     's1',
#     ['next','s0a1','s0a0','s0ldr','s1a1','s1a0','s1ldr','ldsa0', 'ldsa1'],
#     {
#         's1': [['next'], ['s1a0', 's1a1', 's1ldr', 'ldsa0', 'ldsa1']],
#         'ld1': [['next'], ['s1a0', 's1a1', 'ldsa0', 'ldsa1']],
#         's0': [['next'], ['s0a0', 's0a1', 's0ldr', 'ldsa0', 'ldsa1']],
#         'ld0': [['next'], ['s0a0', 's0a1', 'ldsa0', 'ldsa1']],
#     },
#     [   
#         ('s1', 's1a0', 's1'), ('s1', 's1a1', 's1'), ('s1', 'next', 's0'), ('s1', 's1ldr', 'ld1'),
#         ('ld1', 's1a0', 's1'), ('ld1', 's1a1', 's1'), ('ld1', 'next', 'ld0'),
#         ('s0', 's0a0', 's0'), ('s0', 's0a1', 's0'), ('s0', 'next', 's1'), ('s0', 's0ldr', 'ld0'),
#         ('ld0', 's0a0', 's0'), ('ld0', 's0a1', 's0'), ('ld0', 'next', 'ld1'),
        
#     ],
#     [],
#     {'s1': set(),'ld1': set(),'s0': set(),'ld0': set()}
#     )

# # Receiver
# receiver = amas.AMASagent(
#     'Receiver', 
#     1, 
#     ['rs', 'r0','ld0','r1','ld1'],
#     'rs',
#     ['s1a1','s1a0','ldsa0','s0a1','ldsa1'],
#     {
#         'rs': [['s1a1']],
#         'r0': [['s1a0','ldsa0']], 
#         'ld0': [['s1a0']],  
#         'r1': [['s0a1','ldsa1']], 
#         'ld1': [['s0a1']],
#     },
#     [
#         ('rs', 's1a1', 'r1'),
#         ('r0', 's1a0', 'r1'),('r0', 'ldsa0', 'ld0'),
#         ('ld0', 's1a0', 'ld0'),
#         ('r1', 's0a1', 'r0'),('r1', 'ldsa1', 'ld1'),
#         ('ld1', 's0a1', 'ld1'),
#     ],
#     [],
#     {'rs': set(), 'r0': set(), 'ld0': set(), 'r1': set(), 'ld1': set(),}
#     )

# # Separate each agent into a 'writer' and 'reader' modules. The writer has the task of sending messages through
# # channels whilst the readers read from incoming channels
# # Sender
# # Writer
# sender_w = amas.AMASagent(
#     'Sender writer',
#     0,
#     ['s1', 's0'],
#     's1',
#     ['send1','send0','next'],
#     {
#         's1': [['next'],['send1']],
#         's0': [['next'],['send0']],
#     },
#     [
#         ('s1', 'next', 's0'), ('s1', 'send1', 's1'),
#         ('s0', 'next', 's1'), ('s0', 'send0', 's0'),
#     ],
#     [],
#     {'s1': set(), 's0': set()}
# )
# # Reader
# sender_r = amas.AMASagent(
#     'Sender reader',
#     1,
#     ['ab', 'a0', 'a1'],
#     'ab',
#     ['ack1','ack0','ldr'],
#     {
#         'ab': [['ack0','ack1']],
#         'a0': [['ack1','ldr']],
#         'a1': [['ack0','ldr']],
#     },
#     [
#         ('ab', 'ack0', 'a0'), ('ab', 'ack1', 'a1'),
#         ('a0', 'ack1', 'a1'), ('a0', 'ldr', 'ab'),
#         ('a1', 'ack0', 'a0'), ('a1', 'ldr', 'ab'),
#     ],
#     [],
#     {'ab': set(), 'a1': set(), 'a0': set()}
# )
# # Reader
# # Writer
# receiver_w = amas.AMASagent(
#     'Receiver writer',
#     2,
#     ['as'],
#     'as',
#     ['ack1','ack0'],
#     {
#         'as': [['ack1'],['ack0']],
#     },
#     [
#         ('as', 'ack1', 'as'), ('as', 'ack0', 'as'),
#     ],
#     [],
#     {'as': set(), }
# )
# # Reader
# receiver_r = amas.AMASagent(
#     'Receiver reader',
#     3,
#     ['rb', 'r0', 'r1'],
#     'rb',
#     ['send1','send0','lds'],
#     {
#         'rb': [['send0','send1']],
#         'r0': [['send1','lds']],
#         'r1': [['send0','lds']],
#     },
#     [
#         ('rb', 'send0', 'r0'), ('rb', 'send1', 'r1'),
#         ('r0', 'send1', 'r1'), ('r0', 'lds', 'rb'),
#         ('r1', 'send0', 'r0'), ('r1', 'lds', 'rb'),
#     ],
#     [],
#     {'rb': set(), 'r1': set(), 'r0': set()}
# )

# Create AMAS S with the agents (controller and trains)
S = amas.AMAS([sender, receiver])
#S = amas.AMAS([sender_w, sender_r, receiver_w, receiver_r])

# Print all components of each agent of the AMAS S, save contents into train_amas.txt in the "outputs" directory
S.print("abp_amas.txt")

# Induce I/O iCGS M on the AMAS S
M = S.joint_game()

# Print all components of the CGS, save contents into train_cgs.txt in the "outputs" directory
M.print("abp_cgs.txt")

# Project AMAS S on the CGS M.
P = S.project(M)

P.print()

# Expand S with induced CGS M and projections P
expanded = S.expand(M, P)

# Print the expanded AMAS, save contents in text file in directory.
expanded.print("abp_expanded_amas_first.txt")

# Create expanded game (induce I/O iCGS on the expanded AMAS).
expanded_game = expanded.joint_game()

# Print the expanded game and save contents into file in directory.
expanded_game.print("abp_expanded_cgs_first.txt")

# Expand the AMAS again
expanded_expanded = expanded.expand()

# Print it and save
expanded_expanded.print("abp_expanded_amas_second.txt")

# Induce I/O iCGS on this new expansion
expanded_expanded_game = expanded_expanded.joint_game()

# Print it and save
expanded_expanded_game.print("abp_expanded_cgs_second.txt")

expanded_expanded.expand().print("abp_expanded_amas_third.txt")