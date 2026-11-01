"""Independent Cartesian Q6 prefixes and source-bound finite norm extraction."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,pickle,shutil,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from pure_cartesian_ball import Tuning,refine_root
from integer_period_prefix import inputs
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/185_period_six_numerical_audit')

def one(index,N,bits):
    start=time.monotonic();ctx.prec=bits;Q=6
    coefficients,intervals,lower,paths=inputs(Q);b,I=refine_root(coefficients,intervals[index-1],bits+64)
    p=Path(f'../a4-num/ckpt/tuned13_r{index}_p1024.pkl');raw=p.read_bytes();source=dict(path=str(p),sha256=sha256(raw).hexdigest(),bytes=len(raw));state=pickle.loads(raw);del raw
    assert state['ring']=='arb' and state['prec']==1024 and str(state['delta_exact'])=='1/3'
    maxN=max(state['f']);assert maxN>=max(300,N+Q)
    hp=p.with_name(p.stem+'_H.json');hraw=hp.read_bytes();hd=json.loads(hraw);assert hd['period']==Q and hd['delta']=='1/3'
    assert arb(*unpack(state['f'][1][0]))==1 and arb(*unpack(state['f'][1][1])).contains(b)
    source.update(maximum_order=maxN,harmonics_sha256=sha256(hraw).hexdigest())
    solver=Tuning(1,Q,4)
    def progress(n,H,S):print(json.dumps(dict(root=index,n=n,stage='tuning',actual_elapsed_s=time.monotonic()-start)),flush=True)
    f,g,h=solver.prefix(b,N,progress);compared={'f':0,'g':0};norms=[];harmonics=[]
    for field,series,odd in [('f',f,True),('g',g,False)]:
        for n in range(1,N+1):
            for j,packed in enumerate(state[field][n]):
                m=2*j+(1 if odd else 0);own=series[n].sine(m) if m else arb(0);old=arb(*unpack(packed))
                assert own.overlaps(old),('coefficient_mismatch',field,n,m,own.str(20),old.str(20));compared[field]+=1
            for m in range(2*len(state[field][n])+(1 if odd else 0),4*n+1,2):assert series[n].sine(m).contains(0)
    for row in h:
        n=row['n'];assert row['H'].overlaps(arb(hd['H'][str(n)]['str'])) and row['sigma'].overlaps(arb(hd['sigma'][str(n)]))
        harmonics.append(dict(n=n,H=pack(row['H']),sigma=pack(row['sigma']),obstruction=pack(row['obstruction'])))
    for n in range(1,N+1):norms.append(dict(n=n,F=pack(f[n].norm()),G=pack(g[n].norm())))
    rows=[];selected=set(range(1,N+1))|{n for n in [60,120,180,240,300] if n<=maxN}
    for n in sorted(selected):
        if n%60:continue
        row=dict(n=n)
        for field,label in [('f','F'),('g','G')]:
            if field=='g' and n%Q==0 and n>=2*Q and str(n) not in hd['H']:row['G_status']='untuned final harmonic; norm excluded';continue
            values=[arb(*unpack(v)) for v in state[field][n]];norm=sum(map(abs,values),arb(0));mid=sum((abs(v.mid()) for v in values),arb(0));rad=sum((v.rad() for v in values),arb(0));assert norm>0
            row[label+'_norm']=pack(norm);row[label+'_root']=(norm.log()/n).exp().str(50,radius=True);row[label+'_relative_radius']=(rad/mid).str(30,radius=True)
        rows.append(row)
    selected_state={key:{n:state[key][n] for n in sorted(selected)} for key in ['f','g']};packed=pickle.dumps(selected_state,protocol=4);compressed=gzip.compress(packed,compresslevel=6,mtime=0)
    used=sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file());assert used+len(compressed)<2994000000 and shutil.disk_usage('.').free>20000000000
    archive=ROOT/'verification'/f'root{index}_selected.pkl.gz';archive.write_bytes(compressed)
    source.update(selected_sha256=sha256(packed).hexdigest(),selected_bytes=len(packed),archive=str(archive),archive_sha256=sha256(compressed).hexdigest(),archive_bytes=len(compressed))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,root_interval=I,bits=bits,independent_maximum_order=N,source=source,inputs={str(p):sha256(p.read_bytes()).hexdigest() for p in paths},counts=solver.counts,coefficient_comparisons=compared,harmonics=harmonics,independent_norms=norms,source_norms=rows,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(result,indent=2)+'\n');brief={key:result[key] for key in ['root_index','counts','coefficient_comparisons','actual_elapsed_s']};brief['last_norm']=rows[-1];print(json.dumps(brief),flush=True);return brief

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='6');ap.add_argument('--N',type=int,default=60);ap.add_argument('--bits',type=int,default=3072);args=ap.parse_args();start=time.monotonic();rows=[];failures=[]
    for index in map(int,args.roots.split(',')):
        try:rows.append(one(index,args.N,args.bits))
        except Exception as exc:
            fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),root=index,type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)]);(ROOT/'verification'/f'root{index}_FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');failures.append(fail);print(json.dumps(fail),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=not failures,rows=rows,failures=failures,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'roots{args.roots.replace(",","_")}_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['period_six_numerical_audit.py','pure_cartesian_ball.py','stream_precision_audit.py','certified_initial_majorants.py','integer_period_prefix.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    for name in ['tuned_general.py','tuned_c3.py','tuned_cQ.py','ffcore.py']:(ROOT/'sources'/('numerical_'+name)).write_bytes(Path('../a4-num/code',name).read_bytes())
if __name__=='__main__':main()
