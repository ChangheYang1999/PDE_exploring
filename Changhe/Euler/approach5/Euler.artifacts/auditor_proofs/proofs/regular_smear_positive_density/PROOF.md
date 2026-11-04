# Positive local vortex-smear density and averaged basin occupation

Auditor verdict: CONFIRMED (A388), 2026-11-03T01:52:02Z. The complete argument below has been independently checked at its exact written scope.

## 1. Exact hypotheses and conclusions

Let B be a complete C2 vector field and W a complete C1 vector field on R3. Assume

    div B=d>0, div W=0, [B,W]=-kappa W, kappa>d.

Let Phi be the B flow, Psi_t=Phi_(-t), and Gamma be the W flow. Put a=kappa-d>0. Let nu be a probability invariant under every Phi_t, with compact support K. Assume B and W are independent at every point of K.

The additional full-plaque hypotheses are as follows. K has a finite cover by central portions of full C1 curve boxes, with parametrizations gamma_xi(s) contained in K, where s ranges over a fixed bounded open interval in each box. The transverse parameter xi ranges over a metric space; the curves depend continuously in C1 on xi. After shrinking to the chosen boxes, curve speeds and their tangent moduli are uniform, and

    |det(gamma_xi'(s), B(gamma_xi(s)), W(gamma_xi(s)))| >= b>0.

Restrictions of nu to these full boxes disintegrate as

    integral (gamma_xi)_*(f_xi(s) ds) d eta(xi),

where eta is finite and the conditional densities satisfy 0<ell<=f_xi(s)<=L<infinity almost everywhere, uniformly in each of the finitely many boxes. These restricted measures are bounded above by nu and their finite sum dominates nu. Every p in K has a representation gamma_(xi0)(s0) in the interior central portion of such a box with xi0 in supp eta. All asserted bounds hold on a slightly larger parameter interval than the central portions, so that no endpoint is used. This is an explicit uniform full-plaque premise, not a conclusion from mere absolute continuity of arbitrary short measurable partition atoms.

For delta>0 define

    m_delta=(1/(2delta)) integral_(-delta)^delta (Gamma_tau)_*nu d tau.

Then, for every fixed delta>0, m_delta has a compactly supported bounded density rho_delta. There is an open neighborhood N_delta of K and constants 0<c_delta<=C_delta<infinity such that

    c_delta<=rho_delta<=C_delta almost everywhere on N_delta,
    0<=rho_delta<=C_delta almost everywhere on R3.            (1)

Also N_delta is contained in Gamma_[-delta,delta]K. Consequently K is an attracting set for Psi, with a relatively compact trapping neighborhood. If nu is ergodic for the full flow, K is transitive as well.

Let V={y:dist(Psi_t y,K)->0 as t->infinity} be this full open basin. For every nonzero nonnegative F in L1(R3) with compact support contained in V, there is S_F such that, for S>=S_F,

    2 c_delta delta^(d/kappa) ||F||_1 S^(a/kappa)
      <= integral nu(dz) integral_(-S)^S F(Gamma_tau z) d tau
      <= 2 C_delta delta^(d/kappa) ||F||_1 S^(a/kappa).       (2)

Thus the compact occupation exponent is exact after averaging the starting point against nu. This is not a pointwise return-time statement, and no vortex ergodicity is assumed.

## 2. Insert carrier time exactly

Full-flow invariance of nu gives, for every r0>0,

    m_delta=(1/(4delta r0)) integral_(-delta)^delta
                  integral_(-r0)^r0 (Gamma_tau Psi_r)_*nu dr d tau. (3)

This is equality of measures, not a comparison with an arbitrary thickening. For a plaque write

    F_xi(s,r,tau)=Gamma_tau Psi_r gamma_xi(s).

Its Jacobian has the exact magnitude

    |det D F_xi|=exp(a r)
       |det(gamma_xi'(s),B(gamma_xi(s)),W(gamma_xi(s)))|.     (4)

Indeed det D Gamma_tau=1 and det D Psi_r=exp(-dr). Pulling the three columns back by these differentials reduces them to gamma_xi', -B and exp(kappa r)W. Formula(4) follows. The bracket identity also gives the exact commutation

    Psi_t Gamma_tau=Gamma_(tau exp(-kappa t)) Psi_t.         (5)

All short parameter images of the finite boxes stay in a compact set. The uniform C1 plaque bounds, compact flow derivatives and determinant bound give a uniform upper derivative bound, uniform lower singular-value bound and uniform continuity of D F_xi on fixed small parameter windows.

## 3. Upper density and positive density near every support point

For the upper bound, subdivide a fixed bounded parameter box into a uniformly bounded number of sufficiently small convex subboxes. On each, D F_xi varies by less than half its uniform smallest singular value. Integrating the derivative along line segments then proves that F_xi is injective there with a uniform inverse Lipschitz bound. The area formula, (4), and f_xi<=L bound its pushed-forward parameter density by a common constant. Integrate eta, sum the finitely many subboxes and full boxes, and use the domination of nu by the full-box restrictions. Equation(3) gives rho_delta<=C_delta globally for a short delta. A longer fixed vortex window is covered by finitely many translates of a short one; Gamma preserves volume, so the same reasoning gives a finite bound for every fixed delta. Compact support follows from supp m_delta contained in Gamma_[-delta,delta]K.

Now fix p in K and its interior central representation gamma_(xi0)(s0). Choose parameter coordinates centered at (s0,0,0), contained strictly inside the s, r and tau windows. The derivative M=D F_(xi0)(s0,0,0) is invertible. Choose a closed parameter ball of small radius r within these windows so that

    ||M^(-1)(D F_(xi0)-M)||<1/4

there. C1 continuity of the plaques supplies a transverse neighborhood E of xi0 on which the same bound holds with1/2, and F_xi at the parameter center lies uniformly close to p. Since xi0 belongs to supp eta, eta(E)>0.

For clarity, the resulting common-image assertion follows directly by a contraction argument. For y sufficiently close to p, solve

    v=M^(-1)(y-F_xi(0))
        -M^(-1)(F_xi(v)-F_xi(0)-Mv).

The right side maps the closed radius-r parameter ball into itself when y-p and F_xi(0)-p are sufficiently small, and has Lipschitz constant at most1/2. It therefore has a unique fixed point in the ball. After one uniform shrinking of E and of the target ball B(p,epsilon), every F_xi with xi in E maps the chosen parameter neighborhood onto a set containing B(p,epsilon). Its Jacobian is bounded above there by a common finite constant J0.

On this parameter ball the density f_xi(s) ds dr d tau is bounded below by ell times three-dimensional parameter volume. The change-of-variables formula gives, for every Borel A contained in B(p,epsilon),

    (F_xi)_*(f_xi ds dr d tau)(A)>=ell |A|/J0.

Integrating xi in E and multiplying the factor in(3) yields

    m_delta(A)>=ell eta(E) |A|/(4delta r0 J0).

This restricted-box contribution is a lower bound because its original measure is at most nu. In addition, every F_xi image point lies in Gamma_[-delta,delta]K: the whole plaque lies in K and Psi_r K=K. Thus B(p,epsilon) is contained in that smear set.

A finite collection of such balls covers compact K. Their union is N_delta; the minimum of their positive density lower bounds is c_delta. Together with the global upper bound this proves(1). Density statements and the lower inequalities are understood up to Lebesgue-null sets. For a prescribed longer delta, the same short-parameter argument is used directly inside its averaging window, so the lower bound still holds with a changed constant.

## 4. Local attraction follows from the same geometry

On the compact set Gamma_[-delta,delta]K, W is bounded. Equation(5) and invariance of K show that for every y=Gamma_tau z with z in K and |tau|<=delta,

    dist(Psi_t y,K)<=M delta exp(-kappa t), t>=0,           (6)

with M independent of y and t. The bound follows by integrating W over the short vortex arc based at Psi_t z in K.

Choose a bounded open Q with K contained in Q, closure Q contained in N_delta. Let eta0=dist(K,R3 minus Q)>0. By(6), for a sufficiently large T,

    Psi_T(closure Q) is contained in Q,
    intersection_(n>=0) Psi_(nT)(closure Q)=K.              (7)

The inclusions give nested compact sets; (6) puts their intersection in K, while full invariance of K gives the reverse inclusion.

For a full-flow trapping neighborhood set

    U=union_(0<=s<=T) Psi_s Q.

U is open and relatively compact, Psi_t U is contained in U for every t>=0, and Psi_T(closure U) is contained in U. Writing t+s=nT+r, 0<=r<T, verifies positive invariance from(7). Also closure U is contained in the compact union of Psi_s(closure Q),0<=s<=T. Equation(6) on this union proves that its maximal invariant set is exactly K. Thus K is an attracting set.

If nu is ergodic for the full flow, a common generic point for a countable dense family of continuous test functions has forward orbit dense in supp nu=K. Equivalently every relative open set of positive nu measure is visited. Thus K is transitive. Neither conclusion asserts that an arbitrary nonregular SRB support is an attractor.

## 5. Exact averaged occupation throughout the basin

Commutation and invariance give the exact covariance

    m_S=(Phi_t)_*m_delta, S=delta exp(kappa t).

Since det D Phi_t=exp(dt), its densities obey

    rho_S(y)=exp(-dt) rho_delta(Psi_t y) almost everywhere.  (8)

Every compact C contained in V eventually lies in N_delta under all sufficiently large Psi times, uniformly over C. To justify uniformity, each point enters the trapping neighborhood U; a finite cover of C by open preimages of U bounds the entry times. Estimate(6) then gives uniform attraction after entry. The finitely many intermediate times remain in compact images of C and U.

Apply this to a compact support C of F. For all sufficiently large t, (1) and(8) give

    c_delta exp(-dt) ||F||_1
       <= integral F dm_S
       <= C_delta exp(-dt) ||F||_1.

The upper inequality holds for every t; the lower one uses eventual entry in N_delta. Multiply by2S and use exp(-dt)=(delta/S)^(d/kappa). This proves(2).

## 6. Euler application and the exponent comparison

For Euler, d=3c, kappa=1+c and a=1-2c. The regular-support proposal of the auditor starts with K avoiding B=0 and W=0. A056 supplies uniform hyperbolicity, and A207 identifies positive unstable conditionals with alpha-length, alpha=(B cross W).dy. Its proposed recurrence-and-expansion argument supplies full uniform unstable plaques in K; finite boxes then give precisely the geometric hypotheses here. That full-plaque derivation is now independently confirmed as A375. This theorem is conditional on it and does not extend the general A308 support beyond its established scope.

Under these hypotheses, any compact set Q of positive volume with closure contained in V has averaged occupation comparable to S^(a/kappa). If a continuous scalar H is nonzero at some point of V, choose such a compact Q on which integral_Q H2>0. Formula(2) yields a lower bound of order S^(-d/kappa) for the nu-average of the vortex mean of H2 1_Q.

The separately proposed Euler Bernoulli upper bound is of order S^(-2a/kappa). Comparison of these two exponents would force vanishing only if 2a>d, equivalently c<2/7. In the primary range2/5<c<1/2 one has 2a<d, so the bounds are compatible. This is an exponent comparison, not a new theorem in c<2/7, where the hypotheses of any imported Euler bound would have to be checked separately.

No lower bound along almost every individual vortex orbit follows from(2). It concerns the nu-average of a nonnegative occupation integral. No Hopf denominator normalization, uniform orbit-frequency estimate, canonical pressure sign or Liouville conclusion is claimed.

Dependencies: exact bracket-flow covariance, full-flow invariance, the explicit full-plaque measure hypotheses, elementary inverse/change-of-variables and contraction arguments. The regular-support Euler derivation is separate. No external coefficient data or formal sources are used.


## Independent audit checks

The lower bound integrates a positive transverse-measure neighborhood of an actual support parameter, not a single plaque of possibly zero transverse mass. The uniform inverse function argument provides one common three-dimensional ball for all those plaques. For the upper bound, uniform continuity of the parameter derivative and a lower singular-value bound give finitely many injective subboxes; ordinary C1 regularity of W is sufficient. The image ball is contained in the compact smear set as an actual set, which supplies attraction before any basin-uniformity claim. In the trapping proof, the inclusion Psi_T(closure Q) inside Q implies Psi_T(closure U) inside U for U=union_[0,T] Psi_s Q, and the common contraction estimate identifies its maximal invariant set as K. Compact subsets of its open basin eventually enter this neighborhood uniformly by a finite-cover argument. The occupation constants follow from 2S exp(-dt)=2 delta^(d/kappa)S^((kappa-d)/kappa). The Euler premises are now available from A375 for an actual compact support avoiding both zero sets. This does not cover all A308 supports. The comparison c<2/7 remains only a conditional exponent comparison.

The adjacent verification manifest identifies the exact full input read. This record makes no numerical or formal verification claim.
