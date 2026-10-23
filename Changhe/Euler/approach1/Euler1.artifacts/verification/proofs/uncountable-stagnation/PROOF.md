# Obstruction with arbitrary stagnation sets in three dimensions

Status: CONFIRMED by this lane after the independent uncount1 referee supplied a second complete proof and this lane checked it. Updated 2026-10-23T07:08:49.462917+00:00. The actual lead Opus 5.5 reviewed both proofs on 07:19 UTC; this lane independently confirms its reconciled v3 proof in THEORY_V3_AUDIT.md. This lane has not stopped any numerical worker. This is an informal proof, not formal verification. No novelty claim is made. The original proposal is archived by content hash; the second proof and audit are registered in UNCOUNTABLE_AUDIT.md.

## 1. Statement, hypotheses and dependencies

Let 0 < c < 1/2. Let U,P be C^2 on R^3 and solve

    (1-c)U + (c y+U).grad U + grad P = 0,     div U = 0,

with U(y)=o(|y|) uniformly as |y| tends to infinity. The conclusion is that curl U=0 and U is constant. If U tends to zero, U=0. There is no hypothesis on the cardinality or regularity of the stagnation set.

Notation: V(y)=c y+U(y); G=DU, S=(G+G^T)/2, W=(G-G^T)/2, Omega=curl U; W a=Omega cross a/2. Let Z={V=0}, and let

    E={p in Z: lambda_max(S(p)) >= 1}.

Dependencies already proved in ../stagnation-obstruction/PROOF.md: global completeness of the flow Y(a,t) from sublinear growth; compact backward trajectories; the Bernoulli Lyapunov identity; the vorticity transport estimate; and the local null-graph lemma for a C^1 vector field at an equilibrium with a negative-real-part eigenvalue. The latter lemma includes nonhyperbolic center directions: every orbit staying in a sufficiently small neighborhood for all negative time lies in a Lipschitz center-unstable graph of dimension at most two. That graph and each finite-time flow image have zero three-dimensional measure. The present proof restates the uses of these facts and supplies the additional geometric steps.

The statement is specific to spatial dimension three and c<1/2. Neither the affine examples with linear growth nor the c=1/2 case is covered.

## 2. Backward limit sets and points where vorticity could survive

Sublinearity gives V(y).y >= c|y|^2/2 outside a ball. Every backward trajectory stays in a compact ball, and Z is compact. Its alpha-limit set A(a) is nonempty, compact and connected. Also dist(Y(a,t),A(a)) tends to zero as t tends to minus infinity: otherwise a subsequence in the compact trapping ball has a limit outside A(a), contradicting its definition.

Define H=|V|^2/2+P+c(c-1)|y|^2/2. The exact equations imply

    V.grad H = -(1-2c)|V|^2.

H is monotone along a trajectory and bounded on its compact backward orbit. It has a backward limit, is constant on A(a), and A(a) is invariant. Therefore V=0 on A(a); hence A(a) is a connected compact subset of Z. In particular dist(Y(a,t),Z) tends to zero backwards.

The vorticity equation along the flow is Omega'=(G-I)Omega. If A(a) avoids E, compactness and continuity give lambda_max(S)<=1-eta on a neighborhood of A(a) for some eta>0. The trajectory lies there for all sufficiently negative time. Thus

    d|Omega(Y(a,t))|^2/dt <= -2 eta |Omega(Y(a,t))|^2.

Integrating from an arbitrarily early negative time to a fixed later time, and using the bounded vorticity on the compact orbit, gives Omega(a)=0. Consequently every a with Omega(a) nonzero has A(a) intersecting E.

## 3. Rank and local structure at the exceptional zeros

At p in Z the exact vorticity equation gives G(p)Omega(p)=Omega(p). Since W Omega=0, also S Omega=Omega.

If Omega(p) is nonzero, DV(p)=cI+G(p) has eigenvalue 1+c along Omega. The other two eigenvalues, counted algebraically over C, have sum 2c-1<0. At least one has strictly negative real part. If they form a conjugate pair, both do. Thus DV has a positive eigenvalue and a negative-real-part eigenvalue, and rank DV>=2.

If Omega(p)=0 and p is in E, G=S is symmetric. Its trace is zero and lambda_max(S)>=1, so lambda_min(S)<=-1/2. Hence DV has an eigenvalue >=1+c>0 and an eigenvalue <=c-1/2<0. Again rank DV>=2.

If rank DV=3, the inverse function theorem makes p an isolated zero. If rank DV=2, its eigenvalues are simple and real, one positive, one negative and one zero. In the vortical case they are exactly 1+c, 2c-1 and 0; in the irrotational case symmetry gives the same sign pattern (not necessarily the same nonzero values).

