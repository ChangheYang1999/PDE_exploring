"""Lead floating diagnostic for the knot-scale heuristic (report 6.5 item 10). On the vertical axis the weighted trace of
f_0 is g = [r A' + (D - r - 2 r') A]/a_* and that of X.grad rho_0 is q = (3 A + A')/a_*, with A the axis cofactor of
r^-3 rho_0 and r = ell - sum_n (-1)^n P_n. If the knot scale dominates, g^(5) is about r q^(5). This script compares
the central fifth differences of g and q (step 2^-18, inside one span) at the midpoint of every 8th span and a few
outer points. Not a certificate."""
import os,sys,time,json
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
sys.path.insert(0,'code/farres')
from fractions import Fraction as F
from flint import arb,ctx
import profile_points as PP
ctx.prec=160
G=PP.G;aa=G.aa
d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1
def gq(t):
 rh,drh,P,Q,Pt=PP.point(d,cache,t)
 A=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(rh)),arb(0))
 At=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(drh)),arb(0))
 r=ell-sum(((-1)**n*v for n,v in enumerate(P,1)),arb(0))
 rt=-sum(((-1)**n*v for n,v in enumerate(Pt,1)),arb(0))
 tt=aa(t);astar=(aa(F(9,5))*tt).exp()*(1+tt.exp())**(-aa(F(53,10)))
 return (r*At+(D-r-2*rt)*A)/astar,(3*A+At)/astar,r
hs=F(1,2**18)
def d5(t0):
 v={i:gq(t0+i*hs) for i in (-3,-2,-1,1,2,3)}
 c={-3:-1,-2:4,-1:-5,1:5,2:-4,3:1}
 return [sum((c[i]*v[i][k] for i in c),arb(0))/(2*aa(hs)**5) for k in (0,1)]
kn=d.knots;rows=[];st=time.time()
pts=[(kn[i]+kn[i+1])/2 for i in range(0,len(kn)-1,8) if kn[i+1]>kn[i]]
pts=[F(x) for x in pts]+[F(x) for x in (8.25,8.5)]
for t in pts:
 t=F(t).limit_denominator(2**40)
 g0,q0,r=gq(t);g5,q5=d5(t)
 rows.append([float(t),float(g5.mid()),float(q5.mid()),float(r.mid())])
 if len(rows)%40==0:print(len(rows),round(time.time()-st),rows[-1],flush=True)
json.dump({'columns':['t','g5','q5','d_axis'],'rows':rows,'ell0':float(ell.mid())},open('axis_ratio.json','w'))
print('done',len(rows),round(time.time()-st))
