"""Directed rounding and endpoint-window audit of the final numerical summary."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction as F
import gzip,json,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx,fmpq
from stream_precision_audit import dyadic
start=time.monotonic()
base=Path('research/307_final_numerical_summary')
def ref(p):
 p=Path(p);return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def q(x):return arb(fmpq(str(F(x))))
def txt(x):return x.str(55,radius=True)
prior245=Path('research/245_extremal_necessary_radii/verification/checks.json')
prior228=Path('research/228_single_eleven_structure/verification/checks.json')
d245=json.loads(prior245.read_text());d228=json.loads(prior228.read_text())
rows=[]
for delta,M,claimed,safe,old in [(F(4,5),7,'0.0903','0.0902973',d245['rows'][0]['necessary_radius']),
 (F(4,7),9,'0.2366','0.2365977',d245['rows'][1]['necessary_radius']),
 (F(4,9),11,'0.5075','0.507476',d228['necessary_radius'])]:
 vals=[]
 for bits in (512,1024):
  ctx.prec=bits; a=F(2)/(M+1-delta);b=M*a;d=delta/(1-delta)
  H=q(4*d)*(q(a)*q(a).gamma()*q(b).gamma()/q(a+b).gamma())**(1/q(a))
  T=H**(-1/q(delta));vals.append(T)
 assert vals[0].overlaps(vals[1]) and vals[1].overlaps(arb(old))
 assert q(safe)<vals[1]<q(claimed)
 rows.append(dict(delta=str(delta),M=M,claimed_lower=claimed,safe_lower=safe,threshold=txt(vals[1]),claimed_exceeds_threshold=True,excess=txt(q(claimed)-vals[1])))
prior=Path('research/293_sin7_order500/verification/sin7/checks.json.gz')
d=json.loads(gzip.decompress(prior.read_bytes()));assert d['all_checks_pass']
ctx.prec=2048
norms={r['n']:arb(dyadic(r['f_norm'][0],r['f_norm'][1]),dyadic(r['f_norm'][2],r['f_norm'][3])) for r in d['norms'] if r['n'] in (100,300,500)}
assert all(v>0 for v in norms.values())
endpoints=[]
for L,U,printed in [(100,300,'0.5734'),(300,500,'0.5739'),(100,500,'0.5736')]:
 slope=(norms[U].log()-norms[L].log())/(U-L);A=slope.exp();R=(slope*q(F(5,4))).exp()
 assert q(printed)-q(F(1,20000))<A<q(printed)+q(F(1,20000))
 endpoints.append(dict(L=L,U=U,A=txt(A),radius_diagnostic=txt(R),printed_base=printed,rounding_pass=True))
refs=[]
for name in ('NUM_REPORT.md','FARFIELD_NUMERICAL_EXPERIMENTS.md'):
 p=Path('../a4-num')/name;s=p.read_text();lines=s.splitlines()
 selected=[dict(line=i+1,text=line) for i,line in enumerate(lines) if any(x in line for x in ('0.0903','0.2366','0.5075','0.5739','no factorial growth','i.e. ||f_n||'))]
 excerpt=base/'sources'/(name+'.excerpts.json')
 excerpt.write_text(json.dumps(dict(source_path=str(p),source_sha256=sha256(p.read_bytes()).hexdigest(),lines=selected),indent=2)+'\n')
 refs.append(ref(excerpt))
result=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,source=[ref(prior245),ref(prior228),ref(prior)],rounding_rows=rows,endpoints=endpoints,excerpts=refs,scope='Refutes downward-rounding justification for the three displayed lower bounds; does not disprove stronger full-series bounds. Confirms all three distinct finite endpoint windows. No asymptotic law is inferred.',actual_elapsed_s=time.monotonic()-start)
out=base/'verification/checks.json';out.write_text(json.dumps(result,indent=2)+'\n')
(base/'sources/final_numerical_summary_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result,indent=2))
