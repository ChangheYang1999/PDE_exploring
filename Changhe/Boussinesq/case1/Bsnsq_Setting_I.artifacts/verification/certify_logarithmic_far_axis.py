"""Exact horizontal far-field necessary coefficient for frozen source tuples.
No teammate code imports; exact Fraction endpoint sums and exp enclosure.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json,datetime,hashlib
import numpy as np
OUT=Path('research/logarithmic_far_compatibility/verification');OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
PINNED={'J48':('9bce8206006c6541a460045691580ef09c63d7e3952b0e1dcf4de913ed4bfca0','ba92a946fc1a7a66b7968d424e0f43ceafb09887bccca17b4a9c18be924a2a29'),'scaledJ64':('bd3cb33cd7b2649db5a6d64af6863fb93371bcb40a8dfb7bc7281661c410fe4c','946bb66448cc43f648b2f38d0719bfb9233b9be87948292426b61a8badb0e510')}
ALLOWED=set('c a0 J Kw m beta hist Nt Ns tmin gauge alpha se gam l'.split())
def endpoint(n,d):
 if d==0:return F((-1)**n)
 if d==1:return F(2*(-1)**(n+1)*n*n)
 if d==2:return F(4*(-1)**n*n*n*(n*n-1),3)
 raise ValueError(d)
def interval(q):return dict(exact=[str(v) for v in q],approximate=[float(v) for v in q])
def scaled(q,k):return tuple(sorted(k*v for v in q))
def coefficient(p,s,alpha):
 p00,p01,p10,p11,p20,p21=[p[k] for k in [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]]
 h=F(5,3)*p00
 if h<=0:raise ValueError('Nonpositive far horizontal chart')
 # c1=1,c2=alpha/2 extracts coefficient of c1^2.
 A=-p10/h;B=(p10*p01/h**4-p11/h**3)/s**2;g=F(2,9)*A-6*B
 k0=(alpha*p10+p20)/2;k1=(alpha*p11+p21)/2
 L=-2*k0+F(4,3)*p10**2/h
 M=(-2*k1+F(14,3)*p10*p11/h-4*p10**2*p01/h**2)/s**2
 C1=L/h;D1=-L*p01/(s**2*h**4)+M/h**3
 return h,-F(2,9)*C1+6*D1+2*A*g
N=100;lo=sum(F(3**k,factorial(k)) for k in range(N+1));hi=lo+F(3**(N+1),factorial(N+1))/(1-F(3,N+2))
c1=((1-1/lo)/3,(1-1/hi)/3);c1sq=(c1[0]**2,c1[1]**2)
report=dict(start_utc=now(),script_sha256=sha(__file__),exp3=interval((lo,hi)),c1_squared=interval(c1sq),rows=[],scope='Exact stored dyadic tuple with beta3,alpha3,gam0; global chart supplied by separate source-pinned replay. Only a necessary scalar far-field condition, no nearby-solution or broad nonexistence conclusion.')
for label,source in [('J48','candidate_audits/lead_snap48/sources/snap_J48K26.npz'),('scaledJ64','candidate_audits/lead_scaled64/sources/frzA_sc2_J64K34.npz')]:
 source=Path(source)
 if sha(source)!=PINNED[label][0]:raise ValueError('Source changed')
 with np.load(source,allow_pickle=False) as z:
  if set(z.files)-ALLOWED:raise ValueError('Unsupported source fields')
  if not (float(z['beta'])==3 and int(z['m'])==3 and float(z['alpha'])==3):raise ValueError('Unsupported parameters')
  if 'gam' in z.files and float(z['gam'])!=0:raise ValueError('Unsupported angular map')
  for key in ['c','a0','alpha','se']:
   if key in z.files and (z[key].dtype!=np.dtype('float64') or not np.all(np.isfinite(z[key]))):raise ValueError('Expected finite binary64 '+key)
  c=z['c'].reshape(int(z['J'])+1,int(z['Kw'])+1);a=F.from_float(float(z['a0']));s=F.from_float(float(z['se'])) if 'se' in z.files else F(1)
 if s<=0 or a==0:raise ValueError('Degenerate source')
 p={(i,j):sum(F.from_float(float(c[n,k]))*endpoint(n,i)*endpoint(k,j) for n in range(c.shape[0]) for k in range(c.shape[1])) for i,j in [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]}
 hc=sum(F.from_float(float(c[n,k]))*(-1)**k for n in range(c.shape[0]) for k in range(c.shape[1]))
 ptc=sum(F.from_float(float(c[n,k]))*2*n*n*(-1)**k for n in range(c.shape[0]) for k in range(c.shape[1]))
 qc=sum(F.from_float(float(c[n,k]))*2*(-1)**(k+1)*k*k for n in range(c.shape[0]) for k in range(c.shape[1]))/s**2
 ell=(-(hi-1)/18,-(lo-1)/18);pc0=scaled(ell,ptc);pc=(pc0[0]+hc/3,pc0[1]+hc/3)
 if hc<=0 or pc[0]<=0<=pc[1]:raise ValueError('Cannot divide by center p')
 reciprocal=tuple(sorted(1/v for v in pc));correction=scaled(reciprocal,14*qc/hc);acenter=(70*hc+correction[0],70*hc+correction[1])
 h,K=coefficient(p,s,F(3));forcing=2*a/(3*h);terms=scaled(c1sq,K);value=(terms[0]+forcing,terms[1]+forcing);target=scaled(c1sq,-3*h*K/2)
 chart=source.parent.parent/'chart_certificate/replay.json'
 if sha(chart)!=PINNED[label][1]:raise ValueError('Reviewed replay changed')
 cr=json.loads(chart.read_text())
 if F(cr['delta'])<=0 or cr['manufacture_mode']:raise ValueError('Nonpositive or manufactured chart certificate')
 for file,digest in cr['hashes'].items():
  if sha(file)!=digest:raise ValueError('Chart dependency changed: '+file)
 if cr['status']!='CONFIRMED' or cr['pinned_source_sha256']!=sha(source):raise ValueError('Missing matching global chart')
 row=dict(label=label,source=str(source),source_sha256=sha(source),chart_replay_sha256=sha(chart),delta=cr['delta'],p={str(k):str(v) for k,v in p.items()},s=str(s),a=str(a),h=str(h),K=str(K),forcing=str(forcing),F_axis=interval(value),amplitude_required_by_axis=interval(target),center_h=str(hc),center_p=interval(pc),center_q=str(qc),amplitude_required_by_center=interval(acenter),center_far_amplitude_intervals_disjoint=(acenter[1]<target[0] or target[1]<acenter[0]),amplitude_difference_from_axis=interval((a-target[1],a-target[0])),sign='negative' if value[1]<0 else 'positive' if value[0]>0 else 'unresolved')
 report['rows'].append(row);print(json.dumps({k:row[k] for k in ['label','F_axis','amplitude_required_by_axis','sign']}),flush=True)
report['end_utc']=now();(OUT/'axis_exact.json').write_text(json.dumps(report,indent=2)+'\n')
