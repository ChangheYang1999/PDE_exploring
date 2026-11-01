"""Run code/logseries_ld.py (long double) with f_1 = sin(theta) (no amplitude rescaling needed: the long double
exponent range is about 1e+-4932). Usage: run_logseries_ld.py A B N out.jsonl"""
import sys, time
sys.path.insert(0, 'code')
import logseries_ld
A, Bd, N, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
open(out, 'w').close()
t0 = time.time()
F, G, stats, res = logseries_ld.run(A, Bd, {1: 1.0}, N, out=out)
print('time', time.time() - t0)
