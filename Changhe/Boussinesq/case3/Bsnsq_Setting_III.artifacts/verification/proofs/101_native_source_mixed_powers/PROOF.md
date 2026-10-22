# Distinct tail powers for a fixed exponent-three source

Status: CONFIRMED by own complete argument, exact source tests and independent Cartesian differentiation. Written actual Opus 5.5 follow-up audit completed; its advice was checked independently.
Written UTC: 2026-10-21T01:17:50.803407+00:00.
This is a restricted representation theorem for forced continuation equations, not a B2 nonexistence result.

## Statement and exact hypotheses

Let 3<beta<4, s=1/beta, sigma=1/3, m=1-2s, k=2-s and kS=2-sigma=5/3. Let ell be a real source multiplier. All fields are smooth on the physical plane and have the prompt's x-reflection parity. The inverse B is the full-plane relative Biot--Savart operator with kernel K(Z)=(Z_2,-Z_1)/(2pi|Z|^2), so B[q](0)=0. No extra harmonic or uniform field is allowed. The auxiliary forced transport is

    W=beta X+B[Omega]+ell B[f].

The forced equations and residual signs are explicitly

    R_Omega=W.grad Omega+Omega-Theta_x=0,
    R_Theta=W.grad Theta-(beta-2)Theta=0.

Assume, in physical polar coordinates and with angularly uniform differentiated remainders,

    Omega=r^(-s)a(theta)+r^(-2s)b(theta)+O_C1(r^(-3s)),
    Theta=r^m h(theta)+r^(m-s)d(theta)+O_C1(r^(m-2s)),
    f=r^(-sigma)aS(theta)+O_C1(r^(-2sigma)).                    (1)

O_C1(r^q) means that the function and its first Cartesian derivatives are bounded by constants times r^q and r^(q-1), respectively. The angular coefficients are smooth and have the stated parities. Let p and pS be the unique periodic solutions

    p''+k^2 p=-a,     pS''+kS^2 pS=-aS.                       (2)

The frequencies k and kS are nonintegers, so these solutions are unique. Define

    E_T=-d+k p h'-m p'h,
    D_T=kS pS h'-m pS'h,
    E_O=-b+k p a'+s p'a-m cos(theta)h+sin(theta)h',
    D_O=kS pS a'+s pS'a.                                     (3)

The residuals of the forced equations satisfy

    R_Theta=r^(m-s) E_T+ell r^(m-sigma)D_T+O(r^(m-2s)),
    R_Omega=r^(-2s) E_O+ell r^(-s-sigma)D_O+O(r^(-3s)).        (4)

Consequently, for ell != 0 an exact solution with (1) must have all four coefficients E_T,D_T,E_O,D_O equal to zero. If either E_T or ell D_T is not identically zero, the supremum of the absolute temperature residual on the plane is infinite. This follows because both m-s=1-3/beta and m-sigma=2/3-2/beta are strictly positive, distinct, and m-2s=1-4/beta<0.

A useful exact sufficient test for D_T != 0 is the following. Suppose pS has a simple zero at one symmetry-axis angle theta0=pi/2 or -pi/2, and h is nonzero and real analytic near that angle, with a zero there of finite order n>=2. Then D_T != 0. In particular the test applies to a nonzero h=cos(theta)^2 times a trigonometric polynomial. No sign assumption on h or a is needed.

## Full-plane inverse and residual proof

