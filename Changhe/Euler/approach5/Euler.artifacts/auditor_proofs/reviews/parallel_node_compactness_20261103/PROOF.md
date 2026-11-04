# Compact parallel equilibrium curves and exclusion of regular vortical nodes

Status: CONFIRMED A894-A897 with the exact global helicity and natural-decay hypotheses below. The conclusions at critical nodes and the decay-only conjecture remain OPEN, A898.

## 1. Exact statement and dependencies

Fix 2/5<c<1/2 and any finite real omega. Define Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Suppose U belongs to C2(R3;R3), P belongs to C1(R3), and for one finite constant C,

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Let V be the actual C1 scattering tail, W=curl V, and k(z)=(Az).V(z) on R3 minus {0}. Then

    k(z)=0 and dk(z)!=0 imply W(z)=0.                  (1)

Here omega has no size or nonzero restriction. The global helicity and derivative hypotheses are additional premises, not conclusions from bare velocity decay. Statement (1) leaves vortical critical nodes k=dk=0 untreated.

We use the independently checked nodal sheet theorem A810-A818, parallel product and boundary analysis A865-A868, pressure flatness A878-A881, and Stokes exclusion A883-A886. Their standalone arguments are in the team records, in the team records, in the team records, and in the team records. The bounded vortex-half endpoint theorem, including its rho=-a boundary case, is proved in the team records, A658-A659. Below we prove the remaining compactness step and spell out its exact use of these dependencies.

Write B=Ax+U, Omega=curl U. Their complete flows are Phi and Gamma. Completeness follows from the linear growth of B and boundedness of the C1 field Omega. Let K be the compact forward-bounded B core, E=R3 minus K, Xi:E to R3 minus {0} the actual C1 scattering diffeomorphism, K_Omega the complete Gamma lines contained in K, and O=R3 minus K_Omega. The function L in C1(O) extends k composed with Xi and obeys L(Phi_t y)=exp(-at)L(y) and L(Gamma_s y)=L(y).

Normalize pressure by its actual limit Pinf and set

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2, g=U.B=H-Q.

The equation makes these functions C2. For any connected component M of {L=0,dL!=0,Omega!=0}, the sheet theorem gives U=b grad H for one nonzero spatial constant b, and B cross Omega=(1+ab)grad H. The nonparallel case 1+ab!=0 is already excluded by A885. We assume b=-1/a until Section 6.

## 2. Closure identities and the possible missing points

For the parallel sheet let P0={y in M:B(y)=0}, Cbar=closure_R3(M) and C0=closure_R3(P0). The parallel product theorem gives a connected embedded C1 curve P0 without boundary, M diffeomorphic to P0 times R by Gamma, and

    DB Omega=kappa Omega, DB^T U=-aU,
    spec(DB)={0,kappa,-a} on P0.                       (2)

The tangent line to P0 is ker DB. Because B=0, |y|<=||U||_infinity/c on P0; hence C0 is compact. We do not infer that P0 itself is closed or compact from this bound.

Pressure flatness gives, on the entire Cbar,

    H=g=0, dg=dH, U=-grad H/a, U!=0,
    D2Q=0, 2|sym DU|^2=U.curl Omega.                  (3)

In particular no point of Cbar has Omega=D Omega=0: such a point has DU=0 by the last identity and Omega=0. Then dg=A^TU and dH=-aU. Their equality implies (c+a)|U|^2=(1-c)|U|^2=0, contrary to U!=0.

Take q in C0 minus P0. By continuity B(q)=0, U(q)!=0, DB(q)^TU(q)=-aU(q), and the characteristic polynomial in (2) is unchanged. Suppose Omega(q)!=0. The entire Gamma line of q lies in Cbar, since Cbar is invariant under this complete continuous flow. Parallelism and the covector identities also extend there. If either vortex half were contained in K, A658-A659 at rho=-a would give its finite limiting equilibrium qstar in Cbar with Omega(qstar)=D Omega(qstar)=0, contradicting (3). Both signs therefore meet E, so q belongs to O. Continuity of L and dL there gives L(q)=0 and dL(q)=dH(q)!=0. A connected component is closed in its ambient regular vortical zero set, so q belongs to M, and then to P0, a contradiction.

Consequently every missing point satisfies

    B(q)=Omega(q)=0, D Omega(q)!=0, U(q)!=0,
    spec DB(q)={0,kappa,-a}.                           (4)

This is a statement about the closure of this particular curve. It is not a classification of all irrotational equilibria.

## 3. The first vorticity derivative fixes an orientation

Fix a missing point q and abbreviate F=DB(q), D=DU(q), u=U(q), K1=D Omega(q). The bracket identity is D Omega B-DB Omega=-kappa Omega. Its first-order expansion at B=Omega=0 gives

    F K1-K1 F=kappa K1.                               (5)

Only C1 regularity of Omega is needed for this expansion. Since F has three distinct real eigenvalues {0,kappa,-a}, the only pair of eigenvalues whose difference is kappa is kappa minus 0. Thus K1 maps the zero eigenspace into the kappa eigenspace and kills the other two eigenspaces. It is nonzero by (4).

Let n=u/|u| and choose a unit t in ker F. Since F^Tu=-au, both the zero and kappa eigenlines are perpendicular to n. Set e=n cross t and choose a unit kappa eigenvector v with v_e=v.e>0. The two eigenlines are distinct, so this choice is possible. Write v=v_t t+v_e e and K1 t=d v. Then d!=0 and K1 v=0 gives

    K1 e=-(v_t/v_e)d v,
    n.curl Omega=(K1 t).e-(K1 e).t=d/v_e.              (6)

