# A decaying canonical pressure with arbitrarily large pointwise gradients

Status: CONFIRMED at the exact scope in A760-A762; the literal source sign error in A762 is refuted and corrected here.

## 1. Exact construction theorem

For any fixed 0<c<1 and finite real omega, there are smooth fields U:R3->R3 and P:R3->R satisfying

    div U=0, U in L2, DU in L3, grad P in L3,
    U(y)->0 and P(y)->0 uniformly,
    -Delta P=tr((DU)^2),
    P=partial_i partial_j Gamma*(U_iU_j), Gamma=1/(4pi|y|).

The pressure is also the absolutely convergent ordinary Newtonian potential of its L1 Poisson source. Nevertheless both |DU| and |grad P| can exceed every polynomial at points tending to infinity. In particular the following concrete version has centers z_n=(0,0,10^n), n>=1, and points |y_n-z_n|=ell_n/2 such that

    ell_n=2^(-n^2-4n),
    DU(z_n)=diag(2^(n^2+3n),-2^(n^2+3n),0),
    |grad P(y_n)|>=2^(n^2+2n)/3.

For A=cI-omega J, L=(1-c)I+omega J and J(x1,x2,x3)=(-x2,x1,0), the full momentum residual R=LU+(DU)(Ay+U)+grad P satisfies

    (DR)11(z_n)-(DR)22(z_n)=2^(n^2+3n+1)!=0.

Thus it fails exact momentum for every stated c and omega. There is no claim that R is small. The version ell_n=2^(-4n) has the simpler bounds DU(z_n)=diag(2^(3n),-2^(3n),0), |grad P(y_n)|>=2^(2n)/3 and the same conclusions except superpolynomial growth relative to |z_n|.

## 2. One compact smooth bump and its canonical potential

Let s(t)=exp(-1/t) for t>0 and s(t)=0 otherwise. Set

    chi(x)=s(4-|x|^2)/(s(4-|x|^2)+s(|x|^2-1)),
    psi(x)=chi(x)x1x2, v=(partial_2 psi,-partial_1 psi,0).

The denominator is positive. The cutoff is smooth, equals one on |x|<=1 and zero on |x|>=2. Hence v is smooth, compactly supported and divergence free, and v=(x1,-x2,0), Dv=diag(1,-1,0) on the unit ball. Put f=tr((Dv)^2). It is smooth and compactly supported, equals two in that ball, and incompressibility gives f=partial_i partial_j(v_iv_j).

Define p=Gamma*f by its ordinary integral. The local kernel |x|^-1 is integrable and f is smooth and compactly supported, so p is smooth and bounded, with -Delta p=f. One can see smoothness by moving all derivatives onto f in the compact convolution distribution. At infinity, separation from the support gives |D^j p(x)|<=C_j|x|^(-1-j). Integration by parts twice gives exactly p=partial_i partial_j Gamma*(v_iv_j), with no harmonic term. In particular the stronger bound |grad p|<=C|x|^-4 holds at infinity. The compact gradient is bounded, so grad p belongs to L3.

## 3. Scaling, smoothness and uniform decay

Let a_n=2^-n, z_n=(0,0,10^n), and choose either scale ell_n of Section 1. Set

    U_n(y)=a_n v((y-z_n)/ell_n),
    P_n(y)=a_n^2 p((y-z_n)/ell_n),
    U=sum_n U_n, P=sum_n P_n.

The balls B(z_n,2ell_n) are pairwise disjoint and escape every compact set. U is therefore a locally finite smooth divergence-free sum. Outside a large ball, only bumps with large n can remain, and their amplitudes tend to zero; hence U->0 uniformly. Disjoint supports give

    ||U||2^2=||v||2^2 sum_n a_n^2 ell_n^3<infinity,
    ||DU||3^3=||Dv||3^3 sum_n a_n^3<infinity.              (1)

The pressure series converges absolutely uniformly because ||P_n||infinity<=Ca_n^2 and sum a_n^2<infinity. Every fixed P_n tends to zero at infinity. Split into finitely many summands and a uniformly small remainder to prove P->0 uniformly.

Every derivative series converges on compact sets. Indeed, for y in a fixed compact set and sufficiently large n, |y-z_n|>=10^n/2, so

    |D^j P_n(y)|<=C_j a_n^2 ell_n (10^n/2)^(-1-j).

