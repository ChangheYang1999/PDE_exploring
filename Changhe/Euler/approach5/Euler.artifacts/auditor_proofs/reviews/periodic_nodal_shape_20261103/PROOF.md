# No nonconstant periodic angular shape admits the reduced incompressible helicity-free curl reconstruction

Status: CONFIRMED as A487 at the exact prescribed-metric and prescribed-vorticity scope below, 2026-11-03T05:32:48.087030+00:00. Full postwrite reading and the coordinator-supplied focused review are complete. General Euler periodic orbits are not reduced to this ansatz.

## 1. Exact theorem

Let p and beta be nonzero real numbers. Let F in C2(R/(2pi Z);R) be nonconstant. Let I be a nonempty open interval compactly contained in (0,infinity), and epsilon>0. On the flat product collar

    (R/(2pi Z)) times I times(-epsilon,epsilon),

with Euclidean product metric, orientation(theta,h,z), and coordinates(theta,h,z), set

    chi=theta+beta log h,
    w(theta,h)=h^p F(chi),
    W=(w,0,-z w_theta).

There is no C2 vector field V on this whole collar satisfying

    curl V=W, div V=0, V.W=0.                         (1)

The function F may have no zeros, finitely many zeros, or an arbitrary accumulating zero set. No analyticity or finite vanishing order is required. It suffices for V to be defined on an open neighborhood of the central annulus z=0, since shrinking I to a compact subinterval gives a uniform epsilon. The proof is local in h but uses an entire angular interval or connected chain of intervals. It is not a pointwise jet test.

For the negative-covector transport model take beta=nu/sigma, p=kappa/sigma, sigma,kappa>0 and nu!=0. The theorem excludes every nonconstant angular shape in that ansatz. A nonzero constant shape has periodic W trajectories on each z=0 circle, and fails the separate no-closed-vortex requirement of the campaign. Neither fact says that a general flat Euler orbit has this prescribed vorticity.

## 2. A necessary scalar identity using only C2 velocity

Write v=V_z for the third component of V. On an angular interval J where F does not vanish, helicity and the h component of curl V=W give

    V_theta=z(w_theta/w)v,
    partial_theta v=(w_theta/w)(v+z partial_z v).       (2)

For fixed h, the characteristic equations for the second identity have invariant I0=z w, and v/w is constant along them. Choose a fixed phase chi_j in J. Between that phase and any other interior phase, |w| is bounded away from zero on the intervening compact segment. Thus for a sufficiently small starting |z| the characteristic remains in the collar and reaches the reference. Positive or negative characteristic time may be used. Consequently

    v(theta,h,z)=w(theta,h)R_j(h,z w(theta,h))          (3)

near z=0 at every point of that phase band, with one common R_j. The permitted z width may shrink at the endpoints, which is harmless for derivatives at z=0. Explicitly,

    R_j(h,I0)=v(chi_j-beta log h,h,I0/(h^p F(chi_j)))
                     /(h^p F(chi_j)).

It is C2 near I0=0 on a smaller h interval. This also works on the whole circle if F has no zeros: v and w are periodic, and their characteristic relation gives one common R_j. A global scalar potential and its possible angular period are unnecessary.

Set k_j(h)=R_j(h,0), ell_j(h)=partial_I0^2 R_j(h,0). Then k_j is C2, ell_j continuous, and

    V_z(theta,h,0)=k_j(h)w(theta,h),
    partial_z^2 V_z(theta,h,0)=ell_j(h)w(theta,h)^3.

The identity curl curl V=grad div V-Delta V is pointwise valid for C2 V. Since the third component of curl W is -w_h, it gives Delta V_z=w_h. The preceding identities therefore imply

    (k_j w)_hh+(k_j w)_thetatheta+ell_j w^3=w_h.       (4)

Only second derivatives of V and w are used. In particular (2) is not differentiated twice in z, which would require an unavailable third derivative of V.

## 3. Matching k across simple zeros and choosing the integration domain

