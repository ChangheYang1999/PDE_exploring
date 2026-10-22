"""Hydrostatic variant of model.fields: Omega = -D_y^2 Psi (the horizontal part -D_x^2 Psi is dropped).
In this problem a0 is a gauge: x -> lam x, Psi -> lam Psi, Theta -> lam^2 Theta maps solutions to solutions with a0 -> lam^2 a0.
Everything else (generating-function representation, transport, normalizers) is as in model.fields."""
import torch
from jets import Jet

def fields_h(Gc, x0, e0, a0, beta, b=None, p=4, hydro=True):
    a = beta + 2; b = beta - 2
    G = Jet(Gc, p)
    X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p)
    Gx = G.dx(); Ge = G.de()
    A = Gx.de(); B0 = Gx.dx(); C = Ge.de()
    M = a * Ge - b * (H * C)
    Psi = beta * (X * Gx) + b * (H * Ge) - 2 * beta * G
    iA = A.pow(-1.0); BA = B0 * iA
    Dx = lambda f: f.dx() - BA * f.de()
    Dy = lambda f: iA * f.de()
    Om = -Dy(Dy(Psi)) if hydro else -(Dx(Dx(Psi)) + Dy(Dy(Psi)))
    Omx = Om.dx().val(); Ome = Om.de().val()
    Av = A.val(); Bv = B0.val(); Mv = M.val()
    W1 = Mv / Av; W2 = Bv * Mv / Av + b * e0 * Av
    Omv = Om.val()
    R = W1 * Omx + b * e0 * Ome + Omv + a0 * Bv / Av
    Ox = Omx - Bv / Av * Ome; Oy = Ome / Av
    Thx = -a0 * Bv / Av
    N = (W1 * Ox).abs() + (W2 * Oy).abs() + Omv.abs() + Thx.abs()
    y = Gx.val()
    return dict(R=R, N=N, A=Av, Om=Omv, Ox=Ox, Oy=Oy, W1=W1, W2=W2, Thx=Thx, y=y, Psi=Psi.val(),
                U1=W1 - beta * x0, U2=W2 - beta * y, Thy=a0 / Av)
