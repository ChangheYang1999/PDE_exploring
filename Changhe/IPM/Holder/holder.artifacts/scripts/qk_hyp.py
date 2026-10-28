# Q_k = int |G| cos(2k arg G) dA,  G(w) = w/(pi (w^2-1/4)^2), via two 3F2(1) series (derived in notes/maximality.md).
import mpmath as mp
mp.mp.dps = 30
def Qk(k):
    a = mp.mpf(k)/2 - mp.mpf(1)/4; c = -mp.mpf(k)/2 - mp.mpf(1)/4
    t0 = mp.binomial(a, 4*k)/(4*k)
    S1 = t0*mp.hyp3f2(4*k - a, -c, 2*k, 4*k + 1, 2*k + 1, 1)
    s0 = mp.binomial(c, 3*k)/(3*k + mp.mpf(1)/2)
    S2 = s0*mp.hyp3f2(-a, 3*k - c, mp.mpf(3*k)/2 + mp.mpf(1)/4, 3*k + 1, mp.mpf(3*k)/2 + mp.mpf(5)/4, 1)
    return 2*S1 + 2*S2
if __name__ == "__main__":
    for k in range(1, 13):
        q = Qk(k)
        print(k, mp.nstr(q, 15), mp.nstr(k*abs(q), 15), flush=True)
    print("1/(2 sqrt3) =", mp.nstr(1/(2*mp.sqrt(3)), 15))
