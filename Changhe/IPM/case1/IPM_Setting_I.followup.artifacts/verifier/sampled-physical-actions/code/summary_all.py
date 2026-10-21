"""Common-normalizer finite physical audit, with separate angular/radial comparisons."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from itertools import combinations
import sys,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification'
def load(path):
 raw=path.read_bytes();obj=json.loads(raw);assert obj.get('complete'),str(path)+' incomplete';return obj,hashlib.sha256(raw).hexdigest()
base,bsha=load(V/'actions.json');fd,fsha=load(V/'gradients_refined.json');an,asha=load(V/'gradients_chainrule.json')
assert fd['base_actions_sha256']==bsha and fd['points']==base['points']
invs={'a2048_r24':base};hashes={'a2048_r24':bsha};invs['a4096_r24'],hashes['a4096_r24']=load(ROOT/'refinement4096/actions.json')
if '--radial' in sys.argv:invs['a4096_r32'],hashes['a4096_r32']=load(ROOT/'refinement_radial/actions.json')
chosen=list(invs)[-1];pts=np.array(base['points']);n=len(pts);dim=14
for inv in invs.values():assert inv['points']==base['points']
out={'date':datetime.now(timezone.utc).isoformat(),'normalizer_inverse':chosen,'gradient_step':fd['steps'][-1],'source_inverse_sha256':hashes,'gradient_sha256':fsha,'analytic_gradient_sha256':asha,'states':[],'overlaps':[],
 'scope':'Finite58point14column physical numerator actions. Numerical inverse and derivative differences are not certified error bounds. Exterior estimates use numerical gradients. Positive finite-span costs are upper bounds for larger-space infima. No continuum kernel, isolation, family, smooth candidate or endpoint.'}
arrays={};Qs={};Bs={};sing=lambda x:np.linalg.svd(x,compute_uv=False);frob=lambda x:float(np.linalg.norm(x));whiten=lambda A,T:np.linalg.solve(T.T,A.T).T
for st in base['states']:
 tag=st['tag'];gs=next(x for x in fd['states'] if x['tag']==tag);ans=next(x for x in an['states'] if x['tag']==tag)
 assert gs['state_md5']==ans['state_md5']==st['state_md5']
 states={label:next(x for x in inv['states'] if x['tag']==tag) for label,inv in invs.items()}
 for s in states.values():assert s['state_md5']==st['state_md5'] and s['direction_sha256']==st['direction_sha256'] and len(s['rows'])==n
 rho=np.array([r['rho'] for r in st['rows']]);dr=np.array([r['delta_rho'] for r in st['rows']]);dc=np.array(st['dcl'])
 g=np.array(gs['gradient_steps'][-1]['base_gradient']);dg=np.array(gs['gradient_steps'][-1]['delta_gradient'])
 wc=st['cl']*pts+np.array([r['base_U'] for r in states[chosen]['rows']]);nf=abs(rho)+np.sum(abs(wc*g),axis=1);assert np.all(nf>0)
 M=np.vstack([dr/(1+abs(rho[:,None]))/np.sqrt(n),dc]);arr={};tails={};methods={}
 entry={'tag':tag,'state_md5':st['state_md5'],'direction_sha256':st['direction_sha256'],'inverse_diagnostics':{},'spaces':{}}
 for label,s in states.items():
  rr=s['rows'];assert np.array_equal(dr,np.array([r['delta_rho'] for r in rr]))
  U=np.array([r['base_U'] for r in rr]);du=np.array([r['delta_U'] for r in rr]);W=st['cl']*pts+U
  def action(bg,ddg):return (dc[None,:]*np.sum(pts*bg,axis=1)[:,None]+np.einsum('ijk,ik->ij',ddg,W)+np.einsum('ijk,ik->ij',du,bg)-dr)/nf[:,None]/np.sqrt(n)
  arr[label]=action(g,dg);methods[label]={str(step['relative_step']):action(np.array(step['base_gradient']),np.array(step['delta_gradient'])) for step in gs['gradient_steps']}
  methods[label]['analytic_chainrule']=action(np.array(ans['base_gradient']),np.array(ans['delta_gradient']))
  tbase=np.array([float(Fraction(r['base_U_tail_bound_exact'])) for r in rr]);td=np.array([[float(Fraction(z)) for z in r['delta_U_tail_bounds_exact']] for r in rr]);tails[label]=(tbase[:,None]*np.sum(abs(dg),axis=2)+td*np.sum(abs(g),axis=1)[:,None])/nf[:,None]/np.sqrt(n)
  acts=arr[label]*np.sqrt(n);res=(np.sum(W*g,axis=1)-rho)/nf
  entry['inverse_diagnostics'][label]={'max_abs_node_actions':np.max(abs(acts),axis=0).tolist(),'maximizing_point_indices':np.argmax(abs(acts),axis=0).tolist(),'base_max_R_fixed_Nf':float(max(abs(res))),'base_max_point_index':int(np.argmax(abs(res)))}
  arrays[tag+'_'+label+'_A']=arr[label]
 arrays[tag+'_M']=M;arrays[tag+'_Nf']=nf
 for d in [4,10,14]:
  Q,T=np.linalg.qr(M[:,:d],mode='reduced');svm=sing(M[:,:d]);assert svm[-1]>1e-10*svm[0];Qs[tag,d]=Q;space={'metric_condition':float(svm[0]/svm[-1]),'metric_singular_values_descending':svm.tolist(),'inverses':{},'inverse_differences':[]};mat={}
  for label,A in arr.items():
   B=whiten(A[:,:d],T);mat[label]=B;Bs[tag,d,label]=B;arrays[f'{tag}_{d}_{label}_B']=B
   QR,RR=np.linalg.qr(A[:,:d],mode='reduced');svr=sing(RR);assert svr[-1]>1e-12*svr[0]
   ell=np.linalg.solve(RR.T,dc[:d]);cost=1/np.linalg.norm(ell);v=np.linalg.solve(RR,ell)*cost**2
   assert abs(dc[:d]@v-1)<1e-9 and abs(np.linalg.norm(A[:,:d]@v)/cost-1)<1e-9
   methodsums={}
   for name,AA in methods[label].items():
    BB=whiten(AA[:,:d],T);D=BB-B;spec=float(np.linalg.norm(D,2));change=float(max(abs(sing(BB)-sing(B))));assert change<=spec*(1+1e-9)+1e-12
    methodsums[name]={'Frobenius':frob(D),'spectral':spec,'maximum_singular_change':change,'maximum_node_action_change':float(np.max(abs(AA[:,:d]-A[:,:d]))*np.sqrt(n))}
   space['inverses'][label]={'physical_singular_values_ascending':sing(B)[::-1].tolist(),'whitening_relative_reconstruction':frob(B@T-A[:,:d])/frob(A[:,:d]),'tail_Frobenius_bound_using_numerical_gradients':frob(tails[label][:,:d]@abs(np.linalg.solve(T,np.eye(d)))),'derivative_differences':methodsums,'cl_cost':float(cost),'cl_cost_minimizer':v.tolist(),'cl_cost_constraint':float(dc[:d]@v),'node_action_condition':float(svr[0]/svr[-1])}
  for a,b in combinations(mat,2):
   D=mat[a]-mat[b];spec=float(np.linalg.norm(D,2));change=float(max(abs(sing(mat[a])-sing(mat[b]))));assert change<=spec*(1+1e-9)+1e-12
   space['inverse_differences'].append({'from':a,'to':b,'Frobenius':frob(D),'spectral':spec,'maximum_singular_change':change,'Frobenius_over_second_smallest':frob(D)/sing(mat[b])[-1]})
  entry['spaces'][str(d)]=space
 out['states'].append(entry)
for d in [4,10,14]:
 out['overlaps'].append({'d':d,'cosines_descending':sing(Qs['n96m40S',d].T@Qs['n120m48_S',d]).tolist(),'physical_sv_ratios96over120_ascending':(sing(Bs['n96m40S',d,chosen])[::-1]/sing(Bs['n120m48_S',d,chosen])[::-1]).tolist(),'scope':'Same59coordinate sampling with distinct base-density denominators, no continuum-space claim.'})
name='summary_all_'+('radial' if '--radial' in sys.argv else 'angular');out['complete']=True
(V/(name+'.json')).write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(V/(name+'_matrices.npz'),**arrays)
for e in out['states']:
 print(e['tag'],flush=True)
 for d,s in e['spaces'].items():
  print('d',d,'condition',s['metric_condition'],'smallest',s['inverses'][chosen]['physical_singular_values_ascending'][0],'clcost',s['inverses'][chosen]['cl_cost'],'tail',s['inverses'][chosen]['tail_Frobenius_bound_using_numerical_gradients'],flush=True)
  print('inverse differences',s['inverse_differences'],flush=True)
  print('derivative differences',s['inverses'][chosen]['derivative_differences'],flush=True)
print('COMPLETE',name,flush=True)
