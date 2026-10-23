"""Bind the finite MP design and confirm its exact Nf convention."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,struct,numpy as np
from node_export_inverse_stage import finite_arithmetic,RESIDUAL_COLUMNS
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';checks=[];bindings={}
def ck(n,b,**extra):
 checks.append(dict(name=n,passed=bool(b),**extra))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve().relative_to(Path.cwd());q=str(p);s=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+q,(h is None or s==h)and(q not in bindings or bindings[q]==s));bindings[q]=s;return p
for name,status,count in [('MP_STAGE_MANUFACTURES.json','PASS_MP_GEOMETRY_MOMENTS_AND_REAL_RESTART',232),('ACTUAL_MP_JETS.json','PASS_ACTUAL_LOCAL_MP_JET_WITNESSES',183),('INVERSE_DESIGN_ACCEPTANCE.json','ACCEPTED_FOR_FINITE_COMPUTATION',84)]:
 d=json.loads(bind(V/name).read_text());ck('complete gate '+name,d['status']==status and d['count']==count==len(d['checks'])and all(q['passed']for q in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
 if name=='MP_STAGE_MANUFACTURES.json':ck('bookkeeping count distinct',d['bookkeeping_identity_count']==30 and 'not evidence' in d['identity_scope'])
for label in ['mp_design','mp_followup','mp_final_design']:
 p=V/('opus_'+label)
 for n in ['request.txt','response.json','metadata.json','answer.md']:bind(p/n)
 m=json.loads((p/'metadata.json').read_text());ck('actual completed Opus5.5 '+label,m['returned_model']=='claude-opus-5-5'and m['stop_reason']=='end_turn'and m['answer_nonempty'],request_id=m['request_id'])
for p in [__file__,R/'MP_DESIGN_ACCEPTANCE_PROOF.md']:bind(p)
ck('residual column identity',RESIDUAL_COLUMNS==['R','Nf','Nv','Rf','Rv'])
for i,(x,y)in enumerate([(0.,0.),(.1,.2),(-.1,.2),(.1,-.2),(-.1,-.2),(1e6,1e-8),(1e-8,1e6),(3.125,7.75)]):
 for scale in [.25,1.,17.]:
  j=np.array([scale*.1,scale*(-.3),scale*.7,0.]);v=np.array([-.125*scale,.2*scale]);jp=j*np.array([1.01,.9,1.1,1.]);out,_=finite_arithmetic(j,jp,v,v*.7,v*1.2,2.,x,y)
  g,gx,gy=map(lambda z:F(float(z)),j[:3]);xx,yy=F(x),F(y);v1,v2=map(lambda z:F(float(z)),v)
  nf=abs((2*xx+v1)*gx)+abs((2*yy+v2)*gy)+abs(g)
  ck('independent round-once Nf '+str((i,scale)),struct.pack('d',out[1])==struct.pack('d',float(nf)))
for p,h in list(bindings.items()):ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='ACCEPTED_FOR_FINITE_MP_COMPUTATION',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Design and finite conventions only. A/B/C and candidate MP not run. Bound c_l=2; own_jet is g,gx,gy,gxx; Nf exact Fraction then one binary64 rounding. 30 prior MP identities are bookkeeping, not accuracy evidence. Primary unresolved.')
p=V/'MP_DESIGN_ACCEPTANCE.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
