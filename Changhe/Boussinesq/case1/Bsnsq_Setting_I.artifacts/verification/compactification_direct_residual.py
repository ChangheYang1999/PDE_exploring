"""High-precision full-plane mode Green residual test of the fractional far coefficient."""
import mpmath as mp,json,datetime
from pathlib import Path
mp.mp.dps=120
CT={1:list(map(mp.mpf,['.7','-.4','.2'])),3:list(map(mp.mpf,['.11','.06','-.02']))}
CO={2:list(map(mp.mpf,['-.5','.1','.03'])),4:list(map(mp.mpf,['.02','-.01']))}

def value(beta,tau,phi):
 delta=1/beta;gamma=1-2*delta;r=tau**(-beta);E=1+r*r;theta=tr=ta=ur=ua=mp.mpf(0)
 for m,coeff in CT.items():
  for k,b in enumerate(coeff):
   exponent=(gamma-m-k*delta)/2;f=b*r**m*E**exponent;theta+=f*mp.sin(m*phi);tr+=f*(m/r+2*exponent*r/E)*mp.sin(m*phi);ta+=m*f*mp.cos(m*phi)
 for m,coeff in CO.items():
  for k,b in enumerate(coeff):
   power=(m+(k+1)*delta)/2
   ji=b*r**m*mp.hyp2f1(power,m+1,m+2,-r*r)/(2*m+2)
   jo=b*r**(m-2)*E**(1-power)/(2*(power-1))
   ps=(ji+jo)/(2*m);ds=(jo-ji)/2;ur-=m*r*ps*mp.cos(m*phi);ua+=r*ds*mp.sin(m*phi)
 return ((beta*r+ur)*tr+ua/r*ta-(beta-2)*theta)/r**gamma

def lower(beta,tau,phi):
 delta=1/beta;gamma=1-2*delta
 F=lambda j:sum((co[j] if j<len(co) else 0)*mp.sin(m*phi) for m,co in CT.items())
 Fp=lambda j:sum(m*(co[j] if j<len(co) else 0)*mp.cos(m*phi) for m,co in CT.items())
 result=sum(-j*F(j)*tau**j for j in [1,2]);coefficients={j:-j*F(j) for j in [1,2]}
 for i in range(3):
  a=(i+1)*delta;d=2-a
  vr=sum(-m*(co[i] if i<len(co) else 0)/(m*m-d*d)*mp.cos(m*phi) for m,co in CO.items())
  va=sum(d*(co[i] if i<len(co) else 0)/(m*m-d*d)*mp.sin(m*phi) for m,co in CO.items())
  for j in range(3):
   k=i+j+1;c=(gamma-j*delta)*vr*F(j)+va*Fp(j)
   if k<2*beta:result+=c*tau**k;coefficients[k]=coefficients.get(k,0)+c
 C=beta*sum((m-gamma)*co[0]*mp.sin(m*phi) for m,co in CT.items())
 return result,C,coefficients
rows=[]
for b in ['2.8','3.05','3.25']:
 beta=mp.mpf(b)
 for ph in ['.317','.913']:
  phi=mp.mpf(ph);checks=[]
  for n in [1,2,3,4,6,8]:
   tau=mp.mpf(10)**(-n);res=value(beta,tau,phi);polynomial,C,coeff=lower(beta,tau,phi);fraction=(res-polynomial)/tau**(2*beta)
   checks.append({'tau':str(tau),'residual_normalized_by_r_gamma':str(res),'lower_integer_polynomial':str(polynomial),'isolated_fractional_coefficient':str(fraction),'predicted_coefficient':str(C),'relative_coefficient_error':str(abs((fraction-C)/C))})
  rows.append({'beta':b,'phi':ph,'checks':checks});print(json.dumps({'beta':b,'phi':ph,'finest_relative_error':checks[-1]['relative_coefficient_error']}),flush=True)
out=Path('research/compactification_obstruction/verification/direct_residual.json');out.write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'precision_decimal_digits':120,'scope':'Finite manufactured coefficient fields, not solutions. Full-plane inverse uses exact mode Green integrals evaluated with high-precision hypergeometric functions, separate from fitting/Jacobi code. No floors.','rows':rows},indent=2)+'\n')
