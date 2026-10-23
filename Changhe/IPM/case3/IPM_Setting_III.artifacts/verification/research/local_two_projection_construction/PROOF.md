# Smooth canonical fields with two transport projections imposed locally

Verifier result109. Independent reconstruction of proj2. The argument is written before supporting code. The algebraic identities below are also to be checked by a separate exact implementation.

## 1. Exact statement and scope

Let ell be2 or3, D=ell-1, and choose H>0. For ell=2 take a=128+m+sqrt(2), and for ell=3 take a=16+m+sqrt(2), with any integer m>=0. For every E>0 there is a smooth compactly supported density rho on R^2, even in x and odd in y, satisfying all of the following:

* rho_y(0)=a, and q=rho/(a y) has a smooth extension with q(0)=1 and q(X)<1 for X!=0.
* The canonical stream solves -Delta psi=rho_x, U=(-psi_y,psi_x)=o(r), and psi_xy(0)=-D. No harmonic strain is added to this inverse.
* If R=(ell X+U).grad rho-rho and R_j(r)=integral_0^(2pi) R(r,theta)sin(j theta)dtheta, then R_1=R_3=0 for all sufficiently small r>0.
* R_5(r)=pi C_5 r^5+O(r^7) with C_5<0, so these fields are not transport profiles.
* sup_X ||sym DU(X)||_op-D>=E.

Only density frequencies1,3,5 are used globally. The fifth frequency vanishes near zero, but its exterior moment supplies a fourth-frequency harmonic stream there. The support, the disc of exact projected equations, and growth constants can depend on a,H,E. Compact support gives the prompt's density/gradient growth condition for every gamma in(0,1). The theorem gives unbounded slopes for two equations imposed locally. It makes no claim that R_1 or R_3 vanish on the entire plane and does not meet the principal NO or YES endpoint.

## 2. A separately derived full-plane inverse and projections

For r>0 write

    rho=r[f(r)sin theta+g(r)sin3theta+k(r)sin5theta],
    dot F=r F'(r),
    T=int_r^infinity g(s)/s ds,
    S=r^2 int_r^infinity k(s)/s^3 ds,
    J=r^-4 int_0^r s^3 f(s)ds,
    K=r^-6 int_0^r s^5 g(s)ds,
    L=r^-8 int_0^r s^7 k(s)ds.

The integral equations are dot T=-g, dot S=2S-k, dot J=f-4J, dot K=g-6K, dot L=k-8L. Define

    u=(T-J)/2, v=(S-K)/2, w=-L/2,
    psi=r^2[u sin2theta+v sin4theta+w sin6theta].          (1)

To check Poisson without adopting a numerical inverse, one density term r F_j sin(j theta) contributes

    [(2-m)F_(m-1)+dot F_(m-1)
       +(m+2)F_(m+1)+dot F_(m+1)]/2

to the sin(m theta) source coefficient rho_x. Meanwhile -Delta[r^2 h_m sin(m theta)] has coefficient -ddot h_m-4 dot h_m+(m^2-4)h_m. Substitution of the five integral equations makes these coefficients equal for m=2,4,6. At zero, smooth densities have f=a+O(r^2),g=O(r^2),k=O(r^4), which make (1) smooth, including the regular upper-integral harmonics. For compactly supported density, only decaying harmonic terms remain at infinity. Thus (1) is the canonical inverse. The difference from another inverse with sublinear velocity is harmonic; harmonic sublinear gradient is constant, and the stream parities exclude this constant gradient. An arbitrary constant in psi is excluded by its odd parities.

The independent angular calculation uses

    U_r=-psi_theta/r, U_theta=psi_r,
    (U.grad rho)/r
     =sum_(m,j)[-m h_m(F_j+dot F_j)cos(m theta)sin(j theta)
                 +j(2h_m+dot h_m)F_j sin(m theta)cos(j theta)].    (2)

Both products split into two signed sine frequencies. Put B=-u-K+S and C=K-3L/2-S. The coefficients E_j=R_j/(pi r) are

    E1=(ell+u)dot f+B dot g+C dot k+F1,
    E3=B dot f+(ell-3L/2)dot g-u dot k+F3,
    E5=ell dot k+D k+C dot f-u dot g
           +(2J+T)g+2Kf-fg-fk/2-3g^2/4,                 (3)

where

    F1=(D+T)f-f^2/4+fg/2+(-J+2K+4S-2T)g
                         +(-4K+6L-6S)k+gk/2,
    F3=(J+2S)f-f^2/4-fg/2+(D+3L)g
                         +(-2J-3T+f+g/2)k.

