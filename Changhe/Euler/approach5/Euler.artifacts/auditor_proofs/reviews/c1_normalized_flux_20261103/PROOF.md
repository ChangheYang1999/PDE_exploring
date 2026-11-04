# C1 rigidity from the normalized curl relation

## 1. The exact theorem and its extra hypothesis

Let G be a connected open subset of R3 minus{0}, 0<c<1/2 and omega any finite real number. Put

    Jx=e3 cross x, X(x)=(cI-omega J)x,
    gamma=c/(1-c), eta=(1-gamma)/2, m=1/c=1+1/gamma.

Suppose V in C1(G;R3) satisfies

    div V=0, X.grad V=-(1-c)V-omega JV,
    |V|² curl V=eta grad(|V|²) cross V on {V!=0}.          (1)

Define the continuous one-form alpha=|V|^(gamma-1)V.dx off its zeros and alpha=0 there. Then alpha is closed in distributions. Either V=0 throughout G, or every zero lies on a locally isolated smooth X-orbit and the velocity has a positive power lower bound on a transverse disk about that zero. Infinite value vanishing order at one point forces V=0 on G. Here infinite value order means that for every positive integer N, |V(x)|<=C_N|x-x0|^N on a sufficiently small ball, with its own C_N and radius.

If G=R3 minus{0}, V=0 for c!=1/3. At c=1/3 its complete class is V(x)=Kx/|x|³, K real. No momentum equation or pressure assumption is needed. In particular this theorem concerns the additional normalized curl relation (1); neither tail rank nor bounded |V|²/|S| is asserted to imply it.

## 2. Contraction vanishes near a zero before any weak differentiation

Let Q_t=exp(-omega tJ), F_t x=exp(ct)Q_t x. Integration of the C1 homogeneity equation along contained flow segments gives V(F_t x)=exp(-(1-c)t)Q_t V(x). Thus F_t^*alpha=alpha, including at zeros, because gamma(1-c)=c. On {V!=0}, alpha is C1 and

    curl alpha=|V|^(gamma-1)curl V
                    +(gamma-1)|V|^(gamma-3)(grad|V|² cross V)/2=0.

Differentiating pullback invariance there and using symmetry of Dalpha gives grad(alpha.X)=0. Hence alpha.X is constant on each connected component D of {V!=0}.

If G contains a zero, each such component has a nonempty relative boundary in G. Otherwise it would be open and closed in connected G. Every relative boundary point belongs to {V=0}, because a small ball about a nonzero point lies in one component of the open nonzero set. Continuity makes the constant alpha.X vanish at that boundary. Therefore alpha.X=0 throughout G, and equivalently X.V=0. This reasoning uses only classical derivatives on the nonzero set, not Sobolev regularity or an already constructed potential.

## 3. Physical transverse flux in a flowbox

Near a zero take coordinates x=Psi(t,z)=F_t n(z), with z=(z1,z2), so X=partial_t. The Euclidean metric pulls back to exp(2ct)g0(z). Write mu=sqrt(det g0), a=(g0^(ij)) for the transverse 2 by 2 inverse-metric block and b=(g0^(ti)). These are smooth; a is positive definite. Invariance and Section2 give alpha_t=0 and transverse covector alpha(z).

The inverse power relation is V=|alpha|^(m-2)alpha^sharp. Define the actual transverse velocity flux at t=0 by

    F=mu V_transverse=mu (alpha^T a alpha)^((m-2)/2)a alpha. (2)

This F is C1, even though alpha need not yet have a weak derivative. On a compact smaller disk |F| and |V| are comparable, including at zeros: V^t=b^T a^(-1)V_transverse and all coordinate transformations are smooth and bounded. In particular F=0 exactly when V=0.

Contravariant components of V scale by exp(-t), while volume density scales by exp(3ct). Thus divergence freedom is precisely

    div_z F+(3c-1)d.F=0, d=a^(-1)b.                      (3)

Inverting (2) at nonzero F, with A=a^(-1), gives

    alpha=B(z,F)=mu^(-gamma)(F^T A F)^((gamma-1)/2) A F.  (4)

This formula extends continuously to zero. All differentiated uses below are on F!=0.

## 4. The normalized constitutive derivative is uniformly elliptic

Set s=F^T A F. Direct differentiation of (4) gives

    D_F B=mu^(-gamma)s^((gamma-1)/2)
                  [A+(gamma-1)(AF tensor AF)/s].        (5)

For each h, (h.AF)²<=s(h.Ah). Since 0<gamma<1, the bracket is bounded below by gamma A and above by A in quadratic-form order. Consequently

    M=|F|^(1-gamma)D_F B

