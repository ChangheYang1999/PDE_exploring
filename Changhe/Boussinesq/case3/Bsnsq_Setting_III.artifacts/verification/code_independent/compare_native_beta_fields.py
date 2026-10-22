"""Independent between-node field comparison at fixed beta, with own angular FD."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,time
import numpy as np
from r2_state_values import R2State
from finite_difference import stencil
root=Path(sys.argv[1]);root.mkdir(exist_ok=True);started=datetime.now(timezone.utc).isoformat();begin=time.monotonic()
paths=[('3.0315','verification/native_beta3p0315_20261021T0747Z/blamB32_beta3.0315.npz','verification/native_K40_beta3p0315_20261021T1034Z/blamB40chk_beta3.0315.npz'),('3.04','verification/native_beta3p04_3p05_20261021T084200Z/blamB32_beta3.04.npz','verification/native_K40_beta3p04_20261021T1105Z/blamB40chk_beta3.04.npz'),('3.05','verification/K40_beta305_20261021T1631Z/archives/blamB32_beta3.05.npz','verification/K40_beta305_20261021T1631Z/archives/blamB40ext_beta3.05.npz'),('3.062','verification/K40_beta3062_20261021T1653Z/archives/blamB32_beta3.062.npz','verification/K40_beta3062_20261021T1653Z/archives/blamB40ext_beta3.062.npz')]
states=[];manifest=[]
for beta,*names in paths:
 pair=[R2State(p)for p in names];a,b=pair;assert a.beta==b.beta==float(beta)and a.bb==b.bb and a.L==b.L and a.Nt==b.Nt==56 and a.K==32 and b.K==40
 assert a.native_source and b.native_source and np.array_equal(a.seed_field.rawG,b.seed_field.rawG)
 assert all(getattr(a.seed_field,k)==getattr(b.seed_field,k)for k in ['bb','L','K','Nt','grade','degree'])
 manifest.append({'beta':beta,'states':[{'path':str(s.path),'sha256':s.sha256,'K':s.K,'lambda':float(s.meta['lam']),'Nt':s.Nt,'a0':s.center()['F']['value']}for s in pair],'lambda_difference_K40_minus_K32':float(b.meta['lam'])-float(a.meta['lam']),'seed_coefficients_sha256':hashlib.sha256(a.seed_field.rawG.tobytes()).hexdigest(),'same_native_seed':True});states.append(pair)
(root/'manifest.json').write_text(json.dumps({'utc':started,'pairs':manifest},indent=2)+'\n')
radii=np.unique(np.r_[np.geomspace(1e-6,1e8,161),np.geomspace(1e4,1e8,61),.5,1.,5.,500.]);radials=[[s.radial(radii,'G')for s in pair]for pair in states]
z,w=stencil();controls=[]
for pair in states:
 for s in pair:
  phi=np.pi*(np.arange(173)+.371)/173;k=np.arange(s.K);c=np.cos(phi[:,None]*k);der=-np.sin(phi[:,None]*k)*k
  for r in [1e-4,1.,1e4,1e8]:
   g=s.radial(r,'G');direct=der@g;ref=float(np.max(abs(direct)));assert ref>0
   # Remove only the exactly angle-independent mode before FD to avoid
   # subtractive cancellation of an O(1) value against an O(r) derivative.
   gd=g.copy();gd[0]=0.
   for h in [2e-4,1e-4]:
    shifted=phi[:,None]+z*h;fd=(np.cos(shifted[:,:,None]*k)@gd)@w/h;err=float(np.max(abs(fd-direct))/ref);assert err<3e-8,(s.path,r,h,err)
    controls.append({'archive_sha256':s.sha256,'r':r,'h':h,'relative_angular_FD_discrepancy':err})
comparisons=[]
def safe(n,d):
 return np.divide(n,d,out=np.where(n==0,0.,np.inf),where=d!=0)
for na in [719,1439,2879]:
 phi=np.unique(np.r_[np.pi*(np.arange(na)+.371)/na,0.,np.pi,np.pi-np.geomspace(1e-9,.05,101),np.geomspace(1e-9,.05,101)]);pairs=[]
 for index,pair in enumerate(states):
  sums=[]
  for s,g in zip(pair,radials[index]):
   k=np.arange(s.K);sums.append([g@np.cos(k[:,None]*phi),g@(-k[:,None]*np.sin(k[:,None]*phi))])
  item={'beta':paths[index][0],'lambda_difference_K40_minus_K32':manifest[index]['lambda_difference_K40_minus_K32'],'fields':{}}
  for d,key in enumerate(['G','dphiG']):
   aa,bb=sums[0][d],sums[1][d];den=np.max(abs(bb),axis=1);symden=np.maximum(den,np.max(abs(aa),axis=1));dd=abs(bb-aa);di=np.argmax(dd,axis=1);maximum=dd[np.arange(len(radii)),di];rel=safe(maximum,den);sym=safe(maximum,symden);out={}
   for name,mask in [('all_sampled',(radii>=1e-6)),('outer_1e4_1e8',(radii>=1e4)),('core_le3',(radii<=3)),('mid_3_300',(radii>=3)&(radii<=300)),('outer_ge300',(radii>=300))]:
    ix=np.flatnonzero(mask);j=int(ix[np.argmax(rel[ix])]);sc=radii[ix]**(1+1/pair[0].bb);envdiff=maximum[ix]*sc;envden=den[ix]*sc;u=int(ix[np.argmax(envdiff)]);out[name]={'max_radiuswise_K40_relative_difference':float(rel[j]),'radius_at_max':float(radii[j]),'phi_at_max':float(phi[di[j]]),'max_radiuswise_symmetric_relative_difference':float(np.max(sym[ix])),'raw_absolute_difference_max':float(np.max(maximum[ix])),'envelope_scaled_absolute_difference_max':float(np.max(envdiff)),'global_envelope_K40_relative_difference':float(np.max(envdiff)/np.max(envden)),'radius_at_envelope_difference_max':float(radii[u]),'zero_denominators':int(np.sum(den[ix]==0))}
   out['by_radius']={'r':radii.tolist(),'absolute_difference':maximum.tolist(),'K40_supremum':den.tolist(),'K40_relative_difference':rel.tolist()};item['fields'][key]=out
  pairs.append(item)
 comparisons.append({'base_angular_points':na,'actual_angular_points':len(phi),'radial_count':len(radii),'pairs':pairs});print('grid',na,'complete',time.monotonic()-begin,flush=True)
out={'status':'COMPLETE','started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-begin,'manifest':manifest,'angular_FD_controls':controls,'comparisons':comparisons,'scope':'Finite frozen-field distances for G=Omega/x and fixed-r angular derivative, not Omega or U or PDE residuals. Each pair has common beta and slightly different fitted lambda. Half-plane angles suffice by x-reflection. Own SciPy reader, trigonometric derivatives checked by seven-point angular finite differences, three between-node angular grids. Radiuswise and globally envelope-normalized norms are distinct and both reported. No denominator floor, zero/zero=0 and positive/zero=infinity. No convergence limit, exact branch, positivity or error certificate claimed.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'results.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print(out['ended_utc'],'COMPLETE',out['elapsed_seconds'],'FDchecks',len(controls),'FDmax',max(c['relative_angular_FD_discrepancy']for c in controls))
for p in comparisons[-1]['pairs']:print(p['beta'],[(k,p['fields'][k]['outer_1e4_1e8'])for k in ['G','dphiG']])
