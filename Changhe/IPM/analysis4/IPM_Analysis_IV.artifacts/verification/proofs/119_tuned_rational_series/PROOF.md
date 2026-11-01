# Tuned pure series at delta = 2/3: independent audit

Status: PROVED under the exact hypotheses stated below. The abstract theorem and the two explicit algebraic examples have both been independently confirmed by Cartesian exact arithmetic. This document audits the theory part's Theorem T, frozen in sources/thmT.md. The verdict ledger is authoritative.

## Exact statement and normalization

Let c=3, delta=2/3, p_n=1-2n/3 and P_n=p_n+1. Let f_1 be a nonzero real odd-sine polynomial with largest frequency L, and set B=L+1. A pure S1 series has density terms r^(p_n) f_n(theta), with odd sine frequencies, and stream terms r^(P_n) g_n(theta), with positive even sine frequencies. In particular, the stream has no constant angular gauge term. All coefficient functions are periodic. Write a_(n,m) and b_(n,q) for their real sine coefficients.

The equations are

    2(n-1) f_n = sum_(i+j=n) [P_i g_i f_j' - p_j g_i' f_j],
    (q^2-P_n^2) b_(n,q)
        = ((P_n+q)/2) a_(n,q+1) + ((P_n-q)/2) a_(n,q-1).

The second equation is singular precisely at n=3k, k>=2, q=2k-2. Its compatibility condition is O_(3k):=a_(3k,2k-3)=0. Let Pi_n be the inverse at other orders and Pi'_n the inverse with the entire resonant output mode removed at order 3k. Set

    g_(3k)=Pi'_(3k) f_(3k)+H_(3k) sin((2k-2)theta).

Thus H_(3k) is the whole resonant coefficient, including neither of the two input branches in Pi'. This convention is essential.

Let sigma_k be the change in O_(3k+3) caused by changing H_(3k) by one while earlier constants are fixed. It is computed by the three response equations in sources/thmT.md, or equivalently by the independent Cartesian differentiation procedure below.

Assume O_6=0 and sigma_*:=inf_(k>=2)|sigma_k|>0. Then there is a unique pure formal S1 pair with this f_1 and stream normalization. Its coefficients satisfy

    ||f_n||_1+||g_n||_1 <= C A^n

for finite positive C,A. Consequently its density and stream series, with every derivative, converge on a sufficiently large exterior region and solve both stationary equations. A common smooth potential and a single-valued pressure exist there. This is an exterior assertion; it makes no whole-plane stationary extension claim. The potential need not itself have a log-free power expansion.

## Independent recurrence and affine tuning

For a homogeneous function r^q exp(i m theta), direct differentiation gives

    partial_x = (q-m)/2 r^(q-1) exp(i(m+1)theta)
              + (q+m)/2 r^(q-1) exp(i(m-1)theta),
    partial_y = i(m-q)/2 r^(q-1) exp(i(m+1)theta)
              + i(q+m)/2 r^(q-1) exp(i(m-1)theta).

Applying these twice gives Delta = (q^2-m^2) r^(q-2) exp(i m theta). Hence solving -Delta psi=partial_x rho gives exactly the displayed Poisson equation. The coefficient of u dot grad rho, with u=(-psi_y,psi_x), is the Cartesian determinant psi_x rho_y-psi_y rho_x. Its radial power at orders i,j is P_i+p_j-2=p_(i+j). Expanding that determinant in polar components gives P_i g_i f_j'-p_j g_i' f_j. The linear dilation coefficient is c p_n-1=-2(n-1), so the nonlinear term has the positive sign displayed above.

At n=3k, H_n first enters f_(n+1). Up to f_(n+3), every nonlinear product has at most one factor with index at least n, because 2n>n+3 for n>=6. Therefore each of these three coefficients is affine in H_n. Differentiating their recurrences with respect to H_n yields, respectively, one, three and five ordered terms. There is no missing product involving g_3: a changing density first has index n+1, so pairing it with g_3 first occurs at n+4. The last obstruction has the form

    O_(n+3)=R_k+sigma_k H_n.

Here R_k uses only earlier constants. Since O_6 is independent of them, induction gives the unique choice H_(3k)=-R_k/sigma_k. Both the response and sigma_k have degree three in f_1. Scaling f_1 by epsilon scales H_n, f_n and g_n by epsilon^n.

## Norm inequalities and triangular domination

Induction gives frequency bounds Bn-1 for f_n and Bn for g_n; the free frequency 2k-2 is smaller than B(3k). Products of sine and cosine polynomials have coefficient l1 norm at most the product of their norms. Since |p_j|<=j, |P_i|<=4i/3, and differentiation costs at most Bi or Bj, the bilinear norm is at most

    kappa i j ||g_i||_1 ||f_j||_1,  kappa=7B/3.

