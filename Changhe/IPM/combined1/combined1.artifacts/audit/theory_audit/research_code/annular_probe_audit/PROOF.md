# Independent compact-annulus weak-test audit

## Statement and hypotheses

Let rho and its divergence-free velocity U[rho] be smooth on the plane. Fix c, put V=cX+U[rho], F=V.grad rho-rho, and let U[h]=(-R1R2 h,R1^2 h), with Rj the Fourier multiplier i xi_j/|xi|. Suppose h is real, in L2, and satisfies

    F+div(Vh)-(2c+1)h+U[h].grad rho+div(h U[h])=0

as a distribution. No global integrability of F or bound on grad h is assumed. For R>0, let q(s)=(s-1)^2(4-s)^2 on [1,4] and zero elsewhere, and define

    phi_R=y q(r^2/R^2)/R^2,
    S(s)=(3c+1)q(s)+2csq'(s),
    W(s)=q(s)^2+[q(s)+2sq'(s)]^2,
    A^2=(pi/2) integral_1^4 s S(s)^2 ds,
    B^2=R^-4 integral_(R<r<2R) W(r^2/R^2)|U[rho]|^2,
    C^2=R^-4 integral_(R<r<2R) r^2 q(r^2/R^2)^2 |grad rho|^2,
    I=|<F,phi_R>|, D=A+B+C, H=108/R^2.

Then m=||h||2 satisfies I<=Dm+Hm^2. If I>0,

    m>=2I/[D+sqrt(D^2+4HI)].                            (1)

## Weak proof and constants

The multiplier norm ||U[h]||2<=||h||2 follows from its squared vector symbol xi1^2/|xi|^2. Thus h U[h] is integrable. Testing the distributional equation with a smooth compact function phi and integrating by parts gives

    |<F,phi>| <= m (||V.grad phi+(2c+1)phi||2
                      +||phi grad rho||2)
                    +m^2||grad phi||infinity.

Since q and q' vanish at both endpoints, phi_R is compactly supported and C1. Convolution with a smooth approximate identity converges in C1 on one fixed compact set, so every term in this inequality passes to phi_R. The linear factors are locally bounded, h and U[h] are locally square-integrable, and their product is locally integrable. This justifies the test without differentiating h.

One has cX.grad phi_R+(2c+1)phi_R=yS(s)/R^2. The derivative of the radial vector map X q(s)/R^2 is a symmetric matrix with eigenvalues q/R^2 and (q+2sq')/R^2. Its application to e_y equals grad phi_R, so its squared length is at most W/R^4. Also |phi_R|<=r q/R^2. Polar integration gives the displayed A. The triangle inequality gives D.

In z=(s-1)/3, the degree-four Bernstein coefficients of q are [0,0,27/2,0,0], and those of q+2sq' are [0,27,135/2,-108,0]. Nonnegativity and partition of unity of the Bernstein basis bound both eigenvalue magnitudes by108/R^2. This gives H. Solving the increasing quadratic proves (1), including its numerically stable form.

## Independent weak-background evaluation

For the rational single-scale potentials use t=r^2/(1+r^2), u=1-t, delta=1-1/c, a_j=(j+1)delta/2 and the polar fields

    rho=r sum R_(j,n)(t)u^a_j sin(n theta),
    psi=r^2 sum S_(j,m)(t)u^a_j sin(m theta), U=grad^perp psi.

Let T_(a,k)P=(k-2at)P+2tuP'. The field construction and this derivative identity are established in the independently audited polar implementation. Define J_b(P)=integral_(u0)^(u1) t P(t)u^b du, where u0=1/(1+4R^2), u1=1/(1+R^2). Let Q=q(t/(R^2u)) and E=Q+2s q'(s) at s=t/(R^2u). Then the signed pairing can be computed without any residual certificate as

    L=-pi/(2R^2) sum_(j,n=1) J_(a_j-3)(R_(j,1) S(s)),
    N= pi/(4R^2) sum_(|n-m|=1) J_(a_i+a_j-3)
          (R_(i,n)[sign(n-m)m S_(j,m) E
                         -T_(a_j,2)S_(j,m) Q]),
    <F,phi_R>=L+N.                                      (2)

Indeed <F,phi_R>=-integral rho[V.grad phi_R+(2c+1)phi_R]. The angular integral of sin(n theta)cos(m theta)sin(theta) is pi sign(n-m)/2 when |n-m|=1; that of sin(n theta)sin(m theta)cos(theta) is pi/2. Every other pair vanishes. Substitution of the polar velocity proves (2).

For B^2 and C^2, form the complete same-frequency sums of n^2PQ+T_(a,k)P T_(b,k)Q, including factor two for distinct branches. Use k=2 for psi and k=1 for rho. Integrate these polynomials against W or q^2, respectively, by pi J_(a+b-3)/(2R^4). The factor r^2 in C exactly compensates the missing factor r^2 in |grad rho|^2. This uses every angular mode.

## Exact integration and verification scope

A polynomial weight W(s) of degree d becomes u^-d sum_k W_k R^(-2k)t^k u^(d-k). Thus every integral in (2) and in B,C is a finite exact rational polynomial times a single rational power of u on a compact interval with positive endpoints. After substituting t=1-u, integrate each monomial: (u1^(e+1)-u0^(e+1))/(e+1) for e!=-1, and log(u1/u0) for e=-1. Outward Arb operations enclose the result. There is no radial quadrature or asymptotic replacement.

The verifier uses copied canonical potentials and this weak-background pairing. N4 instead pairs its full residual representation with the probe. Comparing the signed pairing, A,B,C,D,H and the radius therefore tests both a separate field derivation and a different integration identity. A successful finite-radius check proves (1) for that radius only; no optimization over all tests or radii is claimed.
