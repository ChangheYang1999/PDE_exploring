# Isotropic axial rank obstruction and the exceptional germ

Status: CONFIRMED A2055-A2060 after a complete six-section final read and exact arithmetic check. General extensions remain OPEN A2061. LIT283 treats a local analytic class, with no whole-space conclusion.

## 1. Exact statement and scalar jets

Let 1/3<c<1/2 and omega be any finite real number. Put

    a=1-2c, b=2(1-c), m=a/c in (0,1), sigma=omega/c,
    q=b/a=2(m+1)/m, h=m(m+1), Jx=e3 cross x,
    X=(cI-omega J)x, x*=e3.

Suppose f,Q are real analytic harmonic functions near x*, satisfying

    X.grad f=-af, X.grad Q=-bQ,
    f(x*)=1, f_1(x*)=f_2(x*)=0,
    D2f(x*)=h diag(-1/2,-1/2,1).

Define E=|grad f|^2/a^2, S=Q-E, F=grad f cross grad S. Then F cannot vanish with all derivatives through order five at x*. It cannot vanish through order four unless (c,omega)=(5/11,0). At this exceptional pair there are analytic harmonic f,Q in the stated class with Q nonzero and F of exact vanishing order five. Here vanishing order five means all derivatives of orders zero through four vanish and some fifth derivative is nonzero.

To track derivative counts, suppose F vanishes through order N, for N=4 or 5. Homogeneity gives grad f(x*)=-m e3. In analytic coordinates (f,u,v), the coefficients of df wedge dS are S_u,S_v. Their zero N-jet says every derivative of S of order at most N+1 containing u or v vanishes. Thus S has the same (N+1)-jet as a function Hfun(f). Differentiating homogeneity, using X.grad E=-bE, gives

    a Hfun^(j+1)(1)=(b-aj)Hfun^(j)(1), j=0,...,N.

Consequently S-D f^q has zero (N+1)-jet for a real D. With B=E+D f^q and G=Delta B, harmonicity of Q gives a zero (N-1)-jet of G. These implications concern finite jets only.

At x*, g=-m e3, H=D2f=h diag(-1/2,-1/2,1) and |H|^2=3h^2/2. The identity

    G=2|D2f|^2/a^2+Dq(q-1)f^(q-2)|grad f|^2

at G=0 fixes D=-(3/2)(m+1)(m+2).

## 2. Convergent modes and the forced nonzero cubic

Write zeta=x1+i x2, rho^2=x1^2+x2^2, z=x3. For an integer j>=0 define

    H_j^(M)=zeta^j z^(-M-j+i sigma j)
                  sum_(k>=0) A_k (rho^2/z^2)^k,
    A_0=1,
    A_(k+1)=-ell_k(ell_k-1)A_k/[4(k+1)(j+k+1)],
    ell_k=-M-j-2k+i sigma j.                               (1)

Use the real branch of log z on z>0. The recurrence follows by comparing the transverse and normal Laplacians. Its coefficient ratio tends to one, so the series and all its derivatives converge on compact sub-cones rho/z<1. Hence its real and imaginary parts are analytic harmonic functions. Homogeneity of each term gives X.grad H_j^(M)=-cM H_j^(M). Rotation cancels the imaginary homogeneity degree exactly.

At the axis, homogeneity determines all normal derivatives from transverse derivatives, and harmonicity determines each transverse trace from lower transverse orders. The hypotheses remove the harmonic transverse degrees one and two. Therefore through degree five every allowed f has the same jet as

    H_0^(m)+Re(C H_3^(m)+A4 H_4^(m)+A5 H_5^(m)),            (2)

for complex coefficients C,A4,A5. This is a finite-jet parameterization, not an assumption about the full function. A transverse rotation commutes with J and preserves the isotropic Hessian; whenever C!=0 it can make C positive real, since its phase changes by three times the rotation angle.

The axisymmetric part of T=D3f has T113=T223=h(m+2)/2 and T333=-h(m+2). Its transverse cubic is Re(C zeta^3). Counting symmetric entries gives

    |T|^2=(5/2)h^2(m+2)^2+144|C|^2.                        (3)

The first derivatives of G vanish automatically. Its transverse quadratic part is isotropic, and

    Delta G=[h^2(m-1)(m+5)+576|C|^2]/a^2.                  (4)

