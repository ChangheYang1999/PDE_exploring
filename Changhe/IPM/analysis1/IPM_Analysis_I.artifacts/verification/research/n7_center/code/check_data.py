"""Exact JSON center algebra and independent Arb/iv enclosures, no producer imports."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sympy as sp
from flint import arb,fmpq,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n7_center';E=D/'evidence';ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aq(q):q=Q(q);return arb(fmpq(q.numerator,q.denominator))
def iq(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return Q(int(m))*Q(2)**int(e)
def ends(z):
 if isinstance(z,arb):return ep(z.lower()),ep(z.upper())
 def f(v):sg,m,e,bc=v;return (-1 if sg else 1)*Q(int(m))*Q(2)**int(e)
 return tuple(f(v) for v in z._mpi_)
def pack(lo,hi):return {'lower_exact':str(lo),'upper_exact':str(hi),'mid_approx':float((lo+hi)/2)}
def main():
 start=time.monotonic();data=json.loads((E/'exact_inputs.json').read_text());o,n=data['data']['original'],data['data']['n7'];old=[[Q(x) for x in row] for row in o['D']];new=[[Q(x) for x in row] for row in n['D']];M=len(new);assert M==260 and n['D_shape']==[260,7]
 mask=[];comp=0;changed=0
 for m in range(M):
  for j in range(1,8):
   if j<=4 and m>j:
    assert new[m][j-1]==0 and old[m][j-1]!=0;mask.append((m,j));changed+=1
   else:assert new[m][j-1]==old[m][j-1];comp+=1
 assert len(mask)==1026 and comp==794 and changed==1026
 b,k,tmin=map(Q,[n['bi'],n['k'],n['tmin']]);assert b>49 and 0<k<1
 assert b==Q(o['bi']) and k==Q(o['k']) and tmin==Q(o['tmin'])
 h7=(new[2][0]+new[3][0]-new[4][0]-new[5][0])/8;assert h7==0
 mstar=max(m for m in range(6,M) if new[m][4]);L=2*mstar+3;ds=new[mstar][4];assert mstar==259 and L==521 and ds>0
 maxd=max(abs(row[4]) for row in new[6:]);assert maxd<Q('6.9e-11')
 removed=max(abs(old[m][j-1]) for m,j in mask)
 ids={};x,y,rr,th,dd,ll,aa=sp.symbols('x y r theta d l a',real=True,positive=True)
 def check(name,v):z=sp.trigsimp(sp.expand_trig(v));assert sp.simplify(z)==0,(name,z);ids[name]='0'
 check('cubic_angular',sp.cos(th)**2*sp.sin(th)-(sp.sin(th)+sp.sin(3*th))/4)
 # General angular identity from the polar first-order differential operator.
 f=rr**dd*sp.sin(ll*th);polar=sp.cos(2*th)*rr*sp.diff(f,rr)-sp.sin(2*th)*sp.diff(f,th)
 check('anisotropic_homogeneous_action',polar-rr**dd*((dd-ll)*sp.sin((ll+2)*th)+(dd+ll)*sp.sin((ll-2)*th))/2)
 g=rr**aa*sp.sin(ll*th);check('polar_laplacian',sp.diff(g,rr,2)+sp.diff(g,rr)/rr+sp.diff(g,th,2)/rr**2-(aa**2-ll**2)*rr**(aa-2)*sp.sin(ll*th))
 gr=rr**ll*sp.log(rr)*sp.sin(ll*th)/(2*ll);check('resonant_laplacian',sp.diff(gr,rr,2)+sp.diff(gr,rr)/rr+sp.diff(gr,th,2)/rr**2-rr**(ll-2)*sp.sin(ll*th))
 sig,cl=sp.symbols('sig cl');ps=sig*x*y;check('canonical_U1',-sp.diff(ps,y)+sig*x);check('canonical_U2',sp.diff(ps,x)-sig*y)
 check('lambda_difference',(cl-(3*cl-1))-(cl+(3*cl-1))-(2-6*cl))
 tau=sp.symbols('tau');bs=sp.symbols('b');joins=0
 for nu in range(7):
  for i in range(7):
   target=sp.factorial(nu)/sp.factorial(nu-i)*bs**(nu-i) if i<=nu else 0
   check('join_'+str(nu)+'_'+str(i),sp.diff(sp.exp(bs*tau)*tau**i,tau,nu).subs(tau,0)-target);joins+=1
 det=math.prod(math.factorial(i) for i in range(7));assert det==24883200
 coeff=Q(2)-6/k;pref=coeff*(13-L)*ds/32;assert pref>0
 margin=Q(13)-(Q(645,100)+Q(307,100)-1);assert margin==Q(112,25)
 values={}
 for name,cv,exp in [('arb512',aq,lambda z:z.exp()),('iv180',iq,iv.exp)]:
  scale=exp(-10*cv(tmin));values[name]={'rminus':ends(exp(cv(tmin))),'rminus_inverse10':ends(scale),'factor_top':ends(cv(ds)*scale),'density_top':ends(cv(ds/8)*scale),'residual_top':ends(cv(pref)*scale),'max_scaled_D5':ends(cv(maxd))}
 bounds={q:pack(min(v[q][0] for v in values.values()),max(v[q][1] for v in values.values())) for q in next(iter(values.values()))}
 assert Q(bounds['residual_top']['lower_exact'])>1
 paths=[Path(__file__),D/'PROOF.md',E/'proof_first.json',E/'exact_inputs.json']+list((E/'source').glob('*.py'))
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_N7_EXACT_CENTER','counts':{'mask_zeros':len(mask),'unchanged_complement':comp,'changed_coefficients':changed,'symbolic_identities':len(ids),'join_entries':joins,'primary_engine_enclosures':12},'exact':{'M':M,'mstar':mstar,'L':L,'Dstar':str(ds),'bi':str(b),'k':str(k),'tmin':str(tmin),'largest_removed_scaled_D':str(removed),'largest_remaining_scaled_D5':str(maxd),'h7':str(h7),'join_determinant':str(det),'residual_prefactor':str(pref),'homogeneity_margin':str(margin)},'bounds':bounds,'identities':ids,'scope':'Local density unconditional; canonical residual conditional on exact normalization. No numerical bound for a residual norm.','files':{str(p.relative_to(B)):sha(p) for p in paths},'seconds':time.monotonic()-start}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['identities','files']},indent=2))
if __name__=='__main__':main()
