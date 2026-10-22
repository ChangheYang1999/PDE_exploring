# New K40 elliptic, transport-geometry and endpoint diagnostics

## Precise scope

This packet independently checks the literal archive blamL2B40_beta3.085.npz against the three newly published ell_, stag_ and ffno_L2K40_b3085.json diagnostics. It is a finite-state audit, not a proof that the inverse error is bounded, that no unobserved stagnation point exists, or that the approximate profile solves B2. P248 already rejects this archive by its exact defining center residual and nonzero tail coefficients. That verdict is unaffected by auxiliary diagnostics. The self inverse is B[Omega]; the forced transport field is W=beta X+B[Omega]+lambda B[f], with f in its stored seed basis. The two source interpretations remain distinct.

For completeness the exact elliptic identities, representation, inverse and differentiation assumptions follow. These are the verifier's previously proved P171 statements, reused without executing numerical-lane code. New finite outcomes are recorded only after the independent runs.

# A Cartesian check of the full-plane inverse, with exact manufactured sources

Status: the identities and manufactured family below are proved. Numerical error estimates from finite samples are diagnostics, not certified full-plane bounds. No B2 profile or full class exclusion is claimed.

## Statement and notation

Use the B2 sign convention U=(-Psi_y,Psi_x), Omega=-Delta Psi. Let V=U-U(0). At every point where the derivatives exist,

    E = d_y V_1 - d_x V_2 - Omega = -Delta Psi - Omega,
    div V = d_x V_1 + d_y V_2 = 0.

Consequently these two combinations of independently differentiated velocity provide elliptic and divergence checks. Neither requires differentiating the radial Green formula or substituting its differential equation. We use physical Cartesian points, with polar convention (x,y)=(r sin phi,-r cos phi).

For each positive integer n, a real weight w, and 1<p<2, put a=(p-n)/2 and

    Psi_n(r,phi) = w r^n (1+r^2)^a sin(n phi),
    Omega_n(r,phi) = -4 a w r^n [(n+1)+(n+a)r^2]
                         (1+r^2)^(a-2) sin(n phi).

Both functions extend smoothly through r=0. The stream has order r^p, its velocity order r^(p-1)=o(r), and its vorticity order r^(p-2). Subtracting w r sin(phi)=w x from Psi_1 and subtracting nothing for n>=2 gives the relative gauge V(0)=0. Finite sums preserve these assertions. The corresponding relative velocity is the canonical whole-plane inverse of the displayed vorticity. Thus the family supplies exact noncompact tests with slow power decay for an independent full-plane quadrature.

## Proof of the identities and manufactured family

Differentiating V eliminates the constant U(0). The formulas for E and divergence follow directly from equality of mixed partial derivatives.

The function r^n sin(n phi) is a homogeneous harmonic polynomial in x,y. Multiplication by (1+r^2)^a is smooth for real a, so all fields extend smoothly through the origin. If q(r)=r^n F(r^2) and t=r^2, direct differentiation gives

    q''+q'/r-n^2 q/r^2 = 4 r^n [(n+1) F'(t)+t F''(t)].

Taking F(t)=w(1+t)^a gives the displayed Omega. For r large the stream and each fixed derivative have the expected symbol orders p,p-1,..., and Omega has order p-2<0. Near0, Psi_1=w x+O(r^3), so subtracting w x removes its constant velocity. For n>=2 the velocity is already zero at0.

For completeness the canonical relative velocity is

    V(X) = integral_R2 [K(X-Y)-K(-Y)] Omega(Y) dY,
    K(Z)=(Z_2,-Z_1)/(2pi |Z|^2).

Local kernel singularities are integrable for smooth Omega. At infinity the difference is O_X(|Y|^-2), and Omega=O(|Y|^(p-2)), so the radial integral is bounded by a constant times integral^infinity r^(p-3) dr, which converges since p<2. The usual local/far split and the same kernel estimate give sublinear growth, in fact O(1+|X|^(p-1)); smoothness and the divergence and curl equations follow by localizing the kernel and differentiating the smooth remainder. Alternatively angular separation gives exactly the convergent modal formulas below and the same equations and growth.

