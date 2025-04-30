import amas


# This has the train controller example.

# Train 1

train1 = amas.AMASagent(
    'Train 1', 
    1, 
    ['W','T','A'],
    'W',
    ['a1','a2','a3'],
    {'A': [['a3']], 'W': [['a1']], 'T': [['a2']]},
    [('A', 'a3', 'W'), ('W', 'a1', 'T'), ('T', 'a2', 'A')],
    ['inside1'],
    {'A': {}, 'W': {}, 'T': {'inside1'}}
    )

# Train 2

train2 = amas.AMASagent(
    'Train 2', 
    2, 
    ['W','T','A'],
    'W',
    ['b1','b2','b3'],
    {'A': [['b3']], 'W': [['b1']], 'T': [['b2']]},
    [('A', 'b3', 'W'), ('W', 'b1', 'T'), ('T', 'b2', 'A')],
    ['inside2'],
    {'A': {}, 'W': {}, 'T': {'inside2'}}
    )

# Controller

controller = amas.AMASagent(
    'Controller', 
    0, 
    ['G','R'],
    'G',
    ['a1','a2','b1','b2'],
    {'G': [['a1'],['b1']], 'R': [['a2','b2']]},
    [('G', 'a1', 'R'), ('G', 'b1', 'R'), ('R', 'a2', 'G'), ('R', 'b2', 'G')],
    ['free'],
    {'G': {'free'}, 'R': {}}
    )

# Create AMAS S with the agents (controller and trains)
S = amas.AMAS([controller,train1,train2])

# Print all components of each agent of the AMAS S, save contents into train_amas.txt in the "outputs" directory
S.print("train_amas.txt")

# Induce I/O iCGS M on the AMAS S
M = S.joint_game()

# Print all components of the CGS, save contents into train_cgs.txt in the "outputs" directory
M.print("train_cgs.txt")

# Project AMAS S on the CGS M.
P = S.project(M)

# Expand S with induced CGS M and projections P
expanded = S.expand(M, P)

# Print the expanded AMAS, save contents in text file in directory.
expanded.print("train_expanded_amas_first.txt")

# Create expanded game (induce I/O iCGS on the expanded AMAS).
expanded_game = expanded.joint_game()

# Print the expanded game and save contents into file in directory.
expanded_game.print("train_expanded_cgs_first.txt")

# Expand the AMAS again
expanded_expanded = expanded.expand()

# Print it and save
expanded_expanded.print("train_expanded_amas_second.txt")

# Induce I/O iCGS on this new expansion
expanded_expanded_game = expanded_expanded.joint_game()

# Print it and save
expanded_expanded_game.print("train_expanded_cgs_second.txt")
