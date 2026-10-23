"""parse_lowslope.py -- table of the low-slope batch (runs/lowslope.out): tag, c_l end, a0, D = c_l - 1, a0/D, steps, |F|max, between-node bins."""
import re, sys
for l in open(sys.argv[1] if len(sys.argv) > 1 else 'runs/lowslope.out'):
    if not l.startswith('QFREE'): continue
    kind = 'fixed' if 'fixed-cl' in l else 'free '; start = re.search(r'from runs/(\S+)\.pt', l).group(1); size = re.search(r'(\d+x\d+)', l).group(1)
    cl = float(re.findall(r'(?<!start )cl=([0-9.]+)', l)[-1]); a0 = float(re.search(r'a0=([-0-9.e]+)', l).group(1)); its = re.search(r'its=(\d+)', l).group(1)
    fmax = re.search(r'\|F\|max=(\S+)', l).group(1); bins = re.search(r'/Nf=\[([^\]]*)\]', l).group(1); D = cl - 1
    print(f"{kind} {size:7s} from {start:26s} -> c_l = {cl:.6f}  a0 = {a0:+.5f}  a0/D = {a0/D:8.3f}  steps {its:>3s}  |F|max {fmax}  bins {bins}")
