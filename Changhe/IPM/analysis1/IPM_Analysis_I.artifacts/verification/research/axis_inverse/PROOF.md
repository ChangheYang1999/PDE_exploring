# Density-mode inversion and evaluation on the positive axis

Status: auxiliary exact identities, independently derived 2026-10-20. Numerical uses are marked separately. This is not an existence or exclusion theorem.

## Statement

Let rho be even in x, odd in y, with the regularity and sublinear growth in the canonical-inverse proof. Define odd sine coefficients a_l(r)=(1/pi) integral_0^{2pi}rho(r,theta) sin(l theta)dtheta. For an even integer m>=2, put a=a_{m-1}, b=a_{m+1}. Then the canonical coefficient of sin(m theta) in the stream function is

psi_m(r) = (1/2)[r^m integral_r^infinity t^{-m} b(t)dt - r^{-m} integral_0^r t^m a(t)dt].

This formula uses density coefficients directly and contains no numerical density derivative. Define

I_m(r)=r^{-m-1} integral_0^r t^m a_{m-1}(t)dt,
J_m(r)=r^{m-1} integral_r^infinity t^{-m} a_{m+1}(t)dt.

The polar velocity contributions are

U_r,m = -(m/2)(J_m-I_m) cos(m theta),
U_theta,m = [(m/2)(J_m+I_m)-(a_{m-1}+a_{m+1})/2] sin(m theta).

In particular U_1(r,0)=sum_{m even>=2}(m/2)(I_m-J_m), when the angular series converges at the axis. Finite partial sums always have the stated meaning; truncation requires a separate bound.

## Proof

In polar coordinates partial_x=cos(theta) partial_r -sin(theta) partial_theta/r. Multiplying and differentiating a_l sin(l theta) shows that the coefficient f_m of sin(m theta) in rho_x is

f_m=(1/2)[a'-(m-1)a/r+b'+(m+1)b/r].

For example, the contribution from l=m-1 uses sin(l theta)cos(theta) and cos(l theta)sin(theta) with the same positive sin(m theta) sign; the l=m+1 contribution has opposite sign in the second trigonometric product. Substitute this expression into the Green formula proved in ../canonical_inverse/PROOF.md. Integration by parts gives

integral_0^r t^{m+1}f_m(t)dt = r^{m+1}(a(r)+b(r))/2 -m integral_0^r t^m a(t)dt,

integral_r^infinity t^{1-m}f_m(t)dt = -r^{1-m}(a(r)+b(r))/2 +m integral_r^infinity t^{-m} b(t)dt.

The boundary terms at zero and infinity vanish by the center and sublinear hypotheses. The local a+b terms cancel after substitution into the Green formula, proving psi_m. Differentiating it gives

psi_m'=(m/2)(J_m+I_m)-(a+b)/2.

The convention U=(-psi_y,psi_x) gives U_r=-partial_theta psi/r and U_theta=partial_r psi, proving the velocity formulas. A separate SymPy differentiation of the density-mode expression verifies the forced radial ODE in ../canonical_inverse/evidence/independent_audit.json.

## Stable compact quadrature variables for X3

For q=1-(1+(r/L)^2)^(-(1-k)/2), set s=1-(1-q)^{2/(1-k)}. Then dr/dq=r/[(1-k)s(1-q)]. With q_*=q(r_*),

I_m(r_*)=integral_0^{q_*} (r(q)/r_*)^{m+1} a_{m-1}(r(q))/[(1-k)s(1-q)] dq,

J_m(r_*)=integral_{q_*}^1 (r_*/r(q))^{m-1} a_{m+1}(r(q))/[(1-k)s(1-q)] dq.

All displayed radius ratios are at most one. At infinity, the m=2 integrand remains bounded for the r^k leading density tail because the exponent in (1-q) cancels. Higher modes have additional vanishing powers. This removes catastrophic powers of large radii. It does not supply a quadrature remainder or an angular truncation bound.

## Scope

The exact identities are analytic. The accompanying density-mode numerical implementation uses floating quadrature and a discrete sine transform, independent of derivative-mode inverse implementations in the other lanes. Its output is evidence for reconstruction and signs only. An axis root certified for the explicit trial would still not prove a corresponding source for an exact nearby profile without a quantitative perturbation theorem.
