"""Exact Cartesian audit of fixed angular Galerkin projection, with no borrowed recurrence."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,time
from laurent_log_audit import L,Q,Poly,parse
from maximal_log_cartesian_check import poisson


def project(A,cap):
    return L(A.q,cap,[Poly([p[A.M+m] if A.M+m>=0 else Q(0) for m in range(-cap,cap+1)]) for p in A.a])


def band(A):
    return max((abs(i-A.M) for p in A.a for i,v in enumerate(p.coeffs()) if v),default=0)


def amplitudes(A):
    return {str(m):[str(2*p[A.M+m]) for p in A.a] for m in range(1,band(A)+1) if any(p[A.M+m] for p in A.a)}


def run():
    start=time.monotonic();rows=[];saved=[]
    out=Path('research/55_fixed_angular_projection/verification/checks.json')
    for delta in [Q(2,3),Q(4,9),Q(1,2)]:
      c=1/(1-delta)
      for cap in [1,3,5]:
        F,G,XF,YF,XG,YG={},{},{},{},{},{}
        first_discarded=None;resonances=[];N=24
        for n in range(1,N+1):
            p=1-n*delta
            non=L(p,0,[])
            if n==1:F[n]=parse(p,{1:['1']})
            else:
                for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
                rhs=project(non,cap);lam=(n-1)*(c-1);term=rhs.scale(1/lam);ans=term
                while term.a:
                    term=term.dt().scale(c/lam);ans=ans+term
                F[n]=project(ans,cap)
                assert (F[n].scale(-lam)+F[n].dt().scale(c)+rhs).zero()
                full_residual=F[n].scale(-lam)+F[n].dt().scale(c)+non
                assert project(full_residual,cap).zero()
                if first_discarded is None and not full_residual.zero():
                    first_discarded=dict(n=n,unprojected_stationary_residual=amplitudes(full_residual))
            G[n]=poisson(F[n]);XF[n],YF[n]=F[n].X(),F[n].Y();XG[n],YG[n]=G[n].X(),G[n].Y()
            assert band(F[n])<=cap and band(G[n])<=cap+1
            assert len(F[n].a)-1<=n-1 and len(G[n].a)-1<=n
            for A,odd in [(F[n],1),(G[n],0)]:
                for poly in A.a:
                    for idx,v in enumerate(poly.coeffs()):
                        m=idx-A.M
                        if v:
                            assert abs(m)%2==odd and poly[A.M-m]==-v
            P=2-n*delta
            if P<0 and P.q==1 and int(P)%2==0 and -int(P)<=cap+1:
                freq=-int(P)
                assert not G[n].a or G[n].a[0][G[n].M+freq]==0
                resonances.append(dict(n=n,mode=freq,density_degree=len(F[n].a)-1,stream_degree=len(G[n].a)-1,canonical_constant_zero=True))
            rows.append(dict(delta=str(delta),cap=cap,n=n,density_band=band(F[n]),stream_band=band(G[n]),density_degree=len(F[n].a)-1,stream_degree=len(G[n].a)-1,projected_stationarity=True,full_poisson=True))
        assert first_discarded is not None
        saved.append(dict(delta=str(delta),cap=cap,completed_order=N,first_discarded=first_discarded,resonances=resonances,last_density=amplitudes(F[N]),last_stream=amplitudes(G[N])))
        print(json.dumps(dict(delta=str(delta),cap=cap,N=N,resonances=resonances,elapsed_s=time.monotonic()-start)),flush=True)
    sources={}
    for name in ['laurent_log_audit.py','maximal_log_cartesian_check.py','fixed_projection_audit.py']:
        blob=Path('code',name).read_bytes();target=out.parent.parent/'sources'/f'{name}.txt';target.write_bytes(blob)
        sources[str(target)]=sha256(blob).hexdigest()
    out.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),method='Exact signed Laurent Cartesian derivatives; project only the stationary density forcing',checks=len(rows),sources=sources,results=rows,actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
    (out.parent/'coefficients.json').write_text(json.dumps(saved,indent=2)+'\n')

if __name__=='__main__':run()
