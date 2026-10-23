# driver (lead, 2026-10-21): for each OPEN pattern of classify.py at the given m, run tc.py (two weight classes) or
# res3g.py (two singleton classes + one class); verdict EXCLUDED if some resultant has all real roots of all its
# nonconstant factors < 1 (so it is nonzero for every real n >= 1). Other class structures: UNSUPPORTED.
import sys, subprocess, ast, re, collections, time
ms=sys.argv[1]; TO=int(sys.argv[2]) if len(sys.argv)>2 else 1200
out=subprocess.run(['python3','classify.py',ms],capture_output=True,text=True).stdout
for line in out.splitlines():
    if not line.endswith('OPEN'): continue
    mm=re.match(r'(\d+) (\d+) (\d+) \(([\d, ]+)\) OPEN',line)
    m,e,A0=int(mm.group(1)),int(mm.group(2)),int(mm.group(3)); mu=[int(x) for x in mm.group(4).split(',')]
    c=collections.Counter(2*x for x in mu); cl=sorted(c.items(),key=lambda kv:(kv[1],-kv[0]))
    if len(cl)==2:
        (w1,k1),(w2,k2)=cl; script='tc.py'; arg='%d,%d,%d,%d,%d'%(A0,w1,k1,w2,k2)
    elif len(cl)==3 and cl[0][1]==1 and cl[1][1]==1:
        script='res3g.py'; arg='%d,%d,%d,%d,%d'%(A0,cl[0][0],cl[1][0],cl[2][0],cl[2][1])
    else:
        print(line,'UNSUPPORTED',cl,flush=True); continue
    t0=time.time()
    try:
        r=subprocess.run(['python3',script,arg],capture_output=True,text=True,timeout=TO).stdout
    except subprocess.TimeoutExpired:
        print(line,script,arg,'TIMEOUT %d s'%TO,flush=True); continue
    verdict='NOT EXCLUDED'; info=[]
    for L in r.splitlines():
        if L.startswith('Res') and 'factors' in L:
            lst=ast.literal_eval(L.split(':',1)[1].strip())
            mx=max([max(f[1]) for f in lst if f[1]]+[-1e9]); info.append(round(mx,4))
            if mx<1-1e-9: verdict='EXCLUDED'
        elif 'identically 0' in L: info.append('0')
    print(line,script,arg,verdict,'max real roots',info,'%.0f s'%(time.time()-t0),flush=True)
    open('drv_logs/%s_%s.log'%(script[:-3],arg.replace(',','_')),'w').write(r)
