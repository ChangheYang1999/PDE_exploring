from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_conforming_repair'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((D/'evidence/compute.json').read_text());b=json.loads((D/'evidence/independent.json').read_text());pins={}
for n,h in b['files'].items():check(sha(B/n)==h,'pin');pins[n]=h
records=[]
for x,y in zip(a['records'],b['records'],strict=True):
 check(x['public']==y['public'],'public bounds');pc=x['columns'];ic=y['columns'];check(len(pc)==len(ic)==x['N'],'allcolumns');best=max(pc,key=lambda z:F(z['sqrt_ratio_arb512'][1]));check(best['column_index']==x['largest_ratio_column'],'actual extremizer');imax=max(ic,key=lambda z:F(z['sqrt_ratio_iv120'][1]));check(imax['column_index']==best['column_index'],'independent extremizer')
 check(max(F(z['sqrt_ratio_arb512'][1]) for z in pc)<F(x['public']['uniform_single_column_relative_broken_energy_upper']) and max(F(z['sqrt_ratio_iv120'][1]) for z in ic)<F(x['public']['uniform_single_column_relative_broken_energy_upper']),'all interval upperbounds strict')
 for p,q in zip(pc,ic,strict=True):
  check(p['pieces']==q['pieces'],'exact piece agreement')
  for j,r in enumerate(p['pieces']):
   if j:check(r['beta_left']==p['pieces'][j-1]['beta_right'],'adjacent trace certificate')
  check(F(p['pieces'][0]['beta_left'])==F(p['pieces'][-1]['beta_right'])==0,'support trace zero')
 records.append({k:v for k,v in x.items() if k!='columns'}|{'maximizer_arb512':{k:v for k,v in best.items() if k!='pieces'},'maximizer_iv120':{k:v for k,v in imax.items() if k!='pieces'},'piece_count':sum(len(z['pieces']) for z in pc),'scope':'Uniform in a single angular mode and a single selected radial column. No arbitrary combination or true weak X distance from the discontinuous raw function.'})
for p in [Path(__file__),D/'evidence/independent.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FULL_REPAIR_OUTPUT_COMPARISON_AND_STRICT_CEILING_AUDIT','records':records,'exact_repaired_trace_checks':a['exact_repaired_trace_checks'],'files':pins};p=D/'evidence/summary.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'columns':sum(x['N'] for x in records)}))
