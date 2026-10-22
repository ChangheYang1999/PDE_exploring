"""Parse the frozen report table independently and check every advertised endpoint."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import re,json,hashlib
D=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=D/'source/NUM_REPORT_7_10.md';text=p.read_text();raw=json.loads((D/'source/runs/forcing/p9_K64_n16_P8_merged.json').read_text());prior=json.loads((D/'evidence/public_bounds_audit.json').read_text())
number=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
normlines=[x for x in text.splitlines() if x.startswith('| ||tau eps~||') or x.startswith('| N_500')];assert len(normlines)==6
advertised={}
for line,key in zip(normlines,[f'{lam}:{name}' for lam in ['1.0','500.0'] for name in ['bound_order3','bound_order4','bound_order_3_1']]):
 c=line.rsplit('|',3)[-3].replace('*','').strip();assert re.fullmatch(number,c);advertised[key]=F(c)
rows=[x for x in text.splitlines() if re.match(r'^\| \([0-4],[0-4]\)',x)];assert len(rows)==5
for order,row in enumerate(rows):
 fields=row.split('|');assert len(fields)==5
 keys=re.findall(r'\(([0-4]),([0-4])\)',fields[1]);assert len(keys)==order+1 and all(int(a)+int(b)==order for a,b in keys)
 for ball,col in [('B94',fields[2]),('B3',fields[3])]:
  clean=re.sub(r'\([^)]*\)','',col);vals=[v.strip() for v in clean.strip().split(',')];assert len(vals)==len(keys)
  for (a,b),v in zip(keys,vals):assert re.fullmatch(number,v);advertised[f'{ball}:{a}_{b}']=F(v)
assert len(advertised)==36
checks=[]
for c in prior['checks']:
 key=c['label'];assert advertised[key]==F(c['advertised'])
 prefix,name=key.split(':');actual=raw['results'][prefix][name] if prefix in ['1.0','500.0'] else raw['sup_D_eps'][prefix][name]
 exact=F.from_float(actual);assert exact==F(c['raw_exact']);passed=advertised[key]>=exact;assert passed==c['ceiling_above_saved_endpoint']
 checks.append({'label':key,'report_exact':str(advertised[key]),'saved_exact':str(exact),'upward_display':passed})
assert sum(not c['upward_display'] for c in checks)==22
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FROZEN_REPORT_TABLE_BINDING','report_sha256':sha(p),'public_checker_sha256':sha(D/'code/check_public_bounds.py'),'public_audit_sha256':sha(D/'evidence/public_bounds_audit.json'),'parsed_claims':len(advertised),'downward_displays':22,'checks':checks,'scope':'These failures refute upward display of saved endpoints only, not ceilings for the unknown exact functions.'}
(D/'evidence/public_binding.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(advertised),22)
