# Positive growth on a zero-work irrotational support forces periodicity

Status: CONFIRMED A471 at the exact hypotheses below after independent reconstruction, full postwrite inspection and the complete focused configured-model review. The global decay-only conjecture remains open.

## 1. Exact hypotheses and conclusion

Let 0<c<1/2, omega in R, U in C2(R3;R3),P in C1 solve the full rotating incompressible Euler profile equation. Assume uniform U=o(|y|), U.curl U=0 everywhere. Put

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c,
    alpha=B cross W, O={W!=0},
    H=P+|U|^2/2+(Ay).U, g=U.B.

Let mu be a compactly supported probability, invariant and ergodic for the whole carrier flow, with S=supp mu, and assume

    mu({B=0})=0, S subset closure(O),
    W=Dalpha=0 everywhere on S.                     (1)

The zero-work identity g=0 on S follows from the companion compact-invariance theorem A470 (LIT106), whose proof is independent of this result. No nonzero DW premise is imposed. There is a finite constant rho such that, at every point of S with U!=0,

    grad g=rho U, Hess g-rho DU=tau U tensor U.        (2)

Almost everywhere U is nonzero. If rho!=0, the backward Lyapunov spectrum, including multiplicity, is(0,-rho,rho-d). If rho=0 it is(0,0,-d). If rho!=2c then U is nonzero on all of S. In this case an aperiodic measure must have rho=d. If rho=2c the spectrum is(0,-2c,-c), whether or not U vanishes somewhere on S.

Consequently every aperiodic measure satisfying(1) has largest backward exponent zero. A measure satisfying(1) with strictly positive largest exponent must be periodic. This conclusion does not exclude the resulting periodic measure.

## 2. Full covector data without a nonflat premise

A413 gives the C1 tensor dH wedge dg=0 on O, so its values and first derivatives vanish on closure(O). The Lamb identity grad H=-aU+alpha makes H C2. At a point of S with U!=0, W=0 makes M=DU symmetric and Dalpha=0 gives Hess H=-aM. The rank identity gives grad g=rho U, with rho=(U.grad g)/|U|^2 C1 on the open set U!=0. Differentiating the rank tensor in every ambient direction gives a symmetric matrix Hess g-rho M with image in R U. This proves(2), with no smoothness of S assumed.

Since g=0 on S, BH=-ag=0 there. Thus H is invariant on S; whole-flow ergodicity and continuity give H=h on S. On any orbit interval with U!=0, differentiate grad g=rho U along B. The Hessian identity and g=U.B=0 give

    (B rho)U=0, so rho is constant on that interval.

Also differentiation of g=U.B, using symmetry of DU at W=0, gives

    grad g=DU B+(DB)^T U,
    dU(Phi_s x)/ds=rho U-(DB)^T U.                    (3)

On the interval rho is one finite constant, and DB is bounded on S. Invertibility of the fundamental matrix for this linear ODE prevents nonzero U from tending to zero at any finite endpoint. Every orbit therefore either has U nowhere zero, with constant rho, or has U identically zero. In the latter case y'=Ay, so |y(s)|=exp(cs)|y(0)|. Two-sided compactness forces y=0, a carrier equilibrium. Such points have mu mass zero by(1). It follows in particular that every zero of U in S is the spatial origin and is a zero of B.

Extend rho measurably on that null invariant set. It is flow invariant almost everywhere, so ergodicity makes it one finite constant almost everywhere. Continuity of the quotient on U!=0 and support density extend that constant to every nonzero-U support point. The pulled-back covector law from(3) is

    D Phi_s(x)^T U(Phi_s x)=exp(rho s)U(x),
    U(Psi_t x)=exp(-rho t)D Psi_t(x)^(-T)U(x),         (4)

where Psi is the backward carrier flow. All identities hold in both time directions.

## 3. The spectrum and the repeated zero case

On compact S the derivative cocycle and inverse have integrable logarithmic norms, so the two-sided multiplicative ergodic theorem applies. The flow direction has exponent zero almost everywhere. To check this without assuming log|B| integrable, the time-one increment log|B(Psi_1 x)|-log|B(x)| is bounded by the derivative bound. Birkhoff gives the limit of its averages. Boundedness of |B| makes that limit nonpositive; recurrence to some set {|B|>=1/j} makes it zero. No time-one ergodicity is needed.

Apply the dual Oseledets decomposition to(4). A nonzero component of U in the dual space corresponding to primal exponent lambda has scaled rate -rho-lambda. Tempered projection bounds allow us to recover that component from the bounded vector U(Psi_t x). A positive rate would contradict boundedness in forward time; a negative rate contradicts boundedness in backward time. Thus every nonzero component has lambda=-rho. Since U!=0 almost everywhere, -rho is a primal exponent.

When rho!=0 this exponent is distinct from the flow exponent zero. The determinant exp(-dt) gives the third exponent rho-d, with multiplicities allowed. When rho=0, suppose the zero exponent had multiplicity one. Its primal space would be the flow line. The corresponding dual space is the annihilator of the sum of the other primal spaces, and a nonzero covector in it pairs nontrivially with that flow line. But U.B=g=0, a contradiction. The zero exponent therefore has multiplicity at least two; the negative total sum makes the spectrum exactly(0,0,-d).

## 4. Excluding a support zero unless rho=2c

Suppose U vanishes on S. By Section2 it vanishes at spatial0, where B=W=0. Put M=DU(0), symmetric and trace-free. If M=0 then y.B(y)=c|y|^2+o(|y|^2), so nearby backward orbits in S converge to0. A relative ball has positive mu mass, contradicting ergodicity or recurrence because mu({B=0})=0.

