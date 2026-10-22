"""Exact last-span polynomial versus derivative controls; independent floating source integral."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math,importlib.util,time
import numpy as np
from numpy.polynomial.legendre import leggauss
B=Path(__file__).resolve().parents[3];D=B/'research/x3_tail_fit_conditioning';C=B/'research/x3_closure_diagnostics'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();v=load(D/'evidence/diagnostic.json');pins=dict(v['files'])
for n,h in pins.items():need(sha(B/n)==h,'diagnostic pin')
xj=load(B/'data_exact/x3.json');ints=xj['integers'];degree=ints['spline_order'];need(degree==7 and ints['degree']==375 and ints['angular']==200,'polynomial degree and coefficient-count conventions');t=[F.from_float(float.fromhex(z)) for z in xj['spline_knots_hex']];z=[F.from_float(float.fromhex(h)) for h in xj['z_hex']];nc=ints['degree']+1;nm=ints['angular']+1
need(len(t)==nc+degree+1 and t[:degree+1]==[F(0)]*(degree+1) and t[-degree-1:]==[F(1)]*(degree+1) and t[nc-1]<1,'clamped end knots');co=[[F(0)]+z[1+j*ints['degree']:1+(j+1)*ints['degree']] for j in range(nm)]
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul_lin(a,c0,c1):
 out=[F(0)]*(len(a)+1)
 for j,y in enumerate(a):out[j]+=c0*y;out[j+1]+=c1*y
 return out
polys=[];denchecks=0
for row in co:
 i=nc-1;dd=[[x] for x in row[i-degree:i+1]]
 for ell in range(1,degree+1):
  for j in range(degree,ell-1,-1):
   ix=i-degree+j;den=t[ix+degree-ell+1]-t[ix];need(den>0,'positive last-span denominator');denchecks+=1;c0=(1-t[ix])/den;c1=1/den;dd[j]=add(mul_lin(dd[j-1],1-c0,-c1),mul_lin(dd[j],c0,c1))
 need(len(dd[-1])==degree+1,'complete polynomial degree');polys.append(dd[-1])
for j in range(nm):
 for nu in range(3):need(polys[j][nu]*math.factorial(nu)==F(v['endpoint_exact_ratios'][nu][j]),'independent exact endpoint coefficient')
exactout={'utc':datetime.now(timezone.utc).isoformat(),'coordinate':'delta=q-1','angular_modes':list(range(nm)),'polynomial_coefficients':[[str(z) for z in row] for row in polys]}
with (D/'data_exact/last_span_polynomials.json').open('x') as f:json.dump(exactout,f,indent=1);f.write('\n')
cc=np.array([[float(z) for z in row] for row in polys]);ccder=cc[:,1:]*np.arange(1,degree+1);k=float(z[0]) if False else float(F.from_float(float.fromhex(xj['scalars_hex']['k'])));L=float.fromhex(xj['scalars_hex']['L']);r0=float.fromhex(xj['scalars_hex']['origin_radius']);p=6+2*k/(2-k);a=1-k;mm=np.arange(nm);jm=np.maximum(mm-1,0);tc=np.array([float.fromhex(h) for h in xj['z_hex'][-ints['singular']:]]);modes=np.array(v['modes'])
def poly(co,delta):
 val=np.zeros((len(delta),len(co)))
 for j in range(co.shape[1]-1,-1,-1):val=val*delta[:,None]+co[:,j]
 return val
def independent_source(rr,nt):
 u=rr/L;w=u**(-2);delta=-np.exp(-a/2*np.log1p(u*u));need(np.all(1+delta>=float(t[nc-1])),'all samples in last spline span');qt=-a*delta/(1+w);bs=poly(cc,delta);bd=poly(ccder,delta);chi=1/(1+r0*r0*w);mult=chi[:,None]**jm;bm=bs*mult;bmt=(bd*qt[:,None]+bs*2*jm[None,:]*r0*r0*w[:,None]/(1+r0*r0*w[:,None]))*mult;T=np.polynomial.chebyshev.chebval(1+2*delta,tc);Tp=np.polynomial.chebyshev.chebval(1+2*delta,np.polynomial.chebyshev.chebder(tc));rad=(1+w)**(-p/2);sg=rad*T;sgt=p*w/(1+w)*sg+rad*2*Tp*qt
 th=np.linspace(0,np.pi/2,nt+1);ct=np.cos(th);st=np.sin(th);g=np.abs(ct)**(p-2)*st**2;cosm=np.cos(2*mm[:,None]*th);hh=(k-3)/2*np.log1p(w[:,None])+bm@cosm+sg[:,None]*g;density=L**3*u[:,None]**k*(ct**2*st)[None,:]*np.exp(hh);ht=k-(k-3)*w/(1+w);rhot=density*(ht[:,None]+bmt@cosm+sgt[:,None]*g)
 weights=np.full(nt+1,np.pi/(2*nt));weights[[0,-1]]*=.5;sin=np.sin(2*th[:,None]*modes);cos=np.cos(2*th[:,None]*modes);val=rhot@(weights[:,None]*ct[:,None]*sin)+density@(weights[:,None]*(ct[:,None]*sin+2*modes[None,:]*st[:,None]*cos));return 4/(np.pi*rr[:,None])*val
rr=[];labels=[]
for name in ['base','td05','td20','ext1e11']:
 s=load(C/'sources/lead'/f'{name}.json');td={'td05':.5,'td20':2.}.get(name,1.)
 for pos in [0.,.5,1.]:rr.append(s['rmax']/10**(td*(1-pos)));labels.append([name,pos])
rr=np.array(rr);runs=[]
for nt in [4096,8192]:runs.append(independent_source(rr,nt))
spec=importlib.util.spec_from_file_location('diag_x3',D/'sources/x3_independent.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);x=mod.X3(B/'data_exact/x3.json');z,wg=leggauss(768);th=(z+1)*np.pi/4;wg=wg*np.pi/4;ref=x.polar(rr,th)['rho_x']@(4/np.pi*wg[:,None]*np.sin(2*th[:,None]*modes));scale=np.maximum(np.abs(ref),1e-290);dif=np.abs(runs[-1]-ref)/scale;need(np.all(np.isfinite(dif)),'finite source comparison');need(float(np.max(dif))<1e-7,'diagnostic source representations agree to stated tolerance')
for n,h in pins.items():need(sha(B/n)==h,'unchanged diagnostic pins')
for pp in [Path(__file__),D/'INDEPENDENT_CHECK_PROOF.md',D/'evidence/diagnostic.json',D/'evidence/diagnostic_v2.log',D/'data_exact/last_span_polynomials.json']:pins[str(pp.relative_to(B))]=sha(pp)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_LAST_SPAN_POLYNOMIAL_AND_FLOATING_SOURCE_DIAGNOSTIC','exact_endpoint_checks':3*nm,'positive_deboor_denominator_checks':denchecks,'complete_exact_polynomial_coefficients':nm*(degree+1),'modes':modes.tolist(),'radius_labels':labels,'radii':rr.tolist(),'source_deboor_Gauss768':ref.tolist(),'source_exactpoly_trapezoid4096':runs[0].tolist(),'source_exactpoly_trapezoid8192':runs[1].tolist(),'max_relative_source_difference_display':float(np.max(dif)),'max_relative_trapezoid_difference_display':float(np.max(np.abs(runs[1]-runs[0])/scale)),'source_scalar_comparisons':len(rr)*len(modes),'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'603 exact endpoint equalities and1608 exact last-span coefficients;60 floating source comparisons with different density representation and angular rule. No rigorous quadrature, fit error, physical residual or endpoint.'}
with (D/'evidence/independent_check.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','seconds','exact_endpoint_checks','complete_exact_polynomial_coefficients','source_scalar_comparisons','max_relative_source_difference_display','max_relative_trapezoid_difference_display']},indent=2))
