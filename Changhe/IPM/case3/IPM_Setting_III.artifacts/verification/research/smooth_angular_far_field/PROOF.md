# Finite far-field expansions with arbitrary smooth angular coefficients

Written 2026-10-21 before supporting checks. Status: complete informal proof, 5722 exact supporting checks; actual Opus5.5 hand review at05:07 and external referee audit21 accepted, with the independently checked zero-trace wording repair applied 2026-10-21T05:38:49.917749+00:00. This is a necessary far-field structure theorem. It is not existence, nonexistence, convergence of an infinite expansion, or a numerical certificate.

## 1. Statement and exact hypotheses

Let ell>1, p=1/ell and delta=1-p. Suppose rho is smooth on the full plane, even in x and odd in y, and its canonical velocity U is defined by

    -Delta psi = rho_x,  U=(-psi_y,psi_x),  U=o(r),

with the parity-preserving stream gauge. Suppose outside a disc that

    (ell X+U).grad rho = rho,
    rho,U belong to S^p,
    r^{-p}rho(r,theta) -> Theta(theta) uniformly.          (1)

Here S^b means that every Cartesian derivative of order j is O(r^{b-j}) outside a disc. Equivalently every product of E=r partial_r and partial_theta applied to the function is O(r^b). These are equivalent assertions because a Cartesian derivative is r^{-1} times a linear combination of those conormal derivatives with smooth angular coefficients. For vector fields use either Cartesian components or polar components; multiplication by the smooth rotation matrix preserves the conormal bounds.

No finite angular support is assumed for rho, Theta or any remainder. The uniform trace and symbol bounds imply Theta is smooth: the functions r^{-p}rho(r,.) have uniformly bounded C^{j+1} norms for every j, hence are precompact in C^j. Every subsequential C^j limit must equal the unique uniform limit Theta. This proves convergence in every fixed C^j and smoothness of Theta. The same argument is valid along arbitrary sequences r tending to infinity.

Define the sets of possible radial degrees

    A = {p-k delta-2l: k,l are nonnegative integers},
    H = {-m-1: m>=2 is an even integer},
    B = A union H.                                       (2)

These sets are locally finite above each fixed lower bound. For A this follows from kdelta+2l being bounded above; for H it is immediate. Coincident numerical degrees are collected, not treated as separate terms.

Theorem. For every b<p with b outside B, there are finite expressions

    rho(r,theta) = sum_(s in A, s>b) r^s P_s(log r,theta) + E_b,
    U(r,theta) = sum_(s in B, s>b) r^s V_s(log r,theta) + F_b,       (3)

where each P_s and each polar-component V_s is a polynomial in log r with smooth periodic angular coefficients, E_b,F_b belong to S^b, and zero coefficients may be omitted. The leading density coefficient is P_p=Theta, with no log. All coefficients collected at a given degree and log power are unique. Expansions at different thresholds agree above their shared threshold. Consequently such finite expansions reach every prescribed finite algebraic depth.

If delta is irrational, every polynomial in (3) is constant in log r. The density degrees then have unique labels (k,l), and no density-induced velocity degree coincides with a degree in H. If delta=u/v is rational in lowest terms, a necessary condition for resonance of a term with a representation s=p-kdelta-2l is

    (k+1)u is divisible by 2v.                           (4)

This only lists possible resonances. Some degrees in A never occur, a resonant source projection can vanish, and no logarithm is asserted to be forced.

For exact primary profiles, the hypotheses (1) are consequences of the symbol theorem in report3.23, independently proved in ../local_ipm_continuation/PROOF.md, together with the far-field theorem. The nonzero trace theorem in ../nonzero_far_field/PROOF.md implies Theta!=0 for a nonzero primary profile, but nonvanishing is not needed for the expansion argument itself. The general canonical inverse lemma used below is proved in ../finite_far_field_cascade/PROOF.md, Section2, with its exact hypotheses and checks. The present theorem removes the finite-leading-angular-support restriction from the finite-depth expansion, not from the highest-mode nonvanishing argument: an arbitrary smooth Theta need not have a highest frequency.

## 2. Inverting one power-log expression with smooth angular coefficients

Take s<1 and a polynomial P(z,theta) in z whose angular coefficients are smooth, even in x and odd in y. The expression r^sP(log r,theta) is used only outside a disc. Its x derivative is

    r^{s-1}G(z,theta),
    G = cos(theta)(s+partial_z)P - sin(theta)partial_theta P.       (5)

