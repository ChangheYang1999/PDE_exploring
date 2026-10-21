# (o8) item 11: N_raw and N_phi of v = -1e-9 u^3 (1 - u^2)^2 with the ndist_ver.py evaluator (definitions only).
src = open('ndist_ver.py').read().split('\npairs = ')[0]
exec(src)
c = v_coeffs([mp.mpf('-1e-9')])
print('coeffs', [mp.nstr(x, 5) for x in c])
for var in ('mono', 'phi'):
    N, parts = ndist(c, var)
    print(var, mp.nstr(N, 12), parts)
print('|v(1/2)| =', mp.nstr(abs(ev(c, mp.mpf(1)/2)), 12))
