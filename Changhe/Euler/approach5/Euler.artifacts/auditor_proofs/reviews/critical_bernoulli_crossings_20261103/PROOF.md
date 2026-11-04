# Critical Bernoulli points and regular predecessor sets

Status: independent audit of B54, with the scope repairs in Section 12. The identities, the nondegenerate local crossing theorem and the conditional regular predecessor classification are proved. Degenerate contacts, global sign control and collapse of a predecessor set to one point remain open.

## 1. Statement and exact assumptions

Fix 0<c<1/2 and any finite real omega. Put Jx=(-x2,x1,0), A=cI-omega J, a=1-2c>0, kappa=1+c. Let U in C2(R3;R3) and P in C1(R3) solve

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U(x)=o(|x|) uniformly, U.curl U=0 everywhere.

Set B=Ax+U, Omega=curl U, H=P+|U|^2/2+(Ax).U, g=U.B, h=grad H, Vort={Omega!=0}, Reg={h!=0}, C=Vort intersect {h=0}. Momentum gives grad P in C1, hence P,H,g in C2. No third derivative of H is assumed.

The following conclusions hold.

1. C is invariant under the complete vortex flow. Along the carrier flow,

       h'=-DB^T h-a grad g.

   Every point of C has U!=0, and B and Omega are linearly independent there.
2. At x in C with v=grad g(x)!=0,

       Bg(x)!=0, D2H(x)=-(a/Bg(x)) v tensor v.

   Near x, H=F0(g) for a C2 scalar F0 with F0'(0)=0 and F0''(0)=-a/Bg(x). The critical set is the C2 surface {g=0}, transverse to B and tangent to Omega. Its carrier crossing is simple and changes the sign of g. If l=(grad g.h)/|h|^2 on Reg, then (t-t0)l(Phi_t x)->-1/a at the crossing time t0.
3. At x in C with dg(x)=0, D2H(x)=lambda U(x) tensor U(x) and D2H(x)B(x)=0 for some real lambda. Thus every critical Hessian on Vort has rank at most one. This statement does not classify the degenerate contacts.
4. C is two-sided carrier invariant if and only if each vortical carrier orbit has g identically zero or g nowhere zero. A local exact Euler example in Section 6 realizes a nondegenerate crossing. It is singular on its axis, and is not a global counterexample to carrier invariance or sign control.

For the predecessor conclusions, additionally let p be a vortical hyperbolic carrier equilibrium with one-dimensional stable manifold. Let gamma(t), t in R, be a nonconstant stable branch, tending to p as t->+infinity. Suppose g(gamma(t))!=0 for all sufficiently large t, as established for the B53 witness. Write K=alpha(gamma). Assume

    (R) h(x)!=0 for every x in K.

Then K is compact, invariant and irrotational, min_K |U|>0, and for one constant r>=0,

    Phi_t^*dH=e^(rt)dH, Phi_t^*U^flat=e^(rt)U^flat on K.

Every nonstationary ergodic invariant probability on K has full Lyapunov spectrum {0,r,3c-r}, with multiplicities. At each equilibrium of K, DB^T U=rU and the two eigenvalues on ker dH sum to 3c-r. At least one equilibrium of K has real level eigenvalues

    lambda_u>=kappa, lambda_s<=-a-r<0.

If 0<r<3c, K contains no periodic orbit. There is no conclusion that K is a single point. These classification conclusions only require (R), not a one-sign assumption on the whole branch.

If g has one weak sign on the entire branch, then H|_K=h_* differs from H(p). In the B53 connection setting p->q with common regular level H(p) and negative covector rate rho, K therefore avoids p, q and L+. Without this whole-branch sign assumption the same avoidance follows from r>=0 versus rho<0, but the inequality h_*!=H(p) is not proved.

## 2. Dependencies and complete flows

The exact profile identities and the global helicity-free rank theorem A413 are

    h=B cross Omega-aU, BH=-ag, Omega H=0,
    [B,Omega]=-kappa Omega, div B=3c,
    dH wedge dg=0 on closure Vort.                     (1)

