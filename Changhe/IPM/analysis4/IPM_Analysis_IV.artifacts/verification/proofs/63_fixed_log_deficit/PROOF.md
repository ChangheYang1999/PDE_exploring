# Every fixed logarithmic deficit has an entire extracted series

Status: CONFIRMED after independent theory-part review at2026-10-31T05:22Z. Written on 2026-10-31. The complete canonical logarithmic expansion remains OPEN. Constants below may depend on the fixed deficit, and no bound uniform in that deficit is asserted.

## Statement

Take delta=2/3, c=3, f_1(theta)=sin(theta), and the canonical polynomial-log recursion with every resonant stream coefficient having zero constant term. Write t=log r. Its density and stream coefficients are F_n(t,theta), G_n(t,theta). Let

    lambda=157/129600.

Fix an integer d>=0. For k>=max(2,d+1), put q=k-1-d and define

    U_(k,r,d)=[t^q]F_(3k+r), r=1,2,3,
    V_(k,r,d)=[t^q]G_(3k+r), r=0,1,2.

Then, in the angular Wiener norm A_0,

    limsup_(k->infinity) (q! ||U_(k,r,d)||_0)^(1/k)
          <=(d+1)lambda,                                  (1)
    limsup_(k->infinity) (q! ||V_(k,r,d)||_0)^(1/k)
          <=(d+1)lambda.                                  (2)

For d=0 the limits equal lambda, as proved in topic44. For d>=1 these are upper bounds; equality is not asserted.

Each extracted subseries

    sum_k z^(3k+r)t^(k-1-d) U_(k,r,d),
    sum_k z^(3k+r)t^(k-1-d) V_(k,r,d)

converges absolutely for all finite complex z,t and all bounded complex angular strips. Every fixed derivative also converges locally uniformly. Thus every fixed distance below the highest allowed logarithmic degree gives an entire extracted density and stream series. These extracted parts need not separately solve the stationary equation.

The theorem does not sum the infinitely many deficits d. An interior maximum whose deficit grows with k is entirely compatible with (1)-(2). In particular this theorem would not settle convergence of the complete rational logarithmic solution.

## 1. The degree grading

The proved degree bounds are

    deg F_n<=max(0,floor((n-1)/3)-1),
    deg G_n<=max(0,floor(n/3)-1).                           (3)

For n>=4, define K_F(n)=floor((n-1)/3), K_G(n)=floor(n/3), so the allowed degrees are K_F-1 and K_G-1. A column at degree K_X-1-a has deficit a. We use this allowed degree even if an individual column vanishes.

For i,j>=4 and i+j=n,

    deg G_i+deg F_j <=deg_bound F_n-1.                     (4)

At n=3k+r, r=1,2,3, the sum of the two unshifted degree bounds is k-2 or k-3. A term using stream deficit a and density deficit b, with ell radial-log derivatives, contributes at degree k-1-d only if

    a+b+ell=d-1 or d-2.                                  (5)

There is at most one such derivative in an individual quadratic term. In particular a,b<=d-1. All interactions with both indices at least4 are therefore known from lower deficits in an induction on d.

If i<=3 or j<=3, the low coefficient is independent of t. In the block 3k+1,3k+2,3k+3, an unknown deficit-d coefficient can occur only at indices in that same block, or in G_(3k). A high child in an earlier block must have smaller deficit to reach the prescribed target degree. Radial-log derivatives also lower the deficit of the input needed to reach that degree. The only not-yet-known contributions at fixed d are consequently a linear three-step cycle.

## 2. The single unknown resonant amplitude

At n=3k the resonant stream frequency is m_k=2k-2. Define

    a_(k,d)=[sin(m_k theta)] [t^(k-1-d)]G_(3k).

For nonresonant frequencies, G_(3k) at this same log degree depends only on lower deficits. Indeed F_(3k) has allowed degree k-2, so its column at degree k-1-d has deficit d-1; higher stream columns in the triangular inversion also have smaller deficit. Thus, modulo known lower-deficit data, the block starts with exactly

    a_(k,d) sin(m_k theta).

At the target degree q=k-1-d, the unknown parts of the density recursion are obtained by dropping all partial_t terms, which only see higher log degrees. Likewise the unknown part of a nonresonant Poisson inverse is its ordinary constant multiplier. The resulting three-step linear map is exactly the top-column map in topic44, equations(6)-(8); it is independent of q.

