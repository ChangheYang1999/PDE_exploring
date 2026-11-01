"""All seven final printed regressions, contrasted with matched unrounded inputs."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
from hashlib import sha256
import json,re,time,sys
sys.dont_write_bytecode=True
from flint import arb,fmpz,ctx
base=Path('research/305_final_conditional_fit_scope')
start=time.monotonic()
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def exact(q):
 q=F(q);return arb(q.numerator)/q.denominator

def unpack(v):
 m,e,r,re=v
 return arb(arb(fmpz(m))*arb(2)**e,arb(fmpz(r))*arb(2)**re)

def fit(ns,ys):
 out={};rms_values={}
 for label,xs in [('power',[arb(n).log()/arb(10).log() for n in ns]),('inverse_order',[arb(1)/n for n in ns]),('exponential',[arb(n) for n in ns])]:
  m=len(xs);sx=sum(xs);sy=sum(ys);sxx=sum(x*x for x in xs);sxy=sum(x*y for x,y in zip(xs,ys));syy=sum(y*y for y in ys)
  D=sxx-sx*sx/m;assert D>0
  c=(sxy-sx*sy/m)/D;b=(sy-c*sx)/m
  explicit=sum((y-b-c*x)**2 for x,y in zip(xs,ys))/m
  identity=(syy-sy*sy/m-(sxy-sx*sy/m)**2/D)/m
  assert explicit>0 and explicit.overlaps(identity)
  out[label]=dict(intercept=b,slope=c,rms=explicit.sqrt())
  if label=='inverse_order':out[label]['limiting_multiplier']=(b*arb(10).log()).exp()
  rms_values[label]=out[label]['rms']
 order=sorted(rms_values,key=lambda k:float(rms_values[k].mid()))
 assert all(rms_values[a]<rms_values[b] for a,b in zip(order,order[1:]))
 return out,order

sources=[];data={};overlaps=[]
ps=sorted(Path('../a4-num/notes').glob('cycle_diag_*.txt'),key=lambda p:tuple(map(int,re.findall(r'\d+',p.name))))
for p in ps:
 nums=list(map(int,re.findall(r'\d+',p.name)))
 if nums[0]<345:continue
 raw=p.read_bytes();frozen=base/'sources'/p.name
 if frozen.exists():assert frozen.read_bytes()==raw
 else:frozen.write_bytes(raw)
 sources.append(ref(frozen))
 for line in raw.decode().splitlines():
  a=line.split()
  if len(a)<8 or not a[0].isdigit():continue
  n=int(a[0])
  if not (348<=n<=438 and int(a[1])==0 and a[2]=='F'):continue
  value=F(a[6])
  if n in data:overlaps.append(dict(n=n,equal=data[n]==value))
  data[n]=value
assert list(sorted(data))==list(range(348,439,3))
assert all(v['equal'] for v in overlaps)
source=Path('research/266_later_conditional_continuations/N440/verification/drift_fit_checks.json')
full=json.loads(source.read_text());assert full['all_checks_pass']
rows={r['n']:r for r in full['rows'] if r['field']=='F' and r['n'] in data}
assert rows.keys()==data.keys()
ctx.prec=768
bins=[]
for n,v in sorted(data.items()):
 x=unpack(rows[n]['multiplier']);center=exact(v);half=exact(F(1,200000))
 ok=bool(center-half<x and x<center+half);assert ok,(n,v,x)
 bins.append(dict(n=n,printed=str(v),interval=rows[n]['multiplier_display'],within_rounding_bin=ok))
windows=[357,370,381,390,400,410,420]
runs=[]
for bits in (768,1536):
 ctx.prec=bits;wout={}
 for low in windows:
  ns=[n for n in sorted(data) if n>=low]
  for mode in ('printed','unrounded'):
   ys=[abs(exact(data[n])).log()/arb(10).log() if mode=='printed' else unpack(rows[n]['log_abs_multiplier']) for n in ns]
   fits,order=fit(ns,ys);wout[low,mode]=(fits,order,ns)
 runs.append(wout)
for key in runs[0]:
 a,order,ns=runs[0][key];b,order2,ns2=runs[1][key]
 assert order==order2 and ns==ns2
 for model in a:
  assert all(a[model][k].overlaps(b[model][k]) for k in a[model])
pat=r'window (\d+)\.\.438: power beta = (\S+) \(rms (\S+)\); 1/n: \|a_inf\| = (\S+), c1 = (\S+) \(rms (\S+)\); linear in n: slope (\S+)/order \(rms (\S+)\)'
table=base/'sources/drift_fit_348_440.txt'
rounding=[]
for line in table.read_text().splitlines():
 m=re.fullmatch(pat,line)
 if not m:continue
 low=int(m[1]);vals=m.groups()[1:]
 f=runs[1][low,'printed'][0]
 targets=[f['power']['slope'],f['power']['rms'],f['inverse_order']['limiting_multiplier'],f['inverse_order']['slope'],f['inverse_order']['rms'],f['exponential']['slope'],f['exponential']['rms']]
 for token,x in zip(vals,targets):
  center=exact(token);half=exact(F(10)**Decimal(token).as_tuple().exponent/2)
  ok=bool(center-half<x and x<center+half);assert ok,(low,token,x)
  rounding.append(dict(window_lower=low,printed=token,enclosed=x.str(40),within_rounding_bin=ok))
assert len(rounding)==49
result=[]
for low in windows:
 row=dict(window=[low,438])
 for mode in ('printed','unrounded'):
  fs,order,ns=runs[1][low,mode]
  row[mode]=dict(count=len(ns),orders=ns,strict_rms_ranking=order,fits={label:{key:value.str(45) for key,value in vals.items()} for label,vals in fs.items()})
 result.append(row)
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out=dict(at=now,all_checks_pass=True,printed_sources=sources,unrounded_source=ref(source),printed_table=ref(table),coefficient_rounding_checks=bins,duplicate_printed_rows=overlaps,printed_statistic_rounding_checks=rounding,windows=result,bits=[768,1536],all_precision_replays_overlap=True,actual_elapsed_s=time.monotonic()-start,scope='Finite matched-class-zero fits to printed and unrounded conditional-on329 inputs; no infinite-tail selection.')
(base/'verification/all_window_fit_checks.json').write_text(json.dumps(out,indent=2)+'\n')
(base/'sources/final_window_fit_replay.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(at=now,rounded_coefficients=len(bins),printed_statistics=len(rounding),fits=42,rankings=[dict(window=r['window'],printed=r['printed']['strict_rms_ranking'],unrounded=r['unrounded']['strict_rms_ranking']) for r in result],final_unrounded=result[-1]['unrounded']['fits'],elapsed=out['actual_elapsed_s']),indent=2))
