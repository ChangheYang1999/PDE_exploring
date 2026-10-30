"""Candidate-specific angular quadrature diagnostics from Arb radial coefficients."""
from pathlib import Path
from datetime import datetime,timezone
import sys,time,json,hashlib
import numpy as np
from flint import arb,arb_poly,fmpq,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from pipeline import load,source,DATA,digest
from radial import ar
BASE=ROOT/'research/angular_resolution'

def run(name):
    start=time.monotonic();ctx.prec=2048
    path=source(name);delta=1-1/fmpq(json.loads(path.read_text())['cl'])
    D=load(name,0);polys=[(ell,n,arb_poly([ar(v) for v in P])) for (ell,kind,n),P in D[0,0].items()]
    del D;maxn=max(n for ell,n,P in polys);nf=(maxn+1)//2;results=[]
    print('converted',len(polys),time.monotonic()-start,flush=True)
    for rr in ['1/2','1','2','5','10','30','100','1000']:
        r=ar(fmpq(rr));u=1/(1+r*r);t=1-u;coeff=[arb(0) for _ in range(nf)]
        powers={ell:r*u**ar(ell*delta/2) for ell,n,P in polys}
        for ell,n,P in polys:coeff[(n-1)//2]+=powers[ell]*P(t)
        den=arb.pi()*sum((x*x for x in coeff),arb(0));assert den>0
        qcoeff=[sum(coeff,arb(0))/r]+[2*sum(coeff[k:],arb(0))/r for k in range(1,nf)]
        quo=arb.pi()/2*qcoeff[0]**2+arb.pi()/4*sum((x*x for x in qcoeff[1:]),arb(0));assert quo>0
        f=np.array([float(x.mid()) for x in coeff]);q=np.array([float(x.mid()) for x in qcoeff]);checks=[]
        for N in [96,128,160,192,256]:
            z,w=np.polynomial.legendre.leggauss(N)
            for rule in ['gauss','midpoint']:
                if rule=='gauss':theta=(z+1)*np.pi/4;weights=w*np.pi/4
                else:theta=(np.arange(N)+.5)*np.pi/(2*N);weights=np.full(N,np.pi/(2*N))
                k=np.arange(nf)[:,None]
                df=f@np.sin((2*k+1)*theta);qf=q@np.cos(2*k*theta)
                density=4*np.sum(weights*df*df);quotient=np.sum(weights*qf*qf)
                checks.append({'order':N,'rule':rule,'density_relative_error':float(density/float(den.mid())-1),
                               'quotient_relative_error':float(quotient/float(quo.mid())-1)})
        results.append({'r':rr,'density_angular_norm_squared':den.str(70),'quotient_quadrant_norm_squared':quo.str(70),
                        'radial_sine_coefficients':[x.str(55) for x in coeff],'checks':checks})
        print('r',rr,'Gauss160',checks[4],time.monotonic()-start,flush=True)
    out={'candidate':name,'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
         'source_sha256':digest(path),'polynomial_sha256':digest(DATA/f'{name}_D0.json.gz'),
         'code_sha256':digest(Path(__file__)),'comparison_status':'FLOAT diagnostics from validated coefficient enclosures',
         'results':results,'elapsed_seconds':time.monotonic()-start}
    (BASE/f'verification/{name}_slices.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run(sys.argv[1])
