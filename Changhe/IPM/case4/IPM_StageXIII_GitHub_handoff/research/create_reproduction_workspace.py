#!/usr/bin/env python3
"""Create a fresh validation workspace without results, sessions, or optimization.

Copies only this task's source and frozen inputs. It never changes a source
workspace or initializes/runs a numerical worker. Existing targets are refused.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import time

ROOT=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination',required=True,type=Path)
    args=parser.parse_args()
    destination=args.destination.expanduser().resolve()
    protected=[Path('/Users/caltech/Changhe/IPM/IPM_R2'),
               Path('/Users/caltech/research/IPM_R2_macpro_reference_20261020'),
               Path('/Users/caltech/research/IPM_R2_macpro_runs/verification_20261020_01'),
               Path('/Users/caltech/research/IPM_R2_macpro_experiments/stage11_five_taylor'),
               Path('/Users/caltech/research/IPM_R2_macpro_experiments/stage12_large_scale'),ROOT]
    if destination.exists() or any(destination==p or p in destination.parents for p in protected):
        raise ValueError('Choose a new destination outside all protected and source workspaces')
    destination.mkdir(parents=True)
    copied={}
    for source in sorted(ROOT.glob('*.py')):
        shutil.copy2(source,destination/source.name)
        copied[source.name]=hashlib.sha256(source.read_bytes()).hexdigest()
    for name in ['base','inputs','hardware','launch_tools']:
        shutil.copytree(ROOT/name,destination/name,copy_function=shutil.copy2)
    for name in ['MATHEMATICAL_DERIVATION.md','OPTIMIZATION_PREPARATION.md','REPRODUCE.md']:
        if (ROOT/name).exists():shutil.copy2(ROOT/name,destination/name)
    (destination/'provenance').mkdir()
    (destination/'results').mkdir()
    shutil.copy2(ROOT/'provenance/base_manifest.json',destination/'provenance/base_manifest.json')
    archived_versions=ROOT/'provenance/source_versions'
    if archived_versions.exists():
        shutil.copytree(archived_versions,destination/'provenance/source_versions',copy_function=shutil.copy2)
    for source in (ROOT/'provenance').glob('*jobs*.json'):
        if source.name.endswith('.state.json'):continue
        plan=json.loads(source.read_text())
        if isinstance(plan,dict) and isinstance(plan.get('jobs'),list):
            shutil.copy2(source,destination/'provenance'/source.name)
    setup_snapshot=ROOT/'provenance/previous_campaign_status_at_setup.json'
    if setup_snapshot.exists():shutil.copy2(setup_snapshot,destination/'provenance'/setup_snapshot.name)
    index_path=destination/'inputs/candidates.json'
    index=json.loads(index_path.read_text())
    for name,row in index['candidates'].items():row['snapshot_path']=str(destination/'inputs'/(name+'.json'))
    index_temporary=index_path.with_name(index_path.name+'.reproduction.partial')
    index_temporary.write_text(json.dumps(index,indent=2)+'\n')
    index_temporary.replace(index_path)
    record={'stage':'XII absolute-loss reproduction only','created_epoch':time.time(),
            'all_writes_restricted_to':str(destination),'base_is_frozen_copy':True,
            'optimization_permitted':False,'reproduces_workspace':str(ROOT),
            'source_python_sha256':copied,'resource_session_copied':False,
            'historical_results_copied':False}
    (destination/'workspace.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'fresh_workspace':str(destination),'next_step':'Initialize its independent resource session; see REPRODUCE.md in the source workspace.'},indent=2))


if __name__=='__main__':main()
