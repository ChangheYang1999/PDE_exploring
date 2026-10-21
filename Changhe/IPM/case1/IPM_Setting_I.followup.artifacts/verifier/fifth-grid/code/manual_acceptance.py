"""Independent exact rational arithmetic on saved component values and pin audit."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib, json, sys, math
from flint import arb, ctx
BASE=Path(__file__).resolve().parents[3]; V=BASE/'verifier/fifth-grid/verification'; tag='dnB_n108m44S'
ctx.prec=256
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((V/n).read_text())
s=read(tag+'_summary.json');b=read(tag+'_broad4096.json');p=read(tag+'_physical.json');c=read(tag+'_center_certificate.json');done=read('completion.json');prepared=read('prepared.json')
checks=[]
def need(ok, label):
 if not ok:raise ValueError(label)
 checks.append(label)
need(sys.flags.optimize==0,'manual interpreter assertions enabled')
need(done['complete'] and not done.get('error'),'launcher completed')
need(done['pins']==prepared['pins'],'prepared/completed pins identical')
for f,h in done['pins'].items():need(sha(BASE/f)==h,'pin '+f)
for d in c['dependencies']:need(sha(BASE/d['file'])==d['sha256'],'center dependency '+d['file'])
need(sha(BASE/'verifier/fifth-grid/data'/f'{tag}.npz')==c['source_sha256']==done['source_sha256'],'exact field SHA binding')
need((BASE/'verifier/fifth-grid/data'/f'{tag}.npz').read_bytes()==Path(done['original_source']).read_bytes(),'published/frozen bytes identical at acceptance')
need(sha(BASE/'verifier/fifth-grid/data'/f'{tag}_exact.json')==c['exact_json_sha256'],'exact JSON input binding')
for k,suffix in [('physical','physical'),('broad','broad4096'),('balls','balls'),('strain','strain'),('reconstruction','reconstruction')]:need(sha(V/f'{tag}_{suffix}.json')==s['input_hashes'][k],'summary input '+k)
cl=F(s['state']['cl']);rows=[]
for label,rs in [('broad',b['rows'])]+[('pass'+str(j),z['transport'])for j,z in enumerate(p['passes'])]:
 for j,r in enumerate(rs):
  w=[cl*F(r['point'][a])+F(r['U'][a])for a in range(2)];g=list(map(F,r['gradient']));rho=F(r['rho'])
  R=sum(w[a]*g[a]for a in range(2))-rho;nf=abs(rho)+sum(abs(w[a]*g[a])for a in range(2));nv=abs(rho)+abs(sum(F(r['point'][a])*g[a]for a in range(2)))+abs(sum(F(r['U'][a])*g[a]for a in range(2)))
  need(nf>0 and nv>0,label+str(j)+' denominators positive')
  errors=[abs(float(R)-r['R']),abs(float(nf)-r['N_report_f']),abs(float(nv)-r['N_report_v']),abs(float(abs(R)/nf)-r['absR_report_f']),abs(float(abs(R)/nv)-r['absR_report_v'])]
  need(max(errors[:3])<1e-9 and max(errors[3:])<1e-12,label+str(j)+' rational components')
  rows.append({'set':label,'index':j,'R_exact_saved_components':str(R),'Nf_exact_saved_components':str(nf),'absR_Nf':float(abs(R)/nf),'errors':errors})
ell=[]
for pi,z in enumerate(p['passes']):
 for r in z.get('elliptic',[]):
  rx=F(r['rho_x'])
  for e in r['checks']:
   du=[[F(x)for x in row]for row in e['DU']]; E=-du[1][0]+du[0][1]-rx;den=abs(du[1][0])+abs(du[0][1])+abs(rx)
   need(abs(float(E)-e['E'])<1e-15,'elliptic signed identity')
   need(abs(float(abs(E)/den)-e['E_normalized'])<1e-14,'elliptic normalizer')
   need(abs(float(du[0][0]+du[1][1])-e['divU'])<1e-15,'divergence components')
   ell.append({'pass':pi,'point':r['point'],'step':e['h'],'E_exact_components':str(E),'normalized':float(abs(E)/den)})
first=arb(c['first_self_consistency_ball']);second=arb(c['second_self_consistency_ball']);need(not first.contains(0) and not second.contains(0),'both center identity balls exclude zero');need((first-second).contains(0),'center identity balls overlap')
for k in ['rho5_sine7_coefficient','transport_balance_determinant']:
 ball=arb(s['center']['values'][k]);need(not ball.contains(0),'center obstruction '+k)
need(s['root']['origin_U']==[0.,0.] and s['state']['first_row_unit'],'origin velocity and normalization row')
need(len(b['rows'])==58 and all(x['complete']for x in [b,p,c]),'all physical and certificate stages complete')
need(read('summary_audit.json')['summary_sha256']==sha(V/f'{tag}_summary.json'),'producer scalar-audit summary binding')
summary={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','number_checks':len(checks),'component_rows':len(rows),'elliptic_checks':len(ell),'maximum_component_rounding_difference':max(max(r['errors'])for r in rows),'maximum_broad_R_Nf_from_rational_components':max(r['absR_Nf']for r in rows if r['set']=='broad'),'summary_sha256':sha(V/f'{tag}_summary.json'),'completion_sha256':sha(V/'completion.json'),'code_sha256':sha(Path(__file__)),'rows':rows,'elliptic':ell,'checks':checks,'scope':'Exact arithmetic on the saved binary component values, not exact physical inverse values. Exact center certificates depend on the separately proved methods. Current bytes and observed launcher environment are audited; no historical direct-import attestation is invented. Fixed-field exclusion only; no endpoint.'}
(V/'manual_acceptance.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items()if k not in ['rows','elliptic','checks']},indent=2))
