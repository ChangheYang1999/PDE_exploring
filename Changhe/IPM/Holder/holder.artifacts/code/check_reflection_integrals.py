"""Independent Cartesian/polar GL diagnostic for the reflection regular cost.
No interval claims are inferred from this floating computation.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib
import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import arb,ctx
ctx.prec=160

def evaluate(alpha,phases,n):
    xx,ww=leggauss(n); t=(xx+1)/2; wt=ww/2
    radius=t[:,None]
    angle0=np.arccos(radius)
    angle=angle0+(np.pi/2-angle0)*t[None,:]
    zm=radius*np.exp(1j*angle)
    gm=zm/(np.pi*(zm*zm-.25)**2)
    wm=radius*(np.pi/2-angle0)*wt[:,None]*wt[None,:]
    x=t[:,None]; ymax=np.sqrt(x*(1-x)); y=ymax*t[None,:]
    zc=x+1j*y; qc=1/(2*np.pi*(zc+.5)**2)
    wc=ymax*wt[:,None]*wt[None,:]
    def costs(z,g,weights):
        horizontal=(2*z.real)**alpha; vertical=(2*z.imag)**alpha; diagonal=(2*np.abs(z))**alpha
        result=[]
        for phase in phases:
            aa=np.abs(g.real)*np.cos(phase); bb=np.abs(g.imag)*np.sin(phase)
            cost=2*np.maximum(aa*horizontal+bb*(diagonal-horizontal),aa*(diagonal-vertical)+bb*vertical)
            result.append(float(np.sum(cost*weights)))
        return np.array(result)
    return costs(zm,gm,wm),costs(zc,qc,wc)

def main():
    p=Path('data/reflection_orbit_certificate_v2_coarse.json'); source=json.loads(p.read_text());m=source['phase_intervals']
    phases=np.arange(m+1)*np.pi/(2*m);rows=[]
    for row in source['rows']:
        alpha=float(Fraction(row['alpha']));out=[]
        for n in [160,320]:
            v,w=evaluate(alpha,phases,n);out.append(v+w)
        enclosed=[]
        for i,text in enumerate(row['regular_grid']):
            interval=arb(text); value=out[-1][i];enclosed.append(float(interval.lower())<=value<=float(interval.upper()))
        if not all(enclosed):raise ArithmeticError((row['alpha'],enclosed))
        rows.append(dict(alpha=row['alpha'],phase_values=out[-1].tolist(),max_grid_change=float(np.max(abs(out[-1]-out[-2]))),all_inside_arb_intervals=all(enclosed),middle=v.tolist(),cross=w.tolist()))
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),method='Independent GL in direct radius and Cartesian disk coordinates',status='Floating diagnostic only',certificate_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),rows=rows)
    Path('data/reflection_regular_diagnostic_v2.json').write_text(json.dumps(result,indent=2)+'\n')
    for r in rows:print(r['alpha'],max(r['phase_values']),r['max_grid_change'],r['all_inside_arb_intervals'])
if __name__=='__main__':main()
