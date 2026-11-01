"""Exact low-order Cartesian check of the leading-stream cancellation family."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from laurent_log_audit import Q,parse
from maximal_log_cartesian_check import poisson


def amplitudes(A):
    assert len(A.a)<=1
    return {m:2*A.a[0][A.M+m] for m in range(1,A.M+1) if A.a[0][A.M+m]} if A.a else {}


def family(gamma,K):
    a=[Q(1)]
    for k in range(1,K+1):a.append(a[-1]*(2*k-1-gamma)/(2*k+1+gamma))
    return a


def main():
    start=time.monotonic();rows=[]
    source=json.loads(Path('research/02_candidate007/data/leading_exact.json').read_text());stored=Q(source['gamma'])
    for gamma in [Q(1,3),Q(1,2),Q(5,9),stored]:
        delta=1-gamma;c=1/gamma;d=c-1
        for K in [0,1,2,3,5,9,20]:
            N=2*K+2;a=family(gamma,K);f=parse(gamma,{2*k+1:[str(v)] for k,v in enumerate(a)})
            g=poisson(f);b=-a[-1]/(2*(N+gamma+1))
            assert amplitudes(g)=={N:b}
            f2=(g.X()*f.Y()-g.Y()*f.X()).scale(1/d)
            aa=amplitudes(f2);norm=sum(abs(v) for v in aa.values())
            exact=a[-1]*sum(v*max((gamma+1)*(2*k+1),gamma*N) for k,v in enumerate(a))/(2*d*(N+gamma+1))
            assert norm==exact
            bound=(1+gamma)**2*a[-1]/(4*gamma*d)
            assert norm<=bound
            assert aa[N+(2*K+1)]==b*a[-1]*(2*K+1-gamma)/(2*d)
            B=(3+gamma)/2;aplus=family(gamma,K+1)[-1]
            assert sum(a)==(B-1-(K+B)*aplus)/gamma
            assert sum(a)<=(1+gamma)/(2*gamma)
            row=dict(gamma=str(gamma),delta=str(delta),K=K,input=[str(v) for v in a],stream={str(N):str(b)},
              density2_norm_exact=str(norm),density2_norm_approx=float(norm),proved_bound_exact=str(bound),
              density2_over_last_input_approx=float(norm/a[-1]),limit_of_this_ratio=float((1+gamma)/(4*d)),
              lower_stream_modes_exact_zero=True,cartesian_density2_matches=True,sum_identity_matches=True)
            rows.append(row)
            if gamma==stored and K in [1,2,3,5,9]:
                Path(f'research/51_shear_approximants/data/stored_delta_K{K}.json').write_text(json.dumps([str(v) for v in a],indent=2)+'\n')
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),checks=rows,actual_elapsed_s=time.monotonic()-start,
      source_hashes={p:sha256(Path(p).read_bytes()).hexdigest() for p in ['code/shear_approximant_audit.py','code/laurent_log_audit.py','code/maximal_log_cartesian_check.py']})
    Path('research/51_shear_approximants/verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(passed=len(rows),elapsed_s=out['actual_elapsed_s'],stored_first3_input=rows[-5]['input'][:3],stored_f2_by_K={r['K']:r['density2_norm_approx'] for r in rows if r['gamma']==str(stored)})))

if __name__=='__main__':main()
