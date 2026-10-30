"""Separate full-polynomial check using direct residual derivatives for the pairing."""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import argparse, hashlib, importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as P, arb, arb_poly, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('t4_independent_polar',HELPER)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
T,W,Z=f.T,f.W,f.ZERO
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ap(p):return arb_poly([f.ar(v) for v in p])
def add(d,k,v):d[k]=d.get(k,Z)+v
@lru_cache(None)
def moment(b,j):
    b=Q(b)
    assert b>-1
    # Integral t W^(b+j) dt. This rational formula avoids gamma functions.
    return f.ar(1/((b+j+1)*(b+j+2)))
def integ(p,b):
    # Coefficients of p(1-W), kept rational until the final scalar sum.
    return sum((f.ar(v)*moment(str(b),j) for j,v in enumerate(p(W)) if v),arb(0))
def integ_ap(p,b):
    ww=arb_poly([arb(1),arb(-1)])
    return sum((v*moment(str(b),j) for j,v in enumerate(p(ww))),arb(0))
def sup_certificate(poly,a,target,nmode):
    polys=[nmode*poly,(1-4*T)*poly+2*T*W*poly.derivative()]
    vals=[(ap(p),ap(p.derivative())) for p in polys]
    pending=[(Q(0),Q(1))];accepted=0;depth=0
    while pending:
        lo,hi=pending.pop();mid=(lo+hi)/2;rad=(hi-lo)/2
        x=arb(f.ar(mid),f.ar(rad)*(1+arb(2)**-100))
        scale=f.ar(1-lo)**f.ar(2-a)
        caps=[scale*(abs(p(f.ar(mid)))+f.ar(rad)*abs(dp(x))) for p,dp in vals]
        if all(v<f.ar(target) for v in caps):
            accepted+=1
        else:
            assert hi-lo>Q(1,2**40),(lo,hi,caps,target)
            pending.extend([(lo,mid),(mid,hi)])
        depth=max(depth,len(pending))
        assert accepted+len(pending)<100000
    return {'method':'rational dyadic subdivision and interval mean-value polynomial bounds','H_upper_exact':str(target),'accepted_cells':accepted,'maximum_stack':depth}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',type=int,default=7);parser.add_argument('--candidate',default='C1-N1-007');parser.add_argument('--a',default='0');parser.add_argument('--bits',type=int,default=2048)
    args=parser.parse_args();ctx.prec=args.bits;start=time.monotonic();a=Q(args.a);nmode=args.mode
    assert nmode>0 and nmode%2==1
    peers=ROOT/'verification'/f'n{nmode}_a{str(a).replace("/","_")}.json'
    row=json.loads(peers.read_text())
    source=ROOT.parent/'projected_laplacian/data/candidate007_canonical.json'
    c,delta,rho,stream=f.fields(json.loads(source.read_text()))
    print('fields constructed',len(rho),len(stream),'seconds',time.monotonic()-start,flush=True)
    poly=sum((Q(v)*T**int(k) for k,v in row['probe_coefficients'].items()),Z)
    probe=(1-4*T)*poly+2*T*W*poly.derivative();A=(2*c+1)*poly+c*probe
    Ds={(j,n):f.td(S,(j+1)*delta/2,2) for (j,n),S in stream.items()}
    Dr={(j,n):f.td(R,(j+1)*delta/2,1) for (j,n),R in rho.items()}
    # Direct combined M modes, without a basis Gram matrix.
    modes={};add(modes,(0,nmode),A)
    for (j,n),S in stream.items():
        add(modes,(j+1,nmode+n),(nmode*Ds[j,n]*poly-n*S*probe)/2)
        m=nmode-n
        if m:add(modes,(j+1,abs(m)),(1 if m>0 else -1)*(-nmode*Ds[j,n]*poly-n*S*probe)/2)
    byn={}
    for (j,n),p in modes.items():byn.setdefault(n,[]).append((j,ap(p)))
    squares={}
    for entries in byn.values():
        for i,(j,p) in enumerate(entries):
            for k,q in entries[i:]:squares[j+k]=squares.get(j+k,arb_poly([]))+p*q*(1 if j==k else 2)
    normM2=arb.pi()/2*sum((integ_ap(p,1-a+j*delta/2) for j,p in squares.items()),arb(0))
    print('M done','seconds',time.monotonic()-start,flush=True)
    # Keep the exact sin(nmode theta)^2 angular weight in the gradient form.
    density={k:ap(p) for k,p in rho.items()};deriv={k:ap(p) for k,p in Dr.items()};squaresC={}
    for (i,n),p in density.items():
        for (j,m),q in density.items():
            ac=2*(n==m)-(abs(n-m)==2*nmode)+(n+m==2*nmode)
            bc=2*(n==m)-(abs(n-m)==2*nmode)-(n+m==2*nmode)
            if ac or bc:
                squaresC[i+j]=squaresC.get(i+j,arb_poly([]))+deriv[i,n]*deriv[j,m]*ac+p*q*(n*m*bc)
    poly2=ap(poly)*ap(poly)
    normC2=arb.pi()/8*sum((integ_ap(p*poly2,1-a+(j+2)*delta/2) for j,p in squaresC.items()),arb(0))
    print('C done','seconds',time.monotonic()-start,flush=True)
    # Pair F with phi directly, differentiating rho rather than integrating by parts.
    pairpoly=ap(poly)
    lin=arb.pi()/2*sum((integ_ap((ap(Dr[j,n])*f.ar(c)-ap(R))*pairpoly,(j+1)*delta/2-1) for (j,n),R in rho.items() if n==nmode),arb(0))
    nonlinear={}
    for (j,m),S in stream.items():
        for (i,n),R in rho.items():
            coeff=arb_poly([])
            if n+m==nmode:
                coeff+=(-m*ap(S)*ap(Dr[i,n])+n*ap(Ds[j,m])*ap(R))*f.ar(Q(1,2))
            if abs(n-m)==nmode:
                coeff+=(1 if n>m else -1)*(-m*ap(S)*ap(Dr[i,n])-n*ap(Ds[j,m])*ap(R))*f.ar(Q(1,2))
            if coeff:nonlinear[i+j]=nonlinear.get(i+j,arb_poly([]))+coeff
    pair=lin+arb.pi()/2*sum((integ_ap(p*pairpoly,(j+2)*delta/2-1) for j,p in nonlinear.items()),arb(0))
    assert normM2>0 and normC2>0 and abs(pair)>0
    M,C=normM2.sqrt(),normC2.sqrt()
    comparisons={key:bool(value.overlaps(arb(row[key]))) for key,value in [('M',M),('C',C),('pairing',pair)]}
    assert all(comparisons.values()),comparisons
    print('pair done; comparisons',comparisons,'seconds',time.monotonic()-start,flush=True)
    # Loose enough to certify independently, tight enough to retain six significant digits.
    htarget=Q(row['H_upper_exact'])
    sup=sup_certificate(poly,a,htarget,nmode)
    CU=Q(row['C_U_exact']);D=M+f.ar(CU)*C
    radius=2*abs(pair)/(D+(D*D+4*f.ar(CU*htarget)*abs(pair)).sqrt())
    floor=Q(int((radius.lower()*arb(10**12)).floor().unique_fmpz()),10**12)
    assert f.ar(floor)<radius
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':args.candidate,'angular_mode':nmode,'a':str(a),'precision_bits':ctx.prec,'source_sha256':sha(source),'peer_sha256':sha(peers),'code_sha256':sha(__file__),'helper_sha256':sha(HELPER),'probe_coefficients':row['probe_coefficients'],'pairing':pair.str(100),'M':M.str(100),'C':C.str(100),'comparisons':comparisons,'sup_certificate':sup,'C_U_exact':str(CU),'D':D.str(100),'radius':radius.str(100),'strict_lower_exact':str(floor),'elapsed_seconds':time.monotonic()-start}
    dest=ROOT/'verification'/f'n{nmode}_a{str(a).replace("/","_")}_direct.json'
    assert not dest.exists()
    dest.write_text(json.dumps(out,indent=2)+'\n');print(dest,'radius',radius.str(35),'strict floor',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
