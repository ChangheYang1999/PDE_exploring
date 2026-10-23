"""Finite provenance and printed-data supplement. No candidate inverse execution."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,re,math,sys,traceback,copy
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
ROOT=Path('research/new_node_export_record_audit');V=ROOT/'verification'
checks=[];bindings={}
def now():return datetime.now(timezone.utc).isoformat()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def read(p,h=None):
 p=Path(p);b=p.read_bytes();s=hashlib.sha256(b).hexdigest()
 if h is not None:ck('SHA256 '+str(p),s==h)
 if str(p)in bindings:ck('unchanged '+str(p),bindings[str(p)]==s)
 bindings[str(p)]=s;return b

def pin(cfg,actual,saved):
 h=cfg['source_design_acceptance_sha256']
 if not isinstance(h,str)or not re.fullmatch('[0-9a-f]{64}',h)or h!=actual or h!=saved:raise ValueError('export manifest acceptance pin')
 return True

def semantic(d,status):
 if d.get('status')!=status or type(d.get('count'))is not int or d['count']!=len(d.get('checks',[]))or d['count']<1 or any(x.get('passed')is not True for x in d['checks']):raise ValueError('semantic PASS entries')
 return True

def tokens(text):
 z=re.findall(r'r in \[([^,]+), ([^\)]+)\): max \|R_h\| (\S+)\s+max \|R_h\|/N_f (\S+)',text)
 expected=[(Q(0),Q('.1')),(Q('.1'),Q(1)),(Q(1),Q(100)),(Q(100),Q('1e300'))]
 if len(z)!=4 or [(Q(a),Q(b))for a,b,_,_ in z]!=expected:raise ValueError('four ordered printed regions')
 for a,b,x,y in z:Q(x);Q(y)
 return [(x,y)for a,b,x,y in z]

def differences(a,b):
 return [dict(region=k,metric=['absR','Rf'][j],old=a[k][j],new=b[k][j])for k in range(4)for j in range(2)if a[k][j]!=b[k][j]]

def decimal_contains(token,value):
 m=re.fullmatch(r'([+-]?\d+)(?:\.(\d+))?[eE]([+-]?\d+)',token)
 if m is None:raise ValueError('scientific decimal token')
 unit=Q(10)**(int(m[3])-len(m[2]or''));c=Q(token);v=Q(value)
 return c-unit/2<=v<=c+unit/2

def rejects(n,fn):
 try:fn()
 except(ValueError,KeyError,AssertionError):ck(n,True)
 else:raise AssertionError('accepted wrong manufacture '+n)

def run():
 a='a'*64;b='b'*64;cfg={'source_design_acceptance_sha256':a}
 ck('manufacture correct pin',pin(cfg,a,a));rejects('manufacture missing pin',lambda:pin({},a,a));rejects('manufacture changed design bytes',lambda:pin(cfg,b,a));rejects('manufacture changed saved pin',lambda:pin(cfg,a,b))
 good=dict(status='P',count=1,checks=[dict(passed=True)])
 ck('manufacture semantic positive',semantic(good,'P'))
 for name,bad in [('status',dict(good,status='F')),('count',dict(good,count=2)),('false',dict(good,checks=[dict(passed=False)])),('empty',dict(good,count=0,checks=[]))]:rejects('manufacture semantic '+name,lambda bad=bad:semantic(bad,'P'))
 t=[('1.000e-6','2.000e-6')]*4;u=list(t);u[2]=('1.001e-6','2.000e-6')
 ck('manufacture equal tokens',differences(t,t)==[]);ck('manufacture changed token',differences(t,u)==[dict(region=2,metric='absR',old='1.000e-6',new='1.001e-6')]);ck('manufacture decimal inclusion',decimal_contains('1.000e+00',1.));ck('manufacture decimal exclusion',not decimal_contains('1.000e+00',1.001))
 mc=len(checks)
 out=json.loads(read(V/'CHECKS.json'));ck('candidate semantic',semantic(out,'PASS_NEW_NODE_EXPORT_RECORDS_REQUIRES_FINAL_REVIEW'))
 for p,h in out['bindings'].items():read(p,h)
 da=json.loads(read(V/'DESIGN_ACCEPTANCE.json',out['bindings'][str(V/'DESIGN_ACCEPTANCE.json')]))
 ck('design semantic',semantic(da,'ACCEPTED_FOR_FINITE_RECORD_AUDIT'))
 mf=json.loads(read(V/'MANUFACTURES.json',out['bindings'][str(V/'MANUFACTURES.json')]))
 ck('manufactures semantic',semantic(mf,'PASS_NEW_EXPORT_RECORD_MANUFACTURES'))
 cfg=json.loads(read(V/'EXPORT_INPUTS.json',out['bindings'][str(V/'EXPORT_INPUTS.json')]))
 ck('actual export acceptance pin',pin(cfg,bindings[str(V/'DESIGN_ACCEPTANCE.json')],out['bindings'][str(V/'DESIGN_ACCEPTANCE.json')]))
 for p,h in da['bindings'].items():read(p,h)
 # Preserve a report of repeated assertion labels without treating the number as independent evidence.
 names=[z['name']for z in out['checks']];freq={n:names.count(n)for n in sorted(set(names))};counts=dict(entries=len(names),distinct_labels=len(freq),repeated_labels={k:v for k,v in freq.items()if v>1},unconditional_identity_scope='Some saved binding and exact-loaded-bytes entries had no external expected hash. They record an observed hash, not an independent identity check.')
 oldmanifest=Path('research/accurate_map_final_audit/verification/INPUTS_SUPPLEMENT.json')
 ac=json.loads(read('research/accurate_map_final_audit/verification/DESIGN_ACCEPTANCE.json'))
 om=json.loads(read(oldmanifest,ac['bindings'][str(oldmanifest)]));oldby={Path(z['frozen']).name:z for z in om['files']}
 comparisons=[]
 for cfgstate,state in zip(cfg['states'],out['states']):
  tag=state['tag'];ck('ordered result tags '+tag,tag==cfgstate['tag'])
  oldname='hs_node_check_c2_N160.txt'if tag=='S160'else'hs_node_check_c2_N128_acc6_fine.txt';old=oldby[oldname]
  before=tokens(read(old['frozen'],old['sha256']).decode());after=tokens(read(cfgstate['record'],cfgstate['record_sha256']).decode());diff=differences(before,after)
  ck('historical changes '+tag,len(diff)==(3 if tag=='S160'else 0),diff)
  pairs=state['selected_own_jets'];prod=state['selected_export_jets'];errors=[(abs(x-y)/(1+abs(x)),i,j,abs(x-y),abs(x-y)/abs(x)if x else None)for i,(v,w)in enumerate(zip(pairs,prod))for j,(x,y)in enumerate(zip(v,w))];mx=max(errors)
  ck('recomputed selected-jet maximum '+tag,mx[0]==state['selected_jet_scaled_max'])
  ef=state['exact_operand_regions'][3]['metrics']['absR'];pf=state['export_arithmetic_regions'][3]['metrics']['absR'];ck('far comparison same maximizing row '+tag,ef['index']==pf['index'])
  comparisons.append(dict(tag=tag,historical_differences=diff,selected_jet_max=dict(scaled=mx[0],index=state['selected_jet_indices'][mx[1]],component=['g','d_x_g','d_y_g'][mx[2]],absolute=mx[3],relative=mx[4]),far_absolute_residual_max=dict(index=ef['index'],exact_operand=ef['value'],export_arithmetic=pf['value'],relative_difference=abs(ef['value']-pf['value'])/ef['value'])))
 draft=read(ROOT/'RESULTS_REPAIRED_DRAFT.md').decode();rows=[x for x in draft.splitlines()if x.startswith('| S160 |')or x.startswith('| G128 |')];ck('eight result rows',len(rows)==8)
 for line,(state,reg)in zip(rows,[(s,r)for s in out['states']for r in s['exact_operand_regions']]):
  fields=[f.strip()for f in line.split('|')[1:-1]];ck('table identity '+fields[0]+' '+fields[1],fields[:3]==[state['tag'],reg['region'],str(reg['count'])])
  for text,m in zip(fields[3:],['absR','Rf','Rv']):ck('rounded table '+state['tag']+' '+reg['region']+' '+m,decimal_contains(text,reg['metrics'][m]['value']))
 for p in [__file__,ROOT/'FINAL_REPAIR_PROOF.md',V/'opus_final/answer.md',V/'opus_final/metadata.json',V/'opus_final/response.json',V/'opus_final/request.txt']:read(p)
 meta=json.loads(read(V/'opus_final/metadata.json'));ck('actual completed final model',meta['returned_model']=='claude-opus-5-5'and meta['stop_reason']=='end_turn')
 return dict(status='PASS_NEW_EXPORT_FINAL_SUPPLEMENT_REQUIRES_MODEL_REVIEW',utc=now(),count=len(checks),manufacture_entries=mc,checks=checks,bindings=bindings,candidate_count_qualification=counts,comparisons=comparisons,scope='Post-design export identity closure and finite table checks only; no independent all-node inverse or historical authenticity.')
if __name__=='__main__':
 try:
  out=run();(V/'FINAL_SUPPLEMENT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['manufacture_entries']);print(json.dumps(out['comparisons'],indent=2))
 except Exception:
  (V/('FINAL_SUPPLEMENT_FAILURE_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')).write_text(json.dumps(dict(utc=now(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
