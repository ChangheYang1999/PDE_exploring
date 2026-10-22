"""Fresh Arb768 audit of exact coefficients, saved intervals and source binding."""
import json,hashlib,sys,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/trial_axis_log/evidence';ctx.prec=768;ctx.threads=1;t0=time.monotonic()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ends(z):
 assert z.is_finite();out=[]
 for a in [z.lower(),z.upper()]:
  assert a.rad()==0;n,e=a.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def saved(o):
 l,h=F(o['lower_exact']),F(o['upper_exact']);assert l<=h;return l,h
def contains(o,z):
 l,h=saved(o);a,b=ends(z);assert l<=a<=b<=h
r=json.loads((E/'checks.json').read_text());run=json.loads((E/'local_run.json').read_text());data=json.loads((B/'data_exact/modal_v2.json').read_text())
assert r['status']=='PASS' and run['returncode']==0
assert r['code_sha256']==sha(B/'research/trial_axis_log/code/check_log.py')
assert r['proof_sha256']==sha(B/'research/trial_axis_log/PROOF.md')
assert r['input_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
assert r['original_npz_sha256']==sha(B/'research/modal_exactification/evidence/trial_v2_h0.008.npz')=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])
d=[F.from_float(float.fromhex(h)) for h in data['arrays']['D']['hex'][::7]];assert len(d)==260
h7=(d[2]+d[3]-d[4]-d[5])/8;b=sum((1-2*m*m)*x for m,x in enumerate(d));assert h7*b!=0
assert r['exact_raw_coefficients']=={'h7':str(h7),'b2raw':str(b),'d2_to_d5':[str(d[m]) for m in range(2,6)]}
k=F.from_float(float.fromhex(data['scalars_hex']['k']));A=2/k-1;p=6+2/A;ta=F.from_float(float.fromhex(data['arrays']['knots']['hex'][0]));bi=F.from_float(float.fromhex(data['scalars_hex']['bi']))
assert 6<p<7 and bi>49 and r['parameters']==dict(k=str(k),A=str(A),p=str(p),ta=str(ta),bi=str(bi))
R=ar(ta).exp();H=ar(h7)/R**2;B2=ar(b)/R**2
zs={'H7':H,'b2':B2,'w_x5log':3*H,'Qf_x4log':-30*H/ar(A),'Qtotal_x6log':ar(-3*h7*b*(9*A-2)/(2*A**3))/R**4}
exports={'H7':[F(-1423,10**12),F(-1421,10**12)],'b2':[F(-237,20000),F(-1183,100000)],'w_x5log':[F(-4267,10**12),F(-853,200000000000)],'Qf_x4log':[F(21,5000000000),F(2101,500000000000)],'Qtotal_x6log':[F(-1079,500000000000000),F(-539,250000000000000)]}
for key,z in zs.items():
 row=r['coefficients'][key];lo,hi=map(F,row['common_strict_bracket']);assert [lo,hi]==exports[key] and lo*hi>0
 for m in ['arb','iv']:
  contains(row[m],z);l,h=saved(row[m]);assert lo<l<=h<hi
# Rebuild full exact angular arrays, distinct from the saved output representation.
Hraw={};Fr={}
for m,x in enumerate(d):
 for n in (1-2*m,1+2*m,3-2*m,3+2*m):Hraw[abs(n)]=Hraw.get(abs(n),F())+(1 if n>0 else -1)*x/8
Hraw={n:h for n,h in Hraw.items() if h}
for n,h in Hraw.items():
 for l,c in [(n+1,5-n),(n-1,5+n)]:
  if l:Fr[l]=Fr.get(l,F())+c*h/2
Fr={n:f for n,f in Fr.items() if f};modes=json.loads((E/'exact_modes.json').read_text())
assert modes=={'density5_raw':{str(n):str(h) for n,h in sorted(Hraw.items())},'forcing4_raw':{str(n):str(f) for n,f in sorted(Fr.items())}}
assert Hraw[7]==h7 and Fr[6]==6*h7 and sum(F(n*(13-n*n),6)*h for n,h in Hraw.items())==b
assert r['checks']=={'all_D_binary_layout':1820,'two_hex_parsers':1820,'density_positive_modes':261,'forcing_positive_modes':261,'H7_formula':1,'b2_formulas':1,'symbolic_log_identities':12,'independent_enclosures':5}
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks_sha256':sha(E/'checks.json'),'exact_modes_sha256':sha(E/'exact_modes.json'),'code_sha256':sha(__file__),'proof_sha256':r['proof_sha256'],'check_code_sha256':r['code_sha256'],'fresh_containments':10,'strict_nonzero_exports':5,'exact_angular_arrays':2,'arb_bits':ctx.prec,'python_flint':flint.__version__,'seconds':time.monotonic()-t0,'scope':'Fresh higher precision audit of both saved enclosures and exact coefficients, not a third independent mathematical implementation.'}
(E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o))
