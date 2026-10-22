"""Interior maxima of both ratios for r < 1e8 from a where2_gpu.py band table (the header's global R/N2 includes the r > 1e8 region where the
direct binary64 evaluation is rounding noise). Usage: python3 wmax.py X.where2.txt [...]"""
import sys, re, os
for f in sys.argv[1:]:
    lines = open(f).read().splitlines(); m1 = m2 = 0; w1 = w2 = ''
    cols = ['0-10', '10-45', '45-80', '80-88', '88-90']
    for ln in lines[2:]:
        if not ln.strip().startswith('r ['): continue
        band = ln.split(':')[0].strip()
        if band.split(',')[0].strip('r [') in ('1e+08', '1e+10'): continue
        for k, tok in enumerate(re.findall(r'([0-9.e+-]+)\[([0-9.e+-]+)\]', ln)):
            a, b = float(tok[0]), float(tok[1])
            if a > m2: m2, w2 = a, '%s deg %s' % (band, cols[k])
            if b > m1: m1, w1 = b, '%s deg %s' % (band, cols[k])
    print('%s: r < 1e8: max R/N %.2e (%s), max R/N2 %.2e (%s)' % (os.path.basename(f).replace('.where2.txt', ''), m1, w1, m2, w2))
