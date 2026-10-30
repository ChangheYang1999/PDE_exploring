"""Whole-plane factored weak tests of locally frozen exact snapshots."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,importlib.util,json,sys,time
from flint import arb,ctx,fmpq as Q
from fields25 import ScaledRadial,ar,field_hash
import weak as W
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/scaled_factored_weak'
sys.set_int_max_str_digits(0)
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
J=module('n4_candidate25_cartesian',ROOT/'research/multiscale_generators/code/cartesian.py')
CAL=module('n4_candidate25_gradient',BASE/'code/calibrate_v2.py')
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def write(path,out):
 with path.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
def run(name,probes,objective_audit=None):
 start=time.monotonic();ctx.prec=2048;assert Path(name).name==name
 directory=ROOT/'research/candidate_audits/data'/name
 manifest_path=directory/'MANIFEST.json';manifest=json.loads(manifest_path.read_text())
 assert manifest['id']==name and len(manifest['coefficient_files'])==1
 entry=manifest['coefficient_files'][0];assert Path(entry['name']).name==entry['name']
 source=directory/entry['name'];rawsha=sha(source);assert rawsha==entry['sha256']
 snapshots={}
 for line in (directory/'SHA256SUMS').read_text().splitlines():
  digest,filename=line.split(None,1);filename=filename.lstrip('*');assert Path(filename).name==filename
  assert sha(directory/filename)==digest;snapshots[filename]=digest
 direct_path=ROOT/'research/generator_sector_audit/verification'/f'{name}_direct.json'
 standard_path=ROOT/'research/candidate_audits/verification'/f'{name}.json'
 audit_path=direct_path if direct_path.exists() else standard_path;audit=json.loads(audit_path.read_text())
 assert audit['generator_sha256']==rawsha and audit['B0n_exact'] and audit['leading_density_equal_state131'] and audit['c_equal_state131']
 sectors=audit.get('sector_summary',audit);assert sectors['all_forbidden_zero']
 for key in ['dependency_sha256']:
  for rel,digest in audit.get(key,{}).items():assert sha(ROOT/rel)==digest
 model=ScaledRadial(source);assert model.c==Q(manifest['c_l_exact']) and model.c>1
 cal_paths=[BASE/'verification/candidate013.json',BASE/'verification/fields.json',ROOT/'research/factored_pole_moments/verification/result.json']
 for p in cal_paths:
  record=json.loads(p.read_text())
  for rel,digest in record.get('inputs',{}).items():assert sha(ROOT/rel)==digest
 assert all(json.loads(cal_paths[0].read_text())['accepted013_overlaps'].values())
 paths=[source,manifest_path,directory/'SHA256SUMS',audit_path,Path(__file__),BASE/'PROOF.md',BASE/'code/fields25.py',BASE/'code/weak.py',BASE/'code/calibrate_v2.py',ROOT/'research/factored_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/multiscale_generators/code/moments.py',*cal_paths]
 objective=None
 if objective_audit:
  objective_audit=Path(objective_audit).resolve();assert objective_audit.is_relative_to(ROOT)
  objective=json.loads(objective_audit.read_text());assert objective['raw_sha256']==rawsha and objective['candidate']==name
  for rel,digest in objective['inputs'].items():assert sha(ROOT/rel)==digest
  paths.append(objective_audit)
 data=json.loads(source.read_text());pointcal=[]
 for x,y in [('1/10','73/100'),('3','4'),('60','80')]:
  jet=J.GeneratorJet(data,x,y,4).fields();values=model.evaluate(x,y)
  checks={key:values[key].overlaps(jet[key]) for key in ['rho','u1','u2','rho_x','rho_y','residual']};assert all(checks.values())
  pointcal.append({'x':x,'y':y,'six_field_overlaps':checks})
 print('CANDIDATE_FIELDS',name,'seconds',time.monotonic()-start,flush=True)
 for n,K in probes:
  tick=time.monotonic();output=BASE/f'verification/{name}_n{n:03d}_K{K:05d}.json';assert not output.exists()
  assert n>=1 and n%2 and K>=max(1,(n-1)//2)
  # This rational is merely a proposed cap. The three global critical values must prove it strictly.
  coarse=CAL.gradient(K,n,Q(2*n,K*K))
  cap=max(arb(x).upper() for x in coarse['amplitudes']);denom=10**24
  bound=Q(int((cap*denom).ceil().unique_fmpz())+1,denom);sup=CAL.gradient(K,n,bound)
  fields=W.construct(model,n,K);points=W.point_checks(model,n,K,fields)
  Iparts,pc,pp,ph=W.pairing_parts(model,fields[0],K)
  projection,counts=W.project(model,n);I,ic=W.integrate_groups(projection,model.delta,Q(-1),K+1,'Idirect')
  assert I.overlaps(Iparts) and min(I.rel_accuracy_bits(),Iparts.rel_accuracy_bits())>150
  M2,mc,mp,mh=W.energy(fields[:1],model,K,'M2');C2,cc,cp,ch=W.energy(fields[1:],model,K,'C2')
  M,C=M2.sqrt(),C2.sqrt();D=M+C;radius=2*abs(I)/(D+(D*D+4*ar(bound)*abs(I)).sqrt())
  floor=Q(int((radius.lower()*10**18).floor().unique_fmpz())-1,10**18);assert floor>0 and ar(floor)<radius
  vals={'pairing':I,'pairing_by_parts':Iparts,'M2':M2,'C2':C2,'M':M,'C':C,'D':D,'radius':radius}
  label='UNCLASSIFIED: no complete objective audit bound'
  if objective is not None:
   match=[r for r in objective['probe_rows'] if r['n']==n and r['K']==K];assert len(match)==1
   label='HELD_OUT: outside audited objective span' if match[0]['outside_span'] else 'DESIGN_OR_SPANNED: no held-out claim'
  out={'utc':now(),'candidate':name,'n':n,'K':K,'precision_bits':ctx.prec,'raw_sha256':rawsha,'snapshot_hashes':snapshots,
       'inputs':{str(p.relative_to(ROOT)):sha(p) for p in paths},'actual_candidate_cartesian_jet_calibration':pointcal,'point_checks':points,
       'field_sha256':[field_hash(f) for f in fields],'projection_sha256':field_hash(projection),'projection_pairs':counts,
       'M_group_sha256':mh,'C_group_sha256':ch,'parts_group_sha256':ph,'M_pairs':mp,'C_pairs':cp,'parts_pairs':pp,
       'M_moments':mc,'C_moments':cc,'parts_moments':pc,'direct_moments':ic,**{key:value.str(100) for key,value in vals.items()},
       'direct_parts_overlap':True,'gradient_certificate':sup,'H_upper_exact':str(bound),'strict_lower_exact':str(floor),'strict_floor_verified':True,
       'probe_objective_status':label,'objective_historical_scope':objective.get('historical_scope') if objective else None,'objective_scope':objective.get('objective_scope') if objective else None,'whole_plane':True,'all_background_modes_retained':True,'probe_elapsed_seconds':time.monotonic()-tick,
       'total_elapsed_seconds':time.monotonic()-start,'status':'OPEN independent candidate-level and backend review; necessary distance under PROOF hypotheses'}
  write(output,out);print('DONE',name,n,K,'root',radius.str(35),'floor',floor,'seconds',out['probe_elapsed_seconds'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('probes',nargs='+',help='n,K integer pair');p.add_argument('--objective-audit');args=p.parse_args()
 run(args.candidate,[tuple(map(int,x.split(','))) for x in args.probes],args.objective_audit)
