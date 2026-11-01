# A triangular majorant for every integer resonance period

Status: PROVED, with independent theory-part confirmation dated2026-10-31T10:38Z and the whole-theorem audit V273. The proof applies to every integer Q>=3. Its hypotheses include a uniform nonzero response.

## Statement

Fix an integer Q>=3, delta=2/Q, c=Q/(Q-2), and an even integer B>=2. Let f_1 be a nonzero real sine polynomial supported on the odd frequencies below B. Use the pure S1 density and stream expansions, with exponents p_n=1-2n/Q and P_n=p_n+1. At each resonance n=kQ, k>=2, remove the entire resonant stream mode in the particular Poisson inverse and denote the remaining harmonic coefficient by H_n.

Suppose the first compatibility obstruction O_(2Q) vanishes and the responses defined by the Q-step equations in130 satisfy

    s := inf_(k>=2) |sigma_k| > 0.

Then there is a unique compatible pure formal density/stream pair in this symmetry and normalization class. Its coefficients satisfy

    ||f_n||_1+||g_n||_1 <= C A^n

for finite C,A. The weighted density and stream power series are analytic in z=r^(-2/Q) near zero and in a nonzero angular strip. Every appropriately weighted spatial derivative converges uniformly on a sufficiently large closed exterior region. The sums solve both stationary equations there. A common smooth potential exists on a possibly smaller exterior region by the potential reconstruction theorem already proved in109. This statement does not assert a quantitative power-log series bound for that potential at general Q.

The sufficient radius can be chosen uniformly when B,Q,||f_1||_1 and1/s are uniformly bounded. The coefficients and sums depend holomorphically on finite-dimensional profile parameters within the compatible locus on which these bounds hold.

## 1. Exact tuning and elementary norm bounds

Topic130 proves that the next obstruction is R_k+sigma_k H_(kQ). Thus H_(kQ)=-R_k/sigma_k is the unique tuning at every step. No higher order free constant can change an earlier obstruction. The first compatibility condition is the only one independent of a preceding free harmonic.

The support bounds are Bn-1 for density and Bn for stream. The free resonant frequency2k-2 is within this bound. Every nonzero factored Poisson divisor has modulus at least2/Q. Each input sine coefficient contributes to at most two output modes with factors of modulus at mostQ/4. Hence both the ordinary inverse and the inverse with the resonant mode deleted satisfy

    ||Pi_n f||_1 <= L ||f||_1,       L=Q/2.                  (1)

This follows from the factored branches a_(m+1)/(2(m-P_n)) and -a_(m-1)/(2(m+P_n)); deleting the whole resonant output can only reduce their absolute bound.

For i,j>=1, |p_j|<=j and |P_i|<= (2-2/Q)i. The sine-product norm and support bound give

    ||T(g_i,f_j)||_1 <= B(3-2/Q) i j ||g_i||_1||f_j||_1.

Also n/lambda_n=n(Q-2)/(2(n-1))<=Q-2 for n>=2. Set

    kappa=B(Q-2)(3-2/Q),
    x_n=n||f_n||_1,
    eta_n=n|H_n| at resonances and0 elsewhere.

Then

    x_n <= kappa sum_(i+j=n) (L x_i+eta_i)x_j.              (2)

Before the first resonance there are no eta terms. In the majorant construction below it is sufficient to set eta_1,...,eta_Q=0, which only adds harmless later terms at artificial nonresonant indices.

## 2. Triangular inequalities for one lookahead block

Fix an actual resonance n=kQ and provisionally set H_n=0. For1<=r<Q define

    u_(n,r)=(n+r)||f_(n+r)^(0)||_1.

Every earlier resonant constant has index at most n-Q. In a convolution at n+r its partner therefore has index at least Q+r, hence at least Q+1. The density-density pairs with one index below r contain a provisional high term; remove them and count the two orientations separately. This gives

    u_(n,r) <= kappa [L sum_(i+j=n+r, i,j>=r) x_i x_j
                       + sum_(i+j=n+r, j>=Q+1) eta_i x_j
                       +2L sum_(s=1)^(r-1) x_s u_(n,r-s)].    (3)

For r=Q the same estimate bounds the provisional obstruction. Since n|R_k| <= (n+Q)||f_(n+Q)^(0)||_1, it gives

    eta_n <= (kappa/s) [L sum_(i+j=n+Q, i,j>=Q) x_i x_j
                         +sum_(i+j=n+Q, j>=Q+1) eta_i x_j
                         +2L sum_(s0=1)^(Q-1) x_s0 u_(n,Q-s0)]. (4)

The extension of the eta sums is legitimate: eta_i=0 for i<=Q, and j>=Q+1 ensures i<=n-1 in(3)-(4). Both density indices in the restricted sums are at most n. All the remaining u indices have smaller lookahead r. Thus equality in(2)-(4), now imposed at every artificial base index n>=Q+1, defines a nonnegative triangular majorant. First compute x_n, then u_(n,1),...,u_(n,Q-1), then eta_n. Induction dominates the actual coefficients and actual resonant lookahead blocks.

## 3. The finite polynomial fixed-point system

Choose a=||f_1||_1 and set the first Q majorant coefficients to

    x_j=Cat_(j-1)(kappa L)^(j-1) a^j,        1<=j<=Q.

They are exactly the coefficients of X=a z+kappa L X^2 through order Q. Write

    P(z)=sum_(j=1)^Q x_j z^j,
    X=P+z^(Q+1)W,
    sum_(n>=Q+1) eta_n z^n=z^(Q+1)E,
    sum_(n>=Q+1) u_(n,r) z^n=z^(Q+1)V_r.

