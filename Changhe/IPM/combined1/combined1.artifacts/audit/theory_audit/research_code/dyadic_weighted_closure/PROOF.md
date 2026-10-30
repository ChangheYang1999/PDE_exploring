# A scale-adapted weighted high space and a conditional closure theorem

## 1. Purpose and exact scope

A decreasing weight on an ordinary fixed-scale Sobolev norm does not control the uniform gradient needed by the weighted low-space contraction. Section 6 proves this failure even for normalized S1 functions. Sections 2 to 5 give a high space that repairs this defect and a conditional a posteriori theorem. The missing input is a uniform high resolvent estimate, stated explicitly as hypothesis (H). No such estimate is proved here for a numerical profile.

All functions are real. S1 means even in x and odd in y. Let 0<a<2, 0<s<1, q=2+s, w(X)=(1+|X|^2)^(-a/2), and H_a=L2(w^2 dX) in S1. Use the unitary Fourier transform in two dimensions, J=(1-Delta)^(1/2), and the usual H^q norm ||J^q f||2. Vector H^q norms sum component squares. The canonical velocity is U[h]=(-R1R2 h,R1^2 h). Assume its already established odd weighted bound

    ||w U[h]||2 <= C_U ||w h||2.                             (1)

For example, the earlier coarse odd Beurling estimate gives the safe constant C_U=1+2/(2-a). If T4-054 is independently accepted, this may be replaced by 2/(2-a). The theorem does not depend on that improvement.

Choose smooth radial cutoffs chi0 and chi with values in [0,1]. Let chi0=1 on |X|<=2, supported on |X|<4. Let chi=1 on 1<=|X|<=2, supported on 1/2<|X|<4. Their derivatives vanish where they equal one, including the endpoints of these plateaux. These are fixed functions, not candidate parameters.

For h in H_a define

    Y(h)^2 = ||w h||2^2
       + ||chi0 h||Hq^2 + ||chi0 U[h]||Hq^2
       + sum_(j>=1) 2^(2(1-a)j)
           ( ||chi(.)h(2^j .)||Hq^2
              + ||chi(.)U[h](2^j .)||Hq^2 ).                (2)

The space Y consists of all h in H_a for which (2) is finite. Its velocity is the canonical extension in (1), not a separate unknown. No density assertion about compactly supported functions in Y is needed below.

## 2. Hilbert structure, point bounds and completeness of the ball

The space Y is Hilbert. To prove completeness, let h_n be Cauchy in (2). It converges to h in H_a, and (1) gives U[h_n] -> U[h] in the weighted vector L2 space. Each localized rescaled component converges in H^q. Its distributional limit must be the corresponding localization of h or U[h], since weighted L2 convergence implies L2 convergence on every compact set. The direct-sum limits therefore represent h, and convergence holds in (2). The parallelogram identity follows from the linearity of U and of all localizations.

Define

    C0=[4 pi (1+s)]^(-1/2),
    C1=[4 pi s(1+s)]^(-1/2).                                (3)

Fourier inversion and Cauchy-Schwarz give, for scalar or vector f,

    ||f||infinity <= C0 ||f||Hq,
    ||Df||infinity,Frobenius <= C1 ||f||Hq.                  (4)

For the second inequality it suffices to sum the two coordinate estimates. The integrals are

    integral (1+|xi|^2)^(-2-s) dxi = pi/(1+s),
    integral |xi|^2(1+|xi|^2)^(-2-s) dxi = pi/[s(1+s)].

The stated C1 is a safe Frobenius constant; optimality is not claimed.

If 2^j<=|X|<=2^(j+1), j>=1, the j-th cutoff is identically one at X/2^j. Applying (4) to that localized rescaling gives

    |h(X)|, |U[h](X)| <= C0 2^((a-1)j) Y(h),
    |Dh(X)|, |DU[h](X)| <= C1 2^((a-2)j) Y(h).             (5)

On |X|<=2 the same bounds hold without the powers of two, using chi0. In particular

    ||Dh||infinity, ||DU[h]||infinity <= C1 Y(h),             (6)

