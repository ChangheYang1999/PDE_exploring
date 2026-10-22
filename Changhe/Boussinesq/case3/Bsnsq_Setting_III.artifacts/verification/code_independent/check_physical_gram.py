from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,shutil,sys
import numpy as np
from scipy.special import beta as betafn
from scipy.interpolate import BSpline
from scipy.integrate import quad_vec
from scipy.linalg import cholesky,svdvals,solve_triangular
import sympy as sp
from physical_gram import build_gram
from r2_state_values import R2State

ROOT=Path('verification');V=ROOT/'research/205_physical_gram_and_strain_norm/verification'
source=ROOT/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz'
start=time.monotonic();utc0=datetime.now(timezone.utc).isoformat();state=R2State(source)
b,L=state.bb,state.L;delta=.25;R=1.
result={'started_utc':utc0,'source_sha256':state.sha256,'geometry':{'b':b,'L':L,'Nt':state.Nt,'K':state.K,'degree':state.degree,'grade':state.grade,'nb':state.nb},'delta':delta,'R':R,'runs':[]}
previous=None
for order in [12,24,48,96]:
    g=build_gram(state.knots,state.degree,state.K,b,L,delta,R,order,True)
    h0=build_gram(state.knots,state.degree,state.K,b,L,delta,R,order,False)
    nb=state.nb
    ones=np.ones(nb)
    expected0=np.pi*L*L*((L/R)**delta*betafn(1+delta/2,1/b-delta/2)+(R/L)**delta*betafn(1-delta/2,1/b+delta/2))
    expected1=np.pi*L*L/2*((L/R)**delta*betafn(2+delta/2,1/b-delta/2)+(R/L)**delta*betafn(2-delta/2,1/b+delta/2))
    measures=[float(ones@g['blocks'][0]@ones),float(ones@g['blocks'][1]@ones),float(ones@h0['blocks'][0]@ones),float(ones@h0['blocks'][1]@ones)]
    expected=[expected0,expected1,np.pi*b*L*L,np.pi*b*b*L*L/(2*(b+1))]
    rec={k:g[k] for k in ['dual_squared','min_eigenvalue','max_eigenvalue','max_block_condition','cholesky_relative_error']}
    rec.update(order=order,analytic_norm_comparisons=[{'value':v,'expected':e,'relative_error':abs(v-e)/e} for v,e in zip(measures,expected)],unweighted_dual_squared=h0['dual_squared'])
    if previous is not None:
        rec['relative_frobenius_change']=float(np.linalg.norm(g['H']-previous['H'])/np.linalg.norm(g['H']))
        rec['largest_diagonal_scaled_entry_change']=float(np.max(np.abs(g['H']-previous['H'])/np.sqrt(np.outer(np.diag(g['H']),np.diag(g['H'])))))
        rec['dual_change']=g['dual_squared']-previous['dual_squared']
    result['runs'].append(rec);previous=g
    print(json.dumps(rec),flush=True)
