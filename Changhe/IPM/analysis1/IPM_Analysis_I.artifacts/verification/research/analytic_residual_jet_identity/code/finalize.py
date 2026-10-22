from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
reviews=[]
expected=[('analytic_residual_jets_complete','b069641d-9e51-484f-b47d-d9297d0e0d57','91ed3a38c5dcb4bb793ad6ebb9076c1960070f07d52c1b1f68fb5f2d73da232a'),('analytic_residual_jets_followup','50b23fc3-c603-4b79-8e5e-a41caa332dce','0b80ae103430356c3cbc3a71bb580a6425fb14280be6be95934e5fb0d276f0e7')]
for tag,rid,digest in expected:
 m=json.loads((BASE/f'notes/reviews/{tag}_metadata.json').read_text());raw=json.loads((BASE/f'notes/reviews/{tag}_response.json').read_text());text=(BASE/f'notes/reviews/{tag}_response.md').read_text();req=BASE/f'notes/reviews/{tag}_request.txt'
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and m['request_id']==rid
 assert sha(req)==m['input_sha256']==digest
 assert text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 assert [s for s in text.splitlines() if s.startswith('VERDICT:')]==['VERDICT: CONFIRM_ANALYTIC_JET_IDENTITIES_AND_LITERAL_SCALARS']
 assert req.read_text().endswith('\n\n'.join('FILE '+f+'\n'+(BASE/f).read_text() for f in m['files']))
 reviews.append(m)
post=json.loads((ROOT/'evidence/postreview_record.json').read_text());assert post['status']=='CONFIRMED_AFTER_READING_BOTH_ACTUAL_REVIEWS'
assert post['adjudication_sha256']==sha(ROOT/'POSTREVIEW_ADJUDICATION.md')
assert post['reviews']==[{'request_id':m['request_id'],'input_sha256':m['input_sha256'],'response_sha256':sha(BASE/f'notes/reviews/{tag}_response.json')} for m,(tag,_,_) in zip(reviews,expected)]
assert datetime.fromisoformat(post['utc'])>max(datetime.fromisoformat(m['end_utc']) for m in reviews)
C=json.loads((ROOT/'evidence/check.json').read_text());S=json.loads((ROOT/'evidence/scalars.json').read_text());contract=json.loads((ROOT/'evidence/index_contract.json').read_text())
assert C['status']=='PASS_EXACT_LAURENT_VERSUS_SOURCE_JETS' and S['status']=='PASS_LITERAL_SCALARS_ONLY'
assert (C['dense_comparisons'],C['basis_pairs'],C['basis_entries'])==(10350,80,1104)
assert C['source_sha256']==sha(ROOT/'sources/xnorm_jets.py')
assert len(S['square_root_windows'])==5 and all(x['exact_square_check'] for x in S['square_root_windows'])
for p,h in contract['source_sha256'].items():
 assert sha(BASE/p)==h
 if p.endswith('.py'):assert sha(ROOT/'sources'/Path(p).name)==h
for p,h in json.loads((ROOT/'data_exact/scalar_sources.json').read_text())['sources'].items():assert sha(ROOT/'sources'/Path(p).name)==h
assert datetime.fromisoformat(reviews[0]['start_utc'])>max(datetime.fromisoformat(C['utc']),datetime.fromisoformat(S['utc']))
files={str(p.relative_to(BASE)):sha(p) for p in ROOT.rglob('*') if p.is_file() and p.name!='verdict.json'}
for tag,_,_ in expected:
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=BASE/f'notes/reviews/{tag}_{suffix}';files[str(p.relative_to(BASE))]=sha(p)
files['../ipmA-num/data/trial_v2_h0.008.npz']=sha(BASE/'../ipmA-num/data/trial_v2_h0.008.npz')
verdict={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ANALYTIC_JET_IDENTITIES_AND_LITERAL_SCALARS','dense_exact_comparisons':10350,'complete_small_basis_pairs':80,'basis_entries':1104,'literal_square_root_windows':S['square_root_windows'],'reviews':reviews,'files':dict(sorted(files.items())),'scope':'Analytic identities for C3 finite modal fields with the stated polar convention; exact synthetic source-algebra checks and literal saved-scalar arithmetic. Default source/input index contract only. No physical jet linkage, quadrature enclosure, historical runtime identity, nonzero-t floating error, omitted tails, global norm/C bound, inverse or IPM endpoint.'}
p=ROOT/'evidence/verdict.json';assert not p.exists();p.write_text(json.dumps(verdict,indent=2)+'\n');print(json.dumps({'utc':verdict['utc'],'status':verdict['status'],'pins':len(files),'sha256':sha(p)}))
