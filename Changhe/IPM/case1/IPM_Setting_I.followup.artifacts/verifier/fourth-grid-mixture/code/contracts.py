"""Own raw-scalar reconstruction and authentication of both fourth-grid samples."""
from pathlib import Path
import hashlib,json,importlib.util,importlib.machinery
import numpy as np
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1]
spec=importlib.util.spec_from_file_location('prior_scalar_contract',BASE/'verifier/combined-sampling/code/contracts.py')
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
construct=prior.construct
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,message):
 if not ok:raise RuntimeError(message)
def local(rel):
 p=Path(rel);p=(p if p.is_absolute() else BASE/p).resolve()
 need(p.is_relative_to(BASE.resolve()),'nonlocal pin '+str(rel));return p
def authenticate(plan):
 for rel,h in plan['pins'].items():need(sha(local(rel))==h,'changed source '+rel)
def audit_link(a,files,code,plan):
 need(a['verdict']=='PASS','audit verdict')
 recorded={local(rel):h for rel,h in a['pins'].items()}
 for p,h in recorded.items():need(sha(p)==h,'audit recorded pin '+str(p))
 for p in [*files,code]:need(recorded.get(p.resolve())==sha(p),'audit missing exact input '+str(p))
 need(recorded[code.resolve()]==plan['pins'][str(code.relative_to(BASE))],'audit code not registered')
def producer_pins(pins,folder,plan):
 for rel,h in pins.items():need(sha(local(rel))==h,'producer recorded pin '+rel)
 for rel in [folder+'/PROOF.md',folder+'/code/run.py','verifier/inverse/code/density.py']:
  need(rel in pins and pins[rel]==plan['pins'][rel],'required producer convention pin '+rel)
def stencil_contract(plan):
 # These source formats do not both record FD metadata. Establish the convention
 # by the inspected, pinned call sites and their field-name mappings instead.
 ep=ROOT/'verification/stencil_evidence.json';e=json.loads(ep.read_text())
 for rel,h in e['source_pins'].items():need(h==plan['pins'][rel]==sha(local(rel)),'stencil evidence pin '+rel)
 for rel,fragments in e['required_source_fragments'].items():
  text=local(rel).read_text()
  for fragment in fragments:need(fragment in text,'changed stencil call site '+fragment)
 need(e['order']==8 and e['relative_steps']==[1/32000,1/16000],'stencil convention')
 ip=ROOT/'verification/import_resolution.json';resolution=json.loads(ip.read_text())
 for folder,modules in resolution['resolutions'].items():
  search=[str(BASE/p)for p in resolution['search_order']+[folder]]
  for name,expected in modules.items():
   spec=importlib.machinery.PathFinder.find_spec(name,search)
   need(spec is not None and spec.origin is not None,'missing module '+name)
   origin=Path(spec.origin).resolve();need(origin==local(expected['file']) and sha(origin)==expected['sha256']==plan['pins'][expected['file']],'module resolution changed '+name)
 return e
