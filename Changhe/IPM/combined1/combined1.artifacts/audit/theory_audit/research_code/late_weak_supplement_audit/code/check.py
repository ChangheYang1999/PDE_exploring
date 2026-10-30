"""Finite T4 replay of accepted weak moments and complete gradient maxima."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,sys,time
from flint import arb,ctx
sys.set_int_max_str_digits(200000)
B=Path(__file__).resolve().parents[1]
ctx.prec=2048
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def A(x):
 x=Q(x);return arb(x.numerator)/arb(x.denominator)
def read(rel):return json.loads((B/rel).read_text())
def main():
 start=time.monotonic(); checks={};manifest=read('data/manifest.json')
 def check(label,truth):
  assert label not in checks,label
  assert truth,label
  checks[label]=True
 for z in manifest:check('binding:'+z['local'],sha(B/z['local'])==z['sha256'])
 rows=read('data/rows.json');external=read('data/external_bindings.json')
 check('all_original_inputs_matched_at_preparation',external['all_matched'] and len(external['bindings'])==69)
 check('six_probes',len(rows)==6)
 expected={'015':'d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae','017':'7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114'}
 outrows=[]
 for row in rows:
  tag=row['candidate'];n,K=row['n'],row['K'];key=f'{tag}:{n}:{K}:';z=row['row'];own=read(row['production']);peer=read(row['peer']);result=read(row['comparison'])
  check(key+'source_production',sha(B/row['production'])==z['own_source_sha256'])
  check(key+'immutable_candidate',own['raw_sha256']==peer['source_sha256']==expected[tag] and result['candidate']==peer['id']==row['id'])
  check(key+'fixed_c',peer['cl']=='4076476460239181/2251799813685248')
  check(key+'probe_origin',K>0 and n>0 and n%2==1 and 2*K+1>=n)
  check(key+'complete_own_production_flags',all(own[x] for x in ['whole_plane','all_background_modes_retained','direct_parts_overlap']))
  check(key+'comparison_checks',result['check_count']==len(result['checks']) and all(result['checks'].values()))
  p=peer['probes'][f'heldout_n{n}_K{K}.json']
  check(key+'peer_unit_monomial',p['status']=='FINITE' and p['angular_mode']==n and p['probe_coefficients']=={str(K):'1'})
  for name,okey,pkey in [('I','pairing','pairing_signed'),('M','M','M'),('C','C','C')]:
   ob,pb=arb(own[okey]),arb(p[pkey])
   check(key+name+'_strict_containment',pb.lower()<ob.lower() and ob.upper()<pb.upper())
   check(key+name+'_comparison_binding',ob.overlaps(arb(z['component_comparisons'][name]['own'])))
  check(key+'reference_parts_identity',arb(own['pairing']).overlaps(arb(own['pairing_by_parts'])))
  H=Q(4*(2*K+1))*Q(K)**K/Q(K+2)**(K+2)
  hs=Q(own['H_upper_exact']);check(key+'coarse_cap_exact',H==Q(z['H_coarse_exact']))
  check(key+'sharp_cap_exact',hs==Q(z['H_sharp_exact']) and 0<hs<H)
  hp=arb(p['H_upper']);check(key+'peer_H_outward',A(H).upper()<hp.lower() and hp.upper()-A(H).lower()<A(Q(1,10**300)))
  aa,bb=2*K+1,2*K+4
  # Differentiate t^K(1-t)^2(A-Bt) by three product-rule terms.
  deriv=[K*aa,-K*(aa+bb)-2*aa-bb,K*bb+2*bb+bb]
  qa,qb,qc=bb*(K+3),-((K+2)*aa+(K+1)*bb),K*aa
  check(key+'exact_derivative_identity',deriv==[qc,qb,qa])
  discr=qb*qb-4*qa*qc;check(key+'two_real_critical_points',discr>0)
  t1=(-qb-arb(discr).sqrt())/(2*qa);t2=(-qb+arb(discr).sqrt())/(2*qa)
  check(key+'critical_points_in_unit_interval',0<t1 and t1<t2 and t2<1)
  ta=A(Q(K,K+2));values=[abs(t**K*(1-t)**2*(aa-bb*t)) for t in [t1,t2]]+[n*ta**K*(1-ta)**2]
  for j,v in enumerate(values):check(key+f'global_gradient_value_{j}',v.upper()<A(hs).lower())
  I=abs(arb(own['pairing']));D=arb(own['M'])+arb(own['C']);check(key+'positive_I_D',I>0 and D>0)
  root=lambda hh:2*I/(D+(D*D+4*hh*I).sqrt())
  rcoarse,rsharp=root(A(H)),root(A(hs))
  check(key+'root_order',rsharp>rcoarse)
  check(key+'coarse_root_display',rcoarse.overlaps(arb(z['coarse_root'])) and rcoarse.overlaps(arb(p['radius'])))
  check(key+'sharp_root_display',rsharp.overlaps(arb(z['sharp_root'])) and rsharp.overlaps(arb(own['radius'])))
  margins={}
  for which,hh,rootvalue in [('coarse',H,rcoarse),('sharp',hs,rsharp)]:
   floor=Q(z[f'strict_{which}_floor']);fb=A(floor)
   check(key+which+'_strict_floor',0<fb and fb<rootvalue)
   margin=I.lower()-D.upper()*fb-A(hh)*fb*fb
   check(key+which+'_quadratic_margin',margin>0)
   margins[which]=margin.str(100)
  check(key+'sharp_floor_saved',Q(own['strict_lower_exact'])==Q(z['strict_sharp_floor']))
  rel=(rsharp-rcoarse)/rsharp
  check(key+'generic_relative_claim_refuted',rel>A(Q(1,100000)))
  check(key+'relative_display',rel.overlaps(arb(z['relative_root_difference'])))
  outrows.append({'candidate':tag,'n':n,'K':K,'H_sharp_exact':str(hs),'radial_critical_points':[t1.str(100),t2.str(100)],'gradient_critical_values':[v.str(100) for v in values],'coarse_root':rcoarse.str(100),'sharp_root':rsharp.str(100),'strict_coarse_floor':z['strict_coarse_floor'],'strict_sharp_floor':z['strict_sharp_floor'],'strict_quadratic_margins':margins,'relative_root_change':rel.str(100)})
 floor=next(Q(z['strict_sharp_floor']) for z in outrows if z['candidate']=='015' and z['n']==23 and z['K']==2400)
 check('015_new_floor_exact',floor==Q('0.003033479200692324'))
 check('015_exceeds_graded_ceiling',floor>Q(25,54684))
 check('015_exceeds_all_specified_scalar_ceilings',floor>Q(3793,10**9))
 for z in manifest:check('unchanged:'+z['local'],sha(B/z['local'])==z['sha256'])
 result={'utc':now(),'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'rows':outrows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'elapsed_seconds':time.monotonic()-start,'new_field_integration':False,'foreign_code_executed':False,'verdict':'CONFIRMED six finite weak-root implications and global caps, conditional on accepted full-plane moments and stated canonical fixed-c L2 equation. Generic relative change less than 1e-5 is REFUTED for all six. No dyadic or full norm conclusion.'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],'CHECKS',len(checks),'SECONDS',result['elapsed_seconds'],'SHA',sha(B/'verification/result.json'))
 for z in outrows:print(z['candidate'],z['n'],z['K'],'strict floor',z['strict_sharp_floor'])
if __name__=='__main__':main()
