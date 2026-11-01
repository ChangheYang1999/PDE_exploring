"""Explain the four three-digit rounding failures using the saved float logs."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,math
from flint import arb,ctx
ROOT=Path('research/244_final_sensitivity350')
def load(path):
 raw=path.read_bytes();rows={}
 for line in raw.decode().splitlines():
  d=json.loads(line)
  if 'n' in d and 'log10_col_l1' in d:rows[d['n']]=d
 return rows,dict(path=str(path),sha256=sha256(raw).hexdigest())
def lse(v):
 v=[x for x in v if x is not None and x>-1e300];m=max(v)
 return m+math.log10(sum(10.0**(x-m) for x in v))
ctx.prec=768
A,ar=load(Path('../a4-num/logs/log_sin1_c3_pert329.jsonl'))
B,br=load(Path('../a4-num/logs/log_sin1_c3_from329.jsonl'))
p=ROOT/'verification/checks_N350.json';d=json.loads(p.read_text());tp=ROOT/'sources/compare_pert_N350.txt';table={}
for line in tp.read_text().splitlines():
 bits=line.split()
 if bits and bits[0].isdigit():table[int(bits[0])]=bits
labels=['dM','dN','dR','maximum_column_difference'];rounding=[];maximum_error=arb(0);compared=0
for row in d['rows']:
 n=row['n'];a=A[n];b=B[n];ma,mb=lse(a['log10_col_l1']),lse(b['log10_col_l1']);na,nb=lse(a['log10_gcol_l1']),lse(b['log10_gcol_l1'])
 vals=[ma-mb,na-nb,(na-ma)-(nb-mb),max(abs(x-y) for x,y in zip(a['log10_col_l1'],b['log10_col_l1']) if x>-1e300 and y>-1e300)]
 for label,x,printed in zip(labels,vals,table[n][2:6]):
  formatted=format(x,'.2e');assert formatted.lstrip('+')==printed.lstrip('+'),(n,label,formatted,printed);compared+=1
  exact=arb(row[label+'_display']);error=abs(exact-arb(x));maximum_error=maximum_error.max(error)
  exponent=int(printed.split('e')[1]);tolerance=arb('0.005')*arb(10)**exponent
  if not exact.overlaps(arb(printed,tolerance)):
   rounding.append(dict(n=n,metric=label,printed=printed,directed_value=row[label+'_display'],binary_float=x,float_error=error.str(40,radius=True)))
assert compared==84 and len(rounding)==4
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,float_table_comparisons=compared,three_digit_rounding_failures=rounding,maximum_absolute_float_error=maximum_error.str(40,radius=True),sources=[ar,br,dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())],scope='All printed values reproduce the saved binary-float logs. Four fail the exact three-digit rounding test against directed coefficient norms; finite qualitative attenuation is unaffected.')
(ROOT/'verification/rounding_explanation.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/sensitivity_rounding350.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(out),flush=True)
