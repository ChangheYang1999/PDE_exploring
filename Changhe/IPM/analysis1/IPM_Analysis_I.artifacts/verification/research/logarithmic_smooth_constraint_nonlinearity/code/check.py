from pathlib import Path
import sys,os,json
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_smooth_constraint_nonlinearity';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='935abeef7acbb87346ccf8471b9e87e5ecc1d337af0a54db99cb0a6e4ec0e701'
parent='research/logarithmic_algebraic_constraint_nonlinearity/evidence/verdict.json';pv=p.load(R/parent);assert p.sha(R/parent)=='01ca5ea5920a5e3a6409d9c728293231b0fc9ccbafde8ef0bee2b4f01f3e46ec';assert pv['status']=='CONFIRMED_FULL_GRAPH_NONLINEAR_DISCONTINUITY_UNDER_ANY_FINITE_ALGEBRAIC_LINEAR_CONSTRAINTS';pins=dict(pv['files']);p.pin(pins,parent);p.rehash(pins)
g0,g1,h0,h1,w0,w1,b00,b01,b10,b11,t,a=S.symbols('g0 g1 h0 h1 w0 w1 b00 b01 b10 b11 t a');G=S.Matrix([g0,g1]);H=S.Matrix([h0,h1]);W=S.Matrix([w0,w1]);B=S.Matrix([[b00,b01],[b10,b11]])
def bil(x,y):return (x.T*B*y)[0]
def q(x):return bil(x,x)
def c(x,y):return bil(x,y)+bil(y,x)
checks={}
def ck(name,value):
 v=S.expand(value);assert v==0,(name,v);checks[name]=str(v)
ck('quadratic_perturbation',q(G+W)-q(G)-c(G,W)-q(W))
ck('cross_scalar_linearity',c(t*G,a*W)-t*a*c(G,W))
ck('plus_packet_correction',c(t*(G+H),a*W)-t*a*(c(G,W)+c(H,W)))
ck('minus_packet_correction',c(t*(G-H),a*W)-t*a*(c(G,W)-c(H,W)))
ck('full_scaled_perturbation',q(t*(G+H)+a*W)-t*t*q(G+H)-t*a*c(G+H,W)-a*a*q(W))
ck('scaled_polarization',q(t*(G+H))-q(t*(G-H))-2*t*t*c(G,H))
# Manufactured finite scalar equations only; these are not IPM constraint data.
fixtures=[]
for power in [5,6,8]:
 nu=S.Rational(power,4)
 for N in [1,2,3,7,16,31,101]:
  n=S.Integer(N)**8;t0=S.Rational(1,N**4);a0=-t0**nu
  assert n*t0*t0==1 and a0==-S.Rational(1,N**power)
  errors=[]
  for sign in [-1,1]:
   x=sign*t0;value=S.simplify(a0+abs(x)**nu);assert value==0;errors.append(str(value))
  ratio=abs(a0)/t0;bound=n*t0*abs(a0)+a0*a0
  assert ratio==S.Rational(1,N**(power-4)) and bound==S.Rational(1,N**(power-4))+S.Rational(1,N**(2*power))
  fixtures.append({'power':power,'nu':str(nu),'N':N,'n':str(n),'t':str(t0),'a':str(a0),'constraint_at_two_signs':errors,'correction_over_t':str(ratio),'cross_plus_square_bound':str(bound)})
out={'start_utc':start,'utc':p.now(),'status':'PASS_QUADRATIC_CORRECTION_ALGEBRA_AND_FINITE_SCALAR_FIXTURES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':dict(sorted(pins.items())),'parent_pin_count':len(pins),'symbolic_identities':checks,'fixtures':fixtures,'scope':'Six generic nonsymmetric quadratic identities and21 manufactured scalar constraints a+abs(x)^nu,42 signed evaluations. They check algebra, not arbitrary nonlinear maps, contraction existence, IPM constraint values, Sobolev bounds or any interval/norm constant.'};p.write(E/'check.json',out);print(json.dumps({k:v for k,v in out.items() if k not in ['parent_files','fixtures']}))
