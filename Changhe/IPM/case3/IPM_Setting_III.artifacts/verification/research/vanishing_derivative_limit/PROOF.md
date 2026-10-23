# Exact global derivative residual limit of the vanishing family

Date: 2026-10-20. Status: independently proved and checked by exact rational integrals and a separate polar implementation (PASS 2026-10-20T19:16:45Z); actual Opus 5.5 review pending. This result concerns an explicit family of non-solutions, not the existence question.

## 1. Statement and definitions

For 0<D<=1 put ell=1+D, eta=D/(1+D), r=|X|, s=r^2, and

    f_eta(X)=(1+r^2)^(-eta/2),
    H_eta(X)=integral_0^1 t^3 f_eta(tX) dt,
    rho_D(X)=4D y f_eta(X),
    psi_D(X)=-4D xy H_eta(X), U_D=(-partial_y psi_D,partial_x psi_D),
    F_D=(ell X+U_D).grad rho_D-rho_D.

The velocity here is the canonical full-plane IPM inverse, as proved in ../vanishing_approximate_family/PROOF.md. These smooth fields have the required parities, sublinear growth, nonzero center slope and exact center strain. They are not solutions of transport.

Let D^3 denote the ordered third derivative tensor, with its Euclidean contraction and Lebesgue L2 norm on the whole plane. Define

    G(X)=-2y log(1+r^2), H(X)=-4y r^2/(1+r^2).

Then, as D decreases to zero, both limits hold in global L2:

    D^3 rho_D / D^2 -> D^3 G,
    D^3 F_D / D^2 -> D^3 H.                              (1)

Consequently the scale invariant derivative residual satisfies

    ||D^3 F_D||_2 / ||D^3 rho_D||_2 -> sqrt(12/7).         (2)

In particular this global residual does not tend to zero, although the two pointwise relative residuals of this same family are at most 4D. All conclusions remain true for the ratio after any D-dependent positive spatial dilation, including the representative with fixed nonzero far-axis amplitude. No uniform global norm convergence of the dilated tensors themselves is asserted.

## 2. Uniform derivative estimates

For every integer j>=1 there is a constant C_j independent of 0<=eta<=1/2 such that

    |D^j f_eta(X)| <= C_j eta (1+r)^(-j).                 (3)

To see this, repeated differentiation of f gives a finite sum of terms

    c (eta/2)(eta/2+1)...(eta/2+k-1)
      X^beta (1+r^2)^(-eta/2-k),

where 1<=k<=j and |beta|=2k-j>=0. The coefficient product is bounded by a constant times eta, and r^(2k-j)(1+r^2)^(-k)<=C_j(1+r)^(-j). The value f itself lies between zero and one. The formula also proves smooth dependence on eta in every local C^j norm, including eta=0.

Differentiating the defining integral of H_eta gives, for j>=1,

    |D^j H_eta(X)| <= C_j eta integral_0^1 t^(3+j)(1+tr)^(-j)dt
                    <= C_j eta (1+r)^(-j).              (4)

For the last inequality, t/(1+tr)<=1/(1+r) for 0<=t<=1. Also |H_eta|<=1/4. These estimates are uniform down to eta=0, and H_eta depends smoothly on eta locally with all derivatives. For its scalar representation h_eta(s), differentiation in s gives

    |h_eta^(k)(s)| <= C_k eta (1+s)^(-k), k>=1,           (5)

by the same proof using t^2/(1+s t^2)<=1/(1+s). All derivatives in (3)-(5) at eta=0 vanish when their order is positive.

The third derivative of y f_eta contains only terms y D^3 f_eta and constant multiples of D^2 f_eta. Equations (3) and eta/D=1/(1+D)<=1 therefore show

    |D^3 rho_D(X)/D^2| <= C (1+r)^(-2).                  (6)

There is no divergent derivative of the linear term y, because its third derivative is zero.

## 3. Exact residual, with the axes removed from the formula

Write q=s/(1+s). The exact residual quotient established by direct differentiation of the canonical stream is

    F_D / D^2 = 4y f_eta [ (1-q)-4H_eta
                    -4(x^2/s)(f_eta-4H_eta)
                    -4eta (x^2-y^2) H_eta/(1+s) ].       (7)

