"""Own exact polynomial jet manufactures, checked against raw mixed MP derivatives."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from flint import fmpq_poly as Poly,fmpq
from far_section_rational import construct,Jet,Parity,RF,set_base
from analytic_far_mp import FarModel

def mq(q):
 q=F(str(q));return mp.mpf(q.numerator)/q.denominator

def as_cheb(p):
 p=Poly(p);W=Poly([-1,2]);ts=[Poly([1])]
 if p.degree()>0:ts.append(W)
 for k in range(2,p.degree()+1):ts.append(2*W*ts[-1]-ts[-2])
 out=[F(0)]*len(ts)
 for k in range(len(ts)-1,-1,-1):
  q=p[k]/ts[k][k];out[k]=F(str(q));p=p-q*ts[k]
 if p:raise ArithmeticError('power/Clenshaw conversion')
 return out

if not __debug__:raise RuntimeError('normal Python required')
examples=[
 ('constant',[[2],[1],[3]],'1','3','11'),
 ('varying',[[2,'1/10','1/50'],[1,'1/3'],[3,'-1/8',2]],'3/2','3','11'),
 ('forcing_only',[[2,'1/20'],[],[]],'7/5','3','11'),
 ('negative_amplitude',[[3,'-1/10'],[-2,1],[0,0,0,2]],'2','3','-7')]
ws=[F(0),F(1,1000),F(1,5),F(1,2),F(4,5),F(999,1000),F(1)]
results=[]
for name,pol,s,alpha,a in examples:
 pol=[Poly([fmpq(str(v)) for v in row]) for row in pol]
 rr=construct(pol,s,alpha,4);A=Poly(rr['A']);B=(Poly([1])+fmpq(2,3)*Poly([1,0,0,-1]))*pol[0]-fmpq(2,3)*Poly([1,0,0,-1])*Poly([0,1])*pol[0].derivative()
 kk=rr['K'];nn=[Poly(p) for p in rr['numerators']]
 rr5=construct(pol,s,alpha,5)
 assert A==rr5['A']
 for p,q in zip(nn,rr5['numerators']):assert p*A**rr5['K']==q*A**kk
 mp_rows=[]
 for prec in (90,130):
  mp.mp.dps=prec;model=FarModel([as_cheb(p) for p in pol],F(s),F(alpha),F(a));c12=model.c1**2
  for w in ws:
   av=A(fmpq(str(w)));bv=B(fmpq(str(w)));assert av>0 and bv>0
   vals=[mq(p(fmpq(str(w)))/(av**kk))*(c12 if j<3 else mq(a)) for j,p in enumerate(nn)]
   physical=[v/mq(bv) for v in vals];r=model.section(w)
   err=max(abs(v-u)/(1+abs(u)) for v,u in zip(physical,r['terms_div_xy']))
   assert err<mp.mpf('1e-75'),(name,prec,str(w),err)
   n=mp.fsum(map(abs,vals));ratio=abs(mp.fsum(vals))/n
   assert abs(ratio-r['grouped_div_ratio'])<mp.mpf('1e-75')
   if name=='forcing_only':assert all(v==0 for v in vals[:3]) and ratio==1
   mp_rows.append({'dps':prec,'w':str(w),'maximum_term_error':mp.nstr(err,35),'grouped_ratio':mp.nstr(ratio,65)})
 results.append({'name':name,'s':s,'alpha':alpha,'a':a,'polynomials':[[str(v) for v in p.coeffs()] for p in pol],'A':[str(v) for v in A.coeffs()],'common_power':kk,'numerator_degrees':[p.degree() for p in nn],'order4_order5_exact_equal':True,'rows':mp_rows})
negative=construct([Poly([-1]),Poly([1]),Poly([1])],'1','3')
assert negative['A'](fmpq('1/2'))<0
rejections=[]
for label,fn in [('nonunit_power',lambda:Jet(2,{(0,0):2}).unit_power('1/3')),('order_increase',lambda:Jet(1).trunc(2)),('zero_inverse',lambda:RF(0).reciprocal())]:
 try:fn()
 except (ValueError,ZeroDivisionError) as e:rejections.append({'case':label,'error':str(e)})
 else:raise AssertionError(label)
root=Path('research/interval_far_section/verification');root.mkdir(exist_ok=True)
files=[Path(__file__),Path('code/far_section_rational.py'),Path('code/analytic_far_mp.py'),Path('research/interval_far_section/PROOF.md')]
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','examples':results,'negative_chart_detected':True,'rejections':rejections,'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'scope':'Exact order-truncation identities and finite two-precision MP comparisons. No global interval certificate yet. The single global polynomial base is reset only between completed source constructions.'}
(root/'rational_manufactures.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(results),'manufactures',sum(len(r['rows']) for r in results),'MP rows',flush=True)
