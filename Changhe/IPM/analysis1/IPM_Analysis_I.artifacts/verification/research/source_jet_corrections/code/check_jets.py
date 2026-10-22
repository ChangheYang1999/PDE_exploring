"""New exact interval consequences of the previously certified modal source."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from collections import Counter
import sympy as s
from flint import arb,fmpq,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];TOPIC=B/'research/source_jet_corrections';E=TOPIC/'evidence'
ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ep(v):
 m,e=v.man_exp();return Q(int(m))*Q(2)**int(e)
def vp(v):
 sign,m,e,_=v;return (-1 if sign else 1)*Q(int(m))*Q(2)**int(e)
def ends(v):return [ep(v.lower()),ep(v.upper())] if isinstance(v,arb) else [vp(t) for t in v._mpi_]
def a(q):q=Q(q);return arb(fmpq(q.numerator,q.denominator))
def v(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def pair(q):return tuple(Q(q[k]) for k in ('lower_exact','upper_exact'))
def pack(q):return {'lower_exact':str(q[0]),'upper_exact':str(q[1]),'lower_approx':float(q[0]),'upper_approx':float(q[1])}
def main():
 tic=time.monotonic();counts=Counter();source=B/'research/modal_source/evidence/source_result.json';j=json.loads(source.read_text());old=json.loads((source.parent/'output_audit.json').read_text())
 assert sha(source)==old['source_result_sha256']=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691'
 assert old['verdict']=='PASS' and old['initial_signs_and_positive_derivative'] and old['bisections_verified_by_exact_width']==28
 deps={'input_sha256':B/'data_exact/modal_v2.json','scalar_input_sha256':B/'research/modal_repair/evidence/independent_gauss_iv.json','source_sha256':B/'research/modal_source/code/certify_source.py','moments_sha256':B/'research/exponential_moments/code/moments.py','Cox_sha256':B/'research/canonical_inverse/code/exact_audit.py'}
 for k,p in deps.items():assert sha(p)==j[k]==old['verified_dependencies'][k]
 deps.update({'old_output_audit':source.parent/'output_audit.json','old_import_audit':source.parent/'import_binding_audit.json','source':source,'proof':TOPIC/'PROOF.md','addendum':TOPIC/'ADDENDUM.md','self':Path(__file__)})
 pins={str(p.relative_to(B)):sha(p) for p in deps.values()}
 assert json.loads((source.parent/'import_binding_audit.json').read_text())['status']=='PASS'
 r=j['initial_root_proof'][0];al,ar=Q(r['a_exact']),Q(r['b_exact']);bl,br=map(Q,j['final_root_endpoints_exact'])
 assert pair(r['w_a'])[1]<0<pair(r['w_b'])[0] and pair(r['wprime_on_box'])[0]>0
 assert al<=bl<br<=ar and (ar-al)/(br-bl)==2**28
 vals={n:pair(j['final_values'][n]) for n in ('xstar','mu_minus_1','g','gprime')}
 xl,xh=vals['xstar'];ml,mh=vals['mu_minus_1'];gl,gh=vals['g'];pl,ph=vals['gprime']
 assert xl<=bl<br<=xh and xl>0 and mh<0 and gl>0 and pl>0
 delta=Q(22,10**9)
 exact={'D':(-mh*gl,-ml*gh),'C':(-mh+gl+pl,-ml+gh+ph),'H':(2*gl-xh*ph,2*gh-xl*pl)}
 dl,dh=exact['D'];cl,ch=exact['C'];exact['margin']=(dl-ch*delta-2*delta**2,dh-cl*delta-2*delta**2)
 assertions={'D_gt_6.70e-7':dl>Q(670,10**9),'C_gt_30.0229':cl>Q(300229,10000),'C_lt_30.0230':ch<Q(300230,10000),'H_gt_57.1':exact['H'][0]>Q(571,10),'positive_exact_margin':exact['margin'][0]>0,'positive_margin_using_only_rounded_safe_bounds':Q(670,10**9)-Q(300230,10000)*delta-2*delta**2>0}
 assert all(assertions.values());counts['strict_exact_consequences']=len(assertions)
 engine={}
 # Each engine evaluates every monotone corner, not a sampled parameter point.
 corners={'D':[(lambda cv: -cv(mh)*cv(gl)),(lambda cv:-cv(ml)*cv(gh))],
          'C':[(lambda cv:-cv(mh)+cv(gl)+cv(pl)),(lambda cv:-cv(ml)+cv(gh)+cv(ph))],
          'H':[(lambda cv:2*cv(gl)-cv(xh)*cv(ph)),(lambda cv:2*cv(gh)-cv(xl)*cv(pl))],
          'margin':[(lambda cv:cv(dl)-cv(ch)*cv(delta)-2*cv(delta)**2),(lambda cv:cv(dh)-cv(cl)*cv(delta)-2*cv(delta)**2)]}
 for name,cv,sqrt in [('arb512',a,lambda z:z.sqrt()),('iv180',v,iv.sqrt)]:
  output={}
  for key,fun in corners.items():
   endpoint_balls=[ends(f(cv)) for f in fun]
   for k,ball in enumerate(endpoint_balls):assert ball[0]<=exact[key][k]<=ball[1];counts[name+'_exact_corner_contains']+=1
   output[key]=pack((endpoint_balls[0][0],endpoint_balls[1][1]))
  rootlo=ends(2*cv(dl)/(cv(ch)+sqrt(cv(ch)**2+8*cv(dl))))
  roothi=ends(2*cv(dh)/(cv(cl)+sqrt(cv(cl)**2+8*cv(dh))))
  output['root_scale']=pack((rootlo[0],roothi[1]));assert delta<rootlo[0]
  engine[name]=output
 # Portable saved bounds are exact rational hulls of both engines.
 bounds={key:(min(Q(engine[n][key]['lower_exact']) for n in engine),max(Q(engine[n][key]['upper_exact']) for n in engine)) for key in ['D','C','H','margin','root_scale']}
 x,y,mu,g,gp,z,u,w,t,zz,vv,sigma,b,R,C,D=s.symbols('x y mu g gp z u w t zz vv sigma b R C D', real=True)
 rho=(g+z+(gp+vv)*x)*y;V1=u;V2=(mu+w)*y
 expr=s.diff(V1*s.diff(rho,x)+V2*s.diff(rho,y)-rho,y).subs({x:0,y:0})
 identities={}
 def ident(name,expr):assert s.simplify(expr)==0,(name,expr);identities[name]=str(expr)
 ident('source_jet',expr-((mu-1)*g+(mu-1)*z+g*w+gp*u+w*z+u*vv))
 G=s.Function('G')(x);density=G*y
 ident('normalized_face',s.diff((-2*sigma*x*s.diff(density,x)+4*sigma*y*s.diff(density,y))/3,y)-2*sigma*(2*G-x*s.diff(G,x))/3)
 ident('x_squared_face_cancel',2*x*x-x*s.diff(x*x,x))
 K=(x*x-y*y)/(2*s.pi*(x*x+y*y)**2)
 ident('kernel_derivative',s.diff(K,y)+y*(3*x*x-y*y)/(s.pi*(x*x+y*y)**3))
 ident('kernel_at_minus_Z',s.diff(K,y).subs({x:-x,y:-y},simultaneous=True)-y*(3*x*x-y*y)/(s.pi*(x*x+y*y)**3))
 ident('weighted_norm_exponent',(2*b-2)+2-2*b)
 ident('scaled_velocity_exponent',(b-1)-1-(b-2))
 ident('scaled_remainder_exponent',(b-1)-3-(b-2)+2)
 # d/dy [y A(t)] = A - A', since dt/dy=-1/y.
 I=s.Function('I')(t)
 ident('h_derivative',I-s.diff(I,t).subs(s.Derivative(I,t),-s.sin(t)/t)-I-s.sin(t)/t)
 f=s.sin(t)/t
 ident('f_derivative',f-s.diff(f,t)-(s.sin(t)-s.cos(t))/t-s.sin(t)/t**2)
 ident('transport_equation',(I+s.sin(t)/t)-I-s.sin(t)/t)
 ident('integration_by_parts_derivative',s.diff(s.cos(t)/t,t)+s.cos(t)/t**2+s.sin(t)/t)
 # Equivalent stable expression evaluated symbolically at a positive formal square root.
 root=2*D/(C+s.sqrt(C*C+8*D))
 ident('quadratic_root',2*root*root+C*root-D)
 ident('unnormalized_coefficient',s.diff(-sigma*x*s.diff(density,x)+sigma*y*s.diff(density,y),y)-sigma*(G-x*s.diff(G,x)))
 for p,h in pins.items():assert sha(B/p)==h,p
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_NEW_JET_AND_FACE_SCALARS','scope':'New interval expressions from prior independent modal-source certificate; analytic proofs in PROOF and ADDENDUM. No X3 endpoint.','files':pins,'root_bracket_exact':[str(bl),str(br)],'delta_exact':str(delta),'exact_ranges':{k:pack(z) for k,z in exact.items()},'portable_bounds':{k:pack(z) for k,z in bounds.items()},'engines':engine,'assertions':assertions,'symbolic_identities':identities,'counts':dict(counts),'seconds':time.monotonic()-tic}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','counts','seconds']}));print(json.dumps(out['portable_bounds'],indent=2))
if __name__=='__main__':main()
