"""Prepared scalar certification; requires the independent analytic acceptance."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import argparse,hashlib,json
R=Path(__file__).resolve().parents[1]
B=R/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def ep(a,hi=False):return Q(str((a.upper() if hi else a.lower()).fmpq()))
def ceil10(q):
 k=-((-q*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);ap.add_argument('--analytic-acceptance',required=True);args=ap.parse_args()
 hashes={}
 def bind(p):
  p=p.resolve();assert p.is_relative_to(R);hashes[str(p.relative_to(R))]=sha(p)
 def accepted(rel,ledger=None):
  p=R/rel;d=load(p);assert d['verdict']=='CONFIRMED'
  if ledger:assert d['ledger']==ledger
  bind(p)
  for name,h in d['sha256'].items():assert sha(R/name)==h,name;bind(R/name)
  return d
 analytic=accepted(args.analytic_acceptance)
 for p in [B/'PROOF.md',B/'cutoff_plan/PROOF.md']:
  assert analytic['sha256'].get(str(p.relative_to(R)))==sha(p)
 phases=accepted('08_improved_upper_bounds/phase_interpolation/verification/accepted.json','V177')
 extra=accepted('05_team_audit/d36_recombination/verification/accepted.json','V179')
 cuts=accepted('08_improved_upper_bounds/explicit_second_term/verification/accepted.json','V118')
 sources={}
 def add(a,U,s,kind,source):
  a=Q(a);assert a not in sources;sources[a]=dict(U=Q(U),s=Q(s),kind=kind,source=source)
 rel='08_improved_upper_bounds/explicit_second_term/verification/rational_cutoffs.json';p=R/rel;bind(p)
 for row in load(p)['rows']:
  if Q(row['alpha']) in [Q(1,1000),Q(1,100)]:
   d=row['bounds']['J_D'];assert 0<Q(d['rho'])<=Q(1,3);add(row['alpha'],d['upper'],d['rho'],'perturbed cutoff',rel)
 rel='data/circle_composite_upper_n768.json';p=R/rel;circle=load(p);bind(p)
 assert circle['source_sha256']==sha(R/'code/combine_circle_upper.py');bind(R/'code/combine_circle_upper.py')
 for name,h in circle['input_sha256'].items():assert sha(R/name)==h;bind(R/name)
 cmp=R/'data/reflection_n768_comparison.json';d=load(cmp);assert d['all_inside'] and d['comparisons']==170;bind(cmp)
 for name,h in d['input_sha256'].items():assert sha(R/name)==h;bind(R/name)
 for row in circle['rows']:
  if Q(row['alpha']) in [Q(1,20),Q(1,10)]:add(row['alpha'],row['safe_upper_D'],'1/2','half-radius',rel)
 for row in extra['rows']:
  if Q(row['alpha']) in [Q(1,5),Q(99,100)]:add(row['alpha'],row['safe_upper_D'],'1/2','half-radius','05_team_audit/d36_recombination/verification/accepted.json')
 for row in phases['rows']:
  if row['operator']=='D':add(row['alpha'],row['safe_upper'],'1/2','half-radius','08_improved_upper_bounds/phase_interpolation/verification/accepted.json')
 assert sorted(sources)==[Q(1,1000),Q(1,100),Q(1,20),Q(1,10),Q(1,5),Q(3,10),Q(1,2),Q(3,4),Q(9,10),Q(99,100)]
 ctx.prec=384;JJ=arb(653)/288-arb(63)/8*(arb(4)/3).log();jlo,jhi=ep(JJ),ep(JJ,True)
 q=Q(1,7);N=256;partial=2*sum((q**(2*n+1)/Q(2*n+1) for n in range(N)),Q(0));tail=2*q**(2*N+1)/((2*N+1)*(1-q*q))
 Jlow=Q(653,288)-Q(63,8)*(partial+tail);Jhigh=Q(653,288)-Q(63,8)*partial
 assert Q(7,4608)<jlo<=Jlow<=Jhigh<=jhi
 rows=[]
 for a,src in sorted(sources.items()):
  ctx.prec=384;s=src['s'];aa,ss=arb(str(a)),arb(str(s));corr=s**4/(512*(1-s)**2) if src['kind']=='perturbed cutoff' else Q(0)
  coeff=JJ*ss**2-arb(str(corr));eta=aa*(1-aa)*(1+ss/2)**(aa-2)*coeff
  lo,hi=ep(eta),ep(eta,True);assert 0<lo<=hi
  ctx.prec=768;AA,SS=arb(str(a)),arb(str(s));factor=AA*(1-AA)*((AA-2)*(1+SS/2).log()).exp()
  freshlo=ep(factor*arb(str(Jlow*s*s-corr)));freshhi=ep(factor*arb(str(Jhigh*s*s-corr)),True)
  assert 0<lo<=freshlo<=freshhi<=hi
  bound=src['U']-lo;safe=ceil10(bound)
  assert src['U']-freshlo<=bound<=Q(safe)<bound+Q(1,10**10) and Q(safe)<src['U']
  rows.append(dict(alpha=str(a),radius=str(s),kind=src['kind'],previous_upper=str(src['U']),source=src['source'],eta_lower=str(lo),eta_upper=str(hi),eta_ball=eta.str(45),safe_upper_D=safe))
 for p in [B/'numerical_values/PROOF.md',Path(__file__)]:bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',precision_bits=[384,768],J=dict(atanh_terms=N,lower=str(Jlow),upper=str(Jhigh),ball=JJ.str(45)),rows=rows,sha256=hashes,method='Radial projection savings; independent exact rational atanh coefficient and ball power recomputation; exact upward rounding')
 (B/'numerical_values/accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],args.ledger,'CONFIRMED')
 for r in rows:print(r['alpha'],r['eta_ball'],r['safe_upper_D'])
if __name__=='__main__':main()
