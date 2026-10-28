"""Lead copy of the verification work code/combine_projection_lower.py: coverage, hash and profile-certificate
audit for projection-cusp lower sums computed in this folder. Only the paths differ: chunk files are
read from ./verification, all hashes are keyed by absolute path, and the profile certificates are read
from the verifier's data (read only)."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib
from flint import arb,ctx
ctx.prec=256;HERE=Path(__file__).resolve().parent;VER=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def safe(v):
 n=int((arb(v.lower())*10**10).floor().unique_fmpz());return f'{n//10**10}.{n%10**10:010d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('prefix');a=p.parse_args()
 folder=HERE/'verification';paths=sorted(folder.glob(a.prefix+'_s*.json'));assert paths
 paths=[q for q in paths if not q.name.endswith('_combined.json')]
 expected=None;coverage={};total=arb(0);sources={};parts=[]
 fields=['alpha','b','shift','K','nx','ny','left','vleft','vright']
 for path in paths:
  d=json.loads(path.read_text());key=tuple(d[x] for x in fields);expected=key if expected is None else expected;assert key==expected
  assert d['sign'] in [-1,1] and d['precision_bits']>=192
  cov=coverage.setdefault(d['sign'],[0]*d['nx']);assert 0<=d['start']<d['stop']<=d['nx']
  for i in range(d['start'],d['stop']):cov[i]+=1
  for name,h in d['source_hashes'].items():assert sha(name)==h,(name,'source changed');sources[name]=h
  sources[str(path)]=sha(path);parts.append(d);v=arb(d['integral_lower_enclosure']);assert v>=0;total+=v
 assert set(coverage)=={-1,1}
 for cov in coverage.values():assert cov==[1]*len(cov)
 assert len({d['right'] for d in parts if d['sign']==1})==1
 assert {d['right'] for d in parts if d['sign']==-1}=={'log(1/2)'}
 alpha=F(parts[0]['alpha']);K=F(parts[0]['K'])
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
 cert=sorted({Path(n).name for d in parts for n in d['source_hashes'] if Path(n).name.startswith('cert_')});assert len(cert)==1
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),method='stieltjes',certifier=cert[0],alpha=str(alpha),b=parts[0]['b'],shift=parts[0]['shift'],K=str(K),nx=parts[0]['nx'],ny=parts[0]['ny'],left=parts[0]['left'],right_positive=next(d['right'] for d in parts if d['sign']==1),right_negative='log(1/2)',vleft=parts[0]['vleft'],vright=parts[0]['vright'],included_D_lower_enclosure=value.str(55,more=True),safe_D_lower_10_places=safe(value),source_hashes=sources,verdict='Lead computation; positive lower sum under the standalone proof; awaiting verifier audit.')
 (folder/(a.prefix+'_combined.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['alpha','safe_D_lower_10_places','included_D_lower_enclosure']},indent=2))
if __name__=='__main__':main()
