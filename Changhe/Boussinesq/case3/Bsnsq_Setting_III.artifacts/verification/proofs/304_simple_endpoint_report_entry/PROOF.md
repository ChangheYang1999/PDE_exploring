# Simple endpoint theorem and local examples: complete entry audit

Written 2026-10-22, before entry controls. This proof audits the whole proposed report item 4.53. It concerns necessary axis equations and local analytic examples only. It neither constructs nor excludes a B2 profile.

## Statement and notation

Fix beta>0. Put L=3beta+2, M=2beta+1, N=7beta+2. Suppose smooth real b,T,eta,v,D near y_* satisfy

    b T_y+(L-2b_y)T=0,
    b eta_y+(M-b_y)eta=T,
    eta=-b_yy-2v,
    b D_y+(N-4b_y)D=8v_y T-12v T_y.              (1)

Assume b(y_*)=0, b_y(y_*)=-c<0, and T is nonzero on a chosen side y=y_*-epsilon s, s>0, epsilon in {-1,1}. Fix A!=0 with A/T>0 on that side. Then T=Cs^n tau(s), tau smooth, tau(0)=1, A/C>0, and n=2+L/c is an integer at least three. In particular T(y_*)=0 need not be assumed separately. Write I=D/T^2 and b=epsilon B(s). The extended real limit of I exists. If D has first nonzero order j, I is asymptotic to a nonzero constant times s^(j-2n); if D is flat, I tends to zero. This is a limit assertion, not a ban on oscillations that tend to a limit.

If b_yy(y_*)!=0, then

    D/T ~ -6 n epsilon b_yy(y_*)/(4beta+3c) s^-1,
    A I -> -sign(epsilon b_yy(y_*)) infinity.     (2)

For a genuine central axis component J, the side containing zero has epsilon=sign(y_*), and the previously established component geometry gives c>0. These are the only global facts used to specialize (1)-(2) to J.

At beta=2,c=1 the four equations admit every finite limit of I and both infinite limits of A I, even when T and eta have the sign of A and the local vanishing orders n=10,m=6 satisfy the profile integrality requirements. At every fixed beta>0 they admit every extended limit of A I without the extra eta sign and integrality conditions. These are separate local examples at one end; no simultaneous prescription of two ends or a distinct center is asserted.

## Derivation of the four equations

Write near x=0

    W_2=b(y)+v(y)x^2+O(x^4),
    W_1=(2beta-b_y)x-v_y x^3/3+O(x^5),
    Theta=T(y)x^2/2+D(y)x^4/24+O(x^6),
    Omega=eta(y)x+O(x^3).

The first two velocity coefficients follow from div W=2beta. The x^2 and x^4 coefficients of W.grad Theta-(beta-2)Theta give the first and fourth equations of (1). The x coefficient of W.grad Omega+Omega-Theta_x gives the second. The x coefficient of -curl W gives the third. No full transverse Taylor hierarchy is inferred from these four coefficients.

## Limit and curvature proof

Write B=sa(s), a(0)=c. Since d_y=-epsilon d_s and b_y=-B_s, the first equation gives T_s/T=(L+2B_s)/B=n/s+g(s), with g smooth through zero. Integration on s>0 gives T=C_0 s^n exp(G(s)), where G is a smooth primitive of g and C_0!=0. Here n>2. Smoothness forces n to be an integer: if the function were flat, Taylor bounds of an integer order larger than n would contradict its nonzero leading asymptotic; its first nonzero Taylor order must equal n. Normalize the analytic unit to obtain tau(0)=1. Taylor's theorem for D proves the stated limit classification.

Set K=D/T. Eliminating v and eta_s from (1) yields

    -B K_s+(4beta+2B_s)K=Q,
    Q=4B_sss-6B_ss(L+2B_s)/B
       -epsilon[(10beta+8+8B_s)eta+4T]/B.         (3)

At the endpoint (M+c)eta(0)=T(0)=0, so eta=O(s). Put B=cs+ks^2+O(s^3). Then k=epsilon b_yy(y_*)/2 and sQ tends to -12kn. With t=int_s^s0 du/B, one has t->infinity and d/dt=-B d/ds. Therefore Z=sK satisfies

    Z_t+(4beta+2B_s+B/s)Z=sQ.

The coefficient tends to 4beta+3c>0. For Z_t+a(t)Z=f(t), a->a_*>0 and f->f_*, the integrating factor shows Z->f_*/a_*: subtract f_*/a_*, split the forcing integral at a fixed late time, let the earlier part decay, and bound the late part by its supremum divided by a positive lower bound for a. This proves (2), since A/T->+infinity. The argument uses smooth Taylor estimates, not formal expansions.

## Beta two examples

For signed u=y_*-y, arbitrary C!=0,H,E, direct differentiation verifies

    b=u, T=C u^10, eta=H u^6-C u^10/4, v=-eta/2,
    D=E u^20-(36/5)CH u^15+5C^2 u^19.

Thus I=E/C^2-(36H/(5C))u^-5+5u^-1. With A/C>0, its A-weighted infinite signs are -sign(H) from below and sign(H) from above if H!=0. If H=0 they are sign(A) from below and -sign(A) from above.

To obtain any constant I=ell with v=0, solve in signed s=u

    s x_s=z-x, s z_s=-s^7 h,
    (1+x)s h_s=(z-6x)h-s^4 g,
    (1+x)s g_s=(2z-10x)g,
    x(0)=z(0)=0, h(0)=H, g(0)=C.

Set b=s(1+x), T=s^10g, eta=s^6h, D=ell T^2. The first two equations give b_ss=-eta. The next two give the first two equations of (1); the fourth follows from N-2L=beta-2=0. Analytic existence follows from the contraction lemma below with eigenvalues -1,0,0,0, forcing order four, and weight one. Choosing H/A>0 preserves both local profile signs, independently of ell.

