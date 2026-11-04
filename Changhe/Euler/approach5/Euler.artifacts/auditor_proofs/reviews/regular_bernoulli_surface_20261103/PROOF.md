# A regular Bernoulli level carrying an exceptional measure

Status: independent reconstruction of LIT95, checked against the focused configured-model review. The covector condition is now supplied by A444 under exactly the stated hypotheses. Final verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). No negative-branch periodicity or automatic growth bound follows from the regular-surface argument alone.

## 1. Exact assumptions and conclusions

Let U in C2(R3;R3), P in C1 solve the full incompressible rotating Euler profile equation for 0<c<1/2 and omega in R. Assume uniform U=o(|y|) and U.curl U=0 everywhere. Set

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c,
    H=P+|U|^2/2+(Ay).U, g=U.B.

Let mu be a whole-flow-ergodic carrier-invariant probability with compact support S, satisfying almost everywhere B!=0,W=0,DW!=0 and D(B cross W)=0. A433 gives backward spectrum (kappa,0,-d-kappa) and image DW=R B there.

A444 supplies COV: one constant rho in {-kappa,d+kappa} satisfies grad g=rho U at every point of S where U!=0; any point of S with U=0 is the spatial origin and a carrier equilibrium. A445 excludes rho=d+kappa in this global helicity-free class. We retain rho in the computations to exhibit both formal alternatives, but the live conclusion has rho=-kappa.

Then H has a constant value h on S. With

    V={B!=0,U!=0,DW!=0,grad H!=0},

the regular surface {H=h} intersect V has exactly one connected component M of full mu measure. On that whole component,

    g=0, grad g=-(rho/a)grad H,
    BH=0, grad(BH)=rho grad H.

For every local carrier flow map Phi_s whose whole segment stays in M,

    D Phi_s(x)^T grad H(Phi_s x)=exp(rho s)grad H(x),
    J_M Phi_s(x)=exp((d-rho)s)|grad H(Phi_s x)|/|grad H(x)|.

In particular the measure nu_M=dA/|grad H| satisfies nu_M(Phi_s E)=exp((d-rho)s)nu_M(E) whenever the displayed local map is defined on E. The component M is noncompact, and

    S outside M is contained in {B=0} union {DW=0}.

The backward tangent spectrum on TM is (0,-d-kappa) if rho=-kappa and (kappa,0) if rho=d+kappa. These are exact geometric conclusions; a noncompact surface may still contain a compact invariant set or a periodic orbit.

## 2. Regularity and the constant level

The Lamb identities are grad H=-aU+B cross W and BH=-ag. They give H C2, and g is C2 from its definition. Global sublinearity makes the C2 carrier complete by its at-most-linear growth. The support is invariant in both time directions.

Continuity extends W=0 and D(B cross W)=0 to S. At a typical point, differentiating U.W=0 gives U.DW(v)=0. Since image DW=R B, g=0 almost everywhere and then everywhere on S. Thus BH=0 on S. H is constant along each full orbit there, so ergodicity makes it constant almost everywhere. Continuity on the support gives the single constant h on all of S. Also grad H=-aU on S.

## 3. Why the rank relation holds on an open neighborhood

At any point with DW!=0, select one scalar component of W and one coordinate derivative which is nonzero. That derivative stays nonzero in a small neighborhood. The scalar zero set there is a regular surface, and the full zero set of W is contained in it. Therefore {W!=0} is dense in that neighborhood. In particular V lies in the interior of closure{W!=0}.

The confirmed global-helicity rank identity A413, dH wedge dg=0 on {W!=0}, consequently holds throughout V by continuity. Since grad H!=0 there, C2 submersion coordinates give g=f(H) in each local coordinate box. The one-variable f is C2. Thus both g and the scalar q defined by grad g=q grad H are locally constant on a regular level patch. Equivalently q is C1, and symmetry of Hess g implies dq wedge dH=0. On each connected component of the level, g and q are constant, since connected manifolds are path connected.

## 4. Choosing one component without a completeness assumption on it

The set S intersect V has full mu measure: the hypotheses give B and DW nonzero almost everywhere, COV gives U nonzero there, and grad H=-aU. It is invariant. A regular carrier orbit cannot reach an equilibrium in finite time by uniqueness. On W=0, the exact first-jet Cauchy law preserves DW!=0. The COV zero restriction prevents U from vanishing on a nonstationary orbit, and the same follows for grad H.

