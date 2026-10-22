"""Joint primitive pilot with exact center jets and two leading tail moments.

This file runs only this lane's implementations. It never imports NUM code.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse,hashlib,json,time
import numpy as np
from scipy.optimize import least_squares
from free_beta_stream import make_chart,grid
from horizontal_primitive_stream import PrimitiveProblem
from joint_primitive_chart import JointChart,JointPrimitiveProblem,FreeBetaJointPrimitive,serialize_coefficients,stream_row,EXTRA_TERMS
from constrained_primitive_certificate import certificate
from primitive_tail_moments import data,serialized

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--max-nfev',type=int,default=90);ap.add_argument('--limit-states',type=int,default=0);args=ap.parse_args()
root=args.root;root.mkdir(exist_ok=True)
controls=[Path('verification/joint_primitive_controls_20261021T0615Z/tests.json'),Path('verification/tail_chart_controls_20261021T0550Z/tests.json'),Path('verification/primitive128_controls_20261021T0530Z/tests.json')]
for p in controls:
    if json.loads(p.read_text()).get('status')!='ALL_CONTROLS_PASSED':raise RuntimeError(str(p)+' has no passing controls')
start=time.perf_counter();rng=np.random.default_rng(1342026)
summary={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'controls_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in controls},'states':[],
 'scope':'Finite polynomial angular tail subspace only. Two exact rational leading moments, center constraints and thermal Taylor coefficients through degree4 are enforced; no full thermal PDE guarantee. Levels change fit domain and resolution together, so this pilot is not an isolated convergence study. No automatic YES. Finite primitive quadrature needs independent differentiation.'}
def save():
    summary['elapsed_seconds']=time.perf_counter()-start;(root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
levels=[(4,4,10.,13,13),(5,5,30.,17,17),(6,6,100.,21,21)]
for free in [False,True]:
  for seed,initial_beta in enumerate([2.25,2.75,3.5]):
    previous=None;beta=initial_beta
    for ni,nj,rmax,nr,na in levels:
      label=f'{"free"if free else"fixed"}_s{seed}_b{initial_beta}_n{ni}_J{nj}'
      points=grid(np.geomspace(.025,rmax,nr),np.linspace(0,np.pi,na));basis=make_chart(beta,ni,nj);chart=JointChart(basis)
      if previous is None:z=rng.normal(scale=[0.,.013,.05][seed],size=chart.size)
      else:
        old=dict(zip(map(tuple,previous['labels']),previous['C']));C=np.array([old.get(l,0.)for l in basis.labels])
        # Project the previously repaired field to the complement before embedding.
        i0=basis.labels.index((3,0,0));i1=basis.labels.index((2,1,0))
        C=C-(C[i0]/chart.tail.d0[i0])*chart.tail.d0-(C[i1]/chart.tail.d1[i1])*chart.tail.d1;z=C[chart.tail.free]
      problem=FreeBetaJointPrimitive(ni,nj,points,initial_beta,32,1e-7)if free else JointPrimitiveProblem(basis,points,initial_beta,32,1e-7)
      initial=np.r_[beta,z]if free else z;calls=[0];tic=time.perf_counter();history=[]
      def fun(v):
        r=problem.residual(v);calls[0]+=1
        row={'call':calls[0],'seconds':time.perf_counter()-tic,'objective_norm':float(np.linalg.norm(r)),'beta':float(v[0])if free else beta};history.append(row)
        if calls[0]==1 or calls[0]%10==0:print(label,row,flush=True)
        return r
      lower=np.r_[2.05,np.full(len(z),-np.inf)]if free else -np.inf;upper=np.r_[5.,np.full(len(z),np.inf)]if free else np.inf
      fit=least_squares(fun,initial,jac=problem.jacobian,bounds=(lower,upper),max_nfev=args.max_nfev,xtol=1e-9,ftol=1e-9,gtol=1e-9,x_scale='jac')
      if free:beta=float(fit.x[0]);z=fit.x[1:];case=problem.case(beta);basis=case.basis
      else:z=fit.x;case=problem
      C,K=case.coefficients(z);ratbeta,ratC,extra,repair_detail=serialize_coefficients(beta,basis.labels,case.chart.raw_coefficients(z));storedC=np.array([float(Q(v))for v in ratC]);storedK=np.array([float(Q(v['coefficient']))for v in extra]);tail=data(ratbeta,basis.labels,ratC)
      assert tail['C_plus']==tail['C_minus']==0
      state={'schema':'independent_horizontal_primitive_stream_v1','variant':'joint_center_tail_chart134','extra_stream_terms':extra,'beta':ratbeta,'a0':'1','labels':list(map(list,basis.labels)),'C':ratC,'ni':ni,'nj':nj,'shifts':[0,1],
       'temperature':'Theta(x,y)=integral_0^x[(beta X+grad_perp Psi-grad_perp Psi(0)).grad(-Delta Psi)-Delta Psi](u,y) du',
       'stream_basis':'x R^(1-1/beta-shift) T_i(2R^(-1/beta)-1) T_j(y/R), R=sqrt(1+x^2+y^2), relative linear stream gauge',
       'coefficient_rounding_correction_max':float(abs(storedC-C).max()),'extra_rounding_correction_max':float(abs(storedK-K).max()),'fit_quadrature_order':32,'fit_quadrature_rule':'sinh','free_beta':free,'initial_beta':initial_beta,
       'fit_domain_radius':rmax,'fit_points':len(points),'created_utc':datetime.now(timezone.utc).isoformat(),'exact_leading_tail_moments':{'plus':'0','minus':'0'},'exact_thermal_jet_through_degree':4}
      path=root/(label+'_state.json');path.write_text(json.dumps(state,indent=2)+'\n');(root/(label+'_history.json')).write_text(json.dumps(history,indent=2)+'\n')
      (root/(label+'_tail.json')).write_text(json.dumps(serialized(tail),indent=2)+'\n')
      exact=certificate(path);assert exact['center_exact'] and exact['through_degree4_zero'] and exact['leading_moments_exact_zero']
      certdir=root/'joint_exact_certificates';certdir.mkdir(exist_ok=True);(certdir/(label+'_certificate.json')).write_text(json.dumps(exact,indent=2)+'\n')
      held=grid(np.r_[np.geomspace(1e-5,1e4,37),.017,.117,1.17],np.linspace(0,np.pi,34))
      holder=SimpleNamespace(beta=beta,s=1/beta,a0=1.,psi=basis.psi+[stream_row(v,basis.s)for v in EXTRA_TERMS],Cbase=np.r_[storedC,storedK],Cnull=np.zeros((basis.n+3,0)))
      audit=PrimitiveProblem(holder,held,64,'sinh');diag,fields=audit.diagnostics(np.zeros(0));sv=np.linalg.svd(fit.jac,compute_uv=False)
      row={'label':label,'state_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'beta':beta,'seed':seed,'free_beta':free,'nfev':fit.nfev,'status':int(fit.status),'message':fit.message,
       'objective_norm':float(np.linalg.norm(fit.fun)),'optimality':float(fit.optimality),'seconds':time.perf_counter()-tic,'jacobian_singular_largest':float(sv[0]),'jacobian_singular_smallest':float(sv[-1]),
       'max_absolute_C':float(abs(storedC).max()),'max_absolute_extra':float(abs(storedK).max()),'exact_local_verdict':exact['verdict'],'coefficient_rounding_max_change':state['coefficient_rounding_correction_max'],'diagnostics':diag,'exact_leading_tail_moments':True,
       'beta_bound_distance':min(beta-2.05,5-beta)if free else None,'verdict':'NO_ACCEPTED_CANDIDATE'}
      summary['states'].append(row);save();print('DONE',label,'beta',beta,'F',diag['thermal_divided']['max_ratio'],'seconds',row['seconds'],flush=True)
      np.savez_compressed(root/(label+'_heldout.npz'),points=held,**{k:fields[k]for k in ['RF','NF','Theta','Omega','S','Sy','H','A','B']})
      previous={'labels':basis.labels,'C':storedC};del audit,fields,problem,case
      if args.limit_states and len(summary['states'])>=args.limit_states:
        summary['status']='COMPLETE_LIMITED_PILOT';summary['ended_utc']=datetime.now(timezone.utc).isoformat();save();raise SystemExit(0)
summary['status']='COMPLETE_NO_CANDIDATE';summary['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',len(summary['states']),summary['elapsed_seconds'],flush=True)