For both infinite signs with those same signs, fix k!=0 and take

    B=u+k u^2+a u^13, a=-Ck/260.

The functions q=(8+2B')/B and p=(5+B')/B have principal parts 10/u and 6/u. Let T=C u^10 exp int_0^u(q-10/t)dt and Y=u^6 exp int_0^u(p-6/t)dt. The integrands are analytic. Put eta=Y(H-int_0^u T/(BY)dt), v=-(eta+B'')/2. The third integrand is analytic of order three. The first three equations of (1) hold. The fourth is I'=f, where

    f=[-4B'''+6B''q+6eta q-4eta']/(BT).

This has pole order at most twelve. Its residue is 48k/5+2496a/C. Here is an exact derivation. At a=0,

    T0=C u^10/(1+ku)^6, Y0=u^6/(1+ku)^4,
    eta0=Y0(H-CJ), J'=u^3/(1+ku)^3, J(0)=0.

The curvature part is 12k(10+4ku)(1+ku)^4/(C u^12), which has zero residue. The eta part is (36+16ku)(H/C-J)/u^6+4/[u^2(1+ku)^2]. Since J=u^4/4-3ku^5/5+O(u^6), its residue is 108k/5-4k-8k=48k/5. Adding a u^13 changes q,p by O(u^11), T/T0,Y/Y0 by 1+O(u^12), and eta-eta0 by O(u^18). The eta residue is unchanged. The denominator correction changes the old curvature term by O(1); the new curvature numerator at degree ten is [-4*13*12*11+6*13*12*10]a u^10=2496a u^10, giving residue 2496a/C. These order bounds control every remaining coefficient.

The chosen a cancels the residue, so f has a convergent meromorphic primitive I with leading term -120k/(11C)u^-11. Then D=T^2 I is analytic, since T^2 has order twenty. All four equations extend through zero by analyticity. Hence A I has sign -sign(k) infinity from below and sign(k) infinity from above. For H/A>0 both required local signs hold. A nonzero residue at a=0 would instead force a u^20 log|u| term in D.

## Every beta: the other local family

Put c=L, a=4beta+3, sigma in {0,1}, and choose ell real. In signed s=epsilon(y_*-y), seek

    b=epsilon s(c+x), T=s^3g, eta=s^3h,
    v=s^(4-sigma)w, D=ell s^(6-sigma)g^2.

Set delta=(1+2sigma)/2 and solve

    s x'=z-x,
    s z'=-epsilon s^4h-2epsilon s^(5-sigma)w,
    (c+x)s g'=(2z-3x)g,
    (c+x)s h'=(z-3x-a)h-g,
    s w'=delta w+(3/2)w(2z-3x)/(c+x)
                    -epsilon ell g[beta-2+sigma(c+x)]/8,

with x=z=0, g=C, h=-C/a and w=epsilon ell C(beta-2+sigma c)/(4(1+2sigma)) at zero. Direct substitution gives (1), including ell=0; the quotient is exactly ell s^-sigma. In the variable order (z,x,g-C,h+C/a,w-w(0)), the linear part is lower triangular with diagonal 0,-1,0,-a/c,delta. Its zero eigenspace is one-dimensional: the x and g rows force x=z=0, and the remaining rows determine h,w from g. Hence its zero Jordan block has size two. The analytic remainder has forcing O(s^4) and derivative O(|s|+|X|). The contraction lemma with weight two and delta<=3/2 gives an actual analytic solution. For finite desired R set sigma=0,ell=R/A; for either infinity set sigma=1 and sign(A ell) accordingly. Choose C with A/C>0. Here eta has sign -A and m=1+M/L lies strictly between one and two. Thus this family does not have the additional profile signs and integrality, as the report expressly states.

## Analytic contraction lemma used above

Suppose sX'=A0 X+R(s,X), R analytic near zero, R(s,0)=O(s^4), and D_XR=O(|s|+|X|). Suppose ||r^-A0||<=C r^-delta(1+|log r|^q), 0<r<=1. On holomorphic functions on a sufficiently small closed complex disk vanishing to order p>delta, use norm sup|X(s)|/|s|^p and map

    F(X)(s)=int_0^1 r^-A0 R(rs,X(rs)) dr/r.

For p=1,delta=0 or p=2,delta<=3/2, the image of zero has norm O(rho^(4-p)). On a fixed ball, the derivative estimate bounds the Lipschitz constant by C'(rho+rho^p), using integrals of r^(p-delta) and r^(2p-delta-1) times powers of |log r|. These converge. Small rho makes the map a contraction of the ball into itself. Uniform convergence gives a holomorphic fixed point, real on the real line by conjugation and uniqueness. Applying s d/ds-A0 to the integral gives the boundary term [r^-A0 R(rs,X(rs))]_0^1; its lower limit vanishes since p>delta. Thus it solves the stated singular ODE. Finite-dimensional Jordan form supplies the matrix estimates in both applications. This proves convergence rather than only formal solvability.

## Dependencies, entry scope, and verification

The coefficient and local analytic arguments are complete above; P296, P299 and P303 are independent antecedent proofs. The application to the center component uses only the explicitly identified hypotheses of report 4.42 and the axis sign and integrality facts in 4.13. The report transformation check must preserve its other claims, all existing tables and the 160 original timeline entries. An extended real limit does not rule out decaying oscillation, so the entry's phrase 'I_2 cannot oscillate' should say 'I_2 has an extended real limit'. No global inverse, center, complete axis hierarchy, far field, or B2 existence conclusion is obtained here. Formal sources are the read-only mathematical sources in verification; no Lean build is performed.
