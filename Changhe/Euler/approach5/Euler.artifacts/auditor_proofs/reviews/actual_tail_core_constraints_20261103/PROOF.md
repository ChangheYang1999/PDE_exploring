# Actual tail vortex curves and their transported scalar zeros

Status: CONFIRMED A701-A703 after full source and independent-proof postreads. Date: 2026-11-03T10:21:12.481281+00:00.

## 1. Statement and reading order

Write J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, B(x)=Ax+U(x), and Omega=curl U. A profile means U in C2(R3;R3), P in C1(R3),

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0.

All omega below are arbitrary finite real numbers. Constants may depend on the profile and omega.

Part I. Suppose 1/3<c<1, U is bounded, U(R .)->0 in distributions, and

    integral_1^infinity m(r) dr/r < infinity,
    m(r)=sup_{|x|>=r}|DU(x)|.

Let V,W be the actual velocity and vorticity tails of A209-A210. Then W on D=R3 minus {0} has no nonconstant periodic integral curve. In particular every full-azimuthal open region away from the rotation axis on which V is C1, axisymmetric and swirl-free is irrotational. No helicity or pressure-tail hypothesis is used in Part I.

Part II. Suppose 2/5<c<1/2, put p=(1-c)/c, a=1-2c and d=p-1=a/c, and impose in addition

    U.Omega=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).

Let P2 be the canonical pressure tail of A530-A531 and let

    k(x)=(Ax).V(x), S(x)=P2(x)-|V(x)|^2/2,
    pi(x)=exp((omega/c)log|x| J)x/|x|,
    K=k restricted to S2, h=S restricted to S2.

If U is nonzero, then Z0={w in S2: K(w)=h(w)=0} is nonempty. For volume-almost every x in D where W(x)!=0, both ends of its maximal W integral curve tend to 0, and the angular distance to Z0 tends to 0 at both ends. In particular h cannot be nowhere zero.

The conclusions retain the actual-profile hypotheses. They are not conclusions about an arbitrary pair V,P2 satisfying five leading equations. The natural estimates in Part II may instead be supplied by U->0 and |DU|=O(sqrt(|x|)) in this c interval, by A601. This does not remove the derivative premise from the campaign conjecture.

Read Sections2-3 for Part I, Sections4-6 for Part II, and Section7 for audit dependencies and limitations. No numerical calculation or formalization is used.

## 2. Periodic tail vortex curves lift with their original parameter

Under Part I, A209 gives the complete carrier flow Phi_s, the limit

    Xi(y)=lim_{s->infinity} exp(-sA)Phi_s(y),

and a compact null set C=Xi^(-1)({0}). Its restriction Xi:E=R3 minus C -> D is a C1 diffeomorphism. A210 gives the exact pointwise identity

    W(Xi(y))=D Xi(y)Omega(y).                         (2.1)

If z is a nonconstant periodic C1 solution of z'=W(z) in D, the compact image of its period has compact inverse image in E. The curve y=Xi^(-1)(z) is C1 and periodic with the same parameter and period. The inverse derivative and (2.1) give

    y'=D Xi(y)^(-1)W(z)=Omega(y).

No existence or uniqueness theorem for a merely continuous W is being assumed here. A proposed curve suffices for the chain rule. Conversely local original Omega flows give local tail flows by Xi, and establish uniqueness wherever a tail curve remains in D.

To exclude the original periodic curve, take curl of the profile equation:

    [B,Omega]=-(1+c)Omega.

Consequently Phi_-s takes an Omega orbit of period T to one with period exp(-(1+c)s)T. The sign can also be checked from

    D Phi_t(y)Omega(y)=exp((1+c)t)Omega(Phi_t(y)).

If |U|<=M, the radial derivative along a carrier trajectory obeys r'>=cr-M whenever r>0. Thus the backward images of a fixed compact set stay inside any sufficiently large ball whose radius exceeds both its original radius and M/c. This gives a single compact ball containing all of the shrinking-period curves. On it L=sup|D Omega| is finite.

