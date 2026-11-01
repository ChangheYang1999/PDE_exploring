"""Construct and exercise a local-only repair of the checkpoint lineage defect."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import difflib, importlib.util, json, pickle, sys, time
sys.dont_write_bytecode=True
sys.path.insert(0,'../a4-num/code')
BASE=Path('research/190_reset_provenance_roundtrip')
start=time.monotonic();source=Path('../a4-num/code/logff.py').read_text()
old="                 'stats': self.stats, 'resonances': self.resonances}"
new="""                 'stats': self.stats, 'resonances': self.resonances,
                 'radii_reset_at': getattr(self, 'radii_reset_at', None),
                 'perturbed_seed': getattr(self, 'perturbed_seed', None)}"""
assert source.count(old)==1
fixed=source.replace(old,new)
old="        obj.stats = state['stats']; obj.resonances = state['resonances']; return obj"
new="""        obj.stats = state['stats']; obj.resonances = state['resonances']
        # Legacy checkpoints retained reset provenance in earlier statistic rows.
        # Any such ancestor keeps all later coefficients conditional.
        resets = [row['radii_reset_at'] for row in obj.stats.values()
                  if row.get('radii_reset_at') is not None]
        if state.get('radii_reset_at') is not None:
            resets.append(state['radii_reset_at'])
        obj.radii_reset_at = min(resets) if resets else None
        obj.perturbed_seed = state.get('perturbed_seed')
        return obj"""
assert fixed.count(old)==1
fixed=fixed.replace(old,new)
path=BASE/'sources/logff_proposed.py';path.write_text(fixed)
patch=''.join(difflib.unified_diff(source.splitlines(True),fixed.splitlines(True),fromfile='code/logff.py',tofile='code/logff.py'))
(BASE/'sources/reset_provenance_proposed.patch').write_text(patch)
spec=importlib.util.spec_from_file_location('verifier_logff_proposed',path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
rows=[]
for name,reset,seed,legacy in [('unreset',None,None,False),('midpoint_reset',1,None,False),('boundary_perturbed',1,20261031,False),('legacy_reset',1,None,True)]:
    obj=module.LogFarField(module.make_ring('arb',128),2,3,['1'])
    if reset is not None:obj.radii_reset_at=reset
    if seed is not None:obj.perturbed_seed=seed
    obj._stats(1)
    output=BASE/'verification'/('proposed_'+name+'.pkl');obj.save(str(output))
    if legacy:
        data=pickle.loads(output.read_bytes());del data['radii_reset_at'];del data['perturbed_seed']
        output.write_bytes(pickle.dumps(data,protocol=4))
    loaded=module.LogFarField.load(str(output));loaded._stats(1)
    assert getattr(loaded,'radii_reset_at',None)==reset
    assert getattr(loaded,'perturbed_seed',None)==seed
    assert loaded.stats[1]['midpoint_only']==(reset is not None)
    pack = lambda state: {n: [[module._arb_pack(x) for x in column] for column in values] for n, values in state.items()}
    from logff import LogFarField as OriginalLogFarField
    baseline = OriginalLogFarField.load(str(output))
    assert pack(loaded.f)==pack(baseline.f) and pack(loaded.g)==pack(baseline.g)
    rows.append(dict(case=name,reset_at=reset,seed=seed,midpoint_only=loaded.stats[1]['midpoint_only'],coefficient_arrays_equal_to_unmodified_loader=True))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,scope='Local proposed copy only; numerical lane source and active processes were not changed.',source_sha256=sha256(source.encode()).hexdigest(),proposed_sha256=sha256(fixed.encode()).hexdigest(),patch_sha256=sha256(patch.encode()).hexdigest(),tests=rows,actual_elapsed_s=time.monotonic()-start)
(BASE/'verification/proposed_fix_checks.json').write_text(json.dumps(result,indent=2)+'\n')
(BASE/'sources/propose_reset_provenance_fix.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result,indent=2))
