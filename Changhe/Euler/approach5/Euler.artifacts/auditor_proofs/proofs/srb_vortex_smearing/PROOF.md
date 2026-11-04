# SRB smearing, Bernoulli vortex averages and the occupation comparison

Date: 2026-11-03T01:37:05Z. CONFIRMED A374 after focused coordinator and literature-agent reviews and independent rechecking. This distinguishes the carrier-invariant measure, its vortex-time smear and ambient volume; it supplies no nonexistence theorem.

## 1. Exact Euler and measure hypotheses

Let U in C2(R3;R3), P in C1 solve the exact rotating divergence-free Euler profile equation, with U tending uniformly to zero, 2/5<=c<1/2 and arbitrary finite omega. Set

    B=(cI-omega J)y+U, Omega=curl U,
    a=1-2c, kappa=1+c, d=3c,
    H0=P0+|U|2/2+((cI-omega J)y).U,

where P0 is the fixed canonical pressure from the audited energy theorem. Let Phi be the complete B flow, Psi_t=Phi_-t, and Gamma the complete volume-preserving Omega flow. A048-A049 give its almost-everywhere recurrence, polynomial spatial bound and exact commutation

    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t.           (1)

Suppose nu is a compactly supported full-Phi-flow-invariant probability with the following properties, supplied by A308 in the C-infinity class or by the quantitative finite-r theorem A312:

* Almost every point has the backward-flow Oseledets splitting with exponents a,0,-kappa and directions E^u,span(B),span(Omega).
* Its conditional measures on full one-dimensional unstable plaques are absolutely continuous with respect to arclength.

Thus B and Omega are nonzero and independent nu-almost everywhere. At C2 this is a separately given measure hypothesis, not a coverage theorem. Ergodicity is not needed for the smearing deduction itself. Define a probability

    m_T=(1/(2T)) integral_(-T)^T (Gamma_s)_*nu ds, T>0.    (2)

The following assertions hold:

(A) m_T has compact support and is absolutely continuous with respect to Lebesgue measure, with an L1 density. Consequently nu-almost every point is recurrent in both directions for Gamma.

(B) With m=m_1 and S=exp(kappa t), every nonnegative Borel F obeys the exact identity

    integral F(H0(Phi_t y)) dm(y)
      =(1/(2S)) integral nu(dz) integral_(-S)^S
                       F(H0(Gamma_s z))ds.              (3)

The two sides are interpreted as nonnegative integrals. In particular, for every bounded continuous F with F(0)=0, the right side tends to0. This applies to F(v)=min(1,v2). If H0 is bounded globally, it applies also to H0 squared. The audited Dini hypothesis supplies that additional boundedness, but is not needed for the clipped conclusion.

(C) If the density rho=dm/dy belongs to Lq for some q>(1-c)/c, including q=infinity, then

    (1/(2S)) integral nu(dz) integral_(-S)^S
                         H0(Gamma_s z)2 ds
      <= C S^(-2a/kappa), S>=1.                         (4)

Absolute continuity alone does not supply this Lq hypothesis in the proof. No unconditional polynomial rate is being asserted.

## 2. Absolute continuity of short smearing

Disintegrate nu on measurable families of C1 full unstable plaques gamma. Their conditional measures have the form f_gamma(s)ds in arclength coordinates, with f_gamma integrable. All statements about almost every s below are with this conditional weight. Full-flow invariance allows insertion of a short average over any fixed interval -delta<r<delta:

    m_T=(1/(4T delta)) integral_(-T)^T integral_(-delta)^delta
                      (Gamma_tau Psi_r)_*nu dr d tau.    (5)

For a fixed plaque consider the C1 map of three real parameters

    F_gamma(s,r,tau)=Gamma_tau(Psi_r(gamma(s))).           (6)

