"""Sampled diagnostic for M. Arb radial coefficients, floating angular matrix.
No positivity between sample points is certified by this program.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib,math
import numpy as np
from flint import arb,ctx
from audit_points import polynomials,eval_fields
HERE=Path(__file__).resolve().parent
ctx.prec=384

def run(name):
 start=time.monotonic();path=HERE/(name+'.json');d=json.loads(path.read_text());c=arb(d['cl']);gamma=1/c
 P=polynomials(d);needed=[(2,2),(0,4),(3,1)];P4={key:P[key] for key in needed}
 nmax=max(n for pol in P4.values() for j,k,n in pol)
 theta=np.arange(65)*math.pi/128
 trig={'c':np.cos(np.outer(np.arange(nmax+1),theta)),'s':np.sin(np.outer(np.arange(nmax+1),theta))}
 allpowers={q for pol in P4.values() for C in pol.values() for q in C}
 rows=[];lowest=(1e99,None,None);maxrad=0.
 for i in range(-24,49):
  r=arb(2)**(arb(i)/4);r2=r*r;t=r2/(1+r2);tp={q:t**q for q in allpowers}
  pref={j:(1+r2)**((3+gamma-j*(1-gamma))/2)/(r2*r2) for j in range(6)}
  radial={}
  for key,pol in P4.items():
   co={}
   for (j,kind,n),C in pol.items():
    val=pref[j]*sum((v*tp[k] for k,v in C.items()),arb(0))
    co[kind,n]=co.get((kind,n),arb(0))+val
   vals=np.zeros(len(theta))
   for (kind,n),v in co.items():
    assert v.is_finite()
    # Midpoint conversion is diagnostic only. Record the absolute Arb radius.
    maxrad=max(maxrad,float(v.rad()))
    vals+=float(v.mid())*trig[kind][n]
   radial[key]=vals
  xx=2*float(c)+1-2*radial[2,2]-radial[0,4];yy=2*float(c)+1+radial[2,2];xy=radial[3,1]
  lm=(xx+yy-np.sqrt((xx-yy)**2+4*xy**2))/2
  k=int(np.argmin(lm));row={'log2_radius':i/4,'radius':float(r),'min_eigenvalue':float(lm[k]),'angle_pi_units':k/128}
  rows.append(row)
  if lm[k]<lowest[0]:lowest=float(lm[k]),i,k
 low,i,k=lowest;r=arb(2)**(arb(i)/4);angle=arb.pi()*k/128;x=r*angle.cos();y=r*angle.sin()
 # Reevaluate the sampled minimum using all-Arb polar fields.
 ar=eval_fields(P,c,x,y)
 first={str(bound):next((row for row in rows if row['min_eigenvalue']<bound),None) for bound in (3.8,0.)}
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'status':'FLOAT_DIAGNOSTIC','method':'73 radii 2^(i/4), i=-24..48; 65 angles k*pi/128. 384-bit Arb radial coefficients, float64 angular summation and eigensolver. Sampled minimum re-evaluated with Arb.','rows':rows,'first_sample_below':first,'sampled_minimum':{'value_float':low,'log2_radius':i/4,'angle_pi_units':k/128,'x_arb':x.str(40),'y_arb':y.str(40),'Mmin_arb':ar['M_lambda_min'].str(60),'F_arb':ar['F'].str(60)},'max_radial_coefficient_arb_radius':maxrad,'seconds':time.monotonic()-start,'scope':'A negative rigorously enclosed sampled value disproves global positivity. Positive sampled values give no global lower bound. First crossing refers only to this specified grid.'}
 (HERE/(name+'_matrix_grid.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(name,'min',out['sampled_minimum'],'first',first,'secs',out['seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:] or [f'algebraic_{base}_k{k}' for base in ('state131','n12_m10') for k in (4,8,16,256,4096)]:run(name)