# Exact/independent simple controls.
a,x,y,th=sp.symbols('a x y th', real=True)
checks={
 'angular_strain_kernel':sp.simplify(sp.sin(th)**2*sp.cos(th)-(sp.cos(th)-sp.cos(3*th))/4)==0,
 'angular_dual_integral':sp.integrate(sp.cos(th)**4*sp.sin(th)**2,(th,0,2*sp.pi))==sp.pi/8,
 'native_jacobian_b3':sp.simplify(sp.diff(L**2*((1-x)**(-6)-1),x)/2-3*L**2*(1-x)**(-7))==0,
 'unweighted_even_b3':sp.integrate((1-x),(x,0,1))==sp.Rational(1,2),
 'unweighted_odd_b3':sp.integrate((1-x)*(1-(1-x)**6),(x,0,1))==sp.Rational(3,8),
 'direction_dual_bound':g['dual_squared']<=1/(16*delta)*(1+1e-10),
 'native_active_count':len(g['active'])==state.K*state.nb-sum(k//2 for k in range(state.K)),
}
# Demonstrate norm-coordinate invariance on a noncommuting small example.
H=np.array([[4.,1.,.2],[1.,3.,.4],[.2,.4,2.]])
A=np.array([[1.,2.,-.3],[-.4,.7,1.1],[.2,-.1,.8]])
P=np.array([[2.,1.,0.],[0.,.5,.2],[0.,0.,3.]])
C=cholesky(H,lower=False);He=P.T@H@P;Ae=np.linalg.solve(P,A@P);Ce=cholesky(He,lower=False)
B=solve_triangular(C.T,(C@A).T,lower=True).T
Be=solve_triangular(Ce.T,(Ce@Ae).T,lower=True).T
sv1=svdvals(B);sv2=svdvals(Be)
checks['basis_invariance']=bool(np.max(np.abs(sv1-sv2))<1e-12)
wrong=cholesky(H,lower=True);Bw=wrong@A@np.linalg.inv(wrong)
result['basis_change_control']={'singular_values':sv1.tolist(),'changed_coordinates':sv2.tolist(),'incorrect_lower_factor':svdvals(Bw).tolist(),'max_error':float(np.max(np.abs(sv1-sv2)))}
# Independent direct physical radius+angle integration on a finite log interval.
# Four fields: actual saved G, mode0 partition unity, mode1 partition unity, and finite-space dual maximizer.
nactive=len(g['active']); vectors=np.zeros((nactive,4)); vectors[:,0]=state.rawG[g['active']];vectors[:nb,1]=1;vectors[nb:2*nb,2]=1;vectors[:,3]=g['dual_coeff']
raw=np.zeros((state.K*nb,4));raw[g['active']]=vectors
spline=BSpline(state.knots,raw.reshape(state.K,nb,4).transpose(1,0,2).reshape(nb,-1),state.degree,extrapolate=False)
phis=np.arange(128)*2*np.pi/128;cosines=np.cos(np.outer(phis,np.arange(state.K)));angular_kernel=-np.sin(phis)**2*np.cos(phis)/np.pi
lo=-50.;hi=180.
def physical_integrand(logr):
    r=np.exp(logr); lz=-np.log1p((r/L)**2)/(2*b); tt=-np.expm1(lz)
    rad=spline(tt).reshape(state.K,4)*np.exp((b+1)*lz)
    rad[1::2]*=r/np.hypot(r,L)
    vals=cosines@rad
    w=np.exp(delta*(logr-np.log(R)))+np.exp(-delta*(logr-np.log(R)))
    norms=np.mean(vals*vals,axis=0)*2*np.pi*w*r*r
    strains=np.mean(angular_kernel[:,None]*vals,axis=0)*2*np.pi*r
    return np.r_[norms,strains]
integral,error,info=quad_vec(physical_integrand,lo,hi,epsabs=2e-11,epsrel=2e-11,full_output=True,limit=2000,points=[-12,-8,-5,-3,-1,0,1,2,3,5,8,12,20,35,60,100])
expected_norm=np.einsum('ij,ij->j',vectors,g['H']@vectors);expected_c=g['q']@vectors
M=np.sum(np.max(np.abs(raw.reshape(state.K,nb,4)),axis=1),axis=0)
rlo=np.exp(lo);rhi=np.exp(hi)
outer=2*np.pi*M*M*L**(2+2/b)*(R**(-delta)*rhi**(delta-2/b)/(2/b-delta)+R**delta*rhi**(-delta-2/b)/(delta+2/b))
inner=2*np.pi*M*M*(R**(-delta)*rlo**(2+delta)/(2+delta)+R**delta*rlo**(2-delta)/(2-delta))
result['physical_quadrature']={'log_interval':[lo,hi],'angular_nodes':128,'success':bool(info.success),'status':int(info.status),'message':info.message,'error_estimate':float(error),'neval':int(info.neval),'direct_norms':integral[:4].tolist(),'gram_norms':expected_norm.tolist(),'norm_absolute_differences':np.abs(integral[:4]-expected_norm).tolist(),'norm_relative_differences':(np.abs(integral[:4]-expected_norm)/expected_norm).tolist(),'direct_strains':integral[4:].tolist(),'exact_strain_rows':expected_c.tolist(),'strain_absolute_differences':np.abs(integral[4:]-expected_c).tolist(),'outer_norm_majorants':outer.tolist(),'inner_norm_majorants':inner.tolist(),'coefficient_majorants':M.tolist()}
checks['physical_quadrature_success']=bool(info.success)
checks['norm_controls']=bool(max(v['relative_error'] for rec in result['runs'] for v in rec['analytic_norm_comparisons'])<2e-9)
# Tail moment may converge more slowly for the dual field, use its recorded explicit truncation majorants instead of claiming exact infinity quadrature.
np.savez_compressed(V/'native_gram.npz',H=g['H'],H0=h0['H'],q=g['q'],dual_coeff=g['dual_coeff'],active=g['active'],beta_basis=b,L=L,delta=delta,R=R,knots=state.knots,degree=state.degree,K=state.K)
result['checks']=checks;result['ended_utc']=datetime.now(timezone.utc).isoformat();result['elapsed_seconds']=time.monotonic()-start
result['input_hashes']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,ROOT/'code_independent/physical_gram.py',ROOT/'code_independent/check_physical_gram.py',ROOT/'code_independent/r2_state_values.py',ROOT/'research/205_physical_gram_and_strain_norm/PROOF.md']}
(V/'gram_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_checks':checks,'elapsed_seconds':result['elapsed_seconds'],'physical':result['physical_quadrature']},indent=2),flush=True)
assert all(checks.values()),checks
