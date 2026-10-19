# As tab_dir.py, for any vaudit log (label = file name), plus the global maximum and its location.
import sys, json, re, os
for f in sys.argv[1:]:
    L = open(f).read().splitlines()
    h = next(json.loads(l) for l in L if l.startswith('{"file"'))
    rows = {}
    for l in L:
        m = re.match(r'\s+(\S+)\s+flux max (\S+) rms (\S+) \| N_v max (\S+) rms (\S+) \| at r (\S+) th (\S+)', l)
        if m: rows[m.group(1)] = m.groups()[1:]
    sp = [l for l in L if l.startswith('J at')][0].split('spread')[1].split('Jmin')[0].split()
    g = lambda k, i: float(rows[k][i])
    print(f"{os.path.basename(f)[:22]:22s} c_l {h['c_l']:.7f} hP-1 {h['hP']-1:+.2e} x* {h['x_star']:.6f} | all {g('all',0):.3e} at r {rows['all'][4]} th {rows['all'][5]}"
          f" rms {g('all',1):.2e} | X-P<0.5 {g('|X-P|<0.5',0):.3e} X-P<2 {g('|X-P|<2',0):.3e} 2-10 {g('2<=r<=10',0):.3e} 0.1-2 {g('0.1<=r<=2',0):.2e}"
          f" 10-100 {g('10<=r<=100',0):.3e} 100-1000 {g('100<=r<=1000',0):.2e} | J.03 {float(sp[5]):.2e} J.01 {float(sp[6]):.2e} | N_v all {g('all',2):.2e} far {g('1000<=r<=R',2):.2e}")
