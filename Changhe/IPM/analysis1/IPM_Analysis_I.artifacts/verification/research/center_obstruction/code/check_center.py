"""Two exact reconstructions and independent Arb/iv coefficient enclosures.
No numerical PDE approximation is used. Input binary64 values denote dyadics.
"""
import json, hashlib, sys, io, zipfile, struct, ast
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from datetime import datetime, timezone
from flint import arb, ctx
from mpmath import iv
BASE=Path(__file__).resolve().parents[3]
OUT=BASE/'research/center_obstruction/evidence'
SRC=BASE/'data_exact/modal_v2.json'
EXPECTED='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
def require(test, msg):
 if not test: raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dyadic_hex(s):
 # Exact parser independent of the Python floating conversion below.
 sign=-1 if s.startswith('-') else 1
 t=s.lstrip('+-'); mant, exponent=t.split('p');whole,frac=mant[2:].split('.')
 return sign*F(int(whole+frac,16),16**len(frac))*F(2)**int(exponent)
def binary64(s):return F.from_float(float.fromhex(s))
def aq(x):return arb(x.numerator)/x.denominator
def iq(x):return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def arf_fraction(x):
 n,e=x.man_exp();return F(int(n))*F(2)**int(e)
def mp_fraction(t):
 sign,man,exponent,bc=t
 return (-1 if sign else 1)*F(man)*F(2)**exponent
def ball_json(x):
 m,e=x.mid().man_exp();r,f=x.rad().man_exp()
 return {'mid_m':str(m),'mid_e':str(e),'rad_m':str(r),'rad_e':str(f)}
