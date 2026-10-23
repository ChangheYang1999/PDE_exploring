# A finite-regularity radial pair with zero first residual projection

Date: 2026-10-20. Status: independent construction and proof below; supporting exact arithmetic checks PASS on 2026-10-20; actual Claude Opus 5.5 independent review CONFIRMED on 2026-10-21 at00:17Z; the amendments below expand its moment-scope proof and clarify notation. Scope: canonical non-profiles with a specified finite regularity at the origin. No exact transport profile or smooth primary-class candidate is constructed.

## 1. Statement and notation

Fix ell>1, D=ell-1, a=4D, p=1/ell and lambda=2D/(ell+1), so 0<lambda<2. For each C>0 there is a radial function f on (0,infinity), smooth there, with

    f(r)=a-C r^lambda+O(r^(2lambda)) at zero,
    f(r)=K r^(p-1)(1+O(r^(p-1))) at infinity, K>0,
    0<f(r)<a, f'(r)<0.

Define rho=y f(r), J=r^(-4) int_0^r s^3 f(s)ds, and psi=-xy J. Then U=(-psi_y,psi_x) is the canonical full-plane velocity of rho, with psi_xy(0)=-D and U=O(r^p) at infinity. The pair satisfies the primary parities, nonzero center slope and sublinear first-derivative growth. It fails the smoothness condition in the primary class and does not satisfy transport. Specifically, for R=(ell X+U).grad rho-rho,

    int_0^(2pi) R(r,theta)sin(theta)dtheta=0 for every r>0,
    R(r,theta)=r C3(r)sin(3theta), C3(r)<0 for every r>0.    (1)

When 0<lambda<1, rho and U have class C^(1,lambda) at zero and are not C^2. When lambda=1, they have class C^(1,1) there and are not C^2. When 1<lambda<2, they have class C^(2,lambda-1) there and are not C^3. The cases lambda<1, lambda=1 and lambda>1 are respectively ell<3, ell=3 and ell>3. Here C^(k,alpha) denotes k continuous derivatives with locally alpha-Holder kth derivatives; alpha=1 means Lipschitz. They are smooth away from the origin. The stated nonregularity of U is verified below, rather than inferred just from rho.

The pair also satisfies |grad rho(X)|<a and ||sym DU(X)||_op<D at every X!=0, with equality in both bounds at zero. Moreover W=ell X+U is strongly monotone: (W(X)-W(Y)).(X-Y)>=|X-Y|^2. These additional bounds are proved in Section6.

All C>0 are related by the genuine spatial scaling. No existence, regularity or slope conclusion about nonradial exact profiles follows.

## 2. Local construction by a convergent integral equation

Put t=log r. The first residual projection and the canonical integral equation, derived independently in result88, are

    dot f=f(f-a)/(4ell-2J), dot J=f-4J.                    (2)

Seek the branch f=a-h, J=D-j, with h,j positive and small as t tends to minus infinity. Set d0=2ell+2, so lambda=a/d0. Equation(2) becomes

    dot h=lambda h+N(h,j), dot j=h-4j,
    N(h,j)=-h(h+2lambda j)/(d0+2j).                       (3)

These formulas hold where the denominator is nonzero. For t<=T_cut define

    (I_h)(t)=int_(-infinity)^t exp(-4(t-s))h(s)ds,
    (M h)(t)=C exp(lambda t)
             +int_(-infinity)^t exp(lambda(t-s))
                     N(h(s),I_h(s))ds.                 (4)

Use the Banach norm ||h||=sup_(t<=T_cut) exp(-lambda t)|h(t)| on continuous functions. Work on the closed ball ||h-C exp(lambda t)||<=C/2. On this ball h is positive and ||I_h||<=3C/[2(lambda+4)]. Since I_h is positive on the ball, d0+2I_h is at least d0. On that ball, directly from the rational expression in(3),

    |N(h(t),I_h(t))| <= K_ell C^2 exp(2lambda t),
    |N(h1,I_h1)-N(h2,I_h2)|(t)
       <= K_ell C exp(2lambda t)||h1-h2||.