Let R(k)=b_(k+1)/b_k be the exact rational function in topic44, valid for k>=3. The top-column map takes an input resonant amplitude b_k to a resonant Poisson forcing whose antiderivative has amplitude R(k)b_k at degree k. Replacing the input degree k-1 by q changes only the final integration divisor from k to q+1=k-d. Hence, for k>max(d,2),

    a_(k+1,d) = k R(k) a_(k,d)/(k-d) + E_(k,d),            (6)

where E_(k,d) depends only on deficits strictly below d. It may include the already determined nonresonant part of the current G_(3k), partial_t corrections, and all interactions covered by (5). There is no hidden deficit-d coefficient from another block.

For clarity, the resonant scalar Poisson equation is

    (4j partial_t-partial_t^2)B=H,  j>=1.

Its positive-degree coefficients satisfy

    B_q=H_(q-1)/(4j q)+(q+1)B_(q+1)/(4j), q>=1.           (7)

The second term is lower-deficit data. The new unknown forcing term therefore has exactly the divisor q in (7). Formula(6) follows with q=k-d at the next resonance. Canonical constants affect only finitely many initial indices at each fixed d.

Normalize the scalar by

    A_(k,d)=(k-1-d)! a_(k,d).

Equation(6) becomes

    A_(k+1,d)=k R(k) A_(k,d)+S_(k,d),
    S_(k,d)=(k-d)! E_(k,d).                               (8)

The homogeneous coefficient is independent of d, and its limit is lambda. This is the main reason for using factorial column norms.

## 3. Polynomial bounds for the finite block operators

The following estimates justify that the forcing in (8) loses at most a fixed power of k when d is fixed. All angular supports satisfy deg F_n<=2n-1 and deg G_n<=2n. Thus within a block an angular derivative or a radial exponent costs O(k).

For n=3k,3k+1,3k+2,3k+3 and a nonresonant even frequency m>=2, write P=2-2n/3. For sufficiently large k, |P|>=k. The gap |m-|P|| is at least2/3 whenever it is nonzero, so

    |m^2-P^2|>=2k/3.                                    (9)

The Poisson right side is an angular first-order operator with coefficients of size O(k), plus one partial_t term. For a nonresonant mode, descending in degree gives

    B_q=[H_q+2P(q+1)B_(q+1)+(q+1)(q+2)B_(q+2)]
                         /(m^2-P^2).                    (10)

At a fixed deficit d this uses only at most d+1 already higher columns. After multiplying each column by its factorial, (9)-(10) have coefficients bounded by a fixed polynomial in k. At resonant order, the nonresonant part of a deficit-d stream uses only lower density deficits as explained in Section2.

The stationary density inverse is similarly triangular:

    F_q=[N_q+3(q+1)F_(q+1)]/[2(n-1)].                    (11)

At fixed deficit it also uses only finitely many higher columns, with polynomially bounded coefficients. The resonant integration (7) has the same property after factorial normalization. The fixed low profiles F_1,F_2,F_3,G_1,G_2 have finite norms independent of k. The three-step block therefore consists of finitely many linear operations with polynomially bounded norms, for each fixed d.

In particular, if every known forcing column in that block, after its own factorial normalization, is O(k^M beta^k), then S_(k,d) and all reconstructed block columns apart from their scalar homogeneous contribution are O(k^(M+M_d) beta^k), for some finite M_d. This assertion involves a fixed number of columns and operators at each fixed d, not the full polynomial-log inverse with growing degree.

## 4. Induction on the deficit

The case d=0 is topic44. Suppose (1)-(2) hold for every a<d. Fix epsilon>0 and set

    beta_a=(a+1)(lambda+epsilon), 0<=a<d.

By the induction hypothesis, all lower-deficit factorial column norms have bounds C_a beta_a^K, after increasing C_a to include their finitely many initial columns. Here K=K_F or K_G for the corresponding coefficient.

