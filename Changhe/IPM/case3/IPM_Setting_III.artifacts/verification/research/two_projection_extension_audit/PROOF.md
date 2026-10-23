# Prescribed-mode obstructions, arbitrary-disc constructions, and a small exterior branch

Independent verifier reconstruction, 2026-10-21 UTC. Written before the associated exact checker. The source under audit is frozen in verification/external_PROOF.frozen.md. The symbol ell below is the source's c; D=ell-1. The construction satisfies two angular projections, not the full IPM transport equation.

## Statements and dependencies

For ell>1, write a smooth three-mode density as

    rho=r[f(r) sin(theta)+g(r) sin(3theta)+k(r) sin(5theta)],
    R=(ell X+U).grad(rho)-rho,
    R_j(r)=integral_0^(2pi) R(r,theta) sin(jtheta) dtheta.

The following are separate assertions.

1. When g is prescribed, its first Taylor coefficient fixes the fourth stream harmonic through a necessary center relation. At certain slopes, additional finite Taylor equations obstruct the specific g used in the one-projection construction. In particular ell=3, a=32N+24, N>=0, and sufficiently small positive epsilon are obstructed. For N=0 the entire interval 0<epsilon<=1/10 is obstructed.
2. For every ell>1, every a>=100(ell+1) outside an explicitly locally finite exceptional set, and every finite R0>0, a smooth compactly supported canonical density exists with slope a, strain -D, q=rho/(ay)<1 off the origin, and R_1=R_3=0 for 0<r<=R0. Its R_5 is nonzero near zero. Neither projected equation is asserted in the extension annulus.
3. A small exterior branch with prescribed fifth density mode and five small initial values exists and has the exact upper Green moments. Its lower moments encode unspecified interior data. No large-center-to-small-exterior connection is proved.

The global question R_1=R_3=0 with unbounded normalized slopes remains OPEN. These statements do not prove a primary YES or NO. Dependencies are elementary finite Fourier calculus, convergent radial Green moments, analytic contraction on a disc, and a weighted contraction on a half-line. The center construction is also independently reconstructed in result109; all formulas needed for its extension are included here.

## Exact modal equations and the inverse

A dot denotes r d/dr and z=r^2. Define

    T=int_r^infinity g(s)/s ds,       S=r^2 int_r^infinity k(s)/s^3 ds,
    J=r^-4 int_0^r s^3 f(s) ds,      K=r^-6 int_0^r s^5 g(s) ds,
    L=r^-8 int_0^r s^7 k(s) ds,
    u=(T-J)/2, v=(S-K)/2, w=-L/2,
    psi=r^2[u sin(2theta)+v sin(4theta)+w sin(6theta)].

Then

    dot T=-g, dot S=2S-k, dot J=f-4J, dot K=g-6K, dot L=k-8L.   (1)

The sin(m theta) coefficient of rho_x is

    [dot F_(m-1)+(2-m)F_(m-1)+dot F_(m+1)+(m+2)F_(m+1)]/2,

where F_1=f,F_3=g,F_5=k and other F vanish. The minus Laplacian of r^2 h sin(m theta) is [-ddot h-4dot h+(m^2-4)h]sin(m theta). Substitution of (1) proves -Delta psi=rho_x directly. Smoothness and sublinear symbol bounds make the moments convergent, the origin regular, and U=o(r). Two such parity-preserving inverses differ by a componentwise harmonic sublinear velocity, which is constant by the disc interior gradient estimate as its radius tends to infinity. The velocity parities remove that constant and the odd-odd stream parity removes its remaining additive constant. Thus the inverse is canonical, without a free global harmonic strain.

To obtain R_j, a pair of modes j,m contributes

    -m h_m(F_j+dot F_j) cos(mtheta)sin(jtheta)
       +j(2h_m+dot h_m)F_j sin(mtheta)cos(jtheta)

to U.grad(rho)/r. Apply the signed sine sum identities. Put B=-u-K+S and C=K-3L/2-S. The exact result is

    E1=R_1/(pi r)=(ell+u)dot f+B dot g+C dot k+F1,
    E3=R_3/(pi r)=B dot f+(ell-3L/2)dot g-u dot k+F3,
    F1=(D+T)f-f^2/4+fg/2+(-J+2K+4S-2T)g
                         +(-4K+6L-6S)k+gk/2,
    F3=(J+2S)f-f^2/4-fg/2+(D+3L)g+(-2J-3T+f+g/2)k,
    E5=R_5/(pi r)=ell dot k+Dk+C dot f-u dot g+(2J+T)g
                          +2Kf-fg-fk/2-3g^2/4.            (2)

