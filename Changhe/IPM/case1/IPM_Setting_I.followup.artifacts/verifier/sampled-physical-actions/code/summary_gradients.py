"""Recombine own saved inverse and signed gradients in a fixed finite metric."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'verification'
def load(p):
 raw=p.read_bytes();a=json.loads(raw);assert a.get('complete'),str(p)+' incomplete'
 return a,hashlib.sha256(raw).hexdigest()
def norm2(x):return float(np.linalg.norm(x,2))
def frob(x):return float(np.linalg.norm(x))
def sv(x):return np.linalg.svd(x,compute_uv=False)
def whitening(A,T):return np.linalg.solve(T.T,A.T).T
base,bsha=load(OUT/'actions.json');grads,gsha=load(OUT/'gradients_refined.json')
assert grads['base_actions_sha256']==bsha and grads['points']==base['points']
invs={'2048':base};hashes={'2048':bsha}
if '--refined' in sys.argv:
 invs['4096'],hashes['4096']=load(ROOT/'refinement4096/actions.json')
 assert invs['4096']['points']==base['points']
chosen_inverse='4096' if '4096' in invs else '2048'
pts=np.array(base['points']);n=len(pts);k=14
result={'date':datetime.now(timezone.utc).isoformat(),'inverse_sha256':hashes,'gradient_sha256':gsha,
        'points':base['points'],'normalizer_inverse':chosen_inverse,'chosen_gradient_step':grads['steps'][-1],
        'scope':'Finite sampled numerator actions only. All Nf values fixed at the chosen inverse and gradient. Step and inverse discrepancies are computed matrix differences, not bounds on remaining errors. Exterior bounds use numerical gradients. No continuum spectrum, kernel, isolation, family or endpoint.',
        'states':[],'crossgrid_sampled_density_spaces':[]}
arrays={};metric_Q={};basis_B={}
for st in base['states']:
 tag=st['tag'];r=st['rows'];assert len(r)==n
 rho=np.array([x['rho'] for x in r]);dr=np.array([x['delta_rho'] for x in r]);dc=np.array(st['dcl'])
 assert dc.shape==(k,) and dr.shape==(n,k)
 gs=next(x for x in grads['states'] if x['tag']==tag);assert gs['state_md5']==st['state_md5']
 gg=gs['gradient_steps'][-1];g=np.array(gg['base_gradient']);dg=np.array(gg['delta_gradient'])
 chosen=next(x for x in invs[chosen_inverse]['states'] if x['tag']==tag)
 Uchosen=np.array([x['base_U'] for x in chosen['rows']]);Wchosen=st['cl']*pts+Uchosen
 nf=abs(rho)+np.sum(abs(Wchosen*g),axis=1);assert np.all(nf>0)
 M=np.vstack([dr/(1+abs(rho[:,None]))/np.sqrt(n),dc])
 matrices={};tails={};entry={'tag':tag,'state_md5':st['state_md5'],'direction_sha256':st['direction_sha256'],
   'gradient_scalar_formula_relative_check':gs['scalar_value_relative_check'],'spaces':{},'inverses':{},'step_comparisons':{}}
 for resolution,inv in invs.items():
  state=next(x for x in inv['states'] if x['tag']==tag)
  assert state['state_md5']==st['state_md5'] and state['direction_sha256']==st['direction_sha256']
  rr=state['rows'];assert np.array_equal(dr,np.array([x['delta_rho'] for x in rr]))
  U=np.array([x['base_U'] for x in rr]);du=np.array([x['delta_U'] for x in rr]);W=st['cl']*pts+U
  bystep={}
  for step in gs['gradient_steps']:
   bg=np.array(step['base_gradient']);ddg=np.array(step['delta_gradient'])
   raw=dc[None,:]*np.einsum('ij,ij->i',pts,bg)[:,None]+np.einsum('ijk,ik->ij',ddg,W)+np.einsum('ijk,ik->ij',du,bg)-dr
   bystep[str(step['relative_step'])]=raw/nf[:,None]/np.sqrt(n)
  matrices[resolution]=bystep
  act=bystep[str(gg['relative_step'])]*np.sqrt(n)
  tb=np.array([float(Fraction(x['base_U_tail_bound_exact'])) for x in rr])
  td=np.array([[float(Fraction(z)) for z in x['delta_U_tail_bounds_exact']] for x in rr])
  tails[resolution]=(tb[:,None]*np.sum(abs(dg),axis=2)+td*np.sum(abs(g),axis=1)[:,None])/nf[:,None]/np.sqrt(n)
  imax=np.argmax(abs(act),axis=0)
  entry['inverses'][resolution]={'max_abs_node_unit_action':np.max(abs(act),axis=0).tolist(),
   'maximizing_point_indices':imax.tolist(),'base_max_abs_R_over_fixed_Nf':float(np.max(abs(np.sum(W*g,axis=1)-rho)/nf)),
   'node_unit_max_tail_bound_using_numerical_gradients':float(np.max(tails[resolution])*np.sqrt(n))}
  arrays[f'{tag}_{resolution}_A']=bystep[str(gg['relative_step'])]
 arrays[f'{tag}_M']=M;arrays[f'{tag}_Nf']=nf;arrays[f'{tag}_gradient']=g;arrays[f'{tag}_delta_gradient']=dg
 for d in (4,10,14):
  Q,T=np.linalg.qr(M[:,:d],mode='reduced');sm=sv(M[:,:d]);assert sm[-1]>1e-10*sm[0]
  metric_Q[(tag,d)]=Q;absinv=abs(np.linalg.solve(T,np.eye(d)))
  space={'metric_singular_values_descending':sm.tolist(),'metric_condition':float(sm[0]/sm[-1]),
   'metric_QR_relative_reconstruction':frob(Q@T-M[:,:d])/frob(M[:,:d]),'metric_Q_orthogonality':frob(Q.T@Q-np.eye(d)),
   'inverses':{},'step_discrepancies':{}}
  Bs={}
  for resolution,ms in matrices.items():
   A=ms[str(gg['relative_step'])][:,:d];B=whitening(A,T);Bs[resolution]=B
   space['inverses'][resolution]={'physical_singular_values_ascending':sv(B)[::-1].tolist(),
    'tail_whitened_Frobenius_upper_using_numerical_gradients':frob(tails[resolution][:,:d]@absinv),
    'whitening_relative_reconstruction':frob(B@T-A)/frob(A)}
   space['step_discrepancies'][resolution]=[]
   for step,aa in ms.items():
    BB=whitening(aa[:,:d],T);delta=BB-B;spec=norm2(delta);ds=float(max(abs(sv(BB)-sv(B))))
    assert ds<=spec*(1+1e-9)+1e-12
    space['step_discrepancies'][resolution].append({'relative_step':float(step),'whitened_Frobenius':frob(delta),
     'whitened_spectral':spec,'max_singular_value_change':ds,'max_node_unit_action_change':float(np.max(abs(aa[:,:d]-ms[str(gg['relative_step'])][:,:d]))*np.sqrt(n))})
   arrays[f'{tag}_{d}_{resolution}_B']=B
  if len(Bs)==2:
   D=Bs['2048']-Bs['4096'];spec=norm2(D);ds=float(max(abs(sv(Bs['2048'])-sv(Bs['4096']))))
   assert ds<=spec*(1+1e-9)+1e-12
   space['inverse_discrepancy']={'whitened_Frobenius':frob(D),'whitened_spectral':spec,
    'max_singular_value_change':ds,'ratio_Frobenius_to_fine_smallest_sv':frob(D)/sv(Bs['4096'])[-1]}
  basis_B[(tag,d)]=Bs[chosen_inverse];entry['spaces'][str(d)]=space
 result['states'].append(entry)
for d in (4,10,14):
 result['crossgrid_sampled_density_spaces'].append({'d':d,'cosines_descending':sv(metric_Q[('n96m40S',d)].T@metric_Q[('n120m48_S',d)]).tolist(),
  'physical_singular_value_ratios96over120_ascending':(sv(basis_B[('n96m40S',d)])[::-1]/sv(basis_B[('n120m48_S',d)])[::-1]).tolist(),
  'qualification':'Same59 sampled coordinates, distinct base-density denominators retained; no continuum-space convergence.'})
name='summary_gradient_refined'+('_4096' if len(invs)==2 else '_2048')
np.savez_compressed(OUT/(name+'_matrices.npz'),**arrays)
(OUT/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(name)
for x in result['states']:
 print(x['tag'],'max10',x['inverses'][chosen_inverse]['max_abs_node_unit_action'][:10])
 for d,s in x['spaces'].items():
  print('d',d,'condition',s['metric_condition'],'singular',s['inverses'][chosen_inverse]['physical_singular_values_ascending'])
  print('steps',s['step_discrepancies'][chosen_inverse]);print('inverse',s.get('inverse_discrepancy'))
