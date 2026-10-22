from pathlib import Path
from fractions import Fraction as F
from flint import fmpq
import json,hashlib,re
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[3];D=R/'research/resolution_aggregate_audit';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dec(t):
 t=t.strip().lower();sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,sep,e=t.partition('e');a,dot,b=m.partition('.');return fmpq(sign*int(a+b))*fmpq(10)**((int(e) if sep else 0)-len(b))
A=json.loads((E/'check.json').read_text());B=json.loads((E/'independent.json').read_text());table={}
for line in (D/'source/NUM_REPORT.md').read_text().splitlines():
 if line.startswith('| '):
  row=[v.strip() for v in line.strip('|').split('|')]
  if len(row)==5 and row[0] in [r+' cells (r range)' for r in ['middle','outer','inner']]:table[row[0].split()[0]]=row[1:]
checks=[]
for ti,tag in enumerate(['','v3_h0.004','v4_M230','v5_R0knot2']):
 for region in ['middle','outer','inner']:
  text=table[region][ti];tokens=re.search(r'\[([^,]+),([^\]]+)\]',text).groups()
  for side,token in zip(['left','right'],tokens):
   d=F(token);dd=dec(token);assert str(d)==str(dd)
   ab=A['regions'][tag][region]['nominal_domain'][side];bb=B['regions'][tag][region]['nominal_domain'][side]
   al,au=F(ab['lo']),F(ab['hi']);bl,bu=fmpq(bb['lo']),fmpq(bb['hi'])
   if side=='left':
    status='OUTWARD_NOMINAL_LABEL' if d<=al else 'INWARD_NOMINAL_LABEL' if d>au else 'AMBIGUOUS'
    other='OUTWARD_NOMINAL_LABEL' if dd<=bl else 'INWARD_NOMINAL_LABEL' if dd>bu else 'AMBIGUOUS'
   else:
    status='OUTWARD_NOMINAL_LABEL' if d>=au else 'INWARD_NOMINAL_LABEL' if d<al else 'AMBIGUOUS'
    other='OUTWARD_NOMINAL_LABEL' if dd>=bu else 'INWARD_NOMINAL_LABEL' if dd<bl else 'AMBIGUOUS'
   assert status==other and status!='AMBIGUOUS'
   checks.append({'tag':tag,'region':region,'side':side,'display_token':token.strip(),'status':status})
assert len(checks)==24 and sum(c['status']=='INWARD_NOMINAL_LABEL' for c in checks)==15
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_24_NOMINAL_DOMAIN_LABEL_CLASSIFICATION','code_sha256':sha(Path(__file__)),'primary_sha256':sha(E/'check.json'),'independent_sha256':sha(E/'independent.json'),'source_sha256':sha(D/'source/NUM_REPORT.md'),'endpoints_checked':24,'inward':15,'outward':9,'checks':checks,'scope':'All12 printed ranges checked against both nominal endpoint enclosures. These are approximate labels, not a physical coverage certificate. Enlarging a label does not prove a bound on the newly included region.'}
with (E/'domain_displays.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(out['status'],out['inward'],'inward',out['outward'],'outward')