The source has only positive even sine frequencies. A particular stream r^{s+1}Q(z,theta) must solve

    [A_s-2(s+1)partial_z-partial_z^2]Q=G,
    A_s=-partial_theta^2-(s+1)^2.                         (6)

Work in the smooth angular space spanned by sin(m theta), m>=2 even. On this space A_s has eigenvalues m^2-(s+1)^2. It has a kernel only when s+1=+m or -m. The positive alternative is impossible because s<1 and m>=2. The negative alternative is precisely s=-m-1 in H, with a one-dimensional kernel spanned by sin(m theta).

On the complement of this possible kernel, A_s has a well-defined inverse on smooth functions. Indeed the Fourier coefficients of a smooth function decay faster than every power of m; division by m^2-(s+1)^2 preserves that decay and improves it by two powers for sufficiently large m. The finitely many other nonzero eigenvalues cause no issue. The Fourier series and every angular derivative converge absolutely. This proves the smoothness statement directly without an assumption of finitely many angular modes.

Write G=sum_(j=0)^d g_j(theta) z^j. On the complement, set q_j=0 for j>d and solve downward by

    A_s q_j = g_j + 2(s+1)(j+1)q_(j+1)
                        +(j+2)(j+1)q_(j+2),            (7)

using the complement projections on both sides. This gives a polynomial Q of degree at most d with smooth coefficients in that complement.

At a resonance s+1=-m, the kernel equation is

    -Q_m''+2m Q_m'=G_m.                                 (8)

A polynomial solution with zero constant term is obtained by

    V_m = sum_(j=0)^d G_m^(j)/(2m)^(j+1),
    Q_m(z)=integral_0^z V_m(t)dt.                       (9)

The finite sum telescopes to 2mV_m-V_m'=G_m. Thus (8) is solved, and only this single angular mode may acquire one additional log power. Choosing Q_m(0)=0 fixes the particular/harmonic division at that resonance. No physical conclusion depends on that division.

It remains to compare this particular expression to the canonical full-plane inverse; a formal particular solution alone is insufficient. Let chi(r) be smooth and radial, zero on a disc and one outside a larger disc. Set

    f=chi(r) r^s P(log r,theta),
    psi_0=chi(r) r^{s+1}Q(log r,theta),
    h=f_x+Delta psi_0.                                  (10)

Both f and psi_0 are smooth on the plane, and h is smooth, compactly supported and odd in both x and y. Outside the cutoff annulus, (5)-(6) imply h=0. The canonical Green solution Phi of -Delta Phi=h has modes

    Phi_m(r)=(1/(2m))[r^{-m} integral_0^r t^{m+1}h_m(t)dt
                         +r^m integral_r^infinity t^{1-m}h_m(t)dt]. (11)

Here h_m=(1/pi) integral h sin(m theta). Formula (11) is valid for a general compact odd-odd source; it does not require h to be the x derivative of a separately chosen density. Smoothness at zero follows either from the angular Taylor coefficients of h in (11), or from the usual smooth Poisson potential with zero monopole. To make the latter assertion explicit, the convolution of the logarithmic fundamental solution with the compact smooth source is smooth by shifting derivatives onto h; odd-odd parity gives zero integral and fixes the parity gauge. Formula (11) is its angular solution and has no growing mode.

If supp h is contained in r<=R, then for r>R,

    Phi(r,theta)=sum_(m even>=2) beta_m r^{-m}sin(m theta),
    beta_m=(1/(2m)) integral_0^R t^{m+1}h_m(t)dt.        (12)

For every L>=0, smoothness and angular integration by parts give |h_m(t)|<=C_L m^{-L}, uniformly for 0<=t<=R. Consequently

    |beta_m| <= C_L m^{-L} R^{m+2}/[2m(m+2)].           (13)

This estimate controls all differentiated tails on r>=2R: conormal derivatives contribute only powers of m and the ratio (R/r)^m is geometric. For any noncritical b, retaining the finitely many terms with velocity degree -m-1>b leaves a velocity in S^b. For completeness, if m0 is the smallest omitted even frequency, then -m0-1<b. Factoring r^{-m0-1} from the differentiated tail leaves a uniformly bounded geometric sum on r>=2R. Thus the tail is even in S^{-m0-1}, which is contained in S^b.

