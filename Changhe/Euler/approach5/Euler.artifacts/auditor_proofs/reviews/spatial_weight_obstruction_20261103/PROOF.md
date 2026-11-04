# Spatial weights: what the pointwise-density obstruction proves

## 1. Scope and exact identity

Let 0<c<2/3, omega be real, A=cI-omega J, and U in C2(R3;R3), P in C1(R3) solve (1-c)U+DU(Ay+U)+omega JU+grad P=0 and div U=0. Here Jx=e3 cross x, and Hb means U is bounded and U(R.) tends to zero in distributions. T(c) is the scalar threshold defined by the first barrier tau=T(c)^2 of h prime=(3/(2t))(1-sqrt(1-t/3-2ch)), h(0)=0. Write V0=||U||_infinity, W=curl U, t=|W|^2 and S=sym DU. Let a>0 be constant and let g(t,y)>=0 be C1 on the range under consideration. Derivatives g_t and grad_y g distinguish its two arguments. Define

    Pi=W tensor W-(t/3)I,
    H[g,a]=2t g_t-3cg-at/2-(2/(3a))t^2 g_t^2.

The chain rule in the scalar curl equation, combined with the compact kinematic identity, gives

    integral phi_R D=a E_R-F_R,
    D=a|S-(g_t/a)Pi|^2+H[g(.,y),a](t)-(Ay+U).grad_y g,
    F_R=-integral g(t,y)(Ay+U).grad phi_R>=0

for sufficiently large radial cutoffs. The sign uses g>=0 and bounded U. No sign of H is assumed.

The obstruction below concerns a proof that requires this D to be nonnegative for every trace-free symmetric S, every W in the asserted pointwise range and every value u with |u|<=V0. This is an algebraic sufficient-test class. It is not a necessary condition imposed by Euler on the jets of an actual profile. The integral C60 argument already goes beyond this pointwise test.

## 2. The core obstruction is valid with that quantifier

Fix a point y with |Ay|<V0; this core is nonempty only when V0>0. Put z=grad_y g(t,y). Minimizing over the specified algebraic values gives exactly

    min_(S,|u|<=V0) D=H-Ay.z-V0|z|
                       <=H+(|Ay|-V0)|z|<=H.

Therefore universal nonnegativity of D forces H[g(.,y),a](t)>=0 on the full asserted t interval. At t=0 this gives -3cg(0,y)>=0. Since g>=0, g(0,y)=0. The repaired scalar first-contact theorem A1727/A1894 now implies that the asserted bound M(y) must satisfy M(y)<=T(c). It does not require a separate monotonicity hypothesis on g_t.

If M(y)>T(c), H is strictly negative at some positive t. Set S=(g_t/a)Pi and choose u aligned with z. This gives a negative density. One may use |u|=v with |Ay|<v<V0, rather than an attained global maximum |u|=V0, so the same strict countertest uses an interior velocity value. If z=0 the choice of u is irrelevant. These are algebraic countervalues, not constructed Euler profiles.

Since ||A||=sqrt(c^2+omega^2), the core contains the ball of radius V0/sqrt(c^2+omega^2). The statement that it is a neighborhood of zero needs V0>0; if V0=0, U is already zero.

## 3. Product weights: a false intermediate inference and its repair

Suppose, on the exterior, g(t,y)=psi(r)G(t), r=|y|, with psi>=0 C1 and eventually monotone, and G>=0 C1 on [0,M^2], for a fixed M>T(c). The source infers integral|psi'|<infinity solely from these assumptions. This inference is false: psi(r)=r is nonnegative and increasing but has infinite variation and r|psi'|=r. Its universal derivative-subsequence assertion is false at this stated scope.

The intended obstruction can nevertheless be proved by splitting two cases. If psi is bounded on the exterior, it has a finite limit psi_inf and finite total variation. There is a sequence r_j tending to infinity with r_j|psi'(r_j)| tending to zero: otherwise |psi'|>=epsilon/r eventually, contradicting finite variation. On these spheres the spatial contribution is bounded by

    (cr_j+V0)|psi'(r_j)|G(t),

