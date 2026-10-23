from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path('verification');assert not sys.flags.optimize and Path.cwd().resolve()==ROOT
R=ROOT/'research/primary_direct_quadrature_spotcheck';V=R/'verification';dest=V/'CHECKS.json';assert not dest.exists();checks=[];bindings={}
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'PROOF.md',R/'DESIGN_REPAIRS_PROOF.md',V/'JOB.json',ROOT/'runs/launch_337.sh']:bind(p)
a=json.loads(bind(V/'DESIGN_ACCEPTANCE.json'));ck('design accepted',a['status']=='ACCEPTED_DIRECT_PRIMARY_DESIGN')
for p,h in a['bindings'].items():bind(p,h)
r=json.loads(bind(V/'RESULTS.json'));ck('completed',r['status']=='COMPLETE_DIRECT_PRIMARY_QUADRATURE');ck('three orders',[x['order']for x in r['rows']]==[96,192,384]);ck('resource records',r['nice']==19 and all(x=='1'for x in r['environment'].values())and all(0<x<=14*1024**3 for x in r['memory_limits']));ex=json.loads(bind(V/'JOB_EXIT.json'));ck('exit zero',ex['returncode']==0)
ref=json.loads(bind(ROOT/'research/primary_fresh_sample/verification/candidate/N44_d110.json'));p=ref['points'][20];ck('source identity',ref['source_sha256']==r['source_sha256']);ck('exact point',r['point']['index']==20 and r['point']['hex']==[float(p[k]).hex()for k in ['x','y']])
for x in r['local_checks']:ck('local direct and reference '+x['field'],max(F(x['direct_scaled_difference']),F(x['reference_scaled_difference']))<F('1e-60'))
for x in r['source_checks']:ck('actual source '+str((x['radius'],x['theta'])),F(x['scaled_difference'])<F('1e-60'))
summary=[]
for row in r['rows']:
 v={k:F(z)for k,z in row['values'].items()};x,y,g,gx,gy,u,w=[v[k]for k in ['x','y','rho','rho_x','rho_y','U1','U2']];tx=(F(5,2)*x+u)*gx;ty=(F(5,2)*y+w)*gy;rr=tx+ty-g;nf=abs(tx)+abs(ty)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(u*gx+w*gy);comb=dict(R=rr,Nf=nf,Nv=nv,R_Nf=abs(rr)/nf,R_Nv=abs(rr)/nv)
 for k,z in comb.items():ck('recombine '+str((row['order'],k)),abs(z-v[k])/max(1,abs(z),abs(v[k]))<F('1e-65'))
 for k,z in v.items():ck('reference difference '+str((row['order'],k)),abs((z-F(p[k]))-F(row['differences'][k]))/max(1,abs(z),abs(F(p[k])))<F('1e-65'))
 for k in ['psi','U1','U2']:ck('inverse comparison '+str((row['order'],k)),abs(F(row['differences'][k]))/max(F(1),abs(F(p[k])))<=F('1e-8'))
 ck('residual normalized difference '+str(row['order']),abs(F(row['differences']['R']))/F(p['Nf'])<=F('1e-9'))
 c=row['conditioning'];scale=abs(gx)*F(c['U1_scale'])+abs(gy)*F(c['U2_scale']);ck('scale propagation '+str(row['order']),abs(scale-F(c['R_scale']))/max(1,scale)<F('1e-65'));ck('epsilon indicator '+str(row['order']),abs(scale/F(2**52)-F(c['epsilon_R_indicator']))/max(1,scale)<F('1e-65'))
 summary.append(dict(order=row['order'],R=float(v['R']),Nf=float(v['Nf']),Nv=float(v['Nv']),R_Nf=float(v['R_Nf']),R_Nv=float(v['R_Nv']),differences={k:float(F(z))for k,z in row['differences'].items()},normalized_residual_difference=float(F(row['differences']['R'])/F(p['Nf'])),R_roundoff_indicator=float(F(c['epsilon_R_indicator'])),scope='roundoff indicator is not an error bound'))
for a,row in zip(r['order_sensitivity'],r['rows'][:-1]):
 ck('order sensitivity label '+str(a['order']),a['order']==row['order'])
 for k,z in a['difference_from384'].items():ck('order sensitivity '+str((a['order'],k)),F(z)==F(row['values'][k])-F(r['rows'][-1]['values'][k]))
for p,h in bindings.items():ck('final stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_DIRECT_PRIMARY_QUADRATURE_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,rows=summary,scope='One actual N44 point, empirical independent quadrature and derivative comparison. Exact recombination of stored fields. No rigorous inverse error, Gaussian weight error bound, uniform residual, far-field matching or continuum convergence.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','rows']},indent=2))
