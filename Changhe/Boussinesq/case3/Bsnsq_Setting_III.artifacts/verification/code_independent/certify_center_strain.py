"""Exact center moment of literal native-source archives, derived in packet160.

All inputs are exact binary scalars, including independently frozen knots.
No numerics-lane code, inverse matrix, server or JS is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json, shutil, time
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.legendre import leggauss

def q(x): return Q.from_float(float(x))
def encode(x): return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
def bounds(x,digits=15):
 scale=10**digits; lo=x.numerator*scale//x.denominator
 return {'lo':encode(Q(lo,scale)),'hi':encode(Q(lo+1,scale)),'digits':digits,
         'display':[f'{lo/scale:.15f}',f'{(lo+1)/scale:.15f}']}
def block(meta,raw,seed=False):
 get=lambda key:meta.get('seed_'+key,meta[key]) if seed else meta[key]
 b=float(meta['beta_seed' if seed else 'beta_basis']); L=float(get('L'))
 K=int(get('K')); nt=int(get('Nt')); p=int(get('deg')); grade=float(get('grade'))
 edges=np.linspace(0,1,nt+1)**grade; knots=np.r_[np.zeros(p),edges,np.ones(p)]
 nb=len(knots)-p-1; cc=np.asarray(raw,dtype=float).reshape(K,nb).copy()
 for n in range(K): cc[n,:n//2]=0
 a=Q(0)
 for j in range(nb):
  c1=q(cc[1,j]) if K>1 else Q(0); c3=q(cc[3,j]) if K>3 else Q(0)
  a+=(c1-c3)*(q(knots[j+p+1])-q(knots[j]))/(p+1)
 strain=-q(b)*q(L)*a/4
 return {'b_hex':b.hex(),'L_hex':L.hex(),'K':K,'Nt':nt,'degree':p,'grade_hex':grade.hex(),
         'knots_hex':[float(k).hex() for k in knots],
         'active_coefficients_hex':[[float(k).hex() for k in row] for row in cc],
         'strain':encode(strain),'strain_bounds':bounds(strain)},strain

def controls():
 # Fourier orthogonality via independent quadrature in the physical angle.
 angular=[]; nodes,w=leggauss(256); ph=np.pi*(nodes+1); eta=-np.sin(ph)
 for n in range(48):
  pol=np.polynomial.chebyshev.chebval(eta,np.eye(1,48,n).ravel())
  val=float(np.sum(w*np.cos(ph)**2*np.sin(ph)*pol))
  target=-.25 if n==1 else (.25 if n==3 else 0.)
  angular.append({'n':n,'value':val,'target':target,'error':abs(val-target),'pass':abs(val-target)<3e-14})
 rng=np.random.default_rng(160); spline=[]
 for p in [1,3,5]:
  for nt in [8,10]:
   for K in [2,4,11]:
    meta={'beta_basis':2.7,'L':1.3,'K':K,'Nt':nt,'deg':p,'grade':1.5}
    nb=nt+p; coeff=rng.normal(size=(K,nb)); data,exact=block(meta,coeff)
    cc=np.array([[float.fromhex(s) for s in row] for row in data['active_coefficients_hex']]); knots=np.array([float.fromhex(s) for s in data['knots_hex']]); spl=BSpline(knots,cc.T,p)
    ga,gw=leggauss(p+1); approx=0.
    for l,r in zip(np.unique(knots)[:-1],np.unique(knots)[1:]):
     vv=spl((l+r)/2+(r-l)*ga/2); mode=vv[:,1]-(vv[:,3] if K>3 else 0)
     approx+=float(np.dot(gw,mode))*(r-l)/2
    approx*= -meta['beta_basis']*meta['L']/4
    err=abs(approx-float(exact)); spline.append({'degree':p,'Nt':nt,'K':K,'exact_float':float(exact),'cell_quadrature':approx,'error':err,'pass':bool(err<3e-14)})
 return {'angular':angular,'spline_integrals':spline,'all_passed':all(a['pass'] for a in angular+spline)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('archives',nargs='+');args=ap.parse_args()
 root=Path(args.output);root.mkdir(parents=True,exist_ok=True); (root/'archives').mkdir(exist_ok=True)
 started=datetime.now(timezone.utc).isoformat(); begin=time.monotonic(); certs=[]
 for name in args.archives:
  src=Path(name); sha=hashlib.sha256(src.read_bytes()).hexdigest(); dest=root/'archives'/src.name
  if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest()!=sha:raise ValueError('Archive changed under same name')
  shutil.copyfile(src,dest)
  with np.load(dest,allow_pickle=False) as z:
   meta={k:z[k].item() for k in z.files if z[k].ndim==0}
   if meta.get('source_mode')!='fixed_velocity_block' or float(meta.get('eps',1))!=1:raise ValueError('Only literal native-source eps1 schema')
   self_block,c=block(meta,z['cG']);seed_block,cs=block(meta,z['cG_f'],True)
   a=q(z['cF'].ravel()[0]);g=q(z['cG'].ravel()[0]);beta=q(meta['beta']);lam=q(meta['lam']);cm=c+lam*cs;m=cm-1-beta/2
   values={'m_self':c-1-beta/2,'RF_self_center':-2*(c-1-beta/2)*a,'RG_self_center':(beta-c+1)*g-2*a,'c_self':c,'c_seed':cs,'c_mixed':cm,'m':m,'a':a,'q':g,'RF_center':-2*m*a,'RG_center':(beta-cm+1)*g-2*a,'G_compatibility_error':g-4*a/beta,'a0_metadata_error':a-q(meta['a0'])}
   cert={'schema':'verification-exact-center-v1','archive':str(dest),'original':str(src),'archive_sha256':sha,'beta_hex':float(beta).hex(),'lambda_hex':float(lam).hex(),'a0_hex':float(meta['a0']).hex(),'self_block':self_block,'seed_block':seed_block,
         'values':{k:encode(v) for k,v in values.items()},'bounds':{k:bounds(v) for k,v in values.items()},
         'diagnostics':{k:meta[k] for k in ('obj','strain_mismatch','continuation_accepted','converged','inner_converged') if k in meta},
         'claim':'Frozen binary fields only; no beta-interval exclusion or fold claim. m<0 and a>0 imply failure of (T) at the divided center limit.'}
   out=root/(src.stem+'.certificate.json');out.write_text(json.dumps(cert,indent=2)+'\n')
   certs.append({'certificate':str(out),'archive_sha256':sha,'beta':float(beta),'m':float(m),'RF_center':float(values['RF_center']),'RG_center':float(values['RG_center']),'c_self':float(c),'c_mixed':float(cm),'diagnostics':cert['diagnostics'],'negative_m':m<0,'positive_a':a>0})
 control=controls(); result={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-begin,'certificates':certs,'controls':control,'all_controls_passed':control['all_passed']}
 (root/'generation.json').write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({k:v for k,v in result.items() if k!='controls'},indent=2))
 if not control['all_passed']:raise SystemExit(1)
if __name__=='__main__':main()
