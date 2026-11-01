"""Replay retained formal-jet intervals and compare the separate second-jet run."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
ctx.prec=4096
root=Path('research/159_higher_parameter_jets')
oldpath=Path('research/157_formal_parameter_curve/verification/second_jet_checks.json')
old=json.loads(oldpath.read_text())['rows'];results=[]
for index in [1,2]:
    path=root/f'verification/root{index}_checks.json';data=json.loads(path.read_text());assert data['max_jet']==12
    previous=None;comparisons=0;slopechecks=0;rows=[]
    for row in data['rows']:
        j=row['j'];m,e,r,re=row['beta_exact_dyadic'];v=arb(int(m))*arb(2)**e+arb(0,arb(int(r))*arb(2)**re)
        assert arb(row['beta']).contains(v)
        if j<=2:assert v.overlaps(arb(old[index-1]['beta'+str(j)]))
        if previous is not None:
            ratio=abs(v/previous);assert arb(row['ratio_abs']).overlaps(ratio);assert arb(row['ratio_over_j']).overlaps(ratio/j)
        if row['slope_check']:
            assert arb(row['predicted_slope']).overlaps(arb(row['observed_slope']));slopechecks+=1
        n=3*(j+1);assert row['constant_comparisons']==2*n*(n+1)
        for label in ['counts_zero','counts_tuned']:
            assert row[label]['ordered_products']==n*(n-1)//2
            assert row[label]['compatible_simple_divisions']==2*j
        comparisons+=row['constant_comparisons'];previous=v
        rows.append(dict(j=j,beta=row['beta'],relative_radius=(v.rad()/abs(v.mid())).str(40,radius=True)))
    results.append(dict(root_index=index,source_sha256=sha256(path.read_bytes()).hexdigest(),constant_comparisons=comparisons,independently_checked_slopes=slopechecks,rows=rows,last=data['rows'][-1]))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,roots=results,separate_second_jet_source=str(oldpath),separate_second_jet_sha256=sha256(oldpath.read_bytes()).hexdigest())
(root/'verification/replay.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/check_higher_parameter_jets.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(all_checks_pass=True,roots=[dict(root_index=r['root_index'],constant_comparisons=r['constant_comparisons'],slopes=r['independently_checked_slopes'],last_beta=r['last']['beta'],last_ratio=r['last']['ratio_abs'],last_relative_radius=r['rows'][-1]['relative_radius']) for r in results])))
