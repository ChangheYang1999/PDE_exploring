import numpy as np, sys
from indicial_rec2 import G
def root(A, a0, lo, hi, n):
    glo = G(lo, A, a0, n)[0]; ghi = G(hi, A, a0, n)[0]
    if np.sign(glo) == np.sign(ghi): return None
    for _ in range(55):
        m = 0.5*(lo+hi); gm = G(m, A, a0, n)[0]
        if np.sign(gm) == np.sign(glo): lo, glo = m, gm
        else: hi = m
    return 0.5*(lo+hi)
if __name__ == "__main__":
    # test: jet resonance curves (polynomial Theta): deg3 a0 = 4A ; deg5 3a0^2-(38A+26)a0+128A(A+1) = 0
    A = 2.0
    print("deg3 test A=2 a0=8: G(3) =", G(3.0, A, 8.0, 2000)[0], " G(3.01)=", G(3.01, A, 8.0, 2000)[0], "G(2.99)=", G(2.99, A, 8.0, 2000)[0])
    disc = (38*A+26)**2 - 12*128*A*(A+1)
    for a0 in [((38*A+26)+np.sqrt(disc))/6, ((38*A+26)-np.sqrt(disc))/6]:
        print(f"deg5 test A=2 a0={a0:.6f}: G(5) =", G(5.0, A, a0, 2000)[0], "G(5.01)=", G(5.01, A, a0, 2000)[0])
    print("control A=2 a0=3: G(3)=", G(3.0, A, 3.0, 2000)[0], "G(5)=", G(5.0, A, 3.0, 2000)[0])
    sys.stdout.flush()
    for eps in [0.01, 0.02, 0.05, 0.1, 0.2]:
        A = 1+2*eps; a0 = 4*eps
        rs = []
        for n in [2000, 20000, 200000]:
            r = root(A, a0, 1+0.5*eps, 1+1.5*eps, n); rs.append(r)
        print(f"eps={eps}: (d-1)/eps =", [round((r-1)/eps, 6) for r in rs], " one-mode a0/(A+3)/eps =", round(a0/(A+3)/eps, 6))
        sys.stdout.flush()
