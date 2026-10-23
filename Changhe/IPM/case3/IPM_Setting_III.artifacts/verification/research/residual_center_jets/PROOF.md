# Residual Taylor identities and the absence of derivative control

Result95. Independent derivation written 2026-10-21, before the companion checker. The first part audits the lead's00:08Z identities. The second is an explicit canonical counterexample to controlling residual derivatives by a value norm. Neither is a profile existence or nonexistence theorem.

## 1. Statement, notation and hypotheses

Let ell>1, A=2ell-1. Let rho be smooth, even in x and odd in y, on R2, with rho_y(0)=a!=0 and the prescribed sublinear density and first-derivative growth. Let psi be the canonical odd-odd stream function, -Delta psi=rho_x and U=(-psi_y,psi_x)=o(r). Write its origin expansions as

    rho = a y + b x^2 y + e y^3 + O(r^5),
    psi = s0 x y + q1 x^3 y + q2 x y^3 + O(r^6).

All coefficients here are Taylor monomial coefficients, not unscaled partial derivatives. In particular b=rho_xxy(0)/2 and e=rho_yyy(0)/6. Put

    C0 = ell+s0-1,
    W = ell X+U,
    R = W.grad rho-rho = r01 y+r21 x^2 y+r03 y^3+O(r^5).

There is no assumption R=0 or C0=0. Then

    q1+q2 = -b/3,
    r01 = a C0,
    r21 = (2A-C0)b+3a q1,
    r03 = (2+3C0)e+a q2.                                 (1)

Define the two compatibility defects by

    D1 = 6e-(a-2A)b,
    D2 = (q1-q2)-(a-4A)b/(3a).

They obey the exact identities

    D1 = r21+3r03-C0(9e-b),
    D2 = (2/(3a))(r21+C0 b).                             (2)

If F4(r)=pi^(-1)int_0^(2pi) rho_x(r,theta) sin(4theta)dtheta is the actual frequency-four Poisson source, then the absolutely convergent canonical moment is

    I4 = int_0^infinity r^(-3) F4(r) dr = q1-q2.          (3)

The lead writes F4 as f_2, indexing only even source frequencies. Equation(3) uses that convention, not the frequency-two source.

## 2. Direct Taylor proof

Differentiation of psi gives

    U1=-s0 x-q1 x^3-3q2 x y^2+O(r^5),
    U2= s0 y+3q1 x^2 y+q2 y^3+O(r^5).

The degree-two part of -Delta psi=rho_x is -6(q1+q2)xy=2bxy, which proves the first line of(1). The coefficient of y in R is a(ell+s0-1). The coefficient of x^2y is

    [2(ell-s0)+(ell+s0)-1]b+3a q1
       =(3ell-s0-1)b+3a q1=(2A-C0)b+3a q1.

The coefficient of y^3 is [3(ell+s0)-1]e+a q2=(2+3C0)e+a q2. This proves(1). Inserting these formulas into the right side of the first line of(2), and using 3a(q1+q2)=-ab, gives 6e-(a-2A)b. Likewise

    D2=2q1+b/3-(a-4A)b/(3a)
       =2q1+4Ab/(3a)=(2/(3a))(r21+C0 b).

No normalization is imposed twice. In applications C0 must come from the actual canonical inverse, even if the solver imposed a discrete strain relation.

## 3. Canonical frequency-four moment

Smoothness and parity give F4=O(r^4) at zero: the only possible degree-two source is a multiple of xy, of angular frequency two. The growth bound gives F4=O(r^(gamma-1)) at infinity. Thus r^(-3)F4 is O(r) at zero and O(r^(gamma-4)) at infinity, both integrable. The canonical coefficient P4 of sin(4theta) in psi is

    P4(r)=(1/8)[r^(-4)int_0^r s^5 F4(s)ds
                         +r^4 int_r^infinity s^(-3)F4(s)ds].

The source bounds give P4(r)=I4*r^4/8+O(r^6) at zero. Regularity excludes the homogeneous r^(-4) mode; U=o(r) excludes the homogeneous r^4 stream mode. The coefficient is therefore fixed by the full-plane inverse, not an arbitrary local harmonic datum. Since

    x^3y=(r^4/4)sin(2theta)+(r^4/8)sin(4theta),
    xy^3=(r^4/4)sin(2theta)-(r^4/8)sin(4theta),

the Taylor coefficient of r^4 sin(4theta) is (q1-q2)/8. Matching proves(3).

## 4. An explicit canonical perturbation with small residual values and large residual jets

Fix ell>1, D=ell-1 and a=4D. Define

    rho0(X)=a y exp(-r^2).

Choose a nonnegative C-infinity radial cutoff chi(r^2), equal to1 for r<=1/2 and zero for r>=1. Let

    sigma(X)=y r^2 chi(r^2),
    h_eps(X)=eps^p sigma(X/eps),
    rho_eps=rho0+h_eps,              1<p<3, 0<eps<=1.

