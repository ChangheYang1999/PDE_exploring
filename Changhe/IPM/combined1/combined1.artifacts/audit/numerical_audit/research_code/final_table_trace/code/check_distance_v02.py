"""Direct source edges and exact principal-distance displays, no integration."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction as Q
import gzip,json,re,time
R=Path(__file__).resolve().parents[3];B=R/'research/final_table_trace'
def now():return datetime.now(timezone.utc).isoformat()
def ball(s):
 m=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',s);assert m,s
 c,e=map(Q,m.groups());assert e>=0;return c-e,c+e

def main():
 start=time.monotonic();cache={};observed={};edges=[];errors=[];inputs={}
 def signature(p):
  s=p.stat();return(s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns)
 def digest(p,decoded=False):
  p=Path(p);p=p if p.is_absolute() else R/p;p=p.resolve(strict=True);assert p.is_relative_to(R)
  sig=signature(p);key=(str(p),decoded,sig)
  if key not in cache:
   h=sha256()
   with (gzip.open(p,'rb') if decoded else p.open('rb')) as f:
    while chunk:=f.read(1048576):h.update(chunk)
   assert signature(p)==sig;cache[key]=h.hexdigest()
  observed[str(p)]=sig;return cache[key]
 def check(owner,kind,p,expected,decoded=False):
  row={'owner':owner,'kind':kind,'path':str(p),'expected_sha256':expected,'decoded_gzip':decoded}
  try:
   assert isinstance(expected,str) and re.fullmatch('[a-f0-9]{64}',expected)
   row['actual_sha256']=digest(p,decoded);row['pass']=row['actual_sha256']==expected
   if not row['pass']:row['error']='digest mismatch'
  except Exception as e:row['pass']=False;row['error']=str(e)
  edges.append(row)
  if not row['pass']:errors.append(row)
  return row['pass']
 def bind(p,expected=None):
  p=Path(p);p=p if p.is_absolute() else R/p;h=digest(p)
  if expected:assert h==expected,(str(p),h,expected)
  inputs[str(p.relative_to(R))]=h;return json.loads(p.read_text()) if p.suffix=='.json' else p.read_text()
 def direct(owner,d):
  for key in ['inputs','own_inputs','frozen_sources']:
   for p,h in d.get(key,{}).items():check(owner,key,p,h)
  for p,e in d.get('frozen_or_retained_sources',{}).items():
   if isinstance(e,str):check(owner,'retained_peer',p,e)
   else:
    check(owner,'stored_peer',p,e['stored_sha256'])
    if e.get('gzip'):check(owner,'decoded_peer',p,e['sha256'],True)
    elif e['sha256']!=e['stored_sha256']:errors.append({'owner':owner,'path':p,'error':'plain peer original/stored disagreement'})
 contract=bind(B/'source/distance_contract_v01.json','356ab63f08690755728ca9a53be5b5ce4afe99cc99d336b53244cac727183820')
 prepared=bind(B/'verification/DISTANCE_PROOF_FIRST_v01.json','e343d965585b30d336dca6c8869b9a019068f6e9026106cfe0054e21ea271cf7');assert not prepared['checker_exists']
 bind(B/'DISTANCE_PROOF.md','79eb425091c77f09f8ebb19a56c0db49a475ec4af491bfb92816cedba6d0d335');bind(Path(__file__).resolve())
 bind(B/'DISTANCE_PROOF_v02.md','1dc8284fc54d24ed1fff21d3c4349aee7731d87247e5d1ca815cf47547880e19')
 bind(B/'code/check_distance_v01.py','45c61a8363394cf36d2e3c65f9618478f3464c855d75751b8585035b93c98f8a')
 bind('logs/final_distance_v01.out','76c4034442312c32fdda38f25e762746e5e06cf44207b1eb22f409ee7ad82fca')
 trace=bind(B/'verification/documentary_v02.json','b808c527961fa59c769486ea2db25e0a2af7f4edf0df9b032d5735095175f97c')
 ledger=bind(B/'source/N4_VERIFY_REPORT_v01.md','e8e425491ee404a14c754522e0032a8a358cfefcf3b8a52b064ff72ab381f3ce')
 summary=bind(B/'source/N4_AUDIT_SUMMARY_v01.md','d99b7001ff575590b27fded3772ffbd1486f4acfadd163e0950a59e87e2bd54a')
 budgets=bind('research/theory_v07_review/verification/result.json')
 assert inputs['research/theory_v07_review/verification/result.json'] in ledger
 # These exact ceilings are already accepted in N4-335. Bind their literal
 # existing records; this script does not rederive the Sobolev embeddings.
 ceiling_strings=set(re.findall(r'"ceiling_exact": "([^"]+)"',json.dumps(budgets)))
 assert set(contract['comparison_ceilings'].values())<=ceiling_strings
 transfer=bind('research/candidate015_three_weak_peer/verification/cap_transfer_v01.json','68c78c8e4e21d20463d5958c183d7630c4c48b98a531fc2b71fc0c2fd7439a0e')
 assert all(transfer['checks'].values());direct('N4-383 sharper-cap transfer',transfer)
 bind('research/candidate015_three_weak_peer/CAP_TRANSFER_PROOF.md','b832a34f9198923fd0ed04544a8d013f519de0e91bb6c3e57e6dc4c6d6f55c10')
 table={x['row']:x for x in trace['trace']};results=[];failures=[];ratios=[]
 for e in contract['entries']:
  owner=e['claim'];root_info=e['accepted_result'];assert root_info['sha256'] in ledger,(owner,'root hash absent from frozen ledger')
  check(owner,'accepted_root',root_info['path'],root_info['sha256']);root=json.loads((R/root_info['path']).read_text());direct(owner,root)
  original=e['original_result'];check(owner,'original_result',original['path'],original['sha256']);orig=json.loads((R/original['path']).read_text())
  if original['path']!=root_info['path']:direct(owner+' original',orig)
  for kind in ['proof','immutable_manifest','immutable_raw']:
   q=e[kind];check(owner,kind,q['path'],q['sha256'])
  man=json.loads((R/e['immutable_manifest']['path']).read_text());assert man['id']==e['candidate'];assert man['c_l_exact']==e['c_exact']=='4076476460239181/2251799813685248'
  assert man['coefficient_files'][0]['sha256']==e['immutable_raw']['sha256']
  bridge=None
  recorded_inputs=[(key,p,h) for d in (root,orig) for key in ('inputs','own_inputs') for p,h in d.get(key,{}).items()]
  direct_raw_paths=[{'map':key,'path':p} for key,p,h in recorded_inputs if h==e['immutable_raw']['sha256']]
  canonical_paths=[]
  if e['canonical_bridge']:
   q=e['canonical_bridge'];check(owner,'canonical_bridge',q['path'],q['sha256']);bridge=json.loads((R/q['path']).read_text())
   assert bridge['generator_sha256']==e['immutable_raw']['sha256']
   canonical_paths=[{'map':key,'path':p} for key,p,h in recorded_inputs if h==bridge['canonical_sha256']]
  raw_connected=bool(direct_raw_paths or canonical_paths)
  assert raw_connected,(owner,'neither direct raw nor audited canonical input is connected')
  for q in e['independent_records']:
   check(owner,'independent_record',q['path'],q['sha256'])
   if q.get('gzip'):check(owner,'independent_decoded',q['path'],q['decoded_sha256'],True)
   if e['number'] in (9,12):assert q['sha256']==root['rows'][e['accepted_row_index']]['peer_sha256']
   if e['number'] in (10,14):assert q['sha256']==root['peer_result_sha256']
  if e['number'] in (9,12):
   mp=Path(root_info['path']).parent/'MANIFEST.json';check(owner,'peer_manifest',mp,root['manifest_sha256']);md=json.loads((R/mp).read_text())
   for name,row in md['files'].items():check(owner,'peer_manifest_file',mp.parent/name,row['sha256'])
  ri=e['accepted_row_index'];ar=root if ri is None else root['rows'][ri];floor=Q(ar[e['accepted_floor_key']]);assert floor==Q(e['accepted_floor'])
  q=e['radius_record'];check(owner,'radius_record',q['path'],q['sha256']);rd=json.loads((R/q['path']).read_text());ri=e['radius_row_index'];rr=rd if ri is None else rd['rows'][ri];lo,hi=ball(rr[e['radius_key']]);assert 0<floor<lo
  display=Q(e['report_principal_strict_floor']);sr=table[e['report_primary_row']];literal=re.search(r'>\s*'+re.escape(e['report_principal_strict_floor'])+r'(?![0-9])',sr['report']['text']) is not None;assert literal,(owner,'display not found')
  summ=Q(e['own_summary_floor']);summary_literal=re.search(r'^\|\s*0*'+str(e['number'])+r'\s*\|\s*>\s*'+re.escape(e['own_summary_floor'])+r'\s*\|',summary,re.M) is not None
  assert summary_literal and summ<=floor,(owner,'own summary floor issue')
  comparison='supported by accepted floor' if display<=floor else ('above accepted root upper; not supported by this certificate' if display>hi else 'between accepted floor and root; separate endpoint comparison needed')
  accepted_display=display<=floor or display<lo
  r={'claim':owner,'candidate':e['candidate'],'accepted_result_sha256':root_info['sha256'],'raw_sha256':e['immutable_raw']['sha256'],'probe':e['probe'],'floor':str(floor),'root_interval':[str(lo),str(hi)],'own_summary_floor':str(summ),'own_summary_floor_supported':True,'report_row':e['report_primary_row'],'report_display':str(display),'report_display_supported':accepted_display,'display_comparison':comparison,'raw_source_connected':raw_connected,'direct_raw_inputs':direct_raw_paths,'canonical_inputs':canonical_paths,'connection_used':'direct raw' if direct_raw_paths else 'audited canonical','independent_records':e['independent_records']}
  if not accepted_display:failures.append(r)
  results.append(r)
  for rn in [e['report_primary_row'],e['report_primary_row']+1]:
   text=table[rn]['report']['text']
   for m in re.finditer(r'(\d+(?:\.\d+)?) times the (sharpw family|graded)(?: ceiling| budget)',text):
    b=Q(contract['comparison_ceilings']['sharpw_upper' if m[2]=='sharpw family' else 'graded']);printed=Q(m[1]);ratios.append({'candidate':e['candidate'],'report_row':rn,'literal':m[0],'exact_lower_ratio':str(floor/b),'printed_factor':str(printed),'supported':printed<=floor/b})
 for p,sig in observed.items():
  if signature(Path(p))!=sig:errors.append({'path':p,'error':'changed during check'})
 checks={'nineteen_candidates':len(results)==19,'all_accepted_floors_strict':all(Q(x['floor'])<Q(x['root_interval'][0]) for x in results),'all_own_summary_floors_supported':all(x['own_summary_floor_supported'] for x in results),'all_selected_distance_ratio_displays_supported':all(x['supported'] for x in ratios),'two_strict_display_defects':{x['report_row'] for x in failures}=={80,90},'all_direct_edges_match':not errors}
 result={'utc':now(),'inputs':inputs,'checks':checks,'results':results,'unsupported_principal_displays':failures,'selected_ratios':ratios,'direct_edge_count':len(edges),'unique_resolved_files':len(observed),'decoded_streams':sum(k[1] for k in cache),'edges':edges,'errors':errors,'scope':contract['scope'],'integration_repeated':False,'foreign_files_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED stated accepted-source and directed-display checks' if all(checks.values()) else 'OPEN inspect explicit source or display findings'}
 out=B/'verification/distance_v02.json'
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'utc':result['utc'],'checks':checks,'edges':len(edges),'unique':len(observed),'ratios':len(ratios),'errors':errors,'result_sha256':digest(out),'elapsed_seconds':result['elapsed_seconds']},indent=2))
if __name__=='__main__':main()
