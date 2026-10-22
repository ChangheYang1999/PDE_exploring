# A conditional exterior dipole formula for the residual impulse

Complete informal proof written before its independent computational controls. It audits lead draft4.36. The expansion is a hypothesis, not a property proved for the full B2 class.

## 1. Statement, notation and scope of the expansion

Fix beta>2, s=1/beta. Let smooth whole-plane fields satisfy

    Omega=-Delta Psi, V=(-Psi_y,Psi_x), V(0)=0,
    W=beta X+V, W.gradTheta=(beta-2)Theta.

Assume Psi is odd in x, Theta even in x, and the vorticity residual f=(W.grad+1)Omega-Theta_x satisfies x f in L^1(R²). Compact support of f is a sufficient special case. Assume Omega=O(r^-s), V=O(r^(1-s)), Theta=O(r^(1-2s)). Suppose on a full exterior region {r>=R0}

    Psi=P+dPsi, Theta=H+dTheta,
    dPsi=o(r^-1), DdPsi=o(r^-2), D²dPsi=o(r^-3),
    dTheta=o(r^-2),                                    (1)

uniformly in angle. After x-odd/even symmetrization we may and do take P odd and H even; the remainder bounds are preserved. P,H are finite sums of powers times polynomials in log r, with smooth angular coefficients. The allowed nonharmonic stream degrees are 2-Ks-n, integers K>=1,n>=0. The temperature degrees are 1-Ls-n, integers L>=2,n>=0. Besides these, P can contain actual harmonic homogeneous terms of degrees1,-1,-2,... . The adjective harmonic applies to each complete appended term, not just to its degree. In particular a degree-1 term times a nonconstant polynomial in log r is not appended as a harmonic term.

Let

    Z={M/d>2: M,d positive coprime integers, 1<=d<=3}.

If beta is outside Z and D is the coefficient of x/r² in P, then

    integral_R² x f = 2 pi (1-3beta)D.                 (2)

The integral is absolutely finite by the weighted L^1 hypothesis. For every beta>2, including beta in Z, it equals the coefficient of R^0(log R)^0 in the full finite boundary expression obtained by substituting P,H into(3). Only the further reduction to the single dipole coefficient requires beta outside Z. If f=0 everywhere, D=0. Also the circular finite part of integral_(B_R) x Omega, defined as the coefficient of R^0(log R)^0 in this finite expansion, is2 pi D. This is a conditional necessary identity, not a construction or a nonexistence result.

## 2. Exact boundary formula

Write p=Psi_x,q=Psi_y and n for the outward unit normal. For every disk, ordinary integration by parts gives

    integral x f
      = (1-3beta) integral x Omega - integral V1 Omega
        + integral Theta
        + boundary_integral [x Omega W.n-x Theta nx].

Indeed div W=2beta and W1=beta x+V1. There are three further identities:

    integral x Omega = boundary_integral(Psi nx-x partial_n Psi),
    V1 Omega = partial_x(pq)+partial_y((q²-p²)/2),
    (3beta-2)integral Theta = boundary_integral Theta W.n.

The last uses exact thermal transport. Substituting gives

    integral_(B_R) x f
      = boundary_integral [ (x Omega+Theta/(3beta-2))W.n
          -x Theta nx-pq nx-(q²-p²)ny/2
          +(1-3beta)(Psi nx-x partial_n Psi) ].          (3)

Every derivative and integral here is classical. As R tends to infinity the left side tends to one fixed real number by x f in L^1. If f is compactly supported it is already constant beyond its support. This derivation also fixes the sign in(2). It is the exact-thermal specialization of145.

## 3. Every substitution error is o(1)

Set Omega_P=-Delta P and V_P=gradperp P. Equation(1) implies dOmega=o(r^-3),dV=o(r^-2). The finite sums inherit the stated leading bounds from the actual fields. On a circle the linear vorticity error is bounded by C r³|dOmega|=o(1); the linear temperature errors by C r²|dTheta|=o(1). The Green bracket contributes at most C[r|dPsi|+r²|DdPsi|]=o(1).

The nonlinear vorticity boundary term has errors bounded by

    r²|V||dOmega|=o(r^-s),
    r²|Omega||dV|=o(r^-s).

