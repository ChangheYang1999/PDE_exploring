# Smooth elliptical shape exclusion

Date: 2026-10-21. Independent reconstruction of the elliptical proposal in the lead's `referee/rep6/answer.md`, extended here by a separate Volterra argument. Analytic verdict: CONFIRMED by the verifier's derivation below; independent model review of the extension is pending. This is a restricted-class theorem, not the primary NO endpoint.

## Statement and exact scope

There is no exact primary full-plane IPM profile of the form

    rho(x,y) = a y F(alpha x^2 + beta y^2),
    alpha>0, beta>0, a!=0, F in C^infinity([0,infinity)), F(0)=1.    (1)

Here smoothness of F includes all right derivatives at zero, equivalently a smooth extension across zero on a small interval. The primary assumptions are ell>1, even-x/odd-y density, odd-x/odd-y stream, U=(-psi_y,psi_x), -Delta psi=rho_x, (ell X+U).grad rho=rho, the canonical growth U=o(r), and for some 0<gamma<1,

    |rho|+(1+r)|grad rho| <= C(1+r)^gamma.

Neither F<=1 nor positivity, monotonicity or analyticity of F is assumed. The original proposal assumed F<=1 to invoke the separate flat-defect exclusion. Sections 4 and 5 remove that assumption for shapes (1). No finite angular expansion is assumed: a general anisotropic F can have infinitely many angular modes.

Set D=ell-1>0 and A=2ell-1=2D+1. The genuine dilation sends (alpha,beta) to (alpha/lambda^2,beta/lambda^2) and preserves a, ell and this subclass. The conclusion is thus invariant under the remaining scaling symmetry.

## 1. Bounds inherited by F

