"""Fresh exact rational extrema and Arb1536 matrix audit."""
import sys,json,hashlib,itertools,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/transition_scale/evidence';ctx.prec=1536;ctx.threads=1;t0=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ends(v):
 assert v.is_finite();out=[]
 for z in [v.lower(),v.upper()]:
  assert z.rad()==0;n,e=z.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
r=json.loads((E/'checks.json').read_text());run=json.loads((E/'local_run.json').read_text())
assert r['status']=='PASS' and run['returncode']==0 and r['code_sha256']==sha(B/'research/transition_scale/code/check_transition.py') and r['proof_sha256']==sha(B/'research/transition_scale/PROOF.md')
assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])
assert r['symbolic_identities']==8 and r['coupling_limit_zero'] and r['rational_rayleigh_checks']==320
expected=[]
for ap,mu in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)]):
 val=-1-(ap+mu)/2+F(307,100)*mu+F(13,4)*ap;expected.append({'A':str(ap),'mu':str(mu),'rate':str(val)})
assert r['source_corners']==expected and min(F(x['rate']) for x in expected)==F(r['source_minimum_exact'])==F(290443,10000)
assert len(r['collapse_examples'])==34
for row in r['collapse_examples']:
 x=F(row['x']);nu=row['nu'];assert x>0 and nu in [1,2] and F(row['rate'])==F(7,4)+F(9,50)*nu/x
assert len(r['matrix_checks'])==4
for row in r['matrix_checks']:
 a,b,d=map(F,row['entries']);val=(ar(a+d)+(ar((a-d)**2+4*b*b)).sqrt())/2;v0,v1=ends(val)
 for key in ['lambda_arb','lambda_iv']:
  o=row[key];assert F(o['lower_exact'])<=v0<=v1<=F(o['upper_exact'])
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks_sha256':sha(E/'checks.json'),'code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'fresh_matrix_containments':8,'exact_corners':4,'exact_collapse_rates':34,'arb_bits':ctx.prec,'python_flint':flint.__version__,'seconds':time.monotonic()-t0,'scope':'Output consistency audit; global symbol calculus and inverse not claimed.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
