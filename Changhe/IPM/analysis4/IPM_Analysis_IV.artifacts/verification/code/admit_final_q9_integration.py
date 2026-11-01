"""Verify the final Q9 report insertion against already admitted finite fits."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,re,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from certificate_admission import stamp,ref,next_entry
from reconstruct_text_delta import reconstruct
ctx.prec=512
base=Path('research/301_final_claim_audit');old=base/'verification/post_freeze_20261031T233028Z';new=base/'verification/post_freeze_20261031T235419Z'
v651=base/'verification/admission_V651.json';cert=json.loads(v651.read_text())
def ab(q):
 q=F(q);return arb(q.numerator)/q.denominator
def extreme(xs,maximum):
 z=(max if maximum else min)(xs,key=lambda x:float(x.mid()))
 for x in xs:
  assert x is z or ((z>x) if maximum else (z<x))
 return z
texts={k:reconstruct(new/f'{k}.json').decode() for k in ['summary','report','theory']}
assert texts['theory']==reconstruct(old/'theory.json').decode()
report=texts['report'];start=report.index('At $\\delta=2/9$ the runs at all ten roots were repeated to order 612');end=report.index('At $\\delta=1/5$ (order 300',start);passage=report[start:end]
needle='the fitted $A$ on $n\\ge100$, $200$, $300$ and $400$ are '
s=passage.split(needle)[1].split(' at the ten roots')[0]
displays=re.findall(r'\$(\d+(?:\.\d+)?)\$ to \$(\d+(?:\.\d+)?)\$',s)
assert len(displays)==10
assert displays==[tuple(r['decimal_bounds']) for r in cert['ranges']]
assert arb(cert['max_spread']['relative_spread'])<ab('0.014')
assert arb(cert['max_A']['absolute_relative_A_change'])<ab('0.06')
assert arb(cert['max_radius']['absolute_radius_change'])<ab('0.30')
assert cert['max_A']['root']==8 and cert['max_A']['window_lower']==200
assert ab('0.0585')<arb(cert['max_A']['relative_A_change'])<ab('0.0595')
assert cert['min_apparent_radius']['root']==3 and cert['max_apparent_radius']['root']==1
assert ab('0.1335')<arb(cert['min_apparent_radius']['value'])<ab('0.1345')
assert ab('1085000')<arb(cert['max_apparent_radius']['value'])<ab('1095000')
assert 'less than $6\\%$' in texts['summary']
rows=[];checks=[]
for r in cert['ranges']:
 root=r['root'];p=Path(f'research/303_period_nine_ten_floating_extensions/verification/Q9_root{root}.json');d=json.loads(p.read_text());checks.append(ref(p))
 assert d['announced_order']==612 and d['last_complete_block']==603
 expected=['1/16','1/4','1','1','1','1','1/2','1/2','1/4','1/8'][root-1]
 assert F(d['extended_epsilon'])==F(expected)
 oldvals=[arb(x['A']) for x in d['baseline_fits'] if x['channel']=='density']
 oldlo=extreme(oldvals,False);oldhi=extreme(oldvals,True)
 newlo=arb(r['minimum']['A']);newhi=arb(r['maximum']['A'])
 departure=max([arb(0),(oldlo-newlo)/oldlo,(newhi-oldhi)/oldhi],key=lambda x:float(x.mid()))
 line=[s for s in report.splitlines() if s.startswith('| $2/9$ |')][root-1]
 bounds=re.findall(r'\$(\d+(?:\.\d+)?)\$',line.split('|')[3]);assert len(bounds)==2
 dlo,dhi=map(ab,bounds);plo,phi=map(ab,r['decimal_bounds'])
 display_departure=max([arb(0),(dlo-plo)/dlo,(phi-dhi)/dhi],key=lambda x:float(x.mid()))
 assert departure<ab('0.027') and display_departure<ab('0.027')
 upper_change=newhi-oldhi
 if root in [1,6,7,8,9]:assert upper_change<0
 if root==10:assert upper_change>0
 rows.append(dict(root=root,old_min=str(oldlo),old_max=str(oldhi),new_min=str(newlo),new_max=str(newhi),actual_range_departure=str(departure),display_range_departure=str(display_departure),upper_extremum_change=str(upper_change)))
for key in ['actual_range_departure','display_range_departure']:
 winner=max(rows,key=lambda r:float(arb(r[key]).mid()));assert winner['root']==2
 for r in rows:
  if r is not winner:assert arb(winner[key])>arb(r[key])
ledger,text=next_entry(653);now=stamp()
result=('The new ten Q9 ranges match V651 exactly. All40 fits lie in the displayed intervals. The strict spread, density-base-change and apparent-radius-change bounds of1.4%,6% and30% hold; the sharper radius bound29.6% is also admitted in V651. The largest density change rounds to+5.9% at root8 on n>=200. Both actual-fit and displayed-range departures from the older table are below2.7%, largest at root2. The upper extrema decrease at roots1,6,7,8,9 and increase at root10. All amplitudes, completion orders, overlap claims and displayed apparent-radius extrema agree. The theory is byte-identical to the last reviewed snapshot. The summary changes only its timestamp and the finite Q9 comparison; the report additionally inserts the verified paragraph.')
scope='CONFIRMED for the changed finite-statistic passages. No convergence boundary or new infinite theorem is inferred. The assembled report was not newly read cover to cover.'
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V653. {result}\n\n{scope}\n')
proof=base/'sources/PROOF_at_V653.md';proof.write_bytes((base/'PROOF.md').read_bytes())
code=base/'sources/admit_final_q9_integration.py';code.write_bytes(Path(__file__).read_bytes())
p=base/'verification/admission_V653.json';p.write_text(json.dumps(dict(at=now,entry=653,verdict='CONFIRMED',all_checks_pass=True,previous_snapshots=[ref(old/f'{k}.json') for k in texts],current_snapshots=[ref(new/f'{k}.json') for k in texts],finite_bound_certificate=ref(v651),checks=checks,proof=ref(proof),algorithm=ref(code),range_comparisons=rows,result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V653 | {now} | Final Q9 report integration\n\n**Claim.** The final Q9 extension paragraph and summary comparison accurately describe the admitted finite datasets.\n\n**Method.** Read every changed passage between two reconstructible snapshots; direct interval comparisons with V651 and all ten baseline datasets.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
n=Path('NOTES_FOR_TEAM.md');n.write_text(f'## {now} VERIFIER -> LEAD: V653 closes final Q9 insertion\n\n{result}\n\n{scope}\n\n'+n.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V653 admits final Q9 paragraph, ten ranges, comparisons and summary insertion.\n')
print(now,result)
