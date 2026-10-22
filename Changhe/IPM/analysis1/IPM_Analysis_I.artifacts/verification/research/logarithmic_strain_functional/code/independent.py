from pathlib import Path
from fractions import Fraction as F
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq
from mpmath import iv
iv.dps=150
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_strain_functional';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();a=p.load(E/'check.json');p.rehash(a['parent_files']);assert p.sha(D/'PROOF.md')==a['proof_sha256']=='d4284c845df4c9717c4618916e7972b84e6a57cd1b5dd4da271062d375616115'
raw=R/'data_exact/modal_v2.json';assert p.sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');man,e=t.split('p');whole,frac=man[2:].split('.');return fmpq(sign*int(whole+frac,16))*fmpq(2)**(int(e)-4*len(frac))
k=hx(p.load(raw)['scalars_hex']['k']);b=fmpq(3,2);s=fmpq(153,50);u=fmpq(1,2);v=fmpq(64,25);v0=fmpq(14,25);fac=fmpq(28,53)*fmpq(78,103)
actual={n:str(x) for n,x in {'k':k,'b':b,'s':s,'u':u,'v':v,'v0':v0,'beta_reduction_factor':fac,'gamma_argument':4,'power_of_two':5,'residual_lower_gap':b-2*k,'strain_upper_gap':2-b}.items()};assert actual==a['actual'] and u+v==s and 0<u<1 and 0<v0<1 and 2*k<b<2
# Numerator from quotient-rule differentiation of -2xy/(x²+y²)².
num={(2,1):fmpq(-2)+8,(0,3):fmpq(-2)};assert num=={(2,1):fmpq(6),(0,3):fmpq(-2)}
def Q(t):t=fmpq(t);return iv.mpf(int(t.p))/int(t.q)
def ep(t):sign,man,ex,bc=t;return F((-1 if sign else 1)*man)*F(2)**ex
def en(t):l,r=map(ep,t._mpi_);return {'lower_exact':str(l),'upper_exact':str(r)}
N=110;series=[]
def half(pp,qq):
 assert 0<pp<1 and 0<qq<1
 coeff=fmpq(1);partial=fmpq(0)
 for n in range(N):
  partial+=coeff/((pp+n)*fmpq(2)**n)
  coeff*=fmpq(n+1)-qq;coeff/=n+1
 first=coeff/((pp+N)*fmpq(2)**N);tail=2*first;assert 0<first
 pref=iv.exp(-Q(pp)*iv.ln(2));out=pref*(Q(partial)+iv.mpf([0,1])*Q(tail))
 series.append({'p':str(pp),'q':str(qq),'N':N,'partial_exact':str(partial),'first_omitted_exact':str(first),'tail_bound_exact':str(tail),'outer_prefactor':en(pref),'value':en(out),'tail_proof':'Every consecutive positive term ratio equals (n+1-q)/(n+1) times (p+n)/(p+n+1) times 1/2, hence is strictly below1/2.'})
 return out
beta=Q(fac)*(half(u,v0)+half(v0,u))
atan=[]
def arctan_bounds(q):
 z=fmpq(1,q);out=fmpq(0)
 for n in range(N):out+=(-1)**n*z**(2*n+1)/(2*n+1)
 nxt=z**(2*N+1)/(2*N+1)
 lo,hi=(out,out+nxt) if N%2==0 else (out-nxt,out)
 assert lo<hi
 atan.append({'q':q,'N':N,'lower_exact':str(lo),'upper_exact':str(hi),'first_omitted_abs_exact':str(nxt),'scope':'Alternating arctan series with strictly decreasing positive magnitudes.'})
 return lo,hi
l1,h1=arctan_bounds(5);l2,h2=arctan_bounds(239);pl=16*l1-4*h2;ph=16*h1-4*l2;assert 0<pl<ph
# The branch in Machin's identity:4atan(1/5)-atan(1/239)>20/26-1/239>0,
# while it is <4/5<1<pi/2 because atan1>1/2 by its positive integral.
tan2=2*fmpq(1,5)/(1-fmpq(1,25));tan4=2*tan2/(1-tan2*tan2);tandiff=(tan4-fmpq(1,239))/(1+tan4/fmpq(239));assert tan2==fmpq(5,12) and tan4==fmpq(120,119) and tandiff==1 and fmpq(20,26)-fmpq(1,239)>0
pi=Q(pl)+iv.mpf([0,1])*Q(ph-pl);C2=Q(fmpq(3,16))*beta/pi;C=iv.sqrt(C2);c=C/3
values={n:en(t) for n,t in {'pi':pi,'beta':beta,'C2':C2,'C':C,'c_bound':c}.items()}
for n,z in values.items():
 lo,hi=map(F,a['strict_windows'][n]);il,iu=F(z['lower_exact']),F(z['upper_exact']);al,au=map(F,[a['arb512'][n]['lower_exact'],a['arb512'][n]['upper_exact']]);assert lo<il<=al<=au<=iu<hi
out={'start_utc':start,'utc':p.now(),'status':'PASS_FMPQ_BETA_HALF_SERIES_MACHIN_PI_IV150_STRAIN_CONSTANT','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(a['parent_files']),'exact_parameters_compared':len(actual),'kernel_numerator':{'x2y':'6','y3':'-2'},'beta_series':series,'arctangent_series':atan,'machin_pi_exact':{'lower_exact':str(pl),'upper_exact':str(ph)},'machin_tangents':{'tan2a':str(tan2),'tan4a':str(tan4),'tan_difference':str(tandiff)},'iv150':values,'all_primary_intervals_inside_independent':True,'strict_windows':a['strict_windows'],'scope':'Exact rational positive beta sums with proved infinite tails and independent rational alternating-series Machin pi, followed by directed iv operations. No gamma routine, built-in pi or primary-code import.'};p.write(E/'independent.json',out);print(json.dumps({n:out[n] for n in ['start_utc','utc','status','parent_pin_count','exact_parameters_compared','all_primary_intervals_inside_independent','strict_windows']}))
