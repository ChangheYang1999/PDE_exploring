from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,time
import sympy as sp
R=Path(__file__).resolve().parents[3];B=R/'research/angular_tensor_peer';PB=R.parent/'c1-t4/research/numerics_final_v06_audit'
spec=importlib.util.spec_from_file_location('own_binding303',R/'research/scaled_hessian_peer/code/check.py');H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H);sha=H.sha

def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists()
 oldp=R/'research/candidate_angular_resolution/verification/result.json';old=json.loads(oldp.read_text());paths=[oldp,B/'PROOF.md',Path(__file__),R/'research/scaled_hessian_peer/code/check.py']
 for rel,h in old['inputs'].items():p=R/rel;assert sha(p)==h;paths.append(p)
 bind=H.Binding(B,paths);pp=PB/'verification/result.json';peer=bind.freeze(pp)
 for rel,h in peer['inputs'].items():bind.freeze(Path(rel),h)
 manifest=json.loads((PB/'source/MANIFEST.json').read_text())
 for rel,row in manifest['files'].items():bind.freeze(PB/'source'/rel,row['sha256'])
 checks={};c,s,A,Bp,C,U,W=sp.symbols('c s A B C U W')
 Hxx=c*c*A-2*c*s*Bp+s*s*C;Hxy=c*s*(A-C)+(c*c-s*s)*Bp;Hyy=s*s*A+2*c*s*Bp+c*c*C
 e1=sp.expand(Hxx**2+2*Hxy**2+Hyy**2-(A*A+2*Bp*Bp+C*C));e2=sp.expand((c*U-s*W)**2+(s*U+c*W)**2-U*U-W*W)
 poly_domain=sp.QQ.frac_field(A,Bp,C,U,W)
 def circle_zero(expr):return sp.rem(sp.Poly(expr,c,s,domain=poly_domain),sp.Poly(c*c+s*s-1,c,s,domain=poly_domain)).is_zero
 checks['tensor_mod_unit_circle']=circle_zero(e1);checks['gradient_mod_unit_circle']=circle_zero(e2)
 checks['trace_mod_unit_circle']=circle_zero(Hxx+Hyy-A-C)
 # Derive the polar Hessian from differentiating Cartesian gradient.
 r=sp.symbols('r',positive=True);f,g,h,k,l=sp.symbols('Fr Ft Frr Frt Ftt')
 # Differential rules act on c,s and the independent radial/angular jet.
 exprx=c*f-s*g/r;expry=s*f+c*g/r
 def dr(e):return sp.diff(e,r)+sp.diff(e,f)*h+sp.diff(e,g)*k
 def dt(e):return -s*sp.diff(e,c)+c*sp.diff(e,s)+sp.diff(e,f)*k+sp.diff(e,g)*l
 values={
  'xx':c*dr(exprx)-s/r*dt(exprx),
  'xy':s*dr(exprx)+c/r*dt(exprx),
  'yx':c*dr(expry)-s/r*dt(expry),
  'yy':s*dr(expry)+c/r*dt(expry)}
 subs={A:h,Bp:k/r-g/r**2,C:f/r+l/r**2}
 for label,expr in [('xx',Hxx),('xy',Hxy),('yx',Hxy),('yy',Hyy)]:checks['polar_derivation_'+label]=sp.expand(values[label]-expr.subs(subs))==0
 z=sp.symbols('z');roots=[]
 for N in range(1,13):
  period=8*N;mod=sp.Poly(sp.cyclotomic_poly(period,z),z,domain=sp.QQ)
  for q in range(0,2*N+1):
   coeff=[0]*period
   for i in range(N):
    power=2*q*(2*i+1);coeff[power%period]+=1;coeff[-power%period]+=1
   remainder=sp.rem(sp.Poly.from_list(list(reversed(coeff)),z,domain=sp.QQ),mod)
   expected=2*N if q==0 else -2*N if q==2*N else 0
   assert remainder==sp.Poly(expected,z),(N,q,remainder)
   roots.append({'N':N,'q':q,'twice_cosine_sum':expected,'exact_cyclotomic_remainder':True})
 checks['cyclotomic_moments']=len(roots)==sum(2*N+1 for N in range(1,13))
 M=old['max_potential_m'];N=old['midpoint_quadrant_nodes'];d=4*M+3
 checks['shape_application']=M==79 and N==180 and d==old['max_residual_frequency']==319
 checks['peer_tensor_claim']=peer['hessian_and_gradient_orthogonal_invariance'] and peer['full_tensor_min_sufficient_N']==2*M+2==160 and peer['individual_component_min_sufficient_N']==2*M+3==161 and peer['actual_N']==N
 full_modes=list(range(1,d+1,2));qset={(a+b)//2 for a in full_modes for b in full_modes}|{abs(a-b)//2 for a in full_modes for b in full_modes}
 checks['full_tensor_indices']=max(qset)==d and d<2*(2*M+2) and len(qset)==peer['cosine_indices_checked']==320
 component=[]
 for order in range(3):
  modes=list(range((1+order)%2,d+order+1,2));indices={(a+b)//2 for a in modes for b in modes}|{abs(a-b)//2 for a in modes for b in modes}
  assert max(indices)==d+order<2*(2*M+3)<=2*N
  component.append({'order':order,'mode_parity':(1+order)%2,'frequency_bound':d+order,'cosine_index_count':len(indices),'sufficient_N':2*M+3,'actual_N_pass':True})
 checks['component_parities_and_indices']=len(component)==3
 assert all(checks.values()),{k:v for k,v in checks.items() if not v};bind.finish()
 result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED T4-374 section5 exact angular quadrature for full tensors and separate components under the stated hypotheses','checks':checks,'check_count':len(checks),'general_full_tensor_sufficient_N':'2M+2','general_order_at_most_two_component_sufficient_N':'2M+3','M':M,'actual_N':N,'full_tensor_sufficient_N':160,'separate_components_sufficient_N':161,'exact_root_of_unity_moments':roots,'root_of_unity_check_count':len(roots),'components':component,'peer_result_sha256':sha(pp),'own295_result_sha256':sha(oldp),'own_inputs':bind.own,'frozen_or_retained_sources':bind.frozen,'peer_bindings':bind.bindings,'foreign_code_executed':False,'no_floating_radial_or_whole_plane_error_claim':True,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(roots),'cyclotomic moments',len(bind.bindings),'bindings',sha(out),result['utc'],'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