These formulas follow by assigning every signed frequency in (2), rather than differentiating a fitted residual. They also specify the normalization of each projection.

## 3. The regular singular local problem

Set z=r^2. Prescribe k=0 near zero, S=Hz, L=0, and seek analytic f,g,T,J,K with

    f(0)=a, g(0)=0, T(0)=a/4-D, J(0)=a/4, K(0)=0.

Then u(0)=-D/2 and psi_xy(0)=2u(0)=-D. Require E1=E3=0 and the three remaining integral differential equations. The derivative matrix of f,g has entries ell+u,B;B,ell. At zero its determinant is

    ell(ell+1)/2-D^2/4=(ell^2+4ell-1)/4>0.

It is therefore invertible in a neighborhood of the initial data. With Y=(f,g,T,J,K), the system becomes zY'=F(z,Y), with F analytic and F(0,Y0)=0.

For a z^n coefficient, n>=1, set lambda=2n. The scalar equations give T_n=-g_n/lambda, J_n=f_n/(lambda+4), K_n=g_n/(lambda+6). Eliminating these variables leaves

    M(lambda) [f_n,g_n]^T=known lower-order forcing,

with

    M11=(ell+1)lambda/2-a/4,
    M12=D lambda/2+2D-a/4-a/lambda,
    M21=D lambda/2-a/4+a/(lambda+4),
    M22=ell lambda+D-a/2.

The off-diagonal product simplifies because

    M12=(lambda+4)(D/2-a/(4lambda)),
    M21=lambda(D/2-a/(4(lambda+4))).

Subtracting this product from M11 M22 gives

    16 det M(lambda)=I_ell(a,lambda)
      =a^2-4[(ell+2)lambda-D]a
           +4(ell^2+4ell-1)lambda^2-8D(ell-3)lambda.     (4)

For integer ell and lambda, this is a^2-4Ba+4C with integers B,C. At a=j+sqrt(2), its irrational part vanishes only when j=2B. The remaining rational part is then2 modulo4 and cannot vanish. Our slopes therefore avoid every positive integer recurrence resonance. All formal coefficients are uniquely determined.

This formal series actually converges. Here are the required details. Let A=D_YF(0,Y0). The previous elimination is equivalent to invertibility of nI-A for every positive integer n, since n,n+2,n+3 from the scalar equations are nonzero. Choose N>||A||+1, construct Y_<=N by recurrence, and set Y=Y_<=N+z^(N+1)V. The equation is

    zV'=(A-(N+1)I)V+G(z,V),

where G is analytic for z small and V bounded. Its V derivative is O(z), since D_YF(z,Y_<=N)-A=O(z) and nonlinear terms carry z^(N+1). Its value at z=0 is independent of V. Put V0=((N+1)I-A)^-1 G(0). On bounded holomorphic functions in a sufficiently small complex disc, with values in a ball about V0, use

    V(z)=int_0^1 t^(N I-A) G(tz,V(tz))dt.               (5)

The operator norm of the power is at most t^(N-||A||), which is integrable. At z=0 (5) equals V0. Uniform continuity makes the map preserve the ball on a small disc, and the O(z) derivative makes it a contraction. Its fixed point is holomorphic, satisfies the differential equation by differentiating the integral, and is real on the real axis by conjugation and uniqueness. The recurrence determines every coefficient, giving uniqueness of the analytic local branch. No appeal to mere formal solvability replaces this convergence argument.

## 4. Strict local one-sidedness and an explicit omitted mode

Write f=a+f2 z+f4 z^2+O(z^3),g=g2 z+g4 z^2+O(z^3), and b=f2+3g2,e=f2-g2. The first-order equations give

    6e=(a-4ell+2)b,
    H=e/a-(5b+3e)/96.

With F_ell=a^2-(4ell+20)a+128ell-64, solve them to obtain

    f2=-24Ha(a-4ell+4)/F_ell,
    g2=8Ha(a-4ell-4)/F_ell,
    b=-192Ha/F_ell,
    e=-32Ha(a-4ell+2)/F_ell.                             (6)

For ell=2, F_2=(a-12)(a-16); for ell=3, F_3=(a-16)^2+64. The chosen slopes make b,e strictly negative. Since g(z)/z is analytic,

    q-1=(b/a)x^2+(e/a)y^2+O(r^4)<0

on a small punctured disc, uniformly in angle. Analyticity bounds the remainder uniformly and the negative definite quadratic controls it.

For k=0, the E5 formula in (3) reduces to

    E5=(K-S)dot f-u dot g+(2J+T)g+2Kf-fg-3g^2/4.