These are identities for arbitrary three-mode densities. They assume no transport equation.

Smooth origin data have f(0)=a, g=O(z), k=O(z^2). The strain condition is

    T(0)=M=a/4-D, J(0)=a/4, K(0)=L(0)=S(0)=0, u(0)=-D/2.

The coefficient H=lim S/z is the global moment int_0^infinity k(s)/s^3 ds. It can be specified while constructing the density, but cannot be changed for an already fixed global density.

## Prescribed third mode and finite-jet incompatibility

Expand f=a+sum f_j z^j, g=sum g_j z^j, k=sum_(j>=2) k_j z^j, S=Hz+O(z^2). The coefficients of z in E1=E3=0 are

    (ell+1-a/4) f_1+(3D-3a/4) g_1=0,
    (D-a/12) f_1+(3ell-1-a/2) g_1+2aH=0.                 (3)

For a!=4(ell+1), these give

    f_1=-3(a-4ell+4)g_1/(a-4ell-4),
    H=F_ell(a)g_1/[8a(a-4ell-4)],
    F_ell(a)=a^2-(4ell+20)a+128ell-64.                     (4)

At a=4(ell+1), the first equation forces g_1=0 because 3D-3a/4=-6. Therefore that exceptional case does not supply an unrestricted H parameter for a prescribed nonzero g_1.

For j>=2, (1) yields

    T_j=-g_j/(2j), J_j=f_j/(2j+4), K_j=g_j/(2j+6),
    S_j=-k_j/(2j-2), L_j=k_j/(2j+8).

The new coefficients in (2) have equations

    A_j f_j+B_j g_j=known lower terms,
    C_j f_j+E_j g_j+V_j k_j=known lower terms,
    A_j=(ell+1)j-a/4,
    B_j=Dj+2D-a/4-a/(2j),
    C_j=Dj-a/4+a/(2j+4), E_j=2ell j+D-a/2,
    V_j=(j+3)[D-a/(4(j-1))].                             (5)

To see the last coefficient explicitly, the linear new-k terms are Dj k_j+(3D-a/4)k_j+2aS_j. Their sum is V_j k_j. No new k_j occurs in E1 since C(0)=0 and the undifferentiated coefficients multiplying k also vanish at zero. Thus (5) is triangular for unknown f_j,k_j when g is prescribed. Its two exceptional slope sets are a=4(ell+1)j and a=4D(j-1).

Now prescribe

    T=M(1+z)^(-epsilon),
    g=2epsilon M z(1+z)^(-1-epsilon), M=a/4-D!=0.          (6)

Let a=4D(m-1), m>=2, and suppose a!=4(ell+1)j for 1<=j<=m. Equations (3)-(5) force every coefficient below order m, and f_m, to be analytic in epsilon. At epsilon=0 all these perturbation coefficients are zero, so all nonlinear products contribute zero to the first epsilon derivative. Let G_j=partial_epsilon g_j at zero=2M(-1)^(j-1). Then partial_epsilon f_j=-B_j G_j/A_j. Because V_m=0, the order-m E3 compatibility has derivative

    Ccompat'(0)=(E_m-C_m B_m/A_m)G_m,
    E_m-C_m B_m/A_m=4m(2ell+m-2)/(ell+2m-1)>0.            (7)

The derivative is nonzero. Analyticity implies Ccompat(epsilon) is nonzero for every sufficiently small positive epsilon, contradicting a necessary finite jet equation. No analyticity of an unknown solution is assumed: every smooth solution has these forced finite Taylor coefficients.

For ell=3 and a=32N+24, take m=4N+4 and M=8N+4. The excluded A_j resonance would require j=2N+3/2, impossible. Equation (7) becomes -4M m(m+4)/(m+1)<0. For N=0, direct polynomial multiplication through z^4 gives

    H=2epsilon/3,
    k_2=8epsilon(14epsilon-1)/5,
    k_3=-32epsilon(413epsilon^2-17epsilon-5)/15,
    Ccompat=32epsilon[289475epsilon^3-21544epsilon^2
                                      +1881epsilon-720]/225.  (8)