Let Z0={chi:F(chi)=F'(chi)=0}. If Z0 is nonempty, choose a component D of its complement containing a point where F!=0. It is an open angular arc, possibly with the same endpoint on the circle; at each endpoint F=F'=0. If Z0 is empty, take D to be the whole circle.

Every zero of F inside D is simple. Such zeros are isolated and cannot accumulate in a compact subset of D: an accumulating sequence of zeros would give F=F'=0 at its limit. There may be infinitely many accumulating at arc endpoints. Across a simple zero chi0, continuity of partial_theta V_z and the identity V_z=k_j w give

    k_left(h) h^p F'(chi0)=k_right(h) h^p F'(chi0).

The nonzero derivative makes the adjacent k functions equal for every h. Any two interior points of D are joined by a compact angular subarc with only finitely many zeros. Hence one C2 function k(h) works on every nodal interval in D. It is not matched across a degenerate endpoint outside D. The ell_j need not be equal.

The function F is nonconstant on D. For a proper arc this follows from its zero endpoint values and a nonzero interior value. On the whole circle it is an assumption. Therefore

    integral_D (F')^2>0.                              (5)

## 4. Integration over the angular domain fixes k

Divide (4) by h^p and expand. On each nodal interval j in D,

    A F''+B F'+C F+E_j F^3=0,                        (6)

where derivatives of F are in chi and

    A=k(1+beta^2/h^2),
    B=2beta k'/h+beta(2p-1)k/h^2-beta/h,
    C=k''+2p k'/h+p(p-1)k/h^2-p/h,
    E_j=ell_j h^(2p).

Multiply (6) by F' and integrate over D. The A and C terms are derivatives of A(F')^2/2 and C F^2/2. Their total boundary contributions vanish, either by periodicity or because F=F'=0 at the arc endpoints. Each E_j term integrates to zero on its nodal interval, since E_j F^3 F' is the derivative of E_j F^4/4 and F vanishes at both endpoints. If F has no zeros, there is one such coefficient and periodicity gives the same cancellation.

There is no hidden bound on ell_j in an infinite family of intervals. For each fixed h, equation (6) gives

    E_j F^3 F'=-(A F''+B F'+C F)F'.                    (7)

The right side is bounded and integrable on D because F is C2 on the compact circle and A,B,C are finite. Thus the left side is absolutely integrable across the union of intervals even if the ell_j are unbounded. Countable additivity permits summing their zero integrals. Internal zeros are simple and have measure zero. This supplies a direct alternative to the finite-exhaustion argument in LIT113.

It follows from (5) that B=0 for every h. Put q=2p-1. Since beta!=0,

    2k'+q k/h=1.                                     (8)

In particular k cannot vanish identically on an open interval. Restrict to a nonempty subinterval I1 where k!=0. Differentiating (8) gives k'=1/2-qk/(2h) and k''=-q k'/(2h)+qk/(2h^2). Substitution in C yields

    C=-q/(4h)-k/(4h^2),
    C/A=-(q h+k)/(4k(h^2+beta^2)).                    (9)

These are identities on I1, with no limit at h=0 or infinity.

## 5. The remaining angular equation is incompatible with p!=0

There is a nonzero phase interval on which F^2 is nonconstant. With zeros this follows from a nodal interval's zero endpoint; without zeros it follows from continuity, fixed sign and nonconstancy on the circle. On this interval F and F^3 are linearly independent. Dividing (6) by A and using B=0 gives

    F''+(C/A)(h)F+(E_j/A)(h)F^3=0.                   (10)

Subtract at any two h values. Independence forces C/A to be one real constant L on I1. Thus (9) gives

    [1+4L(h^2+beta^2)]k=-q h.                         (11)

If q=0, k!=0 would force the bracket to vanish throughout an interval, which is impossible. If q!=0, the bracket never vanishes there. Set t=4L and s=1+t beta^2. Then

    k=-q h/(s+t h^2).

Substitute into (8) and multiply by the nonzero squared denominator. Direct expansion gives

    t^2 h^4+[2s t-q t(2-q)]h^2+s^2+q(q+2)s=0.        (12)

