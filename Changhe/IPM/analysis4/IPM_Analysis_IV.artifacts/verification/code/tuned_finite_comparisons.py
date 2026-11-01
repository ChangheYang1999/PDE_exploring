"""Compare source finite claims with rigorous continuum and point intervals."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=512;start=time.monotonic()
root=Path('research/128_tuned_finite_audit')
choices=sorted(p for p in (root/'verification').iterdir() if p.is_dir() and (p/'checks.json').exists());out=choices[-1]
data=json.loads((out/'checks.json').read_text());coeff=json.loads((out/'coefficient_checks.json').read_text())
rows=[];maxrelative=arb(0);maxpoint=arb(0);maxwidth=arb(0)
for row in data['rows']:
 tests=[]
 for kind,key,ks in [('residual','residual_bounds',range(3)),('next_increment','next_increment_bounds',range(2))]:
  for k in ks:
   bound=row[key][str(k)];lo=arb(bound['lower']);hi=arb(bound['upper']);sourcekey=('resid_k' if kind=='residual' else 'tail_k')+str(k);value=arb(str(row['reported'][sourcekey]));assert value>0
   dlo=lo/value-1;dhi=hi/value-1;error=abs(dlo).max(abs(dhi));maxrelative=maxrelative.max(error)
   width=(hi-lo)/lo;maxwidth=maxwidth.max(width)
   tests.append(dict(quantity=sourcekey,reported_decimal=str(row['reported'][sourcekey]),relative_supremum_minus_report_lower=dlo.str(35,radius=True),relative_supremum_minus_report_upper=dhi.str(35,radius=True),rigorous_maximum_relative_error=error.str(35,radius=True)))
 diffs=[]
 for actual,reported in zip(row['partial_sums'],row['reported']['S_N_at_angles']):
  error=abs(arb(actual)-arb(str(reported)));maxpoint=maxpoint.max(error);diffs.append(error.str(35,radius=True))
 rows.append(dict(N=row['N'],R=row['R'],supremum_comparisons=tests,partial_sum_absolute_errors=diffs))
# These are tolerances on the printed finite observations, not an infinite tail.
print(json.dumps(dict(maximum_relative_error=maxrelative.str(40,radius=True),maximum_point_error=maxpoint.str(40,radius=True))),flush=True)
assert maxpoint<arb('1e-14')
monotonic=[]
for radius in ['1/4','1/2','1','2','4']:
 rrows=[r for r in data['rows'] if r['R']==radius]
 for kind in ['residual_bounds','next_increment_bounds']:
  for k in range(3 if kind=='residual_bounds' else 2):
   for first,last in zip(rrows,rrows[1:]):
    assert arb(last[kind][str(k)]['upper'])<arb(first[kind][str(k)]['lower'])
    monotonic.append(dict(R=radius,kind=kind,derivative_order=k,from_N=first['N'],to_N=last['N']))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,zero_point_two_percent_supremum_tolerance_certified=bool(maxrelative<arb('0.002')),rows=rows,strictly_decreasing_finite_pairs=monotonic,maximum_relative_supremum_error=maxrelative.str(40,radius=True),maximum_relative_supremum_interval_width=maxwidth.str(40,radius=True),maximum_absolute_partial_sum_error=maxpoint.str(40,radius=True),actual_elapsed_s=time.monotonic()-start)
(out/'source_comparisons.json').write_text(json.dumps(result,indent=2)+'\n');(out/'tuned_finite_comparisons.py.txt').write_bytes(Path('code/tuned_finite_comparisons.py').read_bytes())
files={p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file() and p.name!='MANIFEST.json'};(out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','strictly_decreasing_finite_pairs']}),flush=True)
