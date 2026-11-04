# Necessary witnesses for a nonzero helicity-free decaying profile

Status: A571 CONFIRMED after complete source, dependency and independent proof postreads. This is a necessary-structure theorem and a conditional contrapositive, not unrestricted nonexistence.

## 1. Exact global hypotheses and component rate

Fix2/5<c<1/2 and a finite real omega. Let U in C2(R3;R3),P in C1(R3) satisfy

    div U=0, [(1-c)I+omega J]U+DU(Ay+U)+grad P=0,
    U.curl U=0 everywhere, U(y)->0 uniformly as |y|->infinity,
    A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0).

Put B=Ay+U, W=curl U, a=1-2c, kappa=1+c, d=3c, nu=(1-c)/c, H=P+|U|^2/2+(Ay).U and g=U.B. Decay implies uniform sublinearity, so both carrier flow directions are complete. Select a closed ball Q with B(y).y>=b|y|^2 outside it, for some b>0. For the backward flow Psi of -B set K=intersection_(t>=0)Psi_t(Q). For a nonempty connected component E of O={W!=0}, set

    K_E=K intersect closure(E),
    Z_E=K_E intersect ({B=0} union {W=0}).

The exact confirmed A430 theorem makes K_E compact, nonempty and fully invariant. If Z_E is nonempty, let Gamma_E be the attained maximum of the largest backward Lyapunov exponent over compactly supported whole-flow-ergodic probabilities on Z_E; set it to minus infinity otherwise. The associated component derivative growth is max(a,Gamma_E), independent of the chosen admissible Q. The maximum is over a fixed E; no uniform margin across infinitely many components is asserted.

Call the optional strengthened hypothesis N: |U|<=C(1+r)^-nu and |DU|<=C(1+r)^(-nu-1). In the present global class, DU=O(sqrt r) implies N by A498,A476,A492 and the natural-tail estimates. N is not inferred from decay alone.

## 2. The witness theorem

If U is not zero, some E has Gamma_E>=2a. In Z_E there is one of the following objects, selected by a probability attaining an exponent at least2a.

Vortical equilibrium: a point z with B(z)=0,W(z)!=0. It has z!=0,u=U(z)!=0 and

    spec DB(z)={rho,kappa,-a-rho}, rho<=-2a.         (1)

Under N, its allowed rho values reduce to

    {-2(1-c)} union {-(k+3)c:integer k>=0,k<3nu-2}
                    union (-infinity,-(3-2c)].    (2)

Here k0,1 always occur in the listed candidate set, while k2 is included only forc<3/7. These are necessary candidates, not known profile realizations.

Irrotational equilibrium: a point z in closure(E) with B(z)=W(z)=0, z!=0,u!=0 and

    min Re spec DB(z)<=-2a.                        (3)

If K0=DW(z)!=0, the real covector eigenvalue rho in DB(z)^T u=rho u has these alternatives:

(i) The first family {rho,rho+kappa,-a-2rho}, rho>=a/2. In a small regular H-coordinate box, {W=0}={g=0}={H=H(z)}.

(ii) rho<=-2a, and vortical points on the local level H=H(z) accumulate at z. Both A469 families are initially allowed. Under N necessarily rho<=-2(1-c).

(iii) rho<=-2a, and W=0 on that level near z. Then K0=w u^T/|u|^2, w!=0, DB(z)w=(rho+kappa)w. This can belong to the first family; the second family {rho,(-a-rho)/2,(1+4c-rho)/2} permits it in this range only at rho=-1.

When DW(z)=0, (3) still holds. No full local classification or exclusion is supplied here; the flat Hessian and conditional higher-jet restrictions are A563, with their additional hypotheses.

Flat periodic orbit: a nonconstant periodic carrier orbit C in Z_E on which W=DW=0, B!=0,U!=0,g=0. There is a real constant rho with

    U(Phi_t x)=exp(rho t)D Phi_t(x)^(-T)U(x),
    Floquet multipliers={1,exp(rho T),exp((d-rho)T)},
    rho<=-2a or rho>=2-c.                          (4)