A polynomial vanishing on an open interval has all coefficients zero. The coefficient of h^4 forces t=0 and then s=1. The constant coefficient becomes (q+1)^2=4p^2, contradicting p!=0. This proves the theorem.

## 6. Local degenerate barriers and pure harmonics

Two local statements from LIT112 also follow from (6). In both, V is assumed C2 on an open neighborhood of z=0 over a one-sided phase band and a nonempty open h interval. Suppose a C2 phase shape on a one-sided interval has F(0)=F'(0)=0 and F!=0 immediately on that side. For a fixed h with k(h)!=0, (6) is a second-order autonomous polynomial ODE for F with zero initial data. Local Lipschitz uniqueness, proved by the elementary integral Gronwall estimate for (F,F'), forces F=0, a contradiction. Thus k is identically zero. Equation (6) reduces to

    beta F'+p F=ell(h)h^(2p+1)F^3.

If beta!=0, first-order uniqueness at F(0)=0 gives the same contradiction. If beta=0 but p!=0, a fixed h with ell(h)=0 would force F=0 immediately; otherwise F^2 would be a nonzero constant on the nonzero interval and could not tend to zero. Hence every such degenerate barrier, including an infinitely flat one, is impossible whenever (p,beta)!=(0,0). If both vanish, V=(0,-z F(theta),0) is a C2 reconstruction, so this exception is necessary.

For F=A0 sin(m chi+chi0), A0*m!=0, on any nonzero open phase interval, F', F and F^3 are independent and F''=-m^2 F. Equation (6) therefore forces B=0, E_j=0 and C/A=m^2 on a subinterval where k!=0. The same polynomial (12) then has leading coefficient16m^4!=0. Thus for beta!=0 no such harmonic reconstruction exists even locally away from its zeros, for any real p. No full angular circle is needed for this separate assertion.

## 7. Reduced-model interpretation and limits

For beta=nu/sigma and p=kappa/sigma, the identity

    nu w_theta-sigma h w_h=-kappa w

is exact. The theorem excludes every nonconstant C2 periodic angular shape in this fixed ansatz. If F is a nonzero constant, the prescribed W flow on z=0 has h fixed and theta'=h^p F, so every trajectory is a nonconstant periodic vortex orbit. Such a field fails the separate closed-vortex obstruction A014 if it arises from a global C2 Euler profile with uniformly sublinear velocity and 0<c<1/2. The local reconstruction theorem here does not assume those global hypotheses. Constant shapes can satisfy the three local curl conditions alone: take V=(0,0,G(h)) with G'=h^p F. This illustrates why nonconstancy is an explicit hypothesis in the theorem.

This result does not handle nonlinear z dependence, a nonproduct metric in adapted coordinates, or additional vorticity components. It does not impose or derive the actual profile relation B=Ay+U. Passing from the flat-orbit geometry of A474 to the prescribed ansatz is an open step. No high-growth witness of A471 has been excluded in general.

## 8. Dependencies and review record

The initial auditor proof, preserved in verification, treated C3 shapes with a zero and p>0 using a finite-power contradiction. Full reading of LIT112-LIT113 supplied the direct C2 velocity reduction and the elementary polynomial argument for all nonzero p. The present proof retains a separate directly justified integration across arbitrary nodal sets and also covers nonvanishing nonconstant shapes. LIT113's finite-sum exhaustion provides an independent proof of that step.

No computation is needed or used. Critical review points are the common characteristic reference, the matching of partial_theta V_z at simple zeros, absolute integrability in (7), independence of F and F^3, and the signs of (9)-(12). The focused coordinator response and the literature-agent findings have been read in full and independently checked. No global Euler nonexistence claim is made.

## Final audit record

A487, 2026-11-03T05:32:48.087030+00:00: all displayed mathematical arguments were independently reconstructed and the edited proof was read in full. The coordinator-supplied 212-line review was read in full and its findings independently checked. The coordinator is configured for the primary model; the review identifies a coordinator subagent without independent runtime model attestation. No new model client or remote computation was used. Earlier snapshots and metadata remain in verification; the current reconstruction record states the exact current scope.