At any rank-at-least-two zero, select two components of V with independent differentials. Their joint zero set is a C^2 embedded curve in a neighborhood, by the implicit function theorem. The full zero set Z in that neighborhood is a closed subset of that curve. Rank-three zeros could also be handled this way, but are already isolated. Strictly positive and strictly negative real eigenvalues persist in a sufficiently small neighborhood of a rank-two point.

## 4. Local capture near an interval of equilibria

Capture lemma. Let a C^2 vector field in R^3 vanish on an embedded C^2 arc through q. Suppose DV(q) has three simple real eigenvalues lambda_s<0, 0, lambda_u>0, with the zero direction tangent to the arc. There is a neighborhood of q such that a backward-precompact orbit whose distance from the full zero set tends to zero and which accumulates at q is trapped for all sufficiently negative time in an arbitrarily prescribed sufficiently small local null-graph neighborhood of q. For application below it is enough to capture near an interior point of an equilibrium interval contained in its alpha-limit set.

Choose a shorter equilibrium arc on both sides of q. Flatten it into (s,u,z) coordinates with equilibria {(0,0,z): |z|<2a}. Choose the normal axes at q along the stable and unstable eigenvectors. This is a C^2 coordinate change: parametrize the C^2 arc and add the two fixed eigenvectors at q. Its Jacobian at q is invertible. The transformed vector field is C^1 and has the form

    s' = lambda_s s + f_s(s,u,z),
    u' = lambda_u u + f_u(s,u,z),
    z' = g(s,u,z),

where f_s(0,0,z)=f_u(0,0,z)=g(0,0,z)=0. On a small box, continuity of the normal derivatives gives

    |f_s|+|f_u| <= epsilon (|s|+|u|),
    |g| <= K (|s|+|u|).

Here epsilon can be arbitrarily small by shrinking a and the normal radius; the linearization at q is diagonal. The derivative in z is zero along the equilibrium arc. Set beta=min(-lambda_s,lambda_u)>0 and choose 2epsilon<beta.

Consider any finite time segment [t0,t1] staying in this box with |s|,|u|<=eta throughout. Variation of constants, using the stable coordinate forward from t0 and the unstable coordinate backward from t1, gives

    |s(t)| <= eta exp[-beta(t-t0)] + integral(t0,t) exp[-beta(t-v)] epsilon (|s(v)|+|u(v)|) dv,
    |u(t)| <= eta exp[-beta(t1-t)] + integral(t,t1) exp[-beta(v-t)] epsilon (|s(v)|+|u(v)|) dv.

Integrating and adding proves

    integral(t0,t1) (|s|+|u|) dt <= 2eta/(beta-2epsilon).

(The factor two in front of epsilon is conservative.) Therefore the total z displacement on the segment is at most 2K eta/(beta-2epsilon), independently of its duration.

Choose the inner box |z|<a, |s|,|u|<rho, compactly inside the flattening chart. Every zero in the larger chart lies on the same curve, after shrinking the chart using the rank-two implicit-function description. Thus an orbit in the inner box sufficiently close in physical distance to Z has |s|,|u|<=eta, where eta can be made arbitrarily small. Closest zeros cannot lie outside the larger chart when that distance is sufficiently small; the compact inner box has positive separation from its complement.

Choose eta<rho/2 and 2K eta/(beta-2epsilon)<a/2. At a sufficiently negative time tn, the orbit is arbitrarily close to q, hence |z(tn)|<a/4. For all t<=tn its distance to Z is small enough for the eta bound whenever it lies in the inner box. If it had a first exit from this box going backwards, that exit cannot occur through a normal face, because |s|,|u|<=eta<rho/2. It cannot occur through z=+a or -a either: the segment between that exit and tn has total z displacement less than a/2. This contradicts |z(tn)|<a/4. Consequently there is no backward exit.

The box can be selected inside any sufficiently small neighborhood where the local null-graph lemma applies. The trapped point therefore belongs to that graph at time tn. This proves the needed local capture assertion. No convergence theorem for arbitrary gradient-like flows, no analyticity, and no globally normally hyperbolic zero set is assumed.

## 5. A connected limit set touching a local curve contains an equilibrium interval

Elementary topological lemma. Let A be a compact connected set containing p and at least one other point. Suppose that A in a neighborhood of p is contained in a single embedded arc. Then, arbitrarily close to p, that arc contains a nondegenerate interval lying in A.

