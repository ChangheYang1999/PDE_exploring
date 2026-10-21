from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from math import isqrt
import json, hashlib, sys
import numpy as np
root=Path(__file__).resolve().parents[1]; v=root/'verification'
sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity

def load(name):return json.loads((v/name).read_text())
def stats(rows):
 a=np.array([r['R_Nv'] for r in rows]);i=int(np.argmax(a))
 return {'count':len(rows),'l2_report_Nf':float(np.linalg.norm(a)),'max_report_Nf':float(a[i]),'max_point':rows[i]['point']}
def audit(path):
 d=NodalDensity(path);z=np.load(path);B=max(abs(Fraction(float(x))) for x in z['b'].ravel());B0=(B.numerator+B.denominator-1)//B.denominator
 H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1)
 assert d.L==8 and 0<1/Fraction(d.cl)<Fraction(1,5)
 C=512*H*B0;t=Fraction(1,10**25);tail=Fraction(5*C,2)*10**5*Fraction(1,10**24)/(1-t*t)**2
 rr=np.array([.05,.3,1,3,10,100,1000,1e5])[:,None];th=np.array([.001,.03,.3,1.,1.4]);x=rr*np.cos(th);y=rr*np.sin(th);f=d(x,y)
 parity=max(np.max(abs(d(-x,y)-f)),np.max(abs(d(x,-y)+f)))
 return {'md5':hashlib.md5(path.read_bytes()).hexdigest(),'cl':d.cl,'C_aux':d.C,'first_row_one':bool(np.array_equal(z['b'][0],np.ones(d.M))),'parity_error':float(parity),'tail_B_exact':str(B),'tail_H':H,'tail_C':C,'velocity_tail_bound_R1e30_observer1e5':float(tail),'strain_tail_bound_R1e30':float(Fraction(5*C,2*10**24))}
base=load('base_transport2048.json')['rows'];fresh=load('t1p0_fresh2048.json')['rows'];stages=[]
for which,setupfile,actionpath,nfit in [(1,'setup.json',Path('verifier/inverse/verification/dnSB_actions_2048.json'),8),(2,'setup_second.json',v/'t1p0_actions2048.json',26)]:
 setup=load(setupfile);ar=json.loads(actionpath.read_text())['rows'][:nfit];den=np.array([r['Nv'] for r in ar]);stage={'number':which,'setup':setup,'trials':[]}
 reference=base if which==1 else load('t1p0_transport2048.json')['rows']+fresh
 stage['base_fit']=stats(reference[:nfit]);stage['base_holdouts']=stats(reference[nfit:]);stage['base_all']=stats(reference)
 for trial in setup['trials']:
  tag=trial['tag'];rows=load(tag+'_transport2048.json')['rows'];balls=load(tag+'_balls.json');strain=load(tag+'_strain.json');raw=np.array([r['R'] for r in rows[:nfit]])/den;prediction=np.array(trial['linear_prediction'])
  item={'tag':tag,'t':trial['t'],'field':audit(Path(trial['path'])),'fit':stats(rows[:nfit]),'holdouts':stats(rows[nfit:]),'all':stats(rows),'frozen_denominator_fit_l2':float(np.linalg.norm(raw)),'linear_prediction_l2':float(np.linalg.norm(prediction)),'nonlinear_remainder_l2':float(np.linalg.norm(raw-prediction)),'strain':strain,'center_values':balls['values'],'center_contains_zero':balls['contains_zero']}
  if (v/(tag+'_transport4096.json')).exists():
   hi=load(tag+'_transport4096.json')['rows'];item['fine_transport']=[]
   for r in hi:
    nearest=min(rows,key=lambda s:np.linalg.norm(np.array(r['point'])-s['point']))
    assert np.linalg.norm(np.array(r['point'])-nearest['point'])<1e-12
    item['fine_transport'].append({'point':r['point'],'R_report_Nf':r['R_Nv'],'change2048to4096':abs(r['R_Nv']-nearest['R_Nv'])})
  if (v/(tag+'_elliptic4096.json')).exists():item['elliptic4096']=load(tag+'_elliptic4096.json')['rows']
  stage['trials'].append(item)
 stages.append(stage)
out={'date':datetime.now(timezone.utc).isoformat(),'scope':'two independently computed sampled physical Gauss-Newton corrections; first holdouts become second fit points; fresh holdouts are genuinely new; no root, branch or uniform residual claim','stages':stages}
(v/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
for s in stages:
 print('STAGE',s['number'],'base',s['base_fit']['l2_report_Nf'],s['base_holdouts']['l2_report_Nf'],s['base_all']['l2_report_Nf'])
 for r in s['trials']:print(r['tag'],r['fit']['l2_report_Nf'],r['holdouts']['l2_report_Nf'],r['all']['l2_report_Nf'],r['holdouts']['max_report_Nf'],r['strain']['identity_defect_3cl_1_c'],r['nonlinear_remainder_l2'])
