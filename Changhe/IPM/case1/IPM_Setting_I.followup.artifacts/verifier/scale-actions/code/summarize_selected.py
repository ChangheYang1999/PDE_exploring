from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'refinement_selected'
mainpath=ROOT/'verification/actions.json';refpath=OUT/'actions.json'
main=json.loads(mainpath.read_text());ref=json.loads(refpath.read_text());partial='--partial' in sys.argv
assert len(main['points'])==58 and main['config']=={'nang':4096,'order':32,'panel':.075,'rmax':'1e30','relative_steps':[.00003125,.0000625]}
assert ref.get('complete') or partial
assert main.get('complete') or partial
indices=np.array(ref['indices']);pts=np.array(main['points']);assert np.array_equal(pts[indices],ref['points'])
out={'date':datetime.now(timezone.utc).isoformat(),'complete':bool(main.get('complete') and ref.get('complete')),'indices':indices.tolist(),'number_of_output_rows':len(indices),'full_domain_rows':59,'normalization':'main finest FD gradient and N_f, divisor sqrt58, full58point density plus c_l domain QR','main_sha256':hashlib.sha256(mainpath.read_bytes()).hexdigest(),'refinement_sha256':hashlib.sha256(refpath.read_bytes()).hexdigest(),'scope':'Angular and radial sensitivity on these12prescribedoutputrows ONLY. Not a58row matrix error bound, continuum norm or certified quadrature error.','states':[]};arrays={}
for st in main['states']:
 if len(st['rows'])!=58:
  assert partial;continue
 tag=st['tag'];ss=[z for z in ref['states'] if z['tag']==tag];assert len(ss)==1;ss=ss[0];assert ss['source_md5']==st['state_md5']
 pass_rows={r['config']['nang']:r['rows'] for r in ss['passes']}
 if set(pass_rows)!={2048,4096} or any(len(rows)!=len(indices) for rows in pass_rows.values()):
  assert partial;continue
 dirs=np.load(ROOT/'data'/('directions_'+tag+'.npz'))['V'];assert np.array_equal(dirs,np.load(OUT/('directions_'+tag+'.npy')))
 rows=st['rows'];rho=np.array([r['rho'] for r in rows]);dr=np.array([r['delta_rho'] for r in rows]);dc=dirs[-2];M=np.vstack([dr/(1+abs(rho[:,None]))/np.sqrt(58),dc]);N=np.array([r['N_report_f'] for r in rows])[indices];g=np.array([r['gradient'] for r in rows])[indices];dg=np.array([r['delta_gradient'] for r in rows])[indices]
 u_main=np.array([rows[i]['base_U'] for i in indices]);du_main=np.array([rows[i]['delta_U'] for i in indices]);values={4096:(u_main,du_main)}
 for angle,rr in pass_rows.items():
  assert np.array_equal([r['index'] for r in rr],indices) and np.array_equal([r['point'] for r in rr],pts[indices]);values[f'order24_{angle}']=(np.array([r['base_U'] for r in rr]),np.array([r['delta_U'] for r in rr]))
 entry={'tag':tag,'state_md5':st['state_md5'],'spaces':{},'max_velocity_changes':{}}
 comparisons={'angular':('order24_2048','order24_4096'),'radial':('order24_4096',4096)}
 action_diffs={}
 for label,(a,b) in comparisons.items():
  bu,bdu=values[b];au,adu=values[a];eu=bu-au;edu=bdu-adu
  E=(np.einsum('ijk,ik->ij',dg,eu)+np.einsum('ijk,ik->ij',edu,g))/N[:,None]/np.sqrt(58);action_diffs[label]=E;arrays[f'{tag}_{label}_node_action_difference']=E
  entry['max_velocity_changes'][label]={'base_max':float(np.max(abs(eu))),'direction_max':float(np.max(abs(edu))),'base_action_fixed_Nf_max':float(np.max(abs(np.sum(eu*g,axis=1))/N))}
 for k in(4,10,14):
  Q,T=np.linalg.qr(M[:,:k],mode='reduced');entry['spaces'][str(k)]={}
  for label,E in action_diffs.items():
   B=np.linalg.solve(T.T,E[:,:k].T).T;arrays[f'{tag}_{k}_{label}_whitened_difference']=B
   entry['spaces'][str(k)][label]={'Frobenius':float(np.linalg.norm(B)),'spectral':float(np.linalg.norm(B,2)),'max_entry':float(np.max(abs(B)))}
 out['states'].append(entry)
name='summary_partial' if partial else 'summary'
(OUT/(name+'.json')).write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(OUT/(name+'_matrices.npz'),**arrays)
for st in out['states']:
 print(st['tag'],st['max_velocity_changes']);print(st['spaces']['14'])
print('COMPLETE_STATES',len(out['states']),'complete',out['complete'])
