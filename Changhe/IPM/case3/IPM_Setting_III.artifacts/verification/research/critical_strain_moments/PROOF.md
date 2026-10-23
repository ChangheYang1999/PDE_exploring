# Critical strain moments and the limits of local nodal arguments

Date: 2026-10-20. This independently checks the additional claims in the lead's referee/kres1 analysis. The previously proved finite-order resonance, axis geometry, index count and exact trigonometric local model are dependencies in ../critical_far_field_zeros/PROOF.md. No full-class exclusion follows here.

## 1. Setting and the critical strain formula

Assume a smooth exact primary profile with ell>1, p=1/ell, D=ell-1, A=2ell-1 and its canonical full-plane velocity. We use the already proved symbol bounds |D^j rho|+|D^j U|<=C_j(1+r)^(p-j). Let q satisfy W(q)=0 and grad rho(q)=0. Then rho(q)=0 by transport. For z=r(cos theta,sin theta), put

    Q(z)=(sin(3theta),-cos(3theta))/(pi r^3).

The strain at q is the symmetric trace-free matrix with entry vector

    m(q)=integral rho(q-z) Q(z) dz,
    DU(q)=[[m1,m2],[m2,-m1]],    |DU(q)|_op=|m(q)|.           (1)

Indeed the off-zero velocity kernels are K1=-z1 z2/(pi r^4), K2=(z1^2-z2^2)/(2 pi r^4). Their derivative matrix is

    1/(pi r^6) [[z2(3z1^2-z2^2), z1(3z2^2-z1^2)],
                [z1(3z2^2-z1^2),-z2(3z1^2-z2^2)]].         (2)

Its independent entries are Q. The distributional contact derivatives are multiples of grad rho(q), hence zero. Alternatively integrate outside a small circle, subtract the constant and linear Taylor terms, and let its radius vanish. The remaining density is O(r^2), so the boundary error is O(r). The integrand in (1) has size O(r^-1) near zero and O(r^(p-3)) at infinity; both are integrable in two dimensions. This also justifies differentiation of the canonical integral at q. A symmetric trace-free matrix with entries m1,m2 has eigenvalues plus and minus sqrt(m1^2+m2^2), proving the norm statement.

At such a critical equilibrium, suppose the slow eigenvalue lambda_- of DW is nonpositive and lambda_+=2ell-lambda_-. Differentiating transport twice gives the homogeneous quadratic equation (lambda_- u partial_u+lambda_+ v partial_v) P2=P2, because rho and its first derivatives vanish there. The three quadratic weights are2lambda_-<=0, lambda_-+lambda_+=2ell>2, and2lambda_+>=4ell>4. None equals1, hence D^2 rho(q)=0. For a selected double escaping node the resonance fixes lambda_-=-A, lambda_+=4ell-1. The cubic weights are3lambda_-,2lambda_-+lambda_+=1,lambda_-+2lambda_+=6ell-1,and3lambda_+. Only u^2 v has weight1. The selected order2 coefficient has a nonzero linear coefficient along the fast branch, so its cubic density jet is a nonzero multiple of u^2 v. These claims use the exact transport equation, not the kernel alone.

## 2. The additional transport moment

At every q from Section 1,

    D m(q)=-integral rho(q-z)
                 [(U(q-z)-U(q)).grad]Q(z) dz.              (3)

To prove it put f(z)=rho(q-z), deltaU=U(q-z)-U(q), and V(z)=-W(q-z). The equilibrium condition gives V=ell z-deltaU, div V=2ell and V.grad f=f. Homogeneity gives z.grad Q=-3Q. Integrating the transport equation times Q on epsilon<r<R yields

    integral fQ=boundary integral fQ V.n
                       -integral f[2ell Q+V.grad Q].

The inner boundary is O(epsilon), using f=O(epsilon^2), V=O(epsilon), Q=O(epsilon^-3) and arc length O(epsilon). The outer boundary is O(R^(p-1)), hence tends to zero. The remaining expression is ell m+integral f deltaU.grad Q, proving (3). Its integrand is O(r^-1) near zero and O(r^(2p-4)+r^(p-4)) at infinity, so it is absolutely integrable.

The radial and normalized angular derivatives of Q are orthogonal, each of length 3/(pi r^4). Consequently

    |v.grad Q|=3|v|/(pi r^4),
    |DU(q)|_op <= 3/(pi D) integral
                |rho(q-z)| |U(q-z)-U(q)|/r^4 dz.            (4)

