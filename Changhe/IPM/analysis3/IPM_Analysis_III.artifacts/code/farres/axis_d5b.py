"""Lead floating cross-check of V186: fifth derivative of g_axis = gamma/a_* at a given t (default use: t=1001/125, the second point of V186) by central differences.
gamma = d A' + (D - d - 2 d') A from the original data (point evaluation reused from profile_points.py).
Not a certificate: finite differences, no error bound."""
import os,sys,time,json
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
sys.path.insert(0,'code/farres')
from fractions import Fraction as F
from flint import arb,ctx
import profile_points as PP
ctx.prec=160
G=PP.G;aa=G.aa
d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1
def g(t):
 rh,drh,P,Q,Pt=PP.point(d,cache,t)
 A=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(rh)),arb(0))
 At=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(drh)),arb(0))
 r=ell-sum(((-1)**n*v for n,v in enumerate(P,1)),arb(0))
 rt=-sum(((-1)**n*v for n,v in enumerate(Pt,1)),arb(0))
 gam=r*At+(D-r-2*rt)*A
 tt=aa(t);astar=(aa(F(9,5))*tt).exp()*(1+tt.exp())**(-aa(F(53,10)))
 return gam/astar
t0=F(sys.argv[1]);out={}
import bisect;i0=bisect.bisect_right(d.knots,t0)-1;print("knots",[float(x) for x in d.knots[i0-3:i0+5]],"tp",float(d.tp))
for hs in (F(1,2**18),F(1,2**20)):
 st=time.time();v={i:g(t0+i*hs) for i in (-3,-2,-1,1,2,3)}
 d5=(-v[-3]+4*v[-2]-5*v[-1]+5*v[1]-4*v[2]+v[3])/(2*aa(hs)**5)
 out[str(hs)]=d5.str(12);print(hs,d5.str(12),'sec',round(time.time()-st,1),flush=True)
C5=(aa(F(11,2)).gamma()*aa(F(3,4)).gamma()/(2*arb.pi()*aa(F(25,4)).gamma())).sqrt()
print('C5',C5.str(15),'g0',g(t0).str(12))
print(json.dumps(out))