which tends to zero uniformly in angle for each fixed t. If psi_inf=0, H[psi G,a](t) tends to -at/2<0 for every fixed t>0. If psi_inf>0 and G(0)>0, the limiting H is negative at zero and hence at some small positive t. If psi_inf>0 and G(0)=0, apply A1727/A1894 to psi_inf G and M>T(c): its H is strictly negative at some fixed positive t. In every case continuity and the vanishing spatial term give a negative minimized density on sufficiently large selected spheres. Strict negativity suffices; no unproved continuity of an optimal threshold in a small defect is needed.

If psi is unbounded and eventually monotone, it is eventually nondecreasing with psi tending to infinity. For r>V0/c, the product-weight transport term is

    -(cr+u.radial)psi'(r)G(t)<=0

for all |u|<=V0. At any fixed t>0,

    H[psi G,a](t)
      =psi(2tG'-3cG)-at/2-(2/(3a))psi^2 t^2(G')^2.

If G'(t) is nonzero, its negative quadratic term makes H tend to minus infinity. If G'(t)=0, H<=-at/2 because G>=0. Thus this case also fails universal pointwise nonnegativity on a fixed interval reaching M>T(c). The same argument actually excludes many smaller fixed intervals for such an unbounded weight.

This repairs the product-weight obstruction, including unbounded monotone weights, but not the source's false assertion that every such weight has a vanishing radial derivative along a sequence. No theorem for arbitrary nonproduct weights at infinity follows.

## 4. Variable kinematic coefficients and the additive core defect

For a C2 spatial coefficient a(y), the exact identity is

    integral a phi_R(|S|^2-t/2)
       =integral U_i U_j partial_i partial_j(a phi_R).

If a is constant outside a fixed compact set, the limit of the right side is integral U_i U_j partial_i partial_j a. The cutoff remainder tends to zero by the Hb energy bound beta<2. This fixed integral has no sign supplied by the displayed hypotheses. Thus it cannot simply be discarded in the proof. This verifies the claimed boundary bookkeeping, not a theorem that no choice of a can help.

For a_rho(y)=a0(y/rho), it is false without an additional premise that a_rho is constant on B_rho. For example a0(z)=1+|z|^2/(1+|z|^2) is smooth, positive and nonconstant on every ball. Nor does a choice of a_rho force g to be spatially constant. The source's final reduction to the constant core is valid only for a specified scheme in which a0 is constant on B1 and the chosen transport weight is also spatially constant on B_rho. In that restricted scheme grad_y g=0 on B_rho, so the minimized density there is exactly H, even outside the fixed core of Section2. The same scalar first-contact test therefore applies on every B_rho, recovering a global vorticity bound as rho tends to infinity.

Separately, the confirmed integral theorem A1891 gives integral|W|^4<=CX X with X the superthreshold scalar defect. A small far-field limsup can make X finite, but does not make it zero or absorbable. The missing inequality X<integral|W|^4/CX is exactly what would be needed for a contradiction. No such inequality is proved here. The fixed-fraction consequence uses a one-sided comparison of H_- with |W|^4; it is not a second identity that removes X.

## 5. Verdict and limits

The core pointwise minimum and its threshold consequence are confirmed only with the explicit universal algebraic-test quantifier. The assertion about finite variation of arbitrary monotone nonnegative psi is refuted; Section3 gives a complete repair of the intended product-weight obstruction. The automatic plateau claim for a0(y/rho) and g is refuted; its restricted plateau version is confirmed. The additive defect bookkeeping is confirmed. Arbitrary spatial weights, variable coefficients without a plateau and removal of the global bound by other Euler identities remain open.

These results do not exclude an actual profile whose jets fail the sufficient universal test, and they do not contradict C60's positive margin. No numerical computation, formal build, new model client or agent was used. The audit is returned to existing configured model collaborators through working files; actual provider runtime is not independently attested.