The simpler bound |DU(q)|_op <= (1/pi)integral |rho(q-z)|/r^3 dz also follows from (1). Neither right side has been bounded uniformly for exact profiles. The finite-order resonance from the cited dependency says a double escaping zero forces |DU(q)|_op=3ell-1. A strict upper bound below this value in (1) or (4) would exclude that double node, conditionally. Scaling rho_lambda(X)=lambda rho(X/lambda), q_lambda=lambda q leaves every displayed strain and moment invariant.

## 3. Why the kernel and nonnegative density do not give the missing upper bound

This section constructs non-profiles. Fix q=(2,0), ell>1, and a smooth nonnegative radial cutoff chi supported in radius1/10 and equal to one near zero. Set

    rho_b=y[chi(x,y)+(x-2)^2 chi(x-2,y)+(x+2)^2 chi(x+2,y)].

It is even in x, odd in y, nonnegative for y>0, has rho_y(0)=1, and equals y(x-2)^2 near q. For any prescribed a0>0 replace this base by a0 times itself. The following argument is unchanged, with the corresponding base velocity values, and fixes rho_y(0)=a0 and rho=a0 y(x-2)^2 near q. Let eta_delta be a nonnegative radial unit-integral smooth bump of radius delta. For a,b>0 form its parity quadruple

    B_(a,b)=eta_delta(x-a,y-b)+eta_delta(x+a,y-b)
                  -eta_delta(x-a,y+b)-eta_delta(x+a,y+b).

For small delta these supports avoid q and the origin. For a unit point mass quadruple, the values of U1(q) and partial_x U1(q), divided by 2/pi, are

    sum_(s=+-1) (2-sa)b/[(2-sa)^2+b^2]^2,
    sum_(s=+-1) b[b^2-3(2-sa)^2]/[(2-sa)^2+b^2]^3.           (5)

For (a,b)=(3,1), these are -41/169 and -1117/4394. For (a,b)=(1,1/2), they are 11552/34225 and -4564464/6331625. Continuity of the kernels on the bump supports preserves their strict signs at sufficiently small positive delta. Denote these actual smooth-bump values by u_R<0,s_R<0,u_L>0,s_L<0, and the base values by u_b,s_b.

For large t define t_L=(-2ell-u_b-tu_R)/u_L>0 and rho_t=rho_b+t B_(3,1)+t_L B_(1,1/2). Its canonical velocity satisfies U1(q)=-2ell and U2(q)=0 by parity, so W(q)=0. Its local density and center slope remain fixed, and

    partial_x U1(q)=s_b+(-2ell-u_b)s_L/u_L
                           +t(s_R-u_R s_L/u_L) -> -infinity.

The coefficient is negative because u_R s_L/u_L>0. Thus the critical strain is unbounded even with nonnegative upper-half-plane density, an actual canonical inverse, fixed center slope, and fixed cubic at q. These densities are compactly supported and do not satisfy transport. In fact the local cubic would force the finite value partial_x U1(q)=1-3ell. The origin strain and nonzero profile far field are also not imposed. This countertest does not contradict (3) and does not settle the profile question.

## 4. Transverse transport and a sign restriction

Let a regular nodal trajectory have finite transverse order k. Smooth scattering coordinates give D^j rho=0 on it for j<k, and D^k rho=h N^(tensor k), where N is a continuous unit normal and T=W/|W|. Differentiating transport k times leaves only the first-derivative commutator, because all lower density jets vanish. Contracting with N, and using N.N'=0, gives

    h'=[1-k N^T DW N]h.

Also (log|W|)'=T^T DW T and tr DW=2ell. Therefore

    (h/|W|^k)'=(1-2kell)h/|W|^k.                            (6)

In particular a coefficient that vanishes at the limiting saddle at backward infinite time need not vanish at a regular point of the branch. At infinity h is of size r^(p-k), |W| of size r and r of size exp(ell t); the resulting exponent ell(p-2k)=1-2kell agrees with (6).

For a selected critical node, meaning a maximum of the trapped-set potential, the dependency proves that both fast unstable branches escape. Suppose one has finite orders (k,j), with 1<=j<k and k lambda_-+j lambda_+=1. The same k and j apply to the other branch. Here is the matching detail. Restrictions of lower derivative tensors that vanish on one half of the smooth unstable curve are flat at its endpoint. On the opposite half, induction gives a homogeneous tensor ODE with coefficient O(1/|s|), since s'=lambda_+s+O(s^2). Integrating the norm bound for a nonzero solution gives a polynomial lower bound as s approaches0; such a solution cannot be flat. Thus the lower tensors vanish on that half also. The first scalar coefficient has leading nonzero Taylor term C s^j. Smoothness fixes this same leading term on both halves, and (6) preserves its nonzero sign along each half.

