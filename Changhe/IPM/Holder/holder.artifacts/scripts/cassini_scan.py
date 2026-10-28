# Per-Cassini-oval test: Phi_b(sigma) = int_0^{2pi} |q|^{-1/2} |cos((1/2)arg q - 2phi + 2b)| dphi, q = 1/4 + sigma e^{i phi}.
# Question: is argmax_b Phi_b(sigma) = pi/4 for every sigma?
import numpy as np
def Phi(sig, b, n=200000):
    ph = (np.arange(n)+0.5)*2*np.pi/n
    q = 0.25 + sig*np.exp(1j*ph)
    # continuous branch of arg q along the circle: for sigma<1/4 principal arg is continuous; for sigma>1/4 arg q winds once
    aq = np.unwrap(np.angle(q))
    return np.sum(np.abs(q)**-0.5*np.abs(np.cos(0.5*aq - 2*ph + 2*b)))*2*np.pi/n
bs = np.linspace(0, np.pi/4, 9)
for sig in [0.01, 0.05, 0.1, 0.2, 0.24, 0.25, 0.26, 0.3, 0.5, 1, 2, 5, 20, 100]:
    v = [Phi(sig, b) for b in bs]
    print(f"sigma={sig:7.3f} " + " ".join(f"{x:.6f}" for x in v), " argmax", bs[int(np.argmax(v))]/np.pi*4, flush=True)
