"""Independent exact, real-FD, physical-integral and inverse controls of134."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares
import argparse,json,time
import numpy as np
from free_beta_stream import make_chart,grid
from joint_primitive_chart import JointPrimitiveProblem,FreeBetaJointPrimitive,serialize_coefficients,JET_KEYS,EXTRA_TERMS
from constrained_primitive_certificate import certificate,jet_from_state
from exact_bivariate import ordinary_stream_jet
from stream_basis import combine,derivative,evaluate_terms
from finite_difference import derivative as fd
from cartesian_inverse import CartesianInverse,InverseSettings

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True)
tic=time.perf_counter();rng=np.random.default_rng(1342026);rows=[]
points=np.array([[0.,0.],[0.,.41],[0.,-.31],[.23,.4],[.57,-.29],[1.8,1.4],[4.1,-2.2]])
for beta,a0 in [(2.25,1.),(3.,-2.),(4.5,1.)]:
    b=make_chart(beta,4,4,a0=a0);p=JointPrimitiveProblem(b,points,beta,32,1e-5);z=rng.normal(scale=.007,size=p.size)
    v,J=p.chart.parameters(z,True);h=1e-5;Jfd=np.zeros_like(J);JR=p.jacobian(z);JRfd=np.zeros_like(JR)
    for j in range(len(z)):
        d=np.zeros_like(z);d[j]=h
        Jfd[:,j]=(-p.chart.parameters(z+2*d)+8*p.chart.parameters(z+d)-8*p.chart.parameters(z-d)+p.chart.parameters(z-2*d))/(12*h)
        JRfd[:,j]=(-p.residual(z+2*d)+8*p.residual(z+d)-8*p.residual(z-d)+p.residual(z-2*d))/(12*h)
    ej=float(abs(J-Jfd).max()/(1+abs(J).max()));er=float(abs(JR-JRfd).max()/(1+abs(JR).max()));assert ej<1e-8 and er<2e-7,(beta,ej,er)
    C,K=p.coefficients(z);rb,rC,extra,_=serialize_coefficients(beta,b.labels,p.chart.raw_coefficients(z),str(a0))
    state={'beta':rb,'a0':str(a0),'labels':b.labels,'C':rC,'ni':4,'nj':4,'shifts':[0,1],'extra_stream_terms':extra}
    path=root/f'beta{beta}_a{a0}_state.json';path.write_text(json.dumps(state,indent=2)+'\n');cert=certificate(path)
    assert cert['center_exact']and cert['through_degree4_zero']and cert['leading_moments_exact_zero'],cert
    psiE,_=ordinary_stream_jet(Q(rb),b.labels,list(map(Q,rC)),[Q(0)]*len(rC),8)
    exact_jet=np.array([float(psiE.get(k,0))for k in JET_KEYS]);matrix_error=float(abs(p.chart.jet@C-exact_jet).max());assert matrix_error<2e-10,(beta,matrix_error)
    actualC=np.array(list(map(lambda c:float(Q(c)),rC)));actualK=np.array([float(Q(t['coefficient']))for t in extra]);serialization_error=max(abs(actualC-C).max(),abs(actualK-K).max());assert serialization_error<2e-10,(beta,serialization_error)
    bad=dict(state);bad['extra_stream_terms']=[dict(t)for t in extra];bad['extra_stream_terms'][0]['coefficient']=str(Q(extra[0]['coefficient'])+Q(1,1000));badpath=root/f'beta{beta}_tampered.json';badpath.write_text(json.dumps(bad)+'\n');tamper=certificate(badpath);assert not tamper['through_degree4_zero']and tamper['center_exact']and tamper['leading_moments_exact_zero']
    # Completely compressed Cartesian functions and different, linear quadrature.
    terms=combine(*([(c,row['Psi'])for c,row in zip(C,b.psi)]+[(c,row)for c,row in zip(K,EXTRA_TERMS)]));s=1/beta
    px=derivative(terms,0,s);py=derivative(terms,1,s);om=combine((-1,derivative(px,0,s)),(-1,derivative(py,1,s)));ox=derivative(om,0,s);oy=derivative(om,1,s)
    ev=lambda ts,x,y:evaluate_terms(ts,x,y,s);v0=np.array([-float(ev(py,0.,0.)),float(ev(px,0.,0.))])
    def velocity(pts):
        x,y=np.asarray(pts).T;return np.column_stack((-ev(py,x,y),ev(px,x,y)))-v0
    def omega(x,y):return ev(om,x,y)
    def source(x,y):return(beta*x-ev(py,x,y)-v0[0])*ev(ox,x,y)+(beta*y+ev(px,x,y)-v0[1])*ev(oy,x,y)+ev(om,x,y)
    nodes,weights=leggauss(64);nodes=(nodes+1)/2;weights=weights/2
    def theta(x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));shape=x.shape;xx=x.ravel()[:,None]*nodes;yy=np.broadcast_to(y.ravel()[:,None],xx.shape)
        return (x.ravel()*np.sum(source(xx,yy)*weights,axis=1)).reshape(shape)
    pp=points[3:6];expected=velocity(pp);inverse=[]
    for radius in [8.,12.,18.]:
        inv=CartesianInverse(omega,InverseSettings(radius=radius,core_radial_order=16,core_angular_order=32,exterior_radial_order=40,exterior_angular_order=48,decay_power=s));got=inv.relative(pp);ie=float(abs(got-expected).max());assert ie<3e-7,(beta,radius,ie);inverse.append({'core_radius':radius,'error':ie})
    target=p.inner.fields(p.chart.parameters(z))['RF'][3:6]*pp[:,0]**2
    spatial=[]
    for hh in [2e-4,1e-4]:
        tx=fd(theta,pp,0,hh,radius=3);ty=fd(theta,pp,1,hh,radius=3);W=beta*pp+got;th=theta(*pp.T)
        rt=W[:,0]*tx+W[:,1]*ty-(beta-2)*th;qe=float(abs(tx-source(*pp.T)).max());te=float(abs(rt-target).max());assert qe<3e-7 and te<3e-7,(beta,qe,te)
        spatial.append({'h':hh,'actual_primitive_x_error':qe,'thermal_error_vs_divided_generator':te})
    # Free-beta class is tested on its a0=1 chart, including every beta-dependent map.
    fb=FreeBetaJointPrimitive(4,4,points,beta,32,1e-5);zz=np.r_[beta,z];jb=fb.jacobian(zz)[:,0];hh=3e-5;unit=np.r_[hh,np.zeros(len(z))]
    truth=(-fb.residual(zz+2*unit)+8*fb.residual(zz+unit)-8*fb.residual(zz-unit)+fb.residual(zz-2*unit))/(12*hh)
    eb=float(abs(jb-truth).max()/(1+abs(truth).max()));assert eb<5e-7,(beta,eb)
    rows.append({'beta':beta,'a0':a0,'parameter_jacobian_error':ej,'residual_jacobian_error':er,'beta_jacobian_error':eb,'ordinary_jet_matrix_error':matrix_error,'serialization_error':float(serialization_error),'exact_center':True,'exact_moments':True,'degree4_zero':True,'tamper_detected':True,'inverse':inverse,'spatial':spatial})
b=make_chart(3.,4,4);pp=grid(np.geomspace(.13,4.,11),np.linspace(0,np.pi,11));p=JointPrimitiveProblem(b,pp,3.,32)
base=rng.normal(scale=.003,size=p.size);directions=rng.normal(scale=.006,size=(p.size,2));truth=np.array([.13,-.19]);forcing=p.residual(base+directions@truth)
fit=least_squares(lambda v:p.residual(base+directions@v)-forcing,np.zeros(2),jac=lambda v:p.jacobian(base+directions@v)@directions,gtol=1e-12,ftol=1e-12,xtol=1e-12,max_nfev=40);re=float(abs(fit.x-truth).max());assert re<2e-8,re
out={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'cases':rows,'manufactured_recovery_error':re,'scope':'Finite implementation controls only, no unforced profile and no nearby-profile error bound.'}
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['elapsed_seconds'],flush=True)
