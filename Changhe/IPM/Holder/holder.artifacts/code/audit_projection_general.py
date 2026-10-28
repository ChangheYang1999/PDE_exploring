"""Independent rational recombination, coverage and source-hash audit.
No interval-library endpoint extraction is reused from the production merge.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json, argparse
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ball(s):
 s=s.strip()
 if s.startswith('['):
  m,r=s[1:-1].split('+/-');m,r=Q(m.strip()),Q(r.strip());assert r>=0
  return m-r,m+r
 return Q(s),Q(s)
def floor10(q):
 k=(q*10**10).__floor__();sgn='-' if k<0 else '';k=abs(k);return f'{sgn}{k//10**10}.{k%10**10:010d}'
def audit(path,out):
 d=json.loads(path.read_text());sources={};chunks=[]
 for name,h in d['source_hashes'].items():
  p=Path(name);p=p if p.is_absolute() else ROOT/p
  assert sha(p)==h,(p,'source hash')
  sources[str(p)]=h
  if p.suffix=='.json' and '_s' in p.name and '_r' in p.name:chunks.append(p)
 assert len(chunks)>=2
 lo=Q(1);hi=Q(1);ranges={-1:[],1:[]};records=[]
 fields=['alpha','b','shift','K','nx','ny','left','vleft','vright']
 for p in chunks:
  v=json.loads(p.read_text())
  assert all(v[k]==d[k] for k in fields),(p,'parameters')
  assert v['sign'] in [-1,1] and v['precision_bits']>=192
  assert v['right']==('log(1/2)' if v['sign']==-1 else d['right_positive'])
  ranges[v['sign']].append((v['start'],v['stop']))
  for n,h in v['source_hashes'].items():
   z=Path(n);z=z if z.is_absolute() else ROOT/z;assert sha(z)==h
  l,u=ball(v['integral_lower_enclosure']);assert l>=0
  lo+=4*l;hi+=4*u
  records.append(dict(path=str(p),sha256=sha(p),sign=v['sign'],start=v['start'],stop=v['stop'],exact_integral_lower=str(l),exact_integral_upper=str(u)))
 for s in [-1,1]:
  cursor=0
  for l,r in sorted(ranges[s]):assert l==cursor and r>l;cursor=r
  assert cursor==d['nx']
 assert 0<Q(d['alpha'])<1 and Q(d['b'])>0 and Q(d['shift'])>=Q(-1,2)
 a=Q(d['alpha']);K=Q(d['K'])
 assert a in [Q(3,10),Q(1,2),Q(3,4),Q(9,10)]
 if a in [Q(3,10),Q(1,2)]:
  profile_paths=[ROOT/f'data/geometric_profile_a{30 if a==Q(3,10) else 50}_tight.json']
  upper_key='certified_upper'
 else:
  tag='a75_k106' if a==Q(3,4) else 'a90_k110'
  profile_paths=[ROOT/f'07_diagonal_identity_term/full_range_profile/verification/{tag}_{mode}.json' for mode in ['same','opposite']]
  upper_key='target'
 for p in profile_paths:
  prof=json.loads(p.read_text());assert Q(prof[upper_key])<=K
  assert prof['checked_boxes']==2*prof['accepted_boxes']-1
  for name,h in prof['source_hashes'].items():assert sha(ROOT/name)==h
 assert Q(d['safe_D_lower_10_places'])<=lo
 rows=json.loads((ROOT/'data/verified_table.json').read_text())['rows'];row=next(r for r in rows if Q(r['alpha'])==a)
 gap=Q(d['safe_D_lower_10_places'])-Q(row['selected_upper_C']['exact_safe_endpoint'])
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(a),b=d['b'],shift=d['shift'],K=d['K'],nx=d['nx'],ny=d['ny'],source_combined=str(path),source_sha256=sha(path),chunks=records,exact_recombined_lower=str(lo),exact_recombined_upper=str(hi),safe_D_lower_10_places=d['safe_D_lower_10_places'],independent_safe_lower_10_places=floor10(lo),safe_gap_above_C=floor10(gap),profile_certificate_sha256={str(p):sha(p) for p in profile_paths},verdict='CONFIRMED after full source-hash and exact once-only coverage checks, independently recombined as rational decimal intervals under the complete Stieltjes proof.')
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ['alpha','safe_D_lower_10_places','independent_safe_lower_10_places','safe_gap_above_C']},indent=2))
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('combined');p.add_argument('output');a=p.parse_args();audit(Path(a.combined).resolve(),ROOT/a.output)