require(sha(SRC)==EXPECTED,'input pin mismatch')
data=json.loads(SRC.read_text());raw=data['arrays']['D'];M=raw['shape'][0]
require(raw['shape']==[260,7] and len(raw['hex'])==1820,'D shape')
parsed=[dyadic_hex(s) for s in raw['hex']]
require(all(x==binary64(s) for x,s in zip(parsed,raw['hex'])),'independent hex parsers disagree')
# Independently verify the array layout against the pinned original NPY member.
# Parse the binary header and payload directly, without numpy reshape semantics.
raw_source=BASE/'research/modal_exactification/evidence/trial_v2_h0.008.npz'
require(sha(raw_source)==data['source_npz_sha256']=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874','original source pin')
with zipfile.ZipFile(io.BytesIO(raw_source.read_bytes())) as archive:member=archive.read('D.npy')
require(member[:6]==b'\x93NUMPY','NPY magic')
version=tuple(member[6:8]);require(version in ((1,0),(2,0)),'NPY version')
size=2 if version==(1,0) else 4
hlen=int.from_bytes(member[8:8+size],'little');offset=8+size+hlen
header=ast.literal_eval(member[8+size:offset].decode('latin1'))
require(header=={'descr':'<f8','fortran_order':True,'shape':(260,7)},'pinned Fortran binary layout')
physical_values=[F.from_float(v[0]) for v in struct.iter_unpack('<d',member[offset:])]
require(len(physical_values)==1820,'binary payload length')
source_values=[physical_values[m+260*j] for m in range(260) for j in range(7)]
require(source_values==parsed,'original binary D versus exact JSON D')
d=parsed[::7]
require(d==[source_values[7*m] for m in range(M)],'D[m,0] indexing')
k=dyadic_hex(data['scalars_hex']['k']);cl=1/k;c=3/k-1
bi=dyadic_hex(data['scalars_hex']['bi']);ta=dyadic_hex(data['arrays']['knots']['hex'][0])
require(M>=3 and bi>49 and c>0 and d[2]!=0 and d[-1]!=0,'hypotheses')
# Method A: trig products and the radial/angular transport formula.
H=defaultdict(F)
for m,dm in enumerate(d):
 for nu in (1+2*m,1-2*m,3+2*m,3-2*m):
  H[abs(nu)]+=(1 if nu>0 else -1)*dm/8
H={nu:v for nu,v in H.items() if v}
E=defaultdict(F)
for nu,v in H.items():
 E[nu]+=(5*cl-1)*v
 E[nu+2]+=c*(nu-5)*v/2
 low=nu-2;E[abs(low)]+=(-1 if low<0 else 1)*(-c*(nu+5)*v/2)
E={nu:v for nu,v in E.items() if v}
# Method B: exact complex Laurent polynomials on z=x+iy, zbar=x-iy.
# Store the imaginary multiplier q for the coefficient i*q. For rho3,
# x^2*y=(z+zbar)^2*(z-zbar)/(8i).
rho3={3:F(-1,8),1:F(-1,8),-1:F(1,8),-3:F(1,8)}
Dl=defaultdict(F)
for m,dm in enumerate(d):
 Dl[2*m]+=dm/2;Dl[-2*m]+=dm/2
H_complex=defaultdict(F)
for n,q in rho3.items():
 for v,dm in Dl.items():H_complex[n+v]+=q*dm
require(all(H.get(n,F())==-2*q for n,q in H_complex.items() if n>0),'density Laurent mismatch')
require(all(H_complex[-n]==-q for n,q in H_complex.items()),'density reality')
E_complex=defaultdict(F)
for nu,q in H_complex.items():
 p=F(5+nu,2);qb=F(5-nu,2)
 require(p.denominator==1 and qb.denominator==1,'Laurent exponents')
 E_complex[nu]+=(5*cl-1)*q
 E_complex[nu-2]-=c*p*q
 E_complex[nu+2]-=c*qb*q
Ec={n:-2*q for n,q in E_complex.items() if n>0 and q}
require(E==Ec,'entire residual linear term differs between methods')
require(all(E_complex[-n]==-q for n,q in E_complex.items()),'residual reality')
nu_rho=2*M+1;nu_res=2*M+3;expected=c*(M-2)*d[-1]/8
require(max(H)==nu_rho and max(E)==nu_res,'highest frequencies')
require(H[nu_rho]==d[-1]/8 and E[nu_res]==expected,'highest coefficient identity')
# R=exp(ta). Both methods certify the common rational decimal bracket;
# mere interval overlap would not suffice for an enclosure comparison.
ctx.prec=384;iv.dps=160
ball=aq(expected)*(-2*aq(ta)).exp()
ival=iq(expected)/(iv.exp(iq(ta))**2)
blo=arf_fraction(ball.lower());bhi=arf_fraction(ball.upper())
ilo=mp_fraction(ival._mpi_[0]);ihi=mp_fraction(ival._mpi_[1])
# Bracket coarse enough to be human readable; chosen after exact value only.
low=F('0.000000000005');high=F('0.000000000006')
require(low<blo<=bhi<high and low<ilo<=ihi<high,'positive common bracket')
# Check the two rigorous enclosures overlap, as an additional consistency test.
require(max(blo,ilo)<=min(bhi,ihi),'disjoint independent enclosures')
result={
 'utc':datetime.now(timezone.utc).isoformat(),'status':'EXACT_ALGEBRA_AND_ENCLOSURES_CONFIRMED',
 'python':sys.version,'input_sha256':sha(SRC),'code_sha256':sha(Path(__file__)),
 'M':M,'bi':str(bi),'ta':str(ta),'k':str(k),'c':str(c),
 'original_npy_fortran_order':header['fortran_order'],'original_npz_sha256':sha(raw_source),'original_D_row_major_values_checked':len(source_values),'independent_hex_parser_checks':len(parsed),'density_positive_modes':len(H),
 'residual_positive_modes':len(E),'D2':str(d[2]),'Dlast':str(d[-1]),
 'rho_highest_frequency':nu_rho,'residual_highest_frequency':nu_res,
 'rho_highest_coefficient_before_exp_minus_2ta':str(H[nu_rho]),
 'residual_highest_coefficient_before_exp_minus_2ta':str(expected),
 'residual_coefficient_arb':ball_json(ball),'arb_decimal_display':str(ball),
 'iv_lower_exact':str(ilo),'iv_upper_exact':str(ihi),
 'certified_common_rational_bracket':[str(low),str(high)],
 'working_a':'129/20','working_b':'307/100','working_A':'238/25',
 'radial_squared_integrand_power':'-201/25',
 'scope':'Exact modal input only. The nonlinear cubic-velocity term is a degree-five polynomial and cannot cancel this frequency. Analytic regularity and weighted-divergence claims require PROOF.md, not computation alone.'}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'center_checks.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'exact_modes.json').write_text(json.dumps({'density5_before_exp_minus_2ta':{str(k):str(v) for k,v in sorted(H.items())},'linear_residual5_before_exp_minus_2ta':{str(k):str(v) for k,v in sorted(E.items())}},indent=2)+'\n')
print(json.dumps(result,indent=2))
