"""Independent real-coordinate checks of local-circle mass and cost enclosures.
Quadrature diagnostics supplement, rather than replace, the analytic proof.
"""
from pathlib import Path
from datetime import datetime, timezone
from flint import arb
import numpy as np, json, hashlib
from numpy.polynomial.legendre import leggauss
from certify_local_circles_greedy import angular_data, edge_cost, UNIT
ROOT=Path(__file__).resolve().parents[1]

def wreal(r,t,phi):
    c=np.cos(t);s=np.sin(t);D=1+2*r*c+r*r
    cross=(np.cos(phi)*((1+r*c)**2-r*r*s*s)+np.sin(phi)*2*(1+r*c)*r*s)/D**2
    return (np.cos(2*t-phi)-r*r*cross)/(2*np.pi)

def main():
    n=512;nr=256;delta=arb(1)/64;R=arb(1)/2
    gx,gw=leggauss(16);mass_checks=0;sign_checks=0;cost_checks=0;tv_checks=0
    rng=np.random.default_rng(842027)
    for row in [0,1,32,128,255]:
        a=delta+(R-delta)*row/nr;b=delta+(R-delta)*(row+1)/nr
        af=float(a);bf=float(b)
        for k in [0,3,8,10,16]:
            phi=arb.pi()*k/32;pf=np.pi*k/32
            masses,tv,arcs,_=angular_data(a,b,phi,n)
            angles=pf/2+np.pi/4+np.arange(n+1)*2*np.pi/n
            t=(angles[:-1,None]+angles[1:,None])/2+np.pi/n*gx[None,:]
            for r in [af,(3*af+bf)/4,(af+bf)/2,(af+3*bf)/4,bf]:
                value=wreal(r,t,pf);integrals=value@gw*np.pi/n
                for j,m in enumerate(masses[:n]):
                    if m:
                        assert np.sign(m)*integrals[j]+2e-14>=abs(m)/UNIT,(row,k,j,r,m,integrals[j])
                        assert np.min(np.sign(m)*value[j])>=-2e-12
                        mass_checks+=1;sign_checks+=16
                actual_tv=float((abs(value)@gw).sum()*np.pi/n)
                assert actual_tv<=float(tv.upper())+2e-12,(row,k,r,actual_tv,tv)
                tv_checks+=1
            # Verify same-circle unit chord and cross-circle max distance independently.
            for trial in range(64):
                i=int(rng.integers(2*n));j=int(rng.integers(2*n))
                if i==j:continue
                ii=i%n;jj=j%n
                th=angles[ii]+rng.random(8)*2*np.pi/n
                et=angles[jj]+rng.random(8)*2*np.pi/n
                rr=af+(bf-af)*rng.random(8)
                zi=(.5+rr*np.exp(1j*th))*(1 if i<n else -1)
                zj=(.5+rr*np.exp(1j*et))*(1 if j<n else -1)
                bound=edge_cost(i,j,a,b,arb(1)/2,n,arcs)
                if i//n==j//n:
                    normalized=abs(zi-zj)/rr
                    scaled=(float(bound.upper())/(2*(bf**.5-af**.5)))**2
                else:
                    normalized=abs(zi-zj)
                    scaled=(float(bound.upper())/np.log(bf/af))**2
                assert np.max(normalized)<=scaled+2e-11,(row,k,i,j,np.max(normalized),scaled)
                cost_checks+=8
    paths=['code/check_local_circle_cells.py','code/certify_local_circles_greedy.py','code/local_circle_greedy.py','08_improved_upper_bounds/paired_local_circles/PROOF.md']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),mass_checks=mass_checks,sign_samples=sign_checks,cost_samples=cost_checks,total_variation_checks=tv_checks,status='All independent real-coordinate diagnostics passed; analytic proof and exact marginal checks remain the certificate basis',sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/'data/local_circle_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
