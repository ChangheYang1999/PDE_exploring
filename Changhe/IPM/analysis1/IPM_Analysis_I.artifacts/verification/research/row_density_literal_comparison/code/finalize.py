from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,os
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1];TAG='row_density_literal_complete'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
meta=json.loads((BASE/f'notes/reviews/{TAG}_metadata.json').read_text());rawpath=BASE/f'notes/reviews/{TAG}_response.json';raw=json.loads(rawpath.read_text())
request=BASE/f'notes/reviews/{TAG}_request.txt';text=(BASE/f'notes/reviews/{TAG}_response.md').read_text()
assert meta['requested_model']=='us.anthropic.claude-opus-5-5' and meta['actual_response_model']==raw['model']=='claude-opus-5-5'
assert meta['stop_reason']==raw['stop_reason']=='end_turn' and meta['request_id']=='15380932-e7a0-4cc4-8220-db8ff2768f82'
assert sha(request)==meta['input_sha256']=='ead11bc1f5a9e8474669b6bc9c6b04f52dbdd79cd0ca9f1f0d49ef4a43fea79a'
assert text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
assert [s for s in text.splitlines() if s.startswith('VERDICT:')]==['VERDICT: CONFIRM_LITERAL_ROW_DENSITY_COMPARISONS']
suffix='\n\n'.join('FILE '+f+'\n'+(BASE/f).read_text() for f in meta['files']);assert request.read_text().endswith(suffix)
post=json.loads((ROOT/'evidence/postreview_record.json').read_text())
assert post['request_id']==meta['request_id'] and post['input_sha256']==meta['input_sha256'] and post['raw_response_sha256']==sha(rawpath)
assert post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING' and post['adjudication_sha256']==sha(ROOT/'POSTREVIEW_ADJUDICATION.md')
assert datetime.fromisoformat(post['utc'])>datetime.fromisoformat(meta['end_utc'])
manifest=json.loads((ROOT/'data_exact/manifest.json').read_text());pins={}
for rel,h in manifest['sources'].items():
 p=BASE.parent/rel;assert sha(p)==h;pins[os.path.relpath(p,BASE)]=h
for rel,h in manifest['copied'].items():assert sha(BASE/rel)==h
check=json.loads((ROOT/'evidence/check.json').read_text());audit=json.loads((ROOT/'evidence/audit.json').read_text())
assert check['status']=='PASS_LITERAL_COMPARISONS' and audit['status']=='PASS_INDEPENDENT_IEEE_FMPQ_AND_RAW_NPY'
assert check['comparisons']==audit['comparisons']==40 and check['array_comparisons']==audit['array_comparisons']==228
assert check['payload_bytes']==audit['payload_bytes']==2508480
assert datetime.fromisoformat(meta['start_utc'])>datetime.fromisoformat(audit['utc'])
for p in ROOT.rglob('*'):
 if p.is_file() and p.name!='verdict.json':pins[str(p.relative_to(BASE))]=sha(p)
for suffix in ['metadata.json','request.txt','response.json','response.md']:
 p=BASE/f'notes/reviews/{TAG}_{suffix}';pins[str(p.relative_to(BASE))]=sha(p)
verdict=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_LITERAL_ROW_DENSITY_COMPARISONS',comparisons=40,nonzero=40,maxima=check['maxima'],selected_array_comparisons=228,selected_payload_bytes=2508480,opaque_metadata_files=3,actual_review=meta,files=dict(sorted(pins.items())),scope='Exact arithmetic on sixty saved binary64 entries, forty changes, eight maxima; byte-identical selected inputs and saved counts only. No exact retained subspace, singular-minimum certification, continuous norms, convergence, inverse or IPM endpoint.')
p=ROOT/'evidence/verdict.json';assert not p.exists();p.write_text(json.dumps(verdict,indent=2)+'\n');print(json.dumps({'utc':verdict['utc'],'pins':len(pins),'verdict_sha256':sha(p),'status':verdict['status']}))
