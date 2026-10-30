# A global weak residual test, independently audited

Written 2026-10-28. This proof was written and checked before running its numerical reproduction. The frozen target is source/N4_PROOF.md. It extends the independently audited compact test in T2-R3. All integrals and norms below are over the full plane unless another domain is displayed.

## 1. Exact statement and scope

Let c be real. Let rho and its canonical incompressible velocity u=U[rho] be smooth, with u(X)=O(|X|^gamma), D rho(X)=O(|X|^(gamma-1)) at infinity for some gamma<1. The Fourier vector multiplier of U has Euclidean modulus at most one. Set V=cX+u and F=V.D rho-rho. Fix an integer p>=2, and assume F phi_p is integrable, where

    phi_p(x,y)=y(1+x^2+y^2)^(-p).

If h belongs to H^(2+s)(R^2), s>0, and rho+h solves the stationary equation with this same c in distributions, then, writing m=||h||_2 and d=||D h||_infinity,

    |<F,phi_p>| <= m [A_p+(1+2p)B_p+C_p+d N_p],                 (1)

where, with u0=(1+r^2)^(-1), t=1-u0,

    N_p=||phi_p||_2,
    A_p=||phi_p[(3c+1)-2cp t]||_2,
    B_p=||u0^p u||_2,
    C_p=||r u0^p D rho||_2.

Here d is the essential supremum of the Euclidean gradient norm. For a high-norm ball X_(s,w)(h)<=R, with

    X_(s,w)(h)^2=||omega D^2 J^s h||_2^2
                 +w1||D J^s h||_2^2+w2||J^s h||_2^2,
    J=(1-Delta)^(1/2), omega>=1, w1>=2, w2>=1,

one may take

    m=R/sqrt(w2),  d=R/sqrt(4 pi s(1+s)).                       (2)

The D^2 norm is the full ordered tensor norm. A rigorously positive gap in (1) rules out this ball at the fixed c, without any sufficient inverse or background-coercivity hypothesis. It does not rule out larger corrections, a change of c, or arbitrary exact solutions.

## 2. Proof of the necessary inequality

Subtract the stationary equation for rho from that for rho+h:

    0=F+V.Dh-h+U[h].D rho+U[h].Dh.

For a compactly supported smooth real test phi, integration by parts, div u=0 and div V=2c give

    <F,phi>=<h,V.Dphi+(2c+1)phi>
             -<U[h],phi D rho>-<U[h].Dh,phi>.

Plancherel gives ||U[h]||_2<=m. Cauchy-Schwarz and the L-infinity gradient bound therefore give

    |<F,phi>|<=m (||V.Dphi+(2c+1)phi||_2
                    +||phi D rho||_2+d||phi||_2).               (3)

Take phi=chi_R phi_p with a radial smooth cutoff equal to one on r<=R and zero on r>=2R, and ||D chi_R||_infinity<=C/R. The assumed sublinear growth implies that phi_p, V.Dphi_p and phi_p D rho belong to L2. The cutoff error phi_p V.D chi_R has norm bounded by a constant times the L2 norm of phi_p on R<=r<=2R, and hence tends to zero. The left side converges by the assumed integrability of F phi_p. Thus (3) holds for phi_p.

Direct differentiation yields

    Dphi_p=e_y u0^p-2p y X u0^(p+1),
    |Dphi_p|<=(1+2p)u0^p,
    cX.Dphi_p+(2c+1)phi_p=phi_p[(3c+1)-2cp t].

Use the triangle inequality for the u.Dphi_p term and |phi_p|<=r u0^p. This proves (1).

To prove (2), the polynomial inequality z^2+w1 z+w2>=(1+z)^2 for z>=0 and omega>=1 show ||h||_(H^(2+s))<=X_(s,w)(h). Plancherel gives the L2 bound. Fourier Cauchy-Schwarz gives the Euclidean-gradient bound

    ||D h||_infinity <= ||h||_(H^(2+s))/sqrt(4 pi s(1+s))

under the campaign's standard two-dimensional Fourier normalization. Indeed the integral of |xi|^2(1+|xi|^2)^(-2-s), divided by (2pi)^2, equals 1/[4pi s(1+s)]. This proves the stated sufficient upper bounds m,d.

## 3. Independent polar construction and integration