Its apparent singularity at s=0 is removable. Indeed r partial_r H_eta=f_eta-4H_eta, so f_eta-4H_eta=2s h_eta'(s). Thus (7) is identically the smooth Cartesian expression

    F_D/D^2 = 4y f_eta ( B_0(s)+x^2 B_2(s) ),
    B_0=(1+s)^(-1)+(-4+4eta)h_eta-4eta h_eta/(1+s),
    B_2=-8h_eta'-8eta h_eta/(1+s).                       (8)

This formula also verifies all factors in the limit without dividing by y or taking a numerical axis limit.

For k>=0, (5) and |h_eta|<=1/4 give

    |B_0^(k)(s)| <= C_k(1+s)^(-k),
    |B_2^(k)(s)| <= C_k(1+s)^(-1-k).                    (9)

Multiplication by f_eta preserves these estimates. If a scalar function b(s) obeys |b^(k)(s)|<=C_k(1+s)^(-w-k), then the same differentiation expansion as in Section 2 gives |D^j b(r^2)|<=C_j(1+r)^(-2w-j). Apply this for w=0 and w=1 to the two summands of (8). The polynomials y and x^2 y have degrees 1 and 3, respectively. Leibniz's rule now gives the uniform global bound

    |D^3 F_D(X)/D^2| <= C(1+r)^(-2).                    (10)

These bounds hold for the full ordered derivative tensor, not merely its radial part. They include the origin and both symmetry axes. They use only four s-derivatives of h_eta and three of f_eta, so no unproved all-order interchange is needed for (1).

## 4. Local limits and passage to the whole plane

On every compact set,

    (f_eta-1)/eta -> -log(1+r^2)/2

with all derivatives. Since D^3 y=0 and eta/D->1, this proves the first local C0 limit in (1). In (8), at eta=0 one has f_0=1, h_0=1/4 and h_0'=0. Hence B_0=(1+s)^(-1)-1=-s/(1+s), B_2=0, proving the second local limit with all derivatives.

The square of C(1+r)^(-2) is integrable over R^2. Equations (6) and (10), together with their pointwise limits, therefore permit dominated convergence of the squared tensor differences. This proves both global L2 limits in (1). In particular the limits are not inferred merely from compact convergence or from a finite-box calculation.

## 5. Evaluation of the limiting integrals

For a scalar function P=y b(s), the ordered third derivative is

    partial_ijk P = y[4(delta_ij X_k+delta_ik X_j+delta_jk X_i)b''
                       +8 X_i X_j X_k b''']
      +delta_i2[2delta_jk b'+4 X_j X_k b'']
      +delta_j2[2delta_ik b'+4 X_i X_k b'']
      +delta_k2[2delta_ij b'+4 X_i X_j b''].

For G take b=-2log(1+s), and for H take b=-4s/(1+s). Squaring this tensor and integrating its rational terms gives

    ||D^3 G||_2^2 = 512 pi/5,
    ||D^3 H||_2^2 = 6144 pi/35.                          (11)

A reproducible exact integration rule for every nonzero even monomial is

    integral_R2 x^(2a)y^(2b)/(1+r^2)^m dX
       = Gamma(a+1/2) Gamma(b+1/2) Gamma(m-a-b-1)/Gamma(m),

for integers a,b>=0 and m>a+b+1. It follows directly by polar coordinates and the beta integral; odd monomials integrate to zero. Substitution of the displayed derivative formula and the elementary derivatives of b establishes (11). The exact ordered-tensor calculation and two calibration integrals are recorded in ../global_derivative_residual/verification/formal_limit_integrals.json. The independent ordered-tensor polar check in verification/polar_crosscheck.json reproduces both limiting integrals with 96, 192 and 384 radial points and checks nine finite values of D. At D=0.0001 it gives ratio 1.30931982196, approaching sqrt(12/7)=1.30930734142. These numerical checks support the finite algebra, but the global convergence proof is Sections 2-4.

The first norm in (11) is positive. Taking ratios in the proven L2 limits yields (2). Under rho_lambda=lambda rho(X/lambda), F_lambda=lambda F(X/lambda), both third derivative L2 norms scale by lambda^(-1), so the ratio is unchanged, proving the stated dilation scope.

## 6. Dependencies and scope

The only previous analytic dependency is the exact canonical stream and residual of the explicit family, whose derivation is restated in (7)-(8). No numerical result is used to prove global convergence. The rational integrals can be checked by the stated finite algebra and beta formula. This is a quantitative failure test for small pointwise residuals near ell=1. It neither excludes all primary profiles nor describes the limit of any computed solver sequence.
