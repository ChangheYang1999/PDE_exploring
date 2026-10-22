"""Summarize runs/zjac_*.log into one table ."""
import sys, re, glob
files = sys.argv[1:] or sorted(glob.glob('runs/zjac_*.log'))
for f in files:
    txt = open(f).read()
    m = re.search(r"=== (\S+): N=(\d+) M=(\d+) beta=([\d.]+)\s+a0 sign=([+-]\d)", txt)
    if not m: print(f"{f}: (incomplete)"); continue
    name = m.group(1).split('/')[-1].replace('.npz', ''); N = m.group(2); beta = float(m.group(4)); a0 = m.group(5)
    P = re.search(r"P1=\(([\d.]+), 0\): DW eigen = \[\s*([-\d.e+]+)\s+([-\d.e+]+)\s*\]", txt)
    Y = re.findall(r"Y(\d)=\(0, ([\d.]+)\): DW eigen = \[\s*([-\d.e+]+)\s+([-\d.e+]+)\s*\]", txt)
    print(f"{name} (N={N}, beta={beta:g}, a0={a0}): P=({P.group(1)}) eig ({float(P.group(2)):+.4f}, {float(P.group(3)):+.4f}); y-axis zeros: " + ("; ".join(f"y={y[1]} eig ({float(y[2]):+.3f},{float(y[3]):+.3f})" for y in Y) if Y else "none") if P else f"{name}: no x-axis zero found")
    for z in re.finditer(r"Q=\(([\d.]+),([\d.]+)\) r=([\d.]+): Theta=([-+\d.e]+) Omega=([-+\d.e]+) Theta_x=([-+\d.e]+) Omega-Theta_x=([-+\d.e]+) \|gradTheta\|=([\d.e+-]+) \(Theta_y=([-+\d.e]+)\); DW eig=\[([^\]]+)\] \[([^\]]+)\] det=([-+\d.e]+)", txt):
        x, y, r, Th, Om, Thx, dOm, gT, Thy, eig, kind, det = z.groups()
        eig = re.sub(r"\s+", " ", eig.strip())
        print(f"    Q=({float(x):.3f},{float(y):.3f}) r={float(r):.1f}: Theta={float(Th):+.3e} Omega={float(Om):+.3e} Omega-Theta_x={float(dOm):+.2e} |gradTheta|={float(gT):.3e} eig=[{eig}] {kind} det={float(det):+.3f}")