Its z coefficient vanishes, as also required because a homogeneous cubic polynomial cannot have sine frequency5. Its z^2 coefficient is

    C5=-2Hf2+(D-a/20)g4-3g2^2/4.                        (7)

For completeness the second-order recurrence is

    M(4)[f4,g4]^T + [Q1,Q3]^T=0,
    Q1=6Hg2-5f2^2/12-f2g2/2+3g2^2/2,
    Q3=4Hf2+f2^2/12-f2g2/4.                            (8)

The plus sign in (8) is essential and is missing typographically in the external proof. Eliminating f4,g4 from (8), and inserting (6) into (7), gives

    C5=-384H^2 a(15a^4-920a^3+19360a^2-165312a+491520)
              /[5(a-16)^2(a-12)^2(a^2-60a+736)]          (ell=2),
    C5=-384H^2 a(a-16)(3a-32)/(a^2-32a+320)^2           (ell=3).

The second expression is negative for a>16. For the first, a>=128 makes every denominator factor positive, and its numerator polynomial is positive: a^3(15a-920)-165312a>0 there, while the remaining 19360a^2+491520 is positive. Thus R5=pi C5 r^5+O(r^7) is nonzero. The analytic construction already fails the full PDE locally.

## 5. Compact extension with the exact canonical moments

Take a smooth radial cutoff chi, 0<=chi<=1, identically1 near zero and supported inside the disc where q<1. Extend f0=chi f and g0=chi g by zero and set k0=0. Their density is smooth, and chi q<1 off zero: for q>=0 multiplication decreases it, and for q<0 the product is nonpositive.

Choose nonnegative smooth bumps phi3,phi5 supported in an annulus disjoint from that cutoff. Choose their coefficients A3,A5 to enforce

    int_0^infinity [g0+A3 phi3]/r dr=a/4-D,
    int_0^infinity A5 phi5/r^3 dr=H.                     (9)

The two positive finite bump integrals make these coefficients unique. Let g1=g0+A3phi3, k1=A5phi5. Choose a nonnegative radial cutoff zeta, supported away from the local disc and equal to1 on the supports of both bumps. Set f1=f0-B zeta. For B sufficiently large,

    f1+3|g1|+5|k1|<=0

on those supports. The inequalities |sin(jtheta)|<=j|sin theta| for j=3,5 then give q<=0 on this annulus. Where only zeta contributes, q<=0 as well. In the original cutoff region q<1, and in the remaining zero region q=0. Hence the global quotient is strictly below1 off zero. Smoothness across y=0 follows from the polynomial identities for sin3theta/sin theta and sin5theta/sin theta, and from g=O(r^2), k=O(r^4) near zero.

Apply the exact canonical inverse (1) to f1,g1,k1. On a smaller disc the lower integrals J,K,L are unchanged, while (9) makes T=T(0)-int_0^r g/s and S=H r^2. Thus the canonical stream agrees exactly with the local stream. In particular both local projected equations, the center data, and C5 are preserved. Exterior moments have supplied the local harmonic datum H; it was not added as an unauthorized full-plane harmonic strain.

## 6. Strain can be made arbitrarily large

Keep all supports and the observation radius R outside them fixed while increasing B. Set I1=int s^3 f1(s)ds,I3=int s^5g1(s)ds,I5=int s^7k1(s)ds. Outside support,

    psi=-[I1 r^-2 sin2theta+I3 r^-4 sin4theta+I5 r^-6 sin6theta]/2.

For a harmonic stream -I r^-m sin(mtheta)/2, its velocity derivative is symmetric with zero trace. Its operator norm is m(m+1)|I|/(2r^(m+2)), by two derivatives of the holomorphic monomial z^-m, or by the polar Hessian. Consequently at every point of the circle r=R the reverse triangle inequality gives

    ||sym DU||_op>=3|I1|R^-4-10|I3|R^-6-21|I5|R^-8.

The upper moments in (9), I3,I5 and the local branch do not change with B. Since int s^3 zeta(s)ds>0, I1 tends to minus infinity. Choose B to make the lower bound at least D+E. Increasing B preserves the one-sided quotient estimate. This proves the statement.

## Dependencies and verification status

The proof supplies its own modal canonical inverse, regular-singular convergence, moment extension, and omitted-projection calculation. It uses elementary harmonic uniqueness for the canonical gauge, standard contraction on holomorphic functions with the complete integral estimate shown, and compact smooth radial cutoffs. The external proj2 files are frozen in verification/source_manifest.json. Their separate numerical boundary-value experiments are not used or certified. Exact coefficient checks and an actual Opus5.5 lead exchange are to be recorded in verification/ and the report. This is a restricted nonprofile construction, not a solution of either global projected or full transport problem.
