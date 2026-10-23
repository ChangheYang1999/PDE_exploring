"""Bounded counterexamples to the 07:12 repair; no trainer processes are started."""
from pathlib import Path
import ast,datetime,hashlib,json,math
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'snapshots/repair-ledger.py-e5d0d7cc089e51aa.txt'
tree=ast.parse(source.read_text());names={'union_length','exact_and_bounds'}
space={'ts':float}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),str(source),'exec'),space)
# True credited legacy activity has length 1.4 and fits the original subsecond timestamps,
# but floor-to-second endpoints give a wall interval of length one.
legacy=[dict(interval_start=0,interval_end=1,active_seconds=1.4)]
legacy_result=space['exact_and_bounds'](legacy)
assert legacy_result['legacy_upper_seconds']==1.0 < 1.4
# Checkpoint I/O and a short suspension lie between accepted-step endpoint times.
# The implemented branch opens [t_last_step,t] and cannot distinguish their contents.
last_step_end=100.0;io_end=110.0;next_step_end=111.0
accepted_dt=next_step_end-last_step_end
assert accepted_dt<=30.0
recorded=[[last_step_end,next_step_end]]
actual_optimizer=[[io_end,next_step_end]]
chunk_result=space['exact_and_bounds']([dict(chunks=recorded)])
assert chunk_result['exact_union_seconds_chunks']==11.0
assert space['union_length'](actual_optimizer)==1.0
# Stage-advance checkpoint retains cur_batch from the previous stage. If both stages
# begin in block zero, matching only step_drawn accepts the previous stage's batch.
saved={'step_drawn':0,'origin_stage':0};new_stage=1;step=0;resample=5
restored=(saved['step_drawn']==step-step%resample)
assert restored and saved['origin_stage']!=new_stage
# A record explicitly carrying [] really denotes no recorded chunk.
empty=space['exact_and_bounds']([dict(chunks=[],interval_start=0,interval_end=20,active_seconds=20)])
assert empty['exact_union_seconds_chunks']==0 and empty['combined_upper_seconds']==0
out=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 legacy_truncation_counterexample=dict(input=legacy,reported=legacy_result,true_activity_seconds=1.4),
 checkpoint_io_counterexample=dict(recorded_chunks=recorded,eligible_optimizer_intervals=actual_optimizer,reported=chunk_result),
 stage_advance_batch_counterexample=dict(saved=saved,resumed_stage=new_stage,resumed_step=step,incorrectly_restored=restored),
 explicit_empty_chunks_correct=True,all_counterexamples_reproduced=True,
 scope='Executable branch/interval counterexamples, not an Euler numerical experiment. No campaign-time credit.')
(ROOT/'evidence/runtime_repair_counterexamples.json').write_text(json.dumps(out,indent=2)+'\n')
print('Three repair counterexamples and explicit-empty-chunk check passed.')