Proof. Use a tubular coordinate chart near p and write the arc as (0,0,z). Suppose some small arc interval about p contains no nondegenerate subinterval of A. The complement of A on that interval is then dense. Pick z_-<z(p)<z_+, both outside A, so close to z(p) that the corresponding closed short tube excludes a chosen other point of A. Its lateral boundary does not meet A because all nearby A lies on the arc; its two end faces do not meet A because z_-,z_+ are not in A. The intersection of A with the open tube is therefore nonempty, both relatively open and relatively closed in A, and proper. This contradicts connectedness. If A were entirely inside the short chart, the same argument, or connectedness of its z projection, gives a nondegenerate interval directly.

Apply this lemma to A(a) at p in A(a) intersect E. If A(a) is a singleton, the orbit is eventually backward trapped near p. If A(a) is not a singleton, p cannot be an isolated zero. The rank-two curve description from section 3 and the topological lemma give a nondegenerate interval of equilibria in A(a), arbitrarily close to p. At an interior point q of a sufficiently close interval, DV has a positive and a negative eigenvalue; its third eigenvalue is zero because V vanishes along the arc. Section 4 captures the orbit near q in a local null-graph neighborhood.

## 6. Countable covering, without countability of the zeros

For every equilibrium p with at least one negative-real-part eigenvalue, choose an open neighborhood B_p on which the local null-graph lemma holds, with its associated Lipschitz graph M_p of dimension at most two. By the second-countability of R^3, this open cover of that subset of Z has a countable subcover {B_j}. This does not assume that Z is countable.

If A(a) is the singleton p in E, pick B_j containing p. Convergence to p puts the entire sufficiently early backward orbit in B_j; thus Y(a,-n) lies on M_j for some positive integer n, and a lies in Y(M_j,n).

If A(a) is nontrivial and meets E at p, select a covering B_j containing p. Choose the equilibrium interval from section 5 so close to p that an interior point q and its sufficiently small capture box lie in B_j. Section 4 puts the sufficiently early backward orbit entirely inside B_j, so again a belongs to Y(M_j,n) for some positive integer n.

Thus

    {a: Omega(a) != 0} is contained in union over j,n of Y(M_j,n).

Each graph has three-dimensional measure zero and finite-time C^1 flow maps preserve this property. The countable union has measure zero. But nonzero continuous vorticity has a nonempty open nonzero set, which has positive measure. Hence Omega=0 everywhere.

Together with div U=0, this makes every component of U harmonic. The sublinear harmonic Liouville argument, proved in the earlier result, makes U constant. Decay then makes that constant zero.

## 7. Audit checklist and present scope

The following points were checked independently in the cross-audit: (i) the rank-two and simple-sign eigenvalue conclusion in section 3; (ii) uniform coordinate bounds in section 4 despite only C^2 original regularity; (iii) the topological interval lemma for a connected set that may leave and reenter the local chart; (iv) applying the local trapped-set graph to all captured orbits via the countable open subcover. Any failure here leaves L1, with its countability hypothesis, as the accepted result.

There is no numerical claim, no stability claim and no blowup claim. The lead Opus 5.5 independently checked and reconciled both proofs at 07:19 UTC, and the later hostile audit confirms the theorem. The prompt permits the fully checked primary-class obstruction to supersede further blind primary search. It does not exclude c=1/2 or larger-exponent secondary cases and does not create numerical hours. Any final campaign decision must state its scope and unfinished numerical work; see SCOPE_AUDIT.md.

## 8. Strengthened convergence consequence

The capture lemma holds in arbitrarily small neighborhoods of the chosen interior equilibrium point q. For a fixed orbit with q in its alpha-limit set, capture in each such neighborhood puts the entire alpha-limit set in its closure. Shrinking the neighborhoods proves that the alpha-limit set equals {q}. Thus the nontrivial-alpha case meeting E is actually impossible. Every nonzero-vorticity orbit converges backwards to one point of E. Since E is compact, finitely many inner neighborhoods with closures inside corresponding null-graph neighborhoods suffice, followed by the countable integer-time flow images. This simplifies section 6 and confirms that no uncountable union of individual basins is being used.

An independent alternative proof uses the exact identity grad H = -[(1-2c)I + Omega cross]V. At a zero, the bracket is invertible, so Hess H has exactly the rank and kernel of DV. On an equilibrium interval near a rank-two zero, Hess H is nonsingular transversely. Taylor expansion gives |H-h|^(1/2) <= C |grad H|. Together with dH(Y(-t))/dt=(1-2c)|V|^2 and |grad H| <= C'|V|, this bounds remaining trajectory length by a constant times (h-H)^(1/2). A sufficiently late return near an interior arc point is trapped and converges. The cross-audit verifies these estimates, including the indefinite transverse Hessian and the first-exit argument.