There is no missing normal derivative in the last equation: the normal component of curl uses precisely these two tangential derivatives. At q, D is symmetric since Omega(q)=0. It is nonzero, because otherwise F=A would have every eigenvalue of real part c>0, inconsistent with (4). Therefore (3) and (6) give the strict sign

    d=2|D|^2 v_e/|u|>0.                              (7)

This sign is independent of the sign or magnitude of omega. Reversing t also reverses e and the selected v, leaving the conclusion consistent.

On P0 define the oriented unit tangent T by

    U.(T cross Omega)>0.                             (8)

The expression cannot vanish: T spans the zero eigenline, Omega the distinct kappa eigenline, both perpendicular to U. The center eigenline is a C1 line bundle because DB is C1 with distinct fixed eigenvalues. Condition (8) selects exactly one of its two unit vectors, and these local C1 choices agree on overlaps. This defines a global C1 orientation without assuming that the two tangential eigenlines are orthogonal.

## 4. A missing point cannot be a forward accumulation point

At q choose a fixed linear map Pi:R3 to R2 with rank(Pi F)=2. Its kernel on F is precisely ker F. The C2 implicit-function theorem applied to Pi B supplies a C2 arc gamma:(-delta,delta) to R3 with gamma(0)=q and gamma'(0)=t, containing all local zeros of B. In implicit coordinates one may choose a cylinder whose Pi B zero set is exactly this arc, meeting the cylinder boundary only at its two parameter ends. No claim is made that the entire arc consists of B zeros.

Taylor expansion at q, followed by (7), gives

    Omega(gamma(s))=s d v+o(|s|),
    U(gamma(s)).(gamma'(s) cross Omega(gamma(s)))
        =s |u| d v_e+o(|s|).                         (9)

Every P0 point in the cylinder lies on this arc. After shrinking the cylinder, (9) says that its oriented tangent T points toward increasing s on the positive side and toward decreasing s on the negative side. Thus both sides point away from q. This statement is valid for any subset of the containing arc that actually belongs to P0.

An oriented curve in P0 cannot enter this cylinder from outside. At an entry through either parameter end, its direction would have to point inward, whereas (9) points outward. It cannot cross any other face, since there are no zeros of Pi B on those faces, and it cannot pass through q, which is not in P0. These statements can also be read in the implicit s coordinate: on either side, s has the fixed outward derivative sign along the unit tangent. They do not require the complete equilibrium set to be a manifold or to have finitely many components.

## 5. Compactness of the equilibrium curve

If P0 were noncompact, a connected embedded one-dimensional manifold without boundary would be diffeomorphic to R. Its oriented unit tangent has a one-to-one maximal arclength parametrization gamma0:(alpha,beta) to P0 onto P0, where either endpoint may be infinite. Its inverse is continuous in the subspace topology. No completeness of this auxiliary arclength flow is assumed.

Choose times t_j tending to beta. Since P0 is bounded, a subsequence of gamma0(t_j) converges to q in C0. This q cannot belong to P0: continuity of gamma0 inverse would make t_j converge to the interior value gamma0 inverse(q), contradicting t_j tending to beta. Thus q is a missing point of the kind considered above.

Fix an earlier t0<beta and choose q's implicit cylinder small enough to exclude gamma0(t0). Because the subsequence converges to q, the later curve would have to enter this cylinder. Section 4 excludes every possible entry. This contradiction proves P0 compact, hence a C1 embedded circle. The argument covers finite as well as infinite arclength endpoints and does not identify boundedness with properness.

## 6. Consequence for every regular vortical tail node

A881 already makes both vortex signs from P0 escape. Compactness supplies a positive minimum and a finite maximum for the two continuous functions |Xi(Gamma_{+1}q)| and |Xi(Gamma_{-1}q)| on P0. The exact formula

    |Xi(Gamma_zeta q)|
       =|zeta|^(c/kappa)|Xi(Gamma_sign(zeta)q)|

therefore makes M a proper annulus. A886 applies: the two radius-R boundary curves have lengths O(R), and natural vorticity decay makes their circulations O(R^(-p)). The signed surface identity in (3), Stokes on a compact annular exhaustion, and the complete backward vorticity equation exclude M. This uses the full checked exhaustion proof, not merely formal integration over a noncompact surface.

The nonparallel case was excluded in A885, so no regular vortical component M exists in either branch. If a tail point had k=0, dk!=0 and W!=0, its inverse image under Xi would belong to such a component by the C1 scattering intertwining and the construction of L. This proves (1).

The proof does not remove critical vortical nodes k=dk=0, derive global helicity freedom from decay, derive the natural derivative bound, or prove the full nonexistence conjecture. It is valid for the specified C2/C1 actual profiles and every finite real omega.

## 7. Audit method

The submitted eight-section LIT188 proof was read completely. The spectral commutator, the curl orientation sign, and the containing-arc argument were rederived independently. This entire standalone proof was then read after writing. The theoretical question is whether a bounded noncompact parallel equilibrium curve can have a missing endpoint consistent with the pressure identity. The pass criterion is an orientation that excludes every forward-end accumulation without assuming properness, a manifold structure for all equilibria, or isolated zeros. No computation or formalization is needed. Existing configured model agent comparison continues; the provider runtime is not independently attested.
