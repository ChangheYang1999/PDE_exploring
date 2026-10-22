"""Fresh rational source-box extrema and Arb1536 audit of saved derivative constants."""
import json,hashlib,sys,itertools,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/source_matching/evidence';ctx.prec=1536;ctx.threads=1;t0=time.monotonic()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ends(z):
 assert z.is_finite();out=[]
 for t in [z.lower(),z.upper()]:
  assert t.rad()==0;n,e=t.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def contains(o,z):
 lo,hi=F(o['lower_exact']),F(o['upper_exact']);a,b=ends(z);assert lo<=a<=b<=hi
r=json.loads((E/'checks.json').read_text());run=json.loads((E/'local_run.json').read_text())
assert r['status']=='PASS' and run['returncode']==0 and r['code_sha256']==sha(B/'research/source_matching/code/check_source.py') and r['proof_sha256']==sha(B/'research/source_matching/PROOF.md')
assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])
assert r['parameter_box']=={'A':['10','51/5'],'mu':['99/100','101/100'],'g':['29','30']}
for row in r['margins']:
 sigma=F(row['sigma']);actual=[]
 for A,mu,g in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)],[F(29),F(30)]):
  base=1+(A+mu)/2;y=base-sigma*mu;x=base+g-sigma*A
  actual.append(dict(A=str(A),mu=str(mu),g=str(g),ky=str(y),kx=str(x)))
 assert actual==row['corners'];ky=min(F(a['ky']) for a in actual);kx=min(F(a['kx']) for a in actual);assert row['ky']==str(ky) and row['kx']==str(kx) and F(row['inverse_upper_exact'])==1/min(ky,kx)
assert r['window']=={'lower':'3','upper_x':'2373/680','upper_y':'1301/202'} and r['rate_inequalities']==400 and r['symbolic_identities']==12
# Regenerate exact alternating-series enclosure and independently locate pi inside it.
def at(q,n):
 sm=F();term=q
 for j in range(n):sm+=(-1)**j*term/(2*j+1);term*=q*q
 err=(-1)**n*term/(2*n+1);return min(sm,sm+err),max(sm,sm+err)
a,b=at(F(1,5),256);d,e=at(F(1,239),80);pil,pih=16*a-4*e,16*b-4*d
assert r['machin_pi']=={'lower_exact':str(pil),'upper_exact':str(pih),'terms':[256,80]}
piends=ends(arb.pi());assert pil<piends[0]<=piends[1]<pih
# Tangent route to the identity is checked in exact rationals as well.
tan2=2*F(1,5)/(1-F(1,5)**2);tan4=2*tan2/(1-tan2**2);assert tan2==F(5,12) and tan4==F(120,119) and (tan4-F(1,239))/(1+tan4*F(1,239))==1
pubs=[]
for row,export in zip(r['margins'],r['derivative_exports']):
 sig=F(row['sigma']);inv=F(row['inverse_upper_exact']);z=ar(inv)*(1/(8*arb.pi()*ar(sig-1)*ar(sig-2))).sqrt();assert export['sigma']==row['sigma']
 for key in ['source_derivative_bound_arb','source_derivative_bound_iv_machin']:
  contains(export[key],z);assert 0<F(export[key]['lower_exact'])<=F(export[key]['upper_exact'])<F(export['public_strict_upper'])
 pubs.append(export['public_strict_upper'])
assert pubs==['38899/1000000','48647/1000000']
o=r['outside_window_positive_rate'];assert o['rate_exact']==str(F(7,2)*F(51,5)*F(16384,16385)-1-(F(51,5)+F(99,100))/2-29) and F(o['rate_exact'])>0
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks_sha256':sha(E/'checks.json'),'code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'fresh_box_corners':16,'fresh_derivative_containments':4,'public_exports_checked':2,'machin_rational_and_fresh_pi':True,'arb_bits':ctx.prec,'python_flint':flint.__version__,'seconds':time.monotonic()-t0,'scope':'Fresh higher precision output audit, not a third independent mathematical proof.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
