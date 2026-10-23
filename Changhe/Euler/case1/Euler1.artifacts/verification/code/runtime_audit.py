"""Small reproducible counterexamples for the audited trainer lifecycle code.

Only the pure union_seconds function is extracted from the saved source. No
trainer modules, GPU jobs, servers, or external resources are invoked.
"""
from __future__ import annotations
import ast
import copy
import datetime
import hashlib
import math
from pathlib import Path
import torch
from evaluate import ROOT,atomic_json,utc

def main():
    torch.set_num_threads(1)
    source=ROOT/"snapshots/ledger.py-06e47f50bba8b39a.txt"
    tree=ast.parse(source.read_text())
    func=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="union_seconds")
    space={"ts":float}
    exec(compile(ast.Module(body=[func],type_ignores=[]),str(source),"exec"),space)
    records=[dict(interval_start=0,interval_end=2,active_seconds=1),dict(interval_start=0,interval_end=1,active_seconds=1)]
    estimated,plain=space["union_seconds"](records)
    ledger=dict(records=records,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        density_estimate=estimated,covered_wall_seconds=plain,
        true_union_if_A_active_first_second=1.,true_union_if_A_active_second_second=2.,
        conclusion="Identical records allow different true unions. Density estimate can overcount or undercount.")
    assert estimated==1.5
    # Two unit-volume disjoint cells. Origin sampler repeats the first cell.
    residual=[1.,0.];denominator=[1.,1.]
    true_ratio=math.sqrt(sum(v*v for v in residual)/sum(v*v for v in denominator))
    overlap_ratio=math.sqrt((2*residual[0]**2+residual[1]**2)/(2*denominator[0]**2+denominator[1]**2))
    weights=dict(true_physical_ratio=true_ratio,overlapping_sampler_ratio=overlap_ratio,
                 relative_change=overlap_ratio/true_ratio-1,conclusion="Overlapping physical weights do not cancel in a residual ratio.")
    assert abs(overlap_ratio-true_ratio)>.1
    model=torch.nn.Linear(1,1,bias=False,dtype=torch.float64)
    with torch.no_grad():model.weight.fill_(1.)
    saved=model.state_dict();cloned=copy.deepcopy(saved)
    before=float(saved["weight"].item())
    with torch.no_grad():model.weight.fill_(float("nan"))
    model.load_state_dict(saved)
    alias=dict(checkpoint_before_mutation=before,saved_tensor_became_nan=bool(torch.isnan(saved["weight"]).all()),
               reloading_alias_restored_finite=bool(torch.isfinite(model.weight).all()),
               independent_copy_remained_finite=bool(torch.isfinite(cloned["weight"]).all()))
    assert alias["saved_tensor_became_nan"] and not alias["reloading_alias_restored_finite"]
    g=torch.Generator().manual_seed(92031)
    retained_batch=torch.rand(16,generator=g,dtype=torch.float64)
    saved_rng=g.get_state().clone()
    resumed_g=torch.Generator();resumed_g.set_state(saved_rng)
    redrawn_batch=torch.rand(16,generator=resumed_g,dtype=torch.float64)
    resume=dict(max_current_batch_difference=float((retained_batch-redrawn_batch).abs().max()),
                conclusion="Saving only the post-draw RNG state cannot recreate the batch retained across a resampling block.")
    assert resume["max_current_batch_difference"]>0
    C=2.;norm_dzU=3.
    drift=dict(C=C,dzU_norm=norm_dzU,correct_drift_norm=abs(C)*norm_dzU,
               twice_scaled_drift_norm=abs(C)*(abs(C)*norm_dzU),
               scope="Current runs use C=0, so this source defect is dormant in those runs.")
    result=dict(observed_utc=utc(),ledger=ledger,weights=weights,state_dict_alias=alias,
                retained_batch_resume=resume,drift_normalization=drift,all_counterexamples_reproduced=True,
                scope="Source-defect counterexamples, not Euler experiments; these seconds are not counted in the numerical campaign.")
    atomic_json(ROOT/"evidence/runtime_counterexamples.json",result)
    print("All five counterexamples reproduced.")

if __name__=="__main__":main()
