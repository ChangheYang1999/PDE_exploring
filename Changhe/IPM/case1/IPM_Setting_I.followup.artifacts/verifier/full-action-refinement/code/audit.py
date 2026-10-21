"""Independent SVD coordinates and scalar-loop reconstruction of saved finite actions."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
import numpy as np
R=Path(__file__).resolve().parents[1];V=R/'verification'
p=argparse.ArgumentParser();p.add_argument('case',choices=['72','L16']);args=p.parse_args()
folder,tag={'72':('third-grid-actions','n72m30S'),'L16':('scale-actions','n96m40SL16')}[args.case]
mainpath=R.parent/folder/'verification/actions.json';refpath=V/(tag+'_actions.json');summarypath=V/(tag+'_summary.json')
main=json.loads(mainpath.read_text());ref=json.loads(refpath.read_text());summary=json.loads(summarypath.read_text());z=np.load(V/(tag+'_summary.npz'));st=next(t for t in main['states'] if t['tag']==tag)
assert main['complete'] and ref['complete'] and summary['rows']==58
assert summary['main_sha256']==hashlib.sha256(mainpath.read_bytes()).hexdigest() and summary['refinement_sha256']==hashlib.sha256(refpath.read_bytes()).hexdigest()
for key,digest in ref['pins'].items():assert hashlib.sha256((R.parent.parent/ref['files'][key]).read_bytes()).hexdigest()==digest
assert ref['rmax']=='1e30' and ref['points']==main['points']
M=z['M'];checks=[];vel={'main':st['rows']}
for rule in ref['passes']:vel[str(rule['config']['nang'])]=rule['rows']
for name in ['main','2048','4096']:
 raw=np.empty((58,14))
 for i,row in enumerate(st['rows']):
  x=np.array(row['point']);u=np.array(vel[name][i]['base_U']);grad=np.array(row['gradient'])
  for j in range(14):
   dh=np.array(row['delta_gradient'][j]);dv=np.array(vel[name][i]['delta_U'][j]);dc=M[-1,j]
   raw[i,j]=((st['cl']*x+u)@dh+(dc*x+dv)@grad-row['delta_rho'][j])/(row['N_report_f']*np.sqrt(58))
 assert np.max(abs(raw-z[name]))<1e-11
 for k in [4,10,14]:
  _,sm,vhm=np.linalg.svd(M[:,:k],full_matrices=False);C=vhm.T/sm
  assert np.linalg.norm((M[:,:k]@C).T@(M[:,:k]@C)-np.eye(k))<1e-10
  sv=np.linalg.svd(raw[:,:k]@C,compute_uv=False)[::-1]
  target=summary['spaces'][str(k)]['rules'][name]
  assert np.allclose(sv,target['singular_values_ascending'],rtol=1e-9,atol=1e-12)
  _,sa,vha=np.linalg.svd(raw[:,:k],full_matrices=False);dual=(vha@M[-1,:k])/sa;cost=1/np.linalg.norm(dual)
  coeff=vha.T@(dual/sa)*cost**2
  assert abs(M[-1,:k]@coeff-1)<1e-9 and abs(np.linalg.norm(raw[:,:k]@coeff)/cost-1)<1e-9
  assert abs(cost/target['unit_cl_cost']-1)<1e-8
  checks.append({'rule':name,'dimension':k,'SVD_coordinate_sigma_min':float(sv[0]),'SVD_unit_cl_cost':float(cost),'scalar_reconstruction_max_error':float(np.max(abs(raw-z[name])))})
out={'utc':datetime.now(timezone.utc).isoformat(),'tag':tag,'checks':checks,'verdict':'PASS','scope':'Different matrix factorization and scalar-loop action reconstruction; no new inverse evaluation or rigorous floating-point certificate.','pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [mainpath,refpath,summarypath,V/(tag+'_summary.npz'),Path(__file__)]}}
(V/(tag+'_audit.json')).write_text(json.dumps(out,indent=2)+'\n');print('PASS',tag,len(checks))
