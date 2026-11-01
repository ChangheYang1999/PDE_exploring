"""Independent exact Q(k) response at Q=9, reconstructed by b interpolation."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq,fmpq_poly
import sympy as sp
from generic_response_identity import Rat,quotient
import tuned_cartesian_exact as ce
ROOT=Path('research/277_period_nine_symbolic_response')
VALUES=[0,1,-1,2,-2,3,-3,4,-4,5]
ZERO=fmpq_poly([]);ONE=fmpq_poly([1])
def monic(p):return p/p[p.degree()] if p else p
def lcm(a,b):return monic(quotient(a,a.gcd(b))*b)
def pack(p):return [str(c) for c in p]
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def save(name,data):
 p=ROOT/'verification'/name;r=json.dumps(data,separators=(',',':')).encode();p.write_bytes(gzip.compress(r,mtime=0) if p.suffix=='.gz' else r+b'\n')
def log(**d):print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),**d)),flush=True)
def interp(values):
 cols=[ZERO for _ in VALUES]
 for v,y in zip(VALUES,values):
  l=ONE
  for w in VALUES:
   if w!=v:l=l*fmpq_poly([-w,1])/(v-w)
  for j,c in enumerate(l):cols[j]=cols[j]+y*c
 return cols

def main():
 start=time.monotonic();ce.K=Rat;ce.R=Rat;ce.k=Rat(fmpq_poly([0,1]));ce.MOD=None;ce.p=lambda n:1-Rat(2)*n/9
 lowpath=Path('research/267_period_nine_tuning/verification/prefix_polynomials.json.gz');low=json.loads(gzip.decompress(lowpath.read_bytes()));assert low['delta']=='2/9'
 fixed={kind:{int(n):(Rat(row['radial_exponent']),{int(m):fmpq_poly([fmpq(x) for x in coeff]) for m,coeff in row['sine_polynomials'].items()}) for n,row in low['fields'][kind].items() if int(n)<=(9 if kind=='f' else 8)} for kind in ['f','g']}
 def load(kind,value):
  return {n:ce.F(q,{key:Rat(sign*pol(value)/2) for m,pol in terms.items() for key,sign in [((0,m),1),((0,-m),-1)]}) for n,(q,terms) in fixed[kind].items()}
 def response(value,kv=None):
  ff,gg=load('f',value),load('g',value)
  kval=ce.k if kv is None else Rat(kv);n=9*kval
  freq=(2,-2) if kv is None else (0,2*kv-2);key=(2,-1) if kv is None else (0,2*kv-1)
  e=ce.sine(ce.p(n)+1,freq);U={};V={};sizes=[]
  for r in range(1,10):
   total=ce.adv(e,ff[r])
   for s in range(1,r):total=total+ce.adv(V[s],ff[r-s])+ce.adv(gg[r-s],U[s])
   U[r]=total.scale(Rat(7)/(2*(n+r-1)));U[r].check_sine()
   if kv is None:assert all(abs(a)==2 and abs(offset+2 if a==2 else offset-2)<=4*r-1 for a,offset in U[r].v)
   if r<9:V[r]=ce.poisson(U[r])
   sizes.append([len(U[r].v),len(V[r].v) if r<9 else None])
  return 2*U[9].v.get(key,Rat.zero),sizes
 actual=[];rows=[]
 for value in VALUES:
  begin=time.monotonic();a,sizes=response(value);actual.append(a)
  rows.append(dict(b=value,numerator_degree=a.n.degree(),denominator_degree=a.d.degree(),supports=sizes,elapsed_s=time.monotonic()-begin))
  save('generic_partial.json',dict(rows=rows));log(stage='generic',**rows[-1])
 D=ONE
 for a in actual:D=lcm(D,a.d)
 cols=interp([a.n*quotient(D,a.d) for a in actual]);assert len(cols)==10 and cols[-1]
 for value,a in zip(VALUES,actual):assert Rat(sum((c*value**j for j,c in enumerate(cols)),ZERO),D)==a
 G=ZERO
 for c in cols:G=G.gcd(c)
 G=monic(G)
 save('reduced_generic.json.gz',dict(numerator_by_b_degree=[pack(c) for c in cols],denominator=pack(D),coefficient_gcd=pack(G),degree_bound=9))
 log(stage='reconstructed',denominator_degree=D.degree(),numerator_degree=max(c.degree() for c in cols),gcd_degree=G.degree())
 lp=Path('../a4-lead/code/tuned/tq_cert_Q9.log');raw=lp.read_text();lines=raw.splitlines();k,b=sp.symbols('k b')
 find=lambda prefix:next(x[len(prefix):] for x in lines if x.startswith(prefix))
 factors=sp.sympify(find('denominator factors: '),locals={'k':k});D0=ONE;factorrows=[]
 for expr,mult in factors:
  p=sp.Poly(expr,k);assert p.degree()==1
  q=fmpq_poly([fmpq(str(p.nth(i))) for i in range(2)]);root=-q[0]/q[1]
  assert not (root.denominator==1 and root>=19)
  D0=D0*(monic(q)**int(mult));factorrows.append([str(root),int(mult)])
 roots=sp.sympify(find('roots of the gcd: '));G0=ONE
 for root,mult in roots.items():G0=G0*(fmpq_poly([-fmpq(str(root)),1])**int(mult))
 parsed=sp.Poly(sp.sympify(find('gcd of the b-coefficients of the numerator in QQ[k]: '),locals={'k':k}),k)
 PG=fmpq_poly([fmpq(str(parsed.nth(i))) for i in range(parsed.degree()+1)])
 assert monic(PG)==G0
 common=D0.gcd(G0);assert D==quotient(D0,common);assert G==quotient(G0,common)
 assert D0.degree()==595 and G0.degree()==509
 assert len(factors)==82 and len(roots)==83 and sum(int(m) for m in roots.values())==509
 assert min(roots)==sp.Rational(-59,18) and max(roots)==sp.Rational(43,9)
 assert [x for x in roots if x.is_integer]==[sp.Integer(1)]
 assert max(c.degree() for c in cols)+common.degree()==595
 lim=fmpq_poly([c[D.degree()] if c.degree()<=D.degree() else (_ for _ in []).throw(AssertionError('growth')) for c in cols])
 leadlim=sp.Poly(sp.sympify(find('sigma_inf = '),locals={'b':b}),b)
 assert lim==fmpq_poly([fmpq(str(leadlim.nth(j))) for j in range(10)]) and lim.degree()==9
 save('factors.json',dict(denominator_factors=factorrows,claimed_gcd_roots=[[str(r),int(m)] for r,m in roots.items()],D0_degree=D0.degree(),G0_degree=G0.degree(),common_degree=common.degree(),limit_coefficients=pack(lim),all_factor_identities=True))
 log(stage='factor_and_limit_identities',complete=True)
 small=[];direct=[]
 for kv in range(2,25):
  begin=time.monotonic();values=[]
  for value in VALUES:
   a,_=response(value,kv);assert a.n.degree()<=0 and a.d==ONE;values.append(a.n)
  row=interp(values);assert all(c.degree()<=0 for c in row)
  pol=fmpq_poly([c[0] for c in row]);assert pol.degree()==9
  if kv>=19:
   assert pol==fmpq_poly([c(kv)/D(kv) for c in cols]);direct.append(kv)
  else:small.append(dict(k=kv,coefficients=pack(pol)))
  save('small_responses.json.gz',dict(small=small,direct_generic_matches=direct));log(stage='integer_carrier',k=kv,degree=pol.degree(),elapsed_s=time.monotonic()-begin)
 for p in [lp,Path('../a4-lead/code/tuned/tq_cert.py'),Path('../a4-lead/code/tuned/tq_sym.py')]:
  (ROOT/'sources'/(p.name+'.gz')).write_bytes(gzip.compress(p.read_bytes(),mtime=0))
 sources=[]
 for name in ['period_nine_symbolic_response.py','generic_response_identity.py','tuned_cartesian_exact.py']:
  p=Path('code',name);(ROOT/'sources'/name).write_bytes(p.read_bytes());sources.append(ref(p))
 result=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,period=9,distinct_b_values=VALUES,generic_rows=rows,minimal_denominator_degree=D.degree(),minimal_numerator_degree=max(c.degree() for c in cols),minimal_coefficient_gcd=pack(G),claimed_denominator_degree=595,claimed_coefficient_gcd_degree=509,cancelled_common_degree=common.degree(),small_degrees={str(x['k']):9 for x in small},direct_generic_matches=direct,limit_coefficients=pack(lim),inputs=[ref(lowpath),ref(lp)],sources=sources,actual_elapsed_s=time.monotonic()-start,scope='Exact symbolic identity and factor/limit audit; finite decimal values are separate.')
 save('checks.json',result);log(stage='COMPLETE',elapsed_s=result['actual_elapsed_s'])
if __name__=='__main__':
 try:main()
 except Exception as exc:
  failure=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  save('FAILURE.json',failure);log(**failure);raise SystemExit(1)
