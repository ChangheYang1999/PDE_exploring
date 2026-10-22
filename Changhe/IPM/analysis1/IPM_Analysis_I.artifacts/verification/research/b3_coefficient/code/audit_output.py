"""Fresh Arb768 midpoint sums and exact saved-output arithmetic for topic59."""
import json,hashlib,sys,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/b3_coefficient/evidence';ctx.prec=768;ctx.threads=1;t0=time.monotonic()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ends(z):
 assert z.is_finite()
 out=[]
 for a in [z.lower(),z.upper()]:
  assert a.rad()==0;n,e=a.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def saved(o):
 l,h=F(o['lower_exact']),F(o['upper_exact']);assert l<=h;return l,h
def contains(o,z):
 l,h=saved(o);a,b=ends(z);assert l<=a<=b<=h
r=json.loads((E/'checks.json').read_text());run=json.loads((E/'local_run.json').read_text())
assert r['status']=='PASS' and run['returncode']==0
assert r['source_sha256']==sha(B/'research/b3_coefficient/code/check_b3.py')=='0bd807cdd7745d3e0a02a52ab6981ac1f9be8784ccbab0f9892a7ff575552276'
assert r['proof_sha256']==sha(B/'research/b3_coefficient/PROOF.md')=='e0bda870f04cd5c438871165eef3bc6849acd2c4e3627d6674c4b2cdbfd55e94'
assert r['input_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])
rr=json.loads((B/'data_exact/modal_v2.json').read_text());k=F.from_float(float.fromhex(rr['scalars_hex']['k']));A=2/k-1;p=6+2/A
assert r['parameters']=={'k_exact':str(k),'A_exact':str(A),'p_exact':str(p)} and 6<p<7
q=r['quadrature'];N=q['cells'];power=q['substitution_power'];assert N==8192 and power==16
beta=power*(8-p)-1;assert beta>2 and F(q['beta_exact'])==beta
sm=arb(0)
for j in range(N):sm+=(ar(F(2*j+1,2*N))**ar(beta))/N
contains(q['midpoint_sum'],sm)
err=beta*(beta-1)/(24*N*N);assert F(q['error_upper_exact'])>=err
sl,sh=saved(q['midpoint_sum']);ql,qh=saved(q['enclosure']);assert ql<=sl and qh>=sh+F(q['error_upper_exact'])
exact=1/(beta+1);assert F(q['exact_integral'])==exact and ql<=exact<=qh
for row in r['cutoff_constants']:
 d=F(row['delta_exact']);z=ar(d)**ar(8-p)/ar(8-p)
 contains(row['arb'],z);contains(row['iv'],z)
 # Check both saved methods are strictly below the exported rational.
 pub=F(row['public_strict_upper_exact']);assert max(saved(row['arb'])[1],saved(row['iv'])[1])<pub
assert [F(row['public_strict_upper_exact']) for row in r['cutoff_constants']]==[F(159,1000),F(5547,10000)]
b=-sum(F(v)/(j-p) for j,v in {2:1,4:-2,6:3,8:5}.items());ex=r['illustrative_finite_part'];assert F(ex['exact_B3'])==b
for method in ['arb','iv']:assert saved(ex[method])[0]<=b<=saved(ex[method])[1]
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks_sha256':sha(E/'checks.json'),'code_sha256':sha(__file__),'proof_sha256':r['proof_sha256'],'fresh_midpoint_terms':N,'fresh_cutoff_containments':4,'exact_B3_containments':2,'public_exports_checked':2,'arb_bits':ctx.prec,'python_flint':flint.__version__,'seconds':time.monotonic()-t0,'scope':'Exact binding and fresh higher-precision audit of saved arithmetic. Not a third independent mathematical method or an evaluation of the trial B3.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