Now psi=psi_0+Phi satisfies -Delta psi=f_x globally. Its velocity is o(r), because s<1, Q is a finite log polynomial, and Phi decays. Both streams have the required parities. The canonical uniqueness theorem therefore identifies psi with the actual canonical stream of f. One can also verify uniqueness directly: the difference of two smooth full-plane streams has harmonic gradient o(r); each component of that gradient is constant by the mean-value derivative bound on arbitrarily large discs, and the required velocity parities force those constants to vanish. The odd-odd stream gauge then fixes the remaining constant.

This proves that a cutoff power-log density term with arbitrary smooth angular coefficients has its induced power-log velocity plus a decaying harmonic expansion with the controlled tail (13). It also proves explicitly why one may not omit the globally determined harmonic terms. The coefficients beta_m in this cutoff decomposition are moments of h in (10), not generally convergent unrenormalized moments of the original noncompact density source.

## 3. A finite-expression inverse with an arbitrary symbol remainder

Suppose a smooth density equals a finite expression Phi_rho plus E in S^b outside a disc, with all expression degrees less than1 and b<1 outside H. Angular coefficients may have infinite support. Cut off the finitely many terms smoothly. The difference between the original density and their cutoffs is a global smooth parity-preserving density in S^b.

The general weighted inverse lemma gives for that difference a finite sum of harmonic streams beta_m r^{-m}sin(m theta), with -m-1>b, and a stream remainder in S^{b+1}. Its velocity remainder is in S^b. The retained coefficients are convergent moments of that difference's source, as required by the lemma. No finiteness of its angular support is used.

Apply Section2 separately to each cutoff term and retain its harmonic terms above b. There are finitely many terms and finitely many retained harmonic frequencies. Together they give a finite smooth-angular power-log expression for the total velocity with an S^b remainder. Induced terms have the same radial degree as their density source; harmonic velocity terms have degrees in H. This is the inverse statement needed for the nonlinear induction.

## 4. Exact radial integration and finite threshold induction

Let B_0=U.grad rho. The bounds (1) give B_0 in S^{2p-1}. Divide the exact transport equation by ell and differentiate along a ray to obtain

    partial_r(r^{-p}rho)=-(1/ell)r^{-p-1}B_0.

Because 2p-1<p, integration to infinity with the given trace is absolutely convergent and yields the exact identity

    rho=r^p Theta+T B_0,
    Tf(X)=(1/ell) integral_1^infinity t^{-p-1}f(tX)dt.    (14)

For b<p, T maps S^b to S^b. A Cartesian derivative of order j contributes t^j; together with the S^b bound of the differentiated source the integrand is bounded by C r^{b-j}t^{b-p-1}, an integrable function of t. This justifies differentiation under the integral at every order.

For a power-log term of degree s<p and any smooth angular G,

    T[r^s(log r)^d G]
      =(r^s G/ell) sum_(i=0)^d binom(d,i)i!(log r)^{d-i}/(p-s)^{i+1}. (15)

It follows by setting t=exp v and integrating v^i exp(-(p-s)v), which gives i!/(p-s)^{i+1}. Thus T preserves degree and smooth angular dependence; it does not create logarithms from logfree input.

Equation (14) first gives rho=r^pTheta+S^{2p-1}. Start at any threshold b0 strictly between 2p-1 and p that avoids B. Suppose rho has a finite expression above a threshold b<p with remainder S^b and leading term r^pTheta. Section3 gives a velocity expression with remainder S^b. Its degrees are at most p, and its degree-p coefficient, if nonzero, has no log: p is not in H, and the leading density coefficient has no log. In particular Theta=0 is allowed and the leading nonzero velocity term may instead be harmonic. Every lower term, even with logarithms, is in S^p because its degree is strictly below p. Thus each entire finite expression belongs to S^p.

The product of the two finite expressions, with one density derivative, differs from B_0=U.grad rho by an element of S^{p+b-1}=S^{b-delta}. Indeed each mixed error has that order; the product of the two remainders has order 2b-1<p+b-1 because b<p. All product degrees are below p.

Apply (14)-(15) to the finite product. The remaining error is in S^{b-delta}. Select a new threshold

    b' in (b-delta, b-delta/2)

that avoids B and all degrees in the finite expression. Terms below b' can be absorbed into S^{b'} because a strictly lower power times any fixed log polynomial has that symbol order. This produces a new density expression above b' with remainder S^{b'}. The threshold has decreased by at least delta/2. Therefore finitely many repetitions reach below every prescribed finite lower bound.