def all_arrays(tag,plan):
 need(tag=='n84m35S','unexpected state');authenticate(plan);se=stencil_contract(plan)
 f1=BASE/'verifier/fourth-grid-actions';f2=BASE/'verifier/fourth-grid-gauss'
 p1=f1/'verification/actions.json';s1p=f1/'verification/summary.json';z1p=f1/'verification/summary_matrices.npz';a1p=f1/'verification/summary_audit.json'
 r=json.loads(p1.read_text());s=json.loads(s1p.read_text());z1=np.load(z1p,allow_pickle=False);a1=json.loads(a1p.read_text())
 need(r['complete'] and s['complete'],'primary incomplete');need(sha(p1)==s['new_actions_sha256'],'primary hash')
 audit_link(a1,[p1,s1p,z1p],f1/'code/audit_summary.py',plan)
 need(s['code_sha256']==plan['pins']['verifier/fourth-grid-actions/code/summarize.py'],'primary summary code')
 need(len(r['states'])==len(s['states'])==1,'primary state count')
 st=r['states'][0];sm=s['states'][0];need(st['tag']==sm['tag']==tag,'primary tag');rr=st['rows']
 need(len(rr)==58 and [x['point'] for x in rr]==r['points'],'primary row order')
 primary_points=BASE/'verifier/sampled-physical-actions/verification/points.json'
 need(r['point_sha256']==sha(primary_points),'primary point hash')
 point_design=json.loads(primary_points.read_text())
 need(r['points']==point_design['points'],'primary fixed points')
 need({k:r['config'][k]for k in ['nang','order','panel','rmax']}=={'nang':4096,'order':32,'panel':.075,'rmax':'1e30'},'primary rule')
 need(r['config']['relative_steps']==se['relative_steps'],'primary stencil steps')
 producer_pins(st['pins'],'verifier/fourth-grid-actions',plan)
 dirs=f1/'data/directions_n84m35S.npz';data=f1/'data/dnB_n84m35S.npz'
 need(sha(dirs)==st['direction_sha256'],'primary directions');need(hashlib.md5(data.read_bytes()).hexdigest()==st['state_md5'],'primary state')
 with np.load(dirs,allow_pickle=False) as dz:need(np.array_equal(dz['V'][-2],st['dcl']),'parameter row versus frozen directions')
 with np.load(data,allow_pickle=False) as dz:
  state_cl=float(dz['c_l']) if 'c_l' in dz else float(dz['cl'])
 need(st['cl']==state_cl,'primary c_l versus frozen state')
 M1,A1,n1=construct(r['points'],np.full(58,1/58),[x['rho']for x in rr],[x['delta_rho']for x in rr],[x['gradient']for x in rr],[x['delta_gradient']for x in rr],[x['base_U']for x in rr],[x['delta_U']for x in rr],st['cl'],st['dcl'],[x['gradient']for x in rr])
 need(np.allclose(M1,z1[tag+'_M'],rtol=2e-13,atol=1e-14),'primary M');need(np.allclose(A1,z1[tag+'_A'],rtol=2e-10,atol=5e-13),'primary A')
 need(np.allclose(n1,[x['N_report_f']for x in rr],rtol=2e-13,atol=1e-14),'primary stored raw N_f')
 need({(x['state'],x['dimension'])for x in a1['checks']}=={(tag,k)for k in [4,10,14]} and len(a1['checks'])==3,'primary named audit checks')
 for x in a1['checks']:
  target=sm['spaces'][str(x['dimension'])]['unit_cl_cost']
  need(x['metric_reconstruction_error']<1e-10 and target>0 and abs(x['svd_cost']/target-1)<1e-10 and abs(x['QR_cost']/target-1)<1e-10,'primary individual audit check')
 need(len(a1['raw_scalar_checks'])==1,'primary scalar check count');sc=a1['raw_scalar_checks'][0]
 need(sc['state']==tag and sc['entries']==58*14 and sc['max_action_difference']<1e-11 and sc['max_metric_difference']<1e-13,'primary scalar audit')
 p2=f2/'verification'/f'{tag}_actions.json';s2p=f2/'verification'/f'{tag}_summary.json';z2p=f2/'verification'/f'{tag}_matrices.npz';a2p=f2/'verification'/f'{tag}_audit.json'
 g=json.loads(p2.read_text());gs=json.loads(s2p.read_text());z2=np.load(z2p,allow_pickle=False);ga=json.loads(a2p.read_text())
 need(g['complete'] and gs['complete'],'Gauss completion');audit_link(ga,[p2,s2p,z2p],f2/'code/audit_summary.py',plan)
 need(sha(p2)==gs['actions_sha256'],'Gauss action hash');need(gs['summary_code_sha256']==plan['pins']['verifier/fourth-grid-gauss/code/summarize.py'],'Gauss summary code')
 producer_pins(g['pins'],'verifier/fourth-grid-gauss',plan)
 need((f2/'data'/dirs.name).read_bytes()==dirs.read_bytes(),'ordered directions mismatch');need((f2/'data'/data.name).read_bytes()==data.read_bytes(),'density mismatch')
 need(st['state_md5']==g['state_md5']==gs['state_md5'],'state mismatch');need(np.array_equal(st['dcl'],g['dcl']),'parameter mismatch');need(st['cl']==g['c_l'],'base c_l mismatch')
 pp=f2/'verification/points.json';ps=json.loads(pp.read_text());need(g['points']==ps['points'] and g['weights']==ps['weights'],'Gauss design')
 weights=np.array(g['weights']);need(weights.shape==(64,) and np.all(weights>0) and abs(weights.sum()-1)<1e-14,'positive unit Gauss weights')
 fr=g['field_rows'];cfg={'nang':4096,'order':24,'panel':.1,'rmax':'1e30'};selected=[x['rows']for x in g['passes']if x['config']==cfg];need(len(selected)==1,'one fine Gauss pass');vr=selected[0]
 need(len(fr)==len(vr)==64 and [x['point']for x in fr]==[x['point']for x in vr]==g['points'],'Gauss ordering')
 need(g['cpu_gpu_density_checked_points']==64 and g['cpu_gpu_density_max_scaled_error']<1e-10,'Gauss density audit')
 M2,A2,n2=construct(g['points'],g['weights'],[x['rho']for x in fr],[x['delta_rho']for x in fr],[x['FD_gradient']for x in fr],[x['FD_delta_gradient']for x in fr],[x['base_U']for x in vr],[x['delta_U']for x in vr],g['c_l'],g['dcl'],[x['gradient']for x in fr])
 need(np.allclose(M2,z2['M'],rtol=2e-13,atol=1e-14),'Gauss M');need(np.allclose(A2,z2['FD'],rtol=2e-10,atol=5e-13),'Gauss A');need(np.allclose(n2,z2['Nf'],rtol=2e-13,atol=1e-14),'Gauss Nf')
 need({(x['rule'],x['dimension'])for x in ga['checks']}=={(rule,k)for rule in ['2048','4096','FD','FD2']for k in [4,10,14]} and len(ga['checks'])==12,'Gauss named audit checks')
 for x in ga['checks']:
  target=gs['spaces'][str(x['dimension'])]['rules'][x['rule']]
  need(x['max_scalar_action_difference']<1e-11 and x['SVD_sigma_min']>0 and abs(x['SVD_sigma_min']/target['physical_singular_values_ascending'][0]-1)<1e-8 and abs(x['SVD_cost']/target['unit_cl_cost']-1)<1e-8,'Gauss individual audit check')
 source=[p1,s1p,z1p,a1p,p2,s2p,z2p,a2p,dirs,data,f2/'data'/dirs.name,f2/'data'/data.name,pp,primary_points,ROOT/'verification/stencil_evidence.json',ROOT/'verification/import_resolution.json',ROOT/'verification/runtime_observation.json']
 record={'primary_max_action_reconstruction':float(np.max(abs(A1-z1[tag+'_A']))),'Gauss_max_action_reconstruction':float(np.max(abs(A2-z2['FD']))),'normalizers':'primary stencil;Gauss analytic;finer velocity in each','primary_normalizer_storage':'raw rows N_report_f; primary npz has no Nf','stencil_order':se['order'],'step':se['step'],'stencil_provenance':'source configurations incomplete; inspected pinned producer calls, field mappings and density stencil establish convention','inverse58':r['config'],'inverse64':cfg}
 return M1,A1,M2,A2,g,gs,source,record
