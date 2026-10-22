from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import os,json,hashlib,sys
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import mpmath as mp
from interval_residual221 import Field,I,B
mp.mp.dps=230
j={'beta':'3','M':3,'alpha':'3','s':'2','a':'600','outer':[['1','1/100','-1/1000'],['1/90','1/400','-1/1200']],'patches':[{'R':'3/2','L':'5/2','coefficients':[['1/10000','-1/9000','1/8000'],['-1/7500','1/7000','-1/6500']]}]}
f=Field(j);checks=[]
def mr(q):q=F(q);return mp.mpf(q.numerator)/q.denominator
def cheb(t,n):return mp.chebyt(n,2*t-1)
def poly(c,t,w):return sum(mr(z)*cheb(t,i)*cheb(w,k)for i,row in enumerate(c)for k,z in enumerate(row))
def oracle(x,h):
 E=1+x*x+(h/2)**6;q=mp.power(E,-mp.mpf(1)/6);t=-mp.log(1-(1-mp.exp(-3))*q)/3;w=(h/2)**2*q*q;p=j['patches'][0];R,L=mr(p['R']),mr(p['L']);v=poly(j['outer'],t,w)+mp.exp(-(x*x+h*h)/(L*L))*poly(p['coefficients'],x*x/(R*R+x*x),h*h/(R*R+h*h));return x*h*q**(-2)*v
for x,h in [(F(1,3),F(2,5)),(F(3,2),F(7,4)),(F(20),F(3))]:
 width=F(1,2**60);g=f.generating(x,I(I.of(h-width).lo,I.of(h+width).hi))
 for htest in [h-width,h,h+width]:
  for i,k in g.c:
   value=mp.diff(oracle,(mr(x),mr(htest)),(i,k))/(factorial(i)*factorial(k));approx=F(mp.nstr(value,220));interval=g.c[i,k]
   if not interval.contains(approx):raise RuntimeError(('interval oracle containment',x,htest,i,k,mp.nstr(value,12),str(interval.dump())))
   checks.append({'x':str(x),'eta_base':str(h),'eta_test':str(htest),'derivative':[i,k],'width':str(interval.width())})
for where in ['outer','patch']:
 import copy
 bad=copy.deepcopy(j)
 if where=='outer':bad['outer']=[[1,2],[3]]
 else:bad['patches'][0]['coefficients']=[[1],[2,3]]
 try:Field(bad)
 except ValueError:checks.append({'ragged_refused':where})
 else:raise RuntimeError('ragged accepted')
now=datetime.now(timezone.utc).isoformat();paths=[__file__,'code/interval_residual221.py','code/dyadic_root220.py','research/interval_residual221/PROOF.md'];out={'utc':now,'status':'PASS_NONZERO_WIDTH_NONLINEAR_COMPOSITION','check_count':len(checks),'checks':checks,'scope':'230working-digit derivative oracle rounded220digits lies in 135values in45finite-width derivative intervals, plus2ragged-array refusals; this oracle comparison is diagnostic, not certified oracle accuracy. No fitted candidate evaluated.','hashes':{str(Path(p).resolve()):hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in paths}};Path('research/interval_residual221/verification/interval_composition.json').write_text(json.dumps(out,indent=2)+'\n');print(now,out['status'],len(checks))
