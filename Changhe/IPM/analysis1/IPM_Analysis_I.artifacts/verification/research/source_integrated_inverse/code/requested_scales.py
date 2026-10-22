"""Exact outward display of the lead's V32 scales from both audited engines."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
B=Path(__file__).resolve().parents[3];D=B/'research/source_integrated_inverse';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=E/'checks.json';c=json.loads(p.read_text());a=json.loads((E/'output_audit.json').read_text())
assert a['status']=='PASS_THIRD_EXACT_QUADRATURE_AND_FRESH_OUTPUT_AUDIT'
assert a['files'][str(p.relative_to(B))]==sha(p)
lookup={e:{(r['s'],r['ell']):r for r in c['results'][e]['rows']} for e in ('arb','iv')}
def ceiling(x):
 assert x>0
 exponent=0
 while x>=F(10)**(exponent+1):exponent+=1
 while x<F(10)**exponent:exponent-=1
 step=F(10)**(exponent-5);n=x//step+1;v=n*step
 assert x<v
 # Six significant digits, shown as an exact decimal times a power of ten.
 return v, f'{n//100000}.{n%100000:05d}e{exponent}'
rows=[]
for s in ('153/50','31/10'):
 for ell in ('33/2000','1/100','1/200','7/2000','1/500'):
  entry={'s':s,'ell':ell,'ceilings':{}}
  for key in ('R','N_inverse','H_inverse'):
   ups=[F(lookup[e][(s,ell)]['bounds'][key][1]) for e in ('arb','iv')]
   v,text=ceiling(max(ups));assert F(text)==v
   entry['ceilings'][key]={'strict_ceiling_exact':str(v),'display':text,'maximum_audited_upper_exact':str(max(ups))}
  rows.append(entry)
files={str(x.relative_to(B)):sha(x) for x in (p,E/'output_audit.json',Path(__file__))}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_OUTWARD_REQUESTED_SCALE_TABLE','rows':rows,'strict_ceiling_checks':30,'files':files}
(E/'requested_scales.json').write_text(json.dumps(out,indent=2)+'\n')
text='''# Requested V32 scales

These are strict outward ceilings from the maximum of the two independently
audited interval upper endpoints. The calculation uses exact rational
comparisons and six significant decimal digits. The columns are R^*,
B_N=(1+R^*/d^*)^s/a^* in N_(1/ell), and B_H=ell^(-s)B_N in Hs.
They bound the same topic95 compact C4 auxiliary operator, using the
unchanged conservative a^*,d^* of PROOF. No physical rank-one term,
localized residual, outer matching or nonlinear closure is included.
The finite scale table is not a global optimization certificate.

| s | ell | R^* < | N inverse < | Hs inverse < |
|---|---|---|---|---|
'''
for r in rows:
 text+='| '+('3.06' if r['s']=='153/50' else '3.1')+' | '+r['ell']+' | '+' | '.join(r['ceilings'][k]['display'] for k in ('R','N_inverse','H_inverse'))+' |\n'
text+='\nSee evidence/requested_scales.json for every exact comparison and input hash.\n'
(D/'REQUESTED_SCALES.md').write_text(text)
print(text)
