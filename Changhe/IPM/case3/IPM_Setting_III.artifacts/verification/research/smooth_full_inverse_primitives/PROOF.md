# Full-plane inverse primitives for the smooth finite basis

Date: 2026-10-20. The purpose is an independent multiprecision check of the actual stored density, its canonical velocity and its transport residual. Earlier high-precision checks used a double-precision inverse. The formulas here remove that precision limitation for this finite basis. Floating evaluation of these formulas is not an interval certificate.

## Statement and dependencies

Fix L>0,0<alpha<1/2 and finitely many real polynomials P_0,...,P_(M-1). Write

    z=r^2/L^2, w=(1+z)^(-alpha), sigma=z/(1+z),
    rho=y*w*sum_(k=0)^(M-1) sigma^k P_k(1-2w) cos(2k theta).

The Cartesian extension at zero is the one in result83, ../smooth_canonical_high_jets/PROOF.md. Thus rho is smooth, has even-x/odd-y parity, and grows at most r^p with p=1-2alpha in(0,1), with the corresponding gradient bound. Expand P_k(1-2w)=sum_l C_(k,l)w^l, set C_(k,l)=0 for missing indices, and put a_l=alpha(l+1). The a_l are exponents, not the origin slope a0=P_0(-1).

The formulas below determine the canonical stream function and velocity at every r>0 by finite sums, powers, and a scalar hypergeometric function at small z. An alternative finite elementary expression for that function is also given. No finite-radius boundary condition, optimized strain or missing tail is introduced. At zero the fields extend smoothly, with c given by the exact global moments of result83. The analytic dependency is the angular Green inverse in ../inverse/PROOF.md, whose hypotheses and endpoints are checked again below.

## The source retains its vanishing factor

Define T_(k,a)(z)=z^k(1+z)^(-a-k). If g_k(r)=sum_l C_(k,l)T_(k,a_l)(z), the sine coefficients f_m of rho satisfy

    f_1/r=g_0-g_1/2,
    f_(2j+1)/r=(g_j-g_(j+1))/2, j>=1.

These are just sin(theta)cos(2k theta) product identities. Since r d_r T_(k,a)=2kT_(k,a)-2(a+k)T_(k+1,a), the sin(2j theta) coefficient S_(2j) of rho_x is

    S_(2j)=sum_l [A_(j,l) T_(j,a_l)
                     +B_(j,l) T_(j+1,a_l)+E_(j,l) T_(j+2,a_l)],    (1)
    A_(j,l)=j C_(j,l)-eta_j(a_l+j-1)C_(j-1,l),
    B_(j,l)=-(j+1)C_(j+1,l),
    E_(j,l)=(a_l+j+1)C_(j+1,l)/2,
    eta_1=1, eta_j=1/2 for j>=2.

