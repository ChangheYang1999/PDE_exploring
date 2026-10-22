"""Independent far coefficients and source quadrature; floating diagnostics, no residual enclosure."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,math,time,importlib.util
import numpy as np
from scipy.linalg import lstsq,svdvals
from numpy.polynomial.legendre import leggauss
B=Path(__file__).resolve().parents[3];D=B/'research/x3_tail_fit_conditioning';C=B/'research/x3_closure_diagnostics'
def need(x,s):
 if not x:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();manifest=load(D/'data_exact/manifest.json');pins=dict(manifest['files'])
for n,h in pins.items():need(sha(B/n)==h,'input pin')
spec=importlib.util.spec_from_file_location('independent_x3',D/'sources/x3_independent.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);x=mod.X3(B/'data_exact/x3.json');modes=np.array(manifest['modes']);orders=manifest['angular_rules'];a=1-x.k;d=np.array([0,a,2*a,2.]);powers=x.k-1-d
# Endpoint derivatives through differentiated control coefficients, evaluated by de Boor.
kn=x.t.copy();co=x.co.copy();degree=x.spline_order;end=[]
for nu in range(3):
 end.append(x.deboor([1.],kn,co,degree)[0]);den=kn[degree+1:-1]-kn[1:-degree-1];need(np.all(den>0),'differentiated spline denominators');co=degree*np.diff(co,axis=0)/den[:,None];kn=kn[1:-1];degree-=1
endpoint=np.array(end)
# Exact endpoint values by clamped endpoint identities, independent rational control differences.
kt=[F.from_float(float(z)) for z in x.t];cc=[[F.from_float(float(z)) for z in row] for row in x.co[-3:]];p=x.spline_order;last=len(x.co)-1
exact0=cc[-1];exact1=[p*(c-b)/(kt[last+p]-kt[last]) for b,c in zip(cc[-2],cc[-1])]
previous1=[p*(b-aa)/(kt[last-1+p]-kt[last-1]) for aa,b in zip(cc[-3],cc[-2])]
exact2=[(p-1)*(b-aa)/(kt[last+p-1]-kt[last]) for aa,b in zip(previous1,exact1)]
exact=np.array([[float(z) for z in row] for row in [exact0,exact1,exact2]])
errors=np.abs(endpoint-exact);scales=np.maximum(np.abs(exact),1);need(np.all(np.isfinite(errors)),'finite endpoint diagnostic');endpoint=exact.copy() # rounded exact clamped formulas avoid floating second-difference cancellation
tc=[np.polynomial.chebyshev.chebval(1.,np.polynomial.chebyshev.chebder(x.tc,m=i)) for i in range(3)]
def coeff(theta):
 ct=np.cos(theta);st=np.sin(theta);cosm=np.cos(2*x.m[:,None]*theta);g=np.abs(ct)**(x.p-2)*st**2
 h00=endpoint[0]@cosm+tc[0]*g;h10=-endpoint[1]@cosm-2*tc[1]*g;h20=.5*endpoint[2]@cosm+2*tc[2]*g;h01=(x.k-3)/2-x.origin_radius**2*(x.powers*endpoint[0])@cosm-x.p/2*tc[0]*g
 c00=ct**2*st*np.exp(h00);return np.array([c00,c00*h10,c00*(h20+.5*h10*h10),c00*h01])
def angular_integrals(theta,weights):
 cs=coeff(theta);ct=np.cos(theta);st=np.sin(theta);si=np.sin(2*modes[:,None]*theta);co=np.cos(2*modes[:,None]*theta)
 kernel=(x.k-d[:,None,None]+1)*ct[None,None,:]*si[None,:,:]+2*modes[None,:,None]*st[None,None,:]*co[None,:,:]
 return 4/np.pi*np.sum(cs[:,None,:]*kernel*weights[None,None,:],axis=2)
angular=[]
for order in orders:
 z,w=leggauss(order);th=(z+1)*np.pi/4;ww=w*np.pi/4;val=angular_integrals(th,ww);angular.append({'method':'Gauss-Legendre','order':order,'e_jl_n':val.tolist()})
# A genuinely different angular rule for the analytic expressions.
th=np.linspace(0,np.pi/2,8193);ww=np.full(len(th),np.pi/(2*8192));ww[[0,-1]]*=.5;trap=angular_integrals(th,ww);angular.append({'method':'composite_trapezoid','intervals':8192,'e_jl_n':trap.tolist()})
ref=np.array(angular[1]['e_jl_n']);z,w=leggauss(manifest['fit_source_angular_rule']);th=(z+1)*np.pi/4;ww=w*np.pi/4;projection=4/np.pi*ww[:,None]*np.sin(2*th[:,None]*modes)
def source(rr):
 vals=[]
 for off in range(0,len(rr),256):vals.append(x.polar(rr[off:off+256],th)['rho_x']@projection)
 return np.concatenate(vals,axis=0)
records=[];fitmom={}
for name in manifest['fit_cases']:
 saved=load(C/'sources/lead'/f'{name}.json');grid=np.exp(np.linspace(np.log(saved['rmin']),np.log(saved['rmax']),saved['Nr']));R=grid[-1];td={'td05':.5,'td20':2.}.get(name,1.);rr=grid[grid>=R/10**td];f=source(rr);q=powers[:1] if name=='tp_lead' else powers
 X=(rr[:,None]/R)**q[None,:];A,res,rank,s=lstsq(X,f,cond=None,lapack_driver='gelsy');sv=svdvals(X);need(rank==len(q),'full rank floating design');desired=x.L**2*(R/x.L)**q[:,None]*ref[:len(q),:];fit=X@A
 rel=np.max(np.abs(fit-f),axis=0)/np.max(np.abs(f),axis=0);mom=.5*float(np.sum(A[:,0]/(-q)));fitmom[name]=mom
 records.append({'name':name,'reconstructed_radius_count':len(rr),'outer_radius':float(R),'fit_decades':td,'powers':q.tolist(),'design_singular_values':sv.tolist(),'design_condition_display':float(sv[0]/sv[-1]),'QR_rank':int(rank),'fitted_coefficients':A.tolist(),'analytic_asymptotic_coefficients_display':desired.tolist(),'absolute_coefficient_differences':np.abs(A-desired).tolist(),'coefficient_relative_differences':((A-desired)/desired).tolist(),'max_relative_fit_residual_per_mode':rel.tolist(),'fitted_exterior_c_moment':mom,'saved_c':saved['c'],'saved_c_minus_baseline':saved['c']-load(C/'sources/lead/base.json')['c']})
# Extend to the same reference radius before comparing moments across outer extents.
base=load(C/'sources/lead/base.json');ext=load(C/'sources/lead/ext1e11.json');ann=[]
for order in [64,128]:
 z,w=leggauss(order);lo,hi=np.log(base['rmax']),np.log(ext['rmax']);tt=(lo+hi)/2+(hi-lo)*z/2;moment=(hi-lo)/4*np.dot(w,source(np.exp(tt))[:,0]);ann.append({'log_radial_gauss_order':order,'half_integral_mode1_source_over_r':float(moment),'extension_moment_at_base_radius':float(moment+fitmom['ext1e11']),'difference_from_baseline_fitted_moment':float(moment+fitmom['ext1e11']-fitmom['base'])})
changes={n:(z-fitmom['base']) for n,z in fitmom.items() if n!='ext1e11'};changes['tp_none']=-fitmom['base'];changes['ext1e11_at_baseline_radius']=ann[-1]['difference_from_baseline_fitted_moment']
for n,h in pins.items():need(sha(B/n)==h,'unchanged source pin')
for p in [Path(__file__),D/'data_exact/manifest.json',D/'code/diagnose.py',D/'evidence/diagnostic.log']:pins[str(p.relative_to(B))]=sha(p)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'FLOATING_DIAGNOSTICS_ONLY_REQUIRES_REVIEW','modes':modes.tolist(),'powers':powers.tolist(),'endpoint_derivative_scaled_max_difference_from_exact':float(np.max(errors/scales)),'endpoint_derivative_max_abs_differences':np.max(errors,axis=1).tolist(),'exact_endpoint_formula_checks':3*(x.angular+1),'endpoint_exact_ratios':[[str(z) for z in row] for row in [exact0,exact1,exact2]],'angular':angular,'angular_max_abs_rule_differences':[float(np.max(np.abs(np.array(v['e_jl_n'])-ref))) for v in angular],'fits':records,'annulus_moments':ann,'predicted_change_c_at_common_reference':changes,'ulp_of_saved_c':math.ulp(base['c']),'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Own exact-JSON evaluator, two Gauss rules plus trapezoid for asymptotic coefficients, Gauss source quadrature and QR fits. All integration, fits and condition numbers are floating diagnostics. Reconstructed logarithmic radii from saved endpoints are not attested original arrays. No rigorous tail error, physical extrema or IPM endpoint.'}
with (D/'evidence/diagnostic.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'seconds':out['seconds'],'endpoint_scaled_difference':out['endpoint_derivative_scaled_max_difference_from_exact'],'angular_rule_differences':out['angular_max_abs_rule_differences'],'condition_numbers':[(v['name'],v['design_condition_display']) for v in records],'predicted_changes':changes,'ulp_c':out['ulp_of_saved_c']},indent=2))
