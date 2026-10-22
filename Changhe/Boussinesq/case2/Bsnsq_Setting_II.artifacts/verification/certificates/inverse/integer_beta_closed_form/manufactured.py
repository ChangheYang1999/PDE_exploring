#!/usr/bin/env python3
"""Original-basis Cartesian differentiation and physical-radial integration."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import mpmath as mp
import numpy as np
import exact_inverse as inv
ROOT=Path(__file__).resolve().parent

def chebrow(row,t):
    z=2*t-1;left=mp.mpf(1);total=mp.mpf(float(row[0]))
    if len(row)==1:return total
    current=z;total+=mp.mpf(float(row[1]))*current
    for x in row[2:]:
        left,current=current,2*z*current-left;total+=mp.mpf(float(x))*current
    return total

def original(ca,cg,b,x,y):
    r2=x*x+y*y;t=(1+r2)**(-mp.mpf(1)/(2*b));q=r2/(1+r2);phi=mp.atan2(y,x)
    a=mp.fsum(q**m*chebrow(row,t)*mp.cos(2*m*phi) for m,row in enumerate(ca))
    c=mp.fsum(q**m*chebrow(row,t)*mp.cos(2*m*phi) for m,row in enumerate(cg))
    return x*x*y*t**(2*b+2)*a,x*y*t**(2*b+1)*c

def main():
    start=time.monotonic();mp.mp.dps=70;rows=[]
    for b in(2,3,4):
        N=2*b;ca=np.array([[((-1)**(m+j))*(m+1)/(2.**(j+4)) for j in range(N)] for m in range(3)],dtype=np.float64)
        cg=np.array([[(m+2)/(2.**(j+3)) for j in range(N)] for m in range(3)],dtype=np.float64);comp=inv.compiler(ca,cg,b)
        # Independent discrete angular projection of the original basis.
        angles=[2*mp.pi*j/32 for j in range(32)]
        projection=[[mp.fsum(mp.sin(2*k*p)*mp.sin(p)*mp.cos(p)*mp.cos(2*m*p) for p in angles)/16 for m in range(3)] for k in range(1,4)]
        def B(k,r):
            t=(1+r*r)**(-mp.mpf(1)/(2*b));q=r*r/(1+r*r)
            return q*t*mp.fsum(projection[k-1][m]*q**m*chebrow(cg[m],t) for m in range(3))
        radial_errors=[]
        for rs in('1.2','3.1'):
            r=mp.mpf(rs);t=(1+r*r)**(-mp.mpf(1)/(2*b));v=inv.radial(comp,t)
            for k in range(1,4):
                inner=r**(2*k+2)*mp.quad(lambda s:s**(2*k+1)*B(k,r*s),[0,1])
                # Physical rho=r/s^b removes the fractional far-tail power.
                outer=b*r**(2-2*k)*mp.quad(lambda s:s**(b*(2*k-2)-1)*B(k,r/s**b) if s else mp.mpf(0),[0,1])
                h=(r**(-2*k)*inner+r**(2*k)*outer)/(4*k)
                hc=t**(1-2*b)*(v['X'][k-1]+v['Y'][k-1])/(4*k)
                radial_errors.append(abs(h-hc))
        errors=[]
        def psi(x,y):return inv.polar(comp,mp.sqrt(x*x+y*y),mp.atan2(y,x))[0]
        for xs,ys in(('.7','.3'),('1.8','.04'),('2','0'),('0','2')):
            x,y=mp.mpf(xs),mp.mpf(ys);got=inv.cartesian(comp,x,y)
            th=lambda xx,yy:original(ca,cg,b,xx,yy)[0];om=lambda xx,yy:original(ca,cg,b,xx,yy)[1]
            thx,thy=mp.diff(lambda xx:th(xx,y),x),mp.diff(lambda yy:th(x,yy),y)
            omx,omy=mp.diff(lambda xx:om(xx,y),x),mp.diff(lambda yy:om(x,yy),y)
            u1=-mp.diff(lambda yy:psi(x,yy),y);u2=mp.diff(lambda xx:psi(xx,y),x)
            lp=-mp.diff(lambda xx:psi(xx,y),x,2)-mp.diff(lambda yy:psi(x,yy),y,2)
            vals={'Theta':th(x,y),'Omega':om(x,y),'Theta_x':thx,'Theta_y':thy,'Omega_x':omx,'Omega_y':omy,'U1':u1,'U2':u2,'R_Theta':(b*x+u1)*thx+(b*y+u2)*thy-(b-2)*th(x,y),'R_Omega':(b*x+u1)*omx+(b*y+u2)*omy+om(x,y)-thx}
            errors.extend(abs(got[k]-v) for k,v in vals.items());errors.append(abs(lp-om(x,y)))
            if x==0 or y==0:
                assert got['R_Theta']==0 and got['N_Theta']==0 and got['ratio_Theta'] is None
                assert got['R_Omega']==0 and got['N_Omega']==0 and got['ratio_Omega'] is None
                which=0 if y==0 else 1;r=x if y==0 else y;ar=inv.axis(comp,r,which)
                velocity=(lambda z:-mp.diff(lambda w:psi(z,w),0)) if which==0 else (lambda z:mp.diff(lambda w:psi(w,z),0))
                errors.append(abs(ar['U']-velocity(r)))
                errors.append(abs(ar['derivative']-(b+mp.diff(velocity,r))))
        mm=inv.moments(ca,cg,comp)['c'];quad=b*mp.quad(lambda t:(chebrow(cg[0],t)-(1-t**(2*b))**2*chebrow(cg[2],t)/2),[0,1])/4;centererr=abs(quad-mp.mpf(mm.numerator)/mm.denominator)
        nonzero_logs=sum(x['L']<len(x['P']) and x['P'][x['L']]!=0 for x in comp['modes'])
        assert nonzero_logs==3
        assert max(radial_errors)<mp.mpf('1e-55') and max(errors)<mp.mpf('1e-55') and centererr<mp.mpf('1e-55')
        rows.append({'beta':b,'max_physical_radial_error':inv.dec(max(radial_errors)),'max_Cartesian_differentiation_error':inv.dec(max(errors)),'center_quadrature_error':inv.dec(centererr),'nonzero_logarithmic_modes':nonzero_logs,'radial_points':['1.2','3.1'],'Cartesian_points':[['.7','.3'],['1.8','.04'],['2','0'],['0','2']]})
        print(json.dumps(rows[-1]),flush=True)
    out={'finished_utc':datetime.now(timezone.utc).isoformat(),'dps':70,'elapsed_seconds':time.monotonic()-start,'status':'PASS','checks':rows,'code_sha256':inv.sha(inv.__file__),'manufactured_sha256':inv.sha(__file__),'scope':'Numerical manufactured tests, no interval bounds; independently projected original basis and physical radial quadrature plus original Cartesian differentiation.'}
    (ROOT/'verification/manufactured.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','elapsed_seconds':out['elapsed_seconds']}))
if __name__=='__main__':main()
