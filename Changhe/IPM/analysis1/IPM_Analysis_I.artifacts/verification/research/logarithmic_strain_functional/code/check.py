from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
import numpy as np
import sympy as S
from flint import arb,fmpq,ctx
ctx.prec=512;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_strain_functional';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='d4284c845df4c9717c4618916e7972b84e6a57cd1b5dd4da271062d375616115'
parent='research/canonical_residual_weak_axis_membership/evidence/verdict.json';pv=p.load(R/parent);pins=dict(pv['files']);p.pin(pins,parent,'c7bac166b33be55d4a95ed02ebc28e16dd497c447b082ef499fd4efce45bdb9f');p.rehash(pins)
raw=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert p.sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(raw,allow_pickle=False) as z:k=F.from_float(float(z['k'].item()))
b=F(3,2);s=F(153,50);u=2-b;v=s+b-2;v0=v-2;fac=v0*(v0+1)/((u+v0)*(u+v0+1));assert 2*k<b<2 and b<F(5,2) and u==F(1,2) and v==F(64,25) and v0==F(14,25) and fac==F(2184,5459)
actual={n:str(x) for n,x in {'k':k,'b':b,'s':s,'u':u,'v':v,'v0':v0,'beta_reduction_factor':fac,'gamma_argument':2*b+1,'power_of_two':2*b+2,'residual_lower_gap':b-2*k,'strain_upper_gap':2-b}.items()}
x,y,bb,ss=S.symbols('x y b s',positive=True);K=2*y*(3*x*x-y*y)/(S.pi*(x*x+y*y)**3);P=x/(S.pi*(x*x+y*y))
identities={'kernel':S.simplify(S.diff(P,x,y)-K),'kernel_homogeneity':S.simplify(x*S.diff(K,x)+y*S.diff(K,y)+3*K),'folded_jacobian_power':S.simplify((bb-S.Rational(1,2))+1-(bb+S.Rational(1,2))),'gamma_power':S.simplify(2*(bb+S.Rational(1,2))-1-2*bb),'beta_eta_power':S.simplify(4-(2*bb+1)-(3-2*bb)),'beta_first_argument':S.simplify((3-2*bb+1)/2-(2-bb)),'scaling_power':S.simplify((bb-1)+2-3-(bb-2)),'logarithmic_scaling':S.simplify((S.Rational(1,2)-bb)+(bb-1)+S.Rational(1,2))}
assert all(t==0 for t in identities.values())
def Q(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def ep(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def en(x):return {'lower_exact':str(ep(x.lower())),'upper_exact':str(ep(x.upper()))}
def win(x):
 l,r=ep(x.lower()),ep(x.upper());den=10**12;lo=F(l.numerator*den//l.denominator,den);hi=F(r.numerator*den//r.denominator+1,den)
 if lo==l:lo-=F(1,den)
 assert lo<l<=r<hi
 return [str(lo),str(hi)]
pi=arb.pi();beta=Q(u).gamma()*Q(v).gamma()/Q(s).gamma();C2=Q(2*b+1).gamma()*beta/(pi*Q(2)**int(2*b+2));C=C2.sqrt();c=C/3
assert C2>0 and C<F(1,3).numerator/F(1,3).denominator # Only a loose diagnostic; strict rational checks below.
values={'pi':pi,'beta':beta,'C2':C2,'C':C,'c_bound':c}
for n in ['C','c_bound']:assert values[n]<Q(F(1,3) if n=='C' else F(1,9))
out={'start_utc':start,'utc':p.now(),'status':'PASS_ARB512_STRAIN_DUAL_CONSTANT_AND_SYMBOLIC_IDENTITIES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'parent_files':pins,'parent_pin_count':len(pins),'actual':actual,'symbolic_identities':{n:str(v) for n,v in identities.items()},'arb512':{n:en(v) for n,v in values.items()},'strict_windows':{n:win(v) for n,v in values.items()},'scope':'Quantitative nonsharp full-Y dual upper bound. Qualitative threshold and counterexamples are analytic proofs, not inferred from arithmetic.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['start_utc','utc','status','parent_pin_count','actual','symbolic_identities','strict_windows']}))
