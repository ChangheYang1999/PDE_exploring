# Sectorial mass and the absolute center-velocity integral

Status: verifier consequence of the derivative-free angular temperature limit, independently confirmed by actual claude-opus-5-5. A complete informal proof is given here. It removes the velocity derivative assumption from the absolute-component exclusion in the power-sublinear class. It is not a full B2 nonexistence theorem.

## Statement

Let beta>=2 and let smooth B2 fields satisfy the equations, parity, axis condition and nonzero local temperature jet of PROMPT.md. Put V=U-U(0), W=beta X+V. Assume

    |V(X)|<=C(1+|X|)^(1-delta), delta>0.

In particular, the equations used below are div W=2 beta and div(W Omega)-(2 beta-1)Omega=partial_x Theta.

Let q=2/beta and kappa=2-q. There are constants 0<a<b<infinity, epsilon>0, c>0, R0 and a compact set K contained in

    {a<=|X|<=b, X_1>=epsilon |X|}

such that for every R>=R0,

    integral_(R K) |Omega(X)| dX >= c R^kappa.

Consequently the actual vertical center-kernel absolute integral diverges:

    integral_{|X|>1} |X_1 Omega(X)|/|X|^2 dX = infinity.

This does not say that a signed principal value or a prescribed finite part fails to exist. It does not identify radial weighted integrability with component integrability for arbitrary densities.

## Proof

By the exact sign symmetry, assume a0>0. The theorem of research/14 supplies a uniform nonzero temperature limit

    theta_R(X)=R^(-(1-q))Theta(RX) -> Theta_infinity(X)=|X|^(1-q)A(arg X)

on every compact annulus. The continuous function A is zero at both vertical angles and positive somewhere in the right semicircle.

The distribution partial_x Theta_infinity is not identically zero on the open right half-plane. Otherwise on that connected half-plane Theta_infinity would be independent of x. One elementary justification is to convolve on rectangles compactly inside x>0: the x derivative of each smoothed function vanishes, so it is constant along horizontal intervals; pass to the continuous limit. Thus Theta_infinity(x,y)=f(y). For every y!=0, continuity at the vertical axis and its zero value give f(y)=0 by letting x decrease to zero. Continuity within x>0 then gives f(0)=0. This contradicts positivity of A.

There is therefore a smooth compactly supported test phi in the right half-plane, with support K bounded away from the origin and the vertical axis, for which

    I=integral Theta_infinity partial_x phi != 0.

Every such compact K is contained in a sector-annulus of the displayed form for suitable a,b,epsilon. Define omega_R=R^q Omega(RX), w_R=W(RX)/R. No pointwise upper bound on omega_R is assumed. The exact conservative vorticity equation, integrated against phi, is

    integral omega_R [w_R.grad phi+(2 beta-1)phi]
      =integral theta_R partial_x phi.

The limiting homogeneous function is used only away from the origin; when beta=2 it need not extend continuously there. The right side tends to I by uniform temperature convergence. Since U=o(r), w_R is uniformly bounded on K for all large R, and the bracket on the left has a uniform finite sup norm C_phi. It follows that

    integral_K |omega_R| >= |I|/(2 C_phi)>0

for all sufficiently large R. Increase R0 to include the uniform bracket bound, the nonzero tested limit, and R0>=1/a. Constants depend on the profile and the chosen test, not universally on beta alone. Here one can replace C_phi by any larger positive bound; a zero exact bracket would contradict the nonzero right side. The change of variables Y=RX proves the mass lower bound.

On R K, the kernel weight satisfies |Y_1|/|Y|^2 >=epsilon/(bR). Hence

    integral_(R K) |Y_1 Omega(Y)|/|Y|^2 dY
      >= c' R^(kappa-1)=c' R^(1-2/beta).

For beta>2 these lower bounds are already unbounded as R grows, so the total integral cannot be finite. For beta=2 choose a geometric sequence R_j tending to infinity with R_{j+1}/R_j>b/a. The sets R_j K lie in disjoint annuli, and each contributes at least the same positive c'. Their sum diverges. This also supplies a second proof for beta>2.

## Stronger explicit consequences and scope

On the same sector one may replace the center weight by |Y_1||Y|^(-gamma-1). Use the lower constant epsilon b^(-gamma) for gamma>=0 and epsilon a^(-gamma) for gamma<0. Its mass on R K is at least a constant times R^(kappa-gamma). Thus all such component-weight integrals with gamma<=kappa diverge, by the same geometric-annulus argument at equality. This is a consequence for solutions, not an equivalence of function spaces.

No DV decay, vorticity sign, finite enstrophy, bounded vorticity or assumed angular vorticity expansion was used. The additional power bound on V is used to obtain the continuous nonzero angular temperature limit. The ordinary absolute center integral is therefore impossible in the lead's uniform power-decaying vorticity subclass, where the canonical inverse supplies this power velocity bound. A renormalized observer convention remains possible. The broad class with only U=o(r), lacking the power improvement, remains open.

Dependencies: the fully stated angular-limit theorem in research/14, the conservative form of the exact PDE, distributional derivatives of a continuous function, compactly supported testing, and change of variables. No numerical evidence is used as proof.

Audit 2026-10-20T14:26:06.569409+00:00: actual claude-opus-5-5 confirmed the compact-test scaling, absence of any vorticity upper-bound requirement, the critical geometric-annulus argument, and the weighted extension in opus_reviews/06_sector_only/answer.md. This review assumes the angular-limit theorem, whose separate proof is in research/14.
