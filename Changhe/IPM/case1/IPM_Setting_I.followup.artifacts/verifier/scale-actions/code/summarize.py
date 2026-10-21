from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from itertools import combinations
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
from collocation import NodalDensity
from analytic_gradients import gradients
raw=(OUT/'actions.json').read_bytes();data=json.loads(raw)
partial='--partial' in sys.argv
assert data.get('complete') or partial
pts=np.array(data['points']);n=len(pts);assert n==58
oldfile=ROOT.parent/'sampled-physical-actions/verification/summary_all_radial_matrices.npz'
old=np.load(oldfile);oldsummary=json.loads((oldfile.parent/'summary_all_radial.json').read_text())
assert oldsummary['complete']
obj={'date':datetime.now(timezone.utc).isoformat(),'new_actions_sha256':hashlib.sha256(raw).hexdigest(),'old_matrices_sha256':hashlib.sha256(oldfile.read_bytes()).hexdigest(),'complete':bool(data.get('complete')),'states':[],'scope':'Finite58point norms on different base states at fixed N96M40; no continuum spectrum or global action error bound. New scales use the main quadrature; a separate12point refinement sensitivity is recorded separately and does not bound all58rows. L8 refinement does not certify other scales.'}
arrays={};Qs={};Bs={};sv=lambda x:np.linalg.svd(x,compute_uv=False)
for st in data['states']:
 if len(st['rows'])!=n:
  assert partial;continue
 tag=st['tag'];d=NodalDensity(ROOT/'data'/('dnB_'+tag+'.npz'));assert d.md5==st['state_md5']
 dirs=ROOT/'data'/('directions_'+tag+'.npz');assert hashlib.sha256(dirs.read_bytes()).hexdigest()==st['direction_sha256']
 V=np.load(dirs)['V'];dc=V[-2];rr=st['rows'];assert [r['point'] for r in rr]==data['points']
 rho=np.array([r['rho'] for r in rr]);dr=np.array([r['delta_rho'] for r in rr]);du=np.array([r['delta_U'] for r in rr]);W=d.cl*pts+np.array([r['base_U'] for r in rr])
 g=np.array([r['gradient'] for r in rr]);dg=np.array([r['delta_gradient'] for r in rr]);ga,dga=gradients(d,V,pts)
 nf=abs(rho)+np.sum(abs(W*g),axis=1);assert np.all(nf>0)
 M=np.vstack([dr/(1+abs(rho[:,None]))/np.sqrt(n),dc]);arrays[tag+'_M']=M
 def action(bg,ddg):return (dc[None,:]*np.sum(pts*bg,axis=1)[:,None]+np.einsum('ijk,ik->ij',ddg,W)+np.einsum('ijk,ik->ij',du,bg)-dr)/nf[:,None]/np.sqrt(n)
 A=action(g,dg);AA=action(ga,dga);arrays[tag+'_A']=A;arrays[tag+'_analytic_A']=AA
 tbase=np.array([float(Fraction(r['base_U_tail_bound_exact'])) for r in rr]);td=np.array([[float(Fraction(z)) for z in r['delta_U_tail_bounds_exact']] for r in rr]);tails=(tbase[:,None]*np.sum(abs(dg),axis=2)+td*np.sum(abs(g),axis=1)[:,None])/nf[:,None]/np.sqrt(n)
 res=(np.sum(W*g,axis=1)-rho)/nf;entry={'tag':tag,'L':d.L,'source_md5':d.md5,'base_max_R_Nf':float(max(abs(res))),'base_max_index':int(np.argmax(abs(res))),'CPU_GPU_density_max_error':st['cpu_gpu_density_max_error'],'max_analytic_base_gradient_difference':float(np.max(abs(g-ga))),'max_analytic_delta_gradient_difference':float(np.max(abs(dg-dga))),'max_FD_step_action_change_node_units':float(max(max(r['spatial_step_change_fixed_units']) for r in rr)),'spaces':{}}
 for k in (4,10,14):
  Q,T=np.linalg.qr(M[:,:k],mode='reduced');cond=sv(M[:,:k]);assert cond[-1]>1e-10*cond[0];B=np.linalg.solve(T.T,A[:,:k].T).T
  DA=np.linalg.solve(T.T,(AA-A)[:,:k].T).T;QA,RA=np.linalg.qr(A[:,:k],mode='reduced');assert sv(RA)[-1]>1e-12*sv(RA)[0]
  z=np.linalg.solve(RA.T,dc[:k]);cost=1/np.linalg.norm(z);c=np.linalg.solve(RA,z)*cost**2;assert abs(dc[:k]@c-1)<1e-9;assert abs(np.linalg.norm(A[:,:k]@c)/cost-1)<1e-9
  entry['spaces'][str(k)]={'metric_condition':float(cond[0]/cond[-1]),'physical_singular_values_ascending':sv(B)[::-1].tolist(),'unit_cl_cost':float(cost),'cl_minimizer':c.tolist(),'analytic_gradient_action_difference_Frobenius':float(np.linalg.norm(DA)),'analytic_gradient_action_difference_spectral':float(np.linalg.norm(DA,2)),'tail_action_Frobenius_bound_using_numerical_gradients':float(np.linalg.norm(tails[:,:k]@abs(np.linalg.solve(T,np.eye(k)))))}
  Qs[tag,k]=Q;Bs[tag,k]=B;arrays[f'{tag}_{k}_B']=B
 obj['states'].append(entry)
# L8 uses the completed matching quadrature and finest FD gradient matrices.
for k in(4,10,14):
 Qs['n96m40S',k]=np.linalg.qr(old['n96m40S_M'][:,:k],mode='reduced')[0];Bs['n96m40S',k]=old[f'n96m40S_{k}_a4096_r32_B']
obj['scale_comparisons']=[]
for a,b in combinations(sorted({tag for tag,k in Qs}),2):
 for k in(4,10,14):obj['scale_comparisons'].append({'first':a,'second':b,'dimension':k,'domain_sampling_overlap_cosines':sv(Qs[a,k].T@Qs[b,k]).tolist(),'physical_singular_value_ratios_first_over_second_ascending':(sv(Bs[a,k])[::-1]/sv(Bs[b,k])[::-1]).tolist()})
name='summary_partial' if partial else 'summary'
(OUT/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n');np.savez_compressed(OUT/(name+'_matrices.npz'),**arrays)
for st in obj['states']:
 print(st['tag'],st['base_max_R_Nf'])
 for k,v in st['spaces'].items():print(k, 'sigma',v['physical_singular_values_ascending'][0],'cost',v['unit_cl_cost'],'analytic',v['analytic_gradient_action_difference_Frobenius'],'tail',v['tail_action_Frobenius_bound_using_numerical_gradients'])
print('COMPLETE_STATES',len(obj['states']),'complete',obj['complete'])
