"""Independent exact-decimal recombination and profile-completion checks."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,re
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
ctx.prec=256

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def endpoints(text):
 text=text.strip()
 if text.startswith('['):
  mid,rad=text[1:-1].split('+/-');mid,rad=Q(mid.strip()),Q(rad.strip());return mid-rad,mid+rad
 v=Q(text);return v,v

def floordec(x,n=10):
 k=(x*10**n).__floor__();return f'{k//10**n}.{k%10**n:0{n}d}'

base=ROOT/'11_lattice_pole_constraints/axis_clamped_layercake/verification'
combined=base/'a99_b1_long_combined_2097152.json';d=json.loads(combined.read_text())
for name,h in d['source_hashes'].items():assert sha(ROOT/name)==h,name
parts=[];lo=Q(1);hi=Q(1)
for part in ['plus','mid','minus']:
 path=base/f'a99_b1_long_{part}_2097152.json';p=json.loads(path.read_text())
 assert p['part']==part and Q(p['alpha'])==Q(99,100) and Q(p['b'])==1
 assert p['cells']==2097152 and p['start']==0 and p['stop']==2097152 and p['precision_bits']>=256
 assert (Q(p['left']),Q(p['right']))==((Q(1,10000000),Q(24)) if part=='mid' else (Q(-20),Q(900)))
 for name,h in p['source_hashes'].items():assert sha(ROOT/name)==h,name
 l,u=endpoints(p['included_integral_enclosure']);assert l>0
 lo+=2*l;hi+=2*u;parts.append({'part':part,'exact_lower':str(l),'exact_upper':str(u),'sha256':sha(path)})
assert Q(d['safe_D_lower_10_places'])<=lo
rows=json.loads((ROOT/'data/verified_table.json').read_text())['rows'];row=next(r for r in rows if Q(r['alpha'])==Q(99,100))
uc=Q(row['selected_upper_C']['exact_safe_endpoint']);gap=Q(d['safe_D_lower_10_places'])-uc;assert gap>0
out={'time_utc':datetime.now(timezone.utc).isoformat(),'parts':parts,'exact_recombined_lower':str(lo),'exact_recombined_upper':str(hi),'safe_D_lower':d['safe_D_lower_10_places'],'upper_C':str(uc),'safe_positive_gap':floordec(gap),'verdict':'CONFIRMED; exact rational recombination of the original printed component enclosures. The saved combined ball has a coarser printed radius and is not used to reconstruct the safe lower endpoint.'}
(base/'a99_b1_long_independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('D99 lower',out['safe_D_lower'],'gap',out['safe_positive_gap'])

base=ROOT/'07_diagonal_identity_term/full_range_profile/verification'
cover=[]
for mode in ['same','opposite']:
 path=base/f'a90_k110_{mode}.json';p=json.loads(path.read_text())
 assert Q(p['alpha'])==Q(9,10) and Q(p['target'])==Q(11,10) and p['mode']==mode
 assert p['checked_boxes']==2*p['accepted_boxes']-1
 assert endpoints(p['largest_accepted_bound'])[1]<Q(11,10)
 for name,h in p['source_hashes'].items():assert sha(ROOT/name)==h,name
 a=arb(9)/10;e=arb(str(Q(p['epsilon'])));k=1/(1-a);R0=(1-e)**a;c=a*(1-e)**(a-1)
 left=(1-e)**(-a);right=1+(k-1)*c*c*e*e/(8*R0**arb.max(arb(1),k-1))+c/2*e**(1-a)
 assert left<arb(11)/10 and left.overlaps(arb(p['left_endpoint']))
 if mode=='opposite':assert right<arb(11)/10 and right.overlaps(arb(p['right_endpoint']))
 cover.append({'mode':mode,'checked':p['checked_boxes'],'accepted':p['accepted_boxes'],'left_recomputed':left.str(60,more=True),'right_recomputed':None if mode=='same' else right.str(60,more=True),'sha256':sha(path)})
out={'time_utc':datetime.now(timezone.utc).isoformat(),'alpha':'9/10','safe_profile_factor':'11/10','covers':cover,'verdict':'CONFIRMED under the independently checked complete pair-class and interval-bound proofs; both exact rational bisection runs completed, all endpoint regions covered.'}
(base/'a90_k110_independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('P90 seminorm <= 11/10; both completed covers and endpoint recomputations pass')
