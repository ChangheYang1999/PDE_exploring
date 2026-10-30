"""Bind independent source paths and compare every complete Hessian group."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx,fmpq as Q
import gzip,json,sys,time
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/scaled_hessian_peer';PEER=ROOT.parent/'c1-t4'
sys.set_int_max_str_digits(0);ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(x):
 q=Q(x);return arb(q.numerator)/q.denominator
class Binding:
 def __init__(self,base,ownpaths):
  self.base=base;self.own={};self.known={};self.frozen={};self.bindings={}
  for p in ownpaths:self.ownfile(p)
 def ownfile(self,p,h=None):
  p=Path(p);s=sha(p);assert h is None or s==h,(str(p),s,h);self.own[str(p.relative_to(ROOT))]=s;self.known[s]=p
 def freeze(self,p,h=None):
  p=Path(p);blob=p.read_bytes();s=sha256(blob).hexdigest();assert h is None or h==s,(str(p),s,h)
  compressed=False
  if s in self.known:dest=self.known[s]
  else:
   dest=self.base/'source'/p.relative_to(PEER);compressed=len(blob)>1000000
   if compressed:dest=dest.with_name(dest.name+'.gz')
   dest.parent.mkdir(parents=True,exist_ok=True);stored=gzip.compress(blob,mtime=0) if compressed else blob
   if dest.exists():assert dest.read_bytes()==stored
   else:
    with dest.open('xb') as f:f.write(stored)
   if not compressed:self.known[s]=dest
  self.frozen[str(dest.relative_to(ROOT))]={'original':str(p),'sha256':s,'stored_sha256':sha(dest),'gzip':compressed};self.bindings[str(p)]=s
  return json.loads(blob) if p.suffix=='.json' else None
 def finish(self):
  for p,h in self.own.items():assert sha(ROOT/p)==h
  for p,d in self.frozen.items():assert sha(ROOT/p)==d['stored_sha256']
def fullname(n):return {7:'C1-N1-007-d2w-j7-e2bal',16:'C1-N1-016-legqs25-quot013',17:'C1-N1-017-legqs50-quot013'}[n]
def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();checks={};rows=[]
 paths=[B/'PROOF.md',Path(__file__)];owns={}
 for n in [7,16,17]:
  p=ROOT/f'research/scaled_background_hessian/verification/{fullname(n)}.json';d=json.loads(p.read_text());owns[n]=(p,d);paths.append(p)
  for rel,h in d['inputs'].items():p=ROOT/rel;assert sha(p)==h;paths.append(p)
 bind=Binding(B,paths);manifest=bind.freeze(PEER/'research/scaled_hessian_audit/data/manifest.json')
 for rel,h in manifest['files'].items():bind.freeze(PEER/rel,h)
 bind.freeze(PEER/'research/scaled_hessian_audit/PROOF.md',manifest['proof_sha256'])
 for n,(ownp,own) in owns.items():
  peerp=PEER/f'research/scaled_hessian_audit/verification/{n:03d}.json';peer=bind.freeze(peerp);m=manifest['candidates'][str(n)]
  for rel,h in peer['inputs'].items():bind.freeze(PEER/rel,h)
  key=str(n);checks[key+'_identity']=peer['candidate']==n and peer['raw_sha256']==own['raw_sha256']==m['raw_sha256'] and peer['peer_sha256']==sha(ownp)==m['peer_sha256']
  checks[key+'_scope']=peer['whole_plane'] and own['whole_plane'] and peer['no_global_theta_or_inverse_claim'] and own['no_global_theta_claim'] and peer['mixed_derivative_exact_equality'] and all(r['equal'] for r in own['mixed_derivative_checks'])
  checks[key+'_point_count']=len(peer['point_checks'])==len(own['point_checks'])==3
  for i,(pp,op) in enumerate(zip(peer['point_checks'],own['point_checks'],strict=True)):
   checks[f'{key}_point{i}_coordinates']=Q(pp['x'])==Q(op['x']) and Q(pp['y'])==Q(op['y'])
   for k in ['xx','xy','yy']:checks[f'{key}_point{i}_{k}']=arb(pp['values'][k]).overlaps(arb(op['values'][k])) and pp['peer_overlaps'][k] and op['Cartesian_jet_overlaps'][k]
  E={};minimum=1000000;groupcount=0
  for label in ['xx','xy','yy']:
   pc=peer['components'][label];oc=own['component_energies'][label];pm={r['ell']:r for r in pc['moments']};om={r['ell']:r for r in oc['moments']}
   checks[f'{key}_{label}_group_map']=set(pm)==set(om)==set(range(2,17)) and pc['group_count']==oc['group_count']==15
   checks[f'{key}_{label}_pair_count']=pc['pair_count']==oc['pair_count'];total=arb(0)
   for ell,pr in pm.items():
    rr=om[ell];v=arb(pr['value']);minimum=min(minimum,pr['accuracy_bits'],rr['relative_accuracy_bits'])
    tag=f'{key}_{label}_ell{ell}';checks[tag+'_identity']=Q(pr['b'])==Q(rr['b']) and Q(pr['b'])>-1 and rr['m']==1
    checks[tag+'_integral']=v.is_finite() and v.overlaps(arb(rr['integral'])) and pr['peer_moment_overlap']
    checks[tag+'_exact_replays']=pr['exact_CRT_replay'] and rr['exact_decomposition_replayed'] and pr['accuracy_bits']>150 and rr['relative_accuracy_bits']>150
    checks[tag+'_positive_denominators']=len(pr['denominator_powers'])==2 and all(isinstance(k,int) and k>=0 for k in pr['denominator_powers']) and all(Q(a)>0 and isinstance(k,int) and k>0 for a,k in rr['factors'])
    checks[tag+'_own_direct_moment_regressions']=all(z['direct_overlap'] and z['recurrence_accuracy_bits']>150 and z['direct_accuracy_bits']>150 for rows0 in rr['pole_power_checks'].values() for z in rows0)
    total+=v;groupcount+=1
   E[label]=arb.pi()/2*total;checks[f'{key}_{label}_energy']=E[label]>0 and E[label].overlaps(arb(pc['energy'])) and E[label].overlaps(arb(oc['energy'])) and pc['peer_energy_overlap']
  X2=E['xx']+E['xy'];Y2=E['xy']+E['yy'];H2=X2+Y2;K2=((arb(2).log()-arb(1)/2)*X2+(3*arb(2).log()-2)*Y2)/(16*arb.pi())
  squares={'X2':X2,'Y2':Y2,'D2rho_squared':H2,'kappa_squared':K2};values={'X':X2.sqrt(),'Y':Y2.sqrt(),'D2rho':H2.sqrt(),'kappa':K2.sqrt()}
  for k,v in squares.items():checks[f'{key}_square_{k}']=v>0 and v.overlaps(arb(peer['squares'][k])) and v.overlaps(arb(own[k])) and peer['peer_square_overlaps'][k]
  for k,v in values.items():checks[f'{key}_norm_{k}']=v>0 and v.overlaps(arb(peer['values'][k])) and v.overlaps(arb(own['values'][k])) and peer['peer_norm_overlaps'][k]
  cap={7:Q(728164680182325428,10**18),16:Q(735053672993720766,10**18),17:Q(729080538628955349,10**18)}[n];checks[key+'_strict_kappa_cap']=values['kappa']<ar(cap)
  if n==7:
   accepted=json.loads((PEER/'research/scaled_hessian_audit/source/accepted007.json').read_text())
   for label,k,sq in [('X','D_rho_x',X2),('Y','D_rho_y',Y2),('D2rho','D2rho',H2)]:
    old=accepted['norms'][k];cal=peer['007_calibration'][label];checks[f'007_{label}_calibration']=Q(old['weight_error_rational'])==0 and sq.overlaps(arb.pi()/2*ar(Q(old['unweighted_rational_sum']))) and values[label].overlaps(arb(old['norm_upper_ball'])) and cal['exact_energy_overlap'] and cal['containing_norm_ball_overlap']
    exact_norm=(arb.pi()/2*ar(Q(old['unweighted_rational_sum']))).sqrt()
    checks[f'007_{label}_directed_endpoint_diagnostic']=exact_norm.overlaps(arb(old['norm_upper']))==cal['endpoint_ball_overlap_not_required']
   checks['007_Y_directed_endpoint_not_containing']=not peer['007_calibration']['Y']['endpoint_ball_overlap_not_required']
  rows.append({'candidate':fullname(n),'raw_sha256':peer['raw_sha256'],'peer_result_sha256':sha(peerp),'own_result_sha256':sha(ownp),'group_count':groupcount,'minimum_group_accuracy_bits':minimum,'values_reassembled':{k:v.str(90) for k,v in values.items()},'strict_kappa_upper_exact':str(cap),'peer_elapsed_seconds':peer['elapsed_seconds']})
 assert all(checks.values()),{k:v for k,v in checks.items() if not v};bind.finish()
 result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED N4-268 through independent T4-366; upper commutator bound only','checks':checks,'check_count':len(checks),'rows':rows,'own_inputs':bind.own,'frozen_or_retained_sources':bind.frozen,'peer_bindings':bind.bindings,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bind.bindings),'bindings',sha(out),result['utc'],'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