The equilibrium inputs are A478, excluding U=0 at a vortical carrier equilibrium, and A496, giving its velocity-covector eigenvalue rho<=-a. Their hypotheses are precisely the global C2/C1 helicity-free uniformly sublinear class above. The proofs are retained in the earlier audit, including in the team records. The B53 stable-branch properties are proved in the team records. The arguments below do not need a pressure normalization at infinity, natural decay rates or a uniform gradient bound.

Uniform sublinearity implies |B(x)|<=C(1+|x|), so its C2 flow Phi_t is complete. Outside a fixed ball,

    d_t |Phi_t x|^2=2c|Phi_t x|^2+2(Phi_t x).U(Phi_t x)
                   >=c|Phi_t x|^2.

Thus the backward images of a compact set lie in one compact ball. In particular, every negative semiorbit has compact closure.

Let Gamma_s be the initially local C1 vortex flow. Cauchy transport is

    Omega(Phi_t x)=e^(-kappa t) D Phi_t(x) Omega(x).    (2)

For fixed x, the compact closure of its negative carrier semiorbit has a uniform local vortex existence time delta>0. For any finite vortex-time interval, choose T sufficiently large. The curve

    s -> Phi_T Gamma_(e^(-kappa T)s)(Phi_(-T)x)

is then defined on that interval, starts at x, and has derivative Omega by (2). Uniqueness identifies the extensions, proving completeness of the original vortex flow. No bound on Omega at spatial infinity is used.

## 3. Transport, regular zero propagation and nonvanishing velocity

Differentiate BH=-ag once to obtain

    h'=-DB^T h-a grad g.                              (3)

At h=0 this gives h'=-a grad g. Since g-H=|U|^2/2-P, grad g=grad(|U|^2/2-P) there. Differentiating Omega H=0 along the vortex flow gives h'=-D Omega^T h. This homogeneous equation preserves h=0. Uniqueness for Omega prevents finite-time entry into {Omega=0}. Hence C is vortex invariant.

On Reg, l=(grad g.h)/|h|^2 is C1. On closure Vort intersect Reg, (1) implies dg=l dH. Differentiate this identity first on the open vortical set and extend by continuity to get dl wedge dH=0. Thus dl=m dH there, with m=(grad l.h)/|h|^2 continuous. On a regular carrier interval,

    g'=-a l g, h'=(-a l I-DB^T)h.                    (4)

If g vanishes at one regular point, it remains zero on the maximal regular interval. There Bl=m BH=0, so l is constant and

    h(Phi_t x)=e^(rt) D Phi_t(x)^(-T)h(x), r=-a l.   (5)

At any finite endpoint the right side is nonzero. The regular interval is therefore all of R. This proves the regular zero propagation used below, in both time directions. Applying Omega to BH=-ag, using [Omega,B]=kappa Omega and Omega H=0, also gives Omega g=0.

Put F=B cross Omega. The matrix cross-product identity and (2) give

    F'=(-a I-DB^T)F.                                 (6)

Suppose x in C has U(x)=0. Then F(x)=0. A478 excludes B(x)=0. Along its entire carrier orbit, B and Omega stay nonzero by uniqueness and (2), and F stays zero by (6). Thus B and Omega are parallel, and helicity-freeness gives g=0. If the orbit had a regular point, regular zero propagation would make x regular. Hence h=0 everywhere on it. Since F=h+aU=0, U=0 on the orbit and y(t)=e^(tA)x.

Write Omega(y(t))=beta(t)B(y(t)); differentiation gives beta'=-kappa beta. Moreover |B(y(t))|=e^(ct)|B(x)|. Therefore |Omega(y(t))|=e^(-t)|Omega(x)|, which diverges as t->-infinity although y(t)->0. This contradicts continuity of Omega. Thus U!=0 on C. The identity F=aU then shows that B and Omega are independent. It only makes U perpendicular to both; B need not be perpendicular to Omega.

## 4. Nondegenerate and degenerate critical points

Let x in C and v=grad g(x)!=0. Differentiate dH wedge dg=0 on the open set Vort at x. For every z,

    (D2H(x)z) wedge v=0.

The Hessian is symmetric, so D2H(x)=mu v tensor v. Equation (3) gives D2H(x)B(x)=-a v, whence mu Bg(x)=-a. In particular Bg(x)!=0 and the Hessian formula in Section 1 follows.

