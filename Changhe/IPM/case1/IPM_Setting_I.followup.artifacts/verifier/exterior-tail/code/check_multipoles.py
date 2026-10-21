"""Independent direct quadrature of pure exterior angular modes.
The checker uses a stable complex kernel pair, not an angular Green solver.
"""
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
R=2.;Rmax=1e20;nang=512;order=16
edges=np.linspace(np.log(R),np.log(Rmax),120)
g,w=leggauss(order)
logs=((edges[:-1,None]+edges[1:,None])/2+np.diff(edges)[:,None]*g/2).ravel()
weights=(np.diff(edges)[:,None]*w/2).ravel();r=np.exp(logs)
theta=(np.arange(nang)+.27)*2*np.pi/nang;e=np.exp(-1j*theta)
rows=[]
for gamma in [.2,.6,.9]:
 for mode in [1,3,5,7]:
  density=r[:,None]**gamma*np.sin(mode*theta)[None,:]
  for point in [(0.,0.),(.4,.3),(1.,.5)]:
   z=complex(*point).conjugate();t=z/r[:,None]
   rows_complex=(2j/nang)*(density*t*e/(t*t-e*e)**2).sum(1)
   measured=np.sum(weights*rows_complex)
   if mode==1:exact=0j
   else:
    exponent=gamma-mode+2
    moment=(Rmax**exponent-R**exponent)/exponent
    exact=-(mode-1)/2*z**(mode-2)*moment
   error=abs(measured-exact)
   rows.append({'gamma':gamma,'mode':mode,'point':point,'direct':[measured.real,measured.imag],
                'series':[exact.real,exact.imag],'error':error})
assert max(row['error'] for row in rows)<5e-13
out={'method':'direct paired complex kernel over a finite annulus versus exact multipole moment','R':R,'Rmax':Rmax,'rows':rows}
p=Path(__file__).resolve().parents[1]/'verification/manufactured_multipoles.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print('36 exterior-mode tests: max error',max(row['error'] for row in rows))
