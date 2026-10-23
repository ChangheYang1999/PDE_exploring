"""dr_probes_table.py -- matched-time table of the fixed-point probes ('#P' lines: rho rho_x rho_y U1 U2 R_cx of the DR state at (0.5,0.5), (3,0), (0,3), (6,8), (30,40))
and of the sampled max |R*| and max N_f* per region, from DR logs with exact output times.  usage: python3 src/dr_probes_table.py tag1 tag2 ... [taus=0,5,10,15,20]"""
import sys, re
args = [a for a in sys.argv[1:] if '=' not in a]; kw = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)
taus = [float(x) for x in kw.get('taus', '0,5,10,15,20').split(',')]
pts = ['(0.5,0.5)', '(3.0,0.0)', '(0.0,3.0)', '(6.0,8.0)', '(30.0,40.0)']
for tag in args:
    P = {}; S = {}
    for line in open(f'runs/{tag}.log'):
        if line.startswith('#P tau'):
            t = float(line.split()[2]); body = line.split(']', 1)[1]
            vals = {}
            for seg in body.split(';'):
                seg = seg.strip()
                if not seg: continue
                key, nums = seg.split(':'); vals[key.strip()] = [float(x) for x in nums.split()]
            P[round(t, 3)] = vals
        if line.startswith('#  tau'):
            t = float(line.split()[2]); m = re.search(r'\|R\*\| = ([^;]+); max Nf\* = ([^;]+);', line)
            if m: S[round(t, 3)] = ([float(x) for x in m.group(1).split()], [float(x) for x in m.group(2).split()])
    print(f"=== {tag}")
    print("tau    point        rho            rho_x          rho_y          U1             U2             R_cx")
    for t in taus:
        if t not in P: continue
        for p in pts:
            v = P[t][p]; print(f"{t:5.1f}  {p:11s} " + " ".join(f"{x:+.6e}" for x in v))
        if t in S: print(f"{t:5.1f}  sampled max |R*| [<.1 .1-1 1-100 >100] = " + " ".join(f"{x:.3e}" for x in S[t][0]) + "   max N_f* = " + " ".join(f"{x:.3e}" for x in S[t][1]))
