"""Compare independent016 complete moments and the exact coarse gradient cap."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_n3_weak_comparison'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
def main():
 start=time.monotonic();ctx.prec=2048;inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or got==h,(p,h,got);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 bind(B/'PROOF.md');bind(Path(__file__));peer=read(B/'source/N3_probe.json','e71575779cd09d4c06bb438fdae06b9c1e6b43d63bb99e7263f1db8040a44f82')
 for name,h in peer['code_sha256'].items():bind(B/'source'/name,h)
 accepted=read(R/'research/candidate016_weak_peer/verification/result.json','a9a568fd52a50a5a385f9ea698d06255f091e8e3873d9764b03134808a615941');bind(R/'research/candidate016_weak_peer/PROOF.md');bind(R/'research/scaled_factored_weak/PROOF.md')
 rows=[]
 for n,K in [(21,522),(23,2400),(19,1800)]:
  p=R/f'research/scaled_factored_weak/verification/C1-N1-016-legqs25-quot013_n{n:03d}_K{K:05d}.json';own=read(p)
  for rel,h in own['inputs'].items():bind(R/rel,h)
  assert own['raw_sha256']==peer['source_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42' and peer['cl']=='4076476460239181/2251799813685248'
  assert own['n']==n and own['K']==K and own['whole_plane'] and own['all_background_modes_retained'] and own['direct_parts_overlap'] and own['gradient_certificate']['strict_bound_all_critical_points'];checks[f'complete_own_source_{n}_{K}']=True
  pr=peer['probes'][f'heldout_n{n}_K{K}.json'];assert pr['angular_mode']==n and pr['probe_coefficients']=={str(K):'1'}
  comparisons={}
  for label,key in [('I','pairing'),('M','M'),('C','C')]:
   z=arb(own[key]);pp=arb(pr['pairing_signed' if label=='I' else label]);assert z.overlaps(pp) and pp.lower()<z.lower() and z.upper()<pp.upper()
   comparisons[label]={'own':z.str(100),'peer':pp.str(45),'own_strictly_inside_peer_display':True};checks[f'{label}_{n}_{K}']=True
  H=Q((2*K+1)*4)*Q(K)**K/Q(K+2)**(K+2);hb=ar(H);ph=arb(pr['H_upper']);assert hb.upper()<ph.lower() and ph.upper()-hb.lower()<ar(Q(1,10**300));checks[f'exact_closed_H_and_outward_endpoint_{n}_{K}']=True
  I=abs(arb(own['pairing']));D=arb(own['M'])+arb(own['C']);root=lambda h:2*I/(D+(D*D+4*h*I).sqrt());coarse=root(hb);sharpH=Q(own['H_upper_exact']);sharp=root(ar(sharpH))
  assert sharpH<H and sharp>coarse and coarse.overlaps(arb(pr['radius'])) and sharp.overlaps(arb(own['radius']));checks[f'coarse_and_sharp_roots_{n}_{K}']=True
  floor=Q(int((coarse.lower()*10**18).floor().unique_fmpz())-1,10**18);assert floor>0 and ar(floor)<coarse;sf=Q(own['strict_lower_exact']);assert ar(sf)<sharp;checks[f'strict_floors_{n}_{K}']=True
  if n in [19,23]:
   ac=next(z for z in accepted['rows'] if z['n']==n and z['K']==K);assert Q(ac['strict_floor'])==sf and Q(ac['H_upper_exact'])==sharpH;checks[f'prior_independent_acceptance_{n}_{K}']=True
  rows.append({'n':n,'K':K,'own_source_sha256':sha(p),'component_comparisons':comparisons,'H_coarse_exact':str(H),'H_coarse':hb.str(100),'H_sharp_exact':str(sharpH),'coarse_root':coarse.str(100),'N3_radius':pr['radius'],'strict_coarse_floor':str(floor),'sharp_root':sharp.str(100),'strict_sharp_floor':str(sf),'relative_root_difference':((sharp-coarse)/sharp).str(60)})
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':peer['id'],'precision_bits':ctx.prec,'inputs':inputs,'rows':rows,'checks':checks,'foreign_code_executed':False,'new_field_recomputation':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED three independent complete I/M/C comparisons and exact coarse-H roots; distance implications conditional on PROOF hypotheses; other three N3 probes OPEN'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CHECKS',len(checks),'INPUTS',len(inputs),'SECONDS',out['elapsed_seconds'],'SHA',sha(p),flush=True)
if __name__=='__main__':main()
