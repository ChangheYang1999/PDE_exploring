"""Exact finite-data audit of the final Q10 percentage and display bounds."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from certificate_admission import stamp,ref,checkref,next_entry
ctx.prec=768
base=Path('research/301_final_claim_audit')
sourcebase=Path('research/303_period_nine_ten_floating_extensions/verification')
bounds=[('29.60','30.17'),('5.224','5.286'),('2.092','2.116'),('1.341','1.348'),('1.076','1.087'),('0.6955','0.6970'),('0.9218','0.9265'),('1.150','1.159'),('1.524','1.541'),('2.032','2.064'),('2.784','2.825'),('3.886','3.961'),('5.991','6.087'),('13.37','13.61')]
def exact(s):
 f=F(s);return arb(f.numerator)/f.denominator
def strict_max(items,key):
 best=max(items,key=lambda x:float(arb(x[key]).mid()))
 for x in items:
  if x is not best:assert arb(best[key])>arb(x[key])
 return best
def fmt(x):return x.str(42,radius=True)
rows=[];changes=[];radii=[];refs=[];norm=neq=tun=teq=fits=0;diffs=[]
for root,(lo,hi) in enumerate(bounds,1):
 p=sourcebase/f'Q10_root{root}.json';d=json.loads(p.read_text());assert d['all_checks_pass'];checkref(d['source']);checkref(d['baseline']);refs.append(ref(p))
 norm+=d['printed_norm_overlap_count'];neq+=d['exact_norm_overlap_count'];tun+=d['printed_tuning_overlap_count'];teq+=d['exact_tuning_overlap_count'];fits+=len(d['baseline_fits'])+len(d['extended_fits'])
 diffs += [dict(root=root,**r) for r in d['tuning_differences']]
 chosen=[r for r in d['extended_fits'] if r['channel']=='density' and r['window_lower'] in (100,200,300,400)]
 assert len(chosen)==4
 for r in chosen:
  a=arb(r['A']);assert exact(lo)<a<exact(hi), (root, r['window_lower'], lo, r['A'], hi)
  rr=a**5;assert rr.overlaps(arb(r['apparent_radius']))
  radii.append(dict(root=root,window_lower=r['window_lower'],value=fmt(rr)))
 low=min(chosen,key=lambda r:float(arb(r['A']).mid()));high=max(chosen,key=lambda r:float(arb(r['A']).mid()))
 for r in chosen:
  if r is not low:assert arb(r['A'])>arb(low['A'])
  if r is not high:assert arb(high['A'])>arb(r['A'])
 spread=arb(high['A'])/arb(low['A'])-1;assert spread<exact('0.02')
 rows.append(dict(root=root,printed_bounds=[lo,hi],minimum=low['A'],maximum=high['A'],relative_spread=fmt(spread)))
 for r in d['same_window_changes']:
  if r['channel']!='density':continue
  x=arb(r['relative_A_change']);rx=(1+x)**5-1
  assert rx.overlaps(arb(r['relative_apparent_radius_change']))
  assert abs(x)<exact('0.071') and abs(rx)<exact('0.31')
  changes.append(dict(root=root,**r,absolute_radius_change=fmt(abs(rx))))
assert norm==neq==8372 and tun==392 and teq==388 and len(diffs)==4 and fits==252
maxa=strict_max(changes,'absolute_relative_A_change');maxr=strict_max(changes,'absolute_radius_change');maxspread=strict_max(rows,'relative_spread')
down=sum(arb(r['relative_A_change'])<0 for r in changes if r['window_lower']==100);assert down==11
minrad=min(radii,key=lambda r:float(arb(r['value']).mid()));maxrad=strict_max(radii,'value')
for r in radii:
 if r is not minrad:assert arb(r['value'])>arb(minrad['value'])
assert exact('0.1625')<arb(minrad['value'])<exact('0.1635')
assert exact('24900000')<arb(maxrad['value'])<exact('25000000')
now=stamp();entry=633;ledger,text=next_entry(entry)
result=(f"All 56 displayed density-fit values lie strictly within their fourteen outward ranges. All fourteen four-window relative spreads are below2%; maximum {maxspread['relative_spread']} at root{maxspread['root']}. "
 f"Across42 same-window comparisons, maximum absolute A change {maxa['absolute_relative_A_change']} and maximum absolute apparent-radius change {maxr['absolute_radius_change']} occur at root{maxa['root']}, lower{maxa['window_lower']}; strict bounds7.1% and31% hold. "
 f"Exactly11 of14 density A changes at lower100 are negative. The four-window apparent-radius extrema are {minrad['value']} at root{minrad['root']} and {maxrad['value']} at root{maxrad['root']}. "
 "All8372 printed norm components agree;388/392 complete tuning rows agree, with4 components differing by10^-12;252 density/stream fits have been recomputed.")
scope='CONFIRMED for the finite rounded-root floating data. Apparent radii are the fifth powers of fitted A values, not bounds on the true radius.'
with (base/'PROOF.md').open('a') as f:f.write('\n## Final Q10 finite display bounds, V633\n\nFor each of fourteen roots, take the four admitted density fits with lower endpoints100,200,300,400. Strict interval comparisons verify each stated decimal range and (maximum A)/(minimum A)-1<1/50. Compare all42 admitted same-window signed changes x to71/1000 in absolute value. Convert each to (1+x)^5-1 and compare its absolute value to31/100. Direct finite comparisons identify both maxima and count negative changes at lower100. This proves the stated finite-data bounds without using a surrogate bound on (1+|x|)^5-1, which would be too weak here. It does not control unknown coefficient errors, the limiting growth rate or a true convergence boundary.\n')
proof=base/'sources/PROOF_at_V633.md';proof.write_bytes((base/'PROOF.md').read_bytes())
receipt=base/'verification/admission_V633.json';receipt.write_text(json.dumps(dict(at=now,entry=entry,all_checks_pass=True,checks=refs,proof=ref(proof),ranges=rows,changes=changes,max_A=maxa,max_radius=maxr,max_spread=maxspread,min_apparent_radius=minrad,max_apparent_radius=maxrad,negative_at_lower100=down,norm_components=norm,tuning_rows=tun,identical_tuning_rows=teq,tuning_differences=diffs,fit_count=fits,result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V633 | {now} | Final Q10 finite display bounds\n\n**Claim.** The new Q10 ranges, percentage bounds and direction count follow from the admitted finite fits.\n\n**Method.** Exact-decimal input normal equations from topic303, directed interval comparisons, and the exact fifth-power apparent-radius transformation.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: V633 Q10 display and percentage audit\n\n{result}\n\n{scope}\n\n'+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V633 admitted all14 Q10 display ranges,2% spread,7.1% A drift and31% apparent-radius drift.\n')
(base/'sources/final_q10_floating_bounds.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
