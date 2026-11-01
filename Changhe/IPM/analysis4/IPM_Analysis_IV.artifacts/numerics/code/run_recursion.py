"""CLI driver for the far-field recursion.
usage: run_recursion.py --tag T --ring {fmpq,arb,float} [--prec BITS] --cl CL --f1 SPEC --N N [--ckpt-every 10] [--resume]
  CL   : exact rational string 'p/q', decimal string, or 'sqrt5' (delta = 1/sqrt5, c_l = (5+sqrt5)/4), or 'cand007'
  SPEC : 'cand007' | 'sin1' | 'coeffs:a0,a1,...' (odd sine coefficients, rational strings) | 'json:FILE' (list of strings)
         optional suffix '@scale' multiplies f_1 by a rational scale.
Writes logs/<tag>.jsonl (per-order stats) and ckpt/<tag>.pkl.
"""
import sys, os, json, argparse, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(LANE)

def parse_f1(spec, R):
    scale = None
    if '@' in spec: spec, scale = spec.split('@'); scale = R.scalar(scale)
    if spec == 'cand007':
        d = json.load(open(os.path.join(LANE, 'notes', 'cand007_f1.json')))
        a = [R.scalar(x) for x in d['f1_sine_coefficients_exact']]
    elif spec == 'sin1': a = [R.scalar(1)]
    elif spec.startswith('coeffs:'): a = [R.scalar(x) for x in spec[7:].split(',')]
    elif spec.startswith('json:'): a = [R.scalar(x) for x in json.load(open(spec[5:]))]
    else: raise ValueError(spec)
    if scale is not None: a = [x * scale for x in a]
    return a

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tag', required=True); ap.add_argument('--ring', default='arb'); ap.add_argument('--prec', type=int, default=256)
    ap.add_argument('--cl', default='cand007'); ap.add_argument('--f1', default='cand007'); ap.add_argument('--N', type=int, default=100)
    ap.add_argument('--ckpt-every', type=int, default=10); ap.add_argument('--resume', action='store_true')
    ap.add_argument('--stop-rel-rad', type=float, default=1e-6); ap.add_argument('--continue-after-resonance', action='store_true')
    args = ap.parse_args()
    R = make_ring(args.ring, args.prec)
    ck = os.path.join(LANE, 'ckpt', args.tag + '.pkl'); lg = os.path.join(LANE, 'logs', args.tag + '.jsonl')
    if args.resume and os.path.exists(ck):
        ff = FarField.load(ck); mode = 'a'
    else:
        if args.cl == 'cand007':
            cl = json.load(open(os.path.join(LANE, 'notes', 'cand007_f1.json')))['c_l_exact']; delta = None
        elif args.cl == 'sqrt5':
            if R.name == 'arb': delta = arb(1) / arb(5).sqrt()
            elif R.name == 'float': delta = 5 ** -0.5
            else: raise ValueError('sqrt5 needs arb or float ring')
            cl = None
        else: cl = args.cl; delta = None
        f1 = parse_f1(args.f1, R)
        ff = FarField(R, cl, f1, delta=delta); mode = 'w'
    with open(lg, mode) as log:
        print(json.dumps({'tag': args.tag, 'ring': R.name, 'prec': getattr(R, 'prec', None), 'c_l': R.to_float(ff.c_l), 'delta': R.to_float(ff.delta),
                          'f1': [R.to_float(x) for x in ff.f[1]], 'N_target': args.N, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}), file=log, flush=True)
        if mode == 'w':
            from ffcore import _logrow; print(json.dumps(_logrow(ff.stats[1])), file=log, flush=True)
        ff.run(args.N, log=log, ckpt=ck, ckpt_every=args.ckpt_every, stop_rel_rad=args.stop_rel_rad, continue_after_resonance=args.continue_after_resonance)
        print(json.dumps({'done': True, 'N': max(ff.f), 'end_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}), file=log, flush=True)

if __name__ == '__main__': main()