At almost every weighted s, the three directions gamma'(s),B(gamma(s)),Omega(gamma(s)) are linearly independent, since gamma' is in E^u. The exact commutation law, and invariance of B under its own flow and Omega under its own flow, preserve this transversality under all bounded r,tau in(6). Equivalently, pull the three derivative columns back by D Gamma_tau, and then by D Psi_r. They become nonzero scalar multiples of gamma',-B,Omega. Thus the Jacobian of(6) is nonzero at every r,tau for each s where the original three directions are independent. The Oseledets-regular such s form a set of full conditional weight.

At every parameter with nonzero determinant the inverse function theorem provides a local C1 diffeomorphism. A countable such cover shows that a Lebesgue-null target set has null parameter preimage there. The remaining parameter set has zero f_gamma(s)ds dr d tau measure by Tonelli. Hence the pushforward in(6) is absolutely continuous. Integrating the plaque disintegration in(5) proves m_T absolutely continuous. Its density has integral1, so belongs to L1. The support lies in Gamma_[-T,T](supp nu), a compact set by continuity and completeness. This proof does not bound the density above or give any Lq exponent greater than1.

For the recurrence consequence, take the Borel set N of points which fail the full topological positive- or negative-integer recurrence conclusion of A049. It is Lebesgue null. It is invariant under every Gamma_s: a convergent return sequence for x remains a convergent sequence after applying the fixed homeomorphism Gamma_s, and the converse follows with -s. Thus m_T(N)=nu(N) by(2). Absolute continuity makes this zero. This transfers recurrence to nu without asserting that Gamma preserves nu or that nu is Gamma-ergodic.

## 3. Exact transfer and qualitative Bernoulli convergence

By(1) and invariance of nu,

    integral F(H0(Phi_t y)) dm(y)
      =(1/2) integral_(-1)^1 integral nu(dz)
                   F(H0(Phi_t Gamma_tau z))d tau
      =(1/2) integral_(-1)^1 integral nu(dz)
                   F(H0(Gamma_(tau exp(kappa t)) z))d tau.

The substitution s=tau exp(kappa t) proves(3). All exchanges for nonnegative F follow from Tonelli; for bounded signed F use its two parts.

A287 proves H0(Phi_t y)->0 as t tends to infinity through all real times for Lebesgue-almost every y. Since m is absolutely continuous, the same holds m-almost everywhere. Bounded continuous F with F(0)=0 therefore gives convergence to0 by dominated convergence. If H0 is bounded on all R3, F(v)=v2 is bounded on the values in question and the same argument applies. A295 proves the latter boundedness under the full Dini assumptions by uniform decay of H0 at infinity and continuity on compact sets.

There is no rate in dominated convergence for an arbitrary L1 density. The conclusion is an average over nu of long Gamma segments. It is not an almost-everywhere rate on individual Gamma trajectories and is not an assertion that H0 vanishes on supp nu.

## 4. The precise extra density condition for the polynomial rate

A292 proves, on every compact Q, for each 2<=p<p_star=2(1-c)/a,

    ||H0 composed Phi_t||_Lp(Q)<=C_(Q,p) exp(-at), t>=0.  (7)

