"""Anchor actual accepted regional evidence before new whole-plane arithmetic."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/global_residual_second'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={}
def pin(p,h=None):
 n=str(p.relative_to(B));actual=sha(p);check(h is None or h==actual,'source pin '+n);check(n not in pins or pins[n]==actual,'conflicting pin');pins[n]=actual;return actual
oldp=B/'research/global_residual_assembly/evidence/verdict.json';fullp=B/'research/middle_second/evidence/full_q16_verdict.json';old=load(oldp);full=load(fullp)
pin(oldp,'5e451a9a8e03564044539f9c292a76c55c35b11dead58d918501b496af798d93');pin(fullp)
check(old['status']=='CONFIRMED_PRIMARY_ONLY_WHOLE_PLANE_ZEROTH_RESIDUAL_ASSEMBLY','accepted old global');check(full['status']=='CONFIRMED_COMPLETE_INDEPENDENT_MIDDLE_RESIDUAL_SHARED_CANONICAL_INPUTS' and (full['cells'],full['spans'])==(7809,1558),'actual full second method')
for obj in [old,full]:
 for n,h in obj['files'].items():pin(B/n,h)
required=['data_exact/modal_v2.json','research/global_residual_assembly/evidence/primary_assembly_v2.json','research/middle_second/evidence/full_q16_summary.json','research/middle_second/evidence/full_q16_output_audit.json','notes/middle_full_closure/result.json','notes/middle_full_closure/POSTREVIEW_ADJUDICATION.md']
for n in required:check(n in pins,'required inherited path '+n)
check(pins['data_exact/modal_v2.json']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6','same exact trial')
a=load(B/required[1]);s=load(B/required[2]);r=load(B/required[4]);h=s['run_header'];k=F(1615536043799051,9007199254740992);L=F(8614738245908811,1125899906842624)
check((F(a['k_exact']),F(a['L_exact']))==(k,L)==(F(h['k_exact']),F(h['L_exact'])),'same parameters');joins=[F(-685794559684773,140737488355328),F(2289893859708677,281474976710656)];check(list(map(F,a['joins_exact']))==joins,'original joins')
for i,reg in enumerate(['inner','outer']):check(F(h['region_boundary_joins'][reg]['log_radius_exact'])==F(a['regions'][reg]['region_join_log_radius_exact'])==joins[i] and a['regions'][reg]['full_tail'] is True,'same regional join and tail')
check((a['regions']['inner']['cells'],a['regions']['middle']['cells'],a['regions']['outer']['cells'])==(54,7809,89),'region counts');check(a['regions']['middle']['parents']==1558 and [F(a['regions']['middle'][q]) for q in ['first_log_radius_exact','last_log_radius_exact']]==joins,'old middle cover');check(s['source_footer_read'] is True and r['archive_footer_read_by_this_checker'] is True,'actual footers');check(full['maxima']==s['maxima']==r['maxima'] and full['L2_squared_upper_exact']==s['L2_squared_upper_exact']==r['L2_squared_upper_exact'],'actual middle aggregates')
proof=load(D/'evidence/proof_first.json');check(proof['proof_sha256']==sha(D/'PROOF.md'),'proof-first bytes');check(datetime.fromisoformat(proof['utc'])<datetime.now(timezone.utc),'prior proof')
for p in [D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/proof_first.json',Path(__file__)]:pin(p)
for n,hsh in pins.items():check(sha(B/n)==hsh,'final inherited digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ACTUAL_ACCEPTED_FULL_MIDDLE_AND_REGIONAL_INPUTS','k_exact':str(k),'L_exact':str(L),'joins_exact':list(map(str,joins)),'old_global_verdict_sha256':sha(oldp),'actual_full_middle_verdict_sha256':sha(fullp),'cells':{'inner':54,'middle':7809,'outer':89},'files':dict(sorted(pins.items())),'scope':'Preparation only. Same canonical archive dependency; no new global arithmetic or endpoint.'}
with (D/'data_exact/manifest.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins)}))
