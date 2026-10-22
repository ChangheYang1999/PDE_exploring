"""Exact rational frequency-one quadratic polynomial, evaluated with Arb512.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
import json,hashlib,sys,time
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[3];D=B/'research/far_residual_obstruction';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def a(q):q=Q(q);return arb(q.numerator)/q.denominator
def dy(q):m,e=q.man_exp();return Q(int(m))*Q(2)**int(e)
def box(x):
 assert x.is_finite();lo,hi=dy(x.lower()),dy(x.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(45)}
def add(x,y):return [x[i]+y[i] for i in range(len(x))]
def scale(x,y):return [q*y for q in x]
def times(x,y):
 out=[Q(0)]*(len(x)+len(y)-1)
 for i,q in enumerate(x):
  for j,r in enumerate(y):out[i+j]+=q*r
 return out
def run():
 st=time.monotonic();ctx.prec=512;ctx.threads=1
 inp=B/'data_exact/modal_v2.json';assert sha(inp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(inp.read_text());arr=raw['arrays'];assert arr['Aout']['shape']==[260,10]
 hx=lambda x:Q(float.fromhex(x));k=hx(raw['scalars_hex']['k']);t=hx(arr['knots']['hex'][-1]);bo=hx(raw['scalars_hex']['bo']);beta=2*k-1
 assert 0<k<Q(1,2) and bo>120
 pairs=[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[0,2]];assert raw['outer_jl']==pairs
 exps=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo]
 assert exps[0]==k and exps[1]==beta and all(x<beta for x in exps[2:])
 assert [(i,j) for i,x in enumerate(exps) for j,y in enumerate(exps) if x+y-1==beta]==[(0,0)]
 assert all(x+y-1<beta for i,x in enumerate(exps) for j,y in enumerate(exps) if (i,j)!=(0,0))
 assert all(x-2*n-2<beta for x in exps for n in range(1,262))
 d=[[Q(0),Q(0)] for _ in range(262)];b=[Q(0)]*262;cycle=Q(0)
 for m in range(260):
  row=[hx(arr['Aout']['hex'][m*10]),Q(m==0)];r1=hx(arr['Aout']['hex'][m*10+1]);cycle+=row[0]*[1,0,-1,0][m%4]
  for freq in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(freq)-1)//2;sg=Q(1 if freq>0 else -1,8);d[j]=add(d[j],scale(row,sg));b[j]+=sg*r1
 assert d[261]==[0,0] and b[261]==0
 aa=k+1;poly=[Q(0)]*3;denoms=[];witness=[]
 for n in range(1,262):
  m=2*n;den=m*m-aa*aa;assert den>0;denoms.append(den)
  f=scale(add(scale(d[n-1],aa-m),scale(d[n],aa+m)),Q(1,2))
  g=add(scale(d[n-1],m*(2*k+1)-aa),scale(d[n],-m*(2*k+1)-aa))
  term=scale(times(f,g),1/(2*den));poly=add(poly,term)
  if n in (1,2,3,64,260,261):witness.append({'n':n,'dprev':list(map(str,d[n-1])),'dn':list(map(str,d[n])),'F':list(map(str,f)),'term_polynomial':list(map(str,term))})
 zlo=Q('-1.198605236453734890460334164888e-20');zhi=Q('-1.198605236453734890460334164887e-20');z=a(zlo).union(a(zhi))
 norm=B/'research/modal_repair/evidence/audit_verdict.json';nv=json.loads(norm.read_text());assert nv['verdict']=='CONFIRMED'
 nscalar=B/'research/modal_repair/evidence/scalar_result.json';ns=json.loads(nscalar.read_text());zb=arb(ns['A00_correction']['ball']);assert a(zlo)<zb and zb<a(zhi)
 qval=a(poly[0])+z*(a(poly[1])+z*a(poly[2]));linear=(beta/k-1)*b[0]
 ep3=a(3*t).exp();ep5=a(5*t).exp();e0=ep3*a(linear)+ep5*qval;physical=a(-beta*t).exp()*e0
 theta=a((3-k)*t).exp()*(a(cycle)+z)/(2*arb(2).sqrt())
 files={str(p.relative_to(B)):sha(p) for p in (inp,norm,nscalar,D/'PROOF.md',Path(__file__))}
 exact={'k':str(k),'tplus':str(t),'beta':str(beta),'b0':str(b[0]),'linear':str(linear),'cycle':str(cycle),'z_bracket':list(map(str,(zlo,zhi))),'quadratic_sha256':hashlib.sha256(json.dumps(list(map(str,poly)),separators=(',',':')).encode()).hexdigest(),'quadratic_num_bits':[p.numerator.bit_length() for p in poly],'quadratic_den_bits':[p.denominator.bit_length() for p in poly]}
 out={'utc':utc(),'status':'COMPUTED_REQUIRES_OUTPUT_AUDIT','method':'Exact rational signed four-frequency projection, exact quadratic summation and Horner evaluation with Arb512','bits':512,'files':files,'exact':exact,'values':{key:box(x) for key,x in {'e0':e0,'E0':physical,'Theta_pi4':theta,'linear_term':ep3*a(linear),'quadratic_term':ep5*qval,'z':z}.items()},'counts':{'input_outer_coefficients':520,'sine_modes':261,'poisson_modes':261,'positive_denominators':len(denoms),'exponent_products':121,'homogeneous_comparisons':261*11},'witnesses':witness,'seconds':time.monotonic()-st}
 (E/'arb.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','seconds')}));print(json.dumps({k:x['display'] for k,x in out['values'].items()}))
if __name__=='__main__':run()
