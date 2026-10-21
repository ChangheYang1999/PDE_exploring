"""Authenticate and independently reconstruct source arrays; no inverse execution."""
from pathlib import Path
import hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,message):
 if not ok:raise RuntimeError(message)
def load(rel):
 p=BASE/rel;return json.loads(p.read_text())
def state(o,tag):return next(s for s in o['states'] if s['tag']==tag)
def construct(points,weights,rho,dr,g,dg,U,V,cl,dc,normalizer_gradient):
 points=np.asarray(points);weights=np.asarray(weights);rho=np.asarray(rho);dr=np.asarray(dr);g=np.asarray(g);dg=np.asarray(dg);U=np.asarray(U);V=np.asarray(V);dc=np.asarray(dc);ng=np.asarray(normalizer_gradient)
 n=len(points);W=cl*points+U;nf=np.empty(n);M=np.empty((n+1,14));A=np.empty((n,14))
 for i in range(n):
  nf[i]=abs(rho[i])+sum(abs(W[i,b]*ng[i,b]) for b in range(2));need(nf[i]>0,'nonpositive normalizer')
  for j in range(14):
   M[i,j]=np.sqrt(weights[i])*dr[i,j]/(1+abs(rho[i]));total=-dr[i,j]
   for b in range(2):total+=dc[j]*points[i,b]*g[i,b]+W[i,b]*dg[i,j,b]+V[i,j,b]*g[i,b]
   A[i,j]=np.sqrt(weights[i])*total/nf[i]
 M[-1]=dc;return M,A,nf
def authenticate(plan):
 for rel,h in plan['pins'].items():need(sha(BASE/rel)==h,'changed pinned source '+rel)
def old_arrays(tag):
 if tag=='n72m30S':
  folder='verifier/third-grid-actions';r=load(folder+'/verification/actions.json');s=load(folder+'/verification/summary.json');rs=state(r,tag)
  need(r['complete'] and s['complete'],'old completion');need(sha(BASE/folder/'verification/actions.json')==s['new_actions_sha256'],'old action hash')
  rr=rs['rows'];g=[x['gradient'] for x in rr];dg=[x['delta_gradient'] for x in rr];need(r['config']['relative_steps'][0]==1/32000,'72 step');mp=BASE/folder/'verification/summary_matrices.npz';key=tag+'_A'
 else:
  folder='verifier/sampled-physical-actions';r=load(folder+'/refinement_radial/actions.json');b=load(folder+'/verification/actions.json');s=load(folder+'/verification/summary_all_radial.json');fd=load(folder+'/verification/gradients_refined.json');rs=state(r,tag);bs=state(b,tag);fs=state(fd,tag)
  need(all(x['complete'] for x in [r,b,s,fd]),'old completion');need(r['points']==b['points']==fd['points'],'old points');need(rs['state_md5']==bs['state_md5']==fs['state_md5'],'old states')
  need(s['normalizer_inverse']=='a4096_r32' and s['gradient_step']==1/32000,'old normalizer convention')
  need(sha(BASE/folder/'refinement_radial/actions.json')==s['source_inverse_sha256']['a4096_r32'],'radial source hash');need(sha(BASE/folder/'verification/actions.json')==fd['base_actions_sha256']==s['source_inverse_sha256']['a2048_r24'],'base source hash');need(sha(BASE/folder/'verification/gradients_refined.json')==s['gradient_sha256'],'gradient source hash')
  gs=fs['gradient_steps'][-1];need(gs['relative_step']==1/32000,'old step');g=gs['base_gradient'];dg=gs['delta_gradient'];rr=rs['rows'];need([x['rho'] for x in rr]==[x['rho'] for x in bs['rows']],'old density');need([x['delta_rho'] for x in rr]==[x['delta_rho'] for x in bs['rows']],'old directions');mp=BASE/folder/'verification/summary_all_radial_matrices.npz';key=tag+'_a4096_r32_A'
 need({k:r['config'][k] for k in ['nang','order','panel','rmax']}=={'nang':4096,'order':32,'panel':.075,'rmax':'1e30'},'old inverse rule')
 need(len(rr)==58 and [x['point'] for x in rr]==r['points'],'old row order')
 M,A,nf=construct(r['points'],np.full(58,1/58),[x['rho'] for x in rr],[x['delta_rho'] for x in rr],g,dg,[x['base_U'] for x in rr],[x['delta_U'] for x in rr],rs['cl'],rs['dcl'],g)
 z=np.load(mp);need(np.allclose(M,z[tag+'_M'],rtol=2e-13,atol=1e-14),'old M reconstruction');need(np.allclose(A,z[key],rtol=2e-10,atol=5e-13),'old A reconstruction')
 dirs=BASE/folder/'data'/('directions_'+tag+'.npz');need(sha(dirs)==rs['direction_sha256'],'old direction hash');need(np.array_equal(np.load(dirs)['V'][-2],M[-1]),'old parameter row')
 return z[tag+'_M'],z[key],nf,rs,dirs,mp

