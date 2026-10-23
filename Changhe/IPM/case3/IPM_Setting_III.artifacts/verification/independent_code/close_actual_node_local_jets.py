from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import numpy as np
from node_export_arithmetic_strict import residual
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';B={};C=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 C.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);s=sha(p);ck('binding '+str(p),h is None or s==h);B[str(p)]=s;return p
for p in [__file__,R/'LOCAL_CLOSURE_PROOF.md',R/'LOCAL_NORMALIZED_ARITHMETIC_CORRECTION_PROOF.md',R/'LOCAL_RATIO_ARITHMETIC_CORRECTION_PROOF.md',R/'LOCAL_JET_REVIEW_RESOLUTION_PROOF.md',R/'LOCAL_REGIONAL_BOUND_PROOF.md',R/'INVERSE_RESTART_AND_REVIEW_PROOF.md','independent_code/node_export_arithmetic_strict.py','independent_code/node_export_arithmetic.py',V/'LOCAL_REVIEW_COUNTEREVIDENCE.json',V/'LOCAL_REGIONAL_BOUND_CHECKS.json']:bind(p)
for name,count,status in [('ACTUAL_JETS.json',2468,'PASS_ACTUAL_NODE_JETS_AND_EXACT_FIXED_MAP_ARITHMETIC'),('ACTUAL_MP_JETS.json',183,'PASS_ACTUAL_LOCAL_MP_JET_WITNESSES')]:
 d=json.loads(bind(V/name).read_text());ck('completed gate '+name,d['status']==status and d['count']==len(d['checks'])==count and all(x['passed']for x in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
with np.load(V/'actual_node_jets.npz',allow_pickle=False)as f:a={k:f[k]for k in f.files}
with np.load(V/'source_nodes_maps.npz',allow_pickle=False)as f:s={k:f[k]for k in f.files}
x,y=a['X'],a['Y'];own,prod=a['own_jet'],a['producer_jet'];vm=np.column_stack([s['V1_map'],s['V2_map']]);r=np.hypot(x,y);masks=[r<.1,(r>=.1)&(r<1),(r>=1)&(r<100),r>=100];rows=[];jet=[];relative=[];normalized=[];signs=[];zeros=[[],[]]
for i in range(2304):
 o=residual(own[i],vm[i],2,x[i],y[i]);p=residual(prod[i],vm[i],2,x[i],y[i]);d=o['R']-p['R'];dd=(2*F(float(x[i]))+F(float(vm[i,0])))*(F(float(own[i,1]))-F(float(prod[i,1])))+(2*F(float(y[i]))+F(float(vm[i,1])))*(F(float(own[i,2]))-F(float(prod[i,2])))-(F(float(own[i,0]))-F(float(prod[i,0])))
 if d!=dd:raise ArithmeticError('exact map jet identity '+str(i))
 rows.append((o,p));jet.append(abs(d));den=max(abs(o['R']),abs(p['R']));relative.append(abs(d)/den if den else F(0));normalized.append(abs(d)/o['Nf']if o['Nf']else None)
 if o['R']*p['R']<0:signs.append(i)
 for k,v in enumerate([o['R'],p['R']]):
  if not v:zeros[k].append(i)
ck('2304 independent exact difference identities',True)
previous=json.loads((V/'LOCAL_REGIONAL_BOUND_CHECKS.json').read_text());regional=[]
for j,(mask,(lo,hi))in enumerate(zip(masks,[(0,480),(480,1248),(1248,1968),(1968,2304)])):
 ids=list(map(int,np.flatnonzero(mask)));ck('exact regional indexblock '+str(j),ids==list(range(lo,hi)));io=max(ids,key=lambda i:abs(rows[i][0]['R']));ip=max(ids,key=lambda i:abs(rows[i][1]['R']));ij=max(ids,key=lambda i:jet[i]);o=abs(rows[io][0]['R']);p=abs(rows[ip][1]['R']);d=jet[ij];before=previous['rows'][j];ck('regional exact inequality '+str(j),abs(o-p)<=d);ck('regional bound operands '+str(j),list(map(str,[o,p,d]))==before['exact_bound_operands']);ck('regional argmaxes '+str(j),[io,ip,ij]==[before['own_index'],before['producer_index'],before['jet_delta_index']]);ck('regional relativedifference '+str(j),float(abs(o-p)/max(o,p))==before['relative_max_difference']);regional.append(dict(region=before['region'],index_range=[lo,hi],own_index=io,producer_index=ip,jet_index=ij,own_max=float(o),producer_max=float(p),jet_max=float(d),relative_max_difference=float(abs(o-p)/max(o,p))))
ia=max(range(2304),key=lambda i:jet[i]);ir=max(range(2304),key=lambda i:relative[i]);inn=max(range(2304),key=lambda i:normalized[i]);ck('absolute relative normalized maxima',[ia,ir,inn]==[2296,2294,2264]);ck('four signs',len(signs)==4);ck('zero residual counts',zeros==[[],[]]);ck('relative discrepancy exceedsone',relative[ir]>1);ck('normalizedmaxsmall',normalized[inn]<F(8,10**14));counter=json.loads((V/'LOCAL_REVIEW_COUNTEREVIDENCE.json').read_text());ck('absolute counterpart',float(jet[ia])==abs(counter['largest_absolute_jet_delta']['value']));rounded_relative=[abs(float(o['R'])-float(p['R']))/max(abs(float(o['R'])),abs(float(p['R'])))for o,p in rows];ck('roundedrelativeargmax',max(range(2304),key=lambda i:rounded_relative[i])==ir);ck('rounded relative counterpart',rounded_relative[ir]==counter['largest_relative_R_discrepancy']['value']);rounded_normalized=float(jet[inn])/float(rows[inn][0]['Nf']);ck('rounded normalized counterpart',rounded_normalized==counter['largest_normalized_jet_delta']['value'])
reviews=[]
for label in ['actual_jets','local_resolution','local_bound']:
 d=V/('opus_'+label);m=json.loads(bind(d/'metadata.json').read_text());bind(d/'request.txt',m['request_sha256']);bind(d/'response.json');answer=bind(d/'answer.md').read_text();ck('actualOpus5.5 '+label,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']=='claude-opus-5-5'and m['stop_reason']=='end_turn'and m['answer_nonempty']and bool(answer.strip()));reviews.append(m)
for p,h in list(B.items()):ck('stable '+p,sha(p)==h)
out=dict(status='PASS_FINITE_LOCAL_JETS_AND_REVIEW_CORRECTIONS',utc=datetime.now(timezone.utc).isoformat(),count=len(C),checks=C,bindings=B,reviews=reviews,regional=regional,strict_sign_disagreement_indices=signs,zero_residual_indices=zeros,absolute_jet_argmax=ia,relative_jet_argmax=ir,normalized_jet_argmax=inn,maximum_absolute_delta=float(jet[ia]),maximum_relative_delta=float(relative[ir]),maximum_rounded_residual_relative_delta=rounded_relative[ir],maximum_Nf_normalized_delta=float(normalized[inn]),maximum_rounded_Nf_normalized_delta=rounded_normalized,scope='Finite local density derivatives and exact fixed-map arithmetic confirmed. Negligibility relative to each map residual refuted. Independent auxiliary inverse has not run in309; trueinverseerror and historicalmapauthentication OPEN. Primaryfullplane UNRESOLVED.')
(V/'LOCAL_CLOSURE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],signs,out['utc'])
