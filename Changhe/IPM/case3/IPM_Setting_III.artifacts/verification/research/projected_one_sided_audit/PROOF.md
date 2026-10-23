# Independent audit of four one-sided projected-equation results

Result92. Source: the frozen MEL2_SOURCE.md in verification/. Written independently from the defining equations. Status: complete informal arguments below; exact algebra checker and final audit verdict recorded separately.

## Hypotheses and the four statements

Let ell>1, D=ell-1, A=2ell-1. Let rho be smooth on the whole plane, even in x and odd in y, with a=rho_y(0) nonzero and sublinear growth |rho|+(1+r)|grad rho| <= C(1+r)^gamma for some 0<gamma<1. Use its canonical velocity U=(-psi_y,psi_x), -Delta psi=rho_x, U=o(r), and impose the actual center relation psi_xy(0)=-D. Put

    h=rho-ay, H=-h/a, mu=yH, phi=psi+Dxy, V=phi_x,
    W=ell X+U=(Ax-phi_y,y+V), R=W.grad rho-rho,
    B=X.W/r^2, G=V/y,
    R_j(r)=integral_0^{2pi} R(r,theta) sin(j theta) dtheta.

The quotient G is interpreted by smooth odd extension. The additional one-sided hypothesis is mu>=0, equivalently rho/(ay)<=1, with the quotient extended on y=0. It does not assert rho/(ay)>=0. All four statements below are conditional on this additional hypothesis.

1. If 1<ell<=5, a>0, R_1=0 for every r, and h is not flat at zero, then a>=2A. Equality forces first degree n=3 and H_3=alpha x^2 y, alpha>0.
2. If R_1=0 and h is flat at zero, then r_*=inf{|X|:mu(X)>0} is positive and finite, rho=ay on r<r_*, and min_{r=r_*} B<=0. Consequently sup(-X.U/r^2)>=ell.
3. If rho has only odd sine modes through 2N+1, N>=1, and R_1=R_3=...=R_{2N-1}=0, then h cannot be flat. For N=1 only R_1 is needed.
4. If rho has only modes 1 and 3 and R_1=R_3=0, then 0<a<(3A+5)(A+7)=4(3ell+1)(ell+3), for every ell>1.

These are MEL2 Theorem4.1, Theorem4.2, Corollary4.3 and Theorem6.1, respectively. They are necessary conditions for projected equations, not existence results and not exclusions of the unrestricted primary class.

## Canonical first-mode identity and the endpoint relation

Normalize density modes by b_j=pi^{-1} integral rho sin(j theta). The stream coefficient of even index k is

    P_k(r)=(1/2)[r^k integral_r^infinity b_{k+1}(s)s^{-k}ds
                    -r^{-k} integral_0^r b_{k-1}(s)s^k ds].             (1)

To verify (1), differentiate the two moments and use
rho_x mode k = [b'_{k-1}-(k-1)b_{k-1}/r+b'_{k+1}+(k+1)b_{k+1}/r]/2.
Endpoint terms cancel. The complementary homogeneous modes r^k and r^{-k} are excluded by U=o(r) and regularity. Smoothness b_j=O(r^j) and sublinear growth justify all integrals. This gives the canonical strain c=-a/4+integral_0^infinity b_3(s)s^{-2}ds.

Only the stream mode k=2 contributes to the first sine mode of V. Direct differentiation of (1) gives

    v_1(r):=pi^{-1} integral V sin theta
       = r integral_r^infinity b_3(s)s^{-2}ds -(b_1+b_3)/4+Dr.          (2)

The imposed center relation cancels the linear term. If h=O(r^n) with Taylor derivative bounds, then v_1=O(r^n), v'_1=O(r^{n-1}). If h is flat, v_1 is flat. At infinity v_1=O(r), v'_1=O(1). This does not imply that all of V has order n: independent higher angular harmonic velocity terms can remain.

For 2<m<(n+3)/2 define the absolutely convergent quantities

    I_m=integral mu r^{-2m},
    L_m=integral mu (x/r)^2 r^{-2m},
    J_m=pi integral_0^infinity v_1(r)r^{2-2m}dr.

A plane integral representing J_m is circular if V has lower angular jets. Let f=y r^{2-2m}. Direct differentiation gives

    Delta f=4(m-1)(m-2)y r^{-2m},
    f_xx=2(m-1)y r^{-2m}[2m(x/r)^2-1].