On 0<epsilon<=1/10 the positive terms in the bracket are at most 477575/1000<720. Hence (8) is strictly negative throughout this interval. This excludes only the prescription (6) with three density modes. At ell=2, the earlier slopes 24N+18 avoid both sets in (5), so this particular obstruction says nothing about them.

## Derivative matrix barriers

For prescribed g, the f,k derivative determinant in (2) is

    Delta_fk=-(ell+u)u-BC, Delta_fk(0)=D(ell+1)/4>0.

For a globally admissible canonical three-mode density the coefficients and moments tend to zero at infinity, hence Delta_fk tends to zero. A positive unweighted lower bound on the entire half-line is impossible; pointwise nonvanishing is not excluded.

If a continuous radial path reaches u>0 and eta=|K|+|S|+|L|<=u/4, then |B|<=u+eta, |C|<=3eta/2. Therefore

    Delta_fk<=-ell u-u^2+3(u+eta)eta/2
              <=-ell u-17u^2/32<0.

It must pass a zero determinant between the origin and that point. A compatible solution might cross this zero. The conclusion concerns nonsingular inversion of this matrix, not nonexistence.

For prescribed k, the f,g matrix is symmetric:

    Mfg=[[ell+u,B],[B,ell-3L/2]].                         (9)

It tends to ell times the identity at infinity. Its determinant need not stay positive on a large-data connection; for K=S=L=0 and u>ell(1+sqrt(5))/2 it is negative.

## Arbitrary finite discs, all ell>1

Set k=0 near zero, L=0, S=Hz with H>0. At the initial point the determinant of (9) is (ell^2+4ell-1)/4>0, so (1)-(2) reduce to an analytic regular-singular system zY'=F(z,Y) for Y=(f,g,T,J,K), based at Y0=(a,0,M,a/4,0), F(0,Y0)=0. Eliminating the scalar moment equations at order lambda=2j leaves

    A(lambda)=[[ (ell+1)lambda/2-a/4,
                   Dlambda/2+2D-a/4-a/lambda ],
                [ Dlambda/2-a/4+a/(lambda+4),
                   ell lambda+D-a/2 ]].

An exact multiplication gives

    16 det A(lambda)=I_ell(a,lambda)
       =a^2-4[(ell+2)lambda-D]a
                +4(ell^2+4ell-1)lambda^2-8D(ell-3)lambda. (10)

Define E_ell={a:I_ell(a,2j)=0 for some integer j>=1}. On a bounded interval of a the positive lambda^2 term in (10) dominates uniformly at large j. Only finitely many polynomials, each with at most two roots, contribute there. Thus E_ell is locally finite and there are arbitrarily large admissible a outside it.

Here is convergence of the formal series, not just its recursive determination. Let Alin=D_Y F(0,Y0). The same scalar elimination implies jI-Alin is invertible for each integer j>=1. Choose N>||Alin||+1 and form the recursively determined polynomial Y_<=N. Substituting Y=Y_<=N+z^(N+1)V gives

    zV'=(Alin-(N+1)I)V+G(z,V),

where G is analytic, G(0,V) is independent of V and D_V G=O(z) uniformly on a bounded V-ball. The residual of the polynomial has order N+1, and every remaining nonlinear V term carries at least z^(N+1), proving these properties. On bounded holomorphic functions on a small disc the integral map

    TV(z)=int_0^1 t^(NI-Alin) G(tz,V(tz)) dt

is defined since ||t^(NI-Alin)||<=t^(N-||Alin||). At z=0 it equals V0=((N+1)I-Alin)^-1 G(0,V). On a ball around V0, shrinking the disc makes TV-V0=O(|z|) and the Lipschitz constant O(|z|) uniformly. The contraction theorem gives a holomorphic fixed point. Differentiating the integral yields the V equation. Uniqueness under complex conjugation gives a real analytic solution.

The first coefficients are

    f_1=-24Ha(a-4ell+4)/F_ell(a),
    g_1=8Ha(a-4ell-4)/F_ell(a),
    b=f_1+3g_1=-192Ha/F_ell(a),
    e=f_1-g_1=-32Ha(a-4ell+2)/F_ell(a).                    (11)

