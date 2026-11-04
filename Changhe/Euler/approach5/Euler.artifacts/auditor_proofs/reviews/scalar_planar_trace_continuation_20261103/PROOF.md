# Scalar planar continuation and the exact Mercuri source scope

## 1. Statement, premises and dependencies

Let D be a connected open subset of R2, and let u be a real function in C1(D) intersect W2,2_loc(D). Let A be a measurable real symmetric matrix field. On each relatively compact disk assume finite constants C and 0<lambda<=Lambda such that

    lambda I <= A <= Lambda I,
    |A:D2u| <= C (|u|+|Du|) almost everywhere.

Then an open zero set implies u=0 on D. Also, if at one interior point z0 the pointwise bound |u(z)|<=C_j|z-z0|^j holds locally for every positive integer j, then u=0 on D. Each constant and neighborhood may depend on j. No integral version is asserted for these general nondivergence coefficients.

The proof below independently reconstructs LIT263. Its analytic inputs are the Lq Beurling-transform bound with norm tending to1 as q tends to2, the distributional Cauchy right inverse, the measurable Riemann mapping theorem, Stoilow factorization and local Holder continuity of inverse quasiconformal maps. These classical theorems are external dependencies. Local existence for a continuous bounded vector field is the elementary Peano theorem. No formalization, numerical experiment or assertion about all coupled systems is involved.

The pinned submission is in the team records. The actual thirty-page Mercuri v2 manuscript and the literature agent's narrower source-scope audit are pinned alongside it. The record was independently opened with the web tool; its PDF endpoint was unavailable there, so the actual PDF was read from the literature agent's hashed copy. This is not a claim of an independent PDF download.

## 2. Exact real-to-complex reduction

On a fixed disk write A=[[a,b],[b,d]], T=a+d, h=u_z=(u_x-i u_y)/2 and g=A:D2u. Reality gives u_bar_z=bar h and h_bar_z=Delta u/4. Substitution of h_z=(u_xx-u_yy-2i u_xy)/4 gives

    g=2T h_bar_z+(a-d+2ib)h_z+(a-d-2ib)overline(h_z).

Define mu=-(a-d+2ib)/(2T), nu=bar mu, and

    Lf=f_bar_z-mu f_z-nu overline(f_z).

The spectral gap of a positive two by two matrix implies

    |mu|+|nu|=sqrt((a-d)^2+4b^2)/T
             <=k=(Lambda-lambda)/(Lambda+lambda)<1.

Define alpha=g bar h/[2T(u^2+|h|^2)] and beta=g u/[2T(u^2+|h|^2)] away from {u=h=0}, and define both as zero on that set. The trace inequality makes these coefficients bounded. It also makes g zero almost everywhere on the exceptional set. Thus Lh=alpha h+beta u almost everywhere on the full disk. This calculation never differentiates A. The assumed W2,2 regularity makes h continuous and W1,2.

## 3. Right inverse and Riccati cancellation

Choose q>2 so close to2 that k||B||_q<1, where B is the Beurling transform. Extend mu,nu and a bounded right side psi by zero from B_r to the plane. The map

    w -> mu B w+nu overline(B w)+psi

is a real-linear affine contraction on Lq. Its fixed point w is supported in B_r and has norm at most (1-k||B||_q)^(-1)||psi||_q. The Cauchy transform Cw satisfies (Cw)_bar_z=w, (Cw)_z=Bw. Since q'=q/(q-1)<2, direct integration of |z-w|^(-q') over a disk gives

    ||Cw||_infinity,B_r <= C_q r^(1-2/q)||w||_q
                       <= C0 r ||psi||_infinity.

It is continuous and W1,q on the disk. This constructs a real-linear right inverse for L with the stated small-radius bound.

On the unit ball of Linfinity set Q(v)=beta+alpha v-|v|^2+mu v^2+nu bar v^2. Q is uniformly bounded and Lipschitz there. Shrinking r makes v -> L^(-1)Q(v) a contraction of that ball into itself. Hence a bounded continuous W1,q function v solves Lv=Q(v).

Put R=h-vu. The product rule is legitimate in W1,2: u,h are locally bounded, u is C1, and v is bounded W1,q with q>2. Direct expansion, retaining conjugates, gives

    LR=(alpha+mu v)R+(nu bar v-v)bar R.

The coefficient multiplying u is exactly beta+alpha v-|v|^2+mu v^2+nu bar v^2-Lv and is zero. The conjugates agree with the actual rendered page18 of Mercuri v2. If u(z0)=0 and R is zero on a disk centered at z0, then |Du|=2|vu|<=2|u|. Integration along radial segments and Gronwall imply u=0 on that disk. Consequently a nonzero u-germ at a zero produces a nonzero R-germ.

## 4. Factorization, including both denominator-zero sets

Let A0=alpha+mu v and B0=nu bar v-v. Set

    eta=mu+nu overline(R_z)/R_z on {R_z!=0}, zero otherwise,
    xi=A0+B0 bar R/R on {R!=0}, zero otherwise.

Then |eta|<=k and xi is bounded. The equation becomes R_bar_z=eta R_z+xi R almost everywhere. On {R_z=0} the derivative terms being absorbed are both zero, and on {R=0} the zero-order terms are both zero. Thus this reduction does not discard a singular-set equation.

The same right inverse, now for sigma_bar_z-eta sigma_z=xi, gives bounded continuous sigma in W1,q. Sobolev product and chain rules show that F=exp(-sigma)R is continuous W1,2 and solves F_bar_z=eta F_z. Measurable Riemann mapping and Stoilow yield F=G composed with chi, with G holomorphic and chi K-quasiconformal, where K=(1+k)/(1-k)=Lambda/lambda. Therefore

    R=exp(sigma)(G composed with chi).

