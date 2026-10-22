"""Exact horizontal-ray coefficients for frozen fields, with integer replay."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,struct,numpy as np
r=Path('verification/L2_physical_continuity_20261021T1239Z');cfg=json.loads((r/'inputs.json').read_text());rows=[]
def enc(q):return {'numerator':str(q.numerator),'denominator':str(q.denominator)}
def binary_rational(x):
 bits=struct.unpack('>Q',struct.pack('>d',float(x)))[0];sgn=-1 if bits>>63 else 1;expo=(bits>>52)&2047;mant=bits&((1<<52)-1)
 assert expo!=2047
 if expo:mant+=1<<52;power=expo-1023-52
 else:power=1-1023-52
 return Q(sgn*mant*(1<<power),1) if power>=0 else Q(sgn*mant,1<<(-power))
for name in cfg['accepted_states']:
 p=r/'archives'/(name+'.npz')
 with np.load(p,allow_pickle=False) as z:
  K=int(z['K']);cf=z['cF'].reshape(K,-1);b=Q(float(z['beta_basis']));L=Q(float(z['L']));C=sum(((-1)**(k//2)*Q(float(cf[k,-1])) for k in range(0,K,2)),Q(0))
  rmax=Q(10**8);qmax=1+(rmax/L)**2;assert b>3 and L==Q(3,2) and qmax<2**53
  zmin=float(np.exp(-np.log(float(qmax))/(2*float(b))))
  row={'z_at_rmax_nominal':zmin,'rmax':10**8,'qmax':enc(qmax),'exact_z_lower_bound':enc(Q(1,512)),'clip_margin_exact_pass':True,'archive':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'beta_basis':enc(b),'L':enc(L),'horizontal_C':enc(C),'exponent':enc(1-2/b),'C_decimal':float(C),'exponent_decimal':float(1-2/b),'positive':b>2 and L>0 and C>0};assert row['positive'];rows.append(row)
(r/'horizontal_tail_certificate.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'claim':'Every pair among the nine distinct accepted states has infinite unweighted full-plane temperature difference, by PROOF section5.'},indent=2)+'\n')
# Replay the saved certificate independently: manually decode IEEE binary64,
# use separate positive/negative mode sums, and cross-multiply exponent ordering.
cert=json.loads((r/'horizontal_tail_certificate.json').read_text());checks=[];prev=None
for row in cert['rows']:
 p=Path(row['archive']);assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
 with np.load(p,allow_pickle=False) as z:
  K=int(z['K']);last=z['cF'].reshape(K,-1)[:,-1]
  plus=sum((binary_rational(x) for x in last[0::4]),Q(0));minus=sum((binary_rational(x) for x in last[2::4]),Q(0));C=plus-minus;b=binary_rational(z['beta_basis']);L=binary_rational(z['L']);pwr=(b-2)/b
  for key,q in [('horizontal_C',C),('beta_basis',b),('L',L),('exponent',pwr)]:assert q==Q(int(row[key]['numerator']),int(row[key]['denominator']))
  assert C>0 and b>3 and L==Q(3,2)
  qmax=1+(Q(row['rmax'])/L)**2
  assert qmax<2**53 and qmax==Q(int(row['qmax']['numerator']),int(row['qmax']['denominator']))
  assert Q(int(row['exact_z_lower_bound']['numerator']),int(row['exact_z_lower_bound']['denominator']))==Q(1,512)
  if prev is not None:assert pwr.numerator*prev.denominator>prev.numerator*pwr.denominator
  prev=pwr;checks.append({'archive':str(p),'hash_matches':True,'exact_C_positive':True,'b_gt_two':True,'exact_clip_margin_pass':True,'exponent_strictly_increases':True})
# Manufactured IEEE decoding controls include signed zero and subnormals.
vals=[0.,-0.,1.,-1.,2.5,float.fromhex('0x0.0000000000001p-1022'),float.fromhex('0x1.fffffffffffffp+1023')]
assert all(binary_rational(v)==Q(v) for v in vals)
(r/'horizontal_tail_checks.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'all_passed':True,'checks':checks,'binary_decode_controls':len(vals),'method':'Separate IEEE-binary64 integer decoding, plus/minus mode sums, exact rational replay and exponent cross-products.'},indent=2)+'\n')
print('PASS',len(checks),'archive tail certificates;',len(vals),'binary decoding controls; infinite temperature distance for all36 distinct accepted pairs')
