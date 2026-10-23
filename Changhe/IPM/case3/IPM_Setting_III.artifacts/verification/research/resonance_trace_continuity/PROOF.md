# Quantitative persistence of the first resonance near a pure trace

Verifier result157, written 2026-10-21 before supporting arithmetic. This gives a sufficient strong-norm condition for nonvanishing, complementing result156's dependence on arbitrarily high angular modes. The numerical radii obtained below are deliberately conservative. They are not claimed to be useful tolerances for a current numerical state.

## 1. Statement, space and scope

Use either (ell,K,M)=(3,5,2) or (5/2,9,4). Set p=1/ell, delta=1-p and s_i=p-i delta. M is the positive even stream frequency, not the report's half-frequency index. For an odd sine series f(theta)=sum_(n positive odd) a_n sin(n theta), put

    ||f||_j = sum_n (1+n)^j |a_n|, j>=0.

For cosine series use the same weighted coefficient norm, including n=0. The corresponding complete coefficient spaces are denoted X_j. They are continuously embedded in C^j for integer j; the converse embedding is not asserted. Smooth periodic functions belong to every X_j, since sufficiently many integrations by parts make their Fourier coefficients summable with the weight.

Define the finite recurrence P_k[Theta] and the resonant functional g[Theta] as in result156. For Theta in X_K the recurrence is well-defined, with P_k in X_(K-k) for k<=K. It agrees with the finite-polynomial definition and is continuous. Explicit constants defined below satisfy, for R=max(||Theta||_K,||Phi||_K),

    ||P_k[Theta]-P_k[Phi]||_(K-k)
        <=(k+1) C_k R^k ||Theta-Phi||_K,                 (1)

and

    |g[Theta]-g[Phi]| <= M(K+1) C_K R^K ||Theta-Phi||_K.  (2)

Let g0=g[sin(theta)] be the nonzero rational in result150. Define

    epsilon0 = min(1, |g0|/[2 M(K+1) C_K (2^K+1)^K]).    (3)

For any real A!=0, if

    ||Theta-A sin(theta)||_K <= epsilon0 |A|,

then g[Theta] has the same sign as g0 A^(K+1) and

    |g[Theta]| >= |g0| |A|^(K+1)/2 > 0.                 (4)

If Theta is the trace of an exact exterior profile with smooth symbol bounds S^p, this forces its first stream logarithm at degree -M. If Theta is smooth and nonzero, it also forces a nonzero density logarithm at degree p-M-2. These are conditional implications. No such profile is constructed, and logarithms at infinity do not exclude local smoothness or a primary profile.

## 2. Bounds for the particular canonical velocity

For i<K, q_i=|s_i+1| is not a positive even integer. Define

    B_i = sup_(m positive even) (m+q_i)/|m-q_i|.

This is finite. If q_i=0 take B_i=1. Otherwise it suffices to evaluate the positive even neighbors of q_i: for m>q_i the ratio decreases with m, while for 0<m<q_i it increases with m. Include the first even integer2 if q_i<2. Thus B_i is explicitly rational in the two cases here, and its exact calculation involves at most two frequencies per i.

Set

    L_i = B_i [(3/2)^K+1]/2.                            (5)

Let V_i[f] be the polar velocity coefficient obtained by the particular inverse of density r^(s_i) f. Its stream modes are

    H_m = G_m/[m^2-(s_i+1)^2],

where a density mode n contributes (s_i-n)a_n/2 at m=n+1 and (s_i+n)a_n/2 at m=n-1, with m=0 dropped. The polar coefficients are -m H_m in the cosine radial component and (s_i+1)H_m in the sine angular component.

For one input coefficient a_n, the sum of the absolute output amplitudes of the two velocity components, with weight (1+m)^j, divided by (1+n)^j|a_n|, is bounded by

    sum_(m=n+1,n-1; m>0)
      [(1+m)/(1+n)]^j (m+q_i)|s_i +/- n|
                              /[2|m^2-q_i^2|].          (6)

In the upper shift |s_i-n|=|s_i+1-m|<=m+q_i; in the lower shift |s_i+n|=|s_i+1+m|<=m+q_i. Cancel m+q_i from the denominator factorization. Each term of (6) is therefore at most half B_i times its weight ratio. The upper ratio is at most (3/2)^j because n>=1; the lower ratio is at most1. For 0<=j<=K this proves

    ||(V_i[f])_r||_j+||(V_i[f])_theta||_j <= L_i ||f||_j. (7)

For q_i=0 the same argument is valid. No growing or global decaying harmonic term is included in V_i: this is the particular operator for the isolated pure radial degrees. Global harmonic sectors do not meet any of the degrees k delta with k<=K, by result150's radial arithmetic.

## 3. Bilinear bounds and the recurrence

Weighted trigonometric coefficient norms obey ||fg||_j<=||f||_j||g||_j for compatible sine/cosine products. To see it, use product-to-sum and

    1+|n +/- m| <= (1+n)(1+m).

