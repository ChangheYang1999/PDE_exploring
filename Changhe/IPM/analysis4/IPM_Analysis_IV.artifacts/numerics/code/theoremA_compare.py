"""Compare observed growth with Theorem A quantities: y_n = n alpha_n / d_n, A_obs(n) = (n alpha_n)^{1/n}, y_n^{1/n}.
usage: theoremA_compare.py LOG [A_rigorous]"""
import json, sys, math
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]; hdr = rows[0]
st = {r['n']: r for r in rows if 'n' in r and 'log10_l1' in r}
Arig = float(sys.argv[2]) if len(sys.argv) > 2 else None
N = max(st); print(f"{sys.argv[1]}: c_l={hdr['c_l']:.9f} delta={hdr['delta']:.9f} alpha_1={10**st[1]['log10_l1']:.4g} N={N}")
print(f"{'n':>5} {'alpha_n':>11} {'d_n':>8} {'y_n':>11} {'(n alpha_n)^(1/n)':>18} {'y_n^(1/n)':>10} {'Lambda_n':>9}")
ymax = -1e9
for n in sorted(st):
    r = st[n]; la = r['log10_l1']; d = r['d_n']
    ly = math.log10(n) + la - (math.log10(d) if d > 0 else -300)
    ymax = max(ymax, ly / n)
    if n % max(1, N // 20) == 0 or n <= 5 or n == N:
        print(f"{n:5d} {10**la if -300<la<300 else float('nan'):11.3e} {d:8.4f} {10**ly if -300<ly<300 else float('nan'):11.3e} {10**((math.log10(n)+la)/n):18.5f} {10**(ly/n):10.5f} {r.get('Lambda', float('nan')):9.3f}")
print(f"A_obs = (N alpha_N)^(1/N) = {10**((math.log10(N)+st[N]['log10_l1'])/N):.5f};  sup_n y_n^(1/n) = {10**ymax:.5f}" + (f";  rigorous A = {Arig:.4g}  (A / A_obs = {Arig/10**((math.log10(N)+st[N]['log10_l1'])/N):.3g})" if Arig else ''))
