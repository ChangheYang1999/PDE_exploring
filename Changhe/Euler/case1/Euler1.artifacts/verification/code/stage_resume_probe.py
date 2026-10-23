"""Execute an isolated lifecycle reproduction against frozen trainer sources."""
import argparse,importlib.util,json,os,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('mode',choices=['continuous','interrupt','resume']);a=p.parse_args()
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/'snapshots/repair-project-dd9c125438565393'
sys.path.insert(0,str(PROJECT))
spec=importlib.util.spec_from_file_location('audited_train',PROJECT/'train.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# Remove expensive independent diagnostics from this lifecycle test only. Optimization,
# collocation, serialization, counters, RNG and stage transitions are unchanged.
m.validate=lambda *args,**kw:dict(cl=.45,val_score=1.,nonaxi_ratio_core=.1,max_U_sampled=1.,stag_n_zeros=0,ring_n2=.1,ring_n4=.1,inversion_defect_core=.1,zrefl_defect_core=.1)
config=ROOT/'evidence/stage_resume_probe_config.json'
if not config.exists():
 cfg=dict(cl=.45,cl_trainable=False,C=0.,model=dict(width=8,depth=2,feature_set='dir_tau',n_tail=2,zero_last=False),seed=dict(use=True,a=.2,b=-.4,c=.7,trainable=False),sampling=dict(R_core=4.,R_max=16.,r_tube=.2,z_min=.01,R_origin=.5),counts=dict(n_core=8,n_shell=8,n_axis=4,n_origin=4),val_counts=dict(n_core=8,n_shell=8,n_axis=4,n_origin=4),loss=dict(T_lambda=0.,lambda_amp=1.,amp_p=8,n_gauge=8,lambda_nonaxi=0.,log_nonaxi=False),stages=[dict(opt='adam',steps=2,lr=.001,resample_every=5),dict(opt='adam',steps=2,lr=.001,resample_every=5)],eval_every=1000,log_every=1000,ckpt_minutes=10,archive_every_steps=0,rng_seed=7023)
 config.write_text(json.dumps(dict(exp_id='stage_probe',config=cfg),indent=2)+'\n')
if a.mode=='interrupt':
 original=m.atomic_torch_save
 def interrupt_after_stage_advance(obj,path):
  original(obj,path)
  if str(path).endswith('ckpt_last.pt') and obj.get('state',{}).get('stage')==1 and obj['state']['step']==0:
   print('INJECTED EXIT after atomic stage-advance checkpoint',flush=True)
   raise SystemExit(0)
 m.atomic_torch_save=interrupt_after_stage_advance
run=ROOT/'.tmp/stage-resume-probe'/('continuous' if a.mode=='continuous' else 'resumed')
sys.argv=['train.py','--exp',str(config),'--device','cpu','--run-root',str(run),'--no-ledger']
m.main()
