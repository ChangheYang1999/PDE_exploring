# A Hilbert-Schmidt bound for the symmetric weighted coupling error

Status: new T4 alternative, OPEN pending independent Opus review. The full first velocity commutator is not Hilbert-Schmidt in two dimensions. This result uses the additional cancellation in the symmetric part that actually enters the energy estimate.

## 1. Exact statement and hypotheses

Work on real or complex L2(R2), with the usual Lebesgue measure. Let

    U[h]=(-R1 R2 h, R1^2 h), Rj=partial_j(-Delta)^(-1/2),
    v=grad rho, Qh=v.U[h].

Assume v is bounded and globally Lipschitz. Put

    G=||v||_infinity, H=Lip(v).

The vector norm is Euclidean and H can be bounded by the essential supremum of the operator norm of Dv. Let psi be a real bounded globally Lipschitz function such that, for some real constant psi_infinity,

    A=||grad psi||_2<infinity, B=||psi-psi_infinity||_2<infinity,
    L=Lip(psi), Psi=ess sup psi-ess inf psi.

For positive A,B,H0,D define

    R=2B/A, S=D/H0,
    J(A,B;H0,D)=sqrt(2pi) A H0 min(R,S)
                  sqrt(1+log(max(R,S)/min(R,S))).          (1)

If one of these parameters is zero, set J=0 in the cases where the increment appearing below vanishes. Nonzero functions in the stated class have A,B>0, so no other zero case is needed.

Set Sym T=(T+T*)/2 and

    E_psi=Sym(e^psi Q e^(-psi))-Sym Q.

Then E_psi is self-adjoint and Hilbert-Schmidt, with

    ||E_psi||_op <= ||E_psi||_HS
       <= cosh(Psi)/(4pi)
            [G J(A,B;L,Psi)+J(A,B;H,2G)].               (2)

The coarser bound ||E_psi||_op<=G(exp(Psi)-1) is also valid. Either bound, or their minimum, may be used. If rho is S1 and psi is even in both variables, restriction to S1 preserves all conclusions. No high inverse or nonlinear existence claim is made.

## 2. Increment integral lemma

Let f-f_infinity belong to H1(R2), with ||grad f||_2=A and ||f-f_infinity||_2=B. Let g be a scalar or vector function with Lipschitz constant H0 and global increment bound |g(x)-g(y)|<=D. Define

    I(f,g)^2=integral_R2 integral_R2
               |f(x+z)-f(x)|^2 |g(x+z)-g(x)|^2 / |z|^4 dx dz.

The fundamental theorem of calculus and the triangle inequality give

    ||f(.+z)-f||_2 <= min(A|z|,2B),
    ||g(.+z)-g||_infinity <= min(H0|z|,D).

Consequently

    I(f,g)^2 <= 2pi A^2 H0^2
       integral_0^infinity min(r,R)^2 min(r,S)^2 r^(-3) dr.

Writing m=min(R,S) and M=max(R,S), the three intervals (0,m), (m,M), (M,infinity) contribute respectively

    m^2/2, m^2 log(M/m), m^2/2.

Their sum proves I(f,g)<=J(A,B;H0,D). This is a whole-plane estimate. Neither an omitted diagonal singularity nor a finite exterior truncation is present.

Apply it first with f=g=psi, where H0=L and D=Psi. Apply it again with f=psi and g=v, where H0=H and D=2G. These are precisely the two quantities on the right of (2).

## 3. Exact symmetric kernel and its cancellation

With the stated Riesz convention, the off-diagonal vector kernel of U is

    K(z)=(-2 z1 z2, z1^2-z2^2)/(2pi |z|^4),
    |K(z)|=1/(2pi |z|^2).                                (3)

There is also the local term (0,-h/2). Formula (3) follows by differentiating the fundamental solution -(log|z|)/(2pi) of -Delta. The local term contributes multiplication by -v2/2 to Q. It is unchanged under conjugation and cancels exactly in E_psi.

The kernel K is real and even. For x!=y put d=psi(x)-psi(y). The off-diagonal kernel of E_psi is therefore

    e(x,y)=1/2 K(x-y).
       [(cosh d-1)(v(x)+v(y))+sinh d(v(x)-v(y))].         (4)

This follows by adding the kernel e^d v(x).K(x-y) to its transposed kernel e^(-d) v(y).K(x-y), then subtracting v(x).K and v(y).K. In particular e(y,x)=e(x,y).

For |d|<=Psi, Taylor's theorem gives

    |cosh d-1| <= cosh(Psi) d^2/2,
    |sinh d| <= cosh(Psi)|d|.

Since |v(x)+v(y)|<=2G, (3)-(4) imply

    |e(x,y)| <= cosh(Psi)/(4pi |x-y|^2)
        [G |psi(x)-psi(y)|^2
           +|psi(x)-psi(y)| |v(x)-v(y)|].                (5)

The right side has finite L2 norm on R2 times R2 by Section2. The triangle inequality in that product L2 space proves (2).

There is no residual principal-value singularity in (4): both bracketed terms vanish quadratically as y tends to x, so (4) is locally bounded. The kernel identity first holds on compact smooth tests by cancellation of the truncated integrals and of the local term. The finite L2 kernel norm then identifies its bounded Hilbert-Schmidt extension with E_psi on all L2. Thus this argument does not assert a false Hilbert-Schmidt estimate for the individual first commutator [U,e^(-psi)].

For the coarser bound, ||U||_(L2 to vector L2)<=1. Subtracting the midpoint of the range of e^(-psi) gives

    ||[U,e^(-psi)]|| <= sup e^(-psi)-inf e^(-psi).

Multiply by e^psi v and take the symmetric part to obtain G(exp(Psi)-1). This also confirms that the new estimate may safely be intersected with the earlier one.

## 4. Consequence for the localized energy proposal

Assume additionally V=cX+U[rho] is globally Lipschitz, div V=2c, and the chosen realization has the compact smooth core needed for its transport energy identity. Suppose

    g=V.grad psi is bounded,
    theta=(|grad rho|-rho_y)/2 <= theta_c+theta_1,
    theta_c>=0, theta_1>=0 bounded, grad theta_1 in L2,
    Sym Q=P0+K0, ||K0||_op<=kappa.

The independently audited double-commutator identity gives C_T=sqrt((4log2-1)/(8pi)). Combining that identity with (2) yields the weighted energy rate

    beta >= ess inf(1+c+g-theta_1)-theta_c-kappa
               -C_T||grad theta_1||_2-omega_sym,          (6)

where omega_sym is the minimum of the two upper bounds in Section1. This is the same localized rate with a potentially smaller conjugation cost. Its generator and domain assumptions are unchanged. The new additional numerical inputs are G,H,A,B,L,Psi; they are finite for a compactly supported Lipschitz orbit weight and a bounded Lipschitz background gradient.

For psi=epsilon phi, the first term in (2) is quadratic in epsilon and the second is linear. The linear term involves spatial variation of v. This cancellation is the reason the estimate can improve on using the norm of the full first commutator. No claim that it improves a particular current candidate is made until all six inputs have been bounded.

## Dependencies and verification scope

The proof uses the exact canonical velocity kernel, elementary increment estimates, explicit one-dimensional integration, and Hilbert-Schmidt kernel theory. It is independent of the invalid first-commutator proposal. Formula (6) also depends on the already audited localized double-commutator estimate. All constants and hypotheses are displayed; a separate Opus review is required before using this new result as AUDITED.
