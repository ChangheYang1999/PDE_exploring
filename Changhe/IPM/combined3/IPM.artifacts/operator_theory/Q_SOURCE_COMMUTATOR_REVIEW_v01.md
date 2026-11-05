# Independent source-commutator analytic review

Reviewed `../finite_rank/Q_SOURCE_FRACTIONAL_COMMUTATOR.md`. Result: PASS
for the stated analytic inequalities and their actual-source limiting scope.
Numerical whole-plane coefficient bounds remain the source producer's
separate obligation.

For q=2+delta the Hessian of Jq is qJdelta I+qdelta xi tensor xi J^(delta-2),
so its operator norm is at most q(q-1)Jdelta. The ordinary second Taylor
remainder and its fixed-input output derivative therefore have constants
cq=q(q-1)/2 and2cq exactly as stated. The inequality
J(eta+t zeta)^delta<=J(eta)^delta+|zeta|delta holds for0<delta<1.

The first Taylor term has the displayed minus sign from the two physical
derivatives. Its joint input multiplier grad J^(q-2)U has norm at most
J^(q-1), so q sup(W|Db|F) is a valid principal bound. Multiplication by x
on the Fourier remainder differentiates the coefficient or remainder
symbol at fixed input eta; it does not differentiate U(eta). Thus the
coordinate term has the2cq coefficient and the full W2 inequality gives
exactly A_s=M_s(b)+2M_s(xb)+4M_(s-1)(b).

The homogeneous Wiener inequality has the correct Fourier normalization.
Its Cauchy-Schwarz radial integral is
a^(2+2sigma)/[8cos(pi sigma/2)], and minimization gives precisely the
constant Csigma printed in that note. At sigma0 this is1/2, so
M_m(f)<=sqrt(||Dmf||2 ||D^(m+2)f||2)/2.

The actual symbol classes b in S^-gamma and xb in S^(1-gamma) put every
listed derivative in L2. The physical-cutoff error powers in that note
are strictly decaying at all used orders. Weighted first-derivative cutoff
errors also tend uniformly to zero. These facts justify its extension
from compact coefficients to the actual finite-potential center without
assuming b or xb is itself L2.

The outside-ball interpolation powers are1/q,1-delta/q,1 respectively.
They require Q(g)>=M explicitly and assert no global dissipativity. The
analytic result is therefore compatible with the direct forced-evolution
barrier in `Q_FORCED_EVOLUTION_BRIDGE_v02.md`.