Since g is a C2 submersion, take g as one local coordinate. The rank identity says that all derivatives of H in the other coordinates vanish. On a connected coordinate box H=F0(g), with F0 in C2. At x, g=0 because BH=-ag and h=0; F0'(0)=0 and F0''(0)=-a/Bg(x)!=0. After shrinking the box, F0' has its only zero at g=0. This proves C={g=0} locally. The surface is transverse to B because Bg(x)!=0 and tangent to Omega because Omega g=0.

Taking t0=0 on the crossing orbit gives

    g(t)=Bg(x)t+o(t),
    H(t)=H(x)-(a Bg(x)/2)t^2+o(t^2).

For t!=0 sufficiently small, l=1/F0'(g), hence t l(t)->-1/a. More generally, on any zero-free regular interval,

    integral_s^t l(u) du=-(1/a)log(|g(t)|/|g(s)|).     (7)

As t approaches a finite zero from the interior, this oriented integral tends to +infinity. If that endpoint is on the left, the increasing-time integral from the endpoint to s tends to -infinity. In either case l is not absolutely locally integrable there. The orientation is part of the assertion.

Now suppose x in C and dg(x)=0. From h=B cross Omega-aU and helicity-freeness,

    U cross h=-g Omega.

Differentiate at x to obtain U(x) cross D2H(x)z=0 for every z. Since U(x)!=0 and the Hessian is symmetric, D2H(x)=lambda U(x) tensor U(x). Equation (3) gives D2H(x)B(x)=0. This proves the rank-one bound and nothing further about the order or sign of the contact.

## 5. Carrier invariance and the distinction from sign control

If C is carrier invariant, an orbit through C has h=0 everywhere and hence g=0 everywhere. An orbit with a regular zero of g also has g=0 everywhere by Section 3. Thus each vortical orbit has g identically zero or nowhere zero.

Conversely assume this orbit alternative. An orbit through C has a zero of g and therefore g=0 everywhere. It cannot have a regular point, since regular zero propagation would make its initial point regular. Hence the orbit stays in C.

The weaker assertion that g never changes sign does not give this alternative: scalar identities allow a zero of even order. For example B=partial_s, H=s^3 and g=-3s^2/a satisfy BH=-ag and the one-dimensional rank identity. This is only a scalar example, not an Euler field. It shows why an argument based solely on those scalar identities cannot replace nonvanishing by a no-sign-change claim.

## 6. An exact local swirl crossing

Choose K0>0 and omega>0, let p_exp=(1-c)/c>1, and in cylindrical coordinates r>0 put

    f(r)=K0 r^(-p_exp), U=f e_theta, P=-f^2/(2 p_exp),
    B=c r e_r+(f-omega r)e_theta+c z e_z,
    Omega=w e_z, w=f'+f/r=-(a/c)f/r.

The field is divergence-free and helicity-free. In momentum, the radial component is -f^2/r+P'=0, the azimuthal component is (1-c)f+c r f'=0, and the axial component is zero. Thus this is an exact local rotating Euler profile on r>0.

Here

    g=f(f-omega r), H=((p_exp-1)/(2 p_exp))f^2-omega r f,
    H'=w(f-omega r).

The critical cylinder is r0=(K0/omega)^c, where f=omega r0. Since r(t)=r0 e^(ct), with the crossing at t=0,

    g(t)=omega^2 r0^2 e^(-a t)(e^(-t)-1),
    Bg|_(r0)=-omega^2 r0^2, H''(r0)=a omega^2/c^2.

At the crossing and z=0, B,U,Omega are pairwise orthogonal. Elsewhere on that cylinder B.Omega=c z w, usually nonzero. Away from the cylinder B.U=g need not vanish, even if z=0. The c z e_z term in B must be retained.

The velocity is singular on the axis, so the example is outside the global C2 class. Its independence of z also prevents uniform velocity decay, but z-independence alone would not violate uniform sublinearity. This calculation proves that local Euler identities permit nondegenerate crossings. It does not prove that a global stable branch crosses, nor that global sign control is false.

## 7. The regular predecessor limit and its rate

