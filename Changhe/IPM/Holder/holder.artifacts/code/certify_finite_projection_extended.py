"""Arb rectangle enclosure of an admissible finite-alpha D witness.
All singular and infinite tails use explicit analytic bounds from the proof.
Each invocation is a bounded radial-row chunk. No chunk alone is a certificate.
"""
from pathlib import Path
from datetime import datetime, timezone
from flint import arb, acb, ctx
from certify_reflection_chunk import positive_power
import argparse, json, hashlib, time
ctx.prec=160
PI=arb.pi(); ROOT=Path(__file__).resolve().parents[1]

def nonnegative(v):
    return arb.max(v,arb(0))

def signed_amplitude(X,Y,alpha,a,rho):
    dx=X-arb(1)/2; dy=Y-a
    seg=abs(acb(dx,nonnegative(dy)))
    projection=dx/2+arb(3).sqrt()*dy/2
    line=abs(arb(3).sqrt()*dx/2-dy/2)
    endpoint=abs(acb(dx,dy))
    if projection>0: ray=line
    elif projection<0: ray=endpoint
    else: ray=line.union(endpoint)
    dist=arb.min(seg,ray)
    v=abs(acb(dist,Y))
    assert v>0
    pi=nonnegative(2*dist*Y/v)
    P=positive_power(pi,alpha)
    H=positive_power(2*X,alpha)
    B=positive_power(arb.min(v,rho),alpha)
    M=nonnegative(arb.min(arb.min(P,H),(P+H+B-1)/2))
    side=dx-nonnegative(dy)/arb(3).sqrt()
    if side>0:return M
    if side<0:return -M
    return M.union(-M)

def endpoint_terms(alpha,a):
    rho=arb.min(arb(1),a/7);delta=arb.min(rho/4,arb(1)/4);R=arb(4096);L=R-arb(1)/2
    A=((alpha+2)/2).gamma()/(2*PI.sqrt()*((alpha+3)/2).gamma())
    local=2*A*delta**alpha/alpha
    loss=2*alpha*delta/(PI*(1-2*delta))+2*(1+delta)*delta**(alpha+3)/((1-delta)**4*(alpha+3))
    tail=2**alpha*L**(alpha-1)/((1-alpha)*(1-1/(4*L*L))**2)
    return rho,delta,R,local,loss,tail

def main():
    p=argparse.ArgumentParser();p.add_argument('--alpha',default='1/10');p.add_argument('--shape',default='1')
    p.add_argument('--radial',type=int,default=512);p.add_argument('--angular',type=int,default=512)
    p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True);p.add_argument('--out',required=True)
    args=p.parse_args();alpha=arb(args.alpha);a=arb(args.shape)
    assert 0<alpha<=arb(1)/2 and 0<a
    nr=args.radial;nt=args.angular;assert 0<=args.start<args.stop<=3*nr and nt>0
    rho,delta,R,local,loss,tail=endpoint_terms(alpha,a)
    bounds=[delta,arb(1)/2,arb(2),R];logs=[b.log() for b in bounds]
    total=arb(0);start=time.monotonic();cells=0
    for row in range(args.start,args.stop):
        patch,k=divmod(row,nr);ul,ur=logs[patch:patch+2];du=(ur-ul)/nr
        u=(ul+k*du).union(ul+(k+1)*du);r=u.exp()
        if patch==0: limit=PI
        else:
            angle_lo=(-arb(1)/(2*arb(r.upper()))).acos()
            angle_hi=PI if patch==1 and k==0 else (-arb(1)/(2*arb(r.lower()))).acos()
            limit=angle_lo.union(angle_hi)
        assert limit.is_finite(), (row, str(r), str(limit))
        for j in range(nt):
            t=(arb(j)/nt).union(arb(j+1)/nt);theta=limit*t
            X=nonnegative(arb(1)/2+r*theta.cos());Y=nonnegative(r*theta.sin())
            z=acb(X,Y)
            kernel=-(z/(PI*(z*z-arb(1)/4)**2)).imag
            amp=signed_amplitude(X,Y,alpha,a,rho)
            value=2*kernel*amp*r*r*limit
            assert value.is_finite()
            total+=value*du/nt;cells+=1
        if row%32==0:print(row,args.stop,str(total),round(time.monotonic()-start,2),flush=True)
    sources=[Path(__file__),ROOT/'code/certify_reflection_chunk.py',ROOT/'07_diagonal_identity_term/finite_projection_witness/PROOF.md',ROOT/'07_diagonal_identity_term/finite_projection_extended/PROOF.md']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=args.alpha,shape=args.shape,precision_bits=ctx.prec,
             radial_cells_per_patch=nr,angular_cells=nt,row_start=args.start,row_stop=args.stop,cells=cells,
             regular_interval=total.str(45,more=True),local_leading=local.str(45,more=True),local_loss=loss.str(45,more=True),
             tail_error=tail.str(45,more=True),normalizer='Requires separately certified K_alpha',
             elapsed_seconds=time.monotonic()-start,source_hashes={str(s.relative_to(ROOT)):hashlib.sha256(s.read_bytes()).hexdigest() for s in sources},
             status='Partial regular integral. Requires a merge checking exact row coverage before a D lower bound follows.')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n');print(out['regular_interval'],flush=True)
if __name__=='__main__':main()
