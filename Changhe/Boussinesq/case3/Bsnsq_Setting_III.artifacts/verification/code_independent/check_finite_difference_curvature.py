"""Own exact finite differences and independent polynomial controls; no NUM code."""
from pathlib import Path
from fractions import Fraction as Q
import datetime,hashlib,json,re,time,itertools
import numpy as np
import sympy as s
start=time.monotonic();root=Path('research/190_finite_difference_curvature_audit/verification')
raw=Path('verification/mbb_center_20261021T1811Z')
root.mkdir(parents=True,exist_ok=True)
def q(d):return Q(int(d['numerator']),int(d['denominator']))
def out(x):return {'exact':str(x),'approx':float(x)}
rows=[]
for p in sorted(raw.glob('*.certificate.json')):
 d=json.loads(p.read_text());ar=Path(d['archive']);assert hashlib.sha256(ar.read_bytes()).hexdigest()==d['archive_sha256']
 a=np.load(ar,allow_pickle=False);b=q(d['parameters']['beta']);lam=q(d['parameters']['lambda']);v=q(d['inverse']['forced']['values']['m'])
 cs=q(d['inverse']['self']['values']['c']); cf=q(d['inverse']['forced']['values']['c'])
 assert cf-(1+b/2)==v
 meta=Q(float(a['strain_mismatch']));bf=float(b)
 log=Path('../numerics/runs')/f'mbb_b{bf:g}.out'; text=log.read_text();(root/log.name).write_text(text)
 r={'certificate':str(p),'archive':str(ar),'archive_sha256':d['archive_sha256'],'beta':out(b),'lambda':out(lam),'forced_m':out(v),'self_c':out(cs),'seed_c':out((cf-cs)/lam),'self_ratioF':out(q(d['inverse']['self']['values']['ratioF'])),'saved_diagnostic':out(meta),'exact_minus_diagnostic':out(v-meta),'saved_utc':str(a['saved_utc']),'inner_f':float(a['inner_f']),'inner_crit':str(a['inner_crit']),'inner_converged':int(a['inner_converged']),'converged':int(a['converged']),'objective':float(a['obj']),'log':str(root/log.name),'log_sha256':hashlib.sha256(text.encode()).hexdigest()}
 rows.append(r)
assert len(rows)==3
bs=[Q(r['beta']['exact']) for r in rows];vs=[Q(r['forced_m']['exact']) for r in rows];h=Q(1,100);delta=Q(1,500000)
hm=bs[1]-bs[0];hp=bs[2]-bs[1];sl=(vs[1]-vs[0])/hm;sr=(vs[2]-vs[1])/hp;a=(sr-sl)/(hm+hp);d=sl+a*hm;assert a<0
D1=(vs[2]-vs[0])/(2*h);D2=(vs[0]-2*vs[1]+vs[2])/h**2
err1=delta/h;err2=4*delta/h**2;tv=-d/(2*a);qv=vs[1]-d*d/(4*a)
calc={'nominal_h':out(h),'actual_h_minus':out(hm),'actual_h_plus':out(hp),'h_minus_minus_nominal':out(hm-h),'h_plus_minus_nominal':out(hp-h),'D1':out(D1),'D2':out(D2),'hypothetical_delta_not_established':out(delta),'D1_node_error_bound_if_delta':out(err1),'D2_node_error_bound_if_delta':out(err2),'D1_interval_if_delta_and_nominal_nodes':[out(D1-err1),out(D1+err1)],'D2_interval_if_delta_and_nominal_nodes':[out(D2-err2),out(D2+err2)],'quadratic_a':out(a),'quadratic_derivative_center':out(d),'quadratic_second_derivative':out(2*a),'quadratic_vertex_beta':out(bs[1]+tv),'quadratic_vertex_shift':out(tv),'quadratic_vertex_value':out(qv),'quadratic_linear_lambda_adjustment_if_mlambda_2_86':out(-qv/Q(286,100)),'central_saved_m_exceeds_hypothetical_delta':vs[1]>delta,'literal_B2_all_self_ratioF_above_3_over_5':all(Q(r['self_ratioF']['exact'])>Q(3,5) for r in rows)}
# Controls: independently constructed polynomials, exact sample interpolation,
# finite-difference error extrema and Peano-kernel identities.
t=s.symbols('t');checks=[]
def check(name,z):
 assert z,name
 checks.append(name)