Impose also C exp(lambda T_cut)<=1. Then h and I_h are uniformly bounded on the ball, and the constant K_ell is finite and independent of T_cut and C. This harmless additional restriction is compatible with choosing T_cut arbitrarily negative. Integrating these inequalities in(4) shows that M maps the ball to itself and has Lipschitz constant at most K_ell C exp(lambda T_cut)/lambda. Choose T_cut so this is smaller than 1/2. The contraction principle supplies a unique fixed point on this half-line. Differentiating(4) gives(3); the smooth right side bootstraps the fixed point to a smooth solution in t. Also

    h=C exp(lambda t)+O(exp(2lambda t)),
    j=C exp(lambda t)/(lambda+4)+O(exp(2lambda t)).         (5)

Constants in the O terms may depend on ell,C. Differentiating the smooth ODE repeatedly gives the same expansions after any fixed number of t derivatives, with lambda^k multiplying each leading term. This also follows by inserting(5) into(3), differentiating, and induction: every nonlinear remainder contains at least two factors of order exp(lambda t), and all their t derivatives have that order or smaller. Local uniqueness of (2) continues the branch while its denominator remains nonzero.

## 3. Global invariant region and decay

For sufficiently negative t, the expansion(5) puts the branch in the strict region

    0<f<a, f/4<J<f/3, J<D.                               (6)

Indeed J-f/4=h/4-j has positive leading coefficient, J-f/3 tends to -D/3, and j>0. On the boundary J=f/4, the derivative of J-f/4 is -dot f/4>0. On J=D, dot J=f-a<0. On J=f/3, write

    k=(a-f)/(4ell-2J).

There k<1, because a-f<4ell-2f/3 is equivalent to -4-f/3<0. The derivative of J-f/3 there is f(k-1)/3<0. These are inward-pointing inequalities. Region(6) is the open triangle with vertices (0,0), (a,D) and (3D,D); at its only non-equilibrium corner (3D,D), both active faces point inward. The positivity and upper bound on f also follow from f/4<J<f/3 and J<D. The scalar equation dot f=-k f prevents f from reaching zero in finite time and points downward for 0<f<a. Throughout the closure of this region,

    4ell-2J >= 4ell-2D=2ell+2>0.

Thus the solution continues to every finite future time and stays in(6). In particular f and J both strictly decrease. Their limits exist. If the limit of f were positive, its limiting derivative in(2) would be strictly negative since f<a, which is impossible for a function with a finite limit. Thus f tends to zero; the equation dot J=f-4J then forces J to tend to zero.

Put q=J/f. This q is used only in Sections3-4; it is not the density quotient rho/(a y). We have 1/4<q<1/3. Direct differentiation gives

    dot q=1-(4-k)q,
    dot k=k(3f-8J)/(4ell-2J)>0,
    lim_(t->infinity) k=D/ell=:k_inf=1-p<1.               (7)

The inequality for dot k uses q<1/3. Also

    k_inf-k=f(ell-2Dq)/[ell(4ell-2J)]>0.                 (8)

Since k is eventually bounded below by a positive constant, f decays exponentially in t. Hence k_inf-k=O(f) is integrable. Integrating dot f/f=-k proves

    f(t)exp(k_inf t) -> K in (0,infinity).

Equation(8) and the same integral show f=K exp(-k_inf t)(1+O(exp(-k_inf t))). Finally the bounded solution of dot J=f-4J is

    J(t)=int_(-infinity)^t exp(-4(t-s))f(s)ds.             (9)

There is no exp(-4t) homogeneous term because J stays bounded at minus infinity. Dividing(9) by f(t), use f(t-v)/f(t)<=exp(k_inf v), following from k<=k_inf. Dominated convergence yields

    q -> 1/(4-k_inf)=1/(3+p).

This proves the two asymptotic density statements. The ODE gives the corresponding first derivative bounds, in particular |rho|+(1+r)|grad rho|<=C_ell,C (1+r)^p. Equation(9), after r=exp t, is precisely the canonical integral defining J in the statement.

## 4. The third residual is strictly nonzero

For a radial quotient the only residual modes are sin(theta) and sin(3theta). Direct multiplication of the polar velocity

    U_r/r=J cos(2theta), U_theta/r=(J-f/2)sin(2theta)