The second-countable regular level surface has at most countably many connected components. Each S intersect M_i is Borel and invariant, since an orbit is connected and cannot jump components. Ergodicity assigns each zero or full measure; countability and full measure of their union select exactly one M. On S intersect M we know g=0 and q=-rho/a. Local constancy extends both to all of M. Therefore B is tangent to M, and differentiating BH=-ag gives grad(BH)=rho grad H there.

Because mu(M)=1, S is contained in closure M. If p lies in S intersect V, choose a submersion box Q around p inside V, so the full slice {H=h} intersect Q is connected. This slice meets M because M has full measure and p belongs to the support, hence belongs to the same connected component. Thus S intersect V is contained in M. At any point of S outside M, either B or DW vanishes, or U or grad H vanishes. The latter two conditions imply U=0 and hence B=0 by COV. This proves the stated containment. The extension of g and q is along M only, not to other components or nearby H levels. Tangency gives only local invariance for arbitrary points of M; it has not established completeness on this noncompact component.

## 5. The surface measure and noncompactness

Let F_s=D Phi_s along a trajectory staying in M. Pulling back the covector dH and differentiating yields

    d/ds[F_s^T grad H(Phi_s x)]
       =F_s^T grad(BH)(Phi_s x)
       =rho F_s^T grad H(Phi_s x).

This proves the covector identity. Since div B=d, det F_s=exp(ds). The codimension-one area formula for n=grad H/|grad H| is

    J_M Phi_s=det F_s |F_s^(-T)n(x)|.

Solving the covector identity for F_s^(-T)grad H(x) gives the claimed area Jacobian and, after division by |grad H(Phi_s x)|, the exact weighted-area scaling.

If M were compact, it would be an embedded C2 surface without boundary. Its tangent C1 vector field would be complete and each Phi_s would map it onto itself. The measure nu_M(M) would be finite and positive, because |grad H| has a positive minimum on compact M. The scaling would force exp((d-rho)s)=1 for every s. But d-rho equals d+kappa or -kappa, both nonzero. This proves that M is noncompact. It does not imply S is noncompact.

## 6. Tangent Lyapunov exponents

On S, TM=ker dH=U-perpendicular. Since W=0, DU is symmetric. Differentiating g=U.B and using COV gives

    dU/ds=(rho I-DB^T)U,
    U(Psi_t x)=exp(-rho t)D Psi_t(x)^(-T)U(x).

The vector U along a full orbit in compact S is bounded in both directions. Apply the two-sided Oseledets rule to this scaled dual cocycle. A nonzero dual component for primal exponent lambda has rate -rho-lambda; boundedness in both directions forces that rate to vanish. When rho=-kappa, U as a covector annihilates E0+E-, and when rho=d+kappa it annihilates E+ +E0. This does not say that the Euclidean vector U lies in the corresponding primal Oseledets line. Its kernel has the two remaining exponents. No integrability of log|U| or uniform lower bound for |U| on S is assumed; the tempered projections and two-sided boundedness are the same argument already checked in A433.

## 7. Precisely what the inspected surface-flow source does not supply

The actual Araujo manuscript arXiv1806.05245v3 was inspected on pages1 and4-8. Page4 sets a compact finite-dimensional Riemannian ambient manifold and a C1 field inwardly transverse to any boundary. Page5 defines the full transverse linear Poincare cocycle. Theorems E and F on page7 explicitly assume hyperbolic equilibria. Strictly negative liminf of its top rate gives a sink-basin or codimension-one saddle-accumulation alternative; the limsup version gives a sink basin. Theorem G on pages7-8 gives the corresponding inverse-cocycle alternatives. Theorem D concerns negativity of the entire derivative cocycle, including the flow direction, and is a different condition.

Those are statements and scope, not independently certified full proofs. Only the cited pages were read for this audit. The title page has revision11May2020 and internal date26July2021; no date discrepancy is silently normalized. Its informal zero-flow-exponent sentence and periodic-hyperbolicity wording are not used.

The regular part of compact S may approach B=0 or DW=0 outside M. Neither a compact smooth completion of M nor hyperbolicity of all added or existing equilibria has been established. Even the condition S subset M would not by itself make M compact. Therefore the negative tangential exponent above does not verify the inspected source hypotheses, and no negative-rho periodicity conclusion is obtained by citation. The main sign-changing-helicity class is outside the assumptions from the start.

Dependencies: the exact Lamb and Cauchy identities, A413, A433, A444 and A445. For the remaining rho=-kappa alternative, forward weighted area scales by exp((1+4c)s) and the backward tangent exponents are (0,-1-4c). No pressure normalization, far-field derivative estimate, numerical computation or new remote model call enters this proof. The omega=0 global setting is already excluded by A010, and no conclusion about the unresolved sign-changing-helicity class is supplied.
