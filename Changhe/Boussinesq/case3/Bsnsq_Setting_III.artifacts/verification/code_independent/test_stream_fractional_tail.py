"""Independent SymPy controls of packet115's Fraction-only auditor."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
from fractions import Fraction as F
import json,sys,time,tempfile
from stream_fractional_tail_certificate import cheb,transport_derivative,checks,make,verify
start=time.monotonic();z,t=S.symbols('z t');records=[]
for n in range(12):
 a=cheb(n);assert S.expand(sum(S.Rational(v.numerator,v.denominator)*z**i for i,v in enumerate(a))-S.chebyshevt(n,z))==0
for beta in [F(9,4),F(5,2),F(11,4)]:
 for n in range(8):
  for k in [1-1/beta,-1-2/beta]:
   c=transport_derivative(cheb(n),k);a=sum(S.Rational(v.numerator,v.denominator)*z**i for i,v in enumerate(c));b=S.chebyshevt(n,z);assert S.expand(a-(S.Rational(k.numerator,k.denominator)*z*b+(1-z*z)*S.diff(b,z)))==0
   records.append({'test':'operator','beta':str(beta),'degree':n,'power':str(k),'pass':True})
for m in [3,4,5]:
 for ni in [m-1,m,m+1]:
  for nj in [1,3]:
   labels=[(i,j,d) for d in [0,1] for i in range(ni) for j in range(nj)]
   raw=[S.Poly(S.chebyshevt(i,2*t-1)*S.chebyshevt(j,z)*t**(m*d),t,z) for i,j,d in labels]
   gauged=[S.Poly(p.as_expr()-p.eval({t:1,z:0})*t**(m-1),t,z) for p in raw]
   def kernel(polys):
    rows=sorted({mon for p in polys for mon,c in p.terms()});M=S.Matrix([[p.coeff_monomial(mon) for p in polys] for mon in rows]);return len(polys)-M.rank()
   kr=kernel(raw);kg=kernel(gauged);expect=nj*max(0,ni-m);assert kr==expect and kg==expect+int(ni>=m)
   records.append({'test':'kernel_dimension','beta':m,'ni':ni,'nj':nj,'raw':kr,'gauged':kg,'pass':True})
# Exact nonzero-drift manufacture from the proof, independently specified.
manufacture={'beta':'5/2','labels':[(1,0,0),(0,1,1),(0,0,0)],'C':['-1','6/25','0'],'D':['0','-18/25','1']}
mc=checks(manufacture);assert mc['constant_vertical']=='1' and not mc['stream_nonzero'] and not mc['temperature_nonzero']
manufacture['D'][1]='-17/25';mc=checks(manufacture);assert not mc['stream_nonzero'] and mc['temperature_nonzero']
records.append({'test':'nonzero_drift_exact_compatibility_and_perturbation','pass':True})
# Imported coefficients tested against independent exact symbolic polynomial sums.
data={'beta':'5/2','ni':3,'nj':4,'shifts':[0,1],'labels':[(i,j,d) for d in [0,1] for i in range(3) for j in range(4)]}
data['C']=[str(F((17*k)%23-11,19)) for k in range(len(data['labels']))];data['D']=[str(F((11*k)%29-14,17)) for k in range(len(data['labels']))];c=checks(data)
for field,outkey,power in [('C','stream_residual_potential_polynomial',S.Rational(3,5)),('D','temperature_residual_polynomial',S.Rational(-9,5))]:
 A=[sum((-1)**i*S.Rational(v)*S.chebyshevt(j,z) for (i,j,d),v in zip(data['labels'],data[field]) if d==shift) for shift in [0,1]];Cinf=-sum(S.Rational(v)*S.chebyshevt(j,0) for (i,j,d),v in zip(data['labels'],data['C']));expected=S.expand(Cinf*(power*z*A[0]+(1-z*z)*S.diff(A[0],z))-S.Rational(5,2)*A[1]);got=sum(S.Rational(v)*z**i for i,v in enumerate(c[outkey]));assert S.expand(expected-got)==0
out=Path(sys.argv[1]);out.parent.mkdir(exist_ok=True,parents=True)
with tempfile.TemporaryDirectory(dir=out.parent) as td:
 td=Path(td);p=td/'input.json';q=td/'certificate.json';p.write_text(json.dumps(data));make(p,q);assert verify(p,q)
 bad=json.loads(q.read_text());bad['constant_vertical']='0';q.write_text(json.dumps(bad))
 try:verify(p,q);raise AssertionError('tamper accepted')
 except ValueError:pass
results={'status':'COMPLETE','ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'operator_controls':48,'Chebyshev_controls':12,'kernel_dimension_controls':18,'coefficient_controls':2,'tamper_rejection':True,'records':records};out.write_text(json.dumps(results,indent=2)+'\n');print(json.dumps({k:v for k,v in results.items() if k!='records'},indent=2))