The stable branch is vortical: a sufficiently late point is near the vortical equilibrium p, and (2) preserves nonzero vorticity for finite times. Backward trapping makes its negative orbit closure compact. Therefore K is nonempty, compact, connected, two-sided invariant and contained in closure Vort; the distance from gamma(t) to K tends to zero as t->-infinity.

Assumption (R) makes h uniformly nonzero on a neighborhood of K. On a sufficiently early tail, g cannot vanish: a regular zero would propagate along the entire orbit and contradict the assumed late nonzero tail. Thus g has one strict sign on this early tail. H is strictly monotone there and bounded, so it has a backward limit h_* and H=h_* on K. Invariance and BH=-ag give g=0 on K.

The functions l and m in Section 3 are bounded near K. Along the early tail,

    l'=m H', |l(t)-l(s)|<=M |H(t)-H(s)|.

Thus l has a limit l_*, and l=l_* on K. Put r=-a l_*. If r<0, then on an early tail g'=(-a l)g makes |g| grow exponentially backward, contradicting its convergence to zero on K. Hence r>=0. Equations (4)-(5) yield the constant-rate covector law on K.

If g has one weak sign on the whole branch, H is monotone on all of R. Its late tail is strictly monotone, so h_*!=H(p). This proves the stronger level separation only under that additional sign hypothesis.

## 8. Irrotationality and nonvanishing velocity on K

On K, g=0, h!=0 and U cross h=0, so both U and F=h+aU are parallel to h. Define f0=(F.h)/|h|^2 near K. It is C1. Equations (5)-(6) give

    B f0=-(a+r)f0 on K.

Since a+r>0 and K is compact and two-sided invariant, boundedness forces f0=0. Hence B cross Omega=0 and U=-h/a on K.

Suppose x in K is vortical. If B(x)=0, then (3) and dg=l_*dH give DB(x)^T U(x)=rU(x), contradicting A496 because r>=0>-a. Otherwise B and Omega are nonzero and parallel on its orbit. Write B=b(t)Omega; then b'=kappa b. Boundedness of Omega on K gives

    |d_t Phi_t x|<=|b(0)| max_K|Omega| e^(kappa t), t<=0.

The negative-time speed is integrable, so Phi_t x tends to q in K with B(q)=0. Set tau=b(0)e^(kappa t)/kappa, allowing either sign. In this parameter dy/dtau=Omega(y), with finite endpoint y(0)=q. The identity

    y(tau)-q=integral_0^tau Omega(y(s)) ds

extends the solution to that endpoint. If Omega(q)=0, local uniqueness makes it constant, impossible. Thus q is a vortical equilibrium with rate r>=0, again contradicting A496. Consequently Omega=0 on K. Since U=-h/a there, min_K|U|>0 and the covector transport law for U follows.

In the B53 connection setting, p,q,L+ have regular covector rate rho<0. They cannot meet K, where the same well-defined scalar -a l is nonnegative. This proves avoidance even without a whole-branch sign assumption.

## 9. Lyapunov spectra and a distinguished saddle equilibrium

Over K let E_x=ker dH_x. Equation (5) makes E invariant. The normal quotient expansion is e^(rt)|h(x)|/|h(Phi_t x)|. Since div B=3c, the area factor on E is

    |det(D Phi_t|_E)|=e^((3c-r)t)|h(Phi_t x)|/|h(x)|. (8)

The h-ratios are uniformly bounded above and below. For a nonstationary ergodic invariant probability, B is nonzero almost everywhere, lies in E and satisfies D Phi_t B(x)=B(Phi_t x). Its exponent is zero: its norm is bounded above, while recurrence to a set |B|>=1/j gives arbitrarily late positive lower bounds; the exponent exists by the multiplicative ergodic theorem. Equation (8) gives the other level exponent 3c-r. The normal quotient exponent is r. Restriction and quotient therefore give the full multiset {0,r,3c-r}, including repeated values. These applications concern bounded invertible finite-dimensional cocycles over compact invariant sets.

At an equilibrium the covector law gives DB^T U=rU and the level trace 3c-r. At a periodic orbit of period T the three multipliers are

    1, e^((3c-r)T), e^(rT).                           (9)

