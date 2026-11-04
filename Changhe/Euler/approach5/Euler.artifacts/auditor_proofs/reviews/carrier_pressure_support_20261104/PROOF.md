# Independent audit of pressure support at a carrier equilibrium

Status: CONFIRMED at the exact conditional scopes A2770-A2772; unrestricted applicability OPEN A2773. This extends a confirmed conditional theorem by an exact coordinate transformation. It adds no decay-only conclusion.

## 1. Exact statement and dependency

Let Jx=e3 cross x, A=cI-omega J and L=(1-c)I+omega J, for real c and omega. A full profile on an open domain has U in C2, P in C1 and

    LU+DU(Ay+U)+grad P=0, div U=0.                    (1)

Its carrier is B(y)=Ay+U(y). At any carrier equilibrium a, set q=U(a), so Aa+q=0. Define on the translated domain

    V(x)=U(a+x)-q,
    Q(x)=P(a+x)-P(a)-grad P(a).x.                    (2)

Then (V,Q) satisfies the same equation, V(0)=0, Q(0)=0 and grad Q(0)=0. All velocity derivatives and pressure Hessians are carried over by translation.

For a global profile with c>0, assume additionally that for some r>0

    P(a+x)>=P(a)+grad P(a).x  for |x|<r.             (3)

Then U is constant if |omega|<=sqrt(2). For arbitrary omega the same follows if DU(a)=0. In either case U=q=-Aa and grad P=-Lq. If U tends to zero at infinity, then U=0, P is constant and a=0.

The only global dependency is confirmed A2748: a global C2/C1 full profile with c>0, central velocity zero and a local pressure minimum at zero vanishes when |omega|<=sqrt(2), or for arbitrary omega when its central derivative is zero. Its complete proof is auditor_proofs/reviews/pressure_minimum_rotation_20261104/PROOF.md at the agent root, Sections4-6. It requires no decay or global flow completeness.

The local conclusion, for all real c and omega, is that if D2P(a) is positive semidefinite and W=curl U(a) is nonzero, then omega^2|JW|^2>2|W|^2. If W=0 under this positive-semidefinite Hessian assumption, then DU(a)=0. The supporting-plane premise (3) cannot be replaced just by a positive semidefinite Hessian, even for a global profile with U(a)=DU(a)=0.

## 2. Exact translation of the full equation

Since B(a)=0, equation (1) at a gives grad P(a)=-Lq. For y=a+x, Aa=-q gives

    Ax+V(x)=Ay+U(y)=B(y),
    grad Q(x)=grad P(y)+Lq.

Thus

    LV+DV(Ax+V)+grad Q
      =L(U(y)-q)+DU(y)B(y)+grad P(y)+Lq=0.

The divergence and all asserted derivative identities are immediate differentiations of (2). The equation expresses grad P as a C1 field, so P and Q are C2; Hessians are legitimate under the stated C1 starting assumption. Also (3) is exactly Q(x)>=Q(0)=0 near zero.

For an arbitrary point a the transformation V_a(x)=U(a+x)+Aa, Q_a(x)=P(a+x)-P(a)-(LAa).x also preserves (1), by the same cancellation. But V_a(0)=B(a), so central-zero theorems do not apply to it unless a is a carrier equilibrium. In the equilibrium case this equals (2), because grad P(a)=LAa. The affine pressure adjustment is fixed by the full equation, not an independent pressure gauge.

For 0<c<1, both A and L are invertible: their vertical eigenvalues are c and 1-c and their horizontal determinants are c^2+omega^2 and (1-c)^2+omega^2. If an equilibrium is also an ordinary local pressure minimum, grad P(a)=0 gives Lq=0, then q=0 and Aa=0, hence a=0. A supporting tangent plane allows a nonzero pressure gradient and is the appropriate translated premise.

## 3. Conditional global consequence

By Section2, the translated pair meets every hypothesis of A2748 stated in Section1. In the small-rotation case A2748 gives V=0. In the arbitrary-rotation case DV(0)=DU(a)=0 supplies its alternative hypothesis and gives the same result. Therefore U=q everywhere. Equation (1) reduces to grad P=-Lq and the equilibrium identity gives q=-Aa. If decay is assumed, q=0; because c>0 implies A invertible, a=0. No extra characteristic-completeness premise is inserted.

The derivative-zero alternative also shows that any nonconstant global profile satisfying (3) must have DU(a) nonzero. Section4 below then shows that it must have W nonzero as well. Consequently such a nonconstant profile must obey the strict angular inequality. This is a necessary condition within the stated supporting-plane class only.

## 4. Local center algebra at the equilibrium

Set M=DU(a) and H=D2P(a). Differentiating (1) at a eliminates the D2U term because B(a)=0. The result is

    H=-LM-M(A+M)=-M-M^2-omega[J,M],
    tr M=0, tr H=-tr(M^2).                         (4)

