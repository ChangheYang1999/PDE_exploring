"""Finite source, counter, and manufactured ratio readback; no new PDE solves."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,time
r=Path('research/350_final_reading_order_audit');v=r/'verification';tick=time.monotonic();start=datetime.now(timezone.utc);checks=[];inputs={}
def ck(name,b,detail=None):checks.append(dict(name=name,passed=bool(b),detail=detail))
def read(p):
 p=Path(p);b=p.read_bytes();inputs[str(p)]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)};return b.decode()
controls={('farfield_grid_20261020T1930','S0'),('farfield_grid_20261020T1930','manufactured_picard')}
rows=list(csv.DictReader(read('../numerics/artifacts/consolidated_residuals.csv').splitlines()));keys=sorted({(x['folder'],x['label']) for x in rows});results={};global_rows=[]
ck('123_keys',len(keys)==123);ck('121_forced_keys',sum(k not in controls for k in keys)==121);ck('5904_rows',len(rows)==5904)
for folder,label in keys:
 p=Path('research')/folder/'verification/results.json'
 if not p.exists():p=Path('verification')/folder/'results.json'
 if folder not in results:results[folder]=json.loads(read(p))
 states=[s for s in results[folder]['states'] if s['label']==label];ck('unique_state_'+folder+label,len(states)==1);s=states[0]
 fine=[a for a in s['runs'] if a['relative_step']==1e-5];ck('two_finest_runs_'+folder+label,{a['kind'] for a in fine}=={'self','transport'} and len(fine)==2)
 for a in fine:
  for field,b in a['summary'].items():
   reg=[x for x in rows if (x['folder'],x['label'],x['kind'],x['field'])==(folder,label,a['kind'],field)]
   ck('six_regions_'+folder+label+a['kind']+field,len(reg)==6)
   z=sum(int(x['zero_normalizers']) for x in reg);inf=sum(int(x['infinite_ratios']) for x in reg)
   ck('masked_inf_matches_'+folder+label+a['kind']+field,inf==b['infinite_ratios'])
   if (folder,label) not in controls:
    ck('forced_masked_zero_'+folder+label+a['kind']+field,z==0)
    ck('forced_masked_inf_'+folder+label+a['kind']+field,inf==0)
    ck('forced_global_zero_'+folder+label+a['kind']+field,b['zero_normalizers']==(2*s['radii'] if field=='Theta' else 0))
   global_rows.append(dict(folder=folder,label=label,kind=a['kind'],field=field,masked_zero=z,masked_infinite=inf,global_zero=b['zero_normalizers'],radii=s['radii']))
by_field={field:{'groups':sum(x['field']==field and (x['folder'],x['label']) not in controls for x in global_rows),'masked_zero_sum':sum(x['masked_zero'] for x in global_rows if x['field']==field and (x['folder'],x['label']) not in controls),'global_zero_sum':sum(x['global_zero'] for x in global_rows if x['field']==field and (x['folder'],x['label']) not in controls),'masked_infinite_sum':sum(x['masked_infinite'] for x in global_rows if x['field']==field and (x['folder'],x['label']) not in controls)} for field in ['F','G','Theta','Omega']}
ck('thermal_axis_instances76012',by_field['Theta']['global_zero_sum']==76012)
control=json.loads(read('verification/residual_manufactured.json'));manufactured=[]
for a in control['polynomial_control']:
 b={}
 for container,key in [('cartesian','Omega'),('cartesian','Theta'),('desingularized','F'),('desingularized','G')]:
  qs=a[container]['normalized_'+key];ids=[i for i,q in enumerate(qs) if q==1.]
  # Exact polynomial N_Theta=N_F=0 everywhere; exact N_Omega=4|x|, N_G=4.
  ck('unit_ratio_zero_exact_normalizer_'+str(a['step'])+key,all(key in ['Theta','F'] or key=='Omega' and control['points'][i][0]==0 for i in ids))
  b[key]=dict(count=len(ids),point_indices=ids)
 manufactured.append(dict(step=a['step'],unit_ratios=b))
ck('three_control_steps',len(manufactured)==3)
source=read('code_independent/farfield_grid_audit.py');reader=read('code_independent/r2_state_values.py');inverse=read('code_independent/adaptive_modal_inverse.py');regional=read('code_independent/regional_grid_summary.py')
for key,fragment in {'residual_sum':'R=t.sum(1);N=abs(t).sum(1)','F_terms':"A*(2*f+x*fx),W[:,1]*fy,-(s.beta-2)*f",'G_terms':"A*(g+x*gx),W[:,1]*gy,g,-(2*f+x*fx)",'forced_source_kept_native':"source in original beta_seed"}.items():ck(key,fragment in source)
ck('r2_map','logz=-np.log1p((r/self.L)**2)/(2*bb);t=-np.expm1(logz)' in reader)
ck('F_G_powers',"p=bb+(2 if kind=='F' else 1)" in reader)
ck('odd_mode_factor','values[...,1::2]*=(r/np.hypot(r,self.L))[...,None]' in reader)
ck('outer_to_infinity','H=np.asarray(self.modes(r/q),dtype=float)[1:]' in inverse and 'quad_vec(outer,0.,1.' in inverse)
ck('regional_counter_mask',"'zero_normalizers': int((normalizer[ix] == 0).sum())" in regional)
proof=read(r/'PROOF.md');prep=json.loads(read(v/'preparation.json'));ck('revised_proof_before_checks',prep['revised_utc']<start.isoformat());ck('proof_hash',hashlib.sha256(proof.encode()).hexdigest()==prep['proof_sha256'])
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=prep['proof_sha256'],passed=sum(x['passed'] for x in checks),total=len(checks),by_field=by_field,manufactured_unit_ratios=manufactured,global_counter_rows=global_rows,inputs=inputs,checks=checks,scope='Stored regional counters after masks versus original full-grid zero counts at finer step. Counts across entries and velocities are sample instances, not distinct physical locations. No new PDE evaluation or interval bound.')
(v/'scope_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:val for k,val in out.items() if k not in ['inputs','checks','global_counter_rows']},indent=2))
for c in checks:
 if not c['passed']:print('FAILED',c)
