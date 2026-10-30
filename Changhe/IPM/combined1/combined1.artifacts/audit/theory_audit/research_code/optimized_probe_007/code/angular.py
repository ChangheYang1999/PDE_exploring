"""Canonical 007 weak-probe search and outward verification; no imported search code."""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import argparse, hashlib, importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as P, arb, arb_poly, ctx
import mpmath as mp
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('polar',HELPER)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
T,W,Z=f.T,f.W,f.ZERO
ar=f.ar
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ap(p):return arb_poly([ar(v) for v in p])
def add(d,k,p):d[k]=d.get(k,Z)+p
@lru_cache(None)
def moment_row(K,bstr,n):
    # Integral t^(K+1) W^(b+j), j=0..n-1. Integer first Beta argument.
    b=Q(bstr);assert K>=0 and b>-1
    v=ar(1/(b+1))
    for k in range(1,K+2):v*=ar(k/(b+k+1))
    ans=[v]
    for j in range(n-1):ans.append(ans[-1]*ar((b+j+1)/(K+b+j+3)))
    return ans
def integrate(p,K,b):
    coeff=list(p);ms=moment_row(K,str(b),len(coeff))
    return sum((v*m for v,m in zip(coeff,ms)),arb(0))
def transform(d):
    ww=arb_poly([1,-1])
    return {k:p(ww) for k,p in d.items()}
def matrix_value(G,cs):
    return sum((ar(cs[i])*ar(cs[j])*G[i][j] for i in range(len(cs)) for j in range(len(cs))),arb(0))
