import read_input
import amas
import amas_IOiCGS
import amas_projection

S = read_input.read_amas_from_json("train_controller")

M = amas_IOiCGS.AMASIOiCGS(S)

P = amas_projection.MKBSC_AMAS_Projection(M)

E = S.expand(M, P)

