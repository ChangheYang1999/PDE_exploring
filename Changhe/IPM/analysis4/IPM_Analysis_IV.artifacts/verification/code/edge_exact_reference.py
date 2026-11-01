"""Independent exact Cartesian reference for edge-restricted log recursions."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, json, sys, time
sys.dont_write_bytecode=True
import logarithmic_verify as lv
from cartesian_verify import Q, qs, sin_field

def run(K,N):
    F={};G={};velocity={};rows=[]
    for n in range(1,N+1):
        p=1-Q(2*n)/3
        pairs=[(i,n-i) for i in range(1,n) if K is None or min(i,n-i)<=K]
        assert len(pairs)==len(set(pairs))
        source=lv.LogField(p,{})
        for i,j in pairs:
            ux,uy=velocity[i]
            source=source+ux*F[j].dx()+uy*F[j].dy()
        f=lv.LogField.pure(sin_field(p,{1:Q(1)})) if n==1 else lv.solve_dilation(source,Q(3),n)
        g,resonant=lv.poisson(f)
        potential,ux,uy=lv.reconstruct(f,g)
        assert (f.euler().scale(3)-f+source).zero()
        assert (g.laplace().scale(-1)-f.dx()).zero()
        F[n]=f;G[n]=g;velocity[n]=(ux,uy)
        row=dict(n=n,pairs=[list(v) for v in pairs],density=f.amplitudes('sine'),stream=g.amplitudes('sine'),
                 potential=potential.amplitudes('cosine'),density_log_degree=f.degree(),stream_log_degree=g.degree(),
                 potential_log_degree=potential.degree(),resonant_stream_modes=resonant,
                 modified_stationary_identity=True,poisson_identity=True,common_potential_identities=True)
        for field in ['density','stream']:
            cols=row[field]
            row[field+'_plain_norm']=qs(sum((abs(Q(x)) for modes in cols.values() for x in modes.values()),Q(0)))
            row[field+'_max_frequency']=max((int(m) for modes in cols.values() for m in modes),default=0)
        rows.append(row)
        print(json.dumps(dict(K=K,n=n,density_degree=f.degree(),stream_degree=g.degree())),flush=True)
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--N',type=int,default=18);a=ap.parse_args()
    start=time.monotonic();root=Path('research/102_edge_recurrence_reference')
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),delta='2/3',c='3',initial={'1':'1'},
                scope='Exact finite modified recurrences; no convergence or full nonlinear equivalence is asserted.',variants={})
    full=run(None,7)
    for K in [1,3]:
        rows=run(K,a.N)
        for n in range(1,2*K+2):
            for field in ['density','stream','potential']:assert rows[n-1][field]==full[n-1][field],(K,n,field)
        result['variants'][str(K)]=dict(orders=a.N,exact_full_prefix=2*K+1,rows=rows)
        result['actual_elapsed_s']=time.monotonic()-start
        (root/'verification/exact_reference.json').write_text(json.dumps(result,indent=2)+'\n')
    result['full_prefix']=full
    result['source_sha256']={}
    for name in ['edge_exact_reference.py','logarithmic_verify.py','cartesian_verify.py']:
        raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw)
        result['source_sha256'][name]=sha256(raw).hexdigest()
    result['complete']=True;result['actual_elapsed_s']=time.monotonic()-start
    (root/'verification/exact_reference.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(complete=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':main()