and the density derivatives gives

    R/r=C1 sin(theta)+C3 sin(3theta),
    C1=(ell-J/2)dot f+D f-f^2/4,
    C3=J f+(J/2)dot f-f^2/4
       =f^2[q(1-k/2)-1/4].                              (10)

Equation(2) makes C1 exactly zero. To obtain a strict sign for C3, set E=1/(4-k)-q. Equations(7) give

    dot E+(4-k)E=dot k/(4-k)^2>0.

Both q and k have finite limits at minus infinity, namely 1/4 and 0, so E is bounded there. Since 4-k>3, variation of constants from minus infinity gives

    E(t)=int_(-infinity)^t exp(-int_s^t(4-k(u))du)
                               dot k(s)/(4-k(s))^2 ds>0.

The integral converges near minus infinity by(5). Consequently q<1/(4-k). Because 0<k<k_inf<1 by(8),

    C3/f^2 < (1-k/2)/(4-k)-1/4
            =-k/[4(4-k)]<0.                            (11)

This proves(1). It also gives the far coefficient

    C3/f^2 -> (p-1)/[4(p+3)]<0.

Near zero, direct substitution of(5) into(10) gives

    C3=-D lambda(1+lambda/2) C r^lambda/(4+lambda)
           +O(r^(2lambda)).                            (12)

Thus the failure of the full equation occurs at every positive radius. Angular cancellation of its first moment is exact, not a consequence of a tiny numerical residual.

## 5. Canonical inverse, regularity and moment scope

At zero, f=a+O(r^lambda), J=D-C r^lambda/(lambda+4)+O(r^(2lambda)). The stream psi=-xyJ is C^2, and its Laplacian equals -rho_x by differentiating r J'(r)=f-4J away from zero. The first derivatives of rho and second derivatives of psi are continuous at zero, so the Poisson identity extends there by continuity. No point-supported source arises. Parities are immediate, and the polar formulas above show U=O(r^p) at infinity. Any other canonical velocity has harmonic difference o(r); interior harmonic gradient estimates make the difference constant, and the parities force that constant to vanish. Hence this is the full-plane inverse with the required gauge. Its center strain is -J(0)=-D.

The t-derivative expansions in Section2 convert to radial derivative expansions of any fixed order on r>0. The leading nonlinear part of rho is -C y r^lambda. A homogeneous function of degree 1+lambda with smooth angular factor has the Holder class stated in Section1. One elementary proof is to bound its kth derivatives by O(r^(1+lambda-k)), split any two points according to whether their separation exceeds half the larger radius, and otherwise apply the next derivative bound along the connecting segment. The higher-order remainder has the same or better Holder regularity by these derivative bounds. Along the vertical axis,

    rho(0,y)=a y-C y |y|^lambda+O(|y|^(1+2lambda)).

For lambda<1 its second derivative is unbounded; for lambda=1 the one-sided second derivatives differ; for lambda>1 its third derivative is unbounded. The leading terms dominate the differentiated remainders. For velocity, restriction of psi_x to x=0 gives

    U2(0,y)=-y J(|y|)=-D y+[C/(lambda+4)]y|y|^lambda
                  +O(|y|^(1+2lambda)),

so the same nonregularity assertions hold for U. The fields are therefore outside the smooth primary class for every finite ell>1.

Here is a direct moment identity on the interval 2<m<2+lambda/2. Put H=y-rho/a, V=U2+Dy, w_m=y r^(-2m) and h=a-f. Since W=ell X+U has divergence 2ell, differentiation gives

    W.grad H-H-V=-R/a.

Integrate this equation after multiplication by w_m on eps<r<L. Integration by parts gives

    int [w_m V+(2ell+1)w_m H+H W.grad w_m] dX
       =(1/a)int w_m R dX + int_(boundary) w_m H W.n ds.

Near zero, H and V are O(r^(1+lambda)) and W=O(r), so all volume integrands are absolutely integrable if m<2+lambda/2, and the inner boundary term is O(eps^(4+lambda-2m)). At infinity H,V,W=O(r), and both the volume tails and the outer boundary term converge to zero if m>2; the outer term is O(L^(4-2m)). Therefore

    int_R2 [w_m V+(2ell+1)w_m H+H W.grad w_m] dX
       =(1/a)int_R2 w_m R dX=0.                         (13)

