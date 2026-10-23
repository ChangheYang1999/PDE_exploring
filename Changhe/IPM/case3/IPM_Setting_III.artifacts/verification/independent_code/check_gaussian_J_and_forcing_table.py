"""Independent exact modal countertest and bounds on the reported forcing table.

Only numerical checkpoint metadata is read from the other lane. No producer
code is imported. This is a reporting audit, not an exact-profile construction.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import json,hashlib,math
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import mpmath as mp

t,z=s.symbols('t z',positive=True)
E=s.exp(-t)
g2=E*(t/s.Integer(2)+s.Rational(3,4)+3/(4*t))-3/(4*t)
g4=E*(t/s.Integer(4)+s.Rational(3,4)+3/(2*t)+3/(2*t*t))-3/(2*t*t)
for m,g,source in [(2,g2,(3*t-2*t*t)*E),(4,g4,-t*t*E)]:
    assert s.simplify(-4*(t*s.diff(g,t,2)+s.diff(g,t))+m*m*g/t-source)==0
    assert s.limit(g/t**(m//2),t,0).is_finite
    assert s.limit(g,t,s.oo)==0
assert s.limit(g2/t,t,0)==s.Rational(1,8)
# Laurent extraction of angular integrals, independently of the other audit.
v=s.symbols('v',nonzero=True)
sn=lambda n:(v**n-v**(-n))/(2*s.I)
cs=lambda n:(v**n+v**(-n))/2
mean=lambda f:s.expand(f).coeff(v,0)
angular=[]
for k in (1,3):
    for m in (2,4):
        angular.append({'density_mode':k,'stream_mode':m,
          'radial_integral_over_pi':str(2*mean(sn(k)*cs(m)*sn(3))),
          'angular_integral_over_pi':str(2*mean(sn(k)*sn(m)*cs(3)))})
assert [a['radial_integral_over_pi'] for a in angular]==['1/2','-1/2','0','0']
assert [a['angular_integral_over_pi'] for a in angular]==['-1/2','1/2','0','0']
B=s.simplify(2*g2-4*g4-2*t*s.diff(g2,t)+2*t*s.diff(g4,t))
integrand=s.simplify((1+t)*E/t**2*B)
expanded=(t/s.Integer(2)-s.Rational(7,2)/t-12/t**2-21/t**3-12/t**4)*E**2+(-3/t**2+9/t**3+12/t**4)*E
assert s.simplify(integrand-expanded)==0
# Integrate t**z times expanded for Re z>3, then analytically continue to z=0.
# The original integrand is bounded at zero, so this continuation equals its
# convergent integral. Factoring Gamma(z) leaves a factor vanishing at z=0.
Q=(z*(z+1)/(2*2**(z+2))-s.Rational(7,2)/2**z
   -12/((z-1)*2**(z-1))-3/(z-1)
   -21/((z-1)*(z-2)*2**(z-2))+9/((z-1)*(z-2))
   -12/((z-1)*(z-2)*(z-3)*2**(z-3))+12/((z-1)*(z-2)*(z-3)))
assert s.simplify(Q.subs(z,0))==0
I=s.simplify(s.diff(Q,z).subs(z,0))
J=s.simplify(3*s.pi*I/4)
expected=s.pi*(s.Rational(33,8)*s.log(2)-s.Rational(83,32))
assert s.simplify(J-expected)==0
mp.mp.dps=55
series=s.series(integrand,t,0,12).removeO()
f=s.lambdify(t,integrand,'mpmath');small=s.lambdify(t,series,'mpmath')
fnum=lambda u:small(u) if u<mp.mpf('.0001') else f(u)
Jn=3*mp.pi/4*mp.quad(fnum,[0,mp.mpf('.0001'),mp.mpf('.1'),1,8,mp.inf])
Jexact=mp.pi*(mp.mpf(33)/8*mp.log(2)-mp.mpf(83)/32)
assert abs(Jn-Jexact)<mp.mpf('1e-40')
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','gaussian':{
  'sigma':'y(1+4x^2) exp(-r^2)','rho':'-sigma/100','a':'-1/100','D':'1/400',
  'stream_sigma_modes':{'2':str(g2),'4':str(g4)},'angular_integrals':angular,
  'J_sigma_exact':str(J),'J_rho_exact':str(J/10000),'J_rho_decimal':str(Jn/10000),
  'quadrature_error_sigma':str(abs(Jn-Jexact)),'required_J_for_transport':0,
  'conclusion':'Gaussian satisfies strain/sign/kinematic escape but fails this weighted transport identity.'}}
source=Path('../numerics/runs/eps_cl2_eps0.0156.pt')
if source.exists():
    import torch
    torch.set_num_threads(1)
    d=torch.load(source,map_location='cpu',weights_only=True)
    metadata={}
    for k,value in d.items():
        if isinstance(value,(int,float,str,bool)):metadata[k]=value
        elif hasattr(value,'numel') and value.numel()==1:metadata[k]=value.item()
    result['forcing_source']={'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scalar_metadata':metadata,'all_keys':list(d)}
    mu=float(d['mu'])
else:
    mu=.4253011240
    result['forcing_source']={'source':str(source),'available':False,'mu_from_report':mu}
# Both widths bracket the textual ambiguity. Both refute the four large entries.
rows=[]
for width in (.0156,1/64):
    coeff=abs(mu)*width**4
    regional=[]
    for lower,printed in [(1.,1.1e-4),(10.,3.6e-4),(100.,6.0e-4),(1e4,6.4e-4)]:
        bound=coeff/lower**3
        tighter=abs(mu)*lower/(1+(lower/width)**2)**2
        assert printed>bound
        regional.append({'radius_lower':lower,'valid_bound':bound,'tighter_valid_bound':tighter,'printed_max':printed,'printed_over_bound':printed/bound})
    rows.append({'width':width,'coefficient_mu_width_fourth':coeff,'regions':regional})
result['forcing_bounds']=rows
result['scope']='Exact algebra and high precision quadrature for a specified nonprofile; analytic upper bounds refute printed forcing maxima. This does not recompute actual sampled residuals or assert an exact-profile counterexample.'
out=Path('research/monotonicity_and_sign/verification/gaussian_J_and_table.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
