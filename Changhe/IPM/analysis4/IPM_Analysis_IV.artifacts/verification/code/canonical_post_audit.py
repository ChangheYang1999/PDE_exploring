"""Audit plain norms, the quarter inequality, and rounded new source tables."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,re,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=512
start=time.monotonic()
candidates=[]
for p in Path('research/64_log_precision_updates/verification').glob('log_sin1_c3_p512_N*/checks.json'):
 d=json.loads(p.read_text())
 if d['maximum_order']>320:candidates.append((d['maximum_order'],str(p),p,d))
_,_,source,data=max(candidates)
N=data['maximum_order'];tables={field:{r['n']:r for r in data['fields'][field]['all_order_factorial_comparisons']} for field in ['f','g']}
# The factorial comparison table starts at n=7. Recompute its missing
# low prefix from the independent exact Cartesian implementation.
from logarithmic_verify import run as exact_run
from gmpy2 import mpq as Q
from flint import fmpq
prefix=exact_run(Q(3),{1:Q(1)},6)
for row in prefix['rows']:
 for field,key in [('f','density'),('g','stream')]:
  norm=sum((abs(Q(v)) for modes in row[key].values() for v in modes.values()),Q(0))
  tables[field][row['n']]={'log10_plain_norm':(arb(fmpq(str(norm))).log()/arb(10).log()).str(45,radius=True)}
text=lambda x:x.str(35,radius=True)
rows=[];exceeds=[];unresolved=[];maximum=arb(0);maximum_n=None
for n in range(1,N+1):
 lf=arb(tables['f'][n]['log10_plain_norm']);lg=arb(tables['g'][n]['log10_plain_norm']);ratio=(arb(10).log()*(lg-lf)).exp()
 relation='below' if ratio<arb(1)/4 else 'above' if ratio>arb(1)/4 else 'unresolved'
 if relation=='above':exceeds.append(n)
 if relation=='unresolved':unresolved.append(n)
 if ratio>maximum:maximum=ratio;maximum_n=n
 rows.append(dict(n=n,log10_M=text(lf),log10_N=text(lg),log10_N_over_M=text(lg-lf),N_over_M=text(ratio),quarter_relation=relation))
notes=Path('../a4-num/NOTES_FOR_TEAM.md').read_text();excerpt=notes.split('## 2026-10-31T09:10Z',1)[1].split('\n## ',1)[0]
printed=[]
for line in excerpt.splitlines():
 match=re.match(r'^\s*(3\d\d)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+None\s*$',line)
 if not match:continue
 n=int(match[1])
 if n>N:continue
 row=rows[n-1]
 for key,value in zip(['log10_M','log10_N','log10_N_over_M'],match.groups()[1:]):
  assert arb(row[key]).overlaps(arb(value,arb('0.0005'))),(n,key,value,row[key])
  printed.append(dict(n=n,quantity=key,reported=value,all_rounding_checks_pass=True))
slopes=[]
for end in sorted({310,316,320,326,338,350,N}):
 if end>N:continue
 center=end-13;den=sum((i-center)**2 for i in range(end-26,end+1))
 f=sum((arb(rows[i-1]['log10_M'])*(i-center) for i in range(end-26,end+1)),arb(0))/den
 g=sum((arb(rows[i-1]['log10_N'])*(i-center) for i in range(end-26,end+1)),arb(0))/den
 slopes.append(dict(end=end,density=text(f),stream=text(g),difference=text(g-f)))
now=datetime.now(timezone.utc);root=Path('research/82_weighted_loss_criterion/verification')/('plain_update_'+now.strftime('%Y%m%dT%H%M%SZ'));(root/'sources').mkdir(parents=True)
result=dict(checked_at_utc=now.isoformat(timespec='seconds'),input_path=str(source),input_sha256=sha256(source.read_bytes()).hexdigest(),checkpoint_sha256=data['checkpoint_sha256'],maximum_order=N,quarter_first_exceedance=min(exceeds) if exceeds else None,quarter_exceedances=exceeds,quarter_unresolved=unresolved,global_maximum_ratio=text(maximum),global_maximum_order=maximum_n,last_both_field_resolved_prefix=data['last_both_field_resolved_prefix'],last_both_field_1e_minus_6_prefix=data['last_both_field_1e_minus_6_prefix'],printed_comparisons=printed,slopes_27=slopes,rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Finite comparison from independently decoded coefficient enclosures; no infinite extrapolation.')
(root/'sources/exact_low_prefix.json').write_text(json.dumps(prefix,indent=2)+'\n');(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/numerics_table.md').write_text('## 2026-10-31T09:10Z'+excerpt)
(root/'sources/canonical_post_audit.py.txt').write_bytes(Path(__file__).read_bytes())
manifest={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file()};(root/'MANIFEST.json').write_text(json.dumps(dict(files=manifest),indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),**{k:v for k,v in result.items() if k not in ['rows','printed_comparisons']},printed_comparison_count=len(printed)),indent=2),flush=True)