The last equality follows directly from R=r C3 sin(3theta), since w_m has angular factor sin(theta); absolute convergence justifies the polar integral.

For a second direct verification, perform the elementary angular products using the polar velocity above. The left side of(13) equals pi/a times

    int_0^infinity r^(3-2m) h[(4-2m)ell+mJ-f/4] dr.        (14)

In t=log r, the ODE(2) implies dot h=f h/(4ell-2J) and dot J=f-4J. Hence

    d/dt [exp((4-2m)t)(ell-J/2)h]
       =exp((4-2m)t) h[(4-2m)ell+mJ-f/4].                (15)

The bracketed primitive tends to zero at both ends: it is O(exp((4+lambda-2m)t)) as t tends to minus infinity and O(exp((4-2m)t)) at plus infinity. Integrating(15) proves(14) vanishes without a reference to another result. This uses the shorter interval permitted by the actual origin regularity. It does not assert smooth-class identities over the whole interval2<m<3 for this pair.

Finally the scaling rho_s(X)=s rho(X/s) sends f(r) to f(r/s), so C becomes C s^(-lambda) and K becomes K s^(1-p). The local contraction uniqueness and ordinary differential equation uniqueness identify all the constructed C>0 branches as this one scale orbit. The invariant parameters ell and a=4D do not change. This family shows sharpness of the radial regularity obstruction in result88 for the projected equation alone; it does not provide a finite-regularity solution of full IPM transport.

## 6. Global strain and density-gradient bounds

Retain k=-dot f/f and q=J/f from Sections3-4. We proved

    0<k<1, 1/4<q<1/(4-k), q<1/3.

The polar gradient has components f(1-k)sin(theta) and f cos(theta). Therefore

    |grad rho|^2=f^2[(1-k)^2 sin^2(theta)+cos^2(theta)]
                 <=f^2<a^2

at every positive radius. At zero the gradient is (0,a).

In the orthonormal polar frame the trace-free strain S=sym DU is

    S_rr=f(1-3q)cos(2theta), S_theta,theta=-S_rr,
    S_r,theta=f[(2+k)/4-3q]sin(2theta).

Indeed S_rr=partial_r U_r=(J+dot J)cos(2theta), and
2S_r,theta=r^(-1)partial_theta U_r+partial_r U_theta-U_theta/r
=(-2J+dot J-dot f/2)sin(2theta), giving these formulas directly.
Set A=1-3q and B=3q-1/2-k/4. These are temporary scalar coefficients, unrelated to the center parameter 2ell-1. We have

    0<A<1/4,
    0<(1-k)/4<B<3/(4-k)-1/2-k/4<1/4.

For the last inequality subtract 1/4: the result is k(k-1)/[4(4-k)]<0. Consequently

    ||S||_op^2=f^2[A^2 cos^2(2theta)+B^2 sin^2(2theta)]
                   <f^2/16<D^2.

At zero DU=diag(D,-D), so ||S(0)||_op=D. Since U is C^1 everywhere, integrate the symmetric derivative of W along the segment from Y to X. Its least eigenvalue is at least ell-D=1. This gives

    (W(X)-W(Y)).(X-Y)>=|X-Y|^2

for all X,Y. In particular W has no zero outside the origin. The density quotient rho/(a y)=f/a extends positively across y=0, lies strictly between0and1 for r>0 and tends to1 at zero. Thus even these global bounds together with all the convergent first-mode identities do not recover the missing third transport mode in this finite-regularity class. This does not refute any smooth-class theorem or any theorem that assumes the full transport equation.

Dependencies: result88 supplies the independently derived radial inverse and projection; the formulas needed here are restated and checked. The construction uses only the contraction principle, elementary ordinary differential equation continuation and explicitly bounded integrals. The moment identity and its fractional-exponent convergence range are proved directly above. Supporting exact arithmetic may check identities and inequalities but cannot replace this existence and regularity argument.