The factors1/2 and the at most two output frequencies sum to1. Negative sine frequencies are reflected with a sign and may cancel; the triangle inequality is enough. Constant cosine modes cause no loss. Also ||f'||_j<=||f||_(j+1), and ||f||_j<=||f||_(j+1).

The advection of density r^(s_j)P_j by velocity coefficient V_i[P_i] has angular coefficient

    s_j (V_i[P_i])_r P_j + (V_i[P_i])_theta P_j'.

For any integer t>=0 with t+1<=K-j and t<=K-i, (7) and the product bounds give

    ||B_i,j(P_i,P_j)||_t
       <= L_i (|s_j|+1) ||P_i||_(K-i) ||P_j||_(K-j).     (8)

The factor |s_j|+1 is a convenient upper bound; no sharpness is asserted. At recurrence level k, choose t=K-k. Since i+j=k-1, both required inequalities hold.

Define C_0=1 and recursively

    C_k = [ell k delta]^(-1)
          sum_(i+j=k-1) L_i (|s_j|+1) C_i C_j, 1<=k<=K. (9)

All constants are finite positive rationals. Induction using the exact recurrence proves

    ||P_k[Theta]||_(K-k) <= C_k ||Theta||_K^(k+1).

The same bounded linear inverse and bilinear products define P_k for infinite series by completeness. Alternatively approximate Theta by its finite Fourier projections, which converge in X_K; (1), proved next first for polynomials, makes all successive coefficients Cauchy and agrees with the direct bounded-operator construction. There is no inverse in a resonant degree in this construction: only P_K, not H_K, is computed.

For the difference estimate, subtract each bilinear term as

    B(P_i[Theta], P_j[Theta])-B(P_i[Phi],P_j[Phi])
      =B(P_i[Theta]-P_i[Phi],P_j[Theta])
       +B(P_i[Phi],P_j[Theta]-P_j[Phi]).

Apply the induction hypothesis, (8), and the amplitude bound. The two factors of the difference estimates are (i+1)+(j+1)=k+1. The remaining powers sum to R^k. Division by ell k delta and (9) prove (1). This argument passes to the X_K limit, proving continuity without assuming analyticity of Theta.

For X_K data the final source need only be interpreted coefficientwise (or as a distribution); the identity below defines its continuous target coefficient without differentiating an X_0 function pointwise. At s_K=-M-1 the source coefficient of sin(M theta) is -M times the density coefficient of sin((M-1)theta): the adjacent sin((M+1)theta) contribution has factor (s_K+M+1)/2=0. Coefficient extraction is bounded by the X_0 norm. Thus (1) at k=K proves (2).

## 4. Persistence and the density logarithm

For Phi=A sin(theta), ||Phi||_K=2^K|A| and homogeneity gives g[Phi]=g0 A^(K+1). If ||Theta-Phi||_K<=epsilon0|A| with epsilon0<=1, then R<=(2^K+1)|A|. Estimate(2) and (3) give

    |g[Theta]-g0 A^(K+1)| <= |g0| |A|^(K+1)/2.

This proves (4), including its sign assertion for every nonzero real A.

For an actual exterior profile, radial sector isolation still places the first possible resonance at s_K and there is no earlier logarithm. The coefficient just proved nonzero forces stream

    [g/(2M)] r^(-M) log(r) sin(M theta).

Its velocity's highest logarithm acting on the leading density r^p Theta gives

    -(g/2) r^(p-M-2)log(r)
            [p cos(M theta)Theta + sin(M theta)Theta'].   (10)

The decreasing-degree argument of result155 proves this is the entire forcing of the first density logarithm. Transport inversion divides it by ell(M+2).

The bracket in (10) cannot vanish identically for a nonzero smooth Theta. Indeed on any open interval between consecutive zeros of sin(M theta), the equation that it vanishes has solutions

    Theta(theta)=C |sin(M theta)|^(-p/M).

This follows by the first-order integrating factor, and includes the zero solution without dividing by Theta. Since p/M>0, boundedness at either endpoint forces C=0. Every such interval has zero Theta, and continuity then gives Theta identically zero. Thus a nonzero smooth trace and g!=0 force a nonzero first density logarithm.

## 5. Verification and limits

The supporting exact checker computes B_i by its two-neighbor formula, verifies every relevant source/inverse column bound through a finite range while the monotonicity proof covers the tail, computes all C_k and epsilon0 as fractions, checks exact persistence and recurrence algebra, and rechecks the specialized pure coefficients. These computations support the proof; finite sampling alone does not establish the infinite-mode operator bound.

Result156 and this result are compatible. Adding a high Fourier mode can change g, however small its amplitude. If its full X_K norm is sufficiently small, (4) proves that the change cannot cancel or reverse a nonzero pure-trace g. The radius here is a sufficient conservative bound in a strong norm, not a necessary condition, and not a measured error bar for a numerical candidate. A finite set of Fourier coefficients without a tail bound cannot apply (3).

Dependencies: the finite recurrence, exact g0 and radial isolation from result150, the functional interpretation in156, and the conditional finite-depth expansion theorem142. OPEN: profile existence, trace realization, cancellation at larger distances, and every principal endpoint requirement not already verified elsewhere.