For a>=100(ell+1), F_ell(a)>0 and b,e<0. Because g(z)/z is analytic, rho=yf(z)+(g(z)/z)(3x^2y-y^3) is Cartesian analytic. Thus q-1=(b/a)x^2+(e/a)y^2+O(r^4)<0 uniformly on a sufficiently small punctured disc.

The next coefficients solve

    A(4)(f_2,g_2)^t+
      (6Hg_1-5f_1^2/12-f_1g_1/2+3g_1^2/2,
                         4Hf_1+f_1^2/12-f_1g_1/4)^t=0.

From (2), R_5=pi C5 r^5+O(r^7), where

    C5=-2Hf_1+(D-a/20)g_2-3g_1^2/4
       =-384H^2 a P_ell(a)/[5F_ell(a)^2 G_ell(a)],
    G_ell(a)=a^2-(12ell+36)a+32ell^2+384ell-160,
    P_ell(a)=15a^4+(200-560ell)a^3
       +(6704ell^2-2320ell-2816)a^2
       +(-29056ell^3-8512ell^2+63616ell-26048)a
       +40960ell^4+61440ell^3-245760ell^2+184320ell-40960. (12)

Equations (11), (10) and the displayed two-coefficient system give (12) by clearing denominators. For ell>1 its a^2 coefficient is at least 1568ell^2>0, its a coefficient is at least -63616ell^3, and its constant term is at least -286720ell^4. These follow by replacing negative lower powers of ell by ell^2, ell^3 or ell^4, and discarding positive terms. Consequently

    P_ell(a)>=15a^4-560ell a^3-63616ell^3 a-286720ell^4>7a^4

when a>=100(ell+1), since the three subtracted ratios to a^4 are respectively less than6,1,1. Also G_ell(a)>0: a>12ell+36 and its constant term is positive. Thus C5<0 and the full PDE fails on the local disc.

Extend f,g by a radial cutoff 0<=chi<=1 supported inside the local domain and equal to one on a smaller disc; initially set k=0 globally. This preserves q<1 off zero, even where q is negative. In a disjoint outer annulus choose nonnegative bumps phi3,phi5. Unique finite multiples A3,A5 can enforce

    int_0^infinity (chi g+A3 phi3)/s ds=M,
    int_0^infinity A5 phi5/s^3 ds=H.

Choose a nonnegative bump zeta supported off the original cutoff support and equal to one on the two outer bump supports. Add -B0 zeta to f, with B0>3|A3| ||phi3||_infinity+5|A5| ||phi5||_infinity. Since |sin3theta/sintheta|<=3 and |sin5theta/sintheta|<=5, the outer quotient is strictly below one; elsewhere the additional first mode is nonpositive. The new canonical T,S agree with the local ones on the smaller disc by their upper moments and (1). The lower moments are unchanged there. Thus E1=E3=0 and C5<0 persist on that disc. Outside the compact support, T=S=0 and J,K,L decay as r^-4,r^-6,r^-8, so the velocity is sublinear and canonical. The density satisfies every allowed positive sublinear growth exponent.

Finally the exact dilation rho_lambda(X)=lambda rho(X/lambda), psi_lambda=lambda^2 psi(X/lambda) preserves a,strain and q<1, and gives (R_lambda)_j(r)=lambda R_j(r/lambda). Dilate the disc to contain any prescribed finite R0. The coefficient C5 becomes lambda^-4 C5 and remains nonzero. There are no uniform bounds allowing R0 to tend to infinity with an admissible limit; locally the dilations can approach the inadmissible affine density ay.

## Small exterior branch with exact upper moments

Fix ell>1,R0>0,a>0, let t=log(r/R0), alpha=D/ell and 0<beta<alpha. The dot now means d/dt. Set b_beta=3+1/beta. Prescribe smooth k on t>=0 with |k|+|dot k|<=epsilon exp(-beta t), and initial values f0,g0,J0,K0,L0, each of absolute value at most epsilon. Assume

    epsilon<=min(ell/(30b_beta),
       ell(alpha-beta)/(1296b_beta^2), a/26).              (13)