If this node is off the x-axis in y>0 and rho/a0>=0 throughout that half-plane, k must be even to avoid a transverse sign change. Its two leading transverse coefficients have relative sign (-1)^j, so j must also be even. Hence an off-axis selected double node is excluded by this additional sign condition, and any allowed finite order satisfies k>=4. The condition does not exclude an axis double node, whose two branches occupy opposite half-planes. The exact coupled trigonometric local model in the dependency already demonstrates that possibility outside the growth class.

## 5. The second far term gives a cancellation, not a contradiction

Use the verified expansion rho=r^p Theta0+r^(2p-1)Theta1+O(r^(3p-2)), with the corresponding smooth leading velocity u0, and

    Theta1=(p u0r Theta0+u0theta Theta0')/D.

At a double angular zero theta*, put T=Theta0''(theta*)!=0 and b=u0theta(theta*). Then Theta1(theta*)=0 and Theta1'(theta*)=bT/D. The escaping zero trajectory has

    theta(r)-theta*=-(b/D)r^(p-1)+o(r^(p-1)),

by integrating theta_r=(b/ell)r^(p-2)+o(r^(p-2)) toward infinity. If epsilon=r^(p-1), its first two density terms divided by r^p are

    (T/2)(-b epsilon/D)^2
                  +epsilon(bT/D)(-b epsilon/D)+o(epsilon^2)
       =-Tb^2 epsilon^2/(2D^2)+o(epsilon^2).

This has the order of the allowed remainder. If a third uniform expansion with a continuous coefficient Theta2 is separately available, exact vanishing forces Theta2(theta*)=Tb^2/(2D^2). No third expansion is asserted here.

For a direct test on an exterior sector, choose a smooth F and a constant B. The fields W_r=ell r, W_theta=BD r^p and rho=r^p F(theta+B r^(p-1)) have div W=2ell and exact transport. Indeed the angular-argument derivative along W vanishes since ell(p-1)+D=0. Their first three coefficients are F, BF' and B^2 F''/2. They realize the cancellation. They generally fail curl U=-rho_x, as curl U=BD(p+1)r^(p-1), and are not profile candidates.

## 6. Flat transport branches need not be degenerate saddles

At a critical equilibrium with eigenvalues 0,2ell every density jet vanishes: a hypothetical first homogeneous jet would solve 2ell v partial_v P=P, while each monomial has eigenvalue 2ell j, never1. Also a flat angular trace makes rho flat at each regular point of the corresponding exterior trajectory by smooth scattering coordinates. These are one-way implications.

For any lambda<0, mu=2ell-lambda and alpha=-lambda/mu>0, let W=(lambda u,mu v) and, away from the axes, set

    rho(u,v)=sgn(v)|v|^(1/mu)
                    exp[-1/(u^2 |v|^(2alpha))],

extended by zero on the axes. The argument u|v|^alpha is invariant along W, and the prefactor has transport weight1, so W.grad rho=rho. It is smooth and flat on both axes. To check this, every derivative off the axes is the exponential times finitely many powers of u and |v|. On a bounded neighborhood the variable Z=u^-2 |v|^(-2alpha) controls every prescribed inverse power of either coordinate. The limit Z^N exp(-Z)->0 therefore makes each derivative extend by zero. Induction proves smoothness and flatness. This is a hyperbolic saddle with a flat fast branch. It fails Darcy because curl W=0 but rho_u is nonzero. It disproves the inference from flatness to degeneracy for smooth transport alone, and leaves that inference for exact profiles open.

An additional absence of infinitely flat density points, for example real analyticity on the connected plane, would rule out these flat cases for a nontrivial exact profile. Combining that assumption with |DU(q)|_op<=ell at every nonzero critical equilibrium gives Hdyn: a selected node otherwise has lambda_-<=0 and strain ell-lambda_-; the bound forces lambda_-=0, and hence a flat density jet, contradicting the added assumption. Neither added condition is established for all smooth profiles.

## 7. Verification and scope

The separate test script differentiates the kernels, checks the exact point-bump fractions, the directional kernel norm, the transverse exponent, exterior cancellation and hyperbolic flat transport. It uses none of the lead's checking code. The existing independent critical-zero proof supplies the previously checked resonance, trigonometric local model, axis and index-count results. This audit identifies conditional bounds and compatible non-profiles; it neither verifies an admissible solution nor proves full-class nonexistence.
