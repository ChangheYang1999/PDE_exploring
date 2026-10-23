"""Tabulate runs/hs_quadcheck*.txt (src/hs_quadcheck.py output): per state the max |R_h|/N_f by region with the default inner rule (n_in 32, as in the 4P tables)
and with the core-resolving rule, and their ratio.  Usage: python3 src/hs_quadtable.py runs/hs_quadcheck.txt runs/hs_quadcheck_all_part1.txt ..."""
import sys, re
rows = {}
for f in sys.argv[1:]:
    for line in open(f):
        if 'points with' not in line: continue
        tag = line.split()[0]; m = re.search(r'by region \(log rule / n_in32\): (.*)$', line.strip())
        if not m: continue
        regs = re.findall(r'\[([^,]+),([^)]+)\) ([0-9.e+-]+) / ([0-9.e+-]+)', m.group(1))
        mx = re.search(r'max \|R\|/N_f: n_in32 ([0-9.e+-]+), n_in24_t80 ([0-9.e+-]+), n_in1024 ([0-9.e+-]+), log ([0-9.e+-]+)', line)
        rows[tag] = (regs, mx.groups() if mx else None, re.search(r'r >= ([0-9.]+)', line).group(1))
print("# max |R_h|/N_f by region: resolved rule / default n_in 32 (ratio); 'rmin' = smallest radius of the point set")
for tag, (regs, mx, rmin) in rows.items():
    cells = []
    for lo, hi, a, b in regs:
        a, b = float(a), float(b); cells.append(f"[{float(lo):.0e},{float(hi):.0e}): {a:.2e} / {b:.2e} ({a/b:.2f})")
    print(f"{tag:28s} rmin {rmin:>4s}  " + "  ".join(cells))
