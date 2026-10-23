"""Manufactured reconstruction/gradient tests and a radial Green reference."""
from pathlib import Path
import json
from datetime import datetime,timezone
import numpy as np
from scipy.integrate import quad
from q_checkpoint_reader import QCheckpoint
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient

root=Path('evidence/q_reader_tests');root.mkdir(parents=True,exist_ok=True)
rows=[]
for kap in (1.05,1.5,3.,11.):
    L=.7;u=np.array([.91,.17,-.08,.03,-.12,.07,.011])
    # N=3,M=2, B0=.91+.17T1-.08T2+.03T3; B1=-.12+.07T1+.011T2.
    path=root/'manufactured.npz'
    np.savez_compressed(path,N=3,M=2,L=L,p=kap,gamma=1-1/kap,cl=1/(1-1/kap),u=u)
    c=QCheckpoint(path)
    ts=np.array([-1+1e-12,-.997,-.61,-.05,.22,.8,.99,1-1e-8])
    sig=(1+ts)/2;z=1-ts;r=L*np.sqrt(sig)/z**kap
    tt,ss,ww=c.coordinates(r)
    errors=[float(max(abs(tt-ts))),float(max(abs(ss-sig)/sig)),float(max(abs(ww-z/2)/(z/2)))]
    angles=np.array([.037,.29,.7,1.41,2.07,2.8,.54,1.2])
    B0=lambda t: .91+.17*t-.08*(2*t*t-1)+.03*(4*t**3-3*t)
    B1=lambda t: -.12+.07*t+.011*(2*t*t-1)
    BP0=lambda t:.17-.32*t+.03*(12*t*t-3)
    BP1=lambda t:.07+.044*t
    S=B0(ts)+sig*B1(ts)*np.cos(2*angles)
    expected=r*np.sin(angles)*(z/2)*S
    xx=r*np.cos(angles);yy=r*np.sin(angles)
    density_error=float(max(abs(c.rho(xx,yy)-expected)/np.maximum(1e-30,abs(expected))))
    St=BP0(ts)+(.5*B1(ts)+sig*BP1(ts))*np.cos(2*angles)
    Sth=-2*sig*B1(ts)*np.sin(2*angles)
    rdt=1/(1/(4*sig)+kap/z)
    rho_r=np.sin(angles)*(z*S/2+rdt*(-S/2+z*St/2))
    rho_th_over_r=z/2*(np.cos(angles)*S+np.sin(angles)*Sth)
    gx=rho_r*np.cos(angles)-rho_th_over_r*np.sin(angles)
    gy=rho_r*np.sin(angles)+rho_th_over_r*np.cos(angles)
    fd=[];component_fd=[]
    for step in (.003,.0015,.00075):
        dx,dy=cartesian_gradient(c.rho,xx,yy,step,0.)
        component_fd.append(float(max(np.max(abs(dx-gx)/np.maximum(abs(gx),1e-30)),np.max(abs(dy-gy)/np.maximum(abs(gy),1e-30)))))
        fd.append(float(np.max(np.hypot(dx-gx,dy-gy)/np.maximum(np.hypot(gx,gy),1e-100))))
    row={'kappa':kap,'map_errors':errors,'density_relative_error':density_error,'FD8_vector_relative_errors':fd,'FD8_component_relative_errors_including_roundoff_dominated_dx':component_fd}
    rows.append(row);print(json.dumps(row),flush=True)
    assert max(errors)<3e-12 and density_error<3e-12 and min(fd)<2e-8

path=root/'radial.npz';np.savez_compressed(path,N=1,M=1,L=1.,p=1.5,gamma=1/3,cl=3.,u=np.array([1.,0.]))
c=QCheckpoint(path);ct=c.center_and_tail()
assert abs(ct['a0']-1)<1e-15 and abs(ct['quadrature'][-1]['c']+.25)<1e-15
inverse_rows=[]
for level,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
    inv=DirectInverse(c.rho,Quadrature(nr,nt,ne,of,2**-c.kappa,c.p,16.,c.kappa))
    checks=[]
    for x,y in [(0.02,.037),(.53,.49),(10.2,7.3),(3000.,700.)]:
        r=np.hypot(x,y);th=np.arctan2(y,x)
        scaledI,err=quad(lambda v:v**3*float(c.coordinates(np.array(r*v))[2]),0,1,epsabs=1e-12,epsrel=1e-12,limit=200)
        w=float(c.coordinates(np.array(r))[2]);g_over_r=-r*scaledI/2;gp=r*(scaledI-w/2)
        ur=-2*g_over_r*np.cos(2*th);ut=gp*np.sin(2*th)
        exact=np.array([ur*np.cos(th)-ut*np.sin(th),ur*np.sin(th)+ut*np.cos(th)])
        actual=inv.velocity(x,y);error=float(max(abs(actual-exact)))
        checks.append({'x':x,'y':y,'absolute_error':error,'scaled_error':error/max(1.,float(max(abs(exact)))),'reference_quad_error':err})
    inverse_rows.append({'level':level,'points':checks});print(json.dumps(inverse_rows[-1]),flush=True)
assert max(v['scaled_error'] for v in inverse_rows[-1]['points'])<3e-8
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','reconstruction_checks':rows,'radial_inverse_checks':inverse_rows,'scope':'Tests of independently implemented representation/map, Cartesian FD8, and whole-plane kernel against a separately evaluated radial Green integral. Not a profile-existence test.'}
(root/'result.json').write_text(json.dumps(result,indent=2)+'\n')
