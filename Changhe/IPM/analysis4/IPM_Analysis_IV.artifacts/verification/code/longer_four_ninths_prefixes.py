"""Longer independent four-ninths prefixes with isolated evidence paths."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
import other_certified_prefixes as base
from unpack_dyadic4 import unpack
from flint import arb,ctx
from resonance_block_majorant import clean
ROOT=Path('research/179_longer_four_ninths_prefixes')

def main():
    start=time.monotonic();base.ROOT=ROOT;rows=[];failures=[]
    for index in range(1,5):
        try:
            row=base.run_one('two_mode',index,72,3072)
            p=ROOT/'verification'/f'two_mode{index}_checks.json';new=json.loads(p.read_text())
            prior=Path(f'research/176_other_certified_prefixes/verification/two_mode{index}_checks.json');old=json.loads(prior.read_text())
            ctx.prec=3072;norms={r['n']:r for r in new['norms']};harms={r['n']:r for r in new['harmonics']}
            for r in old['norms']:assert arb(*unpack(r['norm_times_n'])).overlaps(arb(*unpack(norms[r['n']]['norm_times_n'])))
            for r in old['harmonics']:
                for key in ['H','sigma']:assert arb(*unpack(r[key])).overlaps(arb(*unpack(harms[r['n']][key])))
            new['prior176_norm_overlaps']=len(old['norms']);new['prior176_harmonic_overlaps']=len(old['harmonics']);new['prior176_sha256']=sha256(prior.read_bytes()).hexdigest();p.write_text(json.dumps(clean(new),indent=2)+'\n')
            rows.append(row)
        except Exception as exc:
            fail=dict(root=index,checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            failures.append(fail);(ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True)
        (ROOT/'verification/partial.json').write_text(json.dumps(clean(dict(rows=rows,failures=failures)),indent=2)+'\n')
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=not failures,rows=rows,failures=failures,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['longer_four_ninths_prefixes.py','other_certified_prefixes.py','pure_cartesian_ball.py','certified_prefix_majorant.py','resonance_block_majorant.py','adaptive_majorant_boxes.py','certified_initial_majorants.py','stream_precision_audit.py','unpack_dyadic4.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':main()
