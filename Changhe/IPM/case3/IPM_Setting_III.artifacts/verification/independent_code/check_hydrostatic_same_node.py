"""Result304. Own physical inverse versus a reconstructed quadrature rule.
Producer source is parsed as data only. Never imports or executes producer code.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,ast,sys,traceback,math,resource
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
import numpy as np
import mpmath as mp
import torch
from scipy.special import roots_legendre
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_power_tail import PowerVerticalInverse
from scalar_mp_hydrostatic_density import ScalarMPDensity
R=Path('research/hydrostatic_same_node_inverse_audit');V=R/'verification';utc=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,d):Path(p).write_text(json.dumps(d,indent=2)+'\n')
def plain(v):return np.asarray(v,float)
def record(jet,vel,c,x,y):
 g,gx,gy,gxx=map(float,jet(x,y));v1,v2=map(float,vel);a=(c*x+v1)*gx;b=(c*y+v2)*gy;rh=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy)
 return dict(x=x,y=y,J=[g,gx,gy,gxx],V=[v1,v2],R=rh,Nf=nf,Nv=nv,Rf=abs(rh)/nf if nf else None,Rv=abs(rh)/nv if nv else None)
def diagnostic_rule(jet,x,y,npan,fd=False,ntail=80,hrel=1e-5):
 # Direct construction from the mathematical rule, using scipy quadrature and our jet.
 s,w=roots_legendre(24);upper=min(1.,y);ts=list(upper*(s+1)/2);weights=list(upper*w/2)
 z,q=roots_legendre(8)
 if y>1:
  edges=np.linspace(0.,math.log(y),npan+1)
  for a,b in zip(edges[:-1],edges[1:]):
   t=np.exp((a+b)/2+(b-a)*z/2);ts.extend(t);weights.extend((b-a)/2*q*t)
 ts=plain(ts);weights=plain(weights);z,q=roots_legendre(ntail);u=(z+1)/2;ratio=u/(1-u);tail=y+(1+y)*ratio**3;tw=q/2*(1+y)*3*u*u/(1-u)**4
 def xx(t):
  if not fd:return jet(x,t)[...,3]
  h=hrel*(1+abs(x));return(jet(x+h,t)[...,1]-jet(x-h,t)[...,1])/(2*h)
 return [-float(np.dot(tw,jet(x,tail)[...,1])),float(np.dot(weights*ts,xx(ts))+y*np.dot(tw,xx(tail)))]
def mj(x,y):
 x,y=np.broadcast_arrays(plain(x),plain(y));a=1+x*x+y*y
 return np.stack([y*a**(-.25),-.5*x*y*a**(-1.25),a**(-.25)-.5*y*y*a**(-1.25),-.5*y*a**(-1.25)+1.25*x*x*y*a**(-2.25)],axis=-1)
def main():
 inp=json.loads((V/'INPUTS.json').read_text());checks=[];out=dict(status='RUNNING',started_utc=utc(),checks=checks,driver_sha256=sha(__file__),proof_sha256=sha(R/'PROOF.md'),input_sha256=sha(V/'INPUTS.json'),review_resolution_sha256=sha(R/'DESIGN_REVIEW_RESOLUTION.md'),modules={f:sha(Path('independent_code')/f)for f in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','hydrostatic_power_tail.py','scalar_mp_hydrostatic_density.py']},rows=[],manufactures=[])
 def save():out['updated_utc']=utc();dump(V/'CHECKS.json',out)
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e));save()
  if not b:raise AssertionError((n,e))
 save()
 try:
  for f in inp['sources']:ck('frozen input '+f['frozen'],sha(f['frozen'])==f['sha256'])
  ck('frozen numeric state',sha(inp['state']['path'])==inp['state']['sha256'])
  for name in ['earlier_solver_static.py','producer_solver_static.py']:
   tree=ast.parse((V/name).read_text());cls=next(n for n in tree.body if isinstance(n,ast.ClassDef)and n.name=='HSModel');fun=next(n for n in cls.body if isinstance(n,ast.FunctionDef)and n.name=='residual');assign={a.targets[0].id:a.value for a in fun.body if isinstance(a,ast.Assign)and len(a.targets)==1 and isinstance(a.targets[0],ast.Name)}
   ck(name+' absolute R expression',ast.dump(assign['R'])==ast.dump(ast.parse('(c * X + V1) * gx + (c * Y + V2) * gy - g',mode='eval').body))
   ck(name+' first row is R',isinstance(assign['rows'],ast.List)and isinstance(assign['rows'].elts[0],ast.Name)and assign['rows'].elts[0].id=='R')
   ck(name+' next two rows normalization',ast.dump(assign['rows'].elts[1])==ast.dump(ast.parse('(a0 - 1.0).reshape(1)',mode='eval').body)and ast.dump(assign['rows'].elts[2])==ast.dump(ast.parse('(K - 1.0).reshape(1)',mode='eval').body))
   exprs=[k.value for n in ast.walk(tree)if isinstance(n,ast.Call)for k in n.keywords if k.arg=='nodes_Fmax'];ck(name+' Fmax absolute rows',len(exprs)==1 and ast.dump(exprs[0])==ast.dump(ast.parse('F.abs().max().item()',mode='eval').body))
  for path,key,module in [('research/hydrostatic_power_tail_inverse/verification/GATE.json','module_sha256','hydrostatic_power_tail.py'),('research/hydrostatic_power_tail_inverse/parent_regression/verification/GATE.json','evaluator_sha256','independent_hydrostatic.py')]:
   d=json.loads(Path(path).read_text());ck('parent gate '+path,d['status']=='PASS'and all(t['passed']for t in d['checks'])and d[key]==out['modules'][module]);out.setdefault('parents',{})[path]=sha(path)
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(inp['state']['path'])
  ck('declared trial',q.N==96 and q.M==24 and q.cl==2. and q.kappa==2. and q.basis=='local');ck('state diagnostic configuration',q.data['result']['inner']=='log'and not q.data['result']['fine']and q.data['result']['centre']=='drop'and not q.data['result']['extra'])
  out['producer_nodes_Fmax_absolute']=q.data['result']['nodes_Fmax'];out['producer_result']=q.data['result'];t=q.tk[1:];rr=q.L*np.sqrt((1+t)/2)/(1-t)**q.kappa;th=(np.arange(q.M)+.5)*np.pi/(2*q.M);xx=(rr[:,None]*np.cos(th)).ravel();yy=(rr[:,None]*np.sin(th)).ravel();idx=int(np.argmin((xx-1998.)**2+(yy-65.4)**2));npan=math.ceil(4*math.log10(max(float(yy.max()),10.)));points=[('reconstructed_node',float(xx[idx]),float(yy[idx])),('rounded_node',1998.,65.4),('annulus_probe',30.,1.)];out['node_recipe']=dict(index=idx,radial_index=idx//q.M+1,angular_index=idx%q.M,r=float(rr[idx//q.M]),theta=float(th[idx%q.M]),npan=npan,maximum_y=float(yy.max()),count=len(xx));ck('node recipe point count',len(xx)==2304 and idx%q.M==0 and abs(xx[idx]-1998)<1 and abs(yy[idx]-65.4)<.1)
  # Independent compact manufacture integral; no producer quantities enter.
  for x,y in [(.137,.219),(30.,1.),(2000.,65.)]:
   with mp.workdps(65):
    X=mp.mpf(x);Y=mp.mpf(y);one=mp.mpf(1);a=one+X*X+Y*Y;v1=X*a**(-mp.mpf(1)/4);v2=-mp.quad(lambda z:(one+X*X+z*z)**(-mp.mpf(1)/4)-X*X/2*(one+X*X+z*z)**(-mp.mpf(5)/4),[0,Y]);expected=[float(v1),float(v2)]
   for order,tail,scale in [(48,160,64.),(88,256,512.)]:
    got=PowerVerticalInverse(mj,.5,order,tail,scale,.125).at(x,y)['V'];err=max(abs(a-b)/(1+abs(b))for a,b in zip(got,expected));ck('radial manufacture '+str((x,y,order)),err<1e-9,err);out['manufactures'].append(dict(x=x,y=y,order=order,expected=expected,computed=got,scaled_error=err))
  jet=CartesianQJet(q)
  for label,x,y in points:
   row=dict(label=label,x=x,y=y,coordinate_hex=[x.hex(),y.hex()],physical=[],diagnostic_rule={},mp=[]);out['rows'].append(row)
   for order,tail,scale in [(48,160,64.),(64,192,128.),(88,256,512.)]:
    inv=PowerVerticalInverse(jet.jet,q.p,order,tail,scale,.125);rec=record(jet.jet,inv.at(x,y)['V'],q.cl,x,y);rec['options']=[order,tail,scale];row['physical'].append(rec);ck(label+' finite physical '+str(order),all(math.isfinite(v)for v in rec['J']+rec['V']+[rec['R'],rec['Nf'],rec['Nv']])and rec['Nf']>0 and rec['Nv']>0)
   for fd in [False,True]:
    v=diagnostic_rule(jet.jet,x,y,npan,fd);row['diagnostic_rule']['fd'if fd else'analytic']=record(jet.jet,v,q.cl,x,y)
   row['fd_step_sensitivity']=[dict(hrel=h,**record(jet.jet,diagnostic_rule(jet.jet,x,y,npan,True,hrel=h),q.cl,x,y))for h in [5e-6,2e-5]]
   high=row['physical'][-1];row['changes']=[dict(options=p['options'],V=[a-b for a,b in zip(p['V'],high['V'])],R=p['R']-high['R'],Rf=p['Rf']-high['Rf'])for p in row['physical'][:-1]]
   for label2,p in row['diagnostic_rule'].items():
    g,gx,gy,gxx=map(F,high['J']);X,Y,C=map(F,[x,y,q.cl]);vf,wf=map(F,high['V']);vg,wg=map(F,p['V']);r1=(C*X+vf)*gx+(C*Y+wf)*gy-g;r2=(C*X+vg)*gx+(C*Y+wg)*gy-g;delta=(vf-vg)*gx+(wf-wg)*gy;ck(label+' exact residual bridge '+label2,r1-r2==delta);row.setdefault('bridges',{})[label2]=dict(exact_R_difference=str(delta),double_R_difference=high['R']-p['R'],V_difference=[a-b for a,b in zip(high['V'],p['V'])]);natural=abs((C*X+vf)*gx)+abs((C*Y+wf)*gy)+abs(g);ck(label+' stored residual arithmetic '+label2,abs(F(high['R'])-r1)<=64*F(float(np.finfo(float).eps))*natural)
   for digits in [72,108]:
    with mp.workdps(digits):
     mm=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);j=mm.jet(x,y);row['mp'].append(dict(digits=digits,J=[mp.nstr(z,digits)for z in j]));save()
   with mp.workdps(108):
    j0=list(map(mp.mpf,row['mp'][0]['J']));j1=list(map(mp.mpf,row['mp'][1]['J']));change=max(abs(a-b)/(1+abs(b))for a,b in zip(j0,j1));ck(label+' MP precision',change<mp.mpf('1e-55'),mp.nstr(change,20));row['scaled_local_jet_change']=float(max(abs(a-mp.mpf(b))/(1+abs(a))for a,b in zip(j1,high['J'])));g,gx,gy,gxx=j1;C=mp.mpf(q.cl);X,Y=mp.mpf(x),mp.mpf(y);v,w=map(mp.mpf,high['V']);a=(C*X+v)*gx;b=(C*Y+w)*gy;rh=a+b-g;nf=abs(a)+abs(b)+abs(g);row['held_velocity_MP']=dict(R=mp.nstr(rh,80),Nf=mp.nstr(nf,80),Rf=mp.nstr(abs(rh)/nf,80),Rf_change=float(abs(rh)/nf-mp.mpf(high['Rf'])));ck(label+' local MP jet empirical consistency',row['scaled_local_jet_change']<2e-9,row['scaled_local_jet_change'])
   print(label,high['V'],high['R'],high['Nf'],high['Rf'],row['diagnostic_rule']['analytic']['V'],utc(),flush=True);save()
  out.update(status='PASS_FINITE_PROBES',finished_utc=utc(),count=len(checks),scope='Numerical sensitivities only. No saved map matrix or actual producer node array reconstructed bit-for-bit. No inverse enclosure or causal conclusion.');save();print('PASS',len(checks),utc(),flush=True)
 except Exception:out.update(status='FAIL',traceback=traceback.format_exc(),finished_utc=utc());save();raise
if __name__=='__main__':main()