This follows by differentiating G twice, using Delta|D2f|^2=2|D3f|^2, Delta|grad f|^2=2|D2f|^2 and grad|grad f|^2=2(D2f)grad f. Equivalently it is the quadratic coefficient obtained from (1)-(2); the trace-free quartic contraction with the isotropic base Hessian vanishes. The scalar equation X.grad G=-2G forces second derivatives with normal indices to vanish once G and its first derivatives vanish. Thus the whole second jet vanishes if and only if

    |C|^2=h^2(1-m)(m+5)/576>0.                            (5)

In particular C cannot be zero. Any prospective rank four- or five-jet already requires this condition.

## 3. Angular separation and the only possible fourth-rank resonance

The homogeneous transverse cubic part of G decomposes uniquely as

    Re(K3 zeta^3)+rho^2 Re(K1 zeta).

Substitution of (1)-(2) gives

    K1=(576/a^2) conjugate(C) A4,
    K3=[3(m+1)(m+2)^2/m]
          [1-5m-18sigma^2+6i(m-2)sigma]C.                  (6)

The coefficients can be checked without assuming any unused jet. If ell=-m-3+3i sigma, the harmonic cubic part of |grad f|^2 is Re(m(3-m-6i sigma)C zeta^3), and that of |D2f|^2 is

    Re(3h[ell^2+(2m+3)ell+(m+2)(m+3)/2]C zeta^3).

The factor f^(q-2) contributes an additional (q-2)m^2 Re(C zeta^3). These give K3. The cross contraction of the transverse cubic and quartic Hessians gives K1. The fifth harmonic mode has a trace-free transverse Hessian and its contraction with the isotropic constant Hessian is zero. Thus A5 does not enter either coefficient. Harmonic degrees one and three are linearly independent, so neither can cancel the other.

Our independent check forms the first two normal derivatives in (1), differentiates in x1,x2, and extracts both cubic harmonics. It keeps arbitrary complex A4,A5 and, after the allowed rotation, positive real C. This loses no case: (6) transforms covariantly under the same rotation. Its question and exact zero-remainder criteria are in the team records.

If F vanishes through order four, Section 1 forces the zero third jet of G. Equation (5) and K1=0 give A4=0. Since C!=0, K3=0 implies

    1-5m-18sigma^2=0, (m-2)sigma=0.

For 0<m<1, this is equivalent to sigma=0 and m=1/5, hence omega=0 and c=5/11. Outside this pair the fourth-order rank vanishing is impossible.

## 4. The fourth trace rules out fifth-rank vanishing

If F vanishes through order five, G has zero four-jet, and Section 3 gives A4=0. Set M=h(m+2)(m+3). The axisymmetric part of Z=D4f has

    Z1111=Z2222=3M/8, Z1122=M/8,
    Z1133=Z2233=-M/2, Z3333=M.

Its squared full tensor norm is 35M^2/8. The other entries have three transverse indices and one normal index, from Re(ell C zeta^3), ell=-m-3+3i sigma. The cubic tensor norm is 144|ell C|^2 and the normal index has four positions, so

    |Z|^2=(35/8)h^2(m+2)^2(m+3)^2
                  +576[(m+3)^2+9sigma^2]|C|^2.            (7)

No fifth or higher potential derivative enters this formula.

For completeness set r=q-2=2/m, e=|g|^2, k=|H|^2, l=g.Hg, w=|Hg|^2 and z3=T(g,g,g), all at x*. The three product Laplacians of

    Delta(f^r e)=2f^r k+r(r-1)f^(r-2)e^2+4r f^(r-1)l

give

    L2=Delta^2(f^r e)
      =4|T|^2+6r(r-1)e k+24r(r-1)w
       +r(r-1)(r-2)(r-3)e^3
       +12r(r-1)(r-2)e l+12r g.grad k
       +8r tr H^3+8r(r-1)z3.                             (8)

One may verify each term with Delta k=2|T|^2, Delta(e^2)=4e k+8w, grad(e^2)=4e Hg, Delta l=2tr H^3+2g.grad k and g.grad l=2w+z3. Thus (8) does not conceal higher undetermined derivatives. Here

    e=m^2, k=3h^2/2, l=m^2h, w=m^2h^2,
    g.grad k=2m(m+2)k, tr H^3=3h^3/4,
    z3=m^3h(m+2).

