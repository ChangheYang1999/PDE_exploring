"""Exact factored high-power weak test, retaining all background modes."""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import argparse, hashlib, importlib.util, json, sys, time
from flint import fmpq as Q, arb, arb_poly, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('t4_polar_highpower',HELPER)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
T,W,Z=f.T,f.W,f.ZERO
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ap(p):return arb_poly([f.ar(v) for v in p])
def add(d,k,v):d[k]=d.get(k,Z)+v
@lru_cache(None)
def moment_base(b,L):
    b=Q(b);assert b>-1 and isinstance(L,int) and L>=0
    value=f.ar(1/((b+1)*(b+2)))
    for ell in range(L):value*=f.ar(Q(ell+2)/(ell+b+3))
    return value

def integ(p,b,L):
    assert b>-1
    value=moment_base(str(b),L);total=arb(0)
    for j,coefficient in enumerate(p):
        total+=coefficient*value
        value*=f.ar(Q(L+j+2)/(L+j+b+3))
    return total

def supremum(K,n):
    assert K>0
    A,B=2*K+1,2*K+4
    aa,bb,cc=B*(K+3),(K+2)*A+(K+1)*B,K*A
    discriminant=bb*bb-4*aa*cc
    assert discriminant>0
    root=arb(discriminant).sqrt()
    roots=[(bb-root)/(2*aa),(bb+root)/(2*aa)]
    assert all(0<x and x<1 for x in roots)
    def g(t):return t**K*(1-t)**2*(A-B*t)
    t=f.ar(Q(K,K+2))
    caps=[abs(g(x)) for x in roots]+[n*t**K*(1-t)**2]
    numer=max(int((cap.upper()*arb(10**20)).ceil().unique_fmpz()) for cap in caps)+1
    H=Q(numer,10**20)
    assert all(cap<f.ar(H) for cap in caps)
    return H,{'method':'complete exact derivative-root classification and outward evaluation',
      'quadratic_coefficients':[aa,-bb,cc], 'discriminant':discriminant,
      'roots':[x.str(60) for x in roots], 'amplitude_caps':[x.str(60) for x in caps],
      'H_upper_exact':str(H)}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--candidate',default='015')
    parser.add_argument('--mode',type=int,default=23);parser.add_argument('--power',type=int,default=600)
    parser.add_argument('--bits',type=int,default=2048)
    args=parser.parse_args();ctx.prec=args.bits;start=time.monotonic()
    nmode,K=args.mode,args.power
    assert nmode>0 and nmode%2==1 and K>0 and K>=(nmode-1)//2
    probe_path=ROOT/'data'/f'probe_{nmode}_{K}.json'
    probe_data=json.loads(probe_path.read_text())
    assert probe_data['angular_mode']==nmode and probe_data['radial_power']==K
    assert Q(probe_data['coefficient'])==1
    source=ROOT.parent/'new_successor_weak/data'/args.candidate/'canonical.json'
    buildpath=ROOT.parent/'new_successor_weak/verification'/f'{args.candidate}_build.json'
    build=json.loads(buildpath.read_text());assert sha(source)==build['canonical_sha256']
    c,delta,rho,stream=f.fields(json.loads(source.read_text()))
    print('fields',len(rho),len(stream),'seconds',time.monotonic()-start,flush=True)
    radial=(2*K+1)-(2*K+4)*T
    A=(2*c+1)+c*radial
    Ds={(j,n):f.td(S,(j+1)*delta/2,2) for (j,n),S in stream.items()}
    Dr={(j,n):f.td(R,(j+1)*delta/2,1) for (j,n),R in rho.items()}
    modes={};add(modes,(0,nmode),A)
    for (j,n),S in stream.items():
        add(modes,(j+1,nmode+n),(nmode*Ds[j,n]-n*S*radial)/2)
        m=nmode-n
        if m:add(modes,(j+1,abs(m)),(1 if m>0 else -1)*(-nmode*Ds[j,n]-n*S*radial)/2)
    byn={}
    for (j,n),p in modes.items():byn.setdefault(n,[]).append((j,ap(p)))
    squares={}
    for entries in byn.values():
        for i,(j,p) in enumerate(entries):
            for k,q in entries[i:]:squares[j+k]=squares.get(j+k,arb_poly([]))+p*q*(1 if j==k else 2)
    exponents=[]
    def integral_record(p,b,L):
        exponents.append(b)
        return integ(p,b,L)
    normM2=arb.pi()/2*sum((integral_record(p,1+j*delta/2,2*K) for j,p in squares.items()),arb(0))
    print('M',normM2.str(20),'seconds',time.monotonic()-start,flush=True)
    density={k:ap(p) for k,p in rho.items()};deriv={k:ap(p) for k,p in Dr.items()};squaresC={}
    for (i,n),p in density.items():
        for (j,m),q in density.items():
            ac=2*(n==m)-(abs(n-m)==2*nmode)+(n+m==2*nmode)
            bc=2*(n==m)-(abs(n-m)==2*nmode)-(n+m==2*nmode)
            if ac or bc:
                squaresC[i+j]=squaresC.get(i+j,arb_poly([]))+deriv[i,n]*deriv[j,m]*ac+p*q*(n*m*bc)
    normC2=arb.pi()/8*sum((integral_record(p,1+(j+2)*delta/2,2*K) for j,p in squaresC.items()),arb(0))
    print('C',normC2.str(20),'seconds',time.monotonic()-start,flush=True)
    lin=arb.pi()/2*sum((integral_record(ap(Dr[j,n])*f.ar(c)-ap(R),(j+1)*delta/2-1,K) for (j,n),R in rho.items() if n==nmode),arb(0))
    nonlinear={}
    for (j,m),S in stream.items():
        for (i,n),R in rho.items():
            coeff=arb_poly([])
            if n+m==nmode:
                coeff+=(-m*ap(S)*ap(Dr[i,n])+n*ap(Ds[j,m])*ap(R))*f.ar(Q(1,2))
            if abs(n-m)==nmode:
                coeff+=(1 if n>m else -1)*(-m*ap(S)*ap(Dr[i,n])-n*ap(Ds[j,m])*ap(R))*f.ar(Q(1,2))
            if coeff:nonlinear[i+j]=nonlinear.get(i+j,arb_poly([]))+coeff
    pair=lin+arb.pi()/2*sum((integral_record(p,(j+2)*delta/2-1,K) for j,p in nonlinear.items()),arb(0))
    parts=-arb.pi()/2*sum((integral_record(ap(R)*ap(B),(j+1+k)*delta/2-1,K) for (j,n),R in rho.items() for (k,m),B in modes.items() if n==m),arb(0))
    assert pair.overlaps(parts)
    assert normM2>0 and normC2>0 and abs(pair)>0
    M,C=normM2.sqrt(),normC2.sqrt();D=M+C
    H,sup=supremum(K,nmode)
    radius=2*abs(pair)/(D+(D*D+4*f.ar(H)*abs(pair)).sqrt())
    floor=Q(int((radius.lower()*arb(10**12)).floor().unique_fmpz()),10**12)
    assert f.ar(floor)<radius
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':args.candidate,
      'angular_mode':nmode,'radial_power':K,'precision_bits':ctx.prec,
      'source_sha256':sha(source),'build_sha256':sha(buildpath),'proof_sha256':sha(ROOT/'PROOF.md'),
      'code_sha256':sha(__file__),'helper_sha256':sha(HELPER),'probe_sha256':sha(probe_path),
      'normM2':normM2.str(100),'normC2':normC2.str(100),'M':M.str(100),'C':C.str(100),
      'pairing':pair.str(100),'pairing_by_parts':parts.str(100),'direct_parts_overlap':True,
      'D':D.str(100),'sup_certificate':sup,'radius':radius.str(100),'strict_lower_exact':str(floor),
      'minimum_endpoint_exponent':str(min(exponents)),'radial_integral_count':len(exponents),
      'moment_base_count':moment_base.cache_info().currsize,'elapsed_seconds':time.monotonic()-start,
      'status':'OPEN independent numerical and new supremum-method review; necessary distance only.'}
    dest=ROOT/'verification'/f'{args.candidate}_n{nmode}_k{K}.json';assert not dest.exists()
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('radius',radius.str(35),'floor',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