The factor m/[2(m-1)] is at most one for m>=2. Every nonzero factored Poisson divisor q+P_n or q-P_n has modulus at least 2/3. Each input coefficient feeds at most two outputs, each with factor at most 3/4. Therefore ||Pi_n|| and ||Pi'_n|| are at most 3/2, without any angular derivative loss.

Put x_n=n||f_n||_1, eta_n=n|H_n| at resonant orders and zero otherwise. Then

    x_n <= kappa sum_(i+j=n) [(3/2)x_i+eta_i]x_j.                 (I1)

For a fixed resonant n, set H_n=0 temporarily and define u_n=(n+1)||f_(n+1)^(0)||_1 and v_n=(n+2)||f_(n+2)^(0)||_1. The first bound uses only coefficients through n. In the second bound remove the pairs (1,n+1),(n+1,1), which together cost 3 kappa x_1 u_n. In the bound at n+3 remove additionally (2,n+1),(n+1,2); these cost 3 kappa x_2 u_n. Thus

    u_n <= kappa [(3/2) sum_(i+j=n+1) x_i x_j
                       + sum_(i+j=n+1,j>=4) eta_i x_j],
    v_n <= kappa [(3/2) sum_(i+j=n+2,i,j>=2) x_i x_j
                       + sum_(i+j=n+2,j>=4) eta_i x_j]
                       +3 kappa x_1 u_n,                         (I2)
    eta_n <= (kappa/sigma_*) [(3/2) sum_(i+j=n+3,i,j>=3) x_i x_j
                       +sum_(i+j=n+3,j>=4) eta_i x_j
                       +3 x_1 v_n+3 x_2 u_n].                    (I3)

The eta sums legitimately exclude the current H_n: every earlier nonzero eta has index at most n-3, hence its partner has index at least four. The larger displayed sums only add nonnegative terms. In the last bound, n|R_k| is at most (n+3)||f_(n+3)^(0)||_1.

Define majorant sequences by these equalities for every n>=4, not just resonances, and take eta_1=eta_2=eta_3=0. Also define x_n by (I1) at n>=2. This is triangular in the order x_n,u_n,v_n,eta_n. Indeed the largest x index on the last three right sides is n and each eta index is less than n. Induction therefore proves domination at every actual resonant order and trivially at other eta orders.

## The generating-function step

Write x_1=a, x_2=d=(3/2)kappa a^2, x_3=e=3 kappa a d, P=a z+d z^2+e z^3 and X=P+z^4 W. Write the eta,u,v generating functions as z^4 E,z^4 U,z^4 V. Direct shifting of the four coefficient identities gives

    W=(3/2)kappa[d^2+2ae+2de z+e^2 z^2]
        +3 kappa P W+(3/2)kappa z^4 W^2+kappa E(P+z^4 W),
    U=(3/2)kappa(2de+e^2 z)+3 kappa(P/z)W
        +(3/2)kappa z^3 W^2+kappa z^3 E W,
    V=(3/2)kappa[e^2+2(d+e z)W+z^2 W^2]
        +kappa z^2 E W+3 kappa a U,
    E=(kappa/sigma_*)[3eW+(3/2)z W^2+z E W+3aV+3dU].

For example the restricted x convolution in (I3) is (e z^3+z^4 W)^2, after dropping its z^6 term and shifting by z^7. The eta convolution always pairs eta with X-P=z^4 W; this explains the powers z^3,z^2,z in U,V,E. The unrestricted eta term in (I1) pairs eta with X and gives E(P+z^4 W).

At z=0 the first equation determines W_0 alone, then the second U_0, the third V_0 and the fourth E_0. Every nonlinear term contains a positive power of z, and the constant linear Jacobian in the order W,U,V,E is strictly lower triangular. Therefore I-J is invertible, with determinant one. The holomorphic implicit function theorem at this explicitly determined constant solution gives a holomorphic solution near zero. Its Taylor coefficients satisfy the same triangular coefficient equations, so they equal the nonnegative formal majorants. Cauchy estimates on any smaller disk give geometric coefficient bounds. No assumption that sigma_* is large is needed.

## Convergence, potential and uniqueness scope

The finite frequency bounds convert the coefficient bound into a geometric bound in an angular strip, with ratio A exp(B tau) r^(-2/3). Each Cartesian derivative introduces an inverse radial power and a polynomial factor in n. The appropriately weighted derivative series are uniformly absolutely convergent for r>=R when R>A^(3/2) and tau is sufficiently small. The unweighted derivative series are uniformly absolutely convergent in their tails too: omit the finitely many terms whose radial exponent is positive, then every remaining radial factor is bounded by its value at R. Finite growing terms do not obstruct uniform convergence of a series. This supplies a minor detail implicit in the theory part's displayed weighted estimate.