Taking curl in (1) gives Omega+B.grad Omega+omega JOmega-DU Omega=0. At a it becomes MW=W+omega JW. Substitute this in (4): the two terms involving M(JW) cancel and give

    HW=-2W-3omega JW-omega^2J^2W,
    W.HW=-2|W|^2+omega^2|JW|^2,
    (JW).HW=-3omega|JW|^2.                         (5)

When H is positive semidefinite and W is nonzero, the second line is nonnegative. Equality would force HW=0 by diagonalization of H, while also forcing omega and JW nonzero. The last line would then contradict HW=0. This proves the strict inequality. When W=0, M is symmetric and (4) gives 0<=tr H=-|M|_F^2, so M=0. None of these local deductions uses (3) away from a.

## 5. Full-profile counterexample to a Hessian-only replacement

Let X=(x,y,z), phi(X)=x^3-3xy^2, and define

    U=grad phi=(3x^2-3y^2,-6xy,0),
    P=-(1-2c)phi-(AX).grad phi-|grad phi|^2/2.       (6)

The polynomial phi is harmonic, so div U=0 and DU is symmetric. Differentiation gives

    grad[(AX).grad phi]=A^T U+DU AX,
    grad(|U|^2/2)=DU U,
    L-A^T=(1-2c)I.

Substitution of these three identities into (1) cancels every term. Thus (6) is an entire full profile for all real c and omega, not merely a kinematic Poisson pair.

Its quadratic velocity gives U(0)=DU(0)=0 and B(0)=0. Its pressure has only homogeneous degrees three and four, so grad P(0)=D2P(0)=0. Euler's homogeneous identity gives

    P=-(1+c)phi+omega(JX).grad phi-|U|^2/2.

At X=(t,0,0), the rotation term vanishes and

    P(t,0,0)=-(1+c)t^3-(9/2)t^4.

For c>0 this is negative for t>0 and positive for all sufficiently small negative t. Since P(0)=grad P(0)=0, no local supporting tangent plane exists at zero. Hence positive semidefinite H, even H=0 and U=DU=0 there, does not suffice for the global conclusion of Section3. The velocity grows quadratically on this line, so this is not a decaying counterexample.

## 6. Verification boundary

At the initial reconstruction, all six source sections and all six independent sections were read. The translation, center identities and counterexample are checked directly in the full equation. The one global dependency is the already confirmed A2748 with exactly its stated hypotheses. No pending LIT326-LIT328 result, numerical calculation, external manuscript, formal build or new client is used. The existence of a carrier equilibrium with the supporting-plane property in the unrestricted decaying class remains open. The comparison was pending at that reconstruction; Section7 records its completion.

## 7. Completed comparison and exact scope (2026-11-04T02:20:45.560635+00:00)

All four items, W1-W3 and eleven checks of the existing configured model coordinator comparison were read in full. The checks were not rerun. Actual provider execution is independently unattested. Sections1-6 were reread against the unchanged source 3bf3166f2cf9a3a844961f3270f09a10c916064ffddf5e8f1155c10eafa4479b. No mathematical gap was found in the claimed results.

There is a sign-clarity defect in comparison item1, not in its check log or the source proof. Without assuming equilibrium, the exact residual of the pair (2) is

    residual(V,Q)(x) = residual(U,P)(a+x)
                       -DU(a+x)(Aa+q)-Lq-grad P(a).

Indeed Ax+V=B(a+x)-(Aa+q), LV=LU-Lq, and grad Q=grad P-grad P(a). Thus both last terms have minus signs, or all three terms must be grouped under a single minus sign. At equilibrium Aa+q=0 and grad P(a)=-Lq, so they cancel. The comparison's log states this correct formula. The theorem does not rely on the defective typography.

Optional W2 extends the counterexample's failure of a supporting plane to every real c: when c is not -1, take t of the sign of 1+c to obtain a negative cubic leading term; when c=-1, the line value is -(9/2)t^4<0. The full polynomial construction is already valid for every real c and omega. The conditional global theorem still assumes c>0, and no extension of that theorem is inferred.

A2770 confirms the transformation and the local positive-semidefinite Hessian consequences. A2771 confirms global rigidity under the explicitly stated supporting-plane and rotation or derivative hypotheses. A2772 confirms the entire growing counterexample to a Hessian-only substitution, including the just-proved all-real-c observation. A2773 leaves unrestricted decaying-profile applicability open. No existence of a carrier equilibrium with pressure support, no pressure normalization at infinity and no new global completeness assumption is supplied.

## 8. Source and comparison revision check

At 2026-11-04T02:26:04.777051+00:00, the complete revision from the archived submission was read. The source revision records A2770-A2773, updates the dependency status and supplies the already checked all-real-c countertest extension. Its new Section7 contains the correct general residual with minus signs on both Lq and grad P(a). The existing coordinator comparison now states the same grouped residual explicitly. Its old sign-clarity defect is repaired; the source theorem and proof equations are unchanged. The exact source hash is 983f4a83385d243d5a0532ce78a7bd2d82c3ff3e621644c22526abbf5211793d; both versions and their diff are retained under verification. A2784 confirms only these revision transfers.
