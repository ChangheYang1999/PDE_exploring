# One-line table of runs/dirc6c logs: eps, c_l, h(P)-1, x*, near-P / band flux maxima, N_v near P, J(0.03), J(0.01), far N_v (at r)
import sys, json, re
for f in sys.argv[1:]:
    L = open(f).read().splitlines()
    h = next(json.loads(l) for l in L if l.startswith('{"file"'))
    eps = next(eval(l)['eps'] for l in L if l.startswith("{'R'") or l.startswith("{'eps'"))
    rows = {}
    for l in L:
        m = re.match(r'\s+(\S+)\s+flux max (\S+) rms (\S+) \| N_v max (\S+) rms (\S+) \| at r (\S+) th (\S+)', l)
        if m: rows[m.group(1)] = m.groups()[1:]
    sp = [l for l in L if l.startswith('J at')][0].split('spread')[1].split('Jmin')[0].split()
    g = lambda k, i: float(rows[k][i])
    print(f"{eps:+.1e} c_l {h['c_l']:.7f} hP-1 {h['hP']-1:+.2e} x* {h['x_star']:.6f} | X-P<0.5 {g('|X-P|<0.5',0):.3e}/{g('|X-P|<0.5',2):.2e}"
          f" X-P<2 {g('|X-P|<2',0):.3e} 0.1-2 {g('0.1<=r<=2',0):.2e} 10-100 {g('10<=r<=100',0):.3e} 100-1000 {g('100<=r<=1000',0):.2e}"
          f" | J.03 {float(sp[5]):.2e} J.01 {float(sp[6]):.2e} | far N_v {g('1000<=r<=R',2):.2e} at r {rows['1000<=r<=R'][4]}")
