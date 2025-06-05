import read_input
import amas
import amas_IOiCGS
import amas_projection

S = read_input.read_amas_from_json("train_controller")

M = amas_IOiCGS.AMASIOiCGS(S, trace_file='cgs_const.trace')

projections : list[amas_projection.AgentProjection] = []

for agent in S.agents:
    projections.append(amas_projection.AgentProjection(S, agent.number, M, trace_file=f'proj_const{agent.number}.trace'))

P = amas_projection.MKBSC_AMAS_Projection(projections)

E = S.expand(M, P)

S.print('train_controller_amas.txt')
M.print('train_controller_cgs.txt')
P.print('train_controller_projections.txt')
E.print('train_controller_amas_expansion1.txt')

