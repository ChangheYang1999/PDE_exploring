# Pushforward density of |q|^{-1/2} dphi under phi -> theta(phi) = (1/2) arg q - 2 phi (mod pi), q = 1/4 + sigma e^{i phi}.
# Sufficient condition for max_b Phi_b(sigma) at b = pi/4 (rearrangement): density nondecreasing on [0, pi/2].
import numpy as np
from scipy.optimize import brentq
def argq(sig, ph):
    # continuous arg of q along phi in [0, 2pi]
    q = 0.25 + sig*np.exp(1j*ph)
    a = np.angle(q)
    if sig > 0.25:
        a = np.where(ph > np.pi, a + 2*np.pi, a) if np.ndim(ph) else (a + 2*np.pi if ph > np.pi else a)
    return a
def theta(sig, ph): return 0.5*argq(sig, ph) - 2*ph
def dtheta(sig, ph):
    c = np.cos(ph); q2 = 1/16 + sig*sig + 0.5*sig*c
    return (sig*sig + 0.25*sig*c)/(2*q2) - 2
def dens(sig, th):
    tot = theta(sig, 2*np.pi)  # -4pi or -3pi
    out = 0.0
    m = 0
    while True:
        t = th - m*np.pi  # theta value in (tot, 0]
        if t <= tot: break
        if t <= 0:
            ph = brentq(lambda p: theta(sig, p) - t, 0, 2*np.pi, xtol=1e-14) if t < 0 else 0.0
            q = 0.25 + sig*np.exp(1j*ph)
            w = abs(q)**-0.5/abs(dtheta(sig, ph))
            out += w if 0 < t or t > tot else w  # endpoints counted once overall
        m += 1
    return out
ths = np.linspace(1e-6, np.pi/2 - 1e-6, 41)
bad = []
for sig in [0.01, 0.05, 0.1, 0.15, 0.2, 0.22, 0.24, 0.249, 0.251, 0.26, 0.3, 0.4, 0.5, 0.75, 1, 2, 5, 20, 100]:
    d = np.array([dens(sig, -t) for t in ths])  # density at theta=-t equals density at t by evenness
    inc = np.all(np.diff(d) >= -1e-12)
    print(f"sigma={sig:7.3f} dens[0]={d[0]:.6f} dens[pi/4]={d[20]:.6f} dens[pi/2]={d[-1]:.6f} nondecreasing={inc} min diff={np.diff(d).min():.3e}", flush=True)
