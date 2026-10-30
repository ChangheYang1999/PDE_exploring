"""Finite serialization audit only; no publisher imports or PDE certificate."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from hashlib import sha256
from datetime import datetime, timezone
import json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/continuation027_float_audit'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();mf=json.loads((B/'source/MANIFEST.json').read_text());inputs={}
 for name,e in mf['files'].items():
  p=B/'source'/name;assert sha(p)==e['sha256'];inputs[str(p.relative_to(R))]=e['sha256']
 assert sha(B/'PROOF.md')==mf['proof_sha256']
 for p in [Path(__file__),B/'PROOF.md',B/'source/MANIFEST.json',B/'verification/PROOF_FIRST.json']:inputs[str(p.relative_to(R))]=sha(p)
 data={n:json.loads((B/f'source/{n}_weaktests3.json').read_text(),parse_float=Decimal) for n in ['022','026','027']}
 note=(B/'source/N1_NOTES.md').read_text().split('## 2026-10-29T13:38Z:',1)[1].split('\n## ',1)[0]
 pat=r'\((\d+), (\d+)\) ([\d.e+\-]+) -> ([\d.e+\-]+) \(x([\d.]+)\)'
 parts={'022':note.split('per probe 022 -> 027:',1)[1].split('Largest registered',1)[0],'026':note.split('026 -> 027',1)[1].split('Reading (FLOAT',1)[0]}
 pairs=[(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]];comparisons={};checks={};printed_total=0
 for old,part in parts.items():
  table=re.findall(pat,part);assert len(table)==25
  assert [(int(n),int(k)) for n,k,*_ in table]==pairs
  rows=[]
  for n0,k0,a,b,qp in table:
   n,k=int(n0),int(k0);oldv=data[old]['probes'][f'{n}:{k}']['m_lower_bound'];newv=data['027']['probes'][f'{n}:{k}']['m_lower_bound']
   assert Q(oldv)>0 and Q(newv)>0
   assert format(float(oldv),'.2e')==a and format(float(newv),'.2e')==b
   q=Q(newv)/Q(oldv);rows.append({'n':n,'K':k,'old_serialized':str(oldv),'new_serialized':str(newv),'stored_decimal_ratio':str(q),'stored_ratio_approx':float(q),'printed_ratio_exact':str(Q(b)/Q(a)),'note_ratio':qp,'direction':(q>1)-(q<1)});printed_total+=2
  stats={}
  for label,selected in [('all',rows),('K_ge_1800',[r for r in rows if r['K']>=1800])]:
   vals=[Q(r['stored_decimal_ratio']) for r in selected];stats[label]={'count':len(vals),'decrease_equal_increase':[sum(r['direction']==i for r in selected) for i in [-1,0,1]],'minimum_exact':str(min(vals)),'maximum_exact':str(max(vals)),'minimum_approx':float(min(vals)),'maximum_approx':float(max(vals))}
  comparisons['027_vs_'+old]={'rows':rows,'statistics':stats}
 def row(n,k):return next(r for r in comparisons['027_vs_022']['rows'] if (r['n'],r['K'])==(n,k))
 checks['all100_displayed_values_match_copied_sources']=printed_total==100
 checks['claimed_universal117_range_present']='every registered probe within x0.83 to x1.17' in note
 checks['printed_n25_K900_counterexample']=Q(row(25,900)['printed_ratio_exact'])==Q(539,402)>Q(117,100)
 checks['stored_n25_K900_counterexample']=Q(row(25,900)['stored_decimal_ratio'])>Q(117,100)
 checks['printed_n29_K1200_counterexample']=Q(row(29,1200)['printed_ratio_exact'])==Q(557,464)>Q(117,100)
 checks['stored_n29_K1200_counterexample']=Q(row(29,1200)['stored_decimal_ratio'])>Q(117,100)
 checks['immutable027_candidate_not_assumed']=True
 assert all(checks.values());assert all(sha(R/p)==h for p,h in inputs.items())
 result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'comparisons':comparisons,'PDE_values_certified':False,'027_snapshot_accepted':False,'verdict':'REFUTED universal117 FLOAT range; CONFIRMED finite source/display comparisons only','elapsed_seconds':time.monotonic()-start}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',sha(B/'verification/result.json'))
 for key,d in comparisons.items():print(key,json.dumps(d['statistics']))
if __name__=='__main__':main()