Here p is a perturbation exponent and is unrelated to the far-field profile exponent1/ell. All these densities are smooth and have the prescribed symmetries and sublinear growth. Let their velocities be canonical. These are explicit non-profile test pairs; no exact transport is asserted.

For any radial factor rho=y f(r), the canonical stream is

    psi=-xy J(r),   J(r)=r^(-4)int_0^r s^3 f(s)ds.

Direct differentiation gives -Delta psi=rho_x; J(0)=f(0)/4, and the decaying or compactly supported f here gives J=O(r^(-4)) at infinity, hence U=O(r^(-3)). This proves canonicity by harmonic uniqueness. In particular, c[rho0]=-a/4=-D and c[sigma]=0. The unnormalized spatial scaling has U[h_eps](X)=eps^p U[sigma](X/eps), so c[h_eps]=eps^(p-1)c[sigma]=0. Therefore

    (rho_eps)_y(0)=a,  ell+(psi_eps)_xy(0)=1

hold exactly for every eps. This is not a change along the remaining normalized spatial scaling orbit: the common background is kept fixed and a compact perturbation is added.

Near zero, sigma=y r^2, so b_eps-b0=e_eps-e0=eps^(p-3). The radial stream formula gives

    (q1_eps-q1_0)=(q2_eps-q2_0)=-eps^(p-3)/6.

Formula(1), with C0=0 and a=4D, now gives

    r21_eps-r21_0=2ell*eps^(p-3),
    r03_eps-r03_0=((8-2ell)/3)*eps^(p-3).                  (4)

The first of these diverges as eps decreases to zero.

Nevertheless the residual differences are small in a weighted value norm:

    sup_(y!=0) |R_eps(X)-R0(X)|/|rho0(X)|
         <= C (eps^(p-1)+eps^(2p-2)) ->0.                 (5)

The quotient has its continuous parity extension across y=0. Here C can depend on ell,p and chi but not eps.

To prove(5), put V=U[sigma] and v_eps=U[h_eps]. The fixed radial compact source makes V smooth, odd-even/even-odd, and O(r^(-3)) at infinity. Consequently

    sup_X (|X| |V(X)|+|V2(X)/y|)<infinity.

The quotient is bounded near the axis by smoothness; for r>=1 the explicit radial formula J_sigma=C_sigma/r^4 gives the asserted bound directly. It follows that

    sup_X (r|v_eps|+|v_eps,2/y|)
       <= C(eps^(p+1)+eps^(p-1)).

Using grad rho0=a exp(-r^2)(-2xy,1-2y^2), one gets

    |v_eps.grad rho0|/|rho0|
       <= 2r|v_eps|+|v_eps,2/y|
       <= C eps^(p-1).

On the support r<=eps of h_eps, smooth parity of the fixed W0=ell X+U[rho0] gives |W0,1|<=C|x| and |W0,2|<=C|y|. Rescaling the polynomial-cutoff formula gives

    |h_eps|<=C eps^(p-1)|y|,
    |(h_eps)_x|<=C eps^(p-2)|y|,
    |(h_eps)_y|<=C eps^(p-1).

The same parities of V give |v_eps,1|<=C eps^p and |v_eps,2|<=C eps^(p-1)|y| there. Thus

    |W0.grad h_eps-h_eps|<=C eps^(p-1)|y|,
    |v_eps.grad h_eps|<=C eps^(2p-2)|y|.

Finally |rho0|>=a exp(-1)|y| on this support, and

    R_eps-R0=(W0.grad h_eps-h_eps)+v_eps.grad rho0+v_eps.grad h_eps.

This proves(5). Also h_eps has the same sign as rho0, so the prompt denominator Nf[rho_eps]>=|rho_eps|>=|rho0|. The same estimate therefore holds for |R_eps-R0|/Nf[rho_eps]. This controls the residual difference, not the full residual R_eps; it does not turn these examples into approximate profiles.

Equations(4)-(5) show that even common exact center normalization and uniformly small normalized differences in residual values do not control cubic residual jets. A finite set of samples supplies still less information. Thus the observed T1/T2 defects must be evaluated separately; they cannot be inferred from a small sampled residual floor.

## 5. Dependencies and verification scope

The first three sections depend only on Taylor calculus and the canonical modal Green formula, repeated with endpoint justification. The example uses an explicitly checked radial inverse and a compactly supported smooth cutoff. A separately implemented rational polynomial checker tests the Taylor coefficients, both defect identities, the residual effect of the perturbation, and source-moment constants on rational manufactured examples. Such checks support the algebra; they are not a certificate for a candidate or a substitute for the displayed analytic bounds. Actual Opus review of the new example remains pending.
