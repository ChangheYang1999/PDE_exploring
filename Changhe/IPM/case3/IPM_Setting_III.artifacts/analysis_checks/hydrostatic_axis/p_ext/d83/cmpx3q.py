# compare my exact eliminants (t5g/t6g pickles) with the external degree-90/154/160 cores of the d = 23 answer
import json,pickle,sys
from flint import fmpz_poly
C='../../../referee/x3q/d23/certificates/'
def ext(pid):
    c=json.load(open(C+pid+'.json')); L=c['Lambda']
    return fmpz_poly([int(t) for t in L['coefficients_low_to_high']]),c.get('variables'),L['shift'],L['all_shifted_coefficients_positive']
def prim(p):
    import math; c=0
    for t in p.coeffs(): c=math.gcd(c,int(t))
    p=fmpz_poly([int(t)//c for t in p.coeffs()])
    return -p if p.coeffs()[-1]<0 else p
pairs=[('t5g_23_1_2_4_4','1_2_2_2_2_1_1_1','core'),('t5g_23_3_4_2_4','3_2_2_2_1_1_1_1','core'),
       ('t5g_23_1_4_2_5','1_2_2_2_1_1_1_1_1','core'),
       ('t6g_23_1_4_6_2_3_L1','1_3_3_2_1_1_1',None),('t6g_23_1_6_2_4_3_L1','1_3_2_2_2_1_1',None),
       ('t6g_23_1_8_4_2_3_L1','1_4_2_2_1_1_1',None),('t6g_23_3_6_4_2_3_L1','3_3_2_2_1_1_1',None)]
for mine,pid,key in pairs:
    E,var,sh,pos=ext(pid); E=prim(E)
    d=pickle.load(open(mine+'.pkl','rb'))
    M=fmpz_poly(d[key] if key else d)
    if key:
        same=(prim(M)==E); print(mine,pid,'deg',E.degree(),'identical up to sign and content:',same,'ext var',var,'shift',sh,pos)
    else:
        q,r=divmod(M,E); print(mine,pid,'deg ext',E.degree(),'divides my Lambda_1 exactly:',r==0,
              'ext var',var,'shift',sh,pos)