In the upper range both local invariant cylinders are irrotational and there is no nearby vortical point with g0. In the lower range the unstable cylinder is irrotational; every nearby Bernoulli loop on the stable cylinder contains a zero of W, and that entire stable cylinder is irrotational if rho<=-kappa. Under N there are no nearby vortical g0 points if -2(1-c)<rho<=-2a.

If every component has none of the above selected witness types, U=0 by contrapositive. In particular every nonzero profile in this class has a nonzero carrier equilibrium in the vortical closure or a flat periodic carrier orbit there. No pointwise classification of arbitrary limit sets is implicit.

## 3. Existence of a large-growth component and a maximizing measure

If W vanishes everywhere, div U0 implies Delta U0 componentwise. Since U decays, the mean-value formula for harmonic functions gives U0. Thus a nonzero U has at least one E. A432 at r2 states: if Gamma_E<2a for every E and helicity has one sign on each essential basin domain, then U0. Global helicity zero satisfies every such sign condition. Contraposition yields an E with Gamma_E>=2a.

This value cannot equal minus infinity, so Z_E is nonempty and A430's projective variational maximum gives a whole-flow-ergodic probability eta on Z_E attaining the top exponent. Its attainment proof is compact projective flow averaging and ergodic decomposition; it assumes neither compactness of the set of ergodic measures nor continuity of the Lyapunov exponent as a function of measure.

All support points lie in closure(E), hence in closure(O). This is precisely the hypothesis required by A467,A470,A471. It must not be omitted by replacing their statements with arbitrary flat-measure statements.

## 4. Classification of the selected probability

Both {B=0} and {W=0} are invariant. Ergodicity makes eta either an equilibrium atom or carried by {B!=0,W=0}. In the latter case A467 says a nonflat first vorticity jet has backward spectrum (a/2,0,-d-a/2), whose top is less than2a, while the other nonflat branch is impossible in this global helicity-free class. Hence the selected probability has DW0 almost everywhere. Continuity extends W=DW=0 to its support, so D(B cross W)=0 there.

A470 yields g0 on this invariant probability support. A471 gives backward spectrum(0,-rho,rho-d), including multiplicity, and says a positive top exponent forces a periodic measure. Since2a>0, we obtain C in(4). Its top is max(0,-rho,rho-d), so the threshold is exactly rho<=-2a or rho>=d+2a=2-c. There is no aperiodic selected flat measure.

The covector law is first supplied almost everywhere by A471 and extends to the periodic orbit by continuity. If U vanished at one point, this law would make it vanish everywhere on C. Then C would solve y'=Ay alone. But along this linear flow |y(t)|=exp(ct)|y(0)|, which has no nonconstant periodic orbit. Thus U!=0 on C. This justifies every nonvanishing hypothesis used by its later local restrictions.

If eta is an equilibrium atom at z, its exponents are the real parts of the eigenvalues of -DB(z). Therefore its selection immediately gives(3), whether or not DW vanishes. This is stronger than the source's min<=0 wording. A478 excludes z0 from the vortical closure; since B(z)=0 and A is invertible, u=-Az!=0. A473 gives the weaker min<=0 condition independently but is not the sharp bound for this selected witness.

## 5. Equilibrium algebra and the natural-tail restrictions

If W(z)!=0, openness and connectedness show z lies in E itself. A468 gives the real spectrum in(1), with top backward exponent max(-rho,a+rho). The threshold2a permits rho<=-2a or rho>=a. A496, valid with global helicity and sublinearity for all finite omega, gives rho<=-a and eliminates the latter branch. This proves(1).

