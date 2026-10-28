"""Independent Fourier differentiation and residual lower bound for tail repair."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial
from datetime import datetime,timezone
import hashlib,json,sys
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.set_int_max_str_digits(0)
p=HERE/'state131_splice.json';d=json.loads(p.read_text())
x=json.loads((BASE/'source_audit/state131_exact.json').read_text())
t=json.loads((BASE/'05_tails/verification/state131_formal_tail.json').read_text())
f=json.loads((BASE/'05_tails/verification/state131_tail.json').read_text())
assert d['canonical_sha256']==x['canonical_serialization_sha256']==t['input_sha256']==f['canonical_serialization_sha256']

def clean(a):return {k:v for k,v in a.items() if v}
def cosine(C):
    out={}
    for m,v in C.items():
        if m:out[m]=out.get(m,Q(0))+v/2;out[-m]=out.get(-m,Q(0))+v/2
        else:out[0]=out.get(0,Q(0))+v
    return out

def deriv(F,s,axis):
    # Coefficients represented after extracting a global i for each y derivative.
    out={}
    for m,v in F.items():
        out[m-1]=out.get(m-1,Q(0))+v*(s+m)/2
        out[m+1]=out.get(m+1,Q(0))+v*(s-m)/2*(1 if axis=='x' else -1)
    return clean(out)

def diffs(F,s,axes):
    for axis in axes:F=deriv(F,s,axis);s-=1
    return F

def sin_imag(F):
    return clean({m: -v/2 for m,v in F.items()}|{-m:v/2 for m,v in F.items()})

checks={}
for n,v in d['homogeneous_potential_orders'].items():
    C={int(k):Q(a) for k,a in v['cosine_coefficients'].items()};s=Q(v['exponent']);H=cosine(C)
    A=diffs(H,s,'xxy');B=diffs(H,s,'yyy')
    rho=clean({k:B.get(k,Q(0))-A.get(k,Q(0)) for k in A.keys()|B.keys()})
    F={int(k):Q(a) for k,a in t['stationary_density_orders'][n]['coefficients'].items()}
    P={int(k):Q(a) for k,a in t['stationary_stream_orders'][n].items()}
    assert rho==sin_imag(F)
    assert diffs(H,s,'xy')==sin_imag(P)
    checks[n]='all Fourier coefficients agree exactly after independent Cartesian differentiation'

# Independent coarse verification of the exact bound tables.
def falling(v,n):
    z=Q(1)
    for k in range(n):z*=v-k
    return z

def one(k,b,n):
    total=Q(0)
    for j in range(n+1):
        if j>2*k:continue
        q=n-j
        radial=Q(0)
        for pairs in range(q//2+1):
            singles=q-2*pairs
            partitions=Q(factorial(q),factorial(singles)*factorial(pairs)*2**pairs)
            radial+=partitions*2**(singles+pairs)*abs(falling(b,singles+pairs))
        total+=comb(n,j)*falling(Q(2*k),j)*radial
    return total

c=Q(d['c']);gamma=1/c;delta=1-gamma
orig={j:Q(0) for j in range(11)};diff={j:Q(0) for j in range(11)};rem={j:Q(0) for j in range(5)}
primary={j:{} for j in range(4)}
for (j,m,k),a in zip(x['canonical_order'],x['canonical_coefficients']):
    v=Q(a);b=(3+gamma-j*delta)/2-k
    primary[j][2*m]=primary[j].get(2*m,Q(0))+v
    for n in range(11):
        orig[n]+=4*abs(v)*one(k,b,n)
        diff[n]+=(2*abs(v*b)*one(k,b-1,n) if j==0 else 4*abs(v)*one(k,b,n))
    for n in rem:rem[n]+=2*abs(v*b)*one(k,b-1,n)
for k,v in d['homogeneous_potential_orders'].items():
    if k=='1':continue
    s=Q(v['exponent'])
    for m,a in v['cosine_coefficients'].items():
        v0=abs(Q(a));m=int(m)
        for j in range(11):
            bound=v0
            for ell in range(j):bound*=abs(s-ell)+m+ell
            diff[j]+=bound
assert orig=={int(k):Q(v) for k,v in d['original_potential_component_symbol_bounds'].items()}
assert diff=={int(k):Q(v) for k,v in d['difference_potential_component_symbol_bounds'].items()}
cut={0:Q(1)}
for n in range(1,11):
    cut[n]=Q(0)
    for b in range(n//2+1):
        a=n-2*b
        partitions=Q(factorial(n),factorial(a)*factorial(b)*2**b)
        cut[n]+=partitions*Q(4,3)**a*Q(2,3)**b*factorial(a+b)*4096**(a+b)
assert cut=={int(k):Q(v) for k,v in d['cutoff_component_derivative_bounds'].items()}
B={n:sum((comb(n,j)*2**j*cut[j]*diff[n-j] for j in range(n+1)),Q(0)) for n in range(11)}
assert B=={int(k):Q(v) for k,v in d['cutoff_difference_component_symbol_bounds'].items()}
K={n:2**(n+3)*(orig[n+3]+B[n+3]) for n in range(8)}
assert K=={int(k):Q(v) for k,v in d['combined_density_velocity_symbol_bounds'].items()}
assert max(K.values())<2**206

# Exact bound on F(rho_original)-r^p2 E1, for r>=1.
def hom(C,s,n):
    out=Q(0)
    for m,a in C.items():
        v=abs(a)
        for j in range(n):v*=abs(s-j)+m+j
        out+=v
    return out
rho=[];grad=[];u=[];pp=[]
for j in range(4):
    p0=gamma-j*delta;pp.append(p0)
    H3=hom(primary[j],p0+3,3);H4=hom(primary[j],p0+3,4)
    rho.append(2*H3);grad.append(4*H4);u.append(2*H3)
er=2*rem[3];ed=4*rem[4];ev=2*rem[3]
CF=sum((abs(c*pp[j]-1)*rho[j] for j in (2,3)),Q(0))+c*ed+er
CF+=sum((u[i]*grad[j] for i in range(4) for j in range(4) if i+j>=1),Q(0))
CF+=ev*sum(grad)+sum(u)*ed+ev*ed
cpow=0
while Q(2)**cpow<CF:cpow+=1
assert delta>Q(2,5)
assert Q(cpow+2)-Q(2,5)*(d['R_power']-1)<-4
E={int(k):Q(v) for k,v in f['E_coefficients']['1'].items()}
assert 3*sum((v*v for v in E.values()),Q(0))>Q(1,64) # pi>3 => full angular norm>1/8
# Therefore full angular residual norm >=r^p2/16 on [R/2,R], and Ns>=16 R.
assert Q(d['p2'])>0
# Coefficient matrix transfer with epsilon=1/1024 and R>=8.
eps=Q(1,1024);rmin=8;cmax=Q(37,20)
alpha2min=1-cmax/5-Q(4,5)*cmax/(1+4*rmin*rmin)
alpha3min=1-6*cmax/5-Q(4,5)*cmax/(1+4*rmin*rmin)
assert alpha2min-Q(19,5)*eps>Q(1,2)
assert alpha3min-Q(24,5)*eps>Q(-5,4)
assert 1-2*eps>Q(9,10) and 2*Q(9,5)+1-2*eps>Q(19,5)
assert eps<Q(1,20) and 3*eps<3 and 7*eps<28 and 24*eps<40
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','source_sha256':d['canonical_sha256'],
 'splice_file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'fourier_differentiation_checks':checks,
 'exact_symbol_tables_recomputed':True,'uniform_symbol_bound':'2^206','R':'2^1024',
 'coefficient_transfer_epsilon':str(eps),'exterior_M2_lower':str(alpha2min-Q(19,5)*eps),
 'exterior_M3_lower':str(alpha3min-Q(24,5)*eps),
 'original_residual_remainder_constant':str(CF),'original_residual_remainder_power_two_exponent':cpow,
 'original_residual_remainder_statement':'|F(rho0)-r^p2 E1(theta)|<=C_F r^p3 for r>=1',
 'leading_full_angular_residual_norm_lower':'1/8','repaired_residual_Ns_lower':'2^1028',
 'scope':'Explicit admissible reference and background coefficient transfer; residual lower bound proves this radius does not meet smallness.'}
(HERE/'splice_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='original_residual_remainder_constant'},indent=2))
