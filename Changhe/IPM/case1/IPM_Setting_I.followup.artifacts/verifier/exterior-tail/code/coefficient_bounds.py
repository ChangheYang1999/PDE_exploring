"""Exact coefficient inequalities and rational exterior bounds.
No numerical integration, and no certification of interior quadrature.
"""
import json,hashlib
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
TEAM=ROOT.parents[1]/'numerics'
xfile=TEAM/'data/c6g_shape.npz'
nfile=TEAM/'data/dnSB_n120m48.npz'

def rat(v):return F.from_float(float(v))
def record(q):return {'numerator':q.numerator,'denominator':q.denominator,'approximate':float(q)}

with np.load(xfile) as z:
 degree=int(z['degree']);mmax=int(z['angular']);order=int(z['spline_order'])
 co=[[F(0) for m in range(mmax+1)] for j in range(degree+1)];sing=[]
 for name,value in zip(z['names'],z['z'][1:]):
  m,j=map(int,name)
  if m<0:sing.append(rat(value))
  else:
   assert 0<=m<=mmax and 0<=j<degree
   co[j+1][m]=rat(value)
 rows=[sum(map(abs,row),F(0)) for row in co];cm=max(rows);sm=sum(map(abs,sing),F(0))
 knots=[rat(v) for v in z['spline_knots']]
 assert len(knots)==degree+1+order+1
 assert all(a<=b for a,b in zip(knots,knots[1:]))
 assert knots[:order+1]==[F(0)]*(order+1) and knots[-order-1:]==[F(1)]*(order+1)
 assert cm<4 and sm<16 and 1<rat(z['L'])<8 and 0<rat(z['k'])<F(1,5)
 cl=rat(z['c_l']);p3=6+2/(2*cl-1);assert p3>6
 x={'md5':hashlib.md5(xfile.read_bytes()).hexdigest(),'coefficient_row_l1_max':record(cm),
    'singular_l1':record(sm),'L':record(rat(z['L'])),'k':record(rat(z['k'])),
    'p3':record(p3),'constant_C':512*3**7,'gamma':'1/5','all_exact_coefficient_assertions':True}
with np.load(nfile) as z:
 N=int(z['N']);M=int(z['M']);B=max(rat(v) for v in np.abs(z['b']).ravel())
 assert (N,M)==(120,48) and B<27 and rat(z['L'])==8
 k=1/rat(z['c_l']);assert 0<k<F(1,5)
 assert 2*N*(2*M-1)<151**2
 q=(1-np.cos(np.arange(N+1)*np.pi/N))/2
 s=(np.arange(M)+.5)*np.pi/(2*M);theta=s+float(z['beta'])*np.sin(2*s)/2
 n={'md5':hashlib.md5(nfile.read_bytes()).hexdigest(),'nodal_abs_max':record(B),'N':N,'M':M,
    'radial_node_transcription_max':float(np.max(np.abs(q-z['q']))),
    'angular_node_transcription_max':float(np.max(np.abs(theta-z['theta']))),
    'evaluation_norm_squared_upper':2*N*(2*M-1),'constant_C':512*27*151,'gamma':'1/5',
    'all_exact_coefficient_assertions':True}
rows=[]
for name,obj in [('X3',x),('dnSB',n)]:
 C=F(obj['constant_C']);gamma=F(1,5)
 for exponent in [5,10,15,20,25,30]:
  R=10**exponent;radial=F(1,10**(4*exponent//5))
  strain=2*C/(1-gamma)*radial
  for radius in [1,10,100,1000,10000,100000]:
   if radius>=R:continue
   t=F(radius,R);velocity=strain*radius/(1-t*t)**2
   remainder=2*C/(3-gamma)*radius**3*radial/F(R**2)*(2-t*t)/(1-t*t)**2
   rows.append({'field':name,'cutoff':R,'observation_radius':radius,'velocity_bound':record(velocity),
                'strain_coefficient_bound':record(strain),'after_strain_remainder_bound':record(remainder)})
result={'statement':'Exact rational coefficient and exterior estimates; interior quadrature is not certified.','X3':x,'dnSB':n,'bounds':rows}
(ROOT/'verification/coefficient_bounds.json').write_text(json.dumps(result,indent=2)+'\n')
for r in rows:
 if r['cutoff']==10**30 and r['observation_radius']==100000:
  print(r['field'],'R=1e30 |X|<=1e5: U_tail <',float(r['velocity_bound']['numerator']/r['velocity_bound']['denominator']),
        'strain <',float(r['strain_coefficient_bound']['numerator']/r['strain_coefficient_bound']['denominator']))
print('coefficient assertions passed; node transcription errors',n['radial_node_transcription_max'],n['angular_node_transcription_max'])