Under N, A517 provides escaping points on the regular vortical zero-g sheet when rho<-a; the selected rho<=-2a meets that strict premise. A518,A534 give its exact scattering-sheet identities, and A551 applies to these same points with mu=-a-rho. It gives mu in {1} union {1+(k+5)c-2:k<3nu-2} union[2,infinity). Solving for rho gives(2). No rho=-a case enters this selected branch, and no moments are inferred at that exceptional nonwitness rate. Since3nu-2=3/c-5 lies in(1,5/2), the only possible integers are0,1 and, forc<3/7,2.

If W(z)=0 and K0!=0, A469 gives two real spectral families without assuming diagonalizability. For family I the three backward rates are -rho,-rho-kappa,a+2rho. The middle one is always smaller than the first, so the threshold is rho<=-2a or rho>=a/2. For family II the rates are -rho,(a+rho)/2,(rho-(1+4c))/2; the last is smaller than the middle by kappa. Its threshold is rho<=-2a or rho>=3a. A522 excludes positive rho in family II and gives the exact regular separating box for positive rho in family I. This proves(i) and leaves the lower ranges.

At K0!=0 one component of W has nonzero derivative. Its zero set contains {W0} and is a C1 surface, so the vortical set is dense in a box. Rank therefore extends throughout it and H is a submersion; A537 supplies g=G(H), G'(H(z))=-rho/a. Thus the regular level through z is zero-g. Either vortical points on it accumulate at z, or W vanishes on a whole level piece. In the first case A537 and A536 give rho=-a or rho<=-2(1-c) under N; the selected threshold excludes -a. In the second case the normal derivative has the rank-one form in(iii). Its nonzero image has eigenvalue rho+kappa. In family II this can equal (-a-rho)/2 only when rho=-1, or (1+4c-rho)/2 only when rho=-a/3. The latter exceeds -2a and is not selected. This proves the exact listed alternatives.

## 6. Periodic cylinders, later refinements and report precision

For(4), A474 supplies the unstable cylinder and the lower stable-cylinder statements. In the upper range2-c>3c, so A523 supplies the second irrotational cylinder as well. A537 excludes nearby vortical zero-g points whenever rho>-a; hence in the whole upper range. Under N it excludes them for -2(1-c)<rho<-a. Since -2a<-a, this gives the stated lower interval with its endpoint included.

CO31's main necessary theorem and contrapositive therefore follow with no added assumption. Its selected equilibrium bound can be sharpened to(3), including DW0. Its phrase 'nothing beyond ... min<=0 is known' should not be used: the selected exponent already gives min<=-2a and A563 supplies further pointwise identities. Its repeated symbol p for the decay exponent and carrier point should be separated, as nu and z here.

Subsequent confirmed refinements are not needed for the core theorem: A559-A560 exclude axisymmetric, nonzero-pitch screw and analytic flat periodic witnesses at their exact local/global hypotheses, and restrict smooth flat witnesses to infinite flatness and two zero cylinders. A563-A566 give higher-regularity equilibrium restrictions and finite jets, never exact C2 Euler constructions. A568 gives a controlled-nodal conditional exclusion of lower escaping sheets. A570 proves full nonexistence under N and axisymmetry of the actual velocity tail, stronger than merely deleting their lower rates. These supersede the source's old SUBMITTED addendum but do not alter its core proof.

## 7. Verification and scope

The entire actual configured-model CO31 assembly and its cited verdicts were read. The complete A430 component-rate and attainment proof was reread, including its closure premise, while A467-A471,A473,A478,A484 and the exact newer restrictions were compared at their recorded scopes. The arguments above reconstruct every combination and every threshold. No numerical computation is needed. Existing agent model collaboration is configured with the primary model; no new client or provider attestation is claimed.

The theorem does not exclude either general witness family, derive derivative control from decay, or treat general sign-changing helicity. No finite-energy or symmetry assumption is hidden in its base statement. The optional natural bounds and later tail-symmetry theorem are explicitly separate.
