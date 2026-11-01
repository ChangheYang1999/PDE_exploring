import sys, time, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from logff import *
R=RingQ(); allok=True
for (A,B,N,f1) in ((2,3,24,['1']),(4,9,22,['1']),(1,2,20,['1']),(2,3,14,['1','1/3','-1/7'])):
    L1=LogFarField(R,A,B,f1); L2=LogFarField(R,A,B,f1)
    for n in range(2,N+1): L1.step(); L2.step_fast2(N)
    same=all(len(L1.f[n])==len(L2.f[n]) and all(len(a)==len(b) and all(x==y for x,y in zip(a,b)) for a,b in zip(L1.f[n],L2.f[n])) for n in L1.f) and all(all(all(x==y for x,y in zip(a,b)) for a,b in zip(L1.g[n],L2.g[n])) for n in L1.g)
    allok = allok and same; print(f'delta={A}/{B} N={N} f1={f1}: fast2 == slow exactly: {same}', flush=True)
print('FAST2_EQUALITY', 'PASS' if allok else 'FAIL', flush=True)
Ra=RingArb(512); La=LogFarField(Ra,2,3,['1']); t0=time.time(); La.run(96); print(f'arb 2/3 N=96 fast2: {time.time()-t0:.1f}s; order-96 time {La.stats[96]["time"]:.2f}s (fast1: 4.6 s at n=96); deg {len(La.f[96])-1}', flush=True)