For a nonzero R-germ, G is not identically zero. Zeros of R are isolated. If R(z0)=0, G has a finite order n>=1 there. On a smaller closed disk the continuous nonzero factors are bounded away from zero. Local 1/K-Holder continuity of chi inverse gives

    |R(z)|>=c|chi(z)-chi(z0)|^n>=c'|z-z0|^(nK).

No differentiability of chi or uniqueness of later trajectories is required.

## 5. Weak and pointwise strong continuation

The set D0 of points having a zero neighborhood is open. If a sequence in D0 tends to z0 in D, then u(z0)=0. If its germ were nonzero, the local R just constructed would be nonzero with isolated zeros, yet it would vanish on a nearby open subset where u and h vanish. This contradiction shows D0 is relatively closed. Connectedness proves weak continuation.

Now assume infinite pointwise value order at0. Then u(0)=Du(0)=0. A nonzero germ would yield R(0)=0 and |R(z)|>=c|z|^N for some finite N. Since v is bounded and u is flat in value, shrinking gives |Du(z)|=2|R+vu|>=c|z|^N on a punctured disk. Thus the continuous field n=Du/|Du| is defined there. Start a Peano trajectory at a point of radius r. It can be continued for time r/4, since its unit speed keeps it in the compact annulus 3r/4<=|z|<=5r/4. Finite continuation uses only continuity and boundedness on this annulus. It uses neither global completeness nor uniqueness. Along the trajectory,

    u(z(r/4))-u(z(0))=integral_0^(r/4)|Du(z(t))|dt
                    >=c1 r^(N+1).

For an integer j>N+1, both endpoint values have absolute value at most C_j(5r/4)^j. This is a contradiction for small r. Hence the germ is zero and weak continuation extends zero throughout D.

## 6. Actual Mercuri Theorem A and the integral conversion

The source is Carlo Mercuri, Unique continuation, nonexistence and bubbling for the critical p-Laplace equation in the plane, arXiv2609.34204v2,25 October2026. The audit read actual PDF text pages1-5,12-22 and26-30, including the complete Theorem A proof and bibliography. The page18 image was also inspected visually. Pages6-11 and23-25 were not read. No certification of Theorems B-E is intended.

Theorem A concerns 1<p<2 and real u in C1,alpha_loc solving -div(|Du|^(p-2)Du)=f(u), with f continuous and |f(s)|<=C_M|s|^(p-1) on each bounded scalar interval. It gives weak continuation and, for each point of a nonzero solution, positive c,r0 and finite m>=0 such that integral_Br|u|^p>=c r^m for0<r<r0. Its Remark1.1 describes an additional generalization whose analysis is omitted; that remark is not promoted here to a separately checked theorem.

Its Section2 imports Tolksdorf1984's weighted difference-quotient estimate. Bounded Du and p<2 turn that estimate into W2,2_loc. The original Tolksdorf proof was not independently read, and remains an explicit external regularity input. On {Du=0}, the Sobolev level-set property gives D2u=0 almost everywhere. Off that set the equation gives

    A:D2u=-f(u)|Du|^(2-p),
    A=I+(p-2)e tensor e, e=Du/|Du|.

Set A=I at critical points. The matrix has eigenvalues p-1,1 off them. Young's inequality bounds the right side by C(|u|+|Du|), including the critical set. Thus Sections2-4 apply with k=(2-p)/p and K=1/(p-1). This part of the source proof passes, subject to its named external regularity input.

For the integral conclusion, a point where u is nonzero gives m=2. At u=0 but Du!=0 a first-order Taylor estimate on a fixed cone gives m=p+2. At a common zero, |R|>=c r^(nK) yields integral_Br|R|^p>=c r^(nKp+2). Testing the original divergence equation by eta^p u and using Young's inequality and the bound on f gives

    integral_Br |Du|^p <= C r^(-p) integral_B2r |u|^p.

The test is compactly supported and admissible by density, and its cut-off gradient is O(1/r). Since |R|^p<=C(|Du|^p+|u|^p), this proves the lower bound with m=nKp+p+2 after rescaling2r. This Caccioppoli step uses the original divergence equation and is not silently imposed on arbitrary measurable nondivergence coefficients.

## 7. The conjugate weight and Euler limitation

Let m>2, let a be measurable and bounded above and below by positive constants locally, and let u in W1,m_loc solve div(a|Du|^(m-2)Du)=0 on a simply connected planar domain. The flux is locally in L^(m/(m-1)). The weak Poincare lemma gives a stream potential v in W1,p'_loc, p'=m/(m-1), with Dv=J2 a|Du|^(m-2)Du. Direct inversion, also at Du=0, gives

    a^(-1/(m-1))|Dv|^(p'-2)Dv=J2 Du.

Taking divergence yields a weighted p'-equation. Although1<p'<2, the factor a^(-1/(m-1)) remains. Positive upper and lower bounds for a do not bound its logarithmic derivative or even make that derivative a function. The actual Euler reduction also has a drift, so this simpler zero-divergence conjugation is not itself its full transformed equation.

Accordingly LIT263's real scalar theorem is CONFIRMED at its exact hypotheses, and the displayed steps of Mercuri's actual Theorem A proof pass with the external inputs explicitly named. Application to every flat Euler tail remains OPEN: the full-disk W2,2 potential, uniformly elliptic trace inequality and bounded lower-order terms still have to be supplied. Existing ratio-energy theorems retain their full-disk W1,2 ratio condition. No value of omega was excluded by this scalar audit, and no argument here derives the needed reduction for arbitrary omega or arbitrary helicity.
