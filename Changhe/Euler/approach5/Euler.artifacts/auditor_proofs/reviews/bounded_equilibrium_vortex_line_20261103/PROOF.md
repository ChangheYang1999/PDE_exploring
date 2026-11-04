# Measures on the forward limit of an equilibrium vortex half-line

Status: CONFIRMED as A540 after complete independent reconstruction, repeated postread and refreshed source comparison. The configured-model premises have separate recorded reviews; a focused review of this synthesis has not been received.

## 1. Exact statement

Let 0<c<1/2, omega be any finite real number, J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, B=Ay+U, W=curl U, a=1-2c and kappa=1+c. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, (1-c)U+(DU)B+omega JU+grad P=0,
    U(y)=o(|y|) uniformly, U.W=0 everywhere.

Let p be a vortical carrier equilibrium: B(p)=0, W(p)!=0. The confirmed A468,A478,A496 give U(p)=-Ap!=0 and a real rho satisfying

    DB(p)^T U(p)=rho U(p), rho<=-a.

Let L+ be either half of the complete W-orbit through p, parametrized as a forward B-orbit by (3) below. Suppose this half-line is bounded, and let K be its forward omega-limit set. Then the conclusions are:

1. K is nonempty, compact and invariant under the full B-flow. It lies in closure{W!=0} and satisfies W=0, H=H(p), g=0, grad H=-aU and grad g=rho U throughout K, where H=P+|U|^2/2+(Ay).U and g=U.B.
2. U has no zero on K. In particular |U| has a positive minimum there and 0 does not belong to K.
3. On K, Phi_t^* U^flat=e^(rho t)U^flat. Every compact whole-flow-ergodic invariant probability nu supported in K with nu(B=0)=0 has forward Lyapunov spectrum {0,rho,3c-rho}, with multiplicity. Its top backward exponent is -rho>0.
4. Every whole-flow-ergodic invariant probability on K is either an atom at a nonzero irrotational carrier equilibrium q satisfying DB(q)^T U(q)=rho U(q), or the orbit probability of a nonconstant periodic B-orbit on which W=DW=0 and U is nonzero, with the same covector rate rho.

If rho<=-2a, the periodic alternative is a lower-window W2 witness and the equilibrium alternative is a W1-irrotational witness. Both inherit the rate rho of p. The classification concerns invariant ergodic probabilities. It does not assert that every point of K belongs to a periodic orbit or is an equilibrium. Connecting or wandering points are not classified by this argument. No uniform velocity decay or derivative bound at infinity is assumed.

## 2. Exact transport on the original vortex line

The full equations give

    grad H=B cross W-aU, BH=-ag, WH=0,
    [B,W]=-kappa W.

The complete W-flow is the confirmed A048 consequence of uniform sublinearity and the bracket. Its orbit through p satisfies

    B(Gamma_tau p)=kappa tau W(Gamma_tau p).              (3)

Indeed both sides solve the corresponding differentiated flow identity with B(p)=0, or equivalently differentiate the bracket commutation law at the equilibrium. W cannot vanish at a finite parameter time, by uniqueness. The two parameter halves tau>0 and tau<0 are B-orbits with tau(t)=tau(0)e^(kappa t). On the entire line, helicity zero gives g=0 and the Lamb identity gives grad H=-aU.

Let Sigma be the connected regular vortical H-level through p. The rank identity A413 and its A496 continuation give

    g=0, dg=-(rho/a)dH on Sigma,
    (B.grad)grad H=rho grad H-DB^T grad H.                 (4)

These statements are valid on the whole component. They do not say grad g=rho U everywhere on that component: generally aU=(f-1)grad H there with f defined by B cross W=f grad H.

Initially U!=0 on the vortex line near p. On each component of that line where U!=0, (4) and grad H=-aU give

    (B.grad)U=rho U-DB^T U.                              (5)

The invertible linear transport prevents U from vanishing at a finite B-time. A finite nonzero vortex-parameter endpoint corresponds to a finite B-time, and U(p)!=0 handles the remaining parameter value tau=0. Consequently U!=0 everywhere on this vortex line, which stays in Sigma. Thus on the line, specifically,

    grad g=rho U,
    Phi_t^*U^flat=e^(rho t)U^flat.                       (6)

This line is an invariant curve tangent to the kappa eigendirection. Calling it the strong unstable curve requires an eigenvalue comparison and is unnecessary here.

## 3. The compact limit set and uniform nonvanishing of velocity

Boundedness of the forward orbit, full completeness of B and local compactness give a nonempty compact full invariant omega-limit set K. For example any sequence of forward times tending to infinity has an accumulation point; translating such sequences by any fixed positive or negative time proves full invariance. It is contained in the vortical closure because the original line has W!=0.

On the half-line, (3) implies

    |W(Phi_t y)|=|B(Phi_t y)|/(kappa |tau(0)|e^(kappa t))->0,

as B is bounded on its compact orbit closure. Hence W=0 on K. By continuity H=H(p), g=0, grad H=-aU and grad g=rho U on K.