The normal convergence in complex z and theta concerns the weighted generating functions r^(-1/3)rho and r^(-4/3)psi near z=0. Density and stream themselves have fractional prefactors there. Both are real analytic at every point of the open exterior. Termwise differentiation and absolutely convergent multiplication establish the two equations. Topic109 then constructs a common C-infinity potential on any strictly smaller exterior domain. Its reflection symmetries and the curl identity imply zero circulation, hence a single-valued pressure.

Uniqueness requires the pure radial lattice, periodic coefficient functions, and the stated S1 odd-even stream symmetry. Within that class the Poisson equation has exactly the single sine harmonic freedom at each resonance and none elsewhere, so the formal tuning argument is exhaustive. If the statement is read as imposing symmetry only on density, it should explicitly retain the stream symmetry: arbitrary extra stream gauges are otherwise outside the specified normalization. No uniqueness of arbitrary exterior stationary solutions is claimed.

## Explicit profiles: arithmetic verification plan

For f_1=sin(theta)+b sin(3 theta), the theory part claims an irreducible degree-six numerator P6 for O6, exactly two real roots in (1/4,1/3) and (1/2,1), nonzero cubic responses for all integer k>=2 with nonzero limit, and nonzero canonical O9 in Q[b]/(P6). All these assertions are to be recomputed using Laurent coefficients and the Cartesian operators above, independently of the theory part's sine-product implementation.

At symbolic k, retain signed Laurent frequencies as affine pairs (coefficient of k, constant term). This avoids the need to infer a folding rule from sampled orders. The response is linear in the initial multipole, so its frequencies have slope +2 or -2 in k. Collisions between these branches can only occur at finitely many small k and can be checked exactly. Compare the rational function of k,b with the frozen claim, prove its numerator coefficients do not vanish simultaneously, and verify the nonzero limit. Verify irreducibility by a finite-field certificate if available, and root counts by an exact Sturm sequence. Compute O9 modulo P6 with the whole resonant stream mode zero. Numerical approximations alone establish none of these infinite-order hypotheses.

Dependencies: topic01 for the original potential formulation; topic109 for the common potential; the elementary holomorphic implicit function theorem; exact arithmetic certificates to be produced in verification. Scope: no explicit convergence radius yet, no claim about the canonical log series for unit sine, and no global extension.

## Completed exact certificate

The independent implementation in code/tuned_cartesian_exact.py completed at 2026-10-31T09:37Z in110.62026560213417seconds. It reproduces O6=P6/35818438656000000 exactly, every claimed response from k2through12, and the full symbolic response in Q(k)[b]. Its signed Laurent support certifies the all-k branch argument without sampling. The four coefficients of N(k,b) have polynomial gcd1. In fact the constant coefficient of N has strictly positive coefficients after k=t+7, providing an alternative elementary proof that N(k,.) is a nonzero cubic for every k>=7. The symbolic limit is exactly the stated nonzero cubic.

Exact factorization confirms P6 irreducible over Q. The retained Sturm sequence has two total real roots, one in each stated isolating interval. Since each root has degree6, none of the nonzero response cubics or their limit can vanish there. A sequence with nonzero limit and no zero terms has strictly positive infimum of absolute values: the tail is bounded below by half the absolute limit, and the remaining finite minimum is positive. This verifies every hypothesis of TheoremT for the two profiles.

Finally the Cartesian recurrence in Q[b]/(P6), with the whole resonant stream mode zero, reproduces the claimed canonical obstruction at order9 as a nonzero degree5 polynomial. Irreducibility implies this obstruction is nonzero at either root. Thus the canonical normalization cannot give a pure series for these profiles, while the uniquely tuned normalization does. All exact outputs and source hashes are retained under verification. A separate proposed topic120 provides a quantitative lower bound and explicit radius.

## A small finite-field certificate for the sextic

An independent irreducibility certificate can replace the exact factorization call. Reduce the primitive integer sextic modulo a prime p not dividing its leading coefficient, and make the reduction F monic. It is enough to check

    x^(p^6)=x modulo F,
    gcd(F,x^(p^3)-x)=gcd(F,x^(p^2)-x)=1.

The polynomial x^(p^6)-x is square-free and is the product of monic irreducible polynomials whose degrees divide6. The two gcd conditions exclude degrees1,2and3, leaving onlydegree6. Thus F is irreducible. A rational factorization of the primitive sextic would reduce to a nontrivial factorization of F, because the leading coefficient is nonzero modulo p; Gauss's lemma therefore proves irreducibility over Q. The certificate retains all remainders and Euclidean chains, so checking it requires only arithmetic in the finite field. The prime itself is checked by trial division through its square root. Root isolations and displayed decimal evaluations are separate rational-sign and interval computations.
