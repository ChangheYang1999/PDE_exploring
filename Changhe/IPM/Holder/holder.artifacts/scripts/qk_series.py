# Q_k via binomial series (see notes): a=k/2-1/4, c=-k/2-1/4,
# Q_k = 2 sum_n C(a,n+4k)C(c,n)/(2n+4k) + 2 sum_m C(a,m)C(c,m+3k)/(2m+3k+1/2)
import mpmath as mp
mp.mp.dps = 30
def Q(k, N=4000):
    a = mp.mpf(k)/2 - mp.mpf(1)/4; c = -mp.mpf(k)/2 - mp.mpf(1)/4
    s1 = mp.nsum(lambda n: mp.binomial(a, n+4*k)*mp.binomial(c, n)/(2*n+4*k), [0, mp.inf])
    s2 = mp.nsum(lambda m: mp.binomial(a, m)*mp.binomial(c, m+3*k)/(2*m+3*k+mp.mpf(1)/2), [0, mp.inf])
    return 2*s1 + 2*s2, 2*s1, 2*s2
for k in range(1, 6):
    q, s1, s2 = Q(k)
    print(k, mp.nstr(q, 20), mp.nstr(s1, 12), mp.nstr(s2, 12), mp.identify(q, ['pi','log(2)','sqrt(2)']))
