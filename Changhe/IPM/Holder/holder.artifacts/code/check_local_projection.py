"""Arb formula certificates and independent quadrature diagnostics for local pairing."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import arb,ctx
ctx.prec=192
root=Path(__file__).resolve().parents[1]
old=json.loads((root/'data/explicit_bounds_intervals.json').read_text())
rows=[]
for r in old['rows']:
    a=arb(r['alpha']); v=r['intervals']; F=arb(v['upper_C']); a2=arb(v['a2']);B=arb(v['B'])
    A=((a+2)/2).gamma()/(2*arb.pi().sqrt()*((a+3)/2).gamma())
    scale=(1-a)*B/(2*A); bound=2*A*scale**a/(a*(1-a))+arb(1)/2
    alt=F*(A/a2)**(1-a)+arb(1)/2
    assert bound.overlaps(alt) and A<a2 and bound<F+arb(1)/2
    up=int((arb(bound.upper())*10**10).ceil().unique_fmpz())
    rows.append(dict(alpha=r['alpha'],A=A.str(45),scale=scale.str(45),upper_D=bound.str(45),
                     safe_decimal_upper_10_places=f'{up//10**10}.{up%10**10:010d}'))
C0=arb(1)/2+(arb(2).log()-1)/arb.pi()
# Independent finite quadratures test the operator identity on nonradial smooth functions.
x,w=leggauss(128); rs=(x+1)*.5; rw=w*.5; ts=(x+1)*np.pi/8; tw=w*np.pi/8
funcs=[('cosine',lambda x,y:np.cos(1.3*x-.7*y)),
       ('shifted Gaussian',lambda x,y:np.exp(-((x-.4)**2+2*(y+.3)**2))),
       ('quadratic',lambda x,y:x*x+.3*x*y-2*y*y)]
checks=[]
for name,f in funcs:
    for z in [(0.,0.),(.4,-.2)]:
        R=.7; f0=f(*z)
        theta=(x+1)*np.pi; thw=w*np.pi; rr=R*rs[:,None]
        vals=f(z[0]-rr*np.cos(theta),z[1]-rr*np.sin(theta))-f0
        N=float(np.sum(rw[:,None]*thw[None,:]*np.cos(2*theta)[None,:]*vals/rs[:,None])/(2*np.pi))
        P=0.;Qt=0.
        for center in [0.,np.pi]:
            for side in [-1,1]:
                plus=center+side*(np.pi/4-ts); minus=center+side*(np.pi/4+ts)
                lam=np.cos(2*ts)
                vplus=f(z[0]-rr*np.cos(plus),z[1]-rr*np.sin(plus))
                vminus=f(z[0]-rr*lam*np.cos(minus),z[1]-rr*lam*np.sin(minus))
                P+=float(np.sum(rw[:,None]*tw[None,:]*np.sin(2*ts)[None,:]*(vplus-vminus)/rs[:,None])/(2*np.pi))
                qr=R*(lam[None,:]+rs[:,None]*(1-lam[None,:]))
                qvals=f(z[0]-qr*np.cos(minus),z[1]-qr*np.sin(minus))-f0
                Qt+=float(np.sum(rw[:,None]*tw[None,:]*np.sin(2*ts)[None,:]*qvals/qr*R*(1-lam)[None,:])/(2*np.pi))
        err=N-P+Qt
        assert abs(err)<2e-13,(name,z,err)
        checks.append(dict(function=name,point=z,N=N,P=P,Q_minus_kappa_f=Qt,identity_error=err))
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,rows=rows,
         D_second_term_upper=(2*C0).str(60),C0=C0.str(60),diagnostics=checks,
         status='Arb intervals certify formula values. Finite quadratures only diagnose the independently proved identity.',
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'data/local_projection_intervals.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows: print(r['alpha'],r['safe_decimal_upper_10_places'])
print('D second term upper',out['D_second_term_upper'])