Since Delta V=a H_xx, two integrations by parts yield

    J_m=a[2m L_m-I_m]/[2(m-2)].                            (3)

The boundary terms containing V project only onto v_1,v'_1, so (2) bounds the inner terms by O(epsilon^{n+3-2m}) and the outer ones by O(L^{4-2m}). The H terms have the same bounds. Thus no unproved pointwise order for all of V is used.

The identity W.grad H-H-V=-R/a, tested against y r^{-2m}, and div W=2ell yield, when R_1=0,

    J_m=2m integral mu B r^{-2m} -(2ell+1)I_m
                               -integral H W_2 r^{-2m}.                (4)

The test kills R precisely because its angular weight is sin theta. Its boundary flux has the same vanishing bounds. Equations(3)-(4), using W_2=y+V, give

    integral mu r^{-2m}{a[2m(x/r)^2-1]/[2(m-2)]
                        +A+3+G-2mB}=0.                               (5)

The displayed integral is absolutely convergent; the apparently singular G term is H V. At infinity H,V,W=O(r); at zero phi=O(r^4), V=O(r^3). These suffice without assumptions on all higher angular derivatives.

If H_n is the first nonzero homogeneous Taylor term, n>=3 odd, set C_n=integral H_n(omega)sin theta>0 and T_n=C_n^{-1}integral cos^2 theta H_n(omega)sin theta. Positivity and continuity give 0<T_n<1. As m tends upward to (n+3)/2, Taylor expansion gives (n+3-2m)I_m -> C_n and L_m/I_m -> T_n. In B=1+(A-1)(x/r)^2+beta, beta=O(r^2). Both the beta and G moments remain bounded at this endpoint, since their inner integrands gain two powers and their tails are integrable. Taking the endpoint in(5) and multiplying out proves

    [a-(n-1)(A-1)] [(n+3)T_n-1]=(n-1)^2.                  (6)

Every step so far uses only R_1=0. It does not substitute the full transport equation for a projected one.

## Proof of statement1

Write N=n-1 and z=(n+3)T_n-1. Equation(6) gives a=N(A-1)+N^2/z, z!=0.
For n=3, H_3=y(alpha x^2+beta y^2) with alpha,beta>=0. Circle moments give T=(alpha+beta)/[2(alpha+3beta)] and z=2alpha/(alpha+3beta). Hence alpha>0, 0<z<=2, and a>=2A, equality precisely beta=0.

For n>=5 and z>0, the strict bound T<1 gives a>N(A-1)+N^2/(N+3)>2A. The last difference is greater than N^2/(N+3)-2>0, since A>1 and N>=4.
For z<0, z>-1 gives a<N(A-n). If n>=9 and A<=9 this contradicts a>0.

For the remaining n=5,7 write H_n(omega)sin theta=sin^2 theta P(cos^2 theta), where P>=0 on[0,1] has degree K=(n-1)/2<=3. Under u=(1+cos varphi)/2, let g=(1-u)P(u). Then T=integral u g/integral g. These trigonometric polynomials have degrees <=5. Integration is exactly the six-point average at varphi_j=(2j+1)pi/6, because the nonconstant Fourier sums vanish through degree5. Since g>=0, T is a weighted average of u_j and so

    T >= (2-sqrt(3))/4 > 1/16.

The final comparison is 49>48 after squaring 7>4sqrt(3). Thus a<4(A-1)-32=4A-36<=0 at n=5; at n=7, a<6(A-1)-96=6A-102<0. Contradictions establish statement1, including its equality claim.

## Proof of statement2

Sublinearity and a!=0 imply mu is not identically zero, so r_*<infinity. Flatness and(2) make(3)-(4) valid for every m>2. Positivity gives 0<L_m<I_m. Consequently J_m/I_m is bounded above uniformly for large m: by a(2m-1)/[2(m-2)] if a>0, or |a|/[2(m-2)] if a<0.

Suppose B>=b0>0 on the support of mu in r<R for some R>r_*. Choose r0 with r_*<r0<R and c0=integral_{r<r0}mu>0. Then I_m>=c0 r0^{-2m}. On the inner disk, W_2/y is smooth and bounded. On r>=R the quantities mu,mu B,H W_2 are O(r^2), so their weighted tails are O(R^{4-2m}/(2m-4)). Even after multiplication by m and division by I_m these tails tend to zero. Equation(4) therefore implies J_m/I_m>=2mb0-C-o(1), contradicting the uniform upper bound.

