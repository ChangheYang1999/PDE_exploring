"""Freeze and independently recombine a complete v7 positive-sum certificate.

All decimal balls are read as exact rational intervals. The output is a
structural/recombination audit; independent geometric replay is separate.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
EXPECTED='69fdc727589ea9c0c472e523f6b2d3edbf67d9f13776ef69dd48199d684dbfaa'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ball(text):
 text=text.strip()
 if not text.startswith('['):return Q(text),Q(text)
 m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',text);assert m,text
 x,r=map(Q,m.groups());assert r>=0;return x-r,x+r

def floor10(q):
 k=(q*10**10).__floor__();return f'{k//10**10}.{k%10**10:010d}'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('plan');ap.add_argument('--out',required=True)
 args=ap.parse_args();planpath=Path(args.plan).resolve();dest=(ROOT/args.out).resolve()
 assert dest.is_relative_to(ROOT);dest.mkdir(parents=True,exist_ok=True)
 plan=json.loads(planpath.read_text());source=planpath.parent.parent/'verification'
 prefix=plan['prefix'];frozen={};sources={};records=[];total=[Q(0),Q(0)]
 def freeze(path):
  h=sha(path);target=dest/'frozen'/(h[:12]+'_'+path.name);target.parent.mkdir(exist_ok=True)
  if target.exists():assert sha(target)==h
  else:target.write_bytes(path.read_bytes())
  frozen[str(target.relative_to(ROOT))]=h;return target
 freeze(planpath)
 for i,p in enumerate(plan['pieces']):
  assert p['sign'] in (-1,1) and p['nx']>0 and p['ny']>0 and p['chunk']>0
  assert Q(p['vleft'])<Q(p['vright'])
  if p['right'] is not None:assert Q(p['left'])<Q(p['right'])
  if p['sign']==-1:
   # All explicit negative-side endpoints are at most -1 < log(1/2).
   assert p['right'] is None or Q(p['right'])<=-1
  cursor=0
  while cursor<p['nx']:
   end=min(cursor+p['chunk'],p['nx']);path=source/f'{prefix}_s{p["sign"]}_p{i}_r{cursor}_{end}.json'
   d=json.loads(path.read_text())
   for key in ('alpha','b','shift','K'):assert Q(d[key])==Q(plan[key])
   for key in ('sign','nx','ny','left','vleft','vright'):assert d[key]==p[key]
   assert d['start']==cursor and d['stop']==end and d['precision_bits']>=192
   assert d['right']==(p['right'] if p['right'] is not None else ('log(1/2)' if p['sign']==-1 else '24'))
   assert 0<=d['positive_cells']<=(end-cursor)*p['ny']
   assert set(d['rule_counts'])=={'v2','v4','mv','mv2','ref'}
   assert all(type(v) is int and v>=0 for v in d['rule_counts'].values())
   assert sum(d['rule_counts'].values())==d['positive_cells']
   for name,h in d['source_hashes'].items():
    dependency=Path(name);assert sha(dependency)==h,(name,'changed')
    if dependency.name=='cert_v7.py':assert h==EXPECTED
    sources[name]=h;freeze(dependency)
   lo,hi=ball(d['integral_lower_enclosure']);assert 0<=lo<=hi
   assert Q(d['safe_partial_D_lower'])<=1+4*lo
   total[0]+=lo;total[1]+=hi;local=freeze(path)
   records.append(dict(piece=i,start=cursor,stop=end,path=str(local.relative_to(ROOT)),
                       sha256=sha(local),integral_lower=str(lo),integral_upper=str(hi),
                       rules=d['rule_counts']))
   cursor=end
 # Domain overlap checks use the original exact log-coordinate endpoints.
 for sign in (-1,1):
  pieces=sorted((Q(p['left']),p['right']) for p in plan['pieces'] if p['sign']==sign)
  for (left,right),(nextleft,nextright) in zip(pieces,pieces[1:]):
   assert right is not None and Q(right)<=nextleft
 alpha,K=Q(plan['alpha']),Q(plan['K']);assert 0<alpha<1 and Q(plan['b'])>0 and Q(plan['shift'])>=Q(-1,2)
 if alpha in (Q(1,20),Q(1,10),Q(1,5)):
  profile=ROOT/'data/profile_constant_certificate.json';d=json.loads(profile.read_text())
  row,=[v for v in d['rows'] if Q(v['alpha'])==alpha]
  assert K>=Q(row['safe_upper']) and Q(row['epsilon'])>0
 elif alpha==Q(3,10):
  profile=ROOT/'data/geometric_profile_a30_tight.json';d=json.loads(profile.read_text())
  assert K>=Q(d['certified_upper']) and d['checked_boxes']==2*d['accepted_boxes']-1
 else:raise AssertionError('Unsupported profile certificate')
 for name,h in d['source_hashes'].items():
  p=ROOT/name;assert sha(p)==h;freeze(p)
 freeze(profile)
 lower,upper=1+4*total[0],1+4*total[1]
 combined=source/(prefix+'_combined.json');merged=json.loads(combined.read_text())
 ml,mu=ball(merged['included_D_lower_enclosure']);assert ml<=lower<=upper<=mu
 assert Q(merged['safe_D_lower_10_places'])<=lower
 frozen_combined=freeze(combined)
 for key in ('alpha','b','shift','K'):assert Q(merged[key])==Q(plan[key])
 assert merged['pieces']==plan['pieces'] and merged['chunks']==len(records)
 proof=ROOT/'05_team_audit/stieltjes_v7/PROOF.md';freeze(proof)
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),
  verdict='STRUCTURAL CHECKS PASS; geometric replay and final acceptance are separate',
  alpha=str(alpha),K=str(K),chunks=records,exact_D_lower=str(lower),exact_D_upper=str(upper),
  safe_D_lower=floor10(lower),producer_safe_D_lower=merged['safe_D_lower_10_places'],
  producer_combined=str(frozen_combined.relative_to(ROOT)),source_hashes=sources,
  frozen_sha256=frozen,auditor_sha256=sha(Path(__file__)),
  provenance_scope='cert_v7 hash observed during production in V135; formal pre-launch hash for a20 not supplied')
 (dest/'independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ('time_utc','alpha','safe_D_lower','producer_safe_D_lower','verdict')},indent=2))

if __name__=='__main__':main()