Consider a quadratic interaction with both indices at least4, and lower deficits a,b satisfying (5). Write Q_i=K_G(i)-1-a, Q_j=K_F(j)-1-b. First ignore the possible single partial_t derivative. The factorial norm of the product at degree Q_i+Q_j contains

    binomial(Q_i+Q_j,Q_i) beta_a^(Q_i+1+a)
                              beta_b^(Q_j+1+b).

For a fixed block and residue pair, summing over all possible Q_i is bounded, up to a constant depending on a,b, by

    (beta_a+beta_b)^(Q_i+Q_j).

The sum Q_i+Q_j is k plus an integer bounded in terms of d. A partial_t derivative or any angular/radial factor changes this estimate by at most a polynomial in k. There are finitely many residue pairs and pairs a,b at fixed d. Since a+b<=d-1,

    beta_a+beta_b<=(d+1)(lambda+epsilon).                  (12)

The known linear terms use smaller deficits and consequently have no greater exponential rate. Section3 now yields, for some C,M depending on d and epsilon,

    |S_(k,d)|<=C k^M [(d+1)(lambda+epsilon)]^k.           (13)

Any harmless bounded shifts in K have been absorbed in C; all beta_a are strictly positive.

Let rho>(d+1)lambda. Choose epsilon so that beta=(d+1)(lambda+epsilon)<rho. Choose a number eta with lambda<eta<rho and, if necessary, enlarge the starting index so that |kR(k)|<=eta. A first-order recurrence y_(k+1)=r_k y_k+s_k with |r_k|<=eta and |s_k|<=C k^M beta^k satisfies |y_k|<=C_rho rho^k. To verify this directly, sum its variation-of-constants formula: each term is bounded by eta^(k-1-l) C l^M beta^l, and the resulting geometric convolution is O(rho^k), since both eta and beta are below rho.

Applying this to (8) proves limsup |A_(k,d)|^(1/k)<=rho. Since rho was arbitrary, the scalar limit superior is at most(d+1)lambda. The finite block reconstruction in Section3 and its lower-deficit forcing preserve this upper exponential rate, since polynomial factors do not alter a kth-root limit superior. This proves (1)-(2) and completes the induction.

## 5. Entire extracted series and its precise limitation

For fixed d and any rho>(d+1)lambda, the proved bounds give

    ||U_(k,r,d)||_0+||V_(k,r,d)||_0
          <=C rho^k/(k-1-d)!.

Their angular frequencies are O(k), so on every fixed complex angular strip an additional factor exp(C_sigma k) suffices. The factorial denominator dominates all powers of finite |z|,|t| and this exponential angular factor. The Weierstrass criterion proves entire dependence on z,t and locally uniform convergence on complex angular strips. Fixed derivatives multiply by powers of k or differentiate a fixed number of log powers, and the same factorial argument applies.

Neither C nor the onset of the estimate is uniform in d. The proof provides no majorant for the subsequent sum over d. It therefore leaves open both geometric bounds on the full coefficient polynomial and convergence of the complete stationary far-field series at rational delta2/3. The result isolates any unresolved growth mechanism to deficits that tend to infinity with the order, rather than any fixed finite collection of top diagonals.

## Dependencies and verification plan

Dependencies are the exact log recurrence and its degree bounds in topics10 and17, the Fourier support bound, and the exact top-column cycle and ratio in topic44. The new argument is the deficit-triangular structure, the scalar transfer(6), and the binomial estimate(12).

An independent exact Cartesian perturbation check of the scalar transfer for several k,d, and finite data comparisons for the first few deficits, will be retained in verification/. These checks cannot prove the induction; the complete informal proof above is the mathematical claim submitted for independent review.

## Completed scalar checks

The independent Cartesian implementation verifies23 complete linearized three-step blocks at k=3,4,5,7,10,15 and d<=min(3,k-1), without angular or log truncation. Both kR(k)/(k-d) and the normalized transfer kR(k) match exactly. Actual elapsed time was0.7016687551513314 seconds. These checks support the new scalar identity; independent review of the all-order induction remains pending.

## Review closure 2026-10-31T05:23:35Z

The theory part independently checked the deficit grading, the resonant triangular equation, the factorial normalization, the binomial forcing rate and the induction. Together with the exact Cartesian transfer checks, this closes the all-order fixed-deficit theorem: CONFIRMED, eligible for PROVED. No bound uniform over all deficits is claimed. The retained review is in sources/.
