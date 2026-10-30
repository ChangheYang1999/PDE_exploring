"""Independent comparison of three complete017 weak calculations and exact H caps."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_three_weak_peer';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def ar(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
def main():
 start=time.monotonic();ctx.prec=2048;inputs={};checks={};target=B/'verification/result.json';assert not target.exists()
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or got==h,(str(p),got,h);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');assert prep['proof_written_before_code'];bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__));m=read(B/'source/MANIFEST.json',prep['source_manifest_sha256'])
 for name,z in m['files'].items():bind(B/'source'/name,z['sha256'])
 extra=read(B/'source/CURRENT_IMPORTS.json',prep['current_imports_sha256'])
 for name,z in extra['files'].items():bind(B/'source'/name,z['sha256'])
 peer=read(B/'source/N3_probe.json');assert peer['id']=='C1-N1-017-legqs50-quot013'
 for name,h in peer['code_sha256'].items():assert m['files'][name]['sha256']==h
 bind(R/'research/scaled50_factored_weak/PROOF.md');audit=read(R/'research/candidate_audits/verification/C1-N1-017-legqs50-quot013.json');assert audit['all_forbidden_zero'] and audit['snapshot_hashes_confirmed'];checks['immutable_candidate_and_forbidden_sectors']=True
 selected=[(21, 522, '2d22cd77aeba6df9ac5ff759932ad8e6a916fd982b9fc5442f8e8a914a1b8aaf'), (23, 2400, '61fe31cd9cbf747b1be985df4620b05796583989e4b4fe998b2fb25e6921e8d6'), (19, 1800, '80db2ef50716df589d2d2b751fc8feb5884005a8782ea122ee486a429fc4d356')];ownrows=[]
 for n,K,h in selected:
  p=R/f'research/scaled50_factored_weak/verification/C1-N1-017-legqs50-quot013_n{n:03d}_K{K:05d}.json';own=read(p,h)
  for rel,z in own['inputs'].items():bind(R/rel,z)
  ownrows.append((n,K,p,own))
 before=dict(inputs)
 with (B/'verification/BOUND_START.json').open('x') as f:json.dump({'utc':now(),'inputs':before,'before_finite_arithmetic':True},f,indent=2);f.write('\n')
 rows=[]
 for n,K,p,own in ownrows:
  assert own['raw_sha256']==peer['source_sha256']==audit['generator_sha256']=='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114' and peer['cl']=='4076476460239181/2251799813685248'
  assert own['n']==n and own['K']==K and own['whole_plane'] and own['all_background_modes_retained'] and own['direct_parts_overlap'] and own['gradient_certificate']['strict_bound_all_critical_points'];checks[f'complete_own_source_{n}_{K}']=True
  pr=peer['probes'][f'heldout_n{n}_K{K}.json'];assert pr['status']=='FINITE' and pr['angular_mode']==n and pr['probe_coefficients']=={str(K):'1'} and pr['H_source'].startswith('closed form:')
  comparisons={}
  for label,key in [('I','pairing'),('M','M'),('C','C')]:
   z=arb(own[key]);pp=arb(pr['pairing_signed' if label=='I' else label]);assert z.overlaps(pp) and pp.lower()<z.lower() and z.upper()<pp.upper()
   comparisons[label]={'own':z.str(100),'peer':pp.str(45),'own_strictly_inside_peer_display':True};checks[f'{label}_{n}_{K}']=True
  assert K>=1 and 1<=n<=2*K+1
  H=Q((2*K+1)*4)*Q(K)**K/Q(K+2)**(K+2);hb=ar(H);ph=arb(pr['H_upper']);assert hb.upper()<ph.lower() and ph.upper()-hb.lower()<ar(Q(1,10**300));checks[f'exact_closed_H_and_outward_endpoint_{n}_{K}']=True
  I=abs(arb(own['pairing']));D=arb(own['M'])+arb(own['C']);root=lambda h:2*I/(D+(D*D+4*h*I).sqrt());coarse=root(hb);sharpH=Q(own['H_upper_exact']);sharp=root(ar(sharpH))
  assert sharpH<H and sharp>coarse and coarse.overlaps(arb(pr['radius'])) and sharp.overlaps(arb(own['radius']));checks[f'coarse_and_sharp_roots_{n}_{K}']=True
  a,b=2*K+1,2*K+4;qa=(K+3)*b;qb=-((K+2)*a+(K+1)*b);qc=K*a;disc=qb*qb-4*qa*qc;assert disc>0
  rad=arb(disc).sqrt();roots=[(-qb-rad)/(2*qa),(-qb+rad)/(2*qa)]
  assert all(0<r<1 for r in roots)
  critical=[abs(r**K*(1-r)**2*(a-b*r)) for r in roots]
  t=ar(Q(K,K+2));critical.append(n*t**K*(1-t)**2)
  assert all(v.upper()<ar(sharpH) for v in critical)
  checks[f'independent_global_sharp_gradient_{n}_{K}']=True

  floor=Q(int((coarse.lower()*10**18).floor().unique_fmpz())-1,10**18);assert floor>0 and ar(floor)<coarse;sf=Q(own['strict_lower_exact']);assert ar(sf)<sharp;checks[f'strict_floors_{n}_{K}']=True
  rel=(sharp-coarse)/sharp;rows.append({'n':n,'K':K,'own_source_sha256':sha(p),'component_comparisons':comparisons,'H_coarse_exact':str(H),'H_coarse':hb.str(100),'H_sharp_exact':str(sharpH),'coarse_root':coarse.str(100),'N3_radius':pr['radius'],'strict_coarse_floor':str(floor),'sharp_root':sharp.str(100),'strict_sharp_floor':str(sf),'relative_root_difference':rel.str(100),'independent_radial_critical_roots':[z.str(100) for z in roots],'independent_gradient_critical_values':[z.str(100) for z in critical],'coarse_H_relative_effect_exceeds_1e_minus5':bool(rel>ar(Q(1,100000)))})
 checks['all_before_hashes_unchanged']=all(sha(R/p)==h for p,h in before.items());assert all(checks.values())
 out={'utc':now(),'candidate':peer['id'],'precision_bits':ctx.prec,'inputs':inputs,'rows':rows,'checks':checks,'check_count':len(checks),'before_binding_sha256':sha(B/'verification/BOUND_START.json'),'foreign_code_executed':False,'new_field_recomputation':False,'peer_historical_import_versions_observed':False,'peer_historical_F_cache_available':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED three independent complete I/M/C comparisons and both exact-cap roots; distance implications conditional on PROOF hypotheses; other three N3 probes OPEN; no dyadic or full norm conclusion'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CHECKS',len(checks),'INPUTS',len(inputs),'SECONDS',out['elapsed_seconds'],'SHA',sha(target),flush=True)
 for z in rows:print('PROBE',z['n'],z['K'],'coarse_floor',z['strict_coarse_floor'],'sharp_floor',z['strict_sharp_floor'],'relative_H_effect',z['relative_root_difference'][:95],flush=True)
if __name__=='__main__':main()
