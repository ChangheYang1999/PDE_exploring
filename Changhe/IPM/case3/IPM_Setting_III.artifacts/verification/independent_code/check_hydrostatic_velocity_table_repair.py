"""Result284: independent extraction against regenerated producer text."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,math
import numpy as np
R=Path('research/hydrostatic_velocity_table_repair');V=R/'verification';O=Path('research/hydrostatic_velocity_sequence_audit/verification')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert R.resolve().is_relative_to(Path('verification'))
checks=[]
def ck(name,ok,e=None):
 checks.append(dict(name=name,passed=bool(ok),evidence=e))
 if not ok:raise AssertionError((name,e))
t0=datetime.now(timezone.utc).isoformat();inp=json.loads((V/'INPUTS.json').read_text())
for x in inp['files']:ck('frozen '+x['frozen'],sha(x['frozen'])==x['sha256'])
old=json.loads((O/'FINAL_STATISTICS.json').read_text());raw=json.loads((O/'RUN.json').read_text());ref=json.loads((O/'REFINEMENT.json').read_text());ad=json.loads((O/'ADAPTIVE.json').read_text())
for j,n in [(old,785),(raw,52),(ref,35),(ad,20)]:ck('gate '+str(n),j['status']=='PASS' and len(j['checks'])==n and all(x['passed']for x in j['checks']))
for name,h in old['sources'].items():ck('277 dependency '+name,sha(O/name)==h)
ck('277 extraction driver',sha('independent_code/finalize_hydrostatic_velocity_statistics.py')==old['driver_sha256'])
ck('277 extraction proof',sha(O.parent/'FINAL_STATISTICS_PROOF.md')==old['proof_sha256'])
for x in json.loads((O/'INPUTS.json').read_text())['states']:ck('coefficient '+x['tag'],sha(x['state']['path'])==x['state']['sha256'])
items={j['tag']:j for j in raw['states']};fine={j['tag']:{q['index']:q for q in j['levels'][-1]['points']}for j in ref['states']}
xy=np.array([[q['x'],q['y'],q['r']]for q in raw['states'][0]['levels'][-1]['points']]);a={tag:np.array([q['V']for q in j['levels'][-1]['points']])for tag,j in items.items()}
ck('grid dimensions',xy.shape==(225,3) and len(items)==7)
regions=[('inner',0,.1),('subunit',.1,1),('annulus',1,100),('far',100,10001)]
rows=[]
def key(d):return tuple(d.get(k)for k in ['kind','c','old','new','tag','region','component','index'])
previous={key(d):d for d in old['comparisons']}
def obs(value,token,kind,**where):
 ck('finite observation '+str(where),math.isfinite(value))
 literal=F(token);mant,_,exp=token.lower().partition('e');places=len(mant.partition('.')[2]);unit=F(10)**((int(exp)if exp else 0)-places);delta=F(str(value))-literal;gap=max(F(0),abs(delta)-unit/2)
 d=dict(kind=kind,value=float(value),printed=token,agrees=gap==0,half_unit=str(unit/2),gap=str(gap),**where);p=previous[key(d)]
 ck('old evaluation agrees '+str(key(d)),abs(value-p['value'])<=2e-14*max(1,abs(value)),[value,p['value']])
 d['previous_printed']=p['printed'];d['changed']=F(p['printed'])!=literal;rows.append(d)
for c in [2,3]:
 text=(V/f'new_c{c}.txt').read_text();ck('q2 header '+str(c),'tail 400, q = 2)'in text)
 tags=sorted([t for t,s in items.items()if s['c']==c],key=lambda t:int(re.search('_N(\\d+)',t)[1]))
 pairlines=[re.match(r'^(\d+)x(\d+)\s*->\s*(\d+)x(\d+)\s+(.*)$',l)for l in text.split('scale of',1)[0].splitlines()];pairlines=[m for m in pairlines if m]
 ck('pair count '+str(c),len(pairlines)==len(tags)-1)
 for oldtag,newtag,m in zip(tags,tags[1:],pairlines):
  ck('pair labels '+oldtag+newtag,[int(m[1]),int(m[3])]==[int(re.search('_N(\\d+)',t)[1])for t in [oldtag,newtag]])
  tokens=re.findall(r'[+-]?\d+\.\d+e[+-]\d+',m[5]);ck('12tokens '+oldtag+newtag,len(tokens)==12)
  d=a[oldtag]-a[newtag];b=a[newtag];rd=xy[:,2];weight=(1+rd)**(1/c)
  for j,(name,lo,hi)in enumerate(regions):
   ii=np.flatnonzero((rd>=lo)&(rd<hi));ck('region '+oldtag+name,len(ii)>0)
   for k in [0,1]:
    ix=int(ii[np.argmax(abs(d[ii,k])/weight[ii])]);obs(float(abs(d[ix,k])/weight[ix]),tokens[3*j+k],'pair_component',c=c,old=oldtag,new=newtag,region=name,component=k,index=ix)
   ds=np.linalg.norm(d,axis=1);bs=np.linalg.norm(b,axis=1);di=int(ii[np.argmax(ds[ii])]);bi=int(ii[np.argmax(bs[ii])]);ck('positive regional denominator '+oldtag+name,bs[bi]>0)
   obs(float(ds[di]/bs[bi]),tokens[3*j+2],'pair_ratio',c=c,old=oldtag,new=newtag,region=name,difference_index=di,scale_index=bi)
 line=next(l for l in text.splitlines()if l.startswith('scale of last:'));tokens=re.findall(r'[+-]?\d+\.\d+e[+-]\d+',line);ck('8scale '+str(c),len(tokens)==8)
 for j,(name,lo,hi)in enumerate(regions):
  ii=np.flatnonzero((xy[:,2]>=lo)&(xy[:,2]<hi))
  for k in [0,1]:obs(float(np.max(abs(a[tags[-1]][ii,k])/(1+xy[ii,2])**(1/c))),tokens[2*j+k],'last_scale',c=c,tag=tags[-1],region=name,component=k)
 chunks=[(1,text.split('V_2(0, y)',1)[1].split('V_1(',1)[0]),(0,text.split('V_1(xi, 0)',1)[1])]
 for k,chunk in chunks:
  lines=[re.match(r'^\s*(\d+)x(\d+):\s*(.*)$',l)for l in chunk.splitlines()];lines=[m for m in lines if m];ck('axisrows '+str((c,k)),len(lines)==len(tags))
  for t,m in zip(tags,lines):
   tokens=re.findall(r'[+-]\d+\.\d+',m[3]);ck('axis labels '+t+str(k),len(tokens)==7 and int(m[1])==int(re.search('_N(\\d+)',t)[1]))
   for j,token in enumerate(tokens):
    ix=36*j+(8 if k==1 else 0);q=fine[t][ix];ck('axiscoord '+t+str(k)+str(j),q['x'if k==1 else'y']==0 and abs(q['r']/10**(j-2)-1)<2e-15)
    denom=(q['r']if k==1 else 1+q['r'])**items[t]['p'];obs(q['V'][k]/denom,token,'axis',c=c,tag=t,component=k,index=ix,r=q['r'])
ck('174unique observations',len(rows)==174 and len({key(x)for x in rows})==174)
changed=[x for x in rows if x['changed']];fail=[x for x in rows if not x['agrees']]
notes=(V/'producer_notes.md').read_text().split('## 152.',1)[1]
claim_all_other='all other\nprinted tokens identical'in notes or'all other printed tokens identical'in notes
omitted=[x for x in changed if x['previous_printed']=='-0.78799'and x['printed']=='-0.78798']
ck('changed N192 independently detected',len(omitted)==1,omitted)
ck('exhaustive prose claim located',claim_all_other)
ck('old4disagreements now within rounding',all(x['agrees']for x in rows if key(x)in {key(y)for y in old['failures']}))
out=dict(status='PASS',utc_started=t0,utc_finished=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,comparisons=rows,changes=changed,disagreements=fail,omitted_note_changes=omitted,printed_verdict='CONFIRMED'if not fail else'REPAIR',change_list_verdict='REFUTED',proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),inputs_sha256=sha(V/'INPUTS.json'),scope='Finite sampled auxiliary velocity tables only; source-of-tail-drift and convergence OPEN; fullplane UNRESOLVED')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'comparisons',len(rows),'changes',len(changed),'disagreements',len(fail));print(json.dumps(changed,indent=2));print('FAILURES',json.dumps(fail,indent=2))
