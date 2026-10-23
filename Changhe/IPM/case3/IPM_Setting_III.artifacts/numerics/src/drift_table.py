"""drift_table.py -- tabulate (step, c_l, a0, a0/D, |F|_2, |F|max) along the free-c_l releases from the per-step logs runs/qfree_*.log
(lead 18:06Z item 1).  Also reports the distance of a0/D to the lattice 8 + 4N.  usage: python3 src/drift_table.py runs/qfree_*.log"""
import sys, re
pat = re.compile(r"qfree it (\d+): \|F\|2 ([0-9.e+-]+) -> ([0-9.e+-]+) \(max ([0-9.e+-]+)\) lam=([0-9.e+-]+) cl=([0-9.]+) a0=([0-9.-]+)")
for fn in sys.argv[1:]:
    rows = []
    for line in open(fn):
        m = pat.search(line)
        if m:
            it = int(m.group(1)); nF2 = float(m.group(3)); nFm = float(m.group(4)); cl = float(m.group(6)); a0 = float(m.group(7))
            rows.append((it + 1, cl, a0, a0 / (cl - 1), nF2, nFm))
    if not rows: continue
    print(f"# {fn}: {len(rows)} steps")
    print("  step    c_l           a0         a0/D      nearest 8+4N   |F|_2      |F|max")
    sel = sorted(set([1, 2, 3, 5, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256] + [len(rows)]))
    for (it, cl, a0, ad, n2, nm) in rows:
        if it in sel:
            N = max(0, round((ad - 8) / 4)); lat = 8 + 4 * N
            print(f"  {it:4d}  {cl:.8f}  {a0:10.6f}  {ad:9.4f}   {lat:3d} ({ad-lat:+.2f})   {n2:.2e}   {nm:.2e}")
