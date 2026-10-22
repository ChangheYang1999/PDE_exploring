"""Independent Jacobian and exact-serialization controls of the130 graph."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import argparse,json,time
import numpy as np
from scipy.optimize import least_squares
from tail_compatible_primitive import TailChart,TailPrimitiveProblem,FreeBetaTailPrimitive,exact_serialized_coefficients
from free_beta_stream import make_chart,grid
from primitive_tail_moments import data
from primitive_center_certificate import residual_from_jet
from exact_bivariate import ordinary_stream_jet

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True)
tic=time.perf_counter();rng=np.random.default_rng(1305);rows=[]
points=np.array([[0.,0.],[0.,.41],[0.,-.31],[.23,.4],[.57,-.29],[1.8,1.4],[4.1,-2.2]])
for beta in [2.25,3.,4.5]:
    b=make_chart(beta,4,4);p=TailPrimitiveProblem(b,points,beta,32,1e-5);z=rng.normal(scale=.013,size=p.size)
    # Five-point differences of the complete map and residual, not its pieces.
    v,J=p.chart.parameters(z,True);h=1e-5;Jfd=np.zeros_like(J);R=p.residual(z);JR=p.jacobian(z);JRfd=np.zeros_like(JR)
    for k in range(len(z)):
        d=np.zeros_like(z);d[k]=h
        Jfd[:,k]=(-p.chart.parameters(z+2*d)+8*p.chart.parameters(z+d)-8*p.chart.parameters(z-d)+p.chart.parameters(z-2*d))/(12*h)
        JRfd[:,k]=(-p.residual(z+2*d)+8*p.residual(z+d)-8*p.residual(z-d)+p.residual(z-2*d))/(12*h)
    ej=float(np.max(abs(J-Jfd))/(1+abs(J).max()));er=float(np.max(abs(JR-JRfd))/(1+abs(JR).max()));assert ej<1e-8 and er<1e-7,(beta,ej,er)
    C=p.coefficients(z);rb,rC,_=exact_serialized_coefficients(beta,b.labels,p.chart.raw_coefficients(z));exact=data(rb,b.labels,rC);assert exact['C_plus']==exact['C_minus']==0
    actual=np.array(list(map(lambda c:float(Q(c)),rC)));e=float(abs(actual-C).max());assert e<1e-10,(beta,e)
    psi,_=ordinary_stream_jet(Q(rb),b.labels,list(map(Q,rC)),[Q(0)]*len(rC),8);cent=residual_from_jet(Q(rb),psi)
    assert cent['strain']==1+Q(rb)/2 and cent['omega_x']==4/Q(rb) and cent['a0']==1
    # Every allowed coefficient field can be projected back to the chosen complement.
    # Recover its complement coordinates directly, since the two graph directions
    # only use degrees<=3,j<=1 and have known nonzero pivot entries.
    i0=b.labels.index((3,0,0));i1=b.labels.index((2,1,0));h0=p.chart.d0;h1=p.chart.d1
    complement=C-(C[i0]/h0[i0])*h0-(C[i1]/h1[i1])*h1
    recovered=complement[p.chart.free];assert np.max(abs(p.coefficients(recovered)-C))<1e-11
    fb=FreeBetaTailPrimitive(4,4,points,beta,32,1e-5);zz=np.r_[beta,z];jb=fb.jacobian(zz)[:,0];hh=3e-5
    target=(-fb.residual(zz+np.r_[2*hh,np.zeros(len(z))])+8*fb.residual(zz+np.r_[hh,np.zeros(len(z))])-8*fb.residual(zz-np.r_[hh,np.zeros(len(z))])+fb.residual(zz-np.r_[2*hh,np.zeros(len(z))]))/(12*hh)
    eb=float(np.max(abs(jb-target))/(1+abs(target).max()));assert eb<3e-7,(beta,eb)
    rows.append({'beta':beta,'parameter_jacobian_relative_error':ej,'residual_jacobian_relative_error':er,'beta_jacobian_relative_error':eb,'exact_serialization_max_change':e,'exact_center':True,'exact_moments_zero':True,'complement_surjective_control':True})
# Manufactured forcing within a two-dimensional slice of the repaired chart.
b=make_chart(3.,4,4);pts=grid(np.geomspace(.13,4.,11),np.linspace(0,np.pi,11));p=TailPrimitiveProblem(b,pts,3.,32)
base=rng.normal(scale=.004,size=p.size);direction=rng.normal(scale=.01,size=(p.size,2));truth=np.array([.13,-.19]);forcing=p.residual(base+direction@truth)
fit=least_squares(lambda z:p.residual(base+direction@z)-forcing,np.zeros(2),jac=lambda z:p.jacobian(base+direction@z)@direction,gtol=1e-12,ftol=1e-12,xtol=1e-12,max_nfev=40)
assert np.max(abs(fit.x-truth))<1e-8
r={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'cases':rows,'manufactured_forcing_recovery_error':float(abs(fit.x-truth).max()),'scope':'Implementation controls only; the manufactured forcing is not the unforced B2 equation.'}
(root/'tests.json').write_text(json.dumps(r,indent=2)+'\n');print(r['status'],r['elapsed_seconds'],flush=True)