since a<2. Both h and U[h] are locally C^(1,alpha) for every 0<alpha<s, are globally Lipschitz, and grow at most like max(1,|X|^(a-1)). They are centrally odd, so their values at the origin vanish. Since the summands in (2) form an l2 sequence, (5) also implies h=o(r^(a-1)) and U[h]=o(r^(a-1)) at infinity, uniformly in angle. The weaker O bound is sufficient below.

The trace c[h]=partial_y U2[h](0) is a continuous linear functional on Y. For every R>0 the ball

    B_R={h in Y: Y(h)<=R, c[h]=0}                           (7)

is complete in the distance ||w(h-k)||2. Indeed a Cauchy sequence has a low limit. A weakly convergent subsequence in the Hilbert space Y has the same distributional limit, and weak lower semicontinuity preserves the radius. Continuity of c preserves the constraint. Thus the low limit lies in B_R. This argument also proves that the image of the ball is closed in H_a.

For a simple membership criterion, suppose a smooth S1 h and its canonical U[h] obey |D^k h|+|D^k U[h]|=O(r^(b-k)) for k=0,1,2,3 outside a ball. If b<a-1, then h belongs to Y. After rescaling, every H^3 norm in (2) is O(2^(bj)), and H^q is bounded by H^3 because q<3. The geometric series converges. The low norm has the same strict power threshold b<a-1. This criterion assumes the stated velocity bounds; they are not inferred merely from the density's leading coefficient.

## 3. Low operators and the explicit missing high estimate

Let rho be a smooth S1 reference with smooth canonical u, V=cX+u, c>0. Assume V is globally Lipschitz and complete, u is sublinear, Drho is bounded, a0=rho_y(0)>0, and

    c+partial_y u2(0)=1.                                   (8)

Let L=V.D-1+U[.].Drho. Assume its weighted low realization has the core energy inequality

    Re <Lh,h>_(H_a) <= -beta ||h||_(H_a)^2, beta>0.         (9)

This includes the usual maximal distributional transport realization and the bounded weighted coupling supplied by (1). An independently verified instance of T4-041 or T4-022 can supply (9). Neither theorem supplies (H) below.

For k in B_R put A_k=L+U[k].D and

    beta_R=beta-a C1 R.                                    (10)

If beta_R>0, A_k has a maximal low inverse with norm at most 1/beta_R. To see this, W=U[k] is globally Lipschitz, divergence free, centrally odd, and |W(X)|<=C1 R |X| by (6). Conjugation by w changes the skew transport W.D into itself plus the scalar -W.D log w, whose modulus is at most a C1 R. Combining with (9) gives low decay beta_R. The complete Lipschitz flow, bounded coupling, graph-core approximation and semigroup integral give the same maximal-domain inverse as in T4-022. Weighted L2 is locally unweighted L2, so the maximal distributional characterization is preserved under conjugation.

The additional high hypothesis is:

(H) There is a finite M such that, for every k in B_R and every f in Y with f_y(0)=0, the low inverse A_k^(-1)f lies in Y and

    Y(A_k^(-1)f)<=M Y(f).                                  (11)

This is a uniform high resolvent estimate for the concrete norm (2), on a specified input hyperplane. It includes high regularity, not just an L2 inverse or a finite matrix condition. Its proof and numerical constants remain OPEN for the current reference profiles.

## 4. Conditional a posteriori statement

Let the exact residual be F=(cX+u).D rho-rho. Assume F belongs to Y, (8)-(11), and

    M Y(F)<=R,
    C_U C1 R < beta_R,
    C1 R<a0.                                               (12)

Then there is a unique h in B_R for which rho+h is an exact stationary IPM profile at the fixed c. Its y slope at the origin is positive. Picard iteration of T(k)=-A_k^(-1)F converges in H_a with contraction ratio at most

    theta=C_U C1 R/beta_R <1.                              (13)

If rho has a specified leading r^gamma profile with gamma>a-1, the correction preserves that profile uniformly in angle.

## 5. Proof of the conditional statement