To obtain an equilibrium with sufficiently strong level expansion, choose time zero on an early regular tail and let n(t)=Omega(gamma(t))/|Omega(gamma(t))| for t<=0. Then n lies in ker dH and follows the normalized derivative cocycle. Cauchy transport gives

    d_t log|Omega(gamma(t))|=n(t).DB(gamma(t))n(t)-kappa.

Average this lifted orbit on [-T,0]. Compactness of the negative orbit closure and of the unit sphere gives weakly convergent occupation measures. A bounded endpoint error under time translation proves invariance of every limit. Its base is in K and its vectors lie in E. For phi(x,n)=n.DB(x)n,

    integral phi dnu_T
      =kappa+(log|Omega(gamma(0))|-log|Omega(gamma(-T))|)/T.

Omega is bounded on the compact negative orbit closure, so the limiting average is at least kappa. Ergodic decomposition supplies an ergodic lifted component with average at least kappa. Birkhoff's theorem identifies this average with its selected vector's forward exponent. Its base projection is ergodic. If that projection were nonstationary, its largest level exponent would be max(0,3c-r)<=3c<kappa, a contradiction. Thus the projection is a point mass at an equilibrium of K.

The level matrix at that equilibrium has maximal real eigenvalue part at least kappa and trace 3c-r. A nonreal conjugate pair would have real part (3c-r)/2<kappa. Hence both eigenvalues are real, and can be ordered as lambda_u>=kappa and lambda_s=3c-r-lambda_u<=-a-r<0. Keeping the selected vector in the level plane is essential: an ambient stretching estimate alone could instead detect the normal exponent r.

## 10. Periodic repellers are excluded when 0<r<3c

Suppose a periodic orbit Gamma subset K has period T0. In this range both transverse multipliers in (9) exceed one, so Gamma is a forward hyperbolic repeller. Its maximal Floquet exponent Lambda=max(r,3c-r) is smaller than kappa. Choose Lambda<beta<kappa. For a sufficiently large integer m, L=mT0 satisfies

    sup_(x in Gamma)||D Phi_L(x)||<e^(beta L).

Indeed the matrices at different phases are uniformly bounded conjugates of powers of one monodromy matrix, and polynomial Jordan factors are absorbed by the strict exponent gap. Continuity gives the same estimate on a neighborhood N of Gamma.

There is a smaller open tube N0 whose whole negative orbits remain in N and approach Gamma. One construction uses the inverse Poincare map: its derivative has spectral radius below one, so an equivalent norm and a sufficiently small transverse disk make it a contraction into that disk; flow saturation gives the tube, with the intervening orbit segments contained in N.

For y in N0, split the derivative from Phi_(-nL)y to y into n blocks. Each starts in N, so its norm is at most e^(beta nL). Omega is bounded by M on the negative orbit tube. By (2),

    |Omega(y)|<=M e^(-(kappa-beta)nL)->0.

Thus N0 is irrotational, contradicting Gamma subset K subset closure Vort. This excludes periodic orbits in K in the stated open rate interval, including a periodic component of a larger K.

## 11. Why this does not give surface collapse

Under (R), the regular surface S={H=h_*} exists near K. Set N=h/|h|^2 and Y=B-(BH)N; then YH=0. On K, BH=0 and d(BH)=r dH, so the divergence of Y with respect to the level area form i_N vol is 3c-r. The backward divergence is r-3c, which has no prescribed positive sign.