At this point the induction only needs a locally finite set containing every possible degree. Section5 proves that B has this property and is closed under the operations just used. Even without that bookkeeping, each stage has only finitely many terms and one can avoid its degrees; the set B then supplies consistent global labels. For any requested b outside B, descend first to a threshold strictly below b, and truncate to degrees above b. The strict gap of each discarded degree below b absorbs its logs into S^b. Apply Section3 once more at b to obtain the matching velocity remainder. This proves existence in (3).

## 5. Allowed degrees and uniqueness

For a density term of degree p-t, call t its degree deficit. Initially t=0. The inverse preserves the degree of its induced terms. The product of an induced velocity term of deficit t1 and a density derivative of deficit t2 has degree

    (p-t1)+(p-t2)-1 = p-(delta+t1+t2).                 (16)

A harmonic velocity term of frequency m>=2 even has degree -m-1. Acting on a density term of deficit t2 it produces degree

    (-m-1)+(p-t2-1) = p-(m+2+t2).                     (17)

The operations t1,t2 -> delta+t1+t2 and t2 -> m+2+t2 preserve the set {kdelta+2l: k,l>=0}, because m is even. T preserves degree. This proves the claimed sets A and B. Source density deficits in both (16) and (17) are strictly smaller than their output deficit; no same-order nonlinear implicit equation is hidden in the construction.

Consider two finite expressions for the same actual rho with remainder in S^b. Their difference is a finite sum of powers and log polynomials with all degrees greater than b and smooth angular coefficients. If it were nonzero, take its largest degree s and then its largest log degree d with nonzero angular coefficient G. Divide by r^s(log r)^d. Lower powers vanish uniformly as r tends to infinity, regardless of their finite log degree; smaller log powers at degree s also vanish uniformly. The scaled S^b remainder vanishes because b<s. It would follow that G=0, a contradiction. The same argument applies componentwise to the total U. This proves uniqueness above the threshold and compatibility between different depths.

At resonances a particular stream can be changed by a multiple of r^{-m}sin(m theta). Only the collected total velocity coefficients are unique; the induced/harmonic split depends on the convention in (9). Coincident numerical representations of a deficit are also collected. No convergence of an infinite sum is used or asserted in this uniqueness argument.

## 6. Irrational and rational degree arithmetic

The only log-producing step in this proof is the single-mode resonance in Section2. A density degree s=p-kdelta-2l resonates precisely when s=-m-1 for some even m>=2. Since p=1-delta, this equality is equivalent to

    (k+1)delta=m+2-2l.                                 (18)

The right side is an even integer, and the left side is positive. If delta is irrational, (18) is impossible. Starting with a logfree leading coefficient, (7), multiplication and (15) then preserve logfree expressions at every finite depth. Harmonic terms are themselves logfree. This proves the irrational assertion.

Also, if kdelta+2l=k'delta+2l' and delta is irrational, then k=k' and l=l'. Relation (18) rules out a coincidence between a density-induced degree and a harmonic degree. These are arithmetic properties of the formal degree sets; they impose no angular finiteness.

If delta=u/v in lowest positive terms, (18) implies (k+1)u=2vJ for a positive integer J. This proves (4), a condition for the inversion resonance that can first introduce logs. Once introduced, logarithms can propagate to nonresonant lower density and velocity degrees through products, transport inversion and nonresonant Poisson inversion; (4) is not a restriction on every degree carrying a logarithm. In particular the least positive k+1 satisfying this divisibility is 2v/gcd(u,2). That divisibility alone does not show that a source with such a representation is generated at that depth, that its angular projection on sin(m theta) is nonzero, or that the resulting log survives the full coupled expression. No claim of a first actual logarithm is made.

## 7. Dependencies, scope and open questions

The argument uses the actual canonical inverse, its full-plane uniqueness, the all-order symbol estimates in (1), and the exact transport equation outside a disc. It retains all harmonic terms above each threshold and all resonant logarithms. It does not impose an artificial boundary condition on a large circle or assume the original noncompact source has convergent multipole moments.

The finite-leading-trace theorem in ../finite_far_field_cascade/PROOF.md can then add a highest-frequency argument to show nonzero particular cascade coefficients. That argument is unavailable for a general smooth infinite trace. The present theorem neither forces nor excludes such traces and does not force a nonzero coefficient at every degree allowed by A.

Formal coefficients at every finite depth do not imply convergence of an infinite series, analyticity in theta or in a compact radial coordinate, control of constants as depth tends to infinity, a globally summable remainder, or an exact solution. In particular the irrational logfree property is a necessary asymptotic statement, not an existence construction or a full primary NO theorem. The primary endpoint remains open.
