import mpmath as mp
mp.mp.dps = 30
Av = mp.mpf('10.150725214760579'); a0 = -4-2/Av; q = 4/Av
K = 8; N = 400
cs = [mp.binomial(q-1, k)*(-1)**k for k in range(N)]
def fp_euler(a):
    # FP int_0^1 t^(a-1)(1-t)^(q-1) dt: on [0,1/4] the remainder series is integrated termwise exactly,
    # on [1/4,1] the remainder is computed directly.
    s1 = sum(cs[k]*mp.mpf(1)/4**(a+k)/(a+k) for k in range(K, N))
    f = lambda t: t**(a-1)*((1-t)**(q-1)-sum(cs[k]*t**k for k in range(K)))
    s2 = mp.quad(f, [mp.mpf(1)/4, mp.mpf(3)/4, 1])
    return s1 + s2 + sum(cs[k]/(a+k) for k in range(K))
print([mp.nstr(fp_euler(a0+j)/mp.beta(a0+j, q)-1, 5) for j in range(3)])
