# Second-order moments in the vorticity direction

## Statement and hypotheses

Let U in C2(R3;R3) and P in C1(R3) solve

    (1-c)U + B dot grad U + omega J U + grad P = 0,
    div U = 0,
    B = (cI-omega J)y + U,

where c and omega are finite real constants and J(x,y,z)=(-y,x,0). The equation implies P is C2. Write G=DU, S=(G+G^T)/2, A=(G-G^T)/2 and Omega=curl U. On Z={Omega!=0}, define

    n=Omega/|Omega|, sigma=n dot S n,
    beta=S n-sigma n, p_nn=n dot D2P n.

Then

    B dot grad sigma = |beta|^2-sigma^2-sigma-p_nn.       (1)

Let mu be a compactly supported probability invariant under the B flow, and assume mu(Z)=1. No positive lower bound for |Omega| on the support is required. Then

    integral sigma dmu = 1,
    integral (|beta|^2-p_nn) dmu
        = 2 + integral (sigma-1)^2 dmu.                  (2)

Separately, for every compactly supported B-invariant probability, including measures charging Omega=0,

    integral [S+S^2+A^2+omega(JS-SJ)+D2P] dmu = 0         (3)

as a componentwise matrix equality. No decay, pressure normalization, integrability at infinity, restriction on omega, or sign condition on c is used in these statements.

## Derivation of the pointwise identity

Differentiate the momentum equation. Since DB=cI-omega J+G, cancellation of the two scalar coefficients gives

    B dot grad G = -G-G^2-omega(JG-GJ)-D2P.

Taking symmetric parts gives

    B dot grad S = -S-S^2-A^2-omega(JS-SJ)-D2P.           (4)

The vorticity equation is

    B dot grad Omega = (G-I-omega J)Omega.

The relation Omega=curl U gives 2Av=Omega cross v. In particular An=0, so Gn=Sn and

    B dot grad log|Omega|=sigma-1,
    B dot grad n=beta-omega Jn.                          (5)

The vanishing An is the essential coupling in this calculation. An independent transported eigenfield W does not in general have this property.

Differentiate sigma using (4)-(5). Since beta is perpendicular to n,

    2(beta-omega Jn) dot Sn
       = 2|beta|^2-2omega(Jn) dot Sn,
    n dot S^2 n = sigma^2+|beta|^2,
    n dot A^2 n = 0,
    n dot (JS-SJ)n = -2(Jn) dot Sn.

The rotation terms cancel exactly, leaving (1).

For completeness, if R denotes the momentum residual with all terms on the left, the same calculation has the additional terms

    2 (curl R) dot beta/|Omega| + n dot (DR)n.

This statement is an algebraic identity wherever the displayed derivatives exist; a random polynomial check is not needed to prove it.

## Invariant integration, including support touching Omega=0

All of sigma, beta and p_nn are bounded on Z intersect supp mu, because n is a unit vector and G,D2P are continuous on a compact set. Formula (1) therefore bounds B dot grad sigma there. Although sigma need not extend continuously across Omega=0, Z is invariant and has full mu measure. For each finite t, the fundamental theorem of calculus on the invariant Z orbits and Fubini give

    integral [sigma(Phi_t x)-sigma(x)] dmu(x)
        = integral_0^t integral (B dot grad sigma)(Phi_s x) dmu(x) ds.

Invariance makes the left side zero and the inner integral independent of s. Thus integral B dot grad sigma dmu=0. This is the needed repair to the shorthand claim that sigma is C1 on the entire support.

To integrate the first identity in (5), put f=log|Omega| on Z. It is finite there but need not be integrable. Choose bounded C1 truncations T_N with |T_N'|<=1 and T_N'(r) tending to 1 for every finite r. For example, take T_N(r)=N T(r/N), where T is a bounded C1 function with T'=1 near zero and |T'|<=1. The orbit derivative of T_N(f) is T_N'(f)(sigma-1), uniformly bounded on supp mu. The same invariant integration gives

    integral T_N'(f)(sigma-1) dmu=0.

