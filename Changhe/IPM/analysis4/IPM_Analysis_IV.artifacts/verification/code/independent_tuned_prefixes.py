"""Finite Q4 audit using two provisional Cartesian continuations per harmonic."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,gzip,pickle,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from pure_cartesian_ball import Tuning,refine_root
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('--roots',default='6');ap.add_argument('--N',type=int,default=40)
ap.add_argument('--bits',type=int,default=1536);args=ap.parse_args()
ctx.prec=args.bits;start=time.monotonic();root=Path('research/148_independent_tuned_prefixes')
source=Path('research/142_period_four_tuning/verification/root_response_certificates.json')
certificate=json.loads(source.read_text());P=list(map(int,certificate['primitive_coefficients_ascending']))
text=lambda x:x.str(65,radius=True)
try:
    for index in map(int,args.roots.split(',')):
        stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        out=root/'verification'/('Q4_root'+str(index)+'_'+stamp);out.mkdir()
        b,interval=refine_root(P,certificate['real_roots'][index-1]['interval'],args.bits+64)
        solver=Tuning(1,4)
        def progress(n,H,S):print(json.dumps(dict(root=index,n=n,H=text(H),sigma=text(S),elapsed_s=time.monotonic()-start)),flush=True)
        f,g,harmonics=solver.prefix(b,args.N,progress)
        comparisons=[];source_path=Path('../a4-num/ckpt/tunedQ4_r'+str(index)+'_p1024.pkl')
        if source_path.exists():
            raw=source_path.read_bytes();source_sha=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
            sourceN=max(state['f']);N=min(args.N,sourceN-4)
            assert state['ring']=='arb' and state['prec']==1024
            assert arb(*unpack(state['f'][1][1])).contains(b)
            selected={key:{n:state[key][n] for n in range(1,N+1)} for key in ['f','g']}
            for key,series,odd in [('f',f,True),('g',g,False)]:
                count=0
                for n in range(1,N+1):
                    for j,packed in enumerate(selected[key][n]):
                        old=arb(*unpack(packed));m=2*j+(1 if odd else 0)
                        own=series[n].sine(m) if m else arb(0)
                        assert own.overlaps(old),('source_mismatch',index,key,n,m,text(own),text(old));count+=1
                comparisons.append(dict(field=key,maximum_order=N,coefficients=count,all_overlap=True))
            packed=pickle.dumps(selected,protocol=4);archive=gzip.compress(packed,compresslevel=6,mtime=0)
            (out/'selected_source.pkl.gz').write_bytes(archive)
            source_info=dict(path=str(source_path),sha256=source_sha,source_maximum_order=sourceN,selected_maximum_order=N,
                             archive_sha256=sha256(archive).hexdigest(),selected_sha256=sha256(packed).hexdigest(),selected_bytes=len(packed))
        else:source_info=dict(path=str(source_path),available=False)
        rows=[]
        for n in range(1,args.N+1):
            F,G=f[n].norm(),g[n].norm()
            rows.append(dict(n=n,density_norm=text(F),stream_norm=text(G),density_root=text((F.log()/n).exp()),stream_root=text((G.log()/n).exp())))
        hrows=[{k:text(v) if k in ['H','sigma','obstruction'] else v for k,v in row.items()} for row in harmonics]
        result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,Q=4,h=1,root_index=index,
                    maximum_order=args.N,arithmetic_bits=args.bits,root_interval=interval,root_ball=text(b),counts=solver.counts,
                    source=source_info,comparisons=comparisons,norms=rows,harmonics=hrows,actual_elapsed_s=time.monotonic()-start,
                    scope='Finite Cartesian enclosures and source comparisons. No improved infinite radius is inferred.')
        (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
        for name in ['pure_cartesian_ball.py','independent_tuned_prefixes.py','stream_precision_audit.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
        files={p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()}
        (out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
        print(json.dumps(dict(root=index,all_checks_pass=True,comparisons=comparisons,elapsed_s=time.monotonic()-start)),flush=True)
except Exception as exc:
    import traceback
    failure=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start)
    (root/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
