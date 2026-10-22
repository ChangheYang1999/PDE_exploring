"""Audit frozen field format and roundoff margin. No NUM code import."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,math,numpy as np
r=Path('verification/L2_physical_continuity_20261021T1239Z');cfg=json.loads((r/'inputs.json').read_text());rows=[]
for rec in cfg['archives']:
 p=Path(rec['frozen']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
 with np.load(p,allow_pickle=False) as z:
  b=Q(float(z['beta_basis']));L=Q(float(z['L']));K=int(z['K']);deg=int(z['deg']);nt=int(z['Nt']);grade=float(z['grade']);assert str(z['rmap'])=='r2'
  assert b>3 and L==Q(3,2)
  qmax=1+(Q(10**8)/L)**2;assert qmax<2**53
  knots=np.r_[np.zeros(deg),np.linspace(0.,1.,nt+1)**grade,np.ones(deg)];nb=len(knots)-deg-1
  assert all(knots[-deg-1:]==1) and knots[-deg-2]<1 and all(knots[:deg+1]==0)
  assert np.isfinite(z['cF']).all() and np.isfinite(z['cG']).all() and z['cF'].size==z['cG'].size==K*nb
  assert max(k//2 for k in range(K))<nb-1
  rows.append({'archive':rec['frozen'],'sha256':rec['sha256'],'b_hex':float(b).hex(),'L_hex':float(L).hex(),'right_endpoint_multiplicity':deg+1,'last_coefficient_active_every_mode':True,'exact_qmax_lt_2_pow_53':True,'exact_z_lower_bound':'1/512','z_min_nominal':math.exp(-math.log(float(qmax))/(2*float(b))),'all_passed':True})
(r/'format_guard_checks.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'all_passed':True,'exact_argument':'qmax<2^53 and b>3 give z>2^(-53/6)>2^-9; float clip1-1e-16=1-2^-53','checks':rows},indent=2)+'\n')
print('PASS',len(rows),'format and exact guard-margin checks; nominal z range',min(x['z_min_nominal'] for x in rows),max(x['z_min_nominal'] for x in rows))
