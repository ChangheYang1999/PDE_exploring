"""Independent exact Q(k) response at Q=10, reconstructed by b interpolation."""
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
ROOT=Path('research/282_period_ten_symbolic_response')
VALUES=[0,1,-1,2,-2,3,-3,4,-4,5,-5]
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
 start=time.monotonic();ce.K=Rat;ce.R=Rat;ce.k=Rat(fmpq_poly([0,1]));ce.MOD=None;ce.p=lambda n:1-Rat(1)*n/5
 lowpath=Path('research/281_period_ten_finite_algebra/verification/prefix_polynomials.json.gz');low=json.loads(gzip.decompress(lowpath.read_bytes()));assert low['delta']=='1/5'
 fixed={kind:{int(n):(Rat(row['radial_exponent']),{int(m):fmpq_poly([fmpq(x) for x in coeff]) for m,coeff in row['sine_polynomials'].items()}) for n,row in low['fields'][kind].items() if int(n)<=(10 if kind=='f' else 9)} for kind in ['f','g']}
 def load(kind,value):
  return {n:ce.F(q,{key:Rat(sign*pol(value)/2) for m,pol in terms.items() for key,sign in [((0,m),1),((0,-m),-1)]}) for n,(q,terms) in fixed[kind].items()}
 def response(value,kv=None):
  ff,gg=load('f',value),load('g',value)
  kval=ce.k if kv is None else Rat(kv);n=10*kval
  freq=(2,-2) if kv is None else (0,2*kv-2);key=(2,-1) if kv is None else (0,2*kv-1)
  e=ce.sine(ce.p(n)+1,freq);U={};V={};sizes=[]
  for r in range(1,11):
   total=ce.adv(e,ff[r])
   for s in range(1,r):total=total+ce.adv(V[s],ff[r-s])+ce.adv(gg[r-s],U[s])
   U[r]=total.scale(Rat(4)/(n+r-1));U[r].check_sine()
   if kv is None:assert all(abs(a)==2 and abs(offset+2 if a==2 else offset-2)<=4*r-1 for a,offset in U[r].v)
   if r<10:V[r]=ce.poisson(U[r])
   sizes.append([len(U[r].v),len(V[r].v) if r<10 else None])
  return 2*U[10].v.get(key,Rat.zero),sizes
 actual=[];rows=[]
 for value in VALUES:
  begin=time.monotonic();a,sizes=response(value);actual.append(a)
  rows.append(dict(b=value,numerator_degree=a.n.degree(),denominator_degree=a.d.degree(),supports=sizes,elapsed_s=time.monotonic()-begin))
  save('generic_partial.json',dict(rows=rows));log(stage='generic',**rows[-1])
 D=ONE
 for a in actual:D=lcm(D,a.d)
 cols=interp([a.n*quotient(D,a.d) for a in actual]);assert len(cols)==11 and cols[-1]
 for value,a in zip(VALUES,actual):assert Rat(sum((c*value**j for j,c in enumerate(cols)),ZERO),D)==a
 G=ZERO
 for c in cols:G=G.gcd(c)
 G=monic(G)
 save('reduced_generic.json.gz',dict(numerator_by_b_degree=[pack(c) for c in cols],denominator=pack(D),coefficient_gcd=pack(G),degree_bound=10))
 log(stage='reconstructed',denominator_degree=D.degree(),numerator_degree=max(c.degree() for c in cols),gcd_degree=G.degree())
 k=sp.Symbol('k');factor_data={}
 for label,poly in [('denominator',D),('coefficient_gcd',G)]:
  spoly=sp.Poly(sum(sp.Rational(str(c))*k**i for i,c in enumerate(poly)),k,domain=sp.QQ)
  scalar,factors=sp.factor_list(spoly);product=fmpq_poly([fmpq(str(scalar))]);frows=[]
  for factor,mult in factors:
   assert factor.degree()==1,(label,'nonlinear factor',str(factor))
   fp=fmpq_poly([fmpq(str(factor.nth(i))) for i in range(2)])
   rt=-fp[0]/fp[1];assert not (rt.denominator==1 and rt>=21),(label,'integer tail zero',str(rt))
   product=product*fp**mult;frows.append(dict(root=str(rt),multiplicity=int(mult),coefficients=pack(fp)))
  assert product==poly
  factor_data[label]=dict(scalar=str(scalar),factors=frows,degree=poly.degree())
 lim=fmpq_poly([c[D.degree()] if c.degree()<=D.degree() else (_ for _ in []).throw(AssertionError('growth')) for c in cols])
 assert lim.degree()==10
 save('factors.json',dict(factor_data=factor_data,limit_coefficients=pack(lim),all_factor_identities=True))
 log(stage='factor_and_limit_identities',complete=True)
 small=[];direct=[]
 for kv in range(2,27):
  begin=time.monotonic();values=[]
  for value in VALUES:
   a,_=response(value,kv);assert a.n.degree()<=0 and a.d==ONE;values.append(a.n)
  row=interp(values);assert all(c.degree()<=0 for c in row)
  pol=fmpq_poly([c[0] for c in row]);assert pol.degree()==10
  if kv>=21:
   assert pol==fmpq_poly([c(kv)/D(kv) for c in cols]);direct.append(kv)
  else:small.append(dict(k=kv,coefficients=pack(pol)))
  save('small_responses.json.gz',dict(small=small,direct_generic_matches=direct));log(stage='integer_carrier',k=kv,degree=pol.degree(),elapsed_s=time.monotonic()-begin)
 sources=[]
 for name in ['period_ten_symbolic_response.py','generic_response_identity.py','tuned_cartesian_exact.py']:
  p=Path('code',name);(ROOT/'sources'/name).write_bytes(p.read_bytes());sources.append(ref(p))
 result=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,period=10,distinct_b_values=VALUES,generic_rows=rows,minimal_denominator_degree=D.degree(),minimal_numerator_degree=max(c.degree() for c in cols),minimal_coefficient_gcd=pack(G),factor_data=factor_data,small_degrees={str(x['k']):10 for x in small},direct_generic_matches=direct,limit_coefficients=pack(lim),inputs=[ref(lowpath)],sources=sources,actual_elapsed_s=time.monotonic()-start,scope='Independent exact symbolic identity and factor/limit audit. Lead comparison and finite decimal values are separate.')
 save('checks.json',result);log(stage='COMPLETE',elapsed_s=result['actual_elapsed_s'])
if __name__=='__main__':
 try:main()
 except Exception as exc:
  failure=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  save('FAILURE.json',failure);log(**failure);raise SystemExit(1)
