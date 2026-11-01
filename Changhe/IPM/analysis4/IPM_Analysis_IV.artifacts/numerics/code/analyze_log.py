import json, sys, math
def load(path):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    hdr = rows[0]; st = [r for r in rows if 'n' in r and 'L2' in r]
    return hdr, st
def report(path, every=10, norm='L2'):
    hdr, st = load(path)
    print(f"== {path}: ring={hdr.get('ring')} prec={hdr.get('prec')} c_l={hdr.get('c_l')} delta={hdr.get('delta')} f1[0]={hdr.get('f1',[None])[0]}")
    N = st[-1]['n']; print(f"   orders computed: {N}")
    byn = {r['n']: r for r in st}
    a1 = byn[1][norm]
    print(f"   {'n':>5} {'K':>6} {norm:>12} {'ratio':>9} {'root':>9} {'root/|f1|':>10} {'minden':>10} {'j*':>4} {'argmax_k':>8} {'relrad':>9} {'bits':>6}")
    for n in sorted(byn):
        if n % every == 0 or n <= 10 or n == N:
            r = byn[n]; prev = byn.get(n - 1)
            ratio = r[norm] / prev[norm] if prev and prev[norm] > 0 else float('nan')
            root = r[norm] ** (1 / n) if r[norm] > 0 else 0
            print(f"   {n:5d} {r['K']:6d} {r[norm]:12.4e} {ratio:9.4f} {root:9.4f} {root / a1:10.4f} {r['min_active_den']:10.4f} {r['min_active_den_j'] or 0:4d} {r['argmax_k']:8d} {r.get('max_rel_rad', 0):9.2e} {r.get('max_bits', r.get('den_bits', 0)) or 0:6d}")
if __name__ == '__main__':
    every = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    report(sys.argv[1], every)