For a nonconstant Omega curve y of period tau, v=y' is periodic, has mean zero, and v'=D Omega(y)v. Periodic Wirtinger therefore gives

    integral_0^tau |v|^2 <= (tau/(2pi))^2 integral_0^tau |v'|^2
                          <= (tau L/(2pi))^2 integral_0^tau |v|^2.

The last integral is positive. For L=0 there is an immediate contradiction; otherwise tau>=2pi/L. The periods exp(-(1+c)s)T violate this bound as s->infinity. This reproduces the needed A014 argument with all confinement and regularity hypotheses explicit.

## 3. The complete-circle consequence

Suppose on one circle with cylindrical radius rho>0 and height z0,

    W(rho cos phi,rho sin phi,z0)=b(phi)e_phi,
    e_phi=(-sin phi,cos phi,0),

where b is continuous, periodic and nowhere zero. Then b has constant sign and |b| has a positive minimum. Inverting the strictly monotone integral of rho/b constructs a global angular solution phi'=b(phi)/rho. Its associated spatial curve is a nonconstant periodic W curve with period

    T=rho integral_0^(2pi) 1/|b(phi)| dphi.

Section2 rules it out. A partial azimuthal arc or a circle with a zero of b does not give this conclusion.

On a full-azimuthal open region where V is C1, axisymmetric and swirl-free, write

    V=V_rho(rho,z)e_rho+V_z(rho,z)e_z.

The cylindrical curl formula gives

    W=(partial_z V_rho-partial_rho V_z)e_phi.

A nonzero value of its coefficient persists as the same nonzero value around the entire corresponding circle. Hence its coefficient must vanish at every point of the region. There is no assumption on the velocity outside this region, nor on the sign or nonvanishing of its radial component. In particular every actual vortical full-azimuthal swirl-free band considered in the interface calculations is excluded at once by this argument. The local leading-equation germs themselves are not refuted.

## 4. Core-return is the additional actual-profile input

Part II implies all assumptions of Part I. A360 gives a stronger fact specific to actual tails in the target c interval: for volume-almost every initial point of {W!=0}, the maximal W arc z:(t_-,t_+)->D has finite duration and finite length in both directions, and

    z(t)->0 as t->t_- or t->t_+.                     (4.1)

Only the two limits in (4.1) are used for Part II. They must not be replaced by recurrence of a complete W flow. The original complete Omega curve may pass through the compact scattering core C; a single tail arc is the image only of a connected interval avoiding C.

For clarity, the checked mechanism in A360 is the complete time change X=r^(p+2)W. In twisted cylindrical variables it has rho'=G_r(w), w'=Y(w), with div_S Y=(p-1)G_r. The angular flow therefore has Jacobian exp((p-1) integral G_r). Positive drift to infinity has angular measure zero by the area estimate of A274. Hopf decomposition and recurrence of continuous sphere flows put almost every nonzero angular point in the dissipative part. At its two ends the radial logarithm tends to minus infinity. Summability of the angular Jacobians gives finite W duration and length because p+2>1>p-1>0. Periodic angular curves with zero radial drift would be the periodic full W curves already excluded in Section2. These statements, including the null-set and endpoint passages, were checked in the full independent A360 proof; no hypothesis of isolated equilibria or of full W completeness is added here.

If W is nonzero anywhere, its continuity supplies a positive-volume open set of such points. At least one curve there has property (4.1).

## 5. A common-zero lemma for finitely many transported scalars

Let F1,...,FN be continuous on D, constant on every W integral curve, and suppose

    Fj(exp((log r)A/c)w)=r^(-delta_j) f_j(w),
    delta_j>0, f_j continuous on S2.

Along any curve with (4.1),

    f_j(pi(z(t)))=|z(t)|^(delta_j) Fj(z(t0))->0

at either end, simultaneously for every j. Compactness of S2 gives a subsequential angular limit at each end. Continuity puts every such limit in the common zero set Z={f1=...=fN=0}. Thus Z is nonempty whenever W is nonzero and a curve with (4.1) exists.