Indeed A292 gives a common coefficient K in Lp(Q) and its all-future error estimate at T=0. Thus ||H0 composed Phi_t||_Lp(Q)<=exp(-at)(||K||_Lp(Q)+C_(Q,p)), proving(7). This also includes the L2 estimate A277. Let Q contain the compact support of m. If 1<q<infinity, Holder gives

    integral rho |H0 composed Phi_t|2
       <=||rho||_Lq ||H0 composed Phi_t||_(L^(2q'))2,
    q'=q/(q-1).

The strict condition 2q'<p_star is equivalent to q>(1-c)/c. Applying(7) and then(3) proves(4). For q=infinity, use p=2 directly. The endpoint q=(1-c)/c would require the unproved endpoint in A292 and is not included.

The hypotheses of Section1 provide conditional arclength absolute continuity, not a uniform conditional-density bound, uniform plaque radii or a uniform angle from the two other directions across a support that may meet zeros. Section2 accordingly gives L1 only. A separate proof of the required Lq density for these Euler SRB measures would upgrade(4) to an unconditional estimate. It is supplied under compact regular support in A375. No such regular-support hypothesis is part of the general given-measure assumptions here.

## 5. An Euler-specific averaged occupation lower bound

This section needs no SRB measure, no Bernoulli scalar and no energy estimate. Suppose only the bounded C2 profile hypotheses with 0<c<1/2, every finite omega, so A048 gives for each bounded Q

    Gamma_[-S,S]Q contained in B_(C_Q(1+S)^(c/kappa)).    (8)

Let Q be bounded measurable with 0<|Q|<infinity and S>=1. Define

    f_S(y)=integral_0^S 1_Q(Gamma_-t y)dt.

Tonelli and volume preservation give integral f_S=S|Q|. Its support lies in the ball in(8), of volume at most C S^(3c/kappa). Cauchy-Schwarz therefore gives

    integral f_S2 >= C_Q S^(2-3c/kappa).                 (9)

Expanding the square using invariance and time differences gives exactly

    integral f_S2
      =2 integral_0^S (S-t)|Q intersect Gamma_t Q|dt
      <=2S integral_0^S |Q intersect Gamma_t Q|dt.

Combining with(9),

    integral_Q integral_0^S 1_Q(Gamma_t y)dt dy
      >= b_Q S^(a/kappa), S>=1, b_Q>0.                  (10)

This is an ambient-volume average over Q. It is not a pointwise occupation lower bound, and gives no deterministic almost-everywhere normalization in the Hopf ratio theorem. A325 therefore does not refute it: that abstract tower has no spatial-growth bound(8).

## 6. Comparing the two averages without a Hopf assertion

Suppose, in addition to Section1 and the Lq premise of Section4, that m assigns positive measure to {H0!=0}. Since m has a density with compact support, there are eta,delta>0 and a bounded measurable positive-volume Q such that

    |H0|>=eta on Q, rho>=delta on Q.                    (11)

Choose these by a countable union of positive level sets. Define

    R_S(mu)=integral mu(dy) integral_(-S)^S 1_Q(Gamma_t y)dt.

By(10) and(11), R_S(m)>=C S^(a/kappa). From the exact definition m=(1/2) integral_(-1)^1 (Gamma_tau)_*nu d tau, nonnegativity and interval inclusion imply

    R_S(m)<=R_(S+1)(nu).

But(11) and(4) give R_(S+1)(nu)<=C(S+1)^(1-2a/kappa). These inequalities contradict one another only if a/kappa>1-2a/kappa, equivalently c<2/7. In the primary interval 2/5<c<1/2 they are compatible. This comparison does not apply the decaying-profile estimate(7) below its stated c range; it identifies the algebraic threshold of the proposed pair of bounds, which lies outside that range. Nonexistence below2/5 is already supplied by the energy theorem.

No individual-orbit transfer or unproved Hopf denominator rate occurs in this averaged comparison. It supports the coordinator's exponent diagnosis while separating the extra Lq premise from what has actually been derived.

## 7. Verification and limitations

The main review targets are the full-unstable-plaque smearing argument, the recurrence transfer from ambient volume to nu, and the Lq threshold in Section4. The occupation proof is elementary but its averaged scope is essential. The qualitative clipped mean uses only actual Bernoulli evolution and canonical pressure, so it is not a purely kinematic scalar identity. These facts still allow long recurrent vortex excursions with sign-changing helicity.

The arbitrary-omega property is preserved throughout. No C2 coverage, unconditional polynomial SRB-average rate, almost-everywhere occupation lower rate, vortex ergodicity, pointwise H0 vanishing or new nonexistence theorem is claimed. No computation is proposed.

The coordinator configured for the primary model and the literature agent independently reconstructed the proof. Their reviews and the original proposal are retained with hashes in verification. Provider identity is not independently attested. The exact three-parameter determinant and the bounded-density special case also agree with A370. No new numerical or formal computation was needed.