def all_arrays(tag,plan):
 authenticate(plan);M1,A1,n1,rs,dirs,mp=old_arrays(tag);need(hashlib.md5((BASE/plan['state_paths'][tag]).read_bytes()).hexdigest()==rs['state_md5'],'old frozen state MD5');folder=BASE/'verifier/gauss-sampled-actions/verification';rp=folder/(tag+'_actions.json');sp=folder/(tag+'_summary.json');gp=folder/(tag+'_matrices.npz');r=json.loads(rp.read_text());s=json.loads(sp.read_text());z=np.load(gp)
 need(r['complete'] and s['complete'],'Gauss completion');need(sha(rp)==s['actions_sha256'],'Gauss action hash');need(s['summary_code_sha256']==plan['pins']['verifier/gauss-sampled-actions/code/summarize.py'],'Gauss summary code')
 for rel,h in r['pins'].items():need(sha(BASE/rel)==h,'Gauss dependency '+rel)
 for rel in ['verifier/gauss-sampled-actions/PROOF.md','verifier/gauss-sampled-actions/code/run.py','verifier/inverse/code/density.py']:need(r['pins'][rel]==plan['pins'][rel],'Gauss recorded convention '+rel)
 gd=folder.parent/'data'/dirs.name;need(gd.read_bytes()==dirs.read_bytes(),'ordered directions differ');need(r['state_md5']==s['state_md5']==rs['state_md5'],'base state differs');need(np.array_equal(r['dcl'],M1[-1]),'parameter row differs')
 pp=load('verifier/gauss-sampled-actions/verification/points.json');need(r['points']==pp['points'] and r['weights']==pp['weights'],'Gauss nodes/weights differ');need(len(r['field_rows'])==64,'Gauss field count');need([x['point'] for x in r['field_rows']]==r['points'],'Gauss field order')
 cfg={'nang':4096,'order':24,'panel':.1,'rmax':'1e30'};pa=next(x for x in r['passes'] if x['config']==cfg);pr=pa['rows'];fr=r['field_rows'];need(len(pr)==64 and [x['point'] for x in pr]==r['points'],'Gauss velocity order')
 M2,A2,n2=construct(r['points'],r['weights'],[x['rho'] for x in fr],[x['delta_rho'] for x in fr],[x['FD_gradient'] for x in fr],[x['FD_delta_gradient'] for x in fr],[x['base_U'] for x in pr],[x['delta_U'] for x in pr],r['c_l'],r['dcl'],[x['gradient'] for x in fr])
 need(np.allclose(M2,z['M'],rtol=2e-13,atol=1e-14),'Gauss M reconstruction');need(np.allclose(A2,z['FD'],rtol=2e-10,atol=5e-13),'Gauss FD reconstruction');need(np.allclose(n2,z['Nf'],rtol=2e-13,atol=1e-14),'Gauss normalizers')
 return M1,A1,z['M'],z['FD'],r,s,[mp,dirs,rp,sp,gp,gd],{'old_source_reconstruction':'all entries checked against raw scalar reconstruction','Gauss_max_action_reconstruction':float(np.max(abs(A2-z['FD']))),'normalizer_conventions':'58 stencil,64 analytic; both finer velocity','stencil_order':8,'h':'max(1,abs(x),abs(y))/32000','inverse58':{'nang':4096,'order':32,'panel':.075,'rmax':'1e30'},'inverse64':cfg}
if __name__=='__main__':
 plan=load('verifier/combined-sampling/verification/plan.json');authenticate(plan)
 for t in plan['states']:old_arrays(t);print('OLD_SOURCE_PASS',t)
