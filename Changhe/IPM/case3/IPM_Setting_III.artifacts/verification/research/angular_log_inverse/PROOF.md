# A second full-plane inverse for weighted diagnostics

Date: 2026-10-20. Status: independently derived formulas; implementation
verification pending. This is an evaluation method, not an existence result.

## Statement, domain and notation

Let a smooth even-x, odd-y density have finitely many angular modes

    rho(r,theta)=r sum_(j=0)^(M-1) b_(2j+1)(s) sin((2j+1)theta),
    s=log r.

Suppose rho and its gradient obey the primary sublinear growth hypothesis,
and the polar formula extends smoothly through zero. Put a=rho_y(0).
Then b_1(s)=a+O(exp(2s)), b_(2j+1)(s)=O(exp(2j s)) for j>=1 as
s tends to minus infinity. Write h_1=b_1-a and h_m=b_m for odd m>=3.
An absent angular mode is zero. Define, for each even n>=2,

    alpha_n(s)=integral_0^infinity exp(-(n+2)z)b_(n-1)(s-z) dz,
    beta_n(s)=integral_0^infinity exp(-(n-2)z)b_(n+1)(s+z) dz.  (1)

For n=2 the latter has no exponential weight, but still converges at both
physical endpoints by smoothness and sublinear growth. All integrals are
absolutely convergent. The canonical stream is

    psi(r,theta)=r^2 sum_(n=2,4,...,2M) p_n(s) sin(n theta),
    p_n=(beta_n-alpha_n)/2,                              (2)

and psi_r/r has coefficients

    d_n=[n(alpha_n+beta_n)-b_(n-1)-b_(n+1)]/2.           (3)

In particular c=psi_xy(0)=-a/4+beta_2(-infinity). These are full-plane
formulas; no finite-radius homogeneous closure is added.

## Derivation and gauge

