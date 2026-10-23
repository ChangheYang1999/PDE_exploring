# Independent full-plane quadrature at a primary residual maximum

Written 2026-10-22T11:55:32.265701+00:00, before implementation and candidate evaluation. Status OPEN. This is a finite diagnostic on the original N44 field at the prospectively fixed index20 of result336. It does not certify a true inverse error or uniform residual.

## Statement and inputs

Read the unchanged exact rational density coefficients, ell,alpha and L from336 INPUTS. At x=0.30214261911456275,y=0.49852850531223214 use the exact stored binary64 coordinates. Compare a new inverse quadrature and analytic polar density derivatives to the110-digit saved336 values. Use Gauss-Legendre orders96,192,384 with binary64 nodes and weights,75-digit arithmetic for the density recurrence and modal sum. These are empirical quadrature refinements, not interval enclosures. The primary class remains unresolved regardless of the result.

## Derivation

For s>0 set q=s²/(L²+s²), w=(1+s²/L²)^(-alpha), t=1-2w and g_k=q^k w P_k(t), where P_k is the imported Chebyshev polynomial. Evaluate its values and derivatives by the forward Chebyshev recurrences T0=1,T1=t,T_(j+1)=2tT_j-T_(j-1) and T'_(j+1)=2T_j+2tT'_j-T'_(j-1). No converted monomial coefficients or existing inverse routines are used. Differentiating q,w,t gives

    B_k=s g'_k=q^k w[(2k(1-q)-2alpha q)P_k+4alpha q w P'_k].

Set g_k=B_k=0 outside the finite coefficient range. The odd sine density modes h_(2k+1)=s A_(2k+1) have A1=g0-g1/2, A_(2k+1)=(g_k-g_(k+1))/2 for k>=1. Define B^A by the same linear combinations of B. These follow from sin(theta)cos(2k theta)=[sin((2k+1)theta)-sin((2k-1)theta)]/2 for k>=1. Differentiation in Cartesian x gives the even source mode

    f_n(s)=((2-n) A_(n-1)+B^A_(n-1)+(n+2) A_(n+1)+B^A_(n+1))/2.

This follows by applying cos(theta) partial_s-sin(theta)/s partial_theta to every h_m sin(m theta); the two contributing modes are m=n-1 and m=n+1. All sums are finite, n=2,...,2M. The density derivatives at the tested point are independently computed from rho_r=sum(A+B^A)sin(m theta) and rho_theta/r=sum m A cos(m theta), followed by the Cartesian rotation. This does not use mp.diff or the336 gradient.

The canonical Green formula of research/inverse/PROOF.md reduces to

    P_n=integral_0^1 u^(n+1) f_n(r u) du,
    Q_n=integral_0^1 u^(n-3) f_n(r/u) du.

For the exterior integral substitute u=v^5, giving Q_n=integral_0^1 5v^(5(n-2)-1) f_n(r/v^5) dv. For the leading source decay s^(p-1), p=1-2alpha, its first-mode endpoint behaves like v^(10alpha-1), integrable since alpha>0; at infinity the remaining modes are no worse. The substitution maps the entire exterior to(0,1) with no artificial boundary or omitted explicit tail. Finite Gaussian quadrature still has unknown error. Recover

    psi=r² sum (P_n+Q_n)sin(n theta)/(2n),
    U_r=-r sum(P_n+Q_n)cos(n theta)/2,
    U_theta=r sum(Q_n-P_n)sin(n theta)/2,

then rotate U to Cartesian components. These are the same unique canonical inverse in a different discretization and source/differentiation implementation. Neither the old primitive integrals nor their converted source polynomials are imported.

## Checks and scope

Before evaluation check Chebyshev derivatives, independent manufactured source against Cartesian differentiation, manufactured density derivatives, and one-mode quadrature against the explicit stream -a x y hyp2f1(alpha,2,3,-r²/L²)/4. Compare actual source modes at several radii and angles to a separate Cartesian derivative only if it is computed; do not claim this test merely from a manufacture. Keep the exact imported ell explicit. The reported candidate outputs include all orders, signed R, both denominators, component differences and the finite order sensitivity. No finite observed difference bounds the exact quadrature error.

All writes stay in this lane. No JavaScript/TypeScript/Node, servers/listeners/tunnels, RLScience cluster, GPU, Lean/Lake, commits/push/posts or human contact. One heavy serial nice19 process,14GiB cap, all commands below10minutes. Actual Opus5.5 design review precedes candidate evaluation; actual results review follows. Preserve failures.
