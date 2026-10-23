from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib
R=Path('research/report84_installation85_prelim_spec63');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();norm=lambda s:' '.join(s.split())
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);d=sha(p);ck('binding '+str(p),h is None or h==d);bindings[str(p)]=d;return p
for p in [Path(__file__),R/'SPEC64_REPAIR_PROOF.md',V/'SPEC64_INPUT.json',V/'spec64_changes.json',V/'CHECKS.json']:bind(p)
base=json.loads((V/'CHECKS.json').read_text());ck('base669 completed',base['count']==669==len(base['checks'])and all(q['passed']for q in base['checks']))
for p,h in base['bindings'].items():bind(p,h)
source=json.loads((V/'SPEC64_INPUT.json').read_text());bind(source['frozen'],source['sha256']);ck('stable64 capture',source['two_reads_equal'])
a=(V/'SPEC63.md').read_text();b=(V/'SPEC64.md').read_text();aa=a.splitlines(keepends=True);bb=b.splitlines(keepends=True);rows=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
 if tag!='equal':rows.append(dict(tag=tag,old=''.join(aa[i:j]),new=''.join(bb[k:l]),old_start=i,new_start=k))
ck('three raw blocks exact',len(rows)==3 and rows==json.loads((V/'spec64_changes.json').read_text()));restored=b
for i,row in enumerate(rows):ck('unique reverse block '+str(i),restored.count(row['new'])==1);restored=restored.replace(row['new'],row['old'],1)
ck('whole reverse equality64to63',restored==a)
ck('header edit only',rows[0]['new'].replace('v64, 2026-10-22T01:37Z','v63, 2026-10-22T01:27Z')==rows[0]['old'])
repair=base['required_spec_repair'];newclause=repair['new'][:-1]+' (checker 307 repair).'
ck('required exact finite/noncausal repair',norm(rows[1]['old']).replace(repair['old'],newclause)==norm(rows[1]['new']))
ck('old causal claim gone',repair['old']not in b)
ck('single changelog insertion',rows[2]['tag']=='insert'and rows[2]['new'].startswith('- v64 2026-10-22T01:37Z:')and rows[2]['new'].count('- v')==1)
ck('changelog accurately scoped','accurate-map solves compare finite-state differences; neither convergence nor causation established'in norm(rows[2]['new']))
ck('pending arithmetic remains','checker 292 pending'in norm(b)and 'would give d >= 25, P >= 27/2'in b)
ck('no allnode upgrade','Not checked: all-node maxima'in norm(b)and 'producer map matrices (unexported)'in norm(b))
ck('observation afterversion',datetime.fromisoformat(source['utc'])>datetime.fromisoformat('2026-10-22T01:37:00+00:00'))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_SCOPED_SPEC_REPAIR_PENDING_FINAL_REVIEW',count=len(checks),checks=checks,bindings=bindings,SPEC64_sha256=sha(V/'SPEC64.md'),scope='Required307 repair installed in observedSPEC64. Three whole-file changed blocks only. No new mathematical theorem, degree23OPEN, primaryUNRESOLVED.')
(V/'SPEC64_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