This reproduction starts only from the canonical rational potential coefficients. It neither imports the N4 field code nor reads its cached residual. Define delta=1-1/c and a_j=(j+1)delta/2. With T=t and W=1-t, the rational potential construction gives finite polar expansions

    rho=r sum_(j,n) W^(a_j) R_(j,n)(t) sin(n theta),
    psi=r^2 sum_(j,n) W^(a_j) S_(j,n)(t) sin(n theta).

Here n is positive, and u_r=-(1/r)partial_theta psi, u_theta=partial_r psi. The canonical potential-to-density and stream formulas were independently verified in T4-018 and T4-031. The present code repeats their rational construction. In particular the cancellation of the first two powers of t is checked exactly before division by t^2.

For a polynomial P define

    T_(a,k)P=(k-2at)P+2t(1-t)P'.

Differentiation then gives

    partial_r rho=sum W^a T_(a,1)R sin(n theta),
    partial_theta rho/r=sum W^a nR cos(n theta),
    u_r=-r sum W^a nS cos(n theta),
    u_theta=r sum W^a T_(a,2)S sin(n theta).

For each pair of branches i,j with the same harmonic n, B_p^2 is the sum of

    (pi/2) integral_0^1 t W^(2p-3+a_i+a_j)
            [n^2 S_i S_j+T_(a_i,2)S_i T_(a_j,2)S_j] dt,         (4)

and C_p^2 is the sum of

    (pi/2) integral_0^1 t W^(2p-3+a_i+a_j)
            [T_(a_i,1)R_i T_(a_j,1)R_j+n^2 R_i R_j] dt.         (5)

Unordered off-diagonal pairs have multiplicity two. The factor pi is the integral of the square of a nonzero sine or cosine. The factor 1/2 and t W^-3 follow from r^3 dr=(1/2)t W^-3 dt.

For additional independence the signed pairing is computed directly from the weak background equation, without constructing F:

    <F,phi_p>=-<rho,cX.Dphi_p+(2c+1)phi_p>-<rho,u.Dphi_p>.

The linear contribution, only for n=1, is

    -(pi/2) sum_j integral_0^1 t W^(a_j+p-3) R_(j,1)
                              [(3c+1)-2cp t] dt.               (6)

The nonlinear contribution consists only of density harmonics n and stream harmonics m with |n-m|=1. Put sigma=sign(n-m). Its contribution for branches j,k is

    (pi/4) integral_0^1 t W^(a_j+a_k+p-3) R_(k,n)
        [sigma m S_(j,m)(1-2pt)-T_(a_j,2)S_(j,m)] dt.           (7)

To verify the signs, the two angular integrals are

    integral sin(n theta)cos(m theta)sin(theta) dtheta
         =sigma pi/2,
    integral sin(n theta)sin(m theta)cos(theta) dtheta=pi/2.

All other angular pairs vanish. Boundary terms in the background integration by parts vanish: for p>=2 and gamma<1, the linear radial boundary is O(r^(gamma+3-2p)) and the nonlinear one O(r^(2gamma+2-2p)), both tending to zero. Smoothness removes the origin boundary.

Finally

    N_p^2=pi/[2(2p-1)(2p-2)],
    A_p^2=(pi/2) integral_0^1 t W^(2p-3)[(3c+1)-2cp t]^2 dt.     (8)

Every polynomial combination and shift t=1-W is formed exactly over the rationals before integration. If Q(W)=sum q_l W^l, then

    integral_0^1 W^b Q(W) dW=sum_l q_l/(b+l+1),

provided each nonzero summand has b+l>-1. The code checks this condition. Arb encloses the finite sums, pi, square roots and the final gaps. There is no quadrature, finite-radius truncation or floating coefficient conversion.

## 4. Verdict and dependencies

The frozen N4 analytic claim is CONFIRMED, with the notation clarification that its u=(1+r^2)^(-1) is a scalar separate from the velocity. The signs of the displayed canonical velocity convention do not affect the Plancherel bound, but the actual signed pairing uses the campaign's already audited potential convention. Numerical exclusions await execution and comparison with an independently produced N4 record. Evidence will be stored in verification/ and the append-only top-level ledger.

Dependencies: integration by parts, Plancherel, Fourier Sobolev embedding, the rational polar construction in T4-018/T4-031, angular orthogonality, and outward Arb arithmetic. No formal source or Lean build is claimed or run.
