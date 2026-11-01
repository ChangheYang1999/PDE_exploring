import sys, time, resource, os, faulthandler; faulthandler.enable()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from logff import *
L=LogFarField.load('ckpt/log_sin1_c3_p512.pkl'); print('loaded', max(L.f), flush=True)
for k in range(3):
    t0=time.time(); n=L.step_fast2(240); print('order', n, 'time %.1f' % (time.time()-t0), 'maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1024, 'cache', len(L._pk), 'deg', len(L.f[n])-1, flush=True)
print('RESUME_TEST_DONE', flush=True)
