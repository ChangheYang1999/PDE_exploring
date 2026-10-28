from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
from flint import arb, fmpq, ctx

out = Path(__file__).resolve().parents[1] / 'evidence' / 'check.json'
r = s.symbols('r', positive=True)
b = s.Function('b')(r)
i2, i6, i8 = (s.Function(n)(r) for n in ('I2', 'I6', 'I8'))
rules = {
    s.diff(i2, r, 2): -b-r*s.diff(b,r), s.diff(i2,r): -r*b,
    s.diff(i6, r, 2): 5*r**4*b+r**5*s.diff(b,r), s.diff(i6,r): r**5*b,
    s.diff(i8, r, 2): 7*r**6*b+r**7*s.diff(b,r), s.diff(i8,r): r**7*b,
}
def reduce(x):
    return s.simplify(x.subs(rules))
def poisson(p,n):
    return reduce(-s.diff(p,r,2)-s.diff(p,r)/r+n*n*p/r**2)
p2=(r*r*i2-r**(-2)*i6)/8
p4=-r**(-4)*i8/8
checks={}
checks['mode2_poisson']=poisson(p2,2)-r*r*(b+r*s.diff(b,r)/4)
checks['mode4_poisson']=poisson(p4,4)-r**3*s.diff(b,r)/8
v=i2/4-r**(-4)*i6/4+r**(-6)*i8/2
checks['axis_velocity']=2*p2/r**2-4*p4/r**2-v
checks['axis_log_derivative']=reduce(r*s.diff(v,r))-(r**(-4)*i6-3*r**(-6)*i8)
th=s.symbols('theta', real=True)
checks['strain_angular']=s.integrate(s.cos(th)**2*s.sin(th)*s.sin(3*th),(th,0,2*s.pi))/s.pi-s.Rational(1,4)
u=s.symbols('u', positive=True)
K=-s.exp(-2*u)/4-s.exp(-6*u)/4+s.exp(-8*u)/2
checks['past_derivative_kernel']=s.simplify(2*K+s.diff(K,u)-(s.exp(-6*u)-3*s.exp(-8*u)))
ss,vv,yy=s.symbols('s v y', real=True)
kernel=(ss**2-(yy-vv)**2)/(2*s.pi*(ss**2+(yy-vv)**2)**2)
checks['strain_kernel']=s.diff(kernel,yy).subs(yy,0)-vv*(3*ss**2-vv**2)/(s.pi*(ss**2+vv**2)**3)
a=s.Rational(17,4); eta=s.Rational(5,4); k=s.symbols('k')
checks['left_integrability_exponent']=4-s.Rational(1,2)-s.Rational(7,2)
checks['right_integrability_exponent']=2*(k-s.Rational(35,8))+s.Rational(27,4)-2*(k-1)
checks['jet_decay_exponent']=(3-k)+(s.Rational(3,8)+k)-s.Rational(27,8)
checks['near_jet_first_bound']=s.Rational(1,8)+s.Rational(1,24)+s.Rational(1,16)-s.Rational(11,48)
checks['near_jet_derivative_bound']=s.Rational(1,6)+s.Rational(3,8)-s.Rational(13,24)
checks['near_jet_gamma_bound']=s.Rational(11,48)+2*s.Rational(13,24)-s.Rational(63,48)
res={name: str(s.simplify(expr)) for name,expr in checks.items()}
assert all(x=='0' for x in res.values()),res
balls=[]
for bits in (384,768):
    ctx.prec=bits
    aa=arb(fmpq(17,4)); ee=arb(fmpq(5,4)); pi=arb.pi()
    m3=((12/pi)**2*2*pi*(arb(5)**(2*aa-8)/(2*aa-8)+(arb(4)/3)**10*arb(4)**(ee-8)/(8-ee))).sqrt()
    fs=[]
    for j in (0,1):
        fac=arb(s.factorial(j+1).__int__())/(2*pi)
        bracket=arb(2)**(2+2*j-ee)/(2*aa-2-2*j)+arb(2)**(2+2*j-ee)/(ee+2)+arb(2)**(ee+5+2*j)+arb(2)**(ee+2)/(2+2*j-ee)
        fs.append((fac**2*2*pi*bracket).sqrt())
    assert m3<arb('20.3')
    assert fs[0]<arb('4')
    assert fs[1]<arb('15')
    balls.append((m3,*fs))
assert all(x.overlaps(y) for x,y in zip(*balls))
data={
    'date_utc':datetime.now(timezone.utc).isoformat(),
    'symbolic_checks':res,
    'interval_constants':[{'precision_bits':p,'M3_bound':str(row[0]),'F0_bound':str(row[1]),'F1_bound':str(row[2])} for p,row in zip((384,768),balls)],
    'proved_upper_bounds':{'M3':'20.3','F0':'4','F1':'15'},
    'status':'PASS',
    'scope':'Universal trace-kernel upper bounds; background A and axis H constants are not evaluated here.'
}
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