Here j=1,...,M; there are no higher source modes. To derive (1), use

    S_(2j)=1/2[f'_(2j-1)-(2j-1)f_(2j-1)/r
                         +f'_(2j+1)+(2j+1)f_(2j+1)/r].

The two derivatives of g_j have opposite coefficients and cancel. The g_(j-1) contribution has zero undifferentiated coefficient after combining its 2(j-1) derivative term with 2-2j; its remaining term is the first negative term in A. The two g_(j+1) terms give B and E. In particular every summand in (1) contains at least z^j. Thus S_(2j)=O(r^(2j)) at zero. This cancellation is performed algebraically before numerical evaluation. At infinity each summand is O(r^(-2a_l)), so S_(2j)=O(r^(p-1)).

## Two radial integrals for one source term

For n=2j and one source T_(k,a), where k is one of j,j+1,j+2 and a>0, define

    P_(j,k,a)(z)=r^(-2j-2) int_0^r s^(2j+1)T_(k,a)(s^2/L^2) ds,
    Q_(j,k,a)(z)=r^(2j-2) int_r^infinity s^(1-2j)T_(k,a)(s^2/L^2) ds.

The changes of variable t=s^2/L^2 give

    P=(1/2)z^(-j-1) int_0^z t^(j+k)(1+t)^(-a-k) dt,             (2)
    Q=(1/2)z^(j-1) int_z^infinity t^(k-j)(1+t)^(-a-k) dt.       (3)

The first endpoint is integrable because j+k>=2; the second because the integrand is O(t^(-a-j)) and a+j>1. Thus the n=2 tail is included and convergent even when a is small.

Let N=j+k and b=a+k. Expanding (1+t)^(-b) in its convergent series for |t|<1 and integrating termwise gives

    P=z^k/[2(N+1)] * hypergeom(b,N+1;N+2;-z).                  (4)

For the intended small-z evaluation, 0<z<=1/2, this series is absolutely convergent. Equality for all positive z can either be defined through the positive integral in (2) or continued analytically, but no such continuation is needed by the implementation.

For a finite elementary expression, expand t^N=((1+t)-1)^N. For any real e define

    J_e(z)=((1+z)^e-1)/e if e!=0,
    J_0(z)=log(1+z).

Then

    P=(1/2)z^(-j-1) sum_(h=0)^N (-1)^(N-h) binom(N,h) J_(h+1-b)(z).  (5)

The e=0 definition follows either by direct integration or the limit of expm1(e log(1+z))/e. Consequently (5) has no exceptional exponent. It is mathematically valid at every z>0; at small z it loses relative precision through subtraction, which is why (4) is used there. Extra working digits and comparisons at two precisions are required even when (5) is used at moderate z.

Finally let d=k-j in{0,1,2}. Expanding t^d=((1+t)-1)^d in the exterior integral gives the short formula

    Q=(1/2)z^(j-1) sum_(h=0)^d (-1)^(d-h) binom(d,h)
                                  (1+z)^(1-a-k+h)/(a+k-h-1).    (6)

Every denominator is positive because a+k-h-1>=a+j-1>0. There is no omitted tail estimate in (6): it is the integral to infinity exactly.

## Stream function, velocity and the gauge

Form P_j(z) and Q_j(z) by the same linear combination of (2)-(3) as the coefficients A,B,E in (1). The canonical Green formula gives

    psi(r,theta)/r^2=sum_(j=1)^M [P_j(z)+Q_j(z)]sin(2j theta)/(4j). (7)

Indeed, the inner and exterior pieces of the Green formula are r^2P_j and r^2Q_j. Differentiating those integrals with respect to r, their boundary source terms cancel. Hence the polar velocity is

    U_r/r=-(1/2)sum_j [P_j+Q_j]cos(2j theta),
    U_theta/r=(1/2)sum_j [-P_j+Q_j]sin(2j theta).               (8)

In particular the signs in (8) implement U=(-psi_y,psi_x). Convert to Cartesian components by U1=U_r cos(theta)-U_theta sin(theta), U2=U_r sin(theta)+U_theta cos(theta).

At zero, S_(2j)=O(r^(2j)), so the inner stream term is O(r^(2j+2)) and the outer term has a finite r^(2j) coefficient. The resulting stream extends smoothly by local elliptic regularity, or by the convergent analytic Taylor recursion of result83. At infinity, S_(2j)=O(r^(p-1)) with p<1 implies psi=O(r^(p+1)) and U=O(r^p)=o(r); the same bounds follow directly by splitting the two integrals at a fixed positive radius. This excludes any growing harmonic term r^(2j)sin(2j theta), in particular the strain term xy. A singular harmonic term is excluded at zero. The finite sum is therefore the canonical full-plane inverse, not a finite-box solution. Odd-odd stream parity fixes its otherwise irrelevant additive constant to zero.

For a check on the n=2 sign and normalization, take only P_0=a0 constant. Then S_2=-a0*alpha*T_(1,alpha). The exact stream is

    psi=-a0*x*y*G(z),
    G(z)=(1/2)int_0^1 t(1+zt)^(-alpha)dt
        =(1/4)hypergeom(alpha,2;3;-z).

Direct differentiation gives -Delta psi=rho_x and c=psi_xy(0)=-a0/4. This independent radial formula supplies manufactured tests of (7)-(8), including the exterior tail.

## Residual evaluation and its limits

Given ell>1, reconstruct rho at a point from the original Cartesian formula using a separate Chebyshev recurrence. Differentiate that scalar formula in multiprecision and combine it with (8) to evaluate R=(ell X+U).grad rho-rho, N_f and N_v. No relation ell+c=1 is enforced by this evaluator. The registered exact JSON inputs include the stored binary values of alpha,L,ell and every coefficient. In particular the effective far exponent is exactly p=1-2alpha for that formula. The residual coefficient ell*p-1 is retained even if a separately rounded floating exponent is numerically printed as 1/ell.

At an exact symmetry zero with N_f=N_v=0 the ratios are undefined. Nonzero tiny denominators are evaluated without flooring. Working-precision comparisons assess numerical stability only at the selected points. They do not provide an interval enclosure, a uniform residual bound, parameter convergence or a nearby-solution theorem. The complete code, point lists, input hashes, timings and raw comparisons must remain with the evidence.

### Differentiation scale in the evaluator

For r=hypot(x,y)>0, Cartesian density derivatives are evaluated as d/du[rho(ru,y)/r] at u=x/r and d/dv[rho(x,rv)/r] at v=y/r. These are exactly rho_x and rho_y by the chain rule. Dimensionless derivative variables avoid losing an absolute perturbation at very large physical coordinates. The first manufactured gate exposed this precision problem in its closed radial reference at r=1e80; the raw failure is preserved, and the repaired test includes r=1e250. This repair changes numerical differentiation conditioning, not the canonical inverse or its analytic formula.

## Residual cancellation allowance (2026-10-20T23:41Z)

At infinity the separately evaluated transport terms are O(r^p). If ell p=1, their leading terms cancel and the residual is generically O(r^(2p-1)). Computing a fixed number of significant residual digits can therefore lose (1-p) log10(r/L)=2 alpha log10(r/L) decimal places. Near a compatible center the affine terms cancel and cubic transport can cost 2 log10(L/r) decimal places. The field evaluator now adds the ceiling of the positive part of these losses to its base working precision, and records that precision per point. This allowance is tested at two precisions, including r=10^250. It is a numerical conditioning strategy, not a theorem that arbitrary further cancellations have been resolved or an interval error bound. The exact first far coefficient must still be used when the stored parameters have ell p different from 1.