for hh in [Q(1,100),Q(1,7),Q(3,2)]:
 H=s.Rational(hh.numerator,hh.denominator)
 for coef in [(1,2,-3),(Q(1,3),Q(-2,5),Q(-3,7)),(0,0,-1)]:
  qq=sum(s.Rational(c)*t**i for i,c in enumerate(coef))
  vals=[qq.subs(t,j*H) for j in [-1,0,1]]
  for target1,target2 in [(0,0),(1,1),(-1,-1),(2,100)]:
   AA=(s.diff(qq,t).subs(t,0)-target1)/H**2
   BB=(s.diff(qq,t,2).subs(t,0)-target2)/(2*H**2)
   f=qq+AA*t*(t*t-H*H)+BB*t*t*(t*t-H*H)
   for j,v in zip([-1,0,1],vals):check(f'node_{hh}_{coef}_{target1}_{target2}_{j}',s.expand(f.subs(t,j*H)-v)==0)
   check(f'arbitrary_d1_{hh}_{coef}_{target1}_{target2}',s.diff(f,t).subs(t,0)==target1)
   check(f'arbitrary_d2_{hh}_{coef}_{target1}_{target2}',s.diff(f,t,2).subs(t,0)==target2)
 for k in range(9):
  f=t**k;fd=(f.subs(t,-H)-2*f.subs(t,0)+f.subs(t,H))/H**2
  integ=(s.integrate((H+t)*s.diff(f,t,2),(t,-H,0))+s.integrate((H-t)*s.diff(f,t,2),(t,0,H)))/H**2
  check(f'Peano_monomial_{hh}_{k}',s.simplify(fd-integ)==0)
  if k==3:check(f'D1_Taylor_sharp_{hh}',((f.subs(t,H)-f.subs(t,-H))/(2*H))==H**2)
  if k==4:check(f'D2_Taylor_sharp_{hh}',fd==2*H**2)
 errors=[tuple(delta*k for k in signs) for signs in itertools.product([-1,1],repeat=3)]
 check(f'D1_node_extremum_{hh}',max(abs((e[2]-e[0])/(2*hh)) for e in errors)==delta/hh)
 check(f'D2_node_extremum_{hh}',max(abs((e[0]-2*e[1]+e[2])/hh**2) for e in errors)==4*delta/hh**2)
for i,(offset,vv) in enumerate(zip([-hm,Q(0),hp],vs)):check(f'actual_unequal_interpolation_{i}',vs[1]+d*offset+a*offset**2==vv)
for left,right in [(Q(1,2),Q(3,5)),(hm,hp)]:
 # Different representation: Vandermonde inverse rather than slope differences.
 nodes=[-left,Q(0),right]; mat=s.Matrix([[1,s.Rational(x),s.Rational(x*x)] for x in nodes]);sol=mat.inv()*s.Matrix([s.Rational(v) for v in vs]);ss=(vs[1]-vs[0])/left;tt=(vs[2]-vs[1])/right;aa=(tt-ss)/(left+right);dd=ss+aa*left
 for j,x in enumerate([vs[1],dd,aa]):check(f'Vandermonde_{left}_{right}_{j}',sol[j]==s.Rational(x))