In the Banach ball ||(f,g)||_beta<=2epsilon, where the norm is sup exp(beta t) max(|f|,|g|), define

    T=int_t^infinity g(s) ds,
    S=int_t^infinity exp[-2(s-t)]k(s) ds,
    J=exp(-4t)J0+int_0^t exp[-4(t-s)] f(s) ds,
    K=exp(-6t)K0+int_0^t exp[-6(t-s)] g(s) ds,
    L=exp(-8t)L0+int_0^t exp[-8(t-s)] k(s) ds.             (14)

The maximum w(t) of |f|,|g|,|T|,|S|,|J|,|K|,|L|,|k|,|dot k| is at most 3b_beta epsilon exp(-beta t). Differences of these nine-component vectors are bounded by b_beta exp(-beta t)||(f,g)-(ftilde,gtilde)||_beta. To check this, the upper convolutions have denominators beta and 2+beta; the lower convolutions have 4-beta,6-beta,8-beta and initial terms bounded by epsilon exp(-beta t). Here beta<1, so every denominator is positive.

Write Mfg=ell I+P as in (9) and

    Q=(F1-Df+C dot k, F3-Dg-u dot k)^t.

Its entries are quadratic in the nine variables; P is linear. The absolute coefficient sums in Q are 30.75 and14.25, so ||Q||_infinity<=31w^2. The row norm of P is at most5w. Equation (13) makes w<=ell/10, hence ||Mfg^-1||_infinity<=2/ell. Since P is symmetric its eigenvalues have modulus at most its row norm, and det Mfg>=ell^2/4.

The equations E1=E3=0 become

    dot x+alpha x=N(x), x=(f,g),
    N=Mfg^-1(alpha P x-Q).

The quadratic numerator has norm at most36w^2 and difference bound72w times the maximum difference in its nine variables. The inverse difference identity gives a bound20/ell^2 times that difference. Therefore

    |N|<=72w^2/ell,
    |N-Ntilde|<=216w/ell times |V-Vtilde|,                (15)

using w<=ell/10 for the latter estimate.

The map

    Tx(t)=exp(-alpha t)x0+int_0^t exp[-alpha(t-s)]N(x)(s)ds

has norm at most epsilon+648b_beta^2 epsilon^2/[ell(alpha-beta)]<=3epsilon/2. Its Lipschitz constant is at most648b_beta^2 epsilon/[ell(alpha-beta)]<=1/2. The estimate used here is sup_t exp(beta t) int_0^t exp[-alpha(t-s)]exp(-2beta s)ds<=1/(alpha-beta), obtained by replacing exp(-2beta s) with exp(-beta s). The contraction theorem supplies the unique fixed point in this ball. The equations first give differentiability, then smoothness follows from smooth k and repeated differentiation of (14) and (2).

Now f+3|g|+5|k|<=13epsilon exp(-beta t)<=a/2. The angular inequalities give q<1 throughout the exterior. The coefficients, first derivatives and moments are O(exp(-beta t)), hence rho,U=O(r^(1-beta)), grad rho=O(r^-beta). This is allowed sublinear growth. The exact upper Green conditions hold by (14). The lower moments are canonical only if an interior density supplies J0,K0,L0, and this theorem asserts no such matching.

Integrating dot g+alpha g=N_3 from t to infinity gives

    T=g/alpha+(1/alpha)int_t^infinity N_3(s)ds,
    |T-g/alpha|<=324b_beta^2 epsilon^2
                        exp(-2beta t)/(ell alpha beta). (16)

Thus T=(ell/D)g is only a linearized finite-radius boundary condition, even on the small exterior branch. The nonlinear correction cannot be discarded exactly.

## Audit verdict and literal repairs

The mathematical arguments above are valid within their stated scopes. The frozen external source omits three literal plus signs: one between the two adjacent density-mode contributions in the rho_x display of Step1, and one between f_1 and g_1 terms in each line of Step2 equation(8). Those displays must use the additions in this proof. Source Step7 has the necessary matrix-plus-forcing sign, unlike the earlier proj2 draft. Exact algebra checks are supporting verification, not a replacement for the convergence and scope arguments.

OPEN: a global normalized solution of both projected equations, the center-to-exterior connection, unrestricted angular upper bounds, and the primary full-plane existence question.
