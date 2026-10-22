"""Independent Gauss-cell stream interpolation manufactures.

Legendre-series fits, not the solver's monomial/Torch implementation.
No teammate code is imported or executed. This script tests representation
identities only; all exact sources are smooth canonical manufactures, not
solutions of the coupled Boussinesq transport equations.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import comb
import hashlib, json, time
import numpy as np
from numpy.polynomial.legendre import leggauss, Legendre


def radius(t, beta, length):
    return length*np.sqrt(np.expm1(-2*beta*np.log1p(-np.asarray(t))))


def map_data(r, beta, length):
    z=np.exp(-np.log1p((r/length)**2)/(2*beta))
    t=-np.expm1(-np.log1p((r/length)**2)/(2*beta))
    dt=r*z/(beta*(length*length+r*r))
    return t,dt


def fit_cell(fun, lo, hi, n):
    xi,_=leggauss(n)
    return Legendre.fit(xi,fun(lo+(hi-lo)*(xi+1)/2),n-1,domain=[-1,1])


def cell_value(poly,t,lo,hi):
    xi=2*(t-lo)/(hi-lo)-1
    return poly(xi),poly.deriv()(xi)*2/(hi-lo)


def velocity(points,poly,lo,hi,beta,length,k=4,power=2):
    x,y=np.asarray(points).T
    r=np.hypot(x,y);phi=np.arctan2(x,-y)
    t,dt=map_data(r,beta,length)
    val,der=cell_value(poly,t,lo,hi)
    stream=r**power*val
    dr=power*r**(power-1)*val+r**power*der*dt
    psir=dr*np.sin(k*phi);psiphi=k*stream*np.cos(k*phi)
    return np.column_stack((np.cos(phi)*psir-np.sin(phi)*psiphi/r,
                            np.sin(phi)*psir+np.cos(phi)*psiphi/r))


def run():
    started=time.monotonic()
    out={'started_utc':datetime.now(timezone.utc).isoformat(),
         'method':'Legendre-series interpolation, independently differentiated stream; no teammate imports',
         'scope':'Smooth canonical manufactured source interpolation only, not a coupled B2 candidate',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'center':[],'interfaces':[]}
    for beta in (2.5,3.):
        for nt in (32,40,64):
            h=nt**-1.5;length=1.5;re=float(radius(h,beta,length))
            for n in (3,5,7):
                poly=fit_cell(lambda t:(t/h)**n,0.,h,n)
                constant=float(poly(-1));exact=1/comb(2*n,n)
                row={'beta':beta,'Nt':nt,'n':n,'first_edge_r':re,
                     'endpoint_value':constant,'exact_endpoint':f'1/{comb(2*n,n)}',
                     'endpoint_absolute_error':abs(constant-exact),
                     'predicted_directional_discrepancy':8*exact,'samples':[]}
                for ratio in (.1,.01,.001,.0001):
                    r=ratio*re
                    pts=r*np.array([[1.,0.],[0.,1.],[2**-.5,2**-.5]])
                    vel=velocity(pts,poly,0.,h,beta,length)/r
                    predicted=(vel[0]+vel[1])/np.sqrt(2)
                    defect=float(np.linalg.norm(vel[2]-predicted))
                    row['samples'].append({'radius':r,'r_over_first_edge':ratio,
                         'velocity_over_r':vel.tolist(),
                         'diagonal_minus_axes_linear_map_norm':defect,
                         'discrepancy_from_limit':abs(defect-8*exact)})
                out['center'].append(row)
    for nt in (16,32,40,64):
        edges=np.linspace(0,1,nt+1)**1.5
        beta=3.;length=1.5;n=7
        for i in (1,nt//2,nt-1):
            t0=edges[i];lo=edges[i-1];hi=edges[i+1]
            hl=t0-lo;hr=hi-t0;H=max(hl,hr)
            fun=lambda t:((t-t0)/H)**n
            pl=fit_cell(fun,lo,t0,n);pr=fit_cell(fun,t0,hi,n)
            sl,dl=cell_value(pl,t0,lo,t0);sr,dr=cell_value(pr,t0,t0,hi)
            jump=float(sr-sl);exact=((hl/H)**n+(hr/H)**n)/comb(2*n,n)
            r0=float(radius(t0,beta,length))
            angle=.37
            ur_jump=-2*r0*jump*np.cos(2*angle)
            xi,weight=leggauss(96);phi=np.pi*(xi+1)
            weak=float(np.dot(np.pi*weight,(-2*r0*jump*np.cos(2*phi))*np.cos(2*phi)*r0))
            weak_exact=-2*np.pi*r0*r0*exact
            out['interfaces'].append({'Nt':nt,'n':n,'interface_index':i,'t0':float(t0),'r0':r0,
                    'h_left':float(hl),'h_right':float(hr),'S_left':float(sl),'S_right':float(sr),
                    'jump_S':jump,'exact_jump_S':exact,'jump_absolute_error':abs(jump-exact),
                    'angle':angle,'normal_velocity_jump':float(ur_jump),
                    'cos2_weighted_weak_divergence':weak,'exact_weak_divergence':weak_exact,
                    'weak_relative_error':abs(weak-weak_exact)/abs(weak_exact),
                    'note':'Normalization H fixes S size on neighboring cells; these different manufactured fields are not a fixed-function refinement study.'})
    out['ended_utc']=datetime.now(timezone.utc).isoformat();out['elapsed_seconds']=time.monotonic()-started
    destination=Path('research/37_revised_stream_interpolation/verification/manufactured.json')
    destination.write_text(json.dumps(out,indent=2)+'\n')
    print('center endpoint max absolute error',max(r['endpoint_absolute_error'] for r in out['center']))
    print('interface trace max absolute error',max(r['jump_absolute_error'] for r in out['interfaces']))
    print('weak divergence max relative error',max(r['weak_relative_error'] for r in out['interfaces']))
    for row in out['center']:
        if row['beta']==3 and row['Nt']==40 and row['n']==7:
            print('center example',json.dumps(row))
    for row in out['interfaces']:
        if row['Nt']==40 and row['interface_index']==20:print('interface example',json.dumps(row))
    print('COMPLETE seconds',out['elapsed_seconds'])


if __name__=='__main__':
    run()