The mixed temperature term has errors r|V||dTheta|=o(r^-s) and r|Theta||dV|=o(r^-2s). The quadratic stream stress error is bounded by C r|V||dV|=o(r^-s). Terms containing two errors are smaller. Thus substituting P,H into the entire right side of(3) changes it by o(1). No third derivative of the stream remainder or derivative of the temperature remainder is required for this boundary evaluation. Such derivatives would be a separate requirement for matching the PDE term by term.

## 4. Exact power bookkeeping, including the linear gauge

A stream term of degree e has velocity degree e-1 and vorticity degree e-2; logarithmic differentiation changes only the polynomial in log r. Include the measure ds in counting powers. The linear stream terms have power e+1; the linear temperature terms h+2. Both nonlinear stream terms have power e+e'-1; the temperature-velocity term has power h+e.

For the two main degree families, a zero power therefore requires one of

    Ks+n=3, Ls+n=3,
    (K+K')s+n+n'=3, (K+L)s+n+n'=3.                    (4)

The positive integer multiple of s on the left must equal1,2 or3. This is equivalent to beta having reduced denominator at most3. Conversely if beta=M/d in lowest terms with d<=3, the single main stream exponent K=M,n=3-d has e=-1. Thus Z is exactly the set admitting at least one algebraic collision in the available families. This says nothing about realization of a nonzero coefficient by a solution.

A harmonic degree1 term represents the fixed exterior constant velocity. Pairing it with a main stream requires that main degree be0, or Ks+n=2. Pairing it with temperature requires h=-1, or Ls+n=2. These are already in Z. A negative harmonic degree -j cannot make a zero nonlinear power: pairing with a main stream would require its degree1+j>=2, exceeding the maximum2-s; pairing with temperature would require h=j>=1, exceeding the maximum1-2s. Two appended harmonic degrees cannot sum to1 because the list is1,-1,-2,... . In particular the pair(1,-1) produces power-1 in the quadratic stress and gives no constant contribution.

The only appended harmonic term producing a linear power0 has degree-1. A harmonic homogeneous term of that degree is r^-1(A cos theta+B sin theta); x-oddness forces B=0. Hence it is D x/r². Its vorticity vanishes on the exterior. In the Green bracket its contribution is

    integral_circle [Psi nx-x partial_n Psi] ds
       = 2D integral_0^(2pi) cos²theta dtheta = 2pi D.  (5)

All other zero powers have been excluded when beta is outside Z. Consequently the constant term of the finite boundary expansion is exactly the right side of(2).

## 5. Logarithms and the extraction of the constant

For a polynomial Q(t,theta), t=log r,

    Delta[r^e Q(log r,theta)]
       = r^(e-2)[(e+partial_t)²+partial_theta²]Q.

Logarithms therefore preserve every exponent in section4. At an appended harmonic degree e nonzero, a harmonic finite polynomial Q in log r must have log degree0. To see this, let q_J(theta) be the highest log coefficient with J>=1. The highest equation says (partial_theta²+e²)q_J=0. Projecting the next equation onto this angular kernel gives2e J q_J=0, because the angular operator is self-adjoint on periodic smooth functions. Thus q_J=0, a contradiction. Iteration leaves no logarithms. There is no appended degree0 term; an x-odd degree0 harmonic term would in any event be zero.

After angular integration, the substituted right side of(3) is a finite sum of R^a times polynomials in log R. Group coincident exponents first. Since it has the same finite limit as the left side, its polynomial at the largest positive exponent must vanish, then the next, successively. Terms with negative exponent tend to0 even with logarithms. At exponent0 only the degree0 log coefficient can survive. Section4 identified that contribution as(5) times1-3beta. This proves(2).

The same argument applied just to the Green formula for integral x Omega shows its finite part is2pi D. This term is not the unrenormalized divergent moment. No expansion for the broad admissible class has been supplied, so that class is not excluded by(2).

## 6. Positive vorticity alone does not determine D

Fix the same s and choose f0(r)>0 smooth in r² near0 and smooth everywhere, with f0(r)=r^(-s-1) for r>=1. Define

    I(r)=integral_0^r t³ f0(t)dt,
    h(r)=-integral_0^r u^-3 I(u)du,
    Psi=x h(r).

Since I(r)=O(r^4), h is smooth in r² near0, h(0)=0 and V(0)=0. Direct polar or Cartesian differentiation gives

    Delta[xh(r)]=x(h''+3h'/r)=-x f0(r).

Thus Omega=x f0(r)>0 on x>0. For r>=1,

    I(r)=r^(3-s)/(3-s)+c0,
    c0=I(1)-1/(3-s),
    h(r)=-r^(1-s)/[(3-s)(1-s)]+C+c0/(2r²).

Therefore D=c0/2 as asserted. For a strictly positive smooth f0 that is very small on most of[0,1] and joins the prescribed tail in a sufficiently thin layer near1, I(1) can be arbitrarily small and D<0. Smooth flat cutoffs construct this join without affecting the tail. Adding a nonnegative nonzero interior bump changes I(1) linearly through arbitrarily large values, retains strict positivity and gives D=0 or D>0 by choosing its amplitude. In fact I(1) ranges over all positive values, by first choosing the thin joining layer below a prescribed value and then adding a bump, so D ranges over exactly (-1/(2(3-s)),infinity). Fubini also gives C=[1/(1-s)-integral_0^1 t f0(t)dt]/2; setting V(0)=0 does not force this exterior constant velocity to vanish.

Theta=0 solves the thermal equation for these fields. They do not satisfy the nonzero B2 temperature normalization. They also do not have exact exterior vorticity transport. Indeed in the radial tail put Omega=r^-s cos theta and Psi=r^(2-s)c cos theta+C x+D r^-1 cos theta, with c=-1/[(3-s)(1-s)]. The leading V.gradOmega has angular coefficient -2c cos theta sin theta at degree-2s, which is nonzero. The dilation part annihilates the leading Omega. The complete tail residual is x y [2 r^(-2s-2)/((3-s)(1-s))-(s+1)C r^(-s-3)+(1-s)D r^(-s-5)]. Its nonzero leading term shows x f is not in L^1: on a fixed sector with |cos theta sin theta| bounded below, |x f| is comparable to r^(1-2s), whose area integral diverges. Thus these examples refute a sign inference from positive vorticity alone; they are not counterexamples to the conditional theorem or to a profile claim.

## 7. Dependencies and verification plan

Dependencies: exact differentiation and disk integration by parts; finite asymptotic sums; periodic angular orthogonality; elementary smooth cutoff construction.145 provides an independently checked version of(3), but section2 derives it again. The whole-plane canonical inverse is the once-subtracted inverse in this lane; for the examples its equality with the constructed relative stream follows from sublinear harmonic uniqueness applied to the velocity difference, not to the superlinear stream. Both the once-subtracted velocity and the constructed velocity have growth O(r^(1-s)) and vanish at0. Their difference is a whole-plane harmonic vector field with sublinear growth, hence constant, and that constant vanishes. The stream is then fixed up to an additive constant, removed by oddness.

Global thermal exactness is essential to(2). For Psi=0 and any nonzero nonnegative compact smooth temperature even in x, f=-Theta_x and integral x f=integral Theta>0 whereas D=0. Such a temperature fails exact thermal transport for beta>2: the equation beta X.gradTheta=(beta-2)Theta would require positive-degree homogeneity, incompatible with nonzero compact support.

Independent controls will enumerate exact rational collisions, check harmonic/log coefficients, verify the radial inverse and D formula, and test(2) on compact-vorticity manufactured fields with exact thermal transport and compact residual. Those controls supplement this proof and do not establish the expansion premise for any nonzero profile. The only verdict presently appropriate for that premise in class A is OPEN.

Written UTC 2026-10-21T08:53:21.802099+00:00

Revision UTC 2026-10-21T08:57:58.636526+00:00: includes integrable residual version, exact range and full residual of the positivity example, and the velocity Liouville clarification after actual Opus216 review. Opus216 writes V(0)=(-h(0),0) for Psi=xh; the vector order/sign in that review is incorrect: V(0)=(0,h(0)). Since h(0)=0 the verdict is unchanged. Our computation uses the stated convention throughout.
