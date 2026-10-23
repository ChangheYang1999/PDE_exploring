"""dr_cscan.py -- C-scan summary (lead 06:56Z item 2): for each run, c_w at tau = 5, 10, 15, the drift rate d log c_w / d tau (central differences of the
exact-time rows at tau +- 1), a0*, and the sampled core residual |R*|/N_f* (r < 0.1 and 0.1-1 bins) of rho* at the save times.  usage: python3 src/dr_cscan.py tag1 tag2 ..."""
import sys, math, numpy as np, re
print("tag              C     tau   c_w          dlog(c_w)/dtau   a0*        |R*|/Nf* (r<.1, .1-1, 1-100)   |R*| (r<.1, .1-1)   max Nf* (r<.1)")
for tag in sys.argv[1:]:
    rows = {}; samp = {}; C = None
    for line in open(f'runs/{tag}.log'):
        if line.startswith('# dr.py'): m = re.search(r"'C': '([0-9.]+)'", line); C = float(m.group(1)) if m else None
        if line.startswith('#  tau'):
            t = float(line.split()[2]); nums = re.findall(r'\[<\.1 \.1-1 1-100 >100\] = ([^;]+);.*?\|R\*\| = ([^;]+);.*?max Nf\* = ([^;]+);', line)
            if nums: samp[round(t)] = ([float(x) for x in nums[0][0].split()], [float(x) for x in nums[0][1].split()], [float(x) for x in nums[0][2].split()])
        if line.startswith('#') or not line.strip(): continue
        p = line.split('|')[0].split()
        try: rows[round(float(p[0]), 3)] = [float(x) for x in p[:18]]
        except ValueError: pass
    for t in (5, 10, 15):
        if t in rows and (t - 1) in rows and (t + 1) in rows:
            cw = rows[t][2]; rate = (math.log(rows[t + 1][2]) - math.log(rows[t - 1][2])) / 2 if rows[t + 1][2] > 0 and rows[t - 1][2] > 0 else float('nan')
            sr = samp.get(t); sr_s = (f"{sr[0][0]:.2e} {sr[0][1]:.2e} {sr[0][2]:.2e}   {sr[1][0]:.2e} {sr[1][1]:.2e}   {sr[2][0]:.2e}" if sr else '')
            print(f"{tag:16s} {C:4.1f}  {t:4d}  {cw:+.5e}  {rate:+.4f}        {rows[t][4]:+.4e}  {sr_s}")
        elif t in rows:
            print(f"{tag:16s} {C:4.1f}  {t:4d}  {rows[t][2]:+.5e}  (no neighbours)   {rows[t][4]:+.4e}")
