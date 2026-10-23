"""Manufactures for the new P=2 inverse, before use on saved states."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
import mpmath as mp
import sympy as sp
import hydrostatic_axis_log_constant as lc
from hydrostatic_axis_tail_series import coordinate,horner
ROOT=Path('research/hydrostatic_axis_log_constant');V=ROOT/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
def st(x):return mp.nstr(x,35)
u=sp.symbols('u');ww=u-u**2/4-u**3/32
check('exact coordinate cubic inversion',sp.series(ww-u*(1-ww)**sp.Rational(1,4),u,0,4).removeO()==0)
x=sp.symbols('x',positive=True);K,Q,c2,c3,B,M=sp.symbols('K Q c2 c3 B M',nonzero=True);ell=sp.symbols('ell')
# x=y^(-1/2); retain log(y) as a formal symbol only after differentiation.
y=sp.symbols('y',positive=True);G=K*sp.sqrt(y)+c2+c3/sp.sqrt(y);U=4*Q*sp.sqrt(y)+B*sp.log(y)+M
R=sp.expand((2*y+U)*sp.diff(G,y)-G);r2=-c2+2*K*Q
RX=sp.expand(R.subs(y,x**-2)).subs(sp.log(x),-ell/2)
expected=r2+x*(K*B*ell/2+K*M/2-2*c3)
check('residual expansion symbolic',sp.series(RX-expected,x,0,2).removeO()==0)
N=2*(K/x+c2+c3*x)+RX
ratio=sp.series(RX/(x*x*N),x,0,1).removeO()
expectedratio=r2/(2*K*x)+B*ell/4+M/4-c3/K-r2*(2*c2+r2)/(4*K*K)
check('normalized constant correction exact',sp.simplify(ratio-expectedratio)==0)
rows=[]
for digits in (65,100):
 with mp.workdps(digits):
  polynomials=[]
  for j in (1,2,3,6):
   k=[mp.mpf(0)]*(j+1);k[j]=mp.mpf(1);polynomials.append(('mode'+str(j),k))
  polynomials.extend([('signed',list(map(mp.mpf,['0','3','-7','2','.125','-1']))),('logzero',list(map(mp.mpf,['0','4','1','-2'])))])
  for tag,k in polynomials:
   i0=lc.integral_I0(k);closed=lc.beta_I0(k);error=abs(i0-closed);check(tag+str(digits)+' convergent I0',error<mp.mpf(10)**(-digits+8),st(error))
   for C0 in ('0.125','1','3.5'):
    C=mp.mpf(C0);H=list(map(mp.mpf,['0','1','-.3','.11','-.04']));const=lc.constants(C,H,k)
    Mind=C*(lc.at(k,2)-lc.at(k,1)+i0)-const['B_log']*mp.log(C)
    check(tag+str(digits)+C0+' independent constant',abs(Mind-const['M'])<mp.mpf(10)**(-digits+7),st(Mind-const['M']))
    for factor in ('16','1e4','1e12'):
     yy=C*mp.mpf(factor);z=lc.velocity(C,k,yy,128);w=z['w'];kp=[j*k[j]for j in range(1,len(k))]
     direct=yy*horner(k,w)+C*mp.quad(lambda v:mp.sqrt(1-v)*horner(kp,v)/(v*v),[w,mp.sqrt(w),mp.mpf('.75'),1])
     error=abs(z['V2']-direct);roundoff=mp.mpf(10)**(-digits+10)*(1+abs(direct));bound=z['remainder_bound']
     label=tag+str(digits)+C0+factor
     check(label+' direct complete integral',error<=bound+roundoff,dict(error=st(error),analytic_tail=st(bound),rounding_allowance=st(roundoff)))
     check(label+' exact map',abs(C*mp.sqrt(1-w)/(w*w)/yy-1)<mp.mpf(10)**(-digits+6))
     if factor=='16':
      rr=lc.velocity(C,k,yy,16);check(label+' analytic truncation bound',abs(rr['V2']-z['V2'])<=rr['remainder_bound']+roundoff)
     if factor=='1e4':
      g,gy=lc.axis_jet(C,H,yy);d=mp.diff(lambda Y:Y*horner(H,coordinate(2,C,Y)),yy)
      check(label+' independent scalar derivative',abs(gy-d)<mp.mpf(10)**(-digits+6))
    # Far expansion checked on increasing physical radii, independently from the proof.
    errors=[]
    for YY in ('1e12','1e20','1e28'):
     yy=mp.mpf(YY);r=lc.residual(C,H,k,yy,128);pred=const['residual_sqrt']*mp.sqrt(yy)+const['residual_log']*mp.log(yy)+const['residual_constant'];err=abs(r['y_signed_R_Nf']-pred)
     errors.append(err)
    check(tag+str(digits)+C0+' asymptotic residual decays',errors[1]<errors[0]/1000 and errors[2]<errors[1]/1000,[st(z)for z in errors])
    if tag=='logzero':check('zero logarithm '+str(digits)+C0,const['B_log']==0)
    rows.append(dict(digits=digits,tag=tag,C=C0,M=st(const['M']),B_log=st(const['B_log']),asymptotic_errors=[st(z)for z in errors]))
result=dict(status='PASS'if all(t['passed']for t in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,proof_sha256=sha(ROOT/'PROOF.md'),module_sha256=sha(lc.__file__),driver_sha256=sha(__file__),coordinate_module_sha256=sha('independent_code/hydrostatic_axis_tail_series.py'))
(V/'GATE.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count']);print([t for t in checks if not t['passed']])
if result['status']!='PASS':raise SystemExit(1)
