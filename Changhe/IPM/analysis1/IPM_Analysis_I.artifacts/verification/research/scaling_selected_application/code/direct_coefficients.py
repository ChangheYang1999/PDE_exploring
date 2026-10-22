"""Supplemental literal exact comparisons, not SHA equality as coefficient equality."""
from pathlib import Path
import sys,resource,os
R=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(R/'research/scaling_norm_lower_bound/code'))
import common as C, cox_monomial as A, deboor_legendre as B
from flint import fmpq as Q
D=R/'research/scaling_selected_application';E=D/'evidence'
assert not sys.flags.optimize and os.getpriority(os.PRIO_PROCESS,0)==19
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
f=C.load(E/'direct_coefficients_freeze.json')
for n,h in f['files'].items():assert C.sha(R/n)==h
start=C.now();aa,bb,c,manifest=C.input_data();rows={r['span']:r for r in C.rows('smoke')};out=[]
for span in [7,620,1564]:
 ha=A.angular(A.modal(*aa,span));hb=B.angular(B.modal(*bb,span));assert len(ha)==len(hb)==261
 d=aa[0][span+1]-aa[0][span];assert d==bb[0][span+1]-bb[0][span]>0
 qa=Q(0);qb=Q(0);counts=[0,0,0]
 for j in range(261):
  ba=-2*ha[j]-ha[j].derivative()/d;bbj=-(2*hb[j]+hb[j].derivative()/d)
  ca=3*ba+ba.derivative()/d;cb=bbj.derivative()/d+3*bbj
  for label,(pa,pb) in enumerate([(ha[j],hb[j]),(ba,bbj),(ca,cb)]):
   assert pa.degree()<=7 and pb.degree()<=7
   for k in range(8):assert pa[k]==pb[k],(span,j,k,label);counts[label]+=1
  qa+=(1+(2*j+1)**2)*A.square_integral(ba)+A.square_integral(ca)
  qb+=B.square_integral(cb)+(1+(2*j+1)**2)*B.square_integral(bbj)
 qa*=d;qb*=d
 assert qa==qb==Q(rows[span]['methods']['cox_monomial']['Q'])==Q(rows[span]['methods']['deboor_legendre']['Q'])>=0
 assert A.digest(ha)==B.digest(hb)==rows[span]['methods']['cox_monomial']['density_coefficients_sha256']
 assert counts==[2088]*3
 out.append({'span':span,'utc':C.now(),'literal_density_equalities':counts[0],'literal_B_equalities':counts[1],'literal_C_equalities':counts[2],'exact_Q':str(qa)})
pins={n:C.sha(R/n) for n in f['files']};C.pin(pins,E/'direct_coefficients_freeze.json');C.pin(pins,C.E/'smoke_rows.jsonl')
C.write(E/'direct_coefficients.json',{'start_utc':start,'utc':C.now(),'status':'PASS_LITERAL_EXACT_COEFFICIENT_COMPARISONS_AND_INDEPENDENT_Q_REPLAY','rows':out,'literal_density_equalities':sum(x['literal_density_equalities'] for x in out),'literal_B_equalities':sum(x['literal_B_equalities'] for x in out),'literal_C_equalities':sum(x['literal_C_equalities'] for x in out),'complete_middle':False,'files':pins})
print(C.now(),'PASS literal density=6264 B=6264 C=6264; three exact Q equalities')