Dominated convergence yields integral sigma dmu=1. Integrating (1), and using sigma^2+sigma=(sigma-1)^2+3sigma-1, proves (2). The condition that log|Omega| be finite almost everywhere is automatic from mu(Z)=1 and is not an extra integrability hypothesis.

## The componentwise matrix identity

Each Cartesian component S_ij is a C1 scalar function and is bounded, together with its orbit derivative, on the compact invariant support. Therefore integral B dot grad S_ij dmu=0. Integrate (4) componentwise to obtain (3).

The fact that n changes along an orbit has no bearing on this step, which never differentiates n. Consequently the assertion in THEORY_B Section 6d, Remark (4), that this matrix identity is invalid is false. The scalar identity (1) and the directional moment (2) remain valid.

## Equality example and scope

For an exact axial affine profile with nonzero constant vorticity in the z direction and S=diag(s,-1-s,1), one has sigma=1 and beta=0. Equation (4) in the z direction gives P_zz=-2, so the integrand in (2) is 2 pointwise. Any compact invariant probability of this profile obeys equality with zero variance. Such affine fields do not decay and are not counterexamples to the main conjecture.

Equation (2) is a necessary condition. The pressure Poisson equation fixes the trace of D2P, not its directional component p_nn. No sign bound on the latter, and no Liouville conclusion in the target interval, follows from this calculation alone.

## Verification evidence and dependencies

This proof is a direct exact differentiation and integration argument. It uses only the displayed profile equation, the identity 2Av=(curl U) cross v, elementary truncation, and invariance of mu. No numerical computation or external theorem is used. B16's symbolic trials are supplementary evidence and are not part of the proof.

## Fixed directions and the rotation correction

For any compactly supported invariant probability, integration of the vorticity equation also gives

    integral (S Omega-Omega-omega J Omega) dmu=0.

Here A Omega=0 pointwise. Taking the quadratic form of (3) in a fixed unit vector e gives

    integral e dot D2P e dmu
      = -integral [e dot S e+|Se|^2-|Omega cross e|^2/4
                   -2omega(Je) dot Se] dmu.                         (6)

Both equalities are valid without any nonvanishing assumption on Omega.

Suppose now mu(Z)=1 and n=e almost everywhere. Since the full-measure set on which this holds is invariant up to null sets, the continuously differentiable function n along almost every orbit is constant. Equation (5) implies

    beta=omega Je,                                                   (7)

not beta=0 in general. Indeed, combining (2) and (6) gives

    2 integral [|beta|^2-omega(Je) dot beta] dmu=0,

which is precisely consistent with (7). The strain-eigenvector conclusion is valid when omega Je=0, in particular when the fixed direction is the rotation axis or omega=0.

Here is a counterexample to the unrestricted constant-direction conclusion. Choose arbitrary finite c, any nonzero omega, and define

    S = [[1,omega,0],[omega,0,0],[0,0,-1]],
    A = [[0,0,0],[0,0,-1],[0,1,0]],
    G=S+A, U(y)=Gy, K=G+G^2+omega(JG-GJ).

The trace of G is zero, curl U=2e_1 and

    S Omega=Omega+omega J Omega.

For a trace-free symmetric S and A v=Omega cross v/2, the antisymmetric part of K is the cross-product matrix associated with

    (Omega-S Omega+omega J Omega)/2.

It therefore vanishes. Thus K is symmetric, and P(y)=-y dot K y/2 makes (U,P) an exact smooth profile. The compact probability delta_0 is B-invariant. On its support, and in fact everywhere,

    n=e_1, sigma=1, beta=omega e_2,
    n dot D2P n=omega^2-2.

The scalar identity and fixed-frame identity both hold, while beta is nonzero. This affine example fails decay and sublinearity; it refutes precisely the asserted local moment consequence, whose hypotheses did not require either condition. It makes no counterexample claim for the main conjecture.
