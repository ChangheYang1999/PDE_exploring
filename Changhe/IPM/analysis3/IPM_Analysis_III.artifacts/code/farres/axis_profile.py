"""Lead floating diagnostic: profile of the weighted axis trace g_axis = gamma/a_* of the residual along t.
At the midpoint of every 4th spline span: g, the fifth derivative by central differences (step 2^-18, inside the span)
and the radial transport coefficient on the axis, d_axis = ell - sum_n (-1)^n P_n (= ell0 + u_t on the axis).
Used to locate the knot-scale part of the high norm. Not a certificate."""
import os,sys,time,json
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
sys.path.insert(0,'code/farres')
from fractions import Fraction as F
from flint import arb,ctx
import profile_points as PP
ctx.prec=160
G=PP.G;aa=G.aa
d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1
def g(t,want_r=False):
 rh,drh,P,Q,Pt=PP.point(d,cache,t)
 A=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(rh)),arb(0))
 At=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(drh)),arb(0))
 r=ell-sum(((-1)**n*v for n,v in enumerate(P,1)),arb(0))
 rt=-sum(((-1)**n*v for n,v in enumerate(Pt,1)),arb(0))
 gam=r*At+(D-r-2*rt)*A
 tt=aa(t);astar=(aa(F(9,5))*tt).exp()*(1+tt.exp())**(-aa(F(53,10)))
 return (gam/astar,r) if want_r else gam/astar
hs=F(1,2**18)
def d5(t0):
 v={i:g(t0+i*hs) for i in (-3,-2,-1,1,2,3)}
 return (-v[-3]+4*v[-2]-5*v[-1]+5*v[1]-4*v[2]+v[3])/(2*aa(hs)**5)
kn=d.knots;rows=[];st=time.time()
pts=[(kn[i]+kn[i+1])/2 for i in range(0,len(kn)-1,4) if kn[i+1]>kn[i]]
pts=[F(x) for x in (-6,-5.5)]+[F(x) for x in pts]+[F(x) for x in (8.25,8.5,9,10,12)]
for t in pts:
 t=F(t).limit_denominator(2**40)
 gv,r=g(t,True);g5=d5(t)
 rows.append([float(t),float(gv.mid()),float(g5.mid()),float(r.mid())])
 if len(rows)%40==0:print(len(rows),round(time.time()-st),rows[-1],flush=True)
json.dump({'columns':['t','g','g5','d_axis'],'rows':rows,'ell0':float(ell.mid())},open('axis_profile.json','w'))
print('done',len(rows),round(time.time()-st))