For a homogeneous angular source r^(-s)a, the stream r^k p solves -Delta Psi=r^(-s)a by (2). Its velocity in the polar orthonormal frame is

    r^(1-s)(-p',k p).

This velocity extends continuously by zero at the origin. It equals the full-plane relative inverse: the relative integral converges at infinity since s>0, and at its origin since s<1. A difference would be a distributionally harmonic full-plane divergence-free velocity of sublinear growth, hence constant; its value at the origin fixes that constant to zero. For the homogeneous candidate there is no distribution supported at the origin: the boundary fluxes vanish as positive powers of the small circle radius. The harmonic constancy claim follows directly from the interior harmonic gradient estimate C R^(-1) sup_(B_R) |V| at any fixed point and sublinear growth as R tends to infinity. The same statements apply to sigma.

For clarity, the needed remainder bound does not assume a convergent ordinary center velocity. If a source remainder g has order r^(-q) at infinity, with 0<q<1, its relative inverse has order r^(1-q). Split the integral into |Y|<r/2, r/2<|Y|<2r, and |Y|>2r. The first piece is bounded by

    C/r integral_0^(r/2) rho |g| drho
      +C integral_0^(r/2) |g| drho=O(r^(1-q));

the comparable-radius piece uses the integrability of |X-Y|^(-1) in two dimensions and has the same order. In the last piece, the difference kernel is bounded by C r/|Y|^2, giving C r integral_(2r)^infty rho^(-q-1) drho=O(r^(1-q)). The local singularities introduced by subtracting the homogeneous leading source are integrable because s,sigma<1 and contribute at most a constant. Thus (1) yields

    B[Omega]=r^(1-s)(-p',k p)+O(r^(1-2s)),
    B[f]=r^(1-sigma)(-pS',kS pS)+O(r^(1-2sigma)).              (5)

The polar gradient of r^m h is r^(m-1)(m h,h'). Its product with (5) gives the two displayed nonlinear temperature coefficients. The radial dilation operator beta r partial_r-(beta-2) annihilates r^m h and sends r^(m-s)d to -r^(m-s)d. All omitted self terms have order at most r^(m-2s). The source times the next temperature term has order r^(m-s-sigma), and its remainder times the first term has order r^(m-2sigma). Both are smaller because sigma>s. This proves the temperature expansion.

Likewise, beta r partial_r+1 annihilates r^(-s)a and sends r^(-2s)b to -r^(-2s)b. The leading self interaction is r^(-2s)(k p a'+s p'a). The leading source interaction is r^(-s-sigma)(kS pS a'+s pS'a). Finally,

    partial_x(r^m h)=r^(-2s)(m cos(theta)h-sin(theta)h').

Every other term has order at most r^(-3s), using s<sigma<2s for the chosen beta interval. This proves the second expansion. Successive division by the two distinct powers in each line proves the exact compatibility statements. For the absolute-residual conclusion choose an angle where the first nonzero coefficient in the temperature line is nonzero and then send r to infinity.

At a simple zero of pS, put delta=theta-theta0 and write pS=B delta+O(delta^2), h=A delta^n+O(delta^(n+1)), with A B != 0. Then

    D_T=(kS n-m) A B delta^n+O(delta^(n+1)).                 (6)

Here kS n>=10/3>m, so the coefficient is nonzero. For nonzero trigonometric-polynomial h, real analyticity ensures a finite vanishing order. This proves the sufficient test.

## Required mixed powers and the endpoint scope

If lower-order corrections are admitted, the missing source contribution to the temperature is

    r^(m-sigma)e(theta),     e=ell D_T/(beta sigma),          (7)

and the missing vorticity contribution is

    r^(-s-sigma)c(theta),    c=ell D_O/(beta sigma).          (8)

Indeed dilation multiplies each by -beta sigma; their other interactions occur only at lower orders in (4). Equations (7)--(8) state necessary leading corrections, not a convergent full expansion or an existence claim. Since sigma/s=beta/3 lies strictly between 1 and 4/3, these powers are absent from an integer ladder in s. They coincide with existing powers at beta=3, where this separated-power theorem does not apply. They disappear when ell=0.

For the stored r2 compactification with basis exponent exactly beta, a nonzero spline endpoint gives h=L^(1+2s)H0, with H0=cos(theta)^2 sum_k cF_(k,end) T_k(-sin(theta)). The next term is d=-L^(1+3s)H1, where H1 uses the exact endpoint spline derivatives. Similarly a=L^(1+s)A0 and b=-L^(1+2s)A1. For a source kept at seed exponent3, aS=L_S^(1+sigma)AS0 and pS=L_S^(1+sigma)PS0, where PS0 solves (2) with AS0. Thus the presence of the mixed source term can be checked by exact rational Laurent arithmetic on H0 and PS0, without evaluating the generally nonrational positive powers of L and L_S. In particular PS0'(theta0) != 0 is an exact rational test at either axis when the stored seed coefficients and beta=3 are treated exactly.

The theorem does not show that a finite-box normalized residual must be large. When beta is close to3, the two positive powers are close and can nearly cancel across a long finite range. It does not rule out approximation by increasingly rich bases or a B2 solution at ell=0. A fixed-source formulation is mathematically legitimate; this theorem concerns the completeness of the particular unknown-field tail representation and the absolute residual of that represented field on the full plane.

## Dependencies and evidence

All formulas used in the proof were derived above. Packet89 independently supplies the stored r2 endpoint expansions, including differentiated remainders and exact binary input interpretation. Packet03 supplies the kernel convention. No numerics-lane code is reused; no formalization is claimed and no Lean or Lake process is run. Computational checks and model review, when complete, are recorded in verification/ with their actual UTC times and limitations.

## Verification record 2026-10-21T01:22:53.808563+00:00
The independently implemented native_mixed_tail_checks.py passed32 high-precision Cartesian residual and Laplacian checks at four rational beta values and four radii, as well as exact exponent orderings and mixed-correction cancellations. The full source-stream angular coefficients of the two actual seed defects were evaluated over exact rationals: their derivatives at the lower/upper axis, after omitting the positive L^(4/3) factor, are approximately4.750932/-1.281165 (K12) and4.750236/-1.280424 (K16), each exactly nonzero. Both source-axis zeros are therefore simple. Thus whenever a saved native-source state has3<beta<4, nonzero lambda and nonzero represented temperature endpoint, theorem(6) gives D_T nonzero and theorem(4) proves its represented absolute temperature residual is unbounded. This is a representation conclusion, not a zero-forcing endpoint exclusion. No such new native-source state was yet available in this check; the source data are the original archived seeds. Runtime0.464134s.

Actual claude-opus-5-5 request122 supplied written sign/exponent checks and requested the explicit residual equations, now added. Its output stopped at the inverse section with provider stop_reason refusal, so it is a partial audit only. Its table row m-3s=-3s is incorrect and unused; that row is rejected. Request123 seeks a written inverse and simple-zero audit.

## Completed model exchange 2026-10-21T01:32:55.405083+00:00
Requests123 and124 used overly narrow briefs: the reviewer asked for hypotheses and an inverse estimate already present above. Request123 also incorrectly treated the fixed source as transported vorticity, inventing a source-source term. That objection was rejected using the explicitly stated residual and withdrawn in124. Request125 received the complete inverse and simple-zero hypotheses and returned a written audit finding no concrete gap (actual model claude-opus-5-5; 38.002913s; end_turn). Its comment about “either axis” misread the two explicitly named symmetry-axis half-lines theta0=+/-pi/2, and does not change(6). The independent argument and32 tests remain the evidence; no model output substitutes for proof.