# Explicit center-positive-curvature counterexample with the actual unequal nodes.
# P=t(t+hm)(t-hp) and tP vanish at all three nodes. P'(0)=-hm hp,
# P''(0)=2(hm-hp), (tP)''(0)=-2hm hp; solve for desired center derivatives.
A=d/(hm*hp);B=(2*a+2*A*(hm-hp)-1)/(2*hm*hp)
coeffs=[vs[1],d-A*hm*hp,a+A*(hm-hp)-B*hm*hp,A+B*(hm-hp),B]
for j,offset in enumerate([-hm,Q(0),hp]):check(f'actual_counterexample_node_{j}',sum(c*offset**i for i,c in enumerate(coeffs))==vs[j])
check('actual_counterexample_derivative_zero',coeffs[1]==0);check('actual_counterexample_curvature_positive',2*coeffs[2]==1)
calc['same_actual_nodes_smooth_counterexample_coefficients']=[out(x) for x in coeffs]
# Exact unequal-node weights and Taylor controls, added after their written proof.
H=hm+hp
w1=[-hp/(hm*H),(hp-hm)/(hm*hp),hm/(hp*H)]
w2=[2/(hm*H),-2/(hm*hp),2/(hp*H)]
L1=sum(abs(x) for x in w1)
calc['actual_node_d_error_bound_if_delta']=out(delta*L1)
calc['actual_node_2a_error_bound_if_delta']=out(4*delta/(hm*hp))
calc['actual_node_d_interval_if_delta']=[out(d-delta*L1),out(d+delta*L1)]
calc['actual_node_2a_interval_if_delta']=[out(2*a-4*delta/(hm*hp)),out(2*a+4*delta/(hm*hp))]
calc['actual_node_d_Taylor_M3_coefficient']=out(hm*hp/6)
calc['actual_node_2a_Taylor_center_M3_coefficient']=out(abs(hp-hm)/3)
calc['actual_node_2a_Taylor_M4_coefficient']=out((hm**3+hp**3)/(12*H))
check('actual_d_weight_identity',sum(w*v for w,v in zip(w1,vs))==d)
check('actual_2a_weight_identity',sum(w*v for w,v in zip(w2,vs))==2*a)
for left,right in [(Q(1,100),Q(1,100)),(Q(1,2),Q(3,5)),(Q(3,5),Q(1,2)),(hm,hp)]:
 total=left+right;v1=[-right/(left*total),(right-left)/(left*right),left/(right*total)];v2=[2/(left*total),-2/(left*right),2/(right*total)]
 l1=sum(abs(z) for z in v1)
 check(f'unequal_L1_correction_{left}_{right}',l1==2/total+abs(right-left)/(left*right)+(right-left)**2/(left*right*total))
 check(f'unequal_L2_weights_{left}_{right}',sum(abs(z) for z in v2)==4/(left*right))
 for idx,(ww,expected) in enumerate([(v1,delta*l1),(v2,4*delta/(left*right))]):
  extremes=[abs(sum(w*delta*sgn for w,sgn in zip(ww,signs))) for signs in itertools.product([-1,1],repeat=3)]
  check(f'unequal_node_extremum_{idx}_{left}_{right}',max(extremes)==expected)
 nodes=[-left,Q(0),right]
 for k in range(5):
  vv=[xx**k for xx in nodes];dval=sum(w*v for w,v in zip(v1,vv));aval=sum(w*v for w,v in zip(v2,vv))
  if k<=2:
   check(f'unequal_d_exact_monomial{k}_{left}_{right}',dval==int(k==1))
   check(f'unequal_2a_exact_monomial{k}_{left}_{right}',aval==2*int(k==2))
  if k==3:
   check(f'unequal_d_sharp_M3_{left}_{right}',dval==left*right)
   check(f'unequal_2a_cubic_{left}_{right}',aval==2*(right-left))
  if k==4:check(f'unequal_2a_sharp_M4_{left}_{right}',aval==2*(left**3+right**3)/total)
report=Path('../numerics/NUM_REPORT.md');(root/'NUM_REPORT_snapshot.md').write_bytes(report.read_bytes())
(root/'NOTES_FOR_LEAD_snapshot.md').write_bytes(Path('../numerics/NOTES_FOR_LEAD.md').read_bytes())
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'rows':rows,'calculations':calc,'exact_control_count':len(checks),'exact_controls':checks,'status':'PASS','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact algebra for three saved reconstructed states. Conditional delta bounds are not established numerical error bounds. All derivative and fold conclusions for an exact inner solution remain OPEN.'}
(root/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['utc'],result['elapsed_seconds'],'s',len(checks),'exact controls')
for r in rows:print(r['beta']['approx'],r['forced_m']['approx'],r['exact_minus_diagnostic']['approx'],r['self_ratioF']['approx'],r['inner_crit'])
for key in ['D1','D2','quadratic_vertex_beta','quadratic_vertex_value','quadratic_linear_lambda_adjustment_if_mlambda_2_86']: print(key,calc[key]['approx'])