Put delta=(1-gamma)/2 in (0,1/2). On the positive vertical axis, s=beta y^2 gives

    rho(0,y)=a y F(s),    rho_y(0,y)=a(F(s)+2s F'(s)).

For s>=1 the primary bounds imply |F(s)|<=C s^(-delta) and |F(s)+2sF'(s)|<=C s^(-delta). Smoothness on compact intervals therefore gives

    |F(s)|+s|F'(s)| <= C(1+s)^(-delta),   s>=0.                 (2)

In particular F(s)->0 at infinity. Constants may depend on the proposed profile and on alpha,beta. No uniform bound over shapes is needed.

## 2. Independent full-plane inverse and its gauge

For t>=0 define

    a_t=alpha/(1+alpha t), b_t=beta/(1+beta t),
    s_t=a_t x^2+b_t y^2,
    omega(t)=(1+alpha t)^(-3/2)(1+beta t)^(-3/2).

The stream is

    psi(x,y)=-(a alpha/2) x y int_0^infinity F(s_t)omega(t)dt.    (3)

To verify it, direct Cartesian differentiation gives

    Delta[xy F(s_t)]
      =xy[6(a_t+b_t)F'(s_t)+4(a_t^2 x^2+b_t^2 y^2)F''(s_t)].

Since a_t'=-a_t^2, b_t'=-b_t^2 and omega'/omega=-3(a_t+b_t)/2, this is the identity

    omega Delta[xy F(s_t)] = -4xy d_t[F'(s_t)omega].             (4)

For fixed X, F'(s_t)omega tends to zero as t->infinity. Its value at t=0 is F'(alpha x^2+beta y^2). Thus (3)-(4) give

    Delta psi=-2a alpha xy F'(alpha x^2+beta y^2)=-rho_x.

The integral and every Cartesian derivative converge locally uniformly: on each compact X-set all F derivatives are bounded and omega=O((1+t)^(-3)); derivatives of s_t introduce only additional bounded factors. Hence psi is smooth and odd in each coordinate, with the required parities of U.

For the growth check, constants c,C>0 depending only on alpha,beta satisfy

    c r^2/(1+t) <= s_t <= C r^2/(1+t),
    omega <= C(1+t)^(-3),  |grad s_t| <= C r/(1+t).

Using (2) in the derivative of xy F(s_t), including its term xy F'(s_t)grad s_t, gives

    |grad psi| <= C r int_0^infinity (1+t)^(-3)
                                   (1+c r^2/(1+t))^(-delta)dt.

For r>=1 split the integral at 1+t=r^2. The part 1<=1+t<=r^2 is at most
C r^(-2delta) int_1^(r^2) u^(delta-3)du <= C r^(-2delta),
while the remaining part is O(r^(-4)). Thus |U|<=C r^(1-2delta)=C r^gamma=o(r). At bounded radii U is smooth. Formula (3) therefore has the canonical gauge.

For completeness, uniqueness of the velocity in this gauge does not require a boundary condition on an axis. The difference of two admissible velocities is divergence free and curl free, hence has harmonic components on the full plane and is o(r). The interior derivative estimate for an entire harmonic function, applied on discs of radius R and then R->infinity, makes its first derivatives zero. It is constant. The first component is odd in x and the second is odd in y, so both constants vanish. No harmonic xy stream is added to (3).

## 3. Center normalization and the nonflat contradiction

Let

    I_K=int_0^infinity (1+alpha t)^(-K)omega(t)dt,   K>=0,
    k=a alpha/2.

Then I_0>0 and 0<I_K<I_0 for every K>0, by pointwise comparison on t>0. Formula (3) gives c=psi_xy(0)=-k I_0. Differentiating exact transport in y at the origin gives ell+c=1 because rho_y(0)=a!=0. Consequently

    k I_0=D,    a>0.                                           (5)

The elementary integral also gives I_0=2/(sqrt(alpha)+sqrt(beta))^2, but this closed value is not needed for the proof.

Suppose F-1 is not flat at zero. For its first nonzero derivative, with integer K>=1,

    F(s)=1+f_K s^K+O(s^(K+1)),   f_K!=0.

All lower nonlinear density and stream terms vanish by (3). The coefficients of x^(2K)y in h=rho-ay and x^(2K+1)y in psi-cxy are respectively

    b_K=a f_K alpha^K,
    p_K=-k f_K alpha^K I_K.

Indeed the Taylor remainder in (3) is dominated uniformly by C r^(2K+2)omega, so the displayed stream expansion follows by integration. The degree-(2K+1) part of exact transport is

    (A x partial_x+y partial_y-1)h_(2K+1) + a v_(2K+1),2=0,

where v=U-(D x,-D y). Comparing x^(2K)y and using v_2=partial_x(psi-cxy) yields

    2K A = k(2K+1) I_K
          =D(2K+1) I_K/I_0 < D(2K+1).                        (6)

But

    2K A-D(2K+1)=(2K-1)D+2K>0,

a contradiction. This step needs no sign of f_K or F-1. It remains to exclude the smooth flat case without adding a sign hypothesis.

## 4. The exact axis equation as a Volterra equation

Put z=alpha x^2. Change variable u=(1+alpha t)^(-1) in (3), and define on [0,1]

    h(u)=beta+(alpha-beta)u,
    mu(u)=sqrt(alpha) u h(u)^(-3/2),
    J(z)=int_0^1 F(zu)mu(u)du.

Here mu is smooth, nonnegative, mu(0)=0, mu(1)=1/alpha, and int mu=I_0. Although h is only an auxiliary polynomial in this section, it is not the density defect used in Section 3.

On y=0, differentiation of (3) gives

    U_1(x,0)=k x J(z),
    partial_y U_2(x,0)=-k[J(z)+2z J'(z)].

Differentiate the full transport equation in y on this symmetry axis. The terms with rho_x and W_2 vanish there, while rho_y=aF(z) and rho_xy=2a alpha x F'(z). Thus, for z>0,

    2z(ell+k J)F' + [D-k J-2kz J']F=0.                     (7)

The density and inverse have been differentiated independently in Cartesian coordinates. No boundary condition was imposed on y=0.

Let g=F-1 and J_g(z)=int_0^1 g(zu)mu(u)du. By (5), ell+k I_0=A. Equation (7) is

    2z(A+k J_g)g'=k(1+g)[J_g+2z J_g'].                    (8)

Integration by parts in u transfers the derivative inside the bracket to the smooth weight:

    J_g+2z J_g' = 2 mu(1)g(z)+int_0^1 nu(u)g(zu)du,
    nu=mu-2(u mu)'=-3sqrt(alpha) beta u h(u)^(-5/2).       (9)

The boundary term at u=0 vanishes since u mu(u)=O(u^2). Therefore, with

    C_mu=2mu(1)+int_0^1 |nu(u)|du<infinity,
    M(z)=sup_(0<=s<=z)|g(s)|,

one has |J_g+2zJ_g'|<=C_mu M(z). These are finite constants for every fixed positive alpha,beta.

## 5. Flat uniqueness and propagation

Assume g is flat at zero. Choose r0>0 sufficiently small that |g|<=1 and |k J_g|<=A/2 on [0,r0]. Equations (8)-(9) give

    |g'(z)| <= C M(z)/z,    0<z<=r0,
    C=2k C_mu/A.                                           (10)

Choose an integer N>C. Flatness makes

    B_N=sup_(0<z<=r0) |g(z)|/z^N

finite. Since M(z)<=B_N z^N and g(0)=0, integrating (10) from zero to z gives

    |g(z)|<= C B_N z^N/N.

Taking the same weighted supremum gives B_N<= (C/N)B_N. Thus B_N=0 and g=0 on [0,r0]. This argument is a uniqueness estimate; it does not infer analyticity from smoothness.

The equality propagates to every finite z. Otherwise let Z be the finite supremum of intervals [0,z] on which g vanishes. It is positive, g=0 on [0,Z], and by continuity one may choose eps>0 so that |g|<=1 and |k J_g|<=A/2 on [0,Z+eps]. Define M_Z(z)=sup_(Z<=s<=z)|g(s)|. In (9) all values with zu<=Z vanish, so the same bound uses M_Z. For Z<=z<=Z+eps,

    |g'(z)|<=(C/Z) M_Z(z),
    M_Z(z)<=(C/Z)int_Z^z M_Z(s)ds.

If P(z)=int_Z^z M_Z(s)ds, then P(Z)=0, P>=0 and P'<=(C/Z)P. Multiplying by exp(-C(z-Z)/Z) proves P=0. This contradicts the definition of Z. Hence g=0 on [0,infinity), so F=1 everywhere. This violates F(s)->0 from (2).

The flat case and the nonflat case are both impossible, completing the theorem.

## Dependencies and verification evidence

The proof uses only the defining PDE, elementary differentiation, convergent one-dimensional integrals, the entire-harmonic uniqueness argument, and the explicitly proved Volterra estimate. It does not use the prior one-sided flat-exclusion theorem or any probabilistic or numerical evidence. Formal sources are absent because Lean/Lake work is prohibited in this run.

The separate script and its exact algebra records, when available in `verification/`, are supporting implementation checks. They are not a substitute for the quantified argument above. The unrestricted primary existence question remains UNRESOLVED.
