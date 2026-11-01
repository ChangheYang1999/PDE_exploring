"""Independent Cartesian and logarithmic checks of the exact top-mode formula."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import sys
import time
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from laurent_log_audit import Q, Poly, L, parse


def scalar_h(delta, B, N):
    d = delta/(1-delta)
    eta = B-delta
    h = [Q(0), Q(1)]
    for n in range(2, N+1):
        total = Q(0)
        for i in range(1, n):
            j = n-i
            kernel = B*(j/(eta*i+2)+i/(eta*j+2))-1
            assert kernel>0
            total += kernel*h[i]*h[j]
        h.append(total/(4*(n-1)*d))
        assert h[-1]>0
    return h


def cartesian_case(delta, initial, N):
    start=time.monotonic()
    c=1/(1-delta)
    B=max(initial)+1
    alpha=Q(initial[B-1])
    h=scalar_h(delta,B,N)
    F,G,XF,YF,XG,YG={},{},{},{},{},{}
    rows=[]
    for n in range(1,N+1):
        p=1-n*delta
        non=L(p,0,[])
        for i in range(1,n):
            j=n-i
            non=non+XG[i]*YF[j]-YG[i]*XF[j]
        F[n]=parse(p,{str(k):[v] for k,v in initial.items()}) if n==1 else non.scale(1/((n-1)*(c-1)))
        assert (F[n].scale(c*p-1)+non).zero() if n>1 else True
        actual=2*F[n].a[0][F[n].M+B*n-1]
        predicted=(-1)**(n-1)*alpha**n*h[n]
        assert actual==predicted, ('density top',n)
        XF[n],YF[n]=F[n].X(),F[n].Y()
        rhs,P=XF[n],p+1
        bb=[]
        for idx,r in enumerate(rhs.a[0].coeffs() if rhs.a else []):
            k=idx-rhs.M
            divisor=k*k-P*P
            assert divisor or not r,('resonance',n,k)
            bb.append(r/divisor if divisor else Q(0))
        G[n]=L(P,rhs.M,[Poly(bb)])
        XG[n],YG[n]=G[n].X(),G[n].Y()
        assert (XG[n].X().scale(-1)+YG[n].Y()-rhs).zero()
        stream_top=2*G[n].a[0][G[n].M+B*n]
        assert stream_top==-actual/(2*((B-delta)*n+2))
        rows.append(dict(n=n,frequency=B*n-1,density_top_exact=str(actual),
                         scalar_h_exact=str(h[n]),cartesian_match=True,poisson_match=True))
    return dict(delta=str(delta),initial={str(k):str(v) for k,v in initial.items()},
                N=N,rows=rows,actual_elapsed_s=time.monotonic()-start)


def main():
    start=time.monotonic()
    target=Path('research/38_extreme_fourier_mode/verification')
    cases=[(Q(4,9),{1:'1'},8),(Q(2,5),{3:'1'},8),
           (Q(3,7),{1:'2/3',3:'-1/7',5:'-3/5'},8),
           (Q(3,7),{5:'-3/5'},8),(Q(1,3),{1:'-2',3:'1/3',7:'1/9'},9)]
    rows=[]
    for delta,initial,N in cases:
        row=cartesian_case(delta,initial,N)
        rows.append(row)
        print(json.dumps(dict(delta=str(delta),L=max(initial),N=N,exact_match=True,
                              elapsed_s=row['actual_elapsed_s'])),flush=True)
    ref=Path('research/21_logarithmic_data_audit/sources/lead_exact_log_data.json')
    raw=ref.read_bytes()
    data=json.loads(raw)
    h=scalar_h(Q(4,9),2,73)
    logrows=[]
    for n in range(1,74):
        ftop=[Q(v) for v in data['density'][str(n)][str(2*n-1)]]
        gtop=[Q(v) for v in data['stream'][str(n)][str(2*n)]]
        expected=(-1)**(n-1)*h[n]
        assert ftop[0]==expected and not any(ftop[1:]),('log f top',n)
        assert gtop[0]==-expected/(2*((2-Q(4,9))*n+2)) and not any(gtop[1:]),('log g top',n)
        logrows.append(dict(n=n,constant_density_match=True,constant_stream_match=True,
                            higher_log_coefficients_exact_zero=True))
    ctx.prec=512
    profile_path=Path('research/02_candidate007/data/leading_exact.json')
    profile=json.loads(profile_path.read_text())
    constants=[]
    for name,delta,B,alpha in [('sin1_sqrt5',1/arb(5).sqrt(),2,arb(1)),
                              ('sin1_4_9',arb(4)/9,2,arb(1)),
                              ('sin3_sqrt5',1/arb(5).sqrt(),4,arb(1)),
                              ('sin5_sqrt5',1/arb(5).sqrt(),6,arb(1)),
                              ('candidate007_sqrt5',1/arb(5).sqrt(),20,arb(Q(profile['density']['19']))),
                              ('candidate007_stored',arb(Q(profile['delta'])),20,arb(Q(profile['density']['19'])))]:
        d=delta/(1-delta)
        aa=2/(B-delta)
        bb=2*(B-1)/(B-delta)
        beta=aa.gamma()*bb.gamma()/(aa+bb).gamma()
        assert beta.overlaps(arb(1).beta_lower(aa,bb))
        radius=4*d*(aa*beta)**(1/aa)/abs(alpha)
        growth=1/radius
        rphysical=growth**(1/delta)
        constants.append(dict(name=name,delta_ball=str(delta),B=B,alpha_ball=str(alpha),
                              beta_a_ball=str(aa),beta_b_ball=str(bb),beta_integral_ball=str(beta),
                              beta_gamma_vs_incomplete_overlap=True,top_z_radius_ball=str(radius),
                              top_growth_limsup_ball=str(growth),physical_radius_lower_bound_ball=str(rphysical),
                              real_boundary_exponent_ball=str(1/bb)))
        print(name,'Rtop=',radius.str(18),'growth=',growth.str(18),flush=True)
    output=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
                cartesian_cases=rows,logarithmic_exact_reference=str(ref),
                logarithmic_exact_reference_sha256=sha256(raw).hexdigest(),logarithmic_rows=logrows,
                arithmetic='exact rational Cartesian and scalar coefficients; Arb 512-bit beta and gamma values',
                constants=constants,profile_input=str(profile_path),profile_sha256=sha256(profile_path.read_bytes()).hexdigest(),
                actual_elapsed_s=time.monotonic()-start)
    (target/'checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print('Complete',output['actual_elapsed_s'],flush=True)


if __name__=='__main__':main()