This is summable for all j>=0 in either construction. Therefore P is smooth, and termwise differentiation is valid locally. Also scaling gives ||grad P_n||3=a_n^2||grad p||3. The triangle inequality proves convergence of the gradient series in L3. Its L3 limit agrees distributionally with the derivative of the uniformly convergent P series, and hence with its smooth gradient. Thus grad P belongs to L3 as claimed.

## 4. The exact Poisson equation and canonical identity

Disjoint velocity supports imply

    f_U:=tr((DU)^2)=sum_n a_n^2 ell_n^-2 f((y-z_n)/ell_n),
    ||f_U||1<=||f||1 sum_n a_n^2 ell_n<infinity.            (2)

At any fixed evaluation point, the Newtonian potential Gamma*f_U converges absolutely. On a fixed nearby ball the source is smooth and bounded, so the kernel singularity is integrable; away from that ball the kernel is bounded and the source is L1. Absolute summation and the change of variables z=z_n+ell_n x show Gamma*f_U=P exactly. Consequently -Delta P=f_U.

Each individual P_n is the canonical pressure of U_n. The disjoint tensors sum to F_ij=U_iU_j, and the partial sums converge in L1 by (1). For a Schwartz test function, D_ij Gamma convolved with the test is bounded; therefore their canonical distributions converge when paired with it. The partial P sums also converge uniformly to P, hence distributionally. This proves P=D_ij Gamma*F_ij with no harmonic ambiguity. It is a specific canonical pressure, not a free choice among Poisson solutions.

## 5. A flux lower bound that includes all pressure interactions

In the core B(z_n,ell_n), all other velocity bumps vanish, and

    U(y)=kappa_n(y1,-y2,0), kappa_n=a_n/ell_n,
    DU=diag(kappa_n,-kappa_n,0), Delta P=-2kappa_n^2.

Apply the divergence theorem to the ball of radius t_n=ell_n/2 about z_n:

    integral_(sphere) grad P.normal=-2kappa_n^2 (4pi/3)t_n^3.

After division by the area 4pi t_n^2, some point y_n on that sphere has

    |grad P(y_n)|>=2kappa_n^2 t_n/3=a_n^2/(3ell_n).

This lower bound uses the total pressure. It does not assume that the pressure of the nth bump dominates the other pressures pointwise. The stated center derivative and gradient lower bounds follow by substituting the scales.

In the superpolynomial variant, |y_n|<=10^n+1. For any fixed finite N>=0, both 2^(n^2+3n)/(1+10^n)^N and 2^(n^2+2n)/(1+10^n+1)^N tend to infinity. Thus no polynomial pointwise upper bound for either gradient can hold, despite their L3 integrability.

## 6. Exact failure of the momentum equation

Let Q rotate by pi/2 about the third axis. The radial cutoff gives psi(Qx)=-psi(x), and differentiation gives v(Qx)=-Qv(x). Thus f(Qx)=f(x). Every z_n is fixed by Q, so U(Qy)=-QU(y), f_U(Qy)=f_U(y), and the rotation-invariant Newtonian kernel gives P(Qy)=P(y). At each center, P11=P22.

In the nth core, G=DU=D_n=diag(kappa_n,-kappa_n,0) is constant. Differentiating R=LU+G(Ay+U)+grad P there yields

    DR=LD_n+D_n A+D_n^2+D^2P
      =D_n+omega(JD_n-D_nJ)+D_n^2+D^2P.

The commutator has zero diagonal, and the first two diagonal entries of D_n^2 and D^2P are equal. Their difference in DR is therefore 2kappa_n, proving the displayed nonzero residual derivative. Exact full momentum is impossible in either version, for all c and omega.

## 7. Scope

This example retains actual curl, incompressibility, the exact pressure Poisson equation, the canonical pressure, finite velocity energy, critical L3 integrability of both gradients and uniform decay of U and P. It does not satisfy full Euler momentum. It therefore refutes no profile theorem or conditional derivative estimate. In particular A031/A500 normalize pressure but do not estimate its pointwise gradient; the construction is consistent with them. It distinguishes the normalization question from the missing estimate using full momentum.

Every step uses explicit smooth functions, distributional integration by parts, absolute convergence, scaling and the divergence theorem. No numerical experiment or formal build was needed. The full LIT129 source, including its added superpolynomial and L3 variants, was read and pinned. A focused existing configured-model comparison remains pending.

Source correction: Section4 equation(7) of the submitted LIT129 source has a missing minus sign in its second velocity component. Section5 above is the corrected identity. A762 refutes that literal display; A760-A761 confirm the corrected construction.