For f_m(r)=r b_m(log r), Cartesian differentiation gives the even sine
coefficient of rho_x at frequency n:

    q_n=(f'_(n-1)-(n-1)f_(n-1)/r)/2
         +(f'_(n+1)+(n+1)f_(n+1)/r)/2.

The radial Green solution of -Delta psi=rho_x is

    psi_n(r)=[r^(-n) integral_0^r t^(n+1)q_n(t)dt
               +r^n integral_r^infinity t^(1-n)q_n(t)dt]/(2n).

One integration by parts in each integral cancels their boundary terms
at r. The remaining expression is

    psi_n(r)=[-r^(-n) integral_0^r t^n f_(n-1)(t)dt
                    +r^n integral_r^infinity t^(-n)f_(n+1)(t)dt]/2.

The terms at zero vanish by smoothness. The terms at infinity vanish
because f_m=O(r^gamma), gamma<1<n-1. Substituting t=r exp(-z) and
t=r exp(z), respectively, proves (1)-(2). Differentiating the two radial
integrals proves (3). Thus the same angular Green law is evaluated with
logarithmic convolution kernels, not a compactified collocation inverse.

The solution is smooth locally since it solves Poisson with a smooth
source and has the regular radial behavior at zero. The whole-plane
velocity has the required parity. At infinity, these formulas give
psi_n=O(r^(gamma+1))+O(r^(-n)) and psi_n'=O(r^gamma)+O(r^(-n-1));
possible borderline logarithms from the lower integral are absent here,
since its upper large-r power is n+gamma>-1. Hence U=o(r).
A difference of two smooth full-plane velocities with the same div-curl
and sublinear velocity growth has harmonic components. A harmonic
function of sublinear growth is constant by the interior gradient bound
on larger and larger balls. Parity removes those constants. This proves
that (2) is the canonical inverse. No harmonic xy term remains adjustable.

## Removing the affine cancellation before numerical integration

Let beta20=integral_(-infinity)^infinity b_3(s)ds and c=-a/4+beta20.
Set

    A_2=integral_0^infinity exp(-4z)h_1(s-z)dz,
    B_2=-integral_(-infinity)^s b_3(t)dt.

For n>=4 use A_n=alpha_n and B_n=beta_n. Then the coefficients of
phi/r^2 and phi_r/r, where phi=psi-cxy, are

    P_n=(B_n-A_n)/2,
    D_n=[n(A_n+B_n)-h_(n-1)-h_(n+1)]/2.                (4)

At n=2 this is an algebraic cancellation of alpha_2=a/4+A_2 and
beta_2=beta20+B_2, before evaluation. Consequently no subtraction of
large affine velocity values is needed to obtain v=(-phi_y,phi_x).
Writing v_r/r=V_r, v_theta/r=V_theta gives

    V_r=-sum n P_n cos(n theta),
    V_theta=sum D_n sin(n theta),
    U_r/r=-c cos(2theta)+V_r,
    U_theta/r=c sin(2theta)+V_theta.                   (5)

These exact formulas do not make a finite quadrature exact. Both the
logarithmic quadrature order and the radial/angle energy grids must be
refined and compared with the separate Cartesian cancellation inverse.

## Finite Q densities and exact third-mode primitives

For the frozen Q representation, put sigma=(1+t)/2, w=1-sigma,

    r=L 2^(-kappa) sigma^(1/2) w^(-kappa),
    rho/r=w sin(theta) sum_(k=0)^(M-1) sigma^k B_k(2sigma-1)cos(2k theta).

The B_k are scalar polynomials read from the frozen coefficients. Simple
sine multiplication yields

    b_1=w[B_0-sigma B_1/2],
    b_(2j+1)=w[sigma^j B_j-sigma^(j+1)B_(j+1)]/2, j>=1. (6)

The center value is a=B_0(-1). The smooth map has sigma=O(r^2), so the
formula is smooth at the origin and obeys the angular vanishing orders.
The density exponent is1-1/kappa<1 when kappa>1, with the stated gradient
bound. Both endpoint mode assertions follow directly from this formula.
The identity

    d(log r)/d sigma=1/(2sigma)+kappa/w

turns the low-mode integral into a polynomial primitive:

    integral_(-infinity)^s b_3(t)dt
      =integral_0^sigma [w(u)/4+kappa u/2]
                         [B_1(2u-1)-u B_2(2u-1)]du.    (7)

Gauss-Legendre with enough points integrates this polynomial exactly in
real arithmetic. Roundoff and coefficients still require separate checks.
The same expression at sigma=1 gives beta20. In particular the canonical
strain includes the local -a/4 term, which cannot be discarded.

A stable evaluation of h/r can use the polynomial C defined by
B_0(t)-a=(t+1)C(t). Its first coefficient in (6) becomes

    h_1=sigma[2w C-a-w B_1/2].                          (8)

This removes the small-center subtraction before numerical evaluation.
The quotient may be computed from exact binary-rational coefficients and
then rounded, or checked at increased precision. A division algorithm
with a discarded nonzero roundoff remainder is not an exact identity.

## Weighted residual without overflowing physical powers

Let H=h/r=sum h_m sin(m theta), dot H=partial_s H and Htheta=partial_theta H.
For arbitrary ell>1 let delta=ell+c-1 and F=R-a delta y, with R the
unforced residual. Direct substitution or result62 gives

    F/r=(ell+U_r/r)(H+dot H)+(U_theta/r)Htheta-H
                                         +a(V_r sin theta+V_theta cos theta). (9)

This uses the actual canonical c. The center defect is reported separately;
subtracting it does not turn a nonprofile into a profile.
For core length l0=L 2^(-kappa), z=log(r/l0), and any2<m<4, the squared
weighted norms of h and F share the common positive factor l0^(4-2m).
After canceling it, their integrands are respectively

    exp((4-2m)z) H^2,
    exp((4-2m)z) (F/r)^2.                              (10)

Thus the ratio can be evaluated without forming r^(-2m), even when the
core is extremely small. Symmetry permits four times a quadrant angular
integral. Finite angular support makes an adequately resolved trapezoid
exact in angle in real arithmetic, but finite log-radius cutoffs remain.

On a finite annulus z0<z<z1, let I=integral weight H^2 and J=integral
weight H(F/r). The exact integration-by-parts check is

    J=[(m-1)ell-1]I + m integral weight(U_r/r)H^2
         +a integral weight H(V_r sin theta+V_theta cos theta)
         +[one-half exp((4-2m)z) integral (ell+U_r/r)H^2 dtheta]_(z0)^(z1). (11)

The lower boundary enters with a minus sign. For the whole plane these
fluxes tend to zero by the same hypotheses as result62. An observed
finite-window ratio remains a quadrature observation unless the tails
are bounded. Several cutoffs and orders quantify sensitivity, not a
uniform global certificate.

## Manufactured test and dependencies

Take independent parameters q,e and

    psi=-q xy exp(-r^2)+e xy(x^2-y^2)exp(-r^2),
    rho=y exp(-r^2)[q(4-2r^2)+e(2x^4-2y^4-6x^2+10y^2-6)].

Direct Cartesian differentiation verifies -Delta psi=rho_x. Its density
modes are

    b_1=exp(-r^2)[q(4-2r^2)+e(-r^4+6r^2-6)],
    b_3=e exp(-r^2)(r^4-4r^2).

Here a=4q-6e and c=-q. The e term has zero center strain despite a
nonzero contribution to a; its local term and entire third moment cancel.
The exact stream has n=2 and n=4, so it tests both the logarithmic
interior/exterior integrals and their cancellation. It is a manufactured
canonical field, not an exact transport profile.

Dependencies: elementary radial Green integration and the canonical
uniqueness argument above; result62 supplies the comparison weighted
identity. No numerics-lane implementation is used. The proposed code is
an additional independent evaluator alongside the existing Cartesian FD8
and full-plane cancellation quadrature. Its validation status is recorded
in verification/, and no numerical claim follows from formulas alone.

## Cartesian strain and gradient checks from the same inverse

For even n, let hminus=h_(n-1), hplus=h_(n+1), with dots denoting
logarithmic derivatives. The angular coefficient of rho_x is

    Q_n=[dot hminus-(n-2)hminus+dot hplus+(n+2)hplus]/2.

The affine term contributes zero, including n=2. Poisson supplies
phi_rr=-phi_r/r-phi_thetatheta/r^2-rho_x. In the orthonormal polar frame,

    Srr=-c cos(2theta)+sum n(P_n-D_n)cos(n theta),
    Srtheta=c sin(2theta)+sum[n^2 P_n-D_n-Q_n/2]sin(n theta),
    Sthetatheta=-Srr.

These formulas follow by differentiating U_r=-psi_theta/r and
U_theta=psi_r, including the polar-frame connection term -U_theta/r
in twice Srtheta. Hence the operator norm of strain is
sqrt(Srr^2+Srtheta^2). The density gradient has polar components

    rho_r=a sin(theta)+H+dot H,
    rho_theta/r=a cos(theta)+Htheta.

An independent Cartesian differentiation of the manufactured polynomial
Gaussian stream and density checks these formulas. Their sampled maxima
remain lower estimates of global maxima, not a strain cap.