The momentum equation makes grad P C1, so P and H are C2. Differentiate BH=-ag along K, and use the just established grad g=rho U=-(rho/a)grad H. This gives

    (B.grad)grad H=rho grad H-DB^T grad H,

and hence (5) on K. The covector law (6) therefore holds on every full orbit in K. In particular {U=0} intersect K is fully invariant.

The origin is not in K. If it were, g(0)=U(0).B(0)=|U(0)|^2=0 would imply U(0)=B(0)=0; also W(0)=0 and 0 would lie in the vortical closure. This contradicts A478, which gives an irrotational neighborhood of such an origin in the present global class.

Now suppose U(q)=0 for any q in K. By (5) and uniqueness for the homogeneous linear equation, U=0 on the entire B-orbit of q. That orbit therefore solves y'=Ay and equals exp(tA)q. It stays in compact K for every t, while |exp(tA)q|=e^(ct)|q|. Thus q=0, already excluded. This proves U is nowhere zero on K. Compactness supplies a strictly positive minimum. This pointwise argument is stronger than merely proving U!=0 almost everywhere for each invariant measure and removes any need to assert integrability of log|U| from temperedness.

## 4. The adjoint exponent and the flow direction

Let nu be whole-flow ergodic, supported in K, with nu(B=0)=0. The derivative cocycle and its inverse are bounded over each unit time on compact K, so the multiplicative ergodic theorem applies. By (6), at a typical x,

    (DPhi_t(x))^(-T)U(x)=e^(-rho t)U(Phi_t x).

Both upper and positive lower bounds for |U| on K show that this vector has adjoint exponent exactly -rho. Adjoint exponents are the negatives of the forward derivative exponents, so rho is a forward exponent.

For the flow direction, DPhi_t(x)B(x)=B(Phi_t x). Its forward exponent exists at an Oseledets regular x, since B(x)!=0. B is bounded on K, giving an upper bound zero. Recurrence supplies a sequence t_j tending to infinity on which |B(Phi_tj x)| is bounded below: for almost every point of {B!=0}, choose a positive-measure set {|B|>=1/m} containing it and use recurrence for the time-one map. This argument does not require that the time-one map itself be ergodic. Thus the existing limit for the flow-direction exponent is zero. Equivalently one can use whole-flow recurrence on a local section. No integrability of log|B| is asserted.

The sum of all three forward exponents is 3c by the exact determinant law det DPhi_t=e^(3ct). Since rho<0, it differs from the flow exponent zero. The remaining exponent is 3c-rho>0. This proves the spectrum and its backward form {0,-rho,rho-3c}.

## 5. Classification of ergodic probabilities

For any whole-flow-ergodic nu supported in K, the set {B=0} is invariant. If it has positive nu mass, it has full mass, and the flow on it is the identity. Ergodicity therefore makes nu a single equilibrium atom delta_q. By Sections 1-3, q!=0, W(q)=0, U(q)!=0 and q is in the vortical closure. Equation (5) at the equilibrium gives DB(q)^T U(q)=rho U(q).

Otherwise nu(B=0)=0 and Section 4 applies. The set {DW=0} on the invariant zero-vorticity locus is invariant under the differentiated vorticity cocycle, so ergodicity gives a flat or nonflat alternative. The confirmed A433 and A467 classify the nonflat possibility in the present global helicity-free class: its backward spectrum would have to be

    {a/2,0,-3c-a/2}.

Comparison with Section 4 forces rho=-a/2, since rho<0 and 3c-rho>0. But A496 gives rho<=-a, with a>0, a contradiction. This excludes the nonflat alternative for every vortical equilibrium in this class, not only for rho<=-2a.

Thus DW=0 almost everywhere. By continuity it vanishes on supp nu, as does W. The support is in the vortical closure, and D(B cross W)=0 there. The confirmed A471, with the precise scope qualifications checked in A484/A497, applies to this compact whole-flow-ergodic measure. An aperiodic such measure has top backward exponent zero. Section 4 instead gives -rho>0. Therefore nu is a periodic-orbit probability. Its orbit has W=DW=0, U nonzero, and the rate is the same rho by (6). This proves the stated alternatives.

Neither the existence of invariant measures nor their classification rules out the compact set K. Both kinds of companion remain admissible under the audited results. A statement that K consists only of their orbits would require a separate pointwise argument.

## 6. Dependencies and source repairs

Used confirmed results: A048 for the W-flow; A413/A496 for the global rank identity, regular-level continuation and rho<=-a; A468/A478 for equilibrium data and origin exclusion; A433/A467 for nonflat measures; A471 with A484/A497 for the flat measure classification. Every use retains global zero helicity, uniform sublinearity, compact support and the vortical-closure premise. The source B32's line-versus-level equality and logarithmic-integrability rationale were repaired explicitly. Its conclusion about ergodic measures is retained, while its occasional pointwise description of the whole limit set is not certified. No numerical or formal computation was used.
