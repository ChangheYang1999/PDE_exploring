"""Exact supporting checks for the general symbol inverse and finite-trace cascade.

Own implementation, no producer imports. The analytic proof precedes this code.
The piecewise modal sources used below test Green formulas only; they are not
claimed to be smooth IPM density profiles. One short single-threaded CPU gate.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time

started=time.monotonic()
counts={}
def check(kind, condition):
    assert condition, kind
    counts[kind]=counts.get(kind,0)+1

def deriv(q): return [(j+1)*q[j+1] for j in range(len(q)-1)] or [F(0)]
def scale(q,a): return [a*x for x in q]
def add(*qs):
    out=[F(0)]*max(map(len,qs))
    for q in qs:
        for i,x in enumerate(q):out[i]+=x
    return out

def euler(q,b,m):
    return scale(add(deriv(deriv(q)),scale(deriv(q),2*(b+1)),scale(q,(b+1)**2-m*m)),-1)

def cadd(x,y):return (x[0]+y[0],x[1]+y[1])
def cscale(x,s):return (x[0]*s,x[1]*s)
def cinv(a,b):return (a/(a*a+b*b),-b/(a*a+b*b))

bvals=[F(1,3),F(4,5),F(-1,2),F(-5,2),F(-7,2),F(-13,2),F(-29,3)]
for m in range(2,34,2):
    for b in bvals:
        la=m+b+1;mu=m-b-1
        check('tail_kernel_positive',mu>0)
        for d in range(7):
            q=[F(0)]*(d+1)
            for j in range(d+1):
                q[d-j]=F(comb(d,j)*factorial(j),2*m)*(F((-1)**j,1)/la**(j+1)+1/mu**(j+1))
            expected=[F(0)]*d+[F(1)]
            check('polynomial_log_resolvent',euler(q,b,m)==expected)
        for w in [F(0),F(1,3),F(7,2),F(-5,4)]:
            q=cscale(cadd(cinv(la,w),cinv(mu,-w)),F(1,2*m))
            pred=cinv(F(m*m)-(b+1)**2+w*w,-2*(b+1)*w)
            check('oscillatory_log_resolvent',q==pred)
            if la<0:
                low=cscale(cadd(cscale(cinv(-la,-w),-1),cinv(mu,-w)),F(1,2*m))
                check('subtracted_moment_sign',low==pred)
        # Piecewise source g_m=r^(b-1) on r>=1, zero below1.
        # Noncritical Green stream: Q*r^(b+1)+h*r^(-m).
        Q=1/(m*m-(b+1)**2);h=-1/(2*m*la)
        check('green_value_at_cutoff',Q+h==F(1,2*m)/mu)
        check('green_first_derivative_at_cutoff',(b+1)*Q-m*h==F(1,2)/mu)
        if la<0:
            J=-1/la
            check('converged_source_moment',h==J/(2*m))
        for power in range(6):
            # r=2^(6power) makes all selected half/third powers exact.
            zexp=-F(6*power)*la
            if zexp.denominator!=1: continue
            z=F(2)**int(zexp)
            scaled_rem=Q if la<0 else Q+h*z
            bound=F(1,2*m)*(1/abs(la)+1/mu)
            check('mode_uniform_remainder_bound',abs(scaled_rem)<=bound)
    for d in range(7):
        b=F(-m-1);q=[F(0)]*(d+2)
        q[d+1]=F(1,2*m*(d+1))
        for j in range(d+1):q[d-j]+=F(comb(d,j)*factorial(j),(2*m)**(j+2))
        expected=[F(0)]*d+[F(1),F(0)]
        check('resonant_log_green',euler(q,b,m)==expected)

# Exact coefficient bounds for a genuinely infinite angular modal-source family.
# a_m=2^(-m); sum is not truncated in the proof. The finite prefixes below and
# geometric derivative-tail inequality test the explicit majorant arithmetic.
for b in [F(1,3),F(-7,2),F(-13,2),F(-21,2)]:
    for radial_power in range(1,6):
        sums=[F(0)]*7;bounds=[F(0)]*7
        for m in range(2,50,2):
            a=F(1,2**m);la=m+b+1;mu=m-b-1
            Q=a/(m*m-(b+1)**2);h=-a/(2*m*la)
            exponent=-F(6*radial_power)*la
            check('exact_test_radius',exponent.denominator==1)
            scaled=Q if la<0 else Q+h*(F(2)**int(exponent))
            bound=a/F(2*m)*(1/abs(la)+1/mu)
            for d in range(7):
                sums[d]+=m**d*abs(scaled);bounds[d]+=m**d*bound
        for d in range(7):check('infinite_family_prefix_majorant',sums[d]<=bounds[d])
    for m in range(50,150,2):
        check('large_mode_denominator',m*m-(b+1)**2>=F(3,4)*m*m)
        check('large_mode_inner_rate',m+b+1>=F(m,2))
        for d in range(2,7):
            ratio=F(m+2,m)**(d-2)/4
            check('geometric_derivative_tail',ratio<=F(1,2))

# Smooth threshold counterexample f=y/(1+r^2)^2: with z=r^2, -Lap psi_2
# equals F''-F'/z, where F=log(1+z)+(1+z)^(-1)-1.
for z in [F(1,1000),F(1,9),F(1),F(7),F(53,2),F(1000)]:
    fprime=z/(1+z)**2;fsecond=(1-z)/(1+z)**3
    check('smooth_resonance_source',fsecond-fprime/z==-2*z/(1+z)**3)
for j in range(1,31):
    coeff=F((-1)**(j+1),j)+(-1)**j
    check('smooth_resonance_origin_series',coeff==(-1)**j*(1-F(1,j)))
check('smooth_resonance_origin_cancellation',F(1)-1==0)

# Polar product, collision grading, paired sign and recurrence.
for n in [1,3,5,9]:
    for p in [F(1,5),F(1,3),F(2,5),F(2,3),F(9,10)]:
        de=1-p;D=1/p-1;C=F(n+1)/de
        A=[F(1)]
        for k in range(1,13):
            terms=[]
            for i in range(k):
                j=k-1-i;u=i+1;v=j+1
                ni=u*(n+1)-1;si=1-u*de;nj=v*(n+1)-1;sj=1-v*de
                polar=-( (si+1)*nj-(ni+1)*sj )/(4*(ni+si+2))
                cij=F(1,4)*(1-F(2*v*(n+1))/(u*(n+p)+2))
                check('polar_transport_coefficient',polar==cij)
                pair=cij+F(1,4)*(1-F(2*u*(n+1))/(v*(n+p)+2))
                check('strict_paired_sign',pair<0)
                terms.append(cij*A[i]*A[j])
            A.append(sum(terms)/(k*D))
            check('nonzero_boundary_amplitude',((-1)**k)*A[k]>0)
            nk=(k+1)*(n+1)-1;sk=p-k*de
            check('boundary_nonresonance',(nk-sk)>0 and nk+sk+2>0)
            for m in range(2,18,2):
                # Any harmonic route with output cost k delta has strict grade.
                t2=k*de-m-2
                if t2>=0:
                    check('coincident_harmonic_grade',m+n+C*t2<nk)
        for N in range(n,n+25,2):
            k=(N+1)//(n+1)
            check('first_omitted_boundary_mode',(k+1)*(n+1)-1>N and (k==0 or k*(n+1)-1<=N))

out=Path('research/finite_far_field_cascade/verification')
report={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-started,'proof_sha256':hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'counts':counts,'total_exact_checks':sum(counts.values()),'verdict':'PASS','scope':'Exact supporting identities and majorant arithmetic. Piecewise modal manufactured sources are not smooth IPM profiles. Infinite-series estimates and main theorem are proved analytically, not inferred from finite tests.'}
(out/'EXACT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