The residual has F_y(0)=a0(c+partial_y u2(0)-1)=0 by (8). If k in B_R and h=A_k^(-1)f belongs to Y, all functions and velocities have first-order expansions at the origin. Parity gives h(0)=U[h](0)=U[k](0)=0. The y-linear coefficient of A_k h is

    (c+partial_y u2(0)-1+c[k])h_y(0)+a0 c[h]=a0 c[h].      (14)

This computation uses only first-order Taylor expansions, not second differentiability of h. Thus f_y(0)=0 implies c[h]=0. Hypothesis (H) and the first inequality in (12) make T a map from B_R to itself.

For k,l in B_R, write h_k=T(k), h_l=T(l). The maximal low domains can be compared because

    (U[k]-U[l]).D h_l belongs to H_a

by (1),(6). Subtraction of the two distributional equations gives

    A_k(h_k-h_l)=U[l-k].D h_l.

The low inverse and (1),(6) imply

    ||w(h_k-h_l)||2 <= beta_R^(-1) C_U C1 R ||w(k-l)||2.

Completeness proved in Section 2 gives a unique fixed point. At a fixed point A_h h=-F, which expands exactly to the stationary equation for rho+h. Conversely, any stationary correction in B_R is in the maximal low domain of A_h, since its equation has right side -F in H_a. Low uniqueness makes it a fixed point. The slope bound follows from (6),(12). The leading-profile assertion follows from (5) and a-1<gamma.

This proves the conditional theorem without treating the transport nonlinearity as a bounded high-to-high map. It does not verify (H) or (12) for any candidate.

## 6. Why simply weighting an ordinary Sobolev norm fails

For every a>0 and every finite q>=0, define the fixed-scale norm

    N(h)=||w J^q h||2.                                     (15)

There is no finite C with ||Dh||infinity<=C N(h) for all smooth normalized S1 h. Even adding ||w J^q U[h]||2 does not repair the assertion when (1) holds.

Choose a nonzero smooth bump psi supported in a small disk, even in both coordinates, with a nonzero y derivative. For R large set

    h_R(X)=R^a sum_(sigma,tau in {-1,1}) tau
                         psi(X-(sigma R,tau R)).           (16)

Its four supports are disjoint, it is S1, and ||Dh_R||infinity is a fixed positive multiple of R^a. Since J^q psi is Schwartz and

    <P>^a <X+P>^(-a) <= 2^(a/2) <X>^a,

each translated term in (15) is bounded uniformly in R. Hence N(h_R) is uniformly bounded. The weighted velocity term is bounded by C_U N(h_R), because U and J^q commute on these smooth odd inputs and (1) applies.

To enforce c[h]=0 exactly, choose a smooth radial eta compactly supported and identically one near zero, and let g=-4y eta(r). The canonical contact formula gives c[g]=1: its local contribution is -g_y(0)/4=1, and the sin(3theta) integral vanishes by angular orthogonality. For h_R, the same formula has no contact term and its kernel is O(R^-3) on four supports of fixed area. Thus c[h_R]=O(R^(a-3)). Put

    htilde_R=h_R-c[h_R]g.

For 0<a<2, the subtracted term tends to zero in (15) and in the uniform gradient norm. Therefore htilde_R is normalized, its N norm stays bounded, and its gradient still diverges. The same construction preserves the added velocity norm. This refutes only a fixed-scale weighted embedding. It does not refute the scale-adapted norm (2), whose dyadic derivative factors penalize these packets.

## 7. Status and dependencies

This is new T4 work and is CLAIMED pending independent Opus review. The analytic conclusions are the high-space properties, the conditional theorem under (H), and the counterexample in Section 6. The concrete weighted high estimate (H), a forcing certificate and a successful numerical closure are OPEN. The original case4 residual is compatible with the power criterion if its density and velocity exponents satisfy b=2/c-1<a-1; leading-profile preservation simultaneously requires a<1+1/c. This leaves the nonempty formal interval 2/c<a<1+1/c because c>1. Compatibility of exponents is not an existence proof.

Dependencies: the independently established odd weighted velocity bound (1), local Fourier Sobolev embedding, Hilbert weak compactness, the maximal weighted transport argument of T4-022, and the canonical contact formula of T4-001. No computation, numerical constant fit, formal proof assistant, or external theorem about a profile is used.
