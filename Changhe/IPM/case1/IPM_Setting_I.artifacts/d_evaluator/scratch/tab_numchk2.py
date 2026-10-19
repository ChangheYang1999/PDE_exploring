# Tabulate vaudit logs of imported numerics states (runs/numchk2/<tag>_vaudit.log). Usage: python3 tab_numchk2.py tag...
import json, sys, re
keys = ('0.1<=r<=2', '2<=r<=10', '10<=r<=100', '100<=r<=1000', '1000<=r<=R', '|X-P|<0.5', '|X-P|<2')
for t in sys.argv[1:]:
    L = open(t + '_vaudit.log').read().splitlines()
    d = json.loads(L[0])
    clx = float(re.search(r"'cl_exporter': ([0-9.]+)", open(t + '_import.log').read()).group(1))
    rows = {}
    for l in L[1:]:
        m = re.match(r'\s*(\S+)\s+flux max (\S+) rms (\S+) \| N_v max (\S+) rms (\S+) \| at r (\S+) th (\S+)', l)
        if m: rows[m.group(1)] = m.groups()[1:]
    J = [l for l in L if l.startswith('J at')][0]
    sp = J.split('spread')[1].split('Jmin')[0].split()
    print(f"{t:12s} cl_id {d['c_l']:.5f} (exp {clx:.5f}) x* {d['x_star']:.4f} hP-1 {d['hP']-1:+.1e} | "
          + ' '.join(f"{k}:{float(rows[k][0]):.1e}/{float(rows[k][2]):.1e}" for k in keys if k in rows)
          + f" | at {rows['|X-P|<2'][4]},{rows['|X-P|<2'][5]} | J.03 {float(sp[5]):.1e} J.01 {float(sp[6]):.1e}")
