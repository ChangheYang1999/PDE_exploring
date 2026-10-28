"""Merge of cert_v7.py chunks for one plan (several disjoint log-d pieces per sign). Checks: common alpha, b, shift, K;
one certifier source; source hashes unchanged; in each piece exact once-only coverage of its nx strips with equal grid
parameters; for each sign the pieces [left, right] are disjoint (rational endpoints; the default sign -1 right end is
log(1/2), every explicit sign -1 right end is <= log(1/2)); a certified profile constant K >= [P]_alpha (the same
registry as combine_lead.py). Output: verification/{prefix}_combined.json with D >= 1 + 4 * (sum of the chunk lower sums)."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib,re
from flint import arb,ctx
ctx.prec=256;HERE=Path(__file__).resolve().parent;VER=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def safe(v):
 n=int((arb(v.lower())*10**10).floor().unique_fmpz());return f'{n//10**10}.{n%10**10:010d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('plan');a=p.parse_args();plan=json.loads(Path(a.plan).read_text());prefix=plan['prefix']
 folder=HERE/'verification';paths=sorted(q for q in folder.glob(prefix+'_s*_p*_r*.json'));assert paths
 total=arb(0);sources={str(Path(a.plan).resolve()):sha(a.plan)};pieces={};counts={}
 for path in paths:
  m=re.fullmatch(re.escape(prefix)+r'_s(-?1)_p(\d+)_r(\d+)_(\d+)\.json',path.name);assert m,path.name
  d=json.loads(path.read_text());k=int(m.group(2));q=plan['pieces'][k]
  assert [d['alpha'],d['b'],d['shift'],d['K']]==[str(F(plan[x])) for x in ['alpha','b','shift','K']]
  assert d['sign']==q['sign']==int(m.group(1)) and d['nx']==q['nx'] and d['ny']==q['ny'] and d['precision_bits']>=192
  assert d['left']==q['left'] and d['vleft']==q['vleft'] and d['vright']==q['vright'] and (d['start'],d['stop'])==(int(m.group(3)),int(m.group(4)))
  assert d['right']==(q['right'] if q['right'] is not None else ('log(1/2)' if q['sign']==-1 else '24'))
  cov=pieces.setdefault(k,[0]*d['nx'])
  for i in range(d['start'],d['stop']):cov[i]+=1
  for name,h in d['source_hashes'].items():assert sha(name)==h,(name,'source changed');sources[name]=h
  sources[str(path)]=sha(path);v=arb(d['integral_lower_enclosure']);assert v>=0;total+=v
  for r,c in d['rule_counts'].items():counts[r]=counts.get(r,0)+c
 assert set(pieces)==set(range(len(plan['pieces'])))
 for cov in pieces.values():assert cov==[1]*len(cov)
 for s in [1,-1]:
  iv=sorted((F(q['left']),q['right']) for q in plan['pieces'] if q['sign']==s)
  for (l1,r1),(l2,r2) in zip(iv,iv[1:]):assert r1 is not None and F(r1)<=l2
  for l,r in iv:
   if s==-1 and r is not None:assert arb(F(r).numerator)/F(r).denominator<=(arb(1)/2).log()
   assert r is None or l<F(r)
 certs=sorted({Path(n).name for n in sources if Path(n).name.startswith('cert_')});assert certs==['cert_v7.py']
 alpha=F(plan['alpha']);K=F(plan['K'])
 if alpha in [F(3,10),F(1,2)]:
  tag='30' if alpha==F(3,10) else '50';p=VER/f'data/geometric_profile_a{tag}_tight.json';cert=json.loads(p.read_text());assert K>=F(cert['certified_upper']);assert cert['checked_boxes']==2*cert['accepted_boxes']-1
  for name,h in cert['source_hashes'].items():assert sha(VER/name)==h;sources[str(VER/name)]=h
  sources[str(p)]=sha(p)
 elif alpha in [F(3,4),F(9,10)]:
  tag='a75_k106' if alpha==F(3,4) else 'a90_k110'
  for mode in ['same','opposite']:
   p=VER/f'07_diagonal_identity_term/full_range_profile/verification/{tag}_{mode}.json';cert=json.loads(p.read_text());assert K>=F(cert['target']);assert cert['checked_boxes']==2*cert['accepted_boxes']-1
   for name,h in cert['source_hashes'].items():assert sha(VER/name)==h;sources[str(VER/name)]=h
   sources[str(p)]=sha(p)
 elif alpha==F(1,5):
  p=VER/'data/profile_constant_certificate.json';cert=json.loads(p.read_text());(row,)=[r for r in cert['rows'] if F(r['alpha'])==alpha]
  assert K>=F(row['safe_upper']) and F(row['epsilon'])>0
  for name,h in cert['source_hashes'].items():assert sha(VER/name)==h;sources[str(VER/name)]=h
  sources[str(p)]=sha(p)
 else:raise AssertionError('No audited profile certificate registered for this exponent')
 value=1+4*total;sources[str(Path(__file__).resolve())]=sha(Path(__file__))
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),method='stieltjes',certifier='cert_v7.py',alpha=str(alpha),b=plan['b'],shift=plan['shift'],K=str(K),pieces=plan['pieces'],chunks=len(paths),rule_counts=counts,included_D_lower_enclosure=value.str(55,more=True),safe_D_lower_10_places=safe(value),source_hashes=sources,verdict='Lead computation; positive lower sum under the standalone proof; awaiting verifier audit.')
 (folder/(prefix+'_combined.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['alpha','safe_D_lower_10_places','included_D_lower_enclosure','rule_counts']},indent=2))
if __name__=='__main__':main()
