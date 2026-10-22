"""Exact nonzero exterior Green moment caused by N7, with independent moment summation."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,hashlib,zipfile,math
import sympy as sp
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n7_center';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();v=json.loads((E/'exact_inputs.json').read_text());old=v['data']['original'];new=v['data']['n7'];b=Q(new['bi']);A=526;l=522
unchanged=[]
with zipfile.ZipFile(old['path']) as zo,zipfile.ZipFile(new['path']) as zn:
 assert set(zo.namelist())==set(zn.namelist())
 for name in sorted(zo.namelist()):
  if name in ['D.npy','Ei.npy']:continue
  assert zo.read(name)==zn.read(name),name;unchanged.append(name)
ds=[Q(x) for x in old['D'][259][:4]];summands=[];S=Q(0);fresh=Q(0)
for j,d in enumerate(ds,1):
 g=(b-2*j)**7/((A+2*j)*(A+b)**7);S+=d*g
 direct=Q(1,A+2*j)
 for i in range(7):
  moment=(-1)**i*Q(math.factorial(i))/(A+b)**(i+1)
  direct-=Q(2*j-b)**i/Q(math.factorial(i))*moment
 assert direct==g;fresh+=d*direct;summands.append(str(d*g))
assert S==fresh and S!=0
ids={};aa,bb,z,t=sp.symbols('A b z t',positive=True);j=sp.symbols('j',positive=True,integer=True)
def chk(name,e):assert sp.simplify(e)==0,(name,e);ids[name]='0'
chk('geometric_remainder',1/(aa+2*j)-sum((bb-2*j)**i/(aa+bb)**(i+1) for i in range(7))-(bb-2*j)**7/((aa+2*j)*(aa+bb)**7))
for nu in range(7):chk('matching_'+str(nu),sp.diff(sp.exp(2*j*t)-sp.exp(bb*t)*sum((2*j-bb)**i*t**i/sp.factorial(i) for i in range(7)),t,nu).subs(t,0))
r,ll=sp.symbols('r l',positive=True);f=sp.Function('f')(r);I=sp.Function('I')(r);J=sp.Function('J')(r);psi=(r**(-ll)*I+r**ll*J)/(2*ll)
expr=-sp.diff(psi,r,2)-sp.diff(psi,r)/r+ll**2*psi/r**2
expr=expr.subs(sp.diff(I,r,2),sp.diff(r**(ll+1)*f,r)).subs(sp.diff(J,r,2),sp.diff(-r**(1-ll)*f,r)).subs(sp.diff(I,r),r**(ll+1)*f).subs(sp.diff(J,r),-r**(1-ll)*f)
chk('canonical_Green_sign',expr-f)
chk('moment_integration_by_parts_factor',-(ll+1+(ll-1))/2+ll)
paths=[Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'addendum_first.json',E/'exact_inputs.json',E/'checks.json',E/'output_audit.json']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_N7_NONZERO_EXTERIOR_CHANGE','counts':{'unchanged_NPY_members':len(unchanged),'independent_exact_moment_equalities':4,'symbolic_identities':len(ids)},'unchanged_members':unchanged,'exact':{'S':str(S),'S_sign':1 if S>0 else -1,'summands':summands,'stream_coefficient_prefactor_S_over16':str(S/16),'angular_frequency':522,'inner_radius_power':526},'scope':'Nonzero exterior frequency522 stream change under exact C6 rejoining; unaffected by mode0 normalization. No assertion about numerical significance or residual norms.','files':{str(p.relative_to(B)):sha(p) for p in paths},'identities':ids}
(E/'remote_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['files','identities']},indent=2))
