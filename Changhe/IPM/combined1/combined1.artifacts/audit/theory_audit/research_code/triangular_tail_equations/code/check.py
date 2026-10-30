"""Exact homogeneous-potential endpoint differentiation and triangular tail checks."""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import hashlib, json, time, sys
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
EXPECTED='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'

def put(out,n,value):
    if n == 0:return
    if n < 0:n,value=-n,-value
    out[n]=out.get(n,Q(0))+value
    if not out[n]:del out[n]

def emit(out):return {str(n):str(v) for n,v in sorted(out.items())}

def run():
    start=time.perf_counter(); source=BASE/'data/canonical007.json'
    assert sha(source)==EXPECTED
    data=json.loads(source.read_text());c=Q(data['cl']);delta=1-1/c;gamma=1/c
    assert Q(1,2)<gamma<Q(3,5)
    N=(2/delta).floor();assert N==4
    amps=defaultdict(lambda:Q(0))
    for (j,m,k),v in zip(data['order'],data['coefficients']):amps[int(j),2*int(m)]+=Q(v)
    rho={j:{} for j in range(N)};psi={j:{} for j in range(N)}
    exponent={j:1-(j+1)*delta for j in range(N)}
    for (j,n),A in amps.items():
        if j>=N or not A:continue
        d=exponent[j]+3
        put(rho[j],n+1,-A*(d*d-n*n)*(d-2-n)/2)
        put(rho[j],n-1,+A*(d*d-n*n)*(d-2+n)/2)
        put(psi[j],n+2,+A*(d-n)*(d-n-2)/4)
        put(psi[j],n-2,-A*(d+n)*(d+n-2)/4)
    prior=json.loads((BASE/'data/prior_branch_result.json').read_text())
    check_prior={j:rho[j].get(1,Q(0))==Q(prior['branches'][j]['first_sine_exact']) for j in range(N)}
    assert all(check_prior.values())
    poisson_checks={}
    for j in range(N):
        e=exponent[j];rhs={}
        for n,A in rho[j].items():
            assert n%2==1
            put(rhs,n+1,(n-e)*A/2)
            put(rhs,n-1,-(n+e)*A/2)
        lhs={n:((e+1)**2-n*n)*A for n,A in psi[j].items()}
        assert all(n%2==0 for n in lhs)
        residual={n:lhs.get(n,Q(0))-rhs.get(n,Q(0)) for n in set(lhs)|set(rhs)}
        poisson_checks[j]=all(v==0 for v in residual.values())
    assert all(poisson_checks.values()),poisson_checks
    checks=[];predicted={}
    for j in range(1,N):
        nonlinear={}
        for l in range(j):
            m=j-1-l
            for frequency_u,A in psi[l].items():
                for frequency_r,B in rho[m].items():
                    # cos(f_u theta) sin(f_r theta), first term in (2).
                    a=-exponent[m]*frequency_u*A*B/2
                    put(nonlinear,frequency_r+frequency_u,a)
                    put(nonlinear,frequency_r-frequency_u,a)
                    # sin(f_u theta) cos(f_r theta), second term in (2).
                    b=(exponent[l]+1)*frequency_r*A*B/2
                    put(nonlinear,frequency_u+frequency_r,b)
                    put(nonlinear,frequency_u-frequency_r,b)
        predicted[j]={n:v/(j*(c-1)) for n,v in nonlinear.items()}
        residual={n:nonlinear.get(n,Q(0))-j*(c-1)*rho[j].get(n,Q(0)) for n in set(nonlinear)|set(rho[j])}
        nonzero={n:v for n,v in residual.items() if v}
        checks.append({'j':j,'angular_coefficients_checked':len(residual),'nonzero_residual_coefficients':emit(nonzero),'all_zero':not nonzero,'density_nonzero_modes':len(rho[j]),'maximum_density_frequency':max(rho[j])})
    assert all(row['all_zero'] for row in checks),checks
    exact={'c':str(c),'gamma':str(gamma),'N':int(N),'exponents':{str(j):str(v) for j,v in exponent.items()},'density_profiles':{str(j):emit(v) for j,v in rho.items()},'stream_profiles':{str(j):emit(v) for j,v in psi.items()},'predicted_density_profiles':{str(j):emit(v) for j,v in predicted.items()}}
    exact_path=BASE/'verification/exact_profiles.json';assert not exact_path.exists()
    exact_path.write_text(json.dumps(exact,indent=2)+'\n')
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-N1-007','method':'homogeneous potential endpoint differentiation and exact trigonometric products','c':str(c),'gamma':str(gamma),'N':int(N),'poisson_checks':poisson_checks,'prior_first_harmonic_checks':check_prior,'triangular_checks':checks,'source_sha256':sha(source),'prior_sha256':sha(BASE/'data/prior_branch_result.json'),'code_sha256':sha(__file__),'proof_sha256':sha(BASE/'PROOF.md'),'exact_profiles_sha256':sha(exact_path),'elapsed_seconds':time.perf_counter()-start,'verdict':'LOCAL exact checks pass; independent Opus and numerical-lane reviews OPEN'}
    dest=BASE/'verification/result.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
