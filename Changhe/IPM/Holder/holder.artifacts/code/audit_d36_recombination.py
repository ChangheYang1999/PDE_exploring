"""Recombine accepted middle, cross and exterior bounds independently."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
import argparse, hashlib, json, re
R=Path(__file__).resolve().parents[1]
B=R/'05_team_audit/d36_recombination';T=R/'05_team_audit/table37_lead'
M=R/'08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification'
P=R/'08_improved_upper_bounds/phase_interpolation/verification/accepted.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def uq(x):return Q(str(x.upper().fmpq()))
def lq(x):return Q(str(x.lower().fmpq()))
def upper(s):
 if not s.startswith('['):return Q(s)
 m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s);assert m,s
 return sum(map(Q,m.groups()))
def ceil10(x):
 k=-((-x*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);args=ap.parse_args();hashes={}
 def bind(p):assert p.is_relative_to(R);hashes[str(p.relative_to(R))]=sha(p)
 for p,v in [(T/'verification/accepted.json','V131'),(M/'accepted.json','V171'),(P,'V177')]:
  d=load(p);assert d['verdict']=='CONFIRMED' and d['ledger']==v;bind(p)
  for name,h in d['sha256'].items():assert sha(R/name)==h,name;bind(R/name)
 submitted=load(B/'source/d36.json')
 for name,h in submitted['source_sha256'].items():
  p=Path(name)
  if '/the lead work/scratch/table37/' in name:p=T/'source'/name.split('/the lead work/scratch/table37/',1)[1]
  elif '/the lead work/scratch/d36/' in name:p=B/'source'/p.name
  assert p.is_relative_to(R) and sha(p)==h,name;bind(p)
 base={r['alpha']:r for r in load(T/'verification/independent_audit.json')['rows']}
 middle={r['alpha']:r for r in load(M/'independent_audit.json')['rows']}
 crosspath=R/'data/cross_disk_certificate.json';farpath=R/'data/far_circle_certificate_fine.json'
 cross={r['alpha']:r for r in load(crosspath)['rows']};far={r['alpha']:r for r in load(farpath)['rows']}
 rows=[]
 for sub in submitted['rows']:
  a=sub['alpha'];A=Q(a);r=base[a];g=middle[a]
  gains=list(map(Q,g['accepted_gains']))
  assert gains==[max(Q(0),Q(x)-Q(y)) for x,y in zip(g['old_source_lower'],g['new_residual_upper'])]
  W=[Q(z['upper'])-v for z,v in zip(r['middle'],gains)]
  X=list(map(upper,cross[a]['cross_phase_intervals']))
  E=[min(Q(z['upper']),upper(s)) for z,s in zip(r['far'],far[a]['far_phase_intervals'])]
  U=[w+x+e for w,x,e in zip(W,X,E)];assert len(U)==17 and all(v>=0 for v in U)
  assert all(v<=Q(s) for v,s in zip(U,sub['phase_values']))
  worst=max(range(17),key=lambda j:U[j]);assert worst==sub['worst_phase']
  ctx.prec=384;aa=arb(a);pi=arb.pi();d=pi/32;c=d.cos();s=d.sin();cl=lq(c)
  near=arb(2)**(1-aa)*((aa+2)/2).gamma()/(2*pi.sqrt()*((aa+3)/2).gamma())/aa+arb(1)/2
  S=uq(near);sec=uq(near+arb(str(max(U)))/(pi/64).cos())
  assert ceil10(sec)==sub['safe_upper_D']
  H=[]
  for u,v in zip(U,U[1:]):
   if v<=u*cl:q=u
   elif u<=v*cl:q=v
   else:
    uu,vv=arb(str(u)),arb(str(v));amp=(uu*uu+vv*vv-2*uu*vv*c).sqrt()/s
    q=min(uq(amp),uq(arb(str(max(u,v)))/(d/2).cos()))
   H.append(q)
  total=S+max(H);safe=ceil10(total)
  assert Q(safe)<=Q(sub['pending_interpolated_D_upper']),(a,safe,sub['pending_interpolated_D_upper'])
  ctx.prec=768;AA=arb(a);pp=arb.pi();dd=pp/32;cc=dd.cos();ss=dd.sin();cll=lq(cc)
  n2=arb(2)**(-AA)*((AA+2)/2).gamma()/(pp.sqrt()*((AA+3)/2).gamma()*AA)+arb(1)/2
  assert uq(n2)<=S
  H2=[]
  for u,v,h in zip(U,U[1:],H):
   if v<=u*cll:q=u
   elif u<=v*cll:q=v
   else:
    uu,vv=arb(str(u)),arb(str(v));b=(vv-uu*cc)/ss
    q=min(uq((uu*uu+b*b).sqrt()),uq(arb(str(max(u,v)))/(dd/2).cos()))
   assert q<=h;H2.append(q)
  assert uq(n2)+max(H2)<=total<=Q(safe)<total+Q(1,10**10)
  rows.append(dict(alpha=a,safe_upper_D=safe,secant_upper_D=sub['safe_upper_D'],producer_interpolated_upper_D=sub['pending_interpolated_D_upper'],uniform_part=str(S),phase_upper=list(map(str,U)),interval_upper=list(map(str,H)),worst_node=worst,worst_interval=max(range(16),key=lambda j:H[j])))
 for p in [T/'verification/independent_audit.json',M/'independent_audit.json',crosspath,farpath,B/'PROOF.md',Path(__file__)]:bind(p)
 for p in (B/'source').iterdir():
  if p.is_file():bind(p)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',precision_bits=[384,768],rows=rows,sha256=hashes,method='Exact rational recombination of accepted V131/V171 middle data with existing cross and exterior endpoints; independent high precision phase interpolation check')
 (B/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['time_utc'],args.ledger,'CONFIRMED')
 for r in rows:print(r['alpha'],r['secant_upper_D'],r['safe_upper_D'])
if __name__=='__main__':main()
