from pathlib import Path
from datetime import datetime, timezone
import sys, json, hashlib
import numpy as np
from scipy.fft import dct
from numpy.polynomial.chebyshev import chebval,chebder
import torch

torch.set_num_threads(1)
root=Path(__file__).resolve().parents[1]
num=root.parents[1]/'numerics/runs'
sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity

inputs=[]
def freeze(name):
 p=num/name
 data=p.read_bytes()
 q=root/'data'/name
 q.write_bytes(data)
 inputs.append(dict(source=str(p),copy=str(q),md5=hashlib.md5(data).hexdigest(),bytes=len(data)))
 return q

def coefficients(values):
 n=values.shape[0]-1
 c=dct(values[::-1],type=1,axis=0)/n
 c[[0,-1],:]*=.5
 c=dct(c,type=2,axis=1)/values.shape[1]
 c[:,0]*=.5
 return c

def stats(c):
 e=c*c
 total=e.sum()
 er=e.sum(axis=1);et=e.sum(axis=0)
 ir=int(np.ceil(2*(len(er)-1)/3));it=int(np.ceil(2*len(et)/3))
 def slope(v):
  x=np.arange(len(v)//2,len(v),dtype=float)
  y=np.log10(v[len(v)//2:]+1e-300)
  x-=x.mean()
  return float(x@y/(x@x))
 return dict(frac_radial_upper_third=float(er[ir:].sum()/total),frac_angular_upper_third=float(et[it:].sum()/total),slope_radial=slope(er),slope_angular=slope(et),ratio_radial_hi_lo=float(er[ir:].mean()/(er[:len(er)//3].mean()+1e-300)),ratio_angular_hi_lo=float(et[it:].mean()/(et[:len(et)//3].mean()+1e-300)),last_radial_shell=float(er[-1]/total),last_angular_shell=float(et[-1]/total))

out=[]
for tag,state in [('n96m40S','dnB_n96m40S.npz'),('n120m48_S','dnSB_n120m48.npz'),('n96m40SL4','dnB_n96m40SL4.npz')]:
 field=NodalDensity(freeze(state))
 raw=torch.load(freeze('ritz_'+tag+'.pt'),map_location='cpu',weights_only=True)
 vectors=raw['Wv'].double().numpy()
 report=json.loads(freeze('smooth_'+tag+'.json').read_text())
 xp=report['xstar']
 q=field.qnodes
 a=(1-field.k)/2
 def radial_q(x):return -np.expm1(-a*np.log1p(np.asarray(x)**2/field.L**2))
 radii=np.full_like(q[1:],np.inf)
 radii[:-1]=field.L*np.sqrt(np.expm1(-np.log1p(-q[1:-1])/a))
 rr=np.repeat(radii,field.M);tt=np.tile(field.thetanodes,field.N)
 dist=np.hypot(rr*np.cos(tt)-xp,rr*np.sin(tt))
 modes=[]
 for j in range(6):
  v=vectors[:,-1-j].copy();v/=np.linalg.norm(v)
  V=np.zeros_like(field.b);V[1:]=v[:field.N*field.M].reshape(field.N,field.M)
  co=coefficients(V)
  spectra={key:stats(coefficients(val)) for key,val in [('delta_b',V),('delta_b_over_b',V/field.b),('weighted_(1-q)_delta_b_over_b',(1-q[:,None])*V/field.b)]}
  e=V[1:].ravel()**2;total=e.sum()
  masks={'d_lt_2':dist<2,'d_lt_0p5':dist<.5,'r_lt_1':rr<1,'r_1_100':(rr>=1)&(rr<100),'r_ge_100':rr>=100}
  fractions={key:float(e[mask].sum()/total) for key,mask in masks.items()}
  axis_co=co.sum(axis=1)
  f=lambda x:chebval(2*radial_q(x)-1,axis_co)
  xs=xp+np.linspace(-3,3,61)
  sup=np.abs(f(xs)).max()
  hs=2.**-np.arange(0,8)
  differences={str(float(h)):float((f(xp+h)-2*f(xp)+f(xp-h))/h**2/sup) for h in hs}
  B=1+xp*xp/field.L**2
  qp=2*a*xp/field.L**2*B**(-a-1)
  qpp=2*a/field.L**2*B**(-a-1)-4*a*(a+1)*xp*xp/field.L**4*B**(-a-2)
  z=2*radial_q(xp)-1
  exact_second=float((4*qp*qp*chebval(z,chebder(axis_co,2))+2*qpp*chebval(z,chebder(axis_co)))/sup)
  old=report['modes'][j]
  spectrum_error=max(abs(spectra[key][x]-old[key][x]) for key in spectra for x in spectra[key])
  energy_error=max(abs(fractions[x]-old['energy_frac_near_P'][x]) for x in fractions)
  d2_error=max(abs(differences[x]-old['axis_second_diff_over_sup'][x]) for x in old['axis_second_diff_over_sup'])
  axis_error=float(np.max(np.abs(f(xs)-old['axis_profile'])))
  imax=int(np.argmax(e))
  modes.append(dict(index=j,dcl=float(v[-2]),dC=float(v[-1]),spectra=spectra,energy_frac_near_P=fractions,axis_second_diff_over_sup=differences,axis_exact_second_derivative_over_sup=exact_second,axis_sup_on_61_samples=float(sup),argmax_r=float(rr[imax]) if np.isfinite(rr[imax]) else None,argmax_is_infinite_endpoint=bool(not np.isfinite(rr[imax])),argmax_theta_degrees=float(np.degrees(tt[imax])),matches_report=dict(spectrum_max_error=float(spectrum_error),fraction_max_error=energy_error,second_difference_max_error=d2_error,axis_profile_max_error=axis_error)))
  assert spectrum_error<1e-8 and energy_error<1e-12 and d2_error<1e-8 and axis_error<1e-10
  print(tag,j,'hi fractions',*[spectra['delta_b'][x] for x in ['frac_radial_upper_third','frac_angular_upper_third']],'nearP',fractions['d_lt_2'],'far',fractions['r_ge_100'],'D2 h=.125',differences['0.125'],'exact',exact_second,'last h',differences['0.0078125'],flush=True)
 out.append(dict(tag=tag,state_md5=field.md5,xstar_from_report_for_matched_check=xp,modes=modes))
# Algebraic counterexample, evaluated by Chebyshev coefficient differentiation.
examples=[]
for n in [8,16,32,64,128]:
 c=np.zeros(n+1);c[0]=1;c[-1]=1/n
 d2=float(chebval(0.,chebder(c,2)))
 assert abs(abs(d2)-n)<1e-10
 examples.append(dict(N=n,upper_third_energy=1/(n*n+1),second_derivative_at_zero=d2))
result=dict(date=datetime.now(timezone.utc).isoformat(),method='Own DCT-I/DCT-II reconstruction, Chebyshev derivative chain rule, direct nodal geometry. No numerics code imported.',inputs=inputs,rows=out,counterexample=examples)
(root/'verification/audit.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print('ALL_MATCHED_DIAGNOSTICS_PASS')
