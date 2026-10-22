"""Two exact angular reconstructions and Arb/iv enclosures of trial axis logs."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,json,hashlib,struct,zipfile,ast,io,time
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from datetime import datetime,timezone
import sympy as s,flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/trial_axis_log/evidence';start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
src=B/'data_exact/modal_v2.json';orig=B/'research/modal_exactification/evidence/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def parse(h):
 sign=-1 if h[0]=='-' else 1;h=h.lstrip('+-');m,e=h.split('p');a,b=m[2:].split('.');return sign*F(int(a+b,16),16**len(b))*F(2)**int(e)
assert sha(src)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
data=json.loads(src.read_text());raw=data['arrays']['D'];assert raw['shape']==[260,7] and len(raw['hex'])==1820
v=[parse(h) for h in raw['hex']];assert all(a==F.from_float(float.fromhex(h)) for a,h in zip(v,raw['hex']))
assert sha(orig)==data['source_npz_sha256']=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with zipfile.ZipFile(io.BytesIO(orig.read_bytes())) as z:mem=z.read('D.npy')
assert mem[:6]==b'\x93NUMPY';ver=tuple(mem[6:8]);assert ver in [(1,0),(2,0)];sz=2 if ver==(1,0) else 4;hl=int.from_bytes(mem[8:8+sz],'little');off=8+sz+hl
header=ast.literal_eval(mem[8+sz:off].decode('latin1'));assert header=={'descr':'<f8','fortran_order':True,'shape':(260,7)}
phys=[F.from_float(a[0]) for a in struct.iter_unpack('<d',mem[off:])];assert len(phys)==1820 and [phys[m+260*j] for m in range(260) for j in range(7)]==v
d=v[::7];db=phys[:260];assert d==db
# Method1: product-to-sum and polar differentiation.
H=defaultdict(F)
for m,dm in enumerate(d):
 for l in [1+2*m,1-2*m,3+2*m,3-2*m]:H[abs(l)]+=(1 if l>0 else -1)*dm/8
H={l:h for l,h in H.items() if h};Force=defaultdict(F)
for l,h in H.items():
 Force[l+1]+=(5-l)*h/2
 if l>1:Force[l-1]+=(5+l)*h/2
Force={l:f for l,f in Force.items() if f}
h7=(d[2]+d[3]-d[4]-d[5])/8;assert h7==H[7] and Force[6]==6*h7 and h7!=0
braw=sum((1-2*m*m)*dm for m,dm in enumerate(d));assert braw==sum(F(l*(13-l*l),6)*h for l,h in H.items()) and braw!=0
# Method2: complex Laurent multiplication from independently read binary column.
# Store coefficient i*q of z^a zbar^b, where a+b=5. Negative powers are allowed away from zero.
P={3:F(-1,8),1:F(-1,8),-1:F(1,8),-3:F(1,8)};C=defaultdict(F)
for l,q in P.items():
 for m,dm in enumerate(db):C[l+2*m]+=q*dm/2;C[l-2*m]+=q*dm/2
C={l:q for l,q in C.items() if q};CF=defaultdict(F)
for l,q in C.items():
 aa=F(5+l,2);bb=F(5-l,2);assert aa.denominator==bb.denominator==1
 CF[l-1]+=aa*q;CF[l+1]+=bb*q
assert CF[0]==0
assert H=={l:-2*q for l,q in C.items() if l>0 and q}
assert Force=={l:-2*q for l,q in CF.items() if l>0 and q}
assert all(C.get(-l,F())==-q for l,q in C.items()) and all(CF.get(-l,F())==-q for l,q in CF.items())
# Symbolic independent differential calculation with z representing log(x).
x=s.symbols('x',positive=True);z,A,p,lam,w3,w5,g4,g6,b2,b4,b6=s.symbols('z A p lam w3 w5 g4 g6 b2 b4 b6')
def D(e):return s.diff(e,x)+s.diff(e,z)/x
def zero(e):assert s.cancel(s.expand(e))==0
r,th=s.symbols('r th',positive=True);ps=r**6*s.log(r)*s.sin(6*th)
zero(s.diff(ps,r,2)+s.diff(ps,r)/r+s.diff(ps,th,2)/r**2-12*r**4*s.sin(6*th))
# Axis derivative via Im((x+i y)^6) log(sqrt(x²+y²)).
y=s.symbols('y',real=True);im6=6*x**5*y-20*x**3*y**3+6*x*y**5
zero(s.diff(im6*s.log(x*x+y*y)/2,y).subs(y,0)-6*x**5*s.log(x))
zero(s.diff(x*x*y,x)-2*x*y);assert F(3-1,8)+F(3+3,8)==1
wm=-A*x+w3*x**3+lam*x**5*z+w5*x**5;gm=x*x+g4*x**4+g6*x**6
w2m=(D(gm)-D(D(wm)))/2;v3m=-D(w2m)/3;fm=s.expand(-(w2m*D(gm)+v3m*gm))
zero(w2m.coeff(x,3).coeff(z,1)+10*lam);zero(s.expand(v3m).coeff(x,2).coeff(z,1)-10*lam);zero(fm.coeff(x,4).coeff(z,1)-10*lam)
invF=1+w3/A*x*x+(lam/A*z+w5/A+w3*w3/A**2)*x**4
qm=s.expand((-A*p+9*w3*x*x+3*lam*(5*z+1)*x**4+15*w5*x**4)*invF/(A*x))
qm=sum(qm.coeff(x,j)*x**j for j in [-1,1,3]);zero(qm.coeff(x,3).coeff(z,1)-(15-p)*lam/A)
q1=qm.coeff(x,1);q30=qm.coeff(x,3).coeff(z,0);q31=qm.coeff(x,3).coeff(z,1)
Em=s.expand(-q1*x*x/2-q30*x**4/4-q31*x**4*(z/4-s.Rational(1,16)));zero(D(Em)+qm+p/x)
zero(Em.coeff(x,4).coeff(z,1)-(p-15)*lam/(4*A))
ee=s.expand(1-Em+Em*Em/2);ee=sum(ee.coeff(x,j)*x**j for j in [0,2,4])
Qf=s.expand(-ee*invF*fm/A);zero(Qf.coeff(x,4).coeff(z,1)+10*lam/A)
Gm=b2*x*x+b4*x**4+b6*x**6;Qt=s.expand(x*ee*(D(Gm)+qm*Gm));zero(Qt.coeff(x,6).coeff(z,1)-(6-p)*(15-p)*lam*b2/(4*A));assert Qt.coeff(x,4).coeff(z,1)==0
j=s.symbols('j');primitive=x**(j-p)*(s.log(x)/(j-p)-1/(j-p)**2);zero(s.diff(primitive,x)-x**(j-p-1)*s.log(x))
# Numerical coefficients in physical x units, not the dimensionless r/R variable.
k=parse(data['scalars_hex']['k']);ta=parse(data['arrays']['knots']['hex'][0]);bi=parse(data['scalars_hex']['bi']);Av=2/k-1;pv=6+2/Av;assert bi>49 and 6<pv<7
assert all(F.from_float(float.fromhex(h))==parse(h) for h in [data['scalars_hex']['k'],data['scalars_hex']['bi'],data['arrays']['knots']['hex'][0]])
def ar(a):a=F(a);return arb(a.numerator)/a.denominator
def ii(a):a=F(a);return iv.mpf(a.numerator)/iv.mpf(a.denominator)
def ae(a):
 assert a.is_finite();out=[]
 for t in [a.lower(),a.upper()]:
  assert t.rad()==0;n,e=t.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def ie(a):return [(-1 if sg else 1)*F(int(n))*F(2)**int(e) for sg,n,e,bc in a._mpi_]
def pack(e):return {'lower_exact':str(e[0]),'upper_exact':str(e[1])}
escale=(-2*ar(ta)).exp();rsq=iv.exp(ii(ta))**2
ha=ar(h7)*escale;ba=ar(braw)*escale;la=3*ha
coeffa={'H7':ha,'b2':ba,'w_x5log':la,'Qf_x4log':-10*la/ar(Av),'Qtotal_x6log':ar(6-pv)*ar(15-pv)*la*ba/(4*ar(Av))}
coeffi={'H7':ii(h7)/rsq,'b2':ii(braw)/rsq,'w_x5log':ii(3*h7)/rsq,'Qf_x4log':ii(-30*h7/Av)/rsq,'Qtotal_x6log':ii(-3*h7*braw*(9*Av-2)/(2*Av**3))/(rsq*rsq)}
rows={}
for name,a in coeffa.items():
 be=ae(a);ce=ie(coeffi[name]);assert max(be[0],ce[0])<=min(be[1],ce[1]);lower=min(be[0],ce[0]);upper=max(be[1],ce[1]);assert lower*upper>0
 mag=max(abs(lower),abs(upper));step=F(1)
 while mag>=step*10000:step*=10
 while mag<step*1000:step/=10
 low=(lower//step-1)*step;high=(upper//step+1)*step;assert low<lower<=upper<high and low*high>0
 rows[name]={'arb':pack(be),'iv':pack(ce),'common_strict_bracket':[str(low),str(high)]}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_sha256':sha(B/'research/trial_axis_log/PROOF.md'),'code_sha256':sha(__file__),'input_sha256':sha(src),'original_npz_sha256':sha(orig),'checks':{'all_D_binary_layout':1820,'two_hex_parsers':1820,'density_positive_modes':len(H),'forcing_positive_modes':len(Force),'H7_formula':1,'b2_formulas':1,'symbolic_log_identities':12,'independent_enclosures':5},'parameters':{'k':str(k),'A':str(Av),'p':str(pv),'ta':str(ta),'bi':str(bi)},'exact_raw_coefficients':{'h7':str(h7),'b2raw':str(braw),'d2_to_d5':[str(d[m]) for m in range(2,6)]},'coefficients':rows,'runtime':{'python':sys.version,'sympy':s.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_dps':iv.dps},'seconds':time.monotonic()-start,'scope':'Trial resonant coefficients and failure of polynomial-only Q subtraction. No value of generalized B3[f], PDE existence, or neighborhood exclusion.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');(E/'exact_modes.json').write_text(json.dumps({'density5_raw':{str(l):str(h) for l,h in sorted(H.items())},'forcing4_raw':{str(l):str(f) for l,f in sorted(Force.items())}},indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':'PASS','seconds':out['seconds'],'coefficients':{k:v['common_strict_bracket'] for k,v in rows.items()}}))