has eigenvalues in one fixed interval [lambda,Lambda], 0<lambda<=Lambda<infinity, on the compact disk and for every F!=0. Holding F fixed, smooth coefficients give |D_z B|<=C|F|^gamma. Let T=DF, T_ij=partial_j F_i. The classical curl equation for (4) and (3) imply

    |tr T|<=C|F|,
    |(MT)_21-(MT)_12|<=C|F|.                            (6)

The singular scalar factor has been removed on the nonzero set; no derivative estimate for alpha at a zero has been assumed.

## 5. The full-disk scalar elliptic inequality

At one point diagonalize M by a simultaneous orientation-preserving rotation of input and output frames. Trace, determinant, Frobenius norm and the antisymmetric scalar in (6) are unchanged. This is pointwise algebra and differentiates no eigenframe. If M=diag(lambda1,lambda2), T11=u,T12=v, then

    T22=-u+e1, T21=(lambda1/lambda2)v+e2/lambda2,
    |e1|+|e2|<=C|F|.

Thus

    -det T=u²+(lambda1/lambda2)v²-u e1+(e2/lambda2)v
              >=c1(u²+v²)-c2|F|²,
    |T|²<=c3(u²+v²+|F|²).

The positive lower eigenvalue ratio makes c1>0. Combining gives

    |DF|²<=K(-det DF)+C|F|², K>=2.                     (7)

A C1 scalar function has gradient zero almost everywhere on its zero level set. Indeed where a partial derivative is nonzero, the implicit function theorem places that level set on a smooth graph of measure zero; a countable cover suffices. Apply this to both components of F. Then DF=0 almost everywhere on {F=0}, so (7) holds on the full disk almost everywhere.

With f=F1-iF2, its Jacobian is Jf=-det DF. The Wirtinger identities |Df|²=2(|partial f|²+|dbar f|²) and Jf=|partial f|²-|dbar f|² turn (7) into

    |dbar f|<=kappa|partial f|+C0|f|,
    kappa=sqrt((K-2)/(K+2))<1.                         (8)

The unknown is one complex scalar. No unique-continuation assertion for an unrestricted vector-valued Beltrami system is being used.

## 6. Factorization with every product justified

Choose measurable complex nu,A1 so that |nu|<=kappa, |A1|<=C0 and dbar f=nu partial f+A1 f. At a point first use nu partial f in the direction of dbar f up to magnitude kappa|partial f|; the residual is at most C0|f| and defines A1 after division by f. At almost every zero both derivatives vanish and A1 can be set to zero.

On a relatively compact disk extend both coefficients by zero to the plane. The Beurling transform S is an L2 isometry and bounded on Lp for 1<p<infinity. Interpolating with any fixed exponent above2 gives ||S||p tending to1 as p decreases to2. Choose p>2 so kappa||S||p<1. The Neumann series defines

    h=(I-nu S)^(-1)A1 in Lp.

Its equation shows h is supported in the coefficient disk. Let s be its Cauchy transform. Then dbar s=h, partial s=Sh and dbar s-nu partial s=A1. The compact support and p>2 make s locally bounded and continuous by Holder's inequality for the Cauchy kernel; also s is W1,p locally. Hence g=exp(-s)f is W1,p locally, and legitimate Sobolev chain and product rules give dbar g=nu partial g.

Scalar measurable Beltrami theory and Stoilow factorization give g=H composed with chi, with chi a quasiconformal homeomorphism and H holomorphic on its image. These classical inputs, including local power bounds for chi and its inverse, are used in the actual Guo-Kar manuscript arXiv:1512.00673v2, Section3.1, printed pages8-10. Those pages and their proof were read and are pinned here. The Neumann-series argument above supplies the bounded lower-order-coefficient case directly. No nonlinear-gradient regularity theorem from that paper is needed. Its phrase that a complex exponential is nonnegative is unnecessary: only nonvanishing and local upper and lower bounds for its modulus are used here.

If H is not identically zero, each zero w0 has a finite order n, hence |H(w)|>=C|w-w0|^n nearby. Local Holder continuity of chi^(-1) gives |chi(z)-chi(z0)|>=C'|z-z0|^L for some finite L. The modulus of exp(s) is locally bounded above and below by positive constants. Therefore

    |F(z)|=|f(z)|>=C''|z-z0|^(Ln)                       (9)

near each zero z0, and that zero is isolated. Otherwise F vanishes on the disk. The prerequisite W1,2 regularity for scalar factorization follows from the proved W1,p regularity of g with p>2.

## 7. Propagation and removability

If V has an open zero region but is not zero on G, take a boundary point of the interior of its zero set. A small flowbox there has both an open zero portion and nonzero points. Homogeneity transfers both to its transverse disk. Factorization cannot give a holomorphic function with an open zero subset and a nonzero value. Equivalently, at this boundary point the local alternative is neither an identically zero neighborhood nor an isolated transverse zero. This contradiction proves that the zero set has empty interior unless V=0 throughout G.

