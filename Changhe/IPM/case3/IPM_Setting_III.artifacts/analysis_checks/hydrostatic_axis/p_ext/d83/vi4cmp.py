import json,pickle,sympy as s,math
x,a,u1=s.symbols('x a u1')
c=json.load(open('../../../referee/x3q/d23/certificates/1_3_2_2_1_1_1_1.json'))
def todict(terms): return {tuple(e):int(v) for e,v in terms}
def norm(D):
    g=0
    for v in D.values(): g=math.gcd(g,v)
    lead=D[max(D)]; sg=1 if lead>0 else -1
    return {k:sg*v//g for k,v in D.items()}
N=pickle.load(open('t6g_23_1_6_4_2_4_s1.pkl','rb'))['N']
for i,P in enumerate(N):
    mine={m:int(v) for m,v in s.Poly(P,u1,a,x).terms()}
    print('equation',i,'identical up to sign/content:',norm(mine)==norm(todict(c['equations'][i])))
for st,i in (('r01',0),('r02',1)):
    mine={(0,)+m:int(v) for m,v in s.Poly(pickle.load(open('t6g_23_1_6_4_2_4_%s.pkl'%st,'rb')),a,x).terms()}
    th=todict(c['inner_resultants'][i])
    print(st,'identical:',norm(mine)==norm(th),len(mine),len(th))