Since Delta^2 k=4|Z|^2, equations (3),(5),(7)-(8) yield

    Delta^2 G=8|Z|^2/a^2+Dq(q-1)L2
      =3(1-m)(m+1)^2(m+2)^2
          [2m^2+27m+31+24(m+5)sigma^2].                   (9)

All factors are strictly positive for 0<m<1 and real sigma. This contradicts the zero four-jet of G, including at the exceptional pair. The exact factorization is independently checked by rational tensor arithmetic. At m=1/5,sigma=0 it equals 47672064/78125, though positivity alone suffices.

## 5. An analytic exceptional germ and its full local momentum equation

Take m=1/5, sigma=0 and C=sqrt(26)/250. Define

    f=H_0^(1/5)+C Re(H_3^(1/5)).                            (10)

The series converge in an invariant cone z>0,rho/z<1. At x*, its gradient and Hessian have the required values and C^2=13/31250 is exactly (5). Here a=1/11, q=12 and D=-99/25. For B=|grad f|^2/a^2+D f^q, equations (4),(6) give the zero transverse three-jet of G=Delta B. Homogeneity X.grad G=-2G recursively gives all normal derivatives in that jet, so its complete three-dimensional three-jet is zero.

Construct Q with X.grad Q=-bQ and the same five-jet as B as follows. Use the modes (1) with M=n=b/c=12/5. At each transverse degree j from zero to five, choose the new degree-j harmonic component to cancel the as-yet unmatched harmonic component of B's transverse jet. It cannot alter lower degrees. To justify the induction, the difference at degree j has zero transverse Laplacian: Delta B and Delta Q agree through degree j-2, and their normal second derivatives at this order agree by the common scalar homogeneity and the already matched transverse jets of degree j-2. Thus that difference is indeed a harmonic polynomial of degree j and can be removed by Re(C_j H_j^(n)). Common homogeneity also determines all mixed normal derivatives from transverse jets of no higher order. A finite sum of the convergent modes therefore realizes the entire five-jet. This is an analytic construction, not only a compatible formal jet.

At x*, Q=B=(m+2)(1-m)/2=22/25, so Q is not zero. The function S=Q-E agrees through order five with D f^q. Differentiating once gives F=grad f cross grad S with zero four-jet. Section 4 says its fifth jet cannot vanish. Its exact vanishing order is five.

To verify actual local Euler momentum, put phi=-f/a+Q, U=grad phi and P=Q-|U|^2/2. Harmonicity makes div U=0. For every harmonic potential phi and the present X, the left side of profile momentum is

    grad[a phi+X.grad phi+|U|^2/2+P].

Indeed differentiating X.grad phi contributes (cI+omega J)grad phi, whose rotation part cancels the explicit omega J U in momentum. Here a phi+X.grad phi=(a-b)Q=-Q, since b-a=1. Thus this gradient is zero exactly. In the exceptional construction omega=0.

On a sufficiently narrow invariant cone the leading tail V=-grad f/a has f>0, grad f!=0 and S=Q-E<0. On the angular section, E/|S| is bounded above and below by positive constants; homogeneity preserves these bounds. Under x->exp(t(cI-omega J))x, the Q contribution to U is one similarity order smaller than V because b-a=1. The exterior cone therefore has the stated natural velocity and derivative decay. It supplies no smooth origin, full angular extension, supported-vorticity interface or whole-space profile.

## 6. Combined scope and verification limits

A2049-A2053 already confirm the distinct-negative-eigenvalue axial case. The present confirmed isotropic case completes the local fifth-order obstruction for every negative-definite transverse Hessian at e3 with f=1 and zero transverse gradient. This union covers exactly those two spectral possibilities; it does not cover indefinite or degenerate transverse Hessians, points off the axis or nonzero transverse gradients.

The scalar reduction, harmonic traces, angular separation, positivity and finite analytic matching have all been written explicitly. The mode convergence and exact potential construction also agree with A1989-A1992 and A2028-A2032. Source snapshots and hashes are retained alongside the independent checker, prior plan and real execution times. The independent exact check took25.484994482714683 actual seconds; its fifteen zero-remainder checks, real start/end times and source code are retained. No numerical optimization or formal verification is claimed. A global supported-matching theorem, natural-regularity interface exclusion and unrestricted rotating nonexistence remain open.