For a polynomial H let [H]_(>=d) mean deletion of all terms of degree less than d. Put P_r=sum_(j=r)^Q x_j z^j, and

    A_r(z,W)=[P_r^2]_(>=Q+r+1)/z^(Q+r+1)
                +2(P_r/z^r)W+z^(Q+1-r)W^2,       1<=r<=Q.

These are polynomials with nonnegative coefficients. Summing the triangular equalities gives

    W=kappa L [P^2]_(>=Q+1)/z^(Q+1)
          +2 kappa L P W+kappa L z^(Q+1)W^2
          +kappa E(P+z^(Q+1)W),

    V_r=kappa [L A_r+z^(Q+1-r)EW
                   +2L sum_(s0=1)^(r-1) x_s0 V_(r-s0)],
                  1<=r<Q,

    E=(kappa/s)[L A_Q+z EW
                   +2L sum_(s0=1)^(Q-1) x_s0 V_(Q-s0)].     (5)

For the eta product, the restriction j>=Q+1 is exactly the product of z^(Q+1)E with z^(Q+1)W; division by the shifted power gives z^(Q+1-r)EW. The boundary terms do not shift the base index n, which explains the absence of an extra z factor multiplying the V terms.

Every genuinely nonlinear term in(5) contains a positive power of z. At z=0 the first equation determines W0 alone. Then each V_r, in increasing r, depends only linearly on W0 and the preceding V values. Finally E0 depends only linearly on W0 and the V values. Therefore the constant Jacobian is strictly lower triangular in the order

    W,V_1,...,V_(Q-1),E.

The matrix I-J is invertible. The holomorphic implicit function theorem gives a solution analytic near z=0. Its Taylor coefficients obey the same triangular equalities, hence equal the nonnegative formal majorants. Cauchy estimates give the claimed geometric bounds. This proves the all-order assertion without treating the finite low-order lookahead as an asymptotic approximation.

## 4. Spatial convergence and parameter dependence

At fixed B, converting a coefficient l1 bound into a complex angular strip costs at most exp(Bn tau). Each spatial derivative costs a polynomial in n and one inverse radial power. Thus any R with A exp(B tau) R^(-2/Q)<1 gives absolute uniform convergence of every weighted derivative. Multiplication of the series is justified by absolute convergence, proving the Poisson and stationary equations term by term. The uniqueness statement refers only to pure series with the imposed stream symmetry; arbitrary exterior solutions are not claimed unique.

For bounded a and1/s, the same positive majorant applies, so one common radius works. Every finite coefficient is a rational function of the profile coefficients with denominators consisting of fixed Poisson divisors and nonvanishing sigma_k. Uniform majorant bounds give normal convergence on a smaller parameter neighborhood, proving holomorphic dependence there. Exact compatibility is still required for the sums to solve the pure equations.

## 5. A uniform response bound and its limiting polynomial

The same norm calculation gives a useful bound without assuming compatibility. Define

    y_r=(n+r)||phi_r||_1/n.

The Q-step response equations yield

    y_r <= kappa[x_r+2L sum_(s0=1)^(r-1) y_s0 x_(r-s0)].

Majorize the low x_r by the Catalan coefficients above. If X=a z+kappa L X^2, the generating function of this last equality is

    Y=kappa X/(1-2kappa L X)
     =[(1-4kappa L a z)^(-1/2)-1]/(2L).

Consequently

    |sigma_k(f_1)| <= (1/2) binom(2Q,Q) kappa^Q L^(Q-1) ||f_1||_1^Q. (6)

This holds uniformly in k for complex profile coefficients. At sufficiently large k every shifted frequency in the finite Q-step response has fixed sign; it is enough that2k-2>=BQ. All response coefficients are then fixed rational functions of k and homogeneous polynomials of degree Q in f_1. The uniform bound(6) forces every polynomial coefficient to have a finite rational-function limit, with O(1/k) remainder. Thus sigma_infinity is a homogeneous polynomial of degree Q, and convergence to it is uniform on bounded profile sets.

The argument in129 therefore extends, conditional on one known uniformly responsive compatible profile: on any connected real analytic compatible submanifold containing that profile, the uniformly responsive set is open, dense and of full measure. This last statement supplies no explicit example at Q>3 by itself.

Dependencies:130for exact tuning and response identities, the elementary factored Poisson inverse, the holomorphic implicit function theorem, and109only for existence of a common smooth potential. No finite numerical experiment is used in this proof. No assertion of optimal constants, canonical zero-multipole convergence, whole-plane stationarity, or convergence at a response zero is made.

## Integral-period and pressure audit

No parity assumption on Q occurs: nonzero q+P_n and q-P_n are in(2/Q)Z, including for even Q. Possible odd-integer values of P_n cannot equal an even stream frequency. The exact resonance progression remains n=kQ,k>=2. Thus every displayed estimate and every finite shift applies unchanged to all integers Q>=3.

For completeness the exterior Darcy pressure is single valued. With u=(-psi_y,psi_x), the Poisson equation gives curl(u+rho e_y)=Delta psi+rho_x=0. The one-form (u+rho e_y) dot dX is invariant under reflection in either coordinate axis, while reflection reverses the orientation of a centered circle. Its period on that circle is therefore zero. Every exterior closed curve has period an integer multiple of this one; hence the closed one-form is exact and defines a single-valued pressure by grad p=-u-rho e_y. This adds no whole-plane extension claim.

The weighted uniform convergence proof also gives unweighted uniform convergence of the tails on every strict exterior: p_n and P_n are negative for all sufficiently large n, so each sufficiently late radial factor attains its maximum at the inner radius. A finite number of growing initial terms does not affect uniform convergence of the series. Topic132 strengthens the smooth-potential conclusion to a convergent potential series on the same strict radius, with only two finite logarithmic corrections.
