"""stream_modes.py -- endpoint data of the discrete stream modes psi = r^2 w sum_n Psi_n(t) sin(n th), n = 2, 4, ...: Psi_n(-1) and Psi_n'(-1) (Lobatto
differentiation matrix).  Cartesian smoothness of psi at the origin requires Psi_n(-1) = 0 for n >= 4 and Psi_n'(-1) = 0 for n >= 6 (sigma ~ r^2; mode n
must vanish like r^(n-2)); nonzero values measure the non-smoothness of the interpolated numerical inverse (referee shift3ref item 2).
usage: python3 src/stream_modes.py states..."""
import sys; import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
for f in [a for a in sys.argv[1:] if '=' not in a]:
    S = qdiag.State(f); PsiC = S.flds['PsiC']; dPsi = S.mdl.rad.DL @ PsiC; d2 = S.mdl.rad.DL @ dPsi
    print(f"{f.split('/')[-1]:>28s} N={S.N:3d} a0={S.a0:9.4f}: Psi_n'(-1), n=2..12: " + " ".join(f"{dPsi[0,j].item():+.2e}" for j in range(6)) + "  | Psi_n''(-1), n=6,8: " + " ".join(f"{d2[0,j].item():+.2e}" for j in [2,3]))
