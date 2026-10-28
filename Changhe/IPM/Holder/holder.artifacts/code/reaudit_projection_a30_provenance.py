"""Rebind V099 to immutable local inputs after an upstream summary rewrite."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/projection_lead_a30'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def interval(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 x,r=map(Q,m.groups());assert r>=0
 return x-r,x+r

def main():
 oldpath=BASE/'verification/independent_audit.json';old=load(oldpath)
 combined=Path(old['source_combined']);d=load(combined)
 assert d['safe_D_lower_10_places']==old['safe_D_lower_10_places']
 for k in ['alpha','b','shift','K','nx','ny']:assert d[k]==old[k]
 dest=BASE/'source_frozen_0945';dest.mkdir(exist_ok=True)
 frozen={};dependencies={};coverage={-1:[],1:[]};lo=Q(0);hi=Q(0)
 def freeze(p):
  target=dest/(sha(p)[:12]+'_'+p.name)
  if target.exists():assert target.read_bytes()==p.read_bytes()
  else:target.write_bytes(p.read_bytes())
  frozen[str(target.relative_to(ROOT))]=sha(target)
  return target
 for entry in old['chunks']:
  p=Path(entry['path']);assert sha(p)==entry['sha256'];c=load(p)
  for k in ['alpha','b','shift','K','nx','ny']:assert c[k]==old[k]
  for k in ['sign','start','stop']:assert c[k]==entry[k]
  assert c['left']=='-18' and c['right']==('24' if c['sign']==1 else 'log(1/2)')
  assert c['vleft']=='-12' and c['vright']=='14'
  a,b=interval(c['integral_lower_enclosure'])
  assert a==Q(entry['exact_integral_lower']) and b==Q(entry['exact_integral_upper'])
  lo+=a;hi+=b;coverage[c['sign']].append((c['start'],c['stop']))
  for name,h in c['source_hashes'].items():
   dependency=Path(name);assert sha(dependency)==h
   dependencies[name]=h;freeze(dependency)
  freeze(p)
 for sign,pairs in coverage.items():
  cursor=0
  for a,b in sorted(pairs):assert a==cursor and b>a;cursor=b
  assert cursor==old['nx']
 lo=1+4*lo;hi=1+4*hi
 assert lo==Q(old['exact_recombined_lower']) and hi==Q(old['exact_recombined_upper'])
 assert Q(d['safe_D_lower_10_places'])<=lo
 combined_interval=interval(d['included_D_lower_enclosure'])
 assert combined_interval[0]<=lo<=hi<=combined_interval[1]
 profile=ROOT/'data/geometric_profile_a30_tight.json'
 assert sha(profile)==old['profile_certificate_sha256'];freeze(profile)
 localcombined=freeze(combined)
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',ledger='V133',
  mathematical_verdict='V099 unchanged',old_summary_sha256=old['source_sha256'],
  current_summary_sha256=sha(combined),old_audit_sha256=sha(oldpath),
  exact_recombined_lower=str(lo),exact_recombined_upper=str(hi),safe_D_lower=old['safe_D_lower_10_places'],
  unchanged_chunk_count=len(old['chunks']),checked_dependencies=dependencies,
  sha256={**frozen,str(oldpath.relative_to(ROOT)):sha(oldpath),str(Path(__file__).relative_to(ROOT)):sha(Path(__file__))},
  explanation='All eight original chunk hashes and component intervals are unchanged. Exact rational recombination reproduces V099. The regenerated external summary is no longer a live dependency; the frozen copy is bound here.')
 out=BASE/'verification/provenance_reaudit.json';out.write_text(json.dumps(result,indent=2)+'\n')
 registry=ROOT/'data/accepted_external_D.json';r=load(registry)
 for row in r['entries']:
  if row['alpha']=='3/10':
   row.update(audit='V099, provenance V133',audit_path=str(out.relative_to(ROOT)),audit_sha256=sha(out),source_path=str(localcombined),source_sha256=sha(localcombined))
 r['time_utc']=result['time_utc'];registry.write_text(json.dumps(r,indent=2)+'\n')
 print(result['time_utc'],result['unchanged_chunk_count'],result['safe_D_lower'],result['verdict'])
if __name__=='__main__':main()
