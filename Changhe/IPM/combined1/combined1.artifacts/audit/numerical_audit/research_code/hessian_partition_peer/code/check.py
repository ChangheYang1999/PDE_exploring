"""Accept independently computed complete radial primitives and domains."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,ctx,fmpq as Q
import importlib.util,json,time
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/hessian_partition_peer';PEER=ROOT.parent/'c1-t4'
spec=importlib.util.spec_from_file_location('n4_hessian_binding',ROOT/'research/scaled_hessian_peer/code/check.py');H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)
sha,ar=H.sha,H.ar;ctx.prec=2048

def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();checks={};rows=[]
 hp=ROOT/'research/scaled_hessian_peer/verification/result.json';accepted=json.loads(hp.read_text());assert all(accepted['checks'].values());paths=[hp,B/'PROOF.md',Path(__file__),ROOT/'research/scaled_hessian_peer/PROOF.md',ROOT/'research/scaled_hessian_peer/code/check.py'];owns={}
 for n in [16,17]:
  p=ROOT/f'research/hessian_radial_partition/verification/{H.fullname(n)}.json';d=json.loads(p.read_text());owns[n]=(p,d);paths.append(p)
  for rel,digest in d['inputs'].items():p=ROOT/rel;assert sha(p)==digest;paths.append(p)
 bind=H.Binding(B,paths)
 for p,d in accepted['frozen_or_retained_sources'].items():assert sha(ROOT/p)==d['stored_sha256'];bind.known[d['sha256']]=ROOT/p if not d['gzip'] else bind.known.get(d['sha256'],ROOT/p)
 # Gzipped entries must not be reused as uncompressed content.
 for p,d in accepted['frozen_or_retained_sources'].items():
  if d['gzip']:bind.known.pop(d['sha256'],None)
 manifest=bind.freeze(PEER/'research/hessian_partition_audit/data/manifest.json')
 for rel,digest in manifest['files'].items():bind.freeze(PEER/rel,digest)
 bind.freeze(PEER/'research/hessian_partition_audit/PROOF.md',manifest['proof_sha256']);r0,R=Q(manifest['r0']),Q(manifest['R']);cuts={'far':1/(1+R*R),'through_middle':1/(1+r0*r0),'whole':Q(1)}
 checks['exact_nominal_radii']=r0==Q(1,50) and R==Q(4178237423365963,500000000000)
 for n,(ownp,own) in owns.items():
  pp=PEER/f'research/hessian_partition_audit/verification/{n:03d}.json';peer=bind.freeze(pp);wp=PEER/f'research/scaled_hessian_audit/verification/{n:03d}.json';whole=bind.freeze(wp)
  for rel,digest in peer['inputs'].items():bind.freeze(PEER/rel,digest)
  key=str(n);row=next(r for r in accepted['rows'] if r['candidate']==H.fullname(n));checks[key+'_identity']=peer['candidate']==n and peer['raw_sha256']==own['raw_sha256']==whole['raw_sha256']==row['raw_sha256'] and peer['peer_sha256']==sha(ownp) and peer['whole_result_sha256']==sha(wp)==row['peer_result_sha256']
  checks[key+'_cuts']=Q(peer['r0'])==Q(own['r0_exact'])==r0 and Q(peer['R'])==Q(own['R_exact'])==R
  checks[key+'_scope']=peer['all_peer_and_whole_comparisons'] and peer['no_quadrature_error_global_theta_or_inverse_claim'] and own['all_full_energy_overlaps'] and own['exact_partition_verified']
  E={};minimum=1000000;count=0
  for label in ['xx','xy','yy']:
   pc,oc=peer['components'][label],own['components'][label];pm={r['ell']:r for r in pc['moments']};om={r['ell']:r for r in oc['moments']};wm={r['ell']:r for r in whole['components'][label]['moments']}
   checks[f'{key}_{label}_groups']=set(pm)==set(om)==set(wm)==set(range(2,17)) and pc['group_count']==oc['group_count']==15 and pc['pair_count']==oc['pair_count']
   totals={k:arb(0) for k in cuts}
   for ell,pr in pm.items():
    rr=om[ell];tag=f'{key}_{label}_{ell}';checks[tag+'_identity']=Q(pr['b'])==Q(rr['b'])==Q(wm[ell]['b']) and Q(pr['b'])>-1
    checks[tag+'_exact_replay']=pr['exact_CRT_replay'] and rr['exact_decomposition_replayed'] and pr['own_whole_overlap'] and rr['whole_group_overlap']
    checks[tag+'_positive_denominators']=len(pr['powers'])==2 and all(isinstance(k,int) and k>=0 for k in pr['powers']) and all(Q(a)>0 and isinstance(k,int) and k>0 for a,k in rr['factors'])
    for name,V in cuts.items():
     x,y=pr['primitives'][name],rr['primitives'][name];v=arb(x['value']);minimum=min(minimum,x['accuracy_bits'],y['relative_accuracy_bits'])
     checks[tag+'_'+name]=Q(x['cut_exact'])==Q(y['cut_exact'])==V and x['accuracy_bits']>150 and y['relative_accuracy_bits']>150 and v.is_finite() and v.overlaps(arb(y['integral'])) and x['peer_overlap']
     checks[tag+'_'+name+'_own_direct_checks']=all(q['recurrence_direct_overlap'] for q in y['hypergeometric_checks'])
     if name=='whole':checks[tag+'_full_group']=v.overlaps(arb(wm[ell]['value']))
     totals[name]+=v;count+=1
   totals={k:arb.pi()/2*v for k,v in totals.items()};de={'origin':totals['whole']-totals['through_middle'],'middle':totals['through_middle']-totals['far'],'far':totals['far'],'whole':totals['whole']}
   for dom,v in de.items():checks[f'{key}_{label}_{dom}_energy']=v>0 and v.overlaps(arb(pc['energies'][dom])) and v.overlaps(arb(oc['energies'][dom]))
   checks[f'{key}_{label}_telescopes']=sum((de[k] for k in ['origin','middle','far']),arb(0)).overlaps(de['whole']) and de['whole'].overlaps(arb(whole['components'][label]['energy']))
   E[label]=de
  metrics={}
  for dom in ['origin','middle','far','whole']:
   X2=E['xx'][dom]+E['xy'][dom];Y2=E['xy'][dom]+E['yy'][dom];H2=X2+Y2;K2=((arb(2).log()-arb(1)/2)*X2+(3*arb(2).log()-2)*Y2)/(16*arb.pi());vals={'X2':X2,'Y2':Y2,'D2':H2,'kappa2':K2,'X':X2.sqrt(),'Y':Y2.sqrt(),'D2rho':H2.sqrt(),'kappa':K2.sqrt()}
   for k,v in vals.items():checks[f'{key}_{dom}_{k}']=v>0 and v.overlaps(arb(peer['domain_metrics'][dom][k])) and v.overlaps(arb(own['domain_metrics'][dom][k]))
   metrics[dom]=vals
  comparison={}
  for k in ['X','Y','kappa']:
   sk=k+'2';full,mid=metrics['whole'][k],metrics['middle'][k];omit=metrics['origin'][sk]+metrics['far'][sk];saved=ar(Q(str(Fraction(own['FLOAT_comparison'][k]['saved_FLOAT']))));d={'full_minus_middle':full-mid,'middle_minus_FLOAT':mid-saved,'full_minus_FLOAT':full-saved,'omitted_squared_fraction':omit/metrics['whole'][sk],'far_fraction_of_omitted_squared':metrics['far'][sk]/omit}
   for q,v in d.items():checks[f'{key}_comparison_{k}_{q}']=v.overlaps(arb(peer['FLOAT_comparison'][k][q])) and v.overlaps(arb(own['FLOAT_comparison'][k][q]))
   checks[key+'_'+k+'_positive_omission']=omit>0 and full>mid;comparison[k]={a:b.str(90) for a,b in d.items()}
   if k=='kappa':checks[key+'_far_kappa_fraction_above_099998']=d['far_fraction_of_omitted_squared']>ar(Q(49999,50000))
  pm,om=peer['mesh_FLOAT'],own['mesh_audit'];checks[key+'_mesh_size']=pm['selected_nodes']==om['selected_nodes']==416 and pm['all_panels_complete'] and om['all_selected_panels_complete'] and len(pm['rows'])==len(om['selected_panels'])==13
  for i,(a,b) in enumerate(zip(pm['rows'],om['selected_panels'],strict=True)):checks[f'{key}_FLOAT_mesh_panel{i}']=a['index']==b['panel'] and a['selected_nodes']==b['kept_nodes']==b['total_nodes']==32 and b['complete'] and a['left_log']==b['left_log_FLOAT'] and a['right_log']==b['right_log_FLOAT']
  rows.append({'candidate':H.fullname(n),'raw_sha256':peer['raw_sha256'],'peer_result_sha256':sha(pp),'own_result_sha256':sha(ownp),'primitive_count':count,'minimum_primitive_accuracy_bits':minimum,'domain_metrics_reassembled':{d:{k:v.str(90) for k,v in vs.items()} for d,vs in metrics.items()},'comparison_reassembled':comparison,'peer_elapsed_seconds':peer['elapsed_seconds']})
 assert all(checks.values()),{k:v for k,v in checks.items() if not v};bind.finish()
 result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED N4-273 through independent T4-367; exact nominal radial energies only','r0_exact':str(r0),'R_exact':str(R),'checks':checks,'check_count':len(checks),'rows':rows,'own_inputs':bind.own,'frozen_or_retained_sources':bind.frozen,'peer_bindings':bind.bindings,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bind.bindings),'bindings',sha(out),result['utc'],'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
