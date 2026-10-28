from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json
from flint import arb,ctx
from high_symbol_certificate import A
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'source_audit'))
from field_eval import State
ctx.prec=384
s=State(131,384)
p=json.loads(Path(__file__).with_name('state131_high_symbol_polynomials.json').read_text())
assert p['input_sha256']==s.data['canonical_serialization_sha256']
polys={key:{(i,j):Q(v) for i,j,v in vals} for key,vals in p['polynomials'].items()}
delta=Q(p['delta']);records=[]
for xi,yi in [('1/10','1/5'),('1','0'),('0','1'),('1','2'),('3','4'),('30','40'),('300','400')]:
 qx,qy=Q(xi),Q(yi);qq=qx*qx+qy*qy
 x=A(qx);y=A(qy);q=A(qq);t=A(qq/(1+qq));z=A((qx*qx-qy*qy)/qq);w=(1-t)**(A(delta)/2);sn=2*x*y/q
 fields={}
 for label in ['chi22','chi04','chi31','chi13','rad']:
  v=arb(0)
  for j in range(4):
   v+=w**(j+1)*sum((A(a)*t**i*z**k for (i,k),a in polys[f'{label}_{j}'].items()),arb(0))
  if label in ['chi31','chi13']:v*=sn
  fields[label]=v
 old=s.evaluate(x,y)
 expect={'chi22':old['du22'],'chi04':-old['rho_y']-old['du22'],'chi31':old['du21'],'chi13':-old['du12'],'rad':(old['u1']*x+old['u2']*y)/(1+q)}
 checks={k:fields[k].is_finite() and v.is_finite() and fields[k].overlaps(v) for k,v in expect.items()}
 assert all(checks.values()),(xi,yi,fields,expect)
 for k,rad,sigma in [(Q(1),Q(1),Q(0)),(Q(1),Q(1),Q(1,5)),(Q(2),Q(1,2),Q(1,5)),(Q(21,10),Q(1,2),Q(1,5)),(Q(3),Q(1,2),Q(6,5))]:
  tau=k-1-sigma;d=A(rad*rad)+(1-A(rad*rad))*t
  scalar=(1+(1-A(k))*s.cl)+A(tau)*(s.cl*t+fields['rad'])/d
  new=[scalar+(A(k)-1)*fields['chi22']-fields['chi04'],scalar-A(k)*fields['chi22'],((1-A(k))*fields['chi31']+(1+A(k))*fields['chi13'])/2]
  vx=s.cl*x+old['u1'];vy=s.cl*y+old['u2']
  sc=1+s.cl+A(tau)*(vx*x+vy*y)/(A(rad*rad)+q)
  direct=[sc-A(k)*(s.cl+old['du11'])+old['rho_y'],sc-A(k)*(s.cl+old['du22']),-A(k)*(old['du12']+old['du21'])/2-old['rho_x']/2]
  assert all(a.is_finite() and b.is_finite() and a.overlaps(b) for a,b in zip(new,direct)),(xi,yi,k,new,direct)
 records.append({'point':[xi,yi],'field_checks':checks,'all_five_matrix_formulas':'agree'})
 print('point',xi,yi,'OK',flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'input_sha256':p['input_sha256'],'checks':records}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
