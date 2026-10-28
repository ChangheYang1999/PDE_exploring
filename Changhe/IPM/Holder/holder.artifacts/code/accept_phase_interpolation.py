"""Second arithmetic audit for unequal phase interpolation; no optimizer."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib,re,argparse
R=Path(__file__).resolve().parents[1];B=R/'08_improved_upper_bounds/phase_interpolation'
M=R/'08_improved_upper_bounds/middle_circle_transport/balanced_residual'
L=R/'08_improved_upper_bounds/local_disk_transport/balanced_residual'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def upper(a):return Q(str(a.upper().fmpq()))
def lower(a):return Q(str(a.lower().fmpq()))
def endupper(s):
 if not s.startswith('['):return Q(s)
 m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s);assert m
 return sum(map(Q,m.groups()))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);ap.add_argument('--cross-read',required=True);a=ap.parse_args()
 cross=(R/a.cross_read).resolve();assert cross.is_relative_to(R) and cross.is_file()
 d=load(B/'verification/independent_audit.json');hashes={}
 def bind(p):hashes[str(p.relative_to(R))]=sha(p)
 for name,h in d['sha256'].items():assert sha(R/name)==h,name;bind(R/name)
 for p,v in [(M/'verification/accepted.json','V168'),(M/'table37/verification/accepted.json','V171')]:
  ac=load(p);assert ac['verdict']=='CONFIRMED' and ac['ledger']==v
  for name,h in ac['sha256'].items():assert sha(R/name)==h,name;bind(R/name)
 mid=load(M/'verification/independent_audit.json');extra=load(M/'table37/verification/independent_audit.json')
 small={r['alpha']:Q(r['small_upper']) for r in load(L/'existing_certificates/verification/independent_audit.json')['rows']}
 near={r['alpha']:endupper(r['near_D']) for r in load(R/'data/middle_composite_upper_n512.json')['rows']}
 sources={}
 for r in mid['rows']:
  for op in ['C','D']:sources[(r['alpha'],op)]=(list(map(Q,r[op+'_phase_upper'])),small[r['alpha']] if op=='C' else near[r['alpha']],r['safe_upper_'+op])
 for r in extra['rows']:sources[(r['alpha'],'C')]=(list(map(Q,r['phase_upper'])),small[r['alpha']],r['safe_upper_C'])
 assert len(sources)==len(d['rows'])==14
 ctx.prec=768;delta=arb.pi()/32;c=delta.cos();s=delta.sin();cl=lower(c);outrows=[]
 for r in d['rows']:
  key=(r['alpha'],r['operator']);u,S,old=sources.pop(key)
  assert list(map(Q,r['phase_upper']))==u and Q(r['uniform_part'])==S and r['previous_upper']==old
  fresh=[]
  for j,p in enumerate(r['intervals']):
   assert p['index']==j and Q(p['left'])==u[j] and Q(p['right'])==u[j+1]
   U,V=arb(str(u[j])),arb(str(u[j+1]))
   if u[j+1]<=u[j]*cl:q=u[j]
   elif u[j]<=u[j+1]*cl:q=u[j+1]
   else:
    b=(V-U*c)/s
    amp=(U*U+b*b).sqrt()
    sec=arb(str(max(u[j],u[j+1])))/(delta/2).cos()
    q=min(upper(amp),upper(sec))
   assert q<=Q(p['certified_upper']),(key,j)
   fresh.append(q)
  assert len(fresh)==16
  stored=[Q(p['certified_upper']) for p in r['intervals']]
  assert r['worst_interval']==max(range(16),key=lambda j:stored[j])
  assert Q(r['regular_upper'])==max(stored) and Q(r['complete_upper'])==S+max(stored)
  safe=Q(r['safe_upper']);assert S+max(fresh)<=Q(r['complete_upper'])<=safe<Q(r['complete_upper'])+Q(1,10**10)
  assert safe<=Q(old) and Q(r['decimal_improvement'])==Q(old)-safe
  outrows.append(dict(alpha=r['alpha'],operator=r['operator'],safe_upper=r['safe_upper'],previous_upper=old,worst_interval=r['worst_interval']))
 assert not sources
 for p in [B/'verification/independent_audit.json',B/'PROOF.md',B/'numerical_values/PROOF.md',cross,Path(__file__)]:bind(p)
 text=cross.read_text();assert sha(B/'PROOF.md') in text and 'no error' in text.lower()
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=a.ledger,verdict='CONFIRMED',precision_bits=768,rows=outrows,
  method='Independent cosine-sine amplitude recomputation, endpoint checks, source-array equality, exact maximum and final upward rounding',
  independent_cross_read=str(cross.relative_to(R)),sha256=hashes)
 (B/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],a.ledger,'CONFIRMED',outrows)
if __name__=='__main__':main()
