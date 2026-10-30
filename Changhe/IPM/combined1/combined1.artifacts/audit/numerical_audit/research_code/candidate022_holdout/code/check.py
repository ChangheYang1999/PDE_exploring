"""Bind actual022 to the audited full basis and recorded analytic probe span."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,json,re,shlex,sys,time,difflib
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate022_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(p,actual,h);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE_v02.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 man=read(B/'source/MANIFEST_v01.json',prep['prior_manifest_sha256'])
 for name,e in man['files'].items():bind(B/'source'/name,e['sha256'])
 prior=read(R/'research/candidate016_holdout/verification/result.json');assert prior['status'].startswith('CONFIRMED')
 for path,h in prior['inputs'].items():bind(R/path,h)
 rank=read(R/'research/higher_mode_rank_peer/verification/result.json','dbbdc67c54ccb2a148e4b2e0a42e6ff0660a27655bd981f7f616d6bd8fd00a20');assert rank['verdict'].startswith('CONFIRMED')
 for path,h in rank['own_inputs'].items():bind(R/path,h)
 for path,e in rank['frozen_or_retained_sources'].items():bind(R/path,e['stored_sha256'])
 abstract_result=read(R/'research/higher_mode_scaled_rank/verification/result.json',rank['own_result_sha256'])
 for path,h in abstract_result['inputs'].items():bind(R/path,h)
 def raw(ident):
  ds=list((R/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'));assert len(ds)==1;d=ds[0];m=read(d/'MANIFEST.json');assert m['id']==d.name and len(m['coefficient_files'])==1;e=m['coefficient_files'][0];p=bind(d/e['name'],e['sha256']);return d.name,p,read(p),m
 name,rawp,actual,manifest=raw('022');pn,parentp,parent,pm=raw('016');phasep=bind(B/'source/N1_022_phase1.json','2a13c07969eb37af27c68a0336fa7f28a9f1747119e1f7ad4623302f58d5fd4f');phase=read(phasep)
 assert sha(rawp)=='85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f' and sha(parentp)=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 assert prior['raw_sha256']==sha(parentp)
 assert actual['cl_exact']==phase['cl_exact']==parent['cl_exact']=='4076476460239181/2251799813685248';checks['same_exact_c']=True
 assert phase['meta']['parent_json']==parentp.name and actual['meta']['parent_json']=='legqs25_m16to23_gpu_m16_s12_exact.json';checks['exact_two_phase_lineage']=True
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
 olds=list(map(shape,parent['generators']));present={(j,m) for j,m,s in olds};blocks=[(j,m) for j in [1,2,3] for m in range(16,24) if (j,m) in present]
 assert blocks==[(1,m) for m in range(16,20)]+[(j,m) for j in [2,3] for m in range(16,24)]
 additions=[(j,m,('legqs',0,N,4,25)) for j,m in blocks for N in range(12)];shapes=olds+additions
 abstract=read(R/'research/higher_mode_scaled_rank/verification/abstract_shapes.json')
 assert list(map(shape,actual['generators']))==list(map(shape,phase['generators']))==list(map(shape,abstract['generators']))==shapes
 assert len(olds)==2174 and len(additions)==240 and len(shapes)==len(set(shapes))==rank['potential_dimension']==rank['density_dimension']==2414;checks['all2414_shapes_match_audited_basis']=True
 c=Q(actual['cl_exact']);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)]
 assert all(z.denominator!=1 for z in ps+[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]) and 3+gamma<4
 witness=4*33*32*(ps[1]-16-Q(4,625));support=sorted({2*m+s for j,m in blocks for s in [-1,1]})
 assert witness!=0 and str(witness)==rank['density31_origin_coefficient'] and support==rank['density_new_mode_support']==list(range(31,48,2));checks['density31_actual_space_witness']=True
 assert 'outside the N4-160 n <= 31 sweep' in manifest['notes'];checks['manifest_outside31_claim_refuted']=True
 rows=lambda raw:[(1,k) if isinstance(k,int) else tuple(k) for k in raw['meta']['pair_k']]
 expected=rows(parent);assert len(expected)==len(set(expected))==67 and rows(actual)==rows(phase)==expected and max(n for n,k in expected)==17;checks['all67_analytic_rows_unchanged']=True
 script=bind(B/'source/N1_chain022.sh').read_text();oldscript=bind(R/'research/expanded_objective_span/data/N1_chain022.sh').read_text()
 commands=lambda text:[shlex.split(line)[shlex.split(line).index('run_quot.py')+1:] for line in text.splitlines() if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line)]
 calls=commands(script);assert calls==commands(oldscript) and len(calls)==2;checks['both_launch_commands_match_frozen_design']=True
 for i,(call,rawdata,steps,logname) in enumerate(zip(calls,[phase,actual],[12,28],['N1_022_phase1.out','N1_022_phase2.out'],strict=True)):
  callrows=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in call[9].split(',')];assert callrows==expected
  meta=rawdata['meta'];assert int(call[1])==meta['angular_midpoint']==180 and int(call[2])==meta['steps']==steps and int(call[5])==meta['middle_order']==16
  assert float(call[6])==meta['wlog']==26214400 and float(call[7])==meta['wkap']==3000000 and float(call[8])==meta['wpair']==1e12 and call[10]==meta['pair_mode']=='penalty'
  log=bind(B/'source'/logname).read_text();assert sha(phasep if i==0 else rawp) in log and 'generators 2414' in log and 'pair rows 67 weight 1000000000000.0' in log and 'per-row weights:' not in log
  iterations=[int(v) for v in re.findall(r'^it\s+(\d+) obj ',log,re.M)];assert iterations==list(range(1,steps+1));checks['phase'+str(i+1)+'_complete_parameters_and_log']=True
 assert phase['meta']['added_legqs']=='1,2,3:16:23:25:12' and actual['meta']['added_legqs'] is None and 'unset IPM_ADD_LEGQS' in script;checks['addition_only_phase1']=True
 before=bind(R/'research/candidate016_holdout/source/N1_run_quot.py').read_text();after=bind(B/'source/N1_run_quot.py').read_text();ast.parse(before);ast.parse(after)
 parser="PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))";assert parser in before and parser in after and 'pair_k=PAIRK' in before and 'pair_k=PAIRK' in after
 diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='frozen016_runner',tofile='current_runner_at022_snapshot'));dp=B/'verification/current_source_delta.diff';assert not dp.exists();dp.write_text(diff);bind(dp)
 impl=bind(B/'source/N1_ipm_opt3.py').read_text();ast.parse(impl);assert 'for q, w in zip(self.pair_k, ws)' in impl and 'phi_(n,K)' in impl;checks['current_row_parser_and_definition_read_as_text']=True
 reg=read(R/'research/heldout_probe_register/verification/register.json');assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:32:00+00:00')<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'));checks['public25_register_predates_recorded_launch']=True
 probes=[]
 for n,K in reg['pairs']+[[n,(n-1)//2+s] for n in range(19,32,2) for s in [0,8,32,128,512]]:
  assert n>17 and n%2 and K>=(n-1)//2 and all(j!=n for j,k in expected)
  probes.append({'n':n,'K':K,'outside_span':True,'all_objective_coefficients_at_n':0,'member_of_25_register':[n,K] in reg['pairs']})
 assert len(probes)==60;checks['all60_probes_outside_recorded_span']=True
 assert all(checks.values())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawp),'parent016_sha256':sha(parentp),'phase1_sha256':sha(phasep),'actual_shapes_match_accepted_rank':True,'generator_count':2414,'potential_dimension':2414,'density_dimension':2414,'new_shapes':240,'density_new_mode_support':support,'density31_origin_coefficient':str(witness),'manifest_support_verdict':'REFUTED: mode31 belongs to the old sweep; only33..47 lie outside','recorded_iterations':[12,28],'accepted_update_count':'Not inferred from iteration count','exact_objective_rows':[list(x) for x in expected],'probe_rows':probes,'registration_utc':reg['utc'],'history_scope':'007->013->quotient->016->022phase1->022phase2 only','source_scope':'Current source inspected as text, not asserted identical to historical bytes','inputs':inputs,'checks':checks,'check_count':len(checks),'publisher_code_executed':False,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED exact actual2414 shapes against accepted rank; recorded67-row history and analytic span separation'}
 dest=B/'verification/result.json'
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',len(checks),'checks',len(inputs),'bindings',sha(dest),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
