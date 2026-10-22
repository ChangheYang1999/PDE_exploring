"""Exact rational scaled-family center residuals; own coefficient sums."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,datetime,hashlib,json
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('--root',default='candidate_audits/lead_scaled64');ap.add_argument('--source-subdir',default='sources');args=ap.parse_args()
ROOT=Path(args.root);OUT=ROOT/'center_exact';OUT.mkdir(exist_ok=True)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def scale(a,c):return mul(a,(c,c))
def ab(a):
 return (F(0) if a[0]<=0<=a[1] else min(abs(x) for x in a),max(abs(x) for x in a))
def serial(a):return {'exact':[str(v) for v in a],'approximate':[float(v) for v in a]}
n=100;ss=sum(F(3**k,factorial(k)) for k in range(n+1));tt=F(3**(n+1),factorial(n+1));exp3=(ss,ss+tt/(1-F(3,n+2)))
report={'start_utc':now(),'script_sha256':sha(__file__),'arithmetic':'exact Fraction operations on stored binary64 coefficients','exponential_enclosure':{'argument':3,'order':n,**serial(exp3)},'rows':[]}
for source in sorted((ROOT/args.source_subdir).glob('*.npz')):
 with np.load(source,allow_pickle=False) as z:
  if not (float(z['beta'])==3 and int(z['m'])==3): raise ValueError('Only exact beta3 m3 supported')
  for key in ['c','a0','alpha','se']:
   if key in z.files and (z[key].dtype!=np.dtype('float64') or not np.all(np.isfinite(z[key]))): raise ValueError('Expected finite binary64 storage: '+key)
  se=F.from_float(float(z['se'])) if 'se' in z.files else F(1)
  if not (se>0 and (float(z['gam'])==0 if 'gam' in z.files else True)): raise ValueError('Unsupported scale or angular map')
  c=z['c'].reshape(int(z['J'])+1,int(z['Kw'])+1);a=F.from_float(float(z['a0']));alpha=F.from_float(float(z['alpha'])) if 'alpha' in z.files else F(0)
  sums=[F(0),F(0),F(0)]
  for j in range(c.shape[0]):
   for k in range(c.shape[1]):
    q=F.from_float(float(c[j,k]))*(-1)**k;sums[0]+=q;sums[1]+=2*j*j*q;sums[2]-=2*k*k*q
 h,t,pw=sums;d=pw/se**2
 if not (h>0 and a!=0 and alpha in [0,3]): raise ValueError("Unsupported center hypothesis")
 ell=(-F(1,6),-F(1,6)) if alpha==0 else scale(add(exp3,(-F(1),-F(1))),-F(1,18))
 p=add((h/3,h/3),scale(ell,t));g=add(scale(p,-60/h),(-12*d/h**3,)*2);theta=scale(p,-6*a/h**2)
 residual=add(scale(p,6*a/h**2-420/h),(-84*d/h**3,)*2)
 # Separate interval assembly of the two center terms must contain the tighter affine range.
 redundant=add(scale(g,7),scale(theta,-1))
 if not (redundant[0]<=residual[0]<=residual[1]<=redundant[1]): raise ArithmeticError("Interval containment failed")
 norm=add(scale(ab(g),7),ab(theta))
 if norm[0]<=0: raise ArithmeticError("Nonpositive normalizer")
 rat=mul(ab(residual),(1/norm[1],1/norm[0]));sign='negative' if residual[1]<0 else 'positive' if residual[0]>0 else 'unresolved'
 row={'state':source.stem,'source_sha256':sha(source),'alpha':str(alpha),'se_exact':str(se),'Pw_unscaled':str(pw),'center_q':str(d),'h':str(h),'Pt':str(t),'scaled_Pw_over_se_squared':str(d),'a':str(a),'p':serial(p),'Omega_xy':serial(g),'Theta_xxy':serial(theta),'D_Omega':serial(residual),'ND_Omega':serial(norm),'ratio':serial(rat),'sign_certified':sign,'ratio_exceeds_1e_minus_6':rat[0]>F(1,10**6),'scope':'Exact dyadic source coefficients and se, exact rational beta3 exponents and exp(alpha); local chart only, no canonical inverse or global positivity claim'}
 report['rows'].append(row);print(json.dumps({'state':source.stem,'sign':sign,'D':row['D_Omega']['approximate'],'ratio':row['ratio']['approximate']}),flush=True)
report['end_utc']=now();report['all_nonzero']=all(r['sign_certified']!='unresolved' for r in report['rows']);(OUT/'audit.json').write_text(json.dumps(report,indent=2)+'\n')
