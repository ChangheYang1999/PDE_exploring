"""Independent two-continuation tuned prefixes for the five four-ninths roots."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from pure_cartesian_ball import Tuning,refine_root

def run():
    ctx.prec=1536;start=time.monotonic();root=Path('research/153_four_ninths_finite_prefixes');out=root/'verification'
    source=Path('research/146_four_ninths_profiles/verification/algebraic_certificates.json');data=json.loads(source.read_text());P=list(map(int,data['primitive_coefficients']))
    reference=json.loads(Path('research/149_compact_response_certificates/verification/checks.json').read_text());rows=[];text=lambda v:v.str(65,radius=True)
    for index,rootdata in enumerate(data['real_roots'],1):
        b,I=refine_root(P,rootdata['interval'],1600);solver=Tuning(2,9)
        def progress(n,H,S):print(json.dumps(dict(root=index,n=n,H=text(H),sigma=text(S),elapsed_s=time.monotonic()-start)),flush=True)
        f,g,H=solver.prefix(b,27,progress);norms=[];comparisons=[]
        for n in range(1,28):
            F,G=f[n].norm(),g[n].norm();norms.append(dict(n=n,density_norm=text(F),stream_norm=text(G),density_root=text((F.log()/n).exp()),stream_root=text((G.log()/n).exp())))
        for item in H:
            old=arb(reference['rows'][index-1]['finite'][item['k']-1]['sigma']);assert item['sigma'].overlaps(old)
            comparisons.append(dict(k=item['k'],two_continuation_response=text(item['sigma']),linear_response=text(old),overlap=True))
        row=dict(root_index=index,root_interval=I,root_ball=text(b),maximum_order=27,arithmetic_bits=1536,counts=solver.counts,norms=norms,harmonics=[{k:text(v) if k in ['H','sigma','obstruction'] else v for k,v in item.items()} for item in H],response_comparisons=comparisons,all_checks_pass=True,elapsed_s=time.monotonic()-start)
        (out/('root'+str(index)+'_checks.json')).write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
        print(json.dumps(dict(root=index,all_checks_pass=True,counts=solver.counts,last_norm=norms[-1],elapsed_s=time.monotonic()-start)),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start,source_sha256=sha256(source.read_bytes()).hexdigest(),scope='Finite prefixes and independent response comparison; no empirical infinite radius.')
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['four_ninths_finite_prefixes.py','pure_cartesian_ball.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};(out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/153_four_ninths_finite_prefixes/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
