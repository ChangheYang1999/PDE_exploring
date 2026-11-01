"""Exact full-recursion tests of the proposed high-harmonic degree bound."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time,argparse,pickle
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from laurent_log_audit import L,Q,Poly,parse
from maximal_log_cartesian_check import poisson
from general_fixed_deficit_audit import solve


def packed(fields):
    return {n:(str(v.q),v.M,[[str(a) for a in col.coeffs()] for col in v.a]) for n,v in fields.items()}

def unpacked(fields):
    return {n:L(Q(q),M,[Poly([Q(a) for a in col]) for col in rows]) for n,(q,M,rows) in fields.items()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('period',type=int);ap.add_argument('harmonic',type=int);ap.add_argument('N',type=int);ap.add_argument('--seconds',type=float,default=420);args=ap.parse_args()
    q,m,N=args.period,args.harmonic,args.N;assert q>=3 and q%2 and m>q and m%2
    start=time.monotonic();d=Q(2,q);c=1/(1-d);ks=(q*(m+1)+2)//4+1;A=ks+3
    root=Path('research/69_log_degree_gap');tag=f'Q{q}_M{m}';checkpoint=root/'verification'/(tag+'.pkl');output=root/'verification'/(tag+'.json')
    if checkpoint.exists():
        fp,gp,rows=pickle.loads(checkpoint.read_bytes());F,G=unpacked(fp),unpacked(gp)
    else:F,G,rows={},{},[]
    XF={n:f.X() for n,f in F.items()};YF={n:f.Y() for n,f in F.items()};XG={n:g.X() for n,g in G.items()};YG={n:g.Y() for n,g in G.items()}
    def bound(k):return max(0,k-(k+3+A-1)//A)
    def save():
        metadata=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),period=q,delta=str(d),harmonic=m,
            Kstar=ks,A=A,requested_N=N,completed_N=len(F),all_complete=len(F)>=N,all_degrees_satisfy_bound=True,rows=rows,actual_current_run_elapsed_s=time.monotonic()-start,
            sources={name:sha256(Path('code',name).read_bytes()).hexdigest() for name in ['log_degree_gap_audit.py','laurent_log_audit.py','maximal_log_cartesian_check.py','general_fixed_deficit_audit.py']})
        output.write_text(json.dumps(metadata,indent=2)+'\n');checkpoint.write_bytes(pickle.dumps((packed(F),packed(G),rows)))
    for n in range(len(F)+1,N+1):
        if n==1:F[n]=parse(1-d,{m:[Q(1)]})
        else:
            S=L(1-d*n,0,[])
            for i in range(1,n):S=S+XG[i]*YF[n-i]-YG[i]*XF[n-i]
            F[n]=solve(S,n,c);assert (F[n].scale((n-1)*(c-1))-F[n].dt().scale(c)-S).zero()
        G[n]=poisson(F[n]);XF[n],YF[n]=F[n].X(),F[n].Y();XG[n],YG[n]=G[n].X(),G[n].Y()
        fd,gd=len(F[n].a)-1,len(G[n].a)-1;fb,gb=bound((n-1)//q),bound(n//q)
        assert fd<=fb and gd<=gb,(q,m,n,fd,fb,gd,gb)
        row=dict(n=n,density_degree=fd,density_bound=fb,stream_degree=gd,stream_bound=gb,
            density_generic_bound=max(0,(n-1)//q-1),stream_generic_bound=max(0,n//q-1),stationary_exact_zero=True,poisson_exact_zero=True)
        rows.append(row)
        if n%q==0 or n==N:
            save();print(json.dumps(dict(n=n,fd=fd,gd=gd,elapsed_s=time.monotonic()-start)),flush=True)
        if time.monotonic()-start>args.seconds:save();break
    for name in ['log_degree_gap_audit.py','laurent_log_audit.py','maximal_log_cartesian_check.py','general_fixed_deficit_audit.py']:
        (root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
    print('Segment completed',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