The difference of this relative inverse and the displayed stream velocity has zero divergence and zero curl, hence harmonic components. It is smooth on the plane and sublinear. A harmonic function h=o(r) is constant: the interior gradient estimate at any fixed X in a disk of radius R bounds |grad h(X)| by C/R times its supremum on that disk; the latter is o(R), so letting R tend infinity gives zero. Both relative fields vanish at0, so the constant difference is zero. This proves the claimed canonical gauge.

For the general finite-mode inverse considered here, assume the field is smooth at0, locally at least C4, and every radial source coefficient is O(r^-s) for a fixed 0<s<1 as r tends infinity. These conditions hold for the manufactured family with s=2-p and for the frozen archive sources described below. They ensure convergence of the relative kernel and sublinear growth by the same estimates. For an angular coefficient h_n(r) of Omega, write psi_n for the radial coefficient of the stream in the relative gauge (in particular psi_1=Psi_1-wr in the manufactured family). Only finite sine sums are used: x-reflection removes the constant and cosine angular modes. Solving the radial Poisson equation gives for n>=2

    psi_n(r)/r = r/(2n) [A_n(r)+B_n(r)],
    psi_n'(r)  = r/2 [-A_n(r)+B_n(r)],
    A_n(r)=int_0^1 z^(n+1) h_n(rz) dz,
    B_n(r)=int_0^1 z^(n-3) h_n(r/z) dz.

For n=1 the convergent relative expression is

    psi_1(r)/r = r/2 [A_1(r)-C(r)],
    psi_1'(r)  = -r/2 [A_1(r)+C(r)],
    C(r)=int_0^1 h_1(rz) dz.

They follow by variation of parameters using homogeneous solutions r^n and r^-n; regularity at0 removes r^-n and sublinearity removes the growing velocity for n>=2. For n=1 no divergent integral is split. If Lq=q''+q'/r-q/r^2, q is regular and q'(0)=w, then Lq=(q'+q/r)' and r^2 Lq=(r^2 q')'-(rq)'. Integrating on[0,r] gives int Lq=q'+q/r-2w and int s^2Lq=r^2q'-rq. With h=-Lq, the displayed relative formula is exactly q-wr. Its derivative gives the second formula. For the general finite smooth sine source, direct endpoint differentiation and the conditions at0 and infinity give the same canonical solution. Direct differentiation of the integral endpoints verifies the Poisson equation, and the preceding uniqueness determines the canonical interpretation. These formulas specify the quadrature being tested; they are not substituted when forming the numerical elliptic residual.

## Differentiation and limits of the numerical audit

For a Cartesian scalar function f define the centered seven-point first difference

    D_h f = [-f(-3h)+9f(-2h)-45f(-h)+45f(h)-9f(2h)+f(3h)]/(60h),

where the arguments denote displacements along one coordinate from the point under test. The polynomial moments give sum_j w_j j=1 and all other moments through degree6 equal0. The degree7 moment is36. Taylor expansion at a point with seven derivatives therefore gives

    D_h f = f' + h^6 f^(7)/140 + o(h^6).

A convergence claim using this order requires the stencil to lie in a sufficiently smooth neighborhood. The stored degree5 splines are only C4 in the source at simple knots, so no uniform sixth-order truncation law across knot circles is asserted. For a C1 velocity, the difference still tends to the derivative, but its rate requires further information. Knot-crossing stencils are recorded separately.

The absolute sum of the first-difference weights is11/6. If each evaluated velocity component has a uniform error at most epsilon on the stencil, then the differentiated component error is at most11 epsilon/(6h), and the two-term elliptic combination error is at most11 epsilon/(3h). If the source evaluation has error epsilon_Omega, add epsilon_Omega to the elliptic error bound. These bounds are conditional on genuine uniform errors; adaptive quadrature estimates do not supply such a certificate. It explains why reducing h can increase error and why a small finite-difference change alone cannot certify the inverse.

The diagnostic normalizer is

    N_E=|d_y V_1|+|d_x V_2|+|Omega|.

At N_E=0 the convention is0/0=0 and nonzero/0=infinity. There is no positive floor. For the exactly x-reflection-symmetric fields, both velocity derivative terms and Omega vanish on x=0, so the exact N_E is zero there. Symmetry-axis points are retained for absolute error; the computed ratios and zero counts are reported separately, because roundoff can make those ratios order one even for an accurate inverse. This elliptic diagnostic does not replace the divided transport residuals and their axis limits required by the B2 prompt.

The stored r2 representation uses b=beta_basis>1, L>0, and

    t=1-(1+(r/L)^2)^(-1/(2b)),
    Omega=x (1-t)^(b+1) sum_k P_k(t) chi_k(r) cos(k phi),
    Theta=x^2 (1-t)^(b+2) sum_k Q_k(t) chi_k(r) cos(k phi),
    chi_k=1 for even k,  r/sqrt(L^2+r^2) for odd k.

Here P_k,Q_k are degree5 splines clamped with multiplicity6 at t=0 and t=1. Their first floor(k/2) coefficients are masked. In this convention cos(phi)=-y/r and x=r sin(phi). Thus Omega has the finite sine expansion from sin(phi) cos(k phi)=(sin((k+1)phi)-sin((k-1)phi))/2 for k>=1, with k=0 giving sin(phi). Theta is even in x; it is not an inverse source and need not have a sine expansion.

The variable t is analytic in r^2 near0, t(0)=0, and dt/d(r^2)(0)=1/(2bL^2)>0. On the first cell the clamped basis function with coefficient index j has a factor t^j for j=0,...,5. Consequently each active cosine mode starts with r^k times a smooth function of r^2; modes with all six first-cell coefficients masked vanish on the first cell. The factor r^k cos(k phi) is a homogeneous harmonic polynomial. Multiplication by x in Omega and by x^2 in Theta preserves smoothness. The assertion is C-infinity regularity near the center only, not at the later simple knots, where the decoded sources are C4.

At infinity every spline is bounded on[0,1] and |chi_k|<=1. Therefore Omega=O(r^-1/b) and Theta=O(r^(1-2/b)). For the inverse the former is the required decay hypothesis s=1/b in(0,1). An additive native seed source has the same formula with its own positive parameters, and any finite combination obeys the slowest of its positive decay exponents. The present elliptic audit uses the self source Omega only. These assertions concern the verified archive format, not generic radial splines.

A small E and div do not test the canonical gauge or the full exterior inverse. For example, adding the harmonic stream -sigma xy changes V by(sigma x,-sigma y), which vanishes at0 and has zero curl and divergence, yet changes the center strain. A tail truncated outside a disk similarly adds a harmonic mode inside that disk. Such an affine strain is prohibited globally by the canonical sublinear law, but local differential residuals do not detect it. Manufactured velocity comparison, center-strain moments, and independent exterior checks remain necessary.

Every reported maximum is over the stated finite sample set. A ratio of separate maxima, max|E|/max N, is a different quantity from max(|E|/N) at common points. Absolute sums of angular mode amplitudes are also different from the pointwise vorticity, which can vanish by cancellation. No global or pointwise physical-vorticity bound follows from a bandwise modal ratio without further estimates.


## Transport geometry

For any nonzero X put q(X)=|W(X)|/(beta|X|) and d(X)=W(X).X/(beta|X|^2). A nonzero W at a finite set establishes only that no zero occurs at those points. Even strict positivity of d there gives no global zero exclusion. We compare all published witness points with the independent full-plane inverse and also sample a shifted grid with different radii and angles. Near0 the exact center derivative diag(beta-c,beta+c) gives q(r,0) tending to|beta-c|/beta. Here c is the strain of the same source mixture used in W. Two Cartesian center-difference scales are compared with that exact moment.

The limitation is structural. Given a finite preserved set, choose an off-axis point p=(a,b) outside it and its reflection, and a smooth cutoff chi supported near p, disjoint from those sets and the axis. With d0>0 set P=-beta b(x-a)+beta a(y-b)+(beta+d0)(x-a)(y-b). The odd stream chi P-(chi P)(-x,y) is compact and has velocity-beta p at p and derivative diag(-beta-d0,beta+d0). Thus W has derivative diag(-d0,2beta+d0) there and a hyperbolic saddle, while its values near every preserved point and0 are unchanged. Its velocity is the ordinary full-plane inverse of its compact vorticity by Gamma*(-Delta psi)=psi. This example is not a B2 profile. It shows why a finite positive scan alone does not supply a zero-exclusion certificate. P194 contains the full extension to an arbitrary base velocity, but no such extension is needed for this elementary diagnostic limitation.

## Exact endpoint coefficient check

Use standard polar angle theta, s=1/beta, m=1-2s, k=2-s. The native archive has beta=beta_basis in(3,4), so at infinity

    Omega=r^(-s)a+r^(-2s)a2+O_C1(r^(-3s)),
    Theta=r^m b+r^(m-s)b2+O_C1(r^(m-2s)).

Write the endpoint splines Q for F and P for G in angular Chebyshev form T_j(-sin theta). Their exact last-cell endpoint value and derivative are available from binary coefficients: value c_last and derivative deg(c_last-c_prev)/(1-t_last_internal). If H0=cos(theta)^2 sum Q_j(1)T_j(-sin theta), H1 the corresponding derivative sum, and A0,A1 use cos(theta) and P_j, then

    a=L^(1+s)A0, a2=-L^(1+2s)A1,
    b=L^(1+2s)H0, b2=-L^(1+3s)H1.

Indeed 1-t=L^s r^(-s)(1+O(r^-2)), and the Taylor remainder on the last interval is quadratic. The odd-mode factor r/sqrt(L^2+r^2) differs from1 by O(r^-2), later than the orders displayed. Multiplication by x or x^2 supplies the powers and angular factors. Fixed derivatives obey the displayed C1 orders because the exterior is one polynomial cell with analytic radial factors.

The leading self stream is r^k p, where p''+k^2p=-a. As k is not an integer, its unique trigonometric solution has Fourier coefficient p_n=a_n/(n^2-k^2). Its velocity components in the radial/angular frame are r^(1-s)(-p',kp). The self equations would require

    a2_pred=kp a'+s p'a-m cos(theta)b+sin(theta)b',
    b2_pred=kp b'-mp'b.

To derive them, beta r partial_r+1 kills r^(-s) and multiplies r^(-2s) by-1; beta r partial_r-(beta-2) kills r^m and multiplies r^(m-s) by-1. Advection by the leading self velocity gives the other displayed products, and partial_x(r^m b)=r^(m-1)[m cos(theta)b-sin(theta)b']. These coefficients are exact for the chosen representation and branch parameters. The angular squared L2 mean is the sum of squared complex Fourier coefficients, so their norms can be computed without angular sampling. Printed norm comparisons are floating evaluations of exact rational coefficient formulas and real powers of L.

The actual forced field also contains the source with exponent sigma=1/3. It adds distinct mixed residual powers r^(-s-sigma) in vorticity and r^(m-sigma) in temperature. No equality of the displayed self relations is expected for a forced profile. Finite-window fits after subtracting modeled mixed terms need not equal the literal endpoint coefficients. In particular their small finite-window mismatch is not a certificate that exact endpoint relations hold. The complete asymptotic remainder and nonzero-witness proof for this archive is in P248; the formulas needed for the finite coefficient comparison are derived above.

## Dependencies and verification plan

The complete statements above precede this packet's new computations. The independent elliptic generator takes Cartesian differences of its own full-plane velocity at210 points, two quadrature tolerances and three step sizes. The geometry check uses the same full-plane inverse with an explicitly constructed native seed mixture, and a shifted polar grid independent of the numerical lane's grid. The endpoint check regenerates the last-cell coefficients with exact Fractions and uses polynomial multiplication/Parseval; no NUM evaluator is imported or executed. Earlier P171 manufactures, P194 structural proof and P248 exact archive certificates are dependencies, not newly counted tests. Finite quadrature success flags and finite differences are diagnostics only. No formalization is claimed or run.