For nonzero V on connected G, every local flux about a zero is therefore nontrivial. Section6 gives one isolated transverse zero with the power lower bound (9); homogeneity extends it along exactly the local smooth orbit. Comparability in Section3 transfers that lower bound to V. Infinite value vanishing order in three dimensions restricts to the transverse disk and contradicts (9), proving the flatness conclusion.

It remains to justify weak closedness. Near a zero, the zero set is now one smooth curve. Take a cutoff chi_epsilon supported away from its epsilon tube, equal to one beyond twice that distance, with gradient bounded by C/epsilon. On a compact local patch its transition volume is O(epsilon²). For a compactly supported smooth test vector phi, classical closedness gives

    integral chi_epsilon alpha.curl phi
                    =-integral alpha.(grad chi_epsilon cross phi).

The right side is O(epsilon), since alpha is locally bounded. The left side converges by dominated convergence. Hence alpha is distributionally closed in the patch. Zero-free patches are already classical, and a finite cover and partition of unity prove closedness on G. The geometric removability input was proved before this passage and not assumed for an arbitrary C1 zero set.

## 8. The global potential and zero drift

For G=R3 minus{0}, simple connectivity and continuous distributional closedness give a global C1 potential psi. One construction mollifies on local balls, passes uniformly in the gradients, and patches the additive constants along homotopies. Pullback invariance implies the spatial difference psi(F_t x)-psi(x) is constant. Its continuous additivity in t gives

    psi(F_t x)=psi(x)+Ct, X.grad psi=C.

Furthermore V=|grad psi|^(m-2)grad psi, so psi is weakly m-harmonic. If C=0, every orbit meets the unit sphere exactly once and psi is invariant along it. The sphere maximum is therefore an attained global maximum.

Here is the required maximum principle at C1 regularity. If h=max psi-psi>=0 has positive and zero points, choose a positive point y whose distance R to the zero set is small enough that the closed ball is inside the domain. In R/2<|x-y|<R compare h with the radial m-harmonic barrier equal to its positive inner-sphere minimum and zero on the outer sphere. For m!=3 this barrier is proportional to (r^k-R^k)/((R/2)^k-R^k), k=(m-3)/(m-1); for m=3 it is proportional to log(R/r). Weak comparison follows by testing the difference with its positive part and strict monotonicity of z to |z|^(m-2)z. The barrier has strictly negative outer radial derivative. At a touching zero this contradicts Dh=0. Thus psi is constant and V=0.

## 9. Nonzero drift and the exceptional class

If C!=0 put beta=C/c, pi(r theta)=exp((omega/c)log(r)J)theta and u=psi restricted to S2. Then psi=beta log r+u(pi(x)). At an extremum theta of u, grad psi=beta theta!=0, so V and alpha are nonzero and alpha is C1 nearby. Consequently psi and u are C2 there. The chain rule at that angular critical point gives

    D²psi=beta(I-2theta tensor theta)+(Dpi)^T Hess_S2(u)Dpi.

The m-Laplace equation becomes

    0=beta(3-m)+tr[(I+(m-2)theta tensor theta)
                                  (Dpi)^T Hess_S2(u)Dpi].     (10)

The trace term is nonnegative at a minimum and nonpositive at a maximum. Choosing the minimum if beta(3-m)>0 and the maximum if it is negative excludes C!=0 unless m=3. This uses every angular mode and every finite omega, with no uniform bound on local constants required.

For m=3 put psi0=beta log r, V0=beta|beta|x/r³. Both V and V0 are divergence free, and psi-psi0 is invariant under F_t. On any annulus integration by parts gives

    integral (V-V0).(grad psi-grad psi0)
        =integral_outer (psi-psi0)(V-V0).n
                       -integral_inner (psi-psi0)(V-V0).n=0.

The two boundary integrals are equal because V-V0 scales by exp(-2ct)Q_t, area by exp(2ct) and the scalar difference is invariant. Strict monotonicity of z to |z|z forces grad psi=grad psi0 and hence V=V0. These radial fields satisfy all of (1) for c=1/3 and every omega. Their nonzero members are singular at the omitted origin, outside the target c interval and outside the smooth whole-space class.

## 10. Audit scope and dependencies

All nine sections of LIT248 and the complete earlier global proof A1552-A1556 were read. The scalar factorization pages of the actual primary manuscript were reread, including the inverse-map power estimate. Every algebraic, regularity, propagation, cutoff and angular step above was independently reconstructed. No computation, formalization or build was used.

The C1 improvement is valid because the physical flux, not the normalized root, is the differentiated unknown. This does not prove the extra normalized curl relation for general tails or unique continuation for the unrestricted coupled pressure system. Existing configured model agents receive the result through files; their runtime model identity is unattested. Main bare-decay nonexistence for arbitrary helicity and all omega remains open.
