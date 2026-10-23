# driver v2 (lead, 2026-10-21T18:30Z): as drv.py, but runs tc.py / res3g.py IN-PROCESS (runpy, stdout captured, SIGALRM
# timeout), so that the job is a single process (the CPU guard pauses child processes of a detached job). Skips the
# patterns already recorded in the log file given as argv[3].
import sys, subprocess, ast, re, collections, time, runpy, io, contextlib, signal, os
ms=sys.argv[1]; TO=int(sys.argv[2]); done=set()
if len(sys.argv)>3 and os.path.exists(sys.argv[3]):
    for L in open(sys.argv[3]):
        mm=re.match(r'(\d+ \d+ \d+ \([\d, ]+\)) OPEN',L)
        if mm: done.add(mm.group(1))
class TO_(Exception): pass
def h(sig,frm): raise TO_()
signal.signal(signal.SIGALRM,h)
out=subprocess.run(['python3','classify.py',ms],capture_output=True,text=True).stdout
for line in out.splitlines():
    if not line.endswith('OPEN'): continue
    mm=re.match(r'(\d+) (\d+) (\d+) \(([\d, ]+)\) OPEN',line)
    key=line[:-5]
    if key in done: continue
    m,e,A0=int(mm.group(1)),int(mm.group(2)),int(mm.group(3)); mu=[int(x) for x in mm.group(4).split(',')]
    c=collections.Counter(2*x for x in mu); cl=sorted(c.items(),key=lambda kv:(kv[1],-kv[0]))
    if len(cl)==2:
        (w1,k1),(w2,k2)=cl; script='tc.py'; arg='%d,%d,%d,%d,%d'%(A0,w1,k1,w2,k2)
    elif len(cl)==3 and cl[0][1]==1 and cl[1][1]==1:
        script='res3g.py'; arg='%d,%d,%d,%d,%d'%(A0,cl[0][0],cl[1][0],cl[2][0],cl[2][1])
    else:
        print(line,'UNSUPPORTED',cl,flush=True); continue
    t0=time.time(); buf=io.StringIO(); sys.argv=[script,arg]; to=False
    try:
        signal.alarm(TO)
        with contextlib.redirect_stdout(buf): runpy.run_path(script,run_name='__main__')
    except TO_: to=True
    except Exception as ex: buf.write('EXCEPTION %r\n'%ex)
    finally: signal.alarm(0)
    r=buf.getvalue()
    open('drv_logs/%s_%s.log'%(script[:-3],arg.replace(',','_')),'w').write(r)
    if to: print(line,script,arg,'TIMEOUT %d s'%TO,flush=True); continue
    verdict='NOT EXCLUDED'; info=[]
    for L in r.splitlines():
        if L.startswith('Res') and 'factors' in L:
            lst=ast.literal_eval(L.split(':',1)[1].strip())
            mx=max([max(f[1]) for f in lst if f[1]]+[-1e9]); info.append(round(mx,4))
            if mx<1-1e-9: verdict='EXCLUDED'
        elif 'identically 0' in L: info.append('0')
    print(line,script,arg,verdict,'max real roots',info,'%.0f s'%(time.time()-t0),flush=True)
