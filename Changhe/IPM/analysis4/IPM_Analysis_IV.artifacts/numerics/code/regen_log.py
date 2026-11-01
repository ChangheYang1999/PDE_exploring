"""Recompute all per-order statistics from a checkpoint (full state) and write logs/<tag>.regen.jsonl.
usage: regen_log.py ckpt/<tag>.pkl [out.jsonl]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
import ffcore
_logrow = ffcore._logrow
if sys.argv[1] == '--log':
    from logff import LogFarField
    ck = sys.argv[2]; L = LogFarField.load(ck)
    out = os.path.join(os.path.dirname(os.path.dirname(ck)), 'logs', os.path.basename(ck)[:-4] + '.regen.jsonl')
    with open(out, 'w') as log:
        print(json.dumps({'tag': os.path.basename(ck)[:-4], 'ring': L.R.name, 'prec': getattr(L.R, 'prec', None), 'delta': str(L.delta_exact), 'c_l': str(L.c_exact), 'log_series': True, 'regenerated_from': os.path.basename(ck)}), file=log)
        for n in sorted(L.f):
            L._stats(n); print(json.dumps(L.stats[n]), file=log)
        print(json.dumps({'done': True, 'N': max(L.f), 'regenerated': True}), file=log)
    print('wrote', out, 'orders', max(L.f)); sys.exit(0)
ck = sys.argv[1]; ff = FarField.load(ck)
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.dirname(ck)), 'logs', os.path.basename(ck)[:-4] + '.regen.jsonl')
R = ff.R
with open(out, 'w') as log:
    print(json.dumps({'tag': os.path.basename(ck)[:-4], 'ring': R.name, 'prec': getattr(R, 'prec', None), 'c_l': R.to_float(ff.c_l), 'delta': R.to_float(ff.delta),
                      'f1': [R.to_float(x) for x in ff.f[1]], 'N_target': max(ff.f), 'regenerated_from': os.path.basename(ck)}), file=log)
    for n in sorted(ff.f):
        old = ff.stats.get(n, {}); keep = {k: old[k] for k in ('min_active_den', 'min_active_den_j', 'resonances', 'time') if k in old}
        ff.stats[n] = keep; ff._fill_stats(n); print(json.dumps(_logrow(ff.stats[n])), file=log)
    if ff.stopped: print(json.dumps({'stop': ff.stopped['reason'], 'n': ff.stopped['n']}), file=log)
    print(json.dumps({'done': True, 'N': max(ff.f), 'regenerated': True}), file=log)
print('wrote', out, 'orders', max(ff.f))

# usage for logarithmic checkpoints: regen_log.py --log ckpt/log_<tag>.pkl  (handled below if the first argument is --log)
