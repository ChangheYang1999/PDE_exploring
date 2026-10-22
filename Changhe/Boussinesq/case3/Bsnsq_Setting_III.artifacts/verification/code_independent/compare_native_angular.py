"""Own common-physical-grid K24/K32/K40 angular comparison, packet120.

No NUM imports. SciPy value reader, direct trigonometric angular sums,
seven-point angular finite differences, and independent root brackets.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time,shutil,itertools
import numpy as np
from scipy.optimize import brentq
from r2_state_values import R2State
from finite_difference import stencil

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--names',nargs='+',default=['blam24v_lambda0.95.npz','blam32v_lambda0.95.npz','blam40v95_lambda0.95.npz']);ap.add_argument('--lambda-value',type=float,default=.95);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True)
t0=time.perf_counter();source=Path('numerics/runs');names=args.names;states=[];manifest=[]
for name in names:
 dest=root/name
 if not dest.exists():shutil.copyfile(source/name,dest)
 s=R2State(dest);states.append(s);manifest.append({'name':name,'source':str(source/name),'sha256':s.sha256,'K':s.K,'beta':s.beta,'basis_beta':s.bb,'lambda':float(s.meta['lam']),'Nt':s.Nt,'source_coeff_sha256':hashlib.sha256(s.seed_defectG.tobytes()).hexdigest()})
assert len({q['source_coeff_sha256']for q in manifest})==1
assert len(states)>=2 and all(s.Nt==56 and float(s.meta['lam'])==args.lambda_value for s in states)
(root/'manifest.json').write_text(json.dumps(manifest,indent=2))
ks=[np.arange(s.K)for s in states]
def curve(i,r,phi,derivative=0):
 g=states[i].radial(r,'G');k=ks[i]
 # stored eta=cos(phi), x=r sin(phi), y=-r cos(phi)
 return np.sum(g[:,None]*((np.cos(k[:,None]*phi))if derivative==0 else -k[:,None]*np.sin(k[:,None]*phi)),axis=0)
def tail(s,delta,derivative=0):
 c=s.Gs(1.)*s.L**(1+1/s.bb);k=np.arange(s.K);g=c*(-1.)**k
 if derivative==0:return np.sin(delta)*np.sum(g[:,None]*np.cos(k[:,None]*delta),axis=0)
 return np.cos(delta)*np.sum(g[:,None]*np.cos(k[:,None]*delta),axis=0)-np.sin(delta)*np.sum((k*g)[:,None]*np.sin(k[:,None]*delta),axis=0)
# Derivative control on generic non-axis points, independent of analytic trig rule.
z,w=stencil();deriv=[]
for i,s in enumerate(states):
 phi=np.linspace(.017,np.pi-.019,171)
 for h in [1e-4,5e-5]:
  val=curve(i,1e7,(phi[:,None]+h*z).ravel()).reshape(len(phi),len(z))@w/h
  exact=curve(i,1e7,phi,1);err=float(np.max(abs(val-exact))/np.max(abs(exact)))
  assert err<3e-8,err
  deriv.append({'K':s.K,'h':h,'max_relative_derivative_error':err})
comparisons=[]
radii=np.geomspace(1e4,1e8,61)
for count in [719,1439,2879]:
 # Between-node grids for all three fitting angular meshes, plus near-axis points.
 phi=np.unique(np.r_[np.pi*(np.arange(count)+.37)/count,0.,np.pi,np.pi-np.geomspace(1e-9,.05,101)])
 rows=[]
 for coarse,fine in ([(0,1),(1,2),(0,2)]if len(states)==3 else list(itertools.combinations(range(len(states)),2))):
  best=[{'value':-1.},{'value':-1.}];ab=[0.,0.];globalden=[0.,0.];globalarg=[None,None]
  for r in radii:
   envelope=r**(1+1/states[fine].bb)
   for d in [0,1]:
    a=curve(coarse,r,phi,d)*envelope;b=curve(fine,r,phi,d)*envelope
    den=float(abs(b).max());diff=abs(a-b);j=int(diff.argmax());v=float(diff[j]/den)
    globalden[d]=max(globalden[d],den)
    if float(diff.max())>ab[d]:globalarg[d]={'r':float(r),'phi':float(phi[j]),'degrees_from_upper_axis':float((np.pi-phi[j])*180/np.pi)}
    ab[d]=max(ab[d],float(diff.max()))
    if v>best[d]['value']:best[d]={'value':v,'r':float(r),'phi':float(phi[j]),'degrees_from_upper_axis':float((np.pi-phi[j])*180/np.pi),'finer_supremum':den}
  rows.append({'pair':[states[coarse].K,states[fine].K],'G':best[0],'dphiG':best[1],'absolute_envelope_scaled_difference_max':ab,'global_supremum_normalized_difference':[ab[d]/globalden[d]for d in [0,1]],'global_finer_suprema':globalden,'global_difference_argmax':globalarg})
 comparisons.append({'angular_points':len(phi),'base_between_node_count':count,'pairs':rows})
peaks=[]
for s in states:
 grid=np.linspace(0,np.pi/2,20001);d=tail(s,grid,1);hits=np.where((d[:-1]>0)&(d[1:]<=0))[0]
 delta_p=float(brentq(lambda a:tail(s,np.array([a]),1)[0],grid[hits[0]],grid[hits[0]+1],xtol=1e-14))if len(hits)else np.pi/2
 A=float(tail(s,np.array([delta_p]))[0]);part=np.linspace(0,delta_p,4097)
 monotone=bool(np.all(tail(s,part,1)>-1e-10))
 row={'K':s.K,'delta_peak':delta_p,'peak_amplitude':A,'numerically_monotone_before_peak':monotone,
      'stored_tail_axis_slope':float(tail(s,np.array([0.]),1)[0])}
 if monotone and A>0:
  for q in [.1,.9]:row[f'delta_{q}']=float(brentq(lambda a:tail(s,np.array([a]))[0]-q*A,0,delta_p,xtol=1e-14))
  row['width_10_90']=row['delta_0.9']-row['delta_0.1']
 peaks.append(row)
result={'status':'COMPLETE','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-t0,
 'manifest':manifest,'derivative_controls':deriv,'common_grid_comparisons':comparisons,'stored_exact_tail_peak_diagnostics':peaks,
 'scope':f'Stored field comparison at lambda{args.lambda_value}; not transported field or a B2 solution. Floating-point grids and roots, no rigorous monotonicity isolation. Three differences do not prove infinite-resolution convergence or its rate. No denominator floor; Both comparison norms are provided: finer angular supremum at each physical radius, and finer supremum over the full sampled radius-angle set. Both differ from PDE pointwise normalizers.'}
(root/'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'elapsed_seconds':result['elapsed_seconds'],'finest_comparison':comparisons[-1],'tail_diagnostics':peaks},indent=2))