The stronger distance assertion also follows directly. If an end admitted a sequence whose angular distance from Z was bounded below by epsilon>0, a convergent subsequence on S2 would have all fj equal to zero while still being at least epsilon from Z, a contradiction. This proves angular distance tends to zero. It does not prove a unique angular limit, nor a zero of V or W at the limiting directions.

For a single nowhere-zero f, the contradiction is immediate: min_S2|f|=m>0 gives |F(z(t))|>=m|z(t)|^(-delta)->infinity, whereas F has a fixed finite value on the curve. Either sign is covered.

## 6. The actual k and S meet every hypothesis of the lemma

A530-A531 give locally Lipschitz V and S, continuous W=curl V, V.W=0 and div(SW)=0. They also prove constancy of S on every C1 W curve, not merely almost every curve. Here is the relevant regularity argument. On a compact neighborhood of a compact segment of a curve, mollify S. Since div W=0 and W.grad S=0 as a distribution, almost everywhere,

    |W(x).grad S_epsilon(x)|
      <= Lip(S) sup_{|x-y|<=epsilon}|W(x)-W(y)|.

The bound tends uniformly to zero. Integrate the derivative of S_epsilon along the curve segment, and pass to its uniform limit S. This gives constancy on each segment, hence on the whole maximal arc. No differentiability of W is needed for this step.

Set L=(1-c)I+omega J. The velocity homogeneity gives DV Ax=-LV almost everywhere. Since V is Lipschitz, the weak product identity gives

    grad k=A^T V+(DV)^T Ax
          =A^T V+Ax cross W+DV Ax
          =Ax cross W-aV.                            (6.1)

The right side is continuous. Thus k is C1 with this gradient and W.grad k=-a V.W=0 at every point. The chain rule makes k constant along every W curve.

The exact scalar homogeneities are

    k(exp(sA)x)=exp(-a s)k(x),
    S(exp(sA)x)=exp(-2(1-c)s)S(x).

In the first equality, the rotation factors cancel in the scalar product and A commutes with them. In the second, both canonical P2 and |V|^2 have the displayed degree. Taking s=(log r)/c gives delta_1=a/c=p-1>0 and delta_2=2p>0. Section5 applied to k,S yields the claimed common zero set and the almost-everywhere angular-distance conclusion.

Finally W identically zero forces Omega=0 on E by (2.1) and invertibility of D Xi. Since C is compact null and Omega is continuous, Omega=0 everywhere. Together with div U=0 this makes U harmonic on R3; boundedness makes it constant and distributional zero blow-down, or decay, makes that constant zero. Thus U!=0 guarantees W!=0 and the preceding common-zero argument is nonvacuous.

## 7. Scope, dependencies and model comparison

This proof confirms LIT173 and LIT174 at exactly their stated conditional profile scopes. The periodic-curve lifting was already part of A360; the useful new explicit consequence is the entire local swirl-free full-azimuthal band obstruction. The common-zero conclusion uses the global scattering realization through A360. It does not follow here from Poisson, rank and homogeneity alone, and does not classify periodic orbits of the separate velocity quotient field Bq.

For actual global-HF/natural profiles, the nowhere-zero-S application of the infinitely-many-vortical-components problem is excluded. Abstract tails with those component configurations are not excluded by this proof. General nodal concentration, sign-changing original helicity, and the derivative bound from bare decay remain open.

Independent dependencies read in full for this audit are the proofs of A209, A210, A360, A531 and A274, together with the later A603 reconstruction. Their primary recurrence and Hopf results were read and retained during the original dependency audits. The local period lower bound was rederived above. No new numerical calculation, formal build, remote computation or model request occurred.

The source submissions request focused comparison from the existing configured model coordinator and theory agents. Their actual responses, when received, must be archived separately; none is inferred merely from a requested review. The separate CO41 response does provide an actual continuing configured-model comparison on A691-A700, not on the new common-zero theorem. Provider runtime is not independently attested.