def certify_H(poly,a,n):
    polys=[n*poly,(1-4*T)*poly+2*T*W*poly.derivative()]
    vals=[(ap(p),ap(p.derivative())) for p in polys]
    def cell(lo,hi):
        mid=(lo+hi)/2;rad=(hi-lo)/2;x=arb(ar(mid),ar(rad)*(1+arb(2)**-100))
        up=max((ar(1-lo)**ar(2-a)*(abs(p(ar(mid)))+ar(rad)*abs(dp(x)))).upper() for p,dp in vals)
        low=max((ar(1-mid)**ar(2-a)*abs(p(ar(mid)))).lower() for p,dp in vals)
        return lo,hi,up,low
    cells=[cell(Q(0),Q(1))];best=arb(0)
    while True:
        for _,_,_,v in cells:
            if v>best:best=v
        worst=max(range(len(cells)),key=lambda i:float(cells[i][2]))
        cap=cells[worst][2]
        if best>0 and cap<best*ar(Q(101,100)):
            target=Q(int((cap*arb(10**12)).ceil().unique_fmpz())+1,10**12)
            assert ar(target)>cap
            return target,{'cells':len(cells),'lower_sample':best.str(40),'upper':cap.str(40),'relative_stop':'101/100'}
        lo,hi,_,_=cells.pop(worst);mid=(lo+hi)/2
        assert len(cells)<10000 and hi-lo>Q(1,2**45)
        cells.extend([cell(lo,mid),cell(mid,hi)])
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',type=int,default=3);parser.add_argument('--a',default='0');parser.add_argument('--bits',type=int,default=2048);args=parser.parse_args()
    nmode=args.mode;assert nmode>0 and nmode%2==1
    a=Q(args.a);assert a in (Q(0),Q(1),Q(6,5))
    CU={Q(0):Q(1),Q(1):Q(2),Q(6,5):Q(808233,500000)}[a]
    ctx.prec=args.bits;mp.mp.dps=85;start=time.monotonic()
    source=ROOT.parent/'projected_laplacian/data/candidate007_canonical.json'
    c,delta,rho,stream=f.fields(json.loads(source.read_text()))
    print('fields',len(rho),len(stream),'seconds',time.monotonic()-start,flush=True)
    Q0=1-4*T;Q1=2*W;A0=(2*c+1)+c*Q0;A1=c*Q1
    Dstream={key:f.td(p,(key[0]+1)*delta/2,2) for key,p in stream.items()}
    Drho={key:f.td(p,(key[0]+1)*delta/2,1) for key,p in rho.items()}
    modes0={(0,nmode):A0};modes1={(0,nmode):A1}
    for (j,n),p in stream.items():
        pieces=[(nmode+n,(nmode*Dstream[j,n]-n*p*Q0)/2,-n*p*Q1/2),
                (nmode-n,(-nmode*Dstream[j,n]-n*p*Q0)/2,-n*p*Q1/2)]
        for m,p0,p1 in pieces:
            if not m:continue
            sign=1 if m>0 else -1
            add(modes0,(j+1,abs(m)),sign*p0);add(modes1,(j+1,abs(m)),sign*p1)
    modes=[{key:ap(p) for key,p in modes0.items()},{key:ap(p) for key,p in modes1.items()}]
    E={}
    for u,v in [(0,0),(0,1),(1,1)]:
        acc={}
        for (j,n),p in modes[u].items():
            for (k,m),q in modes[v].items():
                if m==n:acc[j+k]=acc.get(j+k,arb_poly([]))+p*q
        E[u,v]=transform(acc)
    rr={key:ap(p) for key,p in rho.items()};dr={key:ap(p) for key,p in Drho.items()};C={}
    for (i,n),p in rr.items():
        for (j,m),q in rr.items():
            ac=2*(n==m)-(abs(n-m)==2*nmode)+(n+m==2*nmode)
            bc=2*(n==m)-(abs(n-m)==2*nmode)-(n+m==2*nmode)
            if ac or bc:C[i+j]=C.get(i+j,arb_poly([]))+dr[i,n]*dr[j,m]*ac+p*q*(n*m*bc)
    C=transform(C)
    allI=[]
    for u in [0,1]:
        acc={}
        for (j,n),R in rr.items():
            for (k,m),A in modes[u].items():
                if n==m:acc[j+1+k]=acc.get(j+1+k,arb_poly([]))-2*R*A
        allI.append(transform(acc))
    I0,I1=allI
    print('forms done','seconds',time.monotonic()-start,flush=True)
    kmin=(nmode-1)//2
    Ks=sorted({kmin}|{k for k in [0,1,2,3,4,6,8,12,16,24,32,48,64,96,128] if k>=kmin})
    def GM(k,l):
        return arb.pi()/2*sum((integrate(E[0,0].get(j,arb_poly([]))+(k+l)*E[0,1].get(j,arb_poly([]))+k*l*E[1,1].get(j,arb_poly([])),k+l,1-a+j*delta/2) for j in set(E[0,0])|set(E[0,1])|set(E[1,1])),arb(0))
    def GC(k,l):return arb.pi()/8*sum((integrate(p,k+l,1-a+(j+2)*delta/2) for j,p in C.items()),arb(0))
    def pair(k):return arb.pi()/4*sum((integrate(I0.get(j,arb_poly([]))+k*I1.get(j,arb_poly([])),k,j*delta/2-1) for j in set(I0)|set(I1)),arb(0))
    Gm=[[arb(0) for k in Ks] for l in Ks];Gc=[[arb(0) for k in Ks] for l in Ks]
    Iv=[pair(k) for k in Ks]
    for i,k in enumerate(Ks):
        for j in range(i,len(Ks)):
            Gm[i][j]=Gm[j][i]=GM(k,Ks[j]);Gc[i][j]=Gc[j][i]=GC(k,Ks[j])
        print('Gram row',i,'seconds',time.monotonic()-start,flush=True)
    mpv=lambda x:mp.mpf(x.mid().str(75,radius=False))
    M=mp.matrix([[mpv(x) for x in row] for row in Gm]);Cmat=mp.matrix([[mpv(x) for x in row] for row in Gc]);b=mp.matrix([mpv(x) for x in Iv]);cu=mp.mpf(int(CU.numerator))/mp.mpf(int(CU.denominator))
    best=None
    for ei in range(-30,31):
        mu=mp.power(10,mp.mpf(ei)/10)
        v=mp.lu_solve(M+mu*Cmat,b)
        score=abs((v.T*b)[0])/(mp.sqrt((v.T*M*v)[0])+cu*mp.sqrt((v.T*Cmat*v)[0]))
        if best is None or score>best[0]:best=(score,v,mu)
    _,v,mu=best;sc=max(abs(x) for x in v)
    cs=[Q(int(mp.nint(x/sc*10**30)),10**30) for x in v]
    poly=sum((x*T**k for x,k in zip(cs,Ks)),Z)
    H,hproof=certify_H(poly,a,nmode)
    I=sum((ar(x)*y for x,y in zip(cs,Iv)),arb(0));mn=matrix_value(Gm,cs);cn=matrix_value(Gc,cs)
    assert mn>0 and cn>0
    mnorm,cnorm=mn.sqrt(),cn.sqrt();D=mnorm+ar(CU)*cnorm
    radius=2*abs(I)/(D+(D*D+4*ar(CU*H)*abs(I)).sqrt())
    floor=Q(int((radius.lower()*arb(10**12)).floor().unique_fmpz()),10**12);assert ar(floor)<radius
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-N1-007-d2w-j7-e2bal','a':str(a),'angular_mode':nmode,'C_U_exact':str(CU),'bits':ctx.prec,'input_sha256':sha(source),'code_sha256':sha(__file__),'helper_sha256':sha(HELPER),'probe_coefficients':{str(k):str(x) for k,x in zip(Ks,cs)},'pairing':I.str(100),'M':mnorm.str(100),'C':cnorm.str(100),'H_upper_exact':str(H),'H_certificate':hproof,'radius':radius.str(100),'strict_lower_exact':str(floor),'FLOAT_search_mu':str(mu),'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent numerical audit'}
    dest=ROOT/'verification'/f'n{nmode}_a{str(a).replace("/","_")}.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
    print('RESULT',radius.str(35),'strict',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
