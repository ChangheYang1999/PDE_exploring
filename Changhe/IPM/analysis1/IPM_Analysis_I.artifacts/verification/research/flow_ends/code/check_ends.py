"""Two interval evaluations of consequences of previously audited Green bounds."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,time,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_ends/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ends(x):
 if isinstance(x,arb):return tuple(F(int(m))*F(2)**int(e) for m,e in [v.man_exp() for v in (x.lower(),x.upper())])
 return tuple((-1 if s else 1)*F(int(m))*F(2)**int(e) for s,m,e,b in x._mpi_)
def rec(x):l,u=ends(x);assert l<=u;return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def get_inputs():
 pins={}
 for topic,h in [('inner_majorant','69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc'),('exterior_flow','2a8ae9e75b9cc64a69f950254d01af346eb12aa600ce797680953abc391551dd')]:
  p=B/f'research/{topic}/evidence/verdict.json';assert sha(p)==h;pins[str(p.relative_to(B))]=h
  for f,v in json.loads(p.read_text())['files'].items():assert sha(B/f)==v;pins[f]=v
 a=json.loads((B/'research/inner_majorant/evidence/inner_result.json').read_text());v=json.loads((B/'research/inner_majorant/evidence/inner_iv_audit.json').read_text());o=json.loads((B/'research/exterior_flow/evidence/checks.json').read_text())
 ar=next(c['values'] for c in a['cases'] if c['T_exact']=='0');vr=next(c['values'] for c in v['cases'] if c['T_exact']=='0');ot=next(c for c in o['cases'] if c['T_exact']=='9')
 Cr=max(F(ar['C_r']['upper_exact']),F(vr['C_r']['upper_exact']));Ct=max(F(ar['C_theta']['upper_exact']),F(vr['C_theta']['upper_exact']));P=max(F(ot['P_arb']['upper_exact']),F(ot['P_iv']['upper_exact']));Q=max(F(ot['Q_arb']['upper_exact']),F(ot['Q_iv']['upper_exact']))
 assert P==F(ot['joint_P_upper_exact']) and Q==F(ot['joint_Q_upper_exact']) and F(a['k_exact'])==F(o['parameters_exact']['k'])
 x={'k':F(a['k_exact']),'ta':F(a['ta_exact']),'tb':F(o['parameters_exact']['tb']),'Cr':Cr,'Ct':Ct,'P':P,'Q':Q,'a':F(129,20),'b':F(307,100),'gamma':F(1129,1000),'T':F(9)}
 assert all(x[n]>0 for n in ['k','Cr','Ct','P','Q','a','b','gamma']) and x['k']<1 and x['T']<17
 return x,pins

def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180;x,pins=get_inputs();values={}
 for method,cv in [('arb',aa),('iv',ii)]:
  z={n:cv(v) for n,v in x.items()};cl=1/z['k'];c=3*cl-1;S=z['a']+z['b'];R=z['ta'].exp() if method=='arb' else iv.exp(z['ta']);Re=(z['tb']+9).exp() if method=='arb' else iv.exp(z['tb']+9)
  D=(z['Cr']+522*z['Ct'])*R**2;L=cl-c-D
  assert ends(L)[1]<0 and ends(c)[0]>0
  if method=='arb':
   muR=z['gamma']+(S-z['gamma'])/(1+(R/6)**4);muE=z['gamma']+(S-z['gamma'])/(1+(Re/6)**4)
   innerT=-1-cl+z['a']*(cl-c+D)+z['b']*(cl+c+D)+(muR-S)*L
   outerT=-1-cl+muE*cl+S*z['Q']+(S-z['gamma'])*z['P']
  else:
   # Algebraically different expressions: mu-S=-(S-gamma)r^4/(6^4+r^4).
   negDelta=-(S-z['gamma'])*R**4/(6**4+R**4);muR=S+negDelta;muE=z['gamma']+(S-z['gamma'])*6**4/(6**4+Re**4)
   innerT=-1+(S-1)*cl+(z['b']-z['a'])*c+S*D+negDelta*L
   outerT=-1+(muE-1)*cl+S*(z['Q']+z['P'])-z['gamma']*z['P']
  out={'R':R,'Re':Re,'cl':cl,'c':c,'Cr':z['Cr'],'Ct':z['Ct'],'P':z['P'],'Q':z['Q'],'D':D,'inner_s_lower':L,'inner_v2_lower':cl+c-D,'inner_v1_upper':cl-c+D,'inner_T_upper':innerT,'outer_s_lower':cl-z['P'],'outer_vi_lower':cl-z['Q'],'outer_T_upper':outerT,'muR':muR,'muE':muE};values[method]={n:rec(v) for n,v in out.items()}
 for n in values['arb']:
  a=values['arb'][n];v=values['iv'][n];assert max(F(a['lower_exact']),F(v['lower_exact']))<=min(F(a['upper_exact']),F(v['upper_exact'])),n
 public={'R':('upper','0.007652'),'Re':('lower','27000000'),'D':('upper','0.0123'),'inner_v2_lower':('lower','21.289'),'inner_v1_upper':('upper','-10.138'),'inner_T_upper':('upper','-6.53'),'outer_s_lower':('lower','5.5752'),'outer_vi_lower':('lower','5.5752'),'outer_T_upper':('upper','-0.278')}
 for n,(direction,q) in public.items():
  for method in values:
   row=values[method][n];bound=F(row[direction+'_exact']);assert bound<F(q) if direction=='upper' else bound>F(q),(n,method,float(bound),q)
 assert F(values['arb']['R']['upper_exact'])<F(float(4.8)) and F(values['arb']['Re']['lower_exact'])>20
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/flow_ends/PROOF.md'),'dependency_pins':pins,'exact_inputs':{n:str(v) for n,v in x.items()},'values':values,'public':public,'method':'Arb512 direct conic formula versus iv180 factored mu-S formula; exact dependency and public-rounding checks. Underlying canonical moments are the previously audited shared inputs, not freshly integrated here.','seconds':time.monotonic()-start,'scope':'Whole inner disk and r>=exp(tb+9) only; finite annular flow and inverse remain open.'}
 (E/'checks.json').write_text(json.dumps(o,indent=2)+'\n');s={n:v for n,v in o.items() if n not in ['exact_inputs','values','dependency_pins']};s['inputs_display']={n:float(v) for n,v in x.items()};s['values_display']={m:{n:r['display'] for n,r in row.items()} for m,row in values.items()};s['checks_sha256']=sha(E/'checks.json');s['dependency_pin_count']=len(pins);(E/'review_summary.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps({'utc':o['utc'],'status':o['status'],'seconds':o['seconds'],'values':s['values_display']}))
if __name__=='__main__':main()
