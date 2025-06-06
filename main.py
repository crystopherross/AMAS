import read_input
import amas_IOiCGS
import amas_projection

# Sucessful example
# Construct AMAS S from .json file.
S = read_input.read_amas_from_json("train_controller_success")
# Construct I/O iCGS M for S.
M = amas_IOiCGS.AMASIOiCGS(S, trace_file='succ_cgs_const.trace')

# Construct projections of M on S
projections : list[amas_projection.AgentProjection] = []

for agent in S.agents:
    projections.append(amas_projection.AgentProjection(S, agent.number, M, trace_file=f'succ_proj_const{agent.number}.trace'))

P = amas_projection.MKBSC_AMAS_Projection(projections)

# Expand S, creating SK
SK = S.expand(M, P)

# Construct the I/O iCGS for SK, creating MK
MK = amas_IOiCGS.AMASIOiCGS(SK, trace_file='succ_cgs_exp_const.trace')

# Record the structures to files
S.print('train_controller_succ_amas.txt')
M.print('train_controller_succ_cgs.txt')
P.print('train_controller_succ_projections.txt')
SK.print('train_controller_succ_amas_expansion1.txt')
MK.print('train_controller_succ_expansion1_cgs.txt')

# Failing example
# Construct AMAS S from .json file.
S = read_input.read_amas_from_json("train_controller_fail")
# Construct I/O iCGS M for S.
M = amas_IOiCGS.AMASIOiCGS(S, trace_file='fail_cgs_const.trace')

# Construct projections of M on S
projections : list[amas_projection.AgentProjection] = []

for agent in S.agents:
    projections.append(amas_projection.AgentProjection(S, agent.number, M, trace_file=f'fail_proj_const{agent.number}.trace'))

P = amas_projection.MKBSC_AMAS_Projection(projections)

# Expand S, creating SK
SK = S.expand(M, P)

# Construct the I/O iCGS for SK, creating MK
MK = amas_IOiCGS.AMASIOiCGS(SK, trace_file='fail_cgs_exp_const.trace')

# Record the structures to files
S.print('train_controller_fail_amas.txt')
M.print('train_controller_fail_cgs.txt')
P.print('train_controller_fail_projections.txt')
SK.print('train_controller_fail_expansion1_amas.txt')
MK.print('train_controller_fail_expansion1_cgs.txt')