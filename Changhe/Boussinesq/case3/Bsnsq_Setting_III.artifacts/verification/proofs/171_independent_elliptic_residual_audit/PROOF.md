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

## Exact counterexamples to stronger diagnostic conclusions

The following elementary constructions make the statistical and differentiation limits precise.

1. Fix epsilon>0 and M>epsilon. At two sample locations take (|E|,N)=(epsilon,1) and(epsilon,epsilon/M). Then max|E|/max N=epsilon, whereas max(|E|/N)=M. Thus a ratio of separate maxima cannot bound the pointwise ratio. Here N represents a source amplitude, not the sum of every PDE term, so no triangle-inequality upper bound is assumed.

2. Take a smooth radial bump A supported in an annulus and positive at r0. Set Omega=A(r)(sin phi+sin2phi) and let an approximate inverse instead invert Omega+epsilon A(r)sin phi in the same canonical relative gauge. Both sources are smooth on the plane because they vanish near0 and outside the annulus. At phi=2pi/3, Omega=0 but E=epsilon A(r0)sqrt(3)/2 is nonzero. The modal source-amplitude sum is2A(r0). Thus an arbitrarily small error compared with that sum gives no relative error bound against the pointwise physical vorticity. This construction concerns numerical inverse accuracy, not a B2 profile.

3. For a fixed h>0, let f(t)=t(t^2-h^2)(t^2-4h^2). The two-point centered differences (f(h)-f(-h))/(2h) and (f(2h)-f(-2h))/(4h) both vanish, because all sampled values do. Their Richardson combination and difference vanish, but f'(0)=4h^4 is nonzero. Multiplying f by any constant gives an arbitrarily large error with zero estimated difference. More generally, for any finite set of positive displacement magnitudes A, f(t)=t product_{a in A}(t^2-a^2) vanishes at every stencil sample, while f'(0)=product_{a in A}(-a^2) is nonzero. Every such f is analytic. A finite step comparison therefore needs a quantitative derivative bound or other regularity information to certify its error. It remains useful evidence, not a proof by itself.

4. The harmonic stream error -sigma xy produces delta V=(sigma x,-sigma y). Direct differentiation gives delta E=0 and div delta V=0, and delta V(0)=0, although the B2 strain c=Psi_xy(0) changes by -sigma. This error is ruled out by the true canonical global sublinear law, but cannot be ruled out by interior curl/divergence residuals and a center-velocity check. It is the degree2 mode that an omitted exterior source can induce inside a finite disk.

## Verification plan and dependencies

Write this proof before the controls and archive evaluation. Check the radial identity and difference moments with exact symbolic arithmetic; compare the quadrature with the closed-form velocity for several angular modes and slow tails; evaluate E by Cartesian differences without using the radial Poisson equation. Then freeze the selected numerical archives, use the verifier's own value reader and full-plane inverse, vary both Cartesian step and quadrature tolerance, and retain the raw values, coordinates, knot-crossing flags and quadrature statuses.

The fitting lane's evaluator and differentiation code are not imported or executed. The only shared inputs are numerical archives. Dependence is on elementary harmonic analysis, Taylor expansion and the explicitly displayed formulas. No Lean/Lake, JavaScript, server, cluster or GPU is used. The full B2 transport equations, center constraints and far-field certificates are checked separately in the existing audit corpus.

Written UTC 2026-10-21T13:34:30.740342+00:00, before new control code.

Revision UTC 2026-10-21T13:38:19.512063+00:00: explicit relative modal notation, finite sine scope, direct n=1 antiderivatives, exact-axis normalizer, source-evaluation error, actual r2 center regularity and harmonic blindness added after independently checking review283. No result from a divergent-integral split is used.

Counterexamples written UTC 2026-10-21T13:40:52.372019+00:00, before their exact control code.

Revision UTC 2026-10-21T13:43:53.107211+00:00: explicitly stated source decay, actual angular conversion, clamping and center mapping after independently checking the written portion of review284.

Revision UTC 2026-10-21T13:47:21.769738+00:00: made the two-point Richardson counterexample distinct from the seven-point audit and named c explicitly, following the completed written review285.
