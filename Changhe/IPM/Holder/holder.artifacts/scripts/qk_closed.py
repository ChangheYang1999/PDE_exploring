# Check: closed form Q_k = ((-1)^k/(2k)) G(k/2+3/4) G(3k/2+1/4) / (G(k/2+1/4) G(3k/2+3/4))
# against the 3F2 series (qk_hyp.Qk); monotonicity of r_k = k|Q_k|; and the Fourier identity
# N(pi/4) - N(0) = (4/pi) sum_{k odd} |Q_k|/(4k^2-1), to compare with the direct values 0.4023257139688609 - Lambda_0(0).
import mpmath as mp, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from qk_hyp import Qk
mp.mp.dps = 30
G = mp.gamma
def Qc(k):
    k = mp.mpf(k)
    return (-1)**int(k)/(2*k)*G(k/2+mp.mpf(3)/4)*G(3*k/2+mp.mpf(1)/4)/(G(k/2+mp.mpf(1)/4)*G(3*k/2+mp.mpf(3)/4))
if __name__ == "__main__":
    for k in range(1, 11):
        print(k, mp.nstr(Qk(k), 20), mp.nstr(Qc(k), 20), "diff", mp.nstr(Qk(k)-Qc(k), 3), flush=True)
    r = [k*abs(Qc(k)) for k in range(1, 2001)]
    print("r_k decreasing for k<=2000:", all(r[i+1] < r[i] for i in range(len(r)-1)), "r_2000 =", mp.nstr(r[-1], 12), "limit", mp.nstr(1/(2*mp.sqrt(3)), 12))
    S = mp.nsum(lambda j: abs(Qc(2*j+1))/(4*(2*j+1)**2-1), [0, mp.inf])
    print("N(pi/4)-N(0) via Fourier =", mp.nstr(4/mp.pi*S, 15))
    print("direct: 0.4023257139688609 - 0.2701129378 =", 0.4023257139688609 - 0.2701129378)
