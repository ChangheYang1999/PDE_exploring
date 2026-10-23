"""Static AST and byte-interval inspection. No producer code execution."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib
V=Path('research/hydrostatic_tail_rule_provenance/verification');checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
d=json.loads((V/'SOURCE_OFFSETS.json').read_text())
for row in d['files']:
 a=Path(row['source']).read_bytes();b=Path(row['frozen']).read_bytes();st,en=row['byte_start_inclusive'],row['byte_end_exclusive'];line=1+a[:st].count(b'\n');count=a.count(b)
 ok=a[st:en]==b and hashlib.sha256(b).hexdigest()==row['frozen_sha256'] and line==row['line_start_one_based'] and count==1
 if not ok:raise ValueError('offset mismatch '+row['source'])
 checks.append(dict(file=row['source'],passed=ok,sha256_now=hashlib.sha256(a).hexdigest(),equals_offset_capture_source_hash=hashlib.sha256(a).hexdigest()==row['current_source_sha256'],byte_start_inclusive=st,byte_end_exclusive=en,source_line_one_based=line,current_occurrence_count=count,bytes_match=True,scope='exact byte interval in source as currently read'))
p=Path('independent_code/q_local_checkpoint.py');text=p.read_text();tree=ast.parse(text);sites={}
for a in ast.walk(tree):
 if isinstance(a,ast.Assign):
  for t in a.targets:
   for z in ast.walk(t):
    if isinstance(z,ast.Attribute)and isinstance(z.value,ast.Name)and z.value.id=='self':sites.setdefault(z.attr,[]).append(dict(line_one_based=z.lineno,statement=ast.get_source_segment(text,a)))
required=['N','M','cl','L','kappa','p']
if not all(z in sites for z in required):raise ValueError('reader attribute assignment absent')
checks.append(dict(name='static reader assignments',required=required,assignment_sites={k:sites[k]for k in required},passed=True,reader_sha256=sha(p)))
files=[__file__,V/'SOURCE_OFFSETS.json',p,V.parent/'STATIC_BINDING_PROOF.md']
bindings={str(Path(p).resolve()):sha(p)for p in files}
out=dict(status='PASS_CURRENT_BYTE_OFFSETS_AND_STATIC_READER_ASSIGNMENTS',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings)
(V/'SOURCE_OFFSET_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(checks))