If M!=0, the continuous matrix Hess g-rho DU has at zero the value

    R=2M^2+(2c-rho)M+omega[J,M], tr R=2tr M^2=:t>0.   (5)

There are nonzero support points tending to0, since an isolated support equilibrium would have positive mass. Their U is nonzero by Section2. Formula(2) makes R their rank-at-most-one limit, hence R=t v tensor v for a unit vector v.

Let x be any limiting unit direction of S at0. Taylor expansion of grad g-rho U=0 on S gives Rx=0, hence v.x=0. Dividing(2) by its trace and taking limits shows Mx is a scalar multiple s v. For z in ker M, formula(5) gives z.Rz=0, so v is perpendicular to ker M and lies in range M. The symmetric spectral pseudoinverse satisfies

    t v.Mdagger v=(2c-rho)rank M,                     (6)

because tr(Mdagger M^2)=tr M=0 and the two commutator traces cancel. Writing x=s Mdagger v+z, z in ker M, and pairing with v gives s v.Mdagger v=0. If rho!=2c, the right side of(6) is nonzero, of either sign, so s=0 and Mx=0.

Thus every support limiting direction is in ker M. A compact-unit-sphere sequence argument gives y.B(y)>=(c/2)|y|^2 on nearby S. Backward orbits starting in a sufficiently small relative ball remain there and satisfy d|Psi_t y|^2/dt<=-c|Psi_t y|^2. They converge to0, again contradicting the positive-mass support ball and ergodicity. This proves U!=0 everywhere on S if rho!=2c. At rho=2c the pseudoinverse pairing can vanish; no conclusion about a support zero is taken from this argument.

## 5. Surface dynamics and both time directions

Assume rho!=2c. Compactness now gives a positive minimum for |U| and |grad H|=a|U| on S. On a relatively compact neighborhood with grad H nonzero, take the C2 surface {H=h} and project B to

    Btilde=B-(BH)grad H/|grad H|^2.

This field is C1. On S it equals B, and since d(BH)=rho dH there, its derivative on ker dH equals DB. Uniqueness of the tangent variational equation identifies its tangent cocycle with the original one along S, even at zero-mass carrier equilibria.

From(4), the backward surface area Jacobian is

    exp((rho-d)t)|grad H(Psi_t x)|/|grad H(x)|.        (7)

The one-dimensional normal Poincare derivative has an additional factor |B(x)|/|B(Psi_t x)|. Using sections with tangent normalized by speed introduces the same factor a second time. The bounded gradient ratio and the tempered-speed argument from Section3 show that the speed-normalized normal exponent is rho-d almost everywhere.

The confirmed A465 C1 recurrent-surface lemma, reconstructed in auditor_proofs/reviews/negative_covector_surface_exclusion_20261103/PROOF.md Sections4-5, says that a regular recurrent point near a compact invariant set with negative normalized normal exponent is periodic. Its proof allows accumulation on equilibria. If rho-d<0 apply it to the backward surface flow; if rho-d>0 apply it to the forward surface flow, whose normal exponent is the negative value. The chosen point is regular since mu(B=0)=0, and is recurrent for both time-one and time-minus-one maps by Poincare recurrence. The compact invariant support has complete trajectories; no time-one ergodicity is required. Recurrence and the speed argument hold in both directions. A whole-flow-generic chosen point then identifies mu with the time measure of that periodic orbit. Hence an aperiodic measure with rho!=2c must have rho=d, giving spectrum(0,-d,0).

If rho=2c, Section3 directly gives(0,-2c,-c), with largest exponent zero, and no surface construction at a possible zero of U is needed. This proves the dichotomy using A465. If rho=2c and U is nevertheless nowhere zero on S, the same surface argument applies since2c!=d and forces periodicity. Therefore an aperiodic measure has either rho=d, or rho=2c and the spatial origin is a carrier equilibrium in S. In particular rho=0 forces periodicity.

## 6. Dependencies, scope and verification

The companion LIT106 compact-invariance proof gives g=0 from(1), with no ergodicity required. A465 supplies the C1 surface lemma. A413, the full Lamb identities, ordinary two-sided Oseledets theory on compact invariant support, and elementary linear and convex arguments are the remaining inputs. The origin proof is supplied in full rather than importing A464 with a different covector rate.

In a component core K_E, an ergodic measure with W=DW=0 has Dalpha=0 and support in closure(O), so the dichotomy applies. It leaves periodic flat measures and carrier equilibrium atoms. A449 and A462 require a nonzero first vorticity derivative and cannot be applied to those flat periodic orbits without a new argument. For a periodic flat orbit the top backward exponent is max(0,-rho,rho-d). It is at least2a exactly when rho<=-2a or rho>=d+2a=2-c. This is a necessary obstruction description, not realization or exclusion of such an orbit.

Combining this result with A433 and A467, an ergodic measure on Z_E with top exponent at least2a can only be a carrier-equilibrium atom or a flat periodic measure with that rho range. Nonflat nonstationary measures have top a/2, and aperiodic flat measures have top0. This uses the attained-maximum formulation for each fixed component in A430; it claims no uniform margin over all components. If also U tends uniformly to zero and2/5<=c<1/2, excluding both witness types would meet the componentwise C2 criterion in A432. Neither exclusion is proved here. Global helicity and sublinearity remain essential inputs, and the unrestricted decay-only conjecture is open.

Both submitted source and focused review are pinned in verification. No computation is needed. The full configured-model review checks the finite-endpoint ODE argument, the repeated zero dual exponent, the exceptional rho=2c, support versus almost-everywhere nonvanishing, and the application of A465 in both time directions. Model evidence is the existing configuration, not independent provider attestation.
