from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,gzip,os
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/weighted_tail_candidate_review';src=BASE/'source'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
p=src/'MANIFEST.json';old=json.loads(p.read_text());out=src/'MANIFEST_v02.json';assert not out.exists()
reuses={'006':'research/candidate_audits/data/C1-N1-006-8branch-e2/canonical.json','008':'research/candidate_audits/data/C1-N1-008-d2w-j7-x3bal/canonical.json','009':'research/candidate_audits/data/C1-N1-009-d2w-j7-x3balk/canonical.json','012':'research/candidate_audits/data/C1-N1-012-e2balk1e7-from009/canonical.json','013':'research/factored_monomial_audit/source/T4_canonical.json','014':'research/candidate_audits/reviews/T4_014/source/new_successor_weak/data/014/canonical.json'}
retired=[];new=dict(old['files'])
for n,rel in reuses.items():
 key=f'T4_{n}_canonical.json.gz';record=old['files'][key];dest=ROOT/rel
 assert sha(dest)==record['sha256']
 with gzip.open(src/key,'rb') as f:assert sha256(f.read()).hexdigest()==record['sha256']
 fresh=f'T4_{n}_canonical.json';link=src/fresh;assert not link.exists();link.symlink_to(os.path.relpath(dest,src));assert sha(link)==record['sha256']
 new.pop(key);new[fresh]={**record,'gzip':False,'frozen_sha256':record['sha256'],'frozen_bytes':dest.stat().st_size,'reused_existing_file':rel}
 (src/key).unlink();retired.append({'former_name':key,'former_frozen_sha256':record['frozen_sha256'],'bytes_saved':record['frozen_bytes'],'reused':rel,'uncompressed_sha256':record['sha256']})
with out.open('x') as f:json.dump({'utc':datetime.now(timezone.utc).isoformat(),'files':new,'foreign_code_executed':False,'prior_manifest_sha256':sha(p),'retired_nonaccepted_duplicate_encodings':retired,'code_sha256':sha(Path(__file__))},f,indent=2);f.write('\n')
print('DEDUP',sum(r['bytes_saved'] for r in retired),'manifest',sha(out))