The early stable branch has H!=h_* because H is strictly monotone toward h_* there. Thus it is not an orbit on S. A projection to S has not been shown to preserve the orbit equation. The external surface-orbit hypothesis of the previous surface-collapse lemma is absent, as are the required hypotheses at every equilibrium. Finding one saddle does not supply them. No conclusion K={q'} follows.

Without (R), a zero-g orbit in closure Vort with one critical point has h=0 everywhere by Section 3. Equation (3) gives dg=0 there. The exact one-form identity

    L_B U^flat=dg-dH-a U^flat

then gives Phi_t^*U^flat=e^(-at)U^flat. This does not extend l through the critical set or classify singular predecessor sets.

## 12. Source comparison, repairs and scope

The submitted B54 Proposition 14(a)-(g), its consolidated Theorem VL(12), the full 413-line original consultation proof and the full 425-line referee proof were read. The independent derivations above agree with the referee's mathematical repairs. The original proof's first appeal to uniform decay is replaced by the sublinearity argument in Section 2.

The following scope repairs are necessary when reusing the submission.

- A simple sign-changing crossing requires dg!=0. The last Remark's inference that this is the only way a stable branch can meet g=0 omits this hypothesis. Degenerate critical zeros remain unclassified.
- The local swirl example proves local possibility. It does not disprove global sign control, nor establish failure of carrier invariance in the global class. Include K0,omega>0, the axial carrier term c z e_z, and restrict the pairwise-orthogonality assertion to the crossing at z=0.
- Formula (7) uses an oriented integral toward the endpoint. On the right side of a left endpoint, its increasing-time version has the opposite sign.
- The regular predecessor classification uses its realization as the alpha-limit of a vortical stable branch with a late nonzero-g tail. An arbitrary regular compact invariant set is insufficient. Assumption (R) remains unproved. Whole-branch sign control is needed for h_*!=H(p), but not for the other conclusions proved here.

The parent Theory Agent B agent is configured model, while its two supplied consultation proofs are the external referee (a second model). Their attempted model calls failed at credential retrieval before invocation; they are not completed model reviews. Existing configured model team agents can compare this result through the shared files. Provider runtime and a focused model reply on this B54 proof are not independently attested.

No computation, numerical approximation, formal build, server, remote job or new model invocation was used in this audit. All constants needed for compactness and flow estimates may depend on the profile, c, finite omega and the indicated compact set. No estimate asserts uniformity as |omega| tends to infinity. The theorem itself allows every finite omega.


## 13. Repeated source check and remaining compressed-text corrections

The repaired Proposition14 and TheoremVL(12) were read again against all twelve sections above. Their principal claims now state the dg!=0 hypothesis for a simple crossing, leave degenerate contacts open, and restrict the counterexample conclusion to local Euler identities. The regular-predecessor conclusion is valid under (R) alone as proved in Sections7-10; its weaker statement with an additional one-sign premise is also valid. This repaired mathematical core is CONFIRMED A1059. The result does not acquire new hypotheses or a larger class on this reread.

Some older or compressed wording in the same source still needs correction, recorded as A1060.

1. Remark(xxxi'') omits c z e_z from the carrier. The full three-dimensional carrier of the swirl is B=c r e_r+(f-omega r)e_theta+c z e_z. Proposition14(f) explicitly acknowledges the omission, but the earlier displayed equality should also be repaired.
2. The stated positive crossing radius and the claim that f-omega r is decreasing use K0>0 and omega>0. Include those assumptions in Proposition14(f). A sign-reversed crossing can be treated separately; the displayed positive-parameter calculation does not cover arbitrary K0,omega.
3. Pairwise orthogonality holds at r=r0 AND z=0. At z=0 alone one still has B.U=g=f(f-omega r), which is nonzero unless r=r0. In general B.Omega=c z w, while U.B=0 only on the crossing cylinder.
4. The old phrase that sign control is unavailable in general must be restricted to the local identities. The exact swirl is singular on the axis and is not uniformly decaying as |x| tends to infinity, since it is independent of z. It does not refute a theorem restricted to global smooth decaying profiles.
5. The final residual list still calls the pressure-gradient nondegeneracy and pinning rho=-2(1-c) open for an escaping W1 half-line under the actual HF/natural tail hypotheses. Those two facts are now CONFIRMED A1022 and A1041-A1045. They remain unavailable if the tail hypotheses are removed, and they do not settle the bounded heteroclinic alternative or exclude the permitted exact rate.

Items1 and3 are algebraically false if read as standalone equalities at their printed scope. Item4 is an unsupported local-to-global inference at its broad reading. Item5 is superseded, rather than a newly refuted mathematical conjecture. The explicit repairs follow from the full proof above and the actual-ray and exact-rate reviews. No verdict on the corrected B54 theorem is withdrawn.

The reread snapshot and its hash are retained in verification. This is a source-maintenance audit, not an additional completed model consultation. The source parent is configured model; the two nested proofs are the external referee (a second model) their model attempts failed before invocation.
