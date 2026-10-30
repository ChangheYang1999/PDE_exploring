"""Finite prefix-selection scope check; never execute the producer's selector."""
from pathlib import Path
from datetime import datetime,timezone
import json,gzip,hashlib,re,collections,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def text(s):
 p=B/s;r=p.read_bytes();return (gzip.decompress(r) if p.suffix=='.gz' else r).decode()
def read(s):return json.loads(text(s))
def need(k,v):
 assert v,k
 checks.append(k)
m=read('data/manifest.json')
for p,h in m['inputs'].items():need('binding '+p,sha(B/p)==h)
f=read('data/PROOF_FIRST.json');need('argument first',not f['checker_exists'] and f['proof_sha256']==sha(B/'PROOF.md'))
for row in read('data/initial_sources.json')['rows']:need('decoded source '+row['local'],hashlib.sha256(text(row['local']).encode()).hexdigest()==row['source_sha256'])
s=text('source/T1_check2.py.txt');need('literal preceding240 window','rep[max(0, m.start() - 240):m.start()]' in s)
need('intervening labels filtered',"(PROOF|result|checker|manifest|proof)" in s)
rows=[l.split('\t') for l in text('source/T1_selected_tokens.txt').splitlines() if l];counts=collections.Counter(r[1] for r in rows)
need('exact54saved rows',len(rows)==54)
need('exact partition',dict(counts)=={'MATCH-SAME-NAME':29,'MATCH-OTHER-FILE':10,'NO-MATCH':15})
for i,r in enumerate(rows):need('saved row format '+str(i),len(r)==5 and r[0].isdigit() and re.fullmatch('[a-f0-9]{8,16}',r[3]) is not None)
e=read('data/window_examples.json');flags=[]
for name in ['near','far']:
 v=e[name];pos=v.index(e['token']);window=v[max(0,pos-e['window']):pos];flags.append('THEORY_FINAL' in window)
 need('same explicit filename '+name,'THEORY_FINAL' in v)
 need('same token '+name,v.endswith(e['token']))
need('window counterexample',flags==[True,False])
need('far window has only spaces',set(e['far'][e['far'].index(e['token'])-240:e['far'].index(e['token'])])=={' '})
flat=lambda s:' '.join(s.split())
note=flat(text('source/T1_note75.md'));need('producing lane scope limitation','checks only the 54 hexadecimal tokens' in note and '240 characters' in note and 'wider than note v73' in note)
need('historical draft repair','62' in text('source/T1_note74.md') and '63' in text('source/T1_note74.md'))
r=text('source/report_v183.md.gz');h=hashlib.sha256(r.encode()).hexdigest();need('nominated repaired report',h=='1ee8d6afe69fd431b347d3d11a54b1b40e0c841d9ca55166296aa72d14c78bca' and 'matrix v184' in r[:600])
block=flat('\n'.join(r.splitlines()[2542:2544]));need('repaired finite scope','c1-t1 checked the 54 hash tokens printed after c1-t1 file names' in block and 'wording of T1 team note v75' in block)
need('universal phrase removed','checked every hash prefix of their files' not in r)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'manifest_binding_count':len(m['inputs']),'target_sha256':h,'target_lines':[2543,2544],'selected_rows':len(rows),'saved_tag_counts':dict(counts),'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'verdict':'CONFIRMED finite scope and repaired wording. Rule completeness on arbitrary texts REFUTED; actual exhaustive citation coverage OPEN.','scope':'Two report lines and retained selector/output only. No producer execution or new mathematical claim.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',out['check_count'],'checks',len(m['inputs']),'bindings')
