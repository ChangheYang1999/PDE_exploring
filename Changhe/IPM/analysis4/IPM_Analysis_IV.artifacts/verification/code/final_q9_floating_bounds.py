"""Directed final bounds for all ten admitted period-nine floating extensions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,math,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from certificate_admission import stamp,ref,checkref,next_entry
ctx.prec=768
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);args=ap.parse_args()
start=time.monotonic();base=Path('research/301_final_claim_audit');src=Path('research/303_period_nine_ten_floating_extensions/verification')
def ab(q):
 q=F(q);return arb(q.numerator)/q.denominator
def fmt(x):return x.str(42,radius=True)
def extremum(rows,key,maximize=True):
 selected=(max if maximize else min)(rows,key=lambda r:float(arb(r[key]).mid()))
 for r in rows:
  if r is not selected:
   assert (arb(selected[key])>arb(r[key])) if maximize else (arb(selected[key])<arb(r[key]))
 return selected
def bound(x,scale=1000):
 # Floating arithmetic proposes an integer only. Exact comparison verifies it.
 k=math.floor(float(x.mid())*scale)+1
 assert ab(F(k,scale))>x
 assert ab(F(k-1,scale))<x
 return F(k,scale)
def outward(x,up):
 # The four-significant-digit rounding step is selected approximately, then checked.
 e=math.floor(math.log10(float(x.mid())))-3
 step=F(10)**e
 k=math.floor(float(x.mid())/float(step))+(1 if up else 0)
 q=k*step
 assert ab(q)>x if up else ab(q)<x
 return format(float(q),f'.{max(0,-e)}f'),str(q)
labels=set()
for p in src.glob('admission_V*.json'):labels.update(json.loads(p.read_text()).get('cases',[]))
assert all(f'Q9_root{i}' in labels for i in range(1,11))
rows=[];changes=[];radii=[];refs=[];norm=neq=tuning=teq=fit_count=0;diffs=[]
for root in range(1,11):
 p=src/f'Q9_root{root}.json';d=json.loads(p.read_text());assert d['all_checks_pass'];checkref(d['source']);checkref(d['baseline']);refs.append(ref(p))
 assert d['announced_order']==612 and d['last_printed_order']==611 and d['last_complete_block']==603
 norm+=d['printed_norm_overlap_count'];neq+=d['exact_norm_overlap_count'];tuning+=d['printed_tuning_overlap_count'];teq+=d['exact_tuning_overlap_count'];fit_count+=len(d['baseline_fits'])+len(d['extended_fits'])
 diffs.extend(dict(root=root,**r) for r in d['tuning_differences'])
 selected=[r for r in d['extended_fits'] if r['channel']=='density' and r['window_lower'] in [100,200,300,400]];assert len(selected)==4
 lo=extremum(selected,'A',False);hi=extremum(selected,'A')
 lo_text,lo_q=outward(arb(lo['A']),False);hi_text,hi_q=outward(arb(hi['A']),True)
 for r in selected:
  a=arb(r['A']);assert ab(lo_q)<a<ab(hi_q)
  rr=a**4*a.sqrt();assert rr.overlaps(arb(r['apparent_radius']))
  radii.append(dict(root=root,window_lower=r['window_lower'],value=fmt(rr)))
 spread=arb(hi['A'])/arb(lo['A'])-1
 rows.append(dict(root=root,decimal_bounds=[lo_text,hi_text],exact_bounds=[lo_q,hi_q],minimum=lo,maximum=hi,relative_spread=fmt(spread),baseline_epsilon=d['baseline_epsilon'],extended_epsilon=d['extended_epsilon']))
 for r in d['same_window_changes']:
  if r['channel']!='density':continue
  x=arb(r['relative_A_change']);assert 1+x>0;y=(1+x)**4*(1+x).sqrt()-1
  assert y.overlaps(arb(r['relative_apparent_radius_change']))
  changes.append(dict(root=root,**r,absolute_radius_change=fmt(abs(y))))
assert norm==neq==6100 and tuning==320 and fit_count==180 and len(changes)==30
assert tuning-teq==len({(r['root'],r['k']) for r in diffs})
maxa=extremum(changes,'absolute_relative_A_change');maxr=extremum(changes,'absolute_radius_change');maxspread=extremum(rows,'relative_spread');minrad=extremum(radii,'value',False);maxrad=extremum(radii,'value')
ba=bound(arb(maxa['absolute_relative_A_change']));br=bound(arb(maxr['absolute_radius_change']));bs=bound(arb(maxspread['relative_spread']))
for r in changes:assert arb(r['absolute_relative_A_change'])<ab(ba) and arb(r['absolute_radius_change'])<ab(br)
for r in rows:assert arb(r['relative_spread'])<ab(bs)
down=sum(arb(r['relative_A_change'])<0 for r in changes if r['window_lower']==100);up=sum(arb(r['relative_A_change'])>0 for r in changes if r['window_lower']==100);assert up+down==10
ledger,text=next_entry(args.entry);now=stamp();v=f'V{args.entry}'
result=(f'All40 density fits lie strictly in their ten outward decimal ranges. Maximum four-window relative spread is {maxspread["relative_spread"]} at root{maxspread["root"]}. '
 f'Across30 same-window comparisons, maximum absolute A change is {maxa["absolute_relative_A_change"]} at root{maxa["root"]}, lower{maxa["window_lower"]}; maximum absolute apparent-radius change is {maxr["absolute_radius_change"]} at root{maxr["root"]}, lower{maxr["window_lower"]}. '
 f'Strict upper bounds on spread, A change and apparent-radius change are {float(100*bs):g}%, {float(100*ba):g}% and {float(100*br):g}%, respectively. '
 f'At lower100, {down}/10 changes are negative and {up}/10 positive. Apparent-radius extrema are {minrad["value"]} at root{minrad["root"]} and {maxrad["value"]} at root{maxrad["root"]}. '
 f'All6100 printed norm components agree; {teq}/320 complete tuning rows agree, with {len(diffs)} explicitly retained component differences. All180 finite density/stream fits have been recomputed.')
scope='CONFIRMED for finite statistics of printed rounded-root floating data. The apparent radius is A^(9/2), not a bound on the true convergence radius.'
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, {v}: {result} {scope}\n')
proof=base/'sources'/f'PROOF_at_{v}.md';proof.write_bytes((base/'PROOF.md').read_bytes())
receipt=base/'verification'/f'admission_{v}.json';receipt.write_text(json.dumps(dict(at=now,entry=args.entry,verdict='CONFIRMED',all_checks_pass=True,checks=refs,proof=ref(proof),ranges=rows,changes=changes,max_A=maxa,max_radius=maxr,max_spread=maxspread,strict_bounds=dict(A=str(ba),apparent_radius=str(br),spread=str(bs)),min_apparent_radius=minrad,max_apparent_radius=maxrad,negative_at_lower100=down,positive_at_lower100=up,norm_components=norm,tuning_rows=tuning,identical_tuning_rows=teq,tuning_differences=diffs,fit_count=fit_count,result=result,scope=scope,actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
ledger.write_text(text+f'\n## {v} | {now} | Final Q9 finite display and percentage bounds\n\n**Claim.** The ten Q9 extensions admit the recorded outward ranges, percentage bounds and sign counts.\n\n**Method.** Exact-decimal input fits from topic303; direct interval extrema and rational bounds; independent algebraic evaluation of the9/2 apparent-radius exponent.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
table='\n'.join(f'| {r["root"]} | {r["decimal_bounds"][0]} to {r["decimal_bounds"][1]} |' for r in rows)
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: {v} final Q9 percentage and outward-range audit\n\n{result}\n\n| Root | Outward A range |\n|---|---|\n{table}\n\n{scope}\n\n'+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: {v} admits final Q9 ranges, percentages and sign counts from all ten completed cases.\n')
(base/'sources/final_q9_floating_bounds.py').write_bytes(Path(__file__).read_bytes())
print(now,result);print(table)
