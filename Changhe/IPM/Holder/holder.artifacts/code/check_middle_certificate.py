"""Independent real-coordinate and cell-distance diagnostics for middle transport."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import numpy as np,json
from numpy.polynomial.legendre import leggauss
from certify_middle_circles import bin_data
from certify_far_circles import cell_measures
from check_reflection_integrals import evaluate
ctx.prec=160

def real_density(tt,ss,phase):
    r=np.sin(tt);th=np.pi/2+tt*ss;X=r*np.cos(th);Y=r*np.sin(th)
    dx=X-.5;ex=X+.5;d1=dx*dx+Y*Y;d2=ex*ex+Y*Y
    re=((dx*dx-Y*Y)/d1**2-(ex*ex-Y*Y)/d2**2)/(2*np.pi)
    im=-dx*Y/(np.pi*d1**2)+ex*Y/(np.pi*d2**2)
    return tt*r*np.cos(tt)*(np.cos(phase)*re-np.sin(phase)*im)

def main():
    n=128;nr=64;unit=2**44;gx,gw=leggauss(32);count=0;maxexcess=0.;rng=np.random.default_rng(114544)
    for index in [0,1,8,16,31,47,62,63]:
        lo,hi,rmax,values,M1,M2=bin_data(index,nr,n)
        for phase in [0,np.pi/8,np.pi/4,np.pi/2]:
            cc=arb(str(phase)).cos();ss=arb(str(phase)).sin();mass,tv=cell_measures(values,cc,ss,M1,M2,arb(2)/n,unit)
            for tt in np.linspace(float(lo.mid()),float(hi.mid()),5):
                totalvar=0.
                for j in range(n):
                    s0=-1+2*j/n;s1=s0+2/n;s=(s0+s1)/2+(s1-s0)/2*gx
                    w=real_density(tt,s,phase);value=np.dot(w,gw)*(s1-s0)/2
                    totalvar+=np.dot(abs(w),gw)*(s1-s0)/2
                    if mass[j]:
                        assert np.min(np.sign(mass[j])*w)>-1e-12
                        assert np.sign(mass[j])*value+1e-12>=abs(mass[j])/unit
                    count+=1
                assert totalvar<=float(tv.upper())+1e-10
        # Cell chord bounds, independent random points and both types.
        a=float(lo.mid());b=float(hi.mid())
        for _ in range(300):
            i,j=rng.integers(0,n,2);same=bool(rng.integers(0,2));tt=rng.uniform(a,b)
            si=-1+2*(i+rng.random())/n;sj=-1+2*(j+rng.random())/n
            zi=np.sin(tt)*np.exp(1j*(np.pi/2+tt*si));zj=np.sin(tt)*np.exp(1j*(np.pi/2+tt*sj))
            if not same:zj=-zj
            k=abs(i-j)
            bound=2*np.sin(b)*(np.sin(b*(k+1)/n) if same else np.cos(a*max(0,k-1)/n))
            excess=abs(zi-zj)-bound;maxexcess=max(maxexcess,excess);assert excess<1e-12
    # Cross-disk integral checked in Cartesian coordinates.
    cross=json.loads(Path('data/cross_disk_certificate.json').read_text());phases=np.arange(cross['phase_intervals']+1)*np.pi/(2*cross['phase_intervals']);rows=[]
    for row in cross['rows']:
        from fractions import Fraction
        _,value=evaluate(float(Fraction(row['alpha'])),phases,320)
        for val,interval in zip(value,row['cross_phase_intervals']):
            ball=arb(interval);assert float(ball.lower())<val<float(ball.upper())
        rows.append(dict(alpha=row['alpha'],all_cross_values_enclosed=True,cross_values=value.tolist()))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),middle_mass_checks=count,distance_checks=2400,largest_distance_excess=maxexcess,cross_rows=rows,status='Independent floating diagnostics; analytic cell and transport proofs supply rigor.')
    Path('data/middle_cell_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n');print(count,maxexcess)
if __name__=='__main__':main()
