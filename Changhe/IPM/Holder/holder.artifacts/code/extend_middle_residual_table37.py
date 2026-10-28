"""Extend the accepted, alpha-independent middle extraction to six exponents."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,hashlib,json,re
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/middle_circle_transport/balanced_residual'
OUT=BASE/'table37/verification'
TABLE=ROOT/'05_team_audit/table37_lead'
RAD=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement'
ALPHAS=['1/1000','1/100','1/20','1/10','1/5','99/100']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def end(s):
 if not s.startswith('['):return Q(s),Q(s)
 m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s);assert m,s
 c,r=map(Q,m.groups());return c-r,c+r
def pair(d):return Q(d['lower']),Q(d['upper'])
def uq(x):return Q(str(x.upper().fmpq()))
def lq(x):return Q(str(x.lower().fmpq()))
def rec(x):return dict(lower=str(lq(x)),upper=str(uq(x)),display=x.str(42,more=True))
def func(p,name):
 a=ast.parse(p.read_text());n=[z for z in a.body if isinstance(z,ast.FunctionDef) and z.name==name];assert len(n)==1;return ast.dump(n[0],include_attributes=False)
def ceil10(q):
 k=-((-q*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'
def main():
 hashes={}
 def bind(p):hashes[str(p.relative_to(ROOT))]=sha(p)
 for approval,ledger in [(BASE/'verification/accepted.json','V168'),(RAD/'verification/accepted.json','V161'),(TABLE/'verification/accepted.json','V131')]:
  d=load(approval);assert d['verdict']=='CONFIRMED' and d['ledger']==ledger;bind(approval)
  for name,h in d['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
 assert func(TABLE/'source/code/mid_nodes.py','bin_data')==func(ROOT/'code/certify_middle_chunks.py','bin_data')
 assert sha(TABLE/'source/code/certify_far_circles.py')==sha(ROOT/'code/certify_far_circles.py')
 for p in (TABLE/'source/code/mid_nodes.py',TABLE/'source/code/certify_far_circles.py'):bind(p)
 sources=[];covered=set();oldsource={a:[Q(0)]*17 for a in ALPHAS}
 for p in sorted((TABLE/'source/mid').glob('n512_*.json')):
  d=load(p);bind(p);assert d['precision_bits']==160 and d['angles_per_half']==d['radial_cells']==512 and d['phase_intervals']==16 and d['integer_unit']==2**44
  for name,h in d['source_hashes'].items():assert sha(TABLE/'source/code'/name)==h;bind(TABLE/'source/code'/name)
  for k in range(d['row_start'],d['row_stop']):assert k not in covered;covered.add(k)
  rows={r['alpha']:r for r in d['rows']};assert set(rows)==set(ALPHAS) and all(r['plan_reference_alpha']==a for a,r in rows.items())
  sources.append((p,d,rows))
  for a,r in rows.items():
   for j,s in enumerate(r['residual_intervals']):oldsource[a][j]+=end(s)[0]
 assert covered==set(range(512))
 old={};new={};row_records=[]
 ctx.prec=160;pi160=arb.pi()
 for k in range(512):
  p=BASE/'verification/mass_replay'/f'row_{k:03d}.json';d=load(p);bind(p)
  assert d['row']==k and d['subdivisions']==8
  lo=pi160*k/1024;hi=pi160*(k+1)/1024;rmax=arb(lo.union(hi).sin().upper())
  old[k]={a:[] for a in ALPHAS};new[k]={a:[] for a in ALPHAS};details=[]
  sub=[]
  for q in range(8):
   left=lo+(hi-lo)*q/8;right=lo+(hi-lo)*(q+1)/8;radius=arb.min(arb(1),arb(right.sin().upper()))
   costs=[]
   for a in ALPHAS:
    A=uq((2*radius*radius)**arb(a));B=max(A,uq((2*radius)**arb(a)));costs.append((A,B))
   sub.append((right-left,costs))
  for j,z in enumerate(d['phases']):
   assert z['phase']==j and len(z['subintervals'])==8
   vl,vu=pair(z['variation']);v=arb(str(vl)).union(arb(str(vu)));tau=vu
   values=[arb(0) for _ in ALPHAS]
   for (width,costs),q in zip(sub,z['subintervals']):
    ql,qu=pair(q['signed_residual']);h=min(tau,max(abs(ql),abs(qu)))
    assert h==Q(q['used_unbalanced_mass'])
    for n,(A,B) in enumerate(costs):values[n]+=(arb(str(tau-h))*arb(str(A))+arb(str(h))*arb(str(B)))*width
   for a,vnew in zip(ALPHAS,values):
    vold=(2*rmax)**arb(a)*v*(hi-lo);old[k][a].append((lq(vold),uq(vold)));new[k][a].append(min(uq(vnew),uq(vold)))
   details.append(dict(phase=j,new_upper={a:str(new[k][a][j]) for a in ALPHAS}))
  row_records.append(dict(row=k,phases=details))
 checks=[]
 for p,d,rr in sources:
  for a,r in rr.items():
   for j,text in enumerate(r['residual_intervals']):
    ll=sum((old[k][a][j][0] for k in range(d['row_start'],d['row_stop'])),Q(0));uu=sum((old[k][a][j][1] for k in range(d['row_start'],d['row_stop'])),Q(0));sl,su=end(text)
    assert max(ll,sl)<=min(uu,su),(a,j,p.name,'old residual mismatch')
    checks.append(dict(chunk=str(p.relative_to(ROOT)),alpha=a,phase=j,old_intervals_overlap=True))
 ctx.prec=320
 d=load(RAD/'verification/independent_audit.json');crows={r['alpha']:r for r in d['rows']};bind(RAD/'verification/independent_audit.json')
 d=load(RAD.parent/'existing_certificates/verification/independent_audit.json');small={r['alpha']:Q(r['small_upper']) for r in d['rows']};bind(RAD.parent/'existing_certificates/verification/independent_audit.json')
 results=[];sec=1/(arb.pi()/64).cos()
 for a in ALPHAS:
  news=[sum((new[k][a][j] for k in range(512)),Q(0)) for j in range(17)]
  gains=[max(Q(0),l-h) for l,h in zip(oldsource[a],news)]
  phase=[Q(v)-g for v,g in zip(crows[a]['phase_upper'],gains)];worst=max(range(17),key=lambda j:phase[j]);U=arb(str(small[a]))+sec*arb(str(phase[worst]));safe=ceil10(uq(U))
  assert Q(safe)<=Q(crows[a]['safe_upper_C'])
  results.append(dict(alpha=a,safe_upper_C=safe,previous_upper_C=crows[a]['safe_upper_C'],upper=rec(U),worst_phase=worst,
   phase_upper=list(map(str,phase)),old_source_lower=list(map(str,oldsource[a])),new_residual_upper=list(map(str,news)),accepted_gains=list(map(str,gains))))
  print(a,safe,'phase',worst,flush=True)
 for p in (Path(__file__),BASE/'table37/PROOF.md'):bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='NUMERICAL CHECKS PASS; numerical statement and acceptance pending',rows=results,details=row_records,residual_checks=checks,source_equivalence='bin_data AST equal; complete cell_measures helper file identical',sha256=hashes)
 (OUT/'independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