If r_*=0, then B=1+(A-1)(x/r)^2+O(r^2)>=1/2 near zero, giving that prohibited situation. Hence r_*>0. If B were positive everywhere on its boundary circle, compactness would give B>=b0>0 on an annulus extending slightly beyond that circle; mu vanishes inside the circle, so this again gives the prohibited situation. Thus min B<=0 there. Finally B=ell+X.U/r^2 yields sup(-X.U/r^2)>=ell. Vanishing mu in the open disk gives H=0 off y=0 and then everywhere by continuity; hence rho=ay there. The argument does not claim U is affine inside the disk for R_1 alone.

## Proof of statement3

If h were flat, statement2 would give an affine density disk. Formula(1), using the highest density mode2N+1, gives inside that disk

    psi=-Dxy+sum_{j=2}^N C_j r^{2j}sin(2j theta).

Indeed the exterior source mode for stream2j is b_{2j+1}, so no higher harmonic is present. On the disk R=a phi_x=a sum_{j=2}^N 2j C_j r^{2j-1}sin((2j-1)theta). The stated projections force each C_j=0. Thus W=(Ax,y) in the disk and B>=1 on its boundary, contradicting statement2. The empty sum at N=1 causes no exception.

## Proof of statement4

Statement3 excludes flatness. Let the first degree of h be N+1, N>=2 even, with

    b_1=ar+alpha r^{N+1}+O(r^{N+3}),
    b_3=beta r^{N+1}+O(r^{N+3}).

One-sidedness gives alpha/a<0 and lambda=beta/alpha in[-1/3,1], since the angular polynomial is 1+lambda(4cos^2 theta-1)>=0. Formula(1) gives the stream coefficients

    P_2=-D r^2/2 -(alpha/(N+4)+beta/N)r^{N+2}/2+O(r^{N+4}),
    P_4=-beta r^{N+2}/[2(N+6)]+O(r^{N+4}).

No intermediate harmonic jets occur in this two-mode case. Expanding U_r=-2P_2 cos2theta/r-4P_4 cos4theta/r, U_theta=P'_2 sin2theta+P'_4 sin4theta, and the density gradient, the two leading projection coefficients, multiplied by4, are the rows of

    [[N(A+3)-a,             (N+4)(A-1-a/N)],
     [N(A-1-a/(N+4)),       2((N+1)A+N-1-a)]] [alpha,beta]^T = 0.       (7)

The independent checker derives these by direct angular products, not by substituting the producer's projected formulas.

Put E=A-1>0 and d=1+(N+4)lambda/N. Then (2N-4)/(3N)<=d<=2+4/N. The first row of(7) says (E-a/N)d+4=0. Therefore d>0 and a=N(E+4/d)>0. The second row reduces to

    E(d+1)+2N(d-3+1/d)=0,
    E/N=F(d)=2(-d^2+3d-1)/[d(d+1)].                      (8)

In particular delta=(3-sqrt5)/2<d<(3+sqrt5)/2. For N<=6,

    a<6E+24/delta=6E+36+12sqrt5<6E+64<(3E+8)(E+8).

Here sqrt5<7/3 follows from45<49. For N>=8 set L_N=(2N-4)/(3N) in[1/2,2/3) and T_N=2+4/N in(2,5/2]. The derivative F'=(-8d^2+4d+2)/[d^2(d+1)^2] has one positive critical point, a maximum. Moreover F(L_N)>=2/3 and F(T_N)<=1/3. Thus F(d)>=F(T_N) on the whole allowed interval. It follows that

    E>=N F(T_N)=N(N^2-4N-16)/[(3N+4)(N+2)] > N/3-22/9.

The last strict difference equals (52N+176)/[9(3N+4)(N+2)]>0. Since d>=1/2, we get

    a<=N(E+8)<(3E+22/3)(E+8)<(3E+8)(E+8).

Replacing E=A-1 yields statement4. Neither this estimate nor statement3 asserts that the projected two-mode class is nonempty. Our separate finite-angular full-transport exclusion requires additional projections and is consistent with these statements.

## Audit limits

The source assumptions, sign conditions, circular integrals, endpoint limits, affine-disk conclusion, equality case, harmonic modes and the two-mode restriction have all been checked explicitly. These proofs do not establish an upper bound on a for unrestricted angular content or force the one-sided condition in the primary class. No projected identity is treated as the full PDE. No computer-assisted existence claim is made. Formal sources: none; no Lean or Lake build was run.
