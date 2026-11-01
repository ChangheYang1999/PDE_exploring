"""Run code/logseries.py with f_1 = amp*sin(theta) (amplitude rescaling avoids double-precision underflow at high
order; coefficients scale as f_n -> amp^n f_n). Usage: run_logseries_amp.py A B N amp out.jsonl"""
import sys, time, json
sys.path.insert(0, 'code')
import logseries

A, Bd, N, amp, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
open(out, 'w').close()
t0 = time.time()
F, G, stats, res = logseries.run(A, Bd, {1: amp}, N, out=out)
print('time', time.time() - t0, 'amp', amp)
print('resonances', len(res))
