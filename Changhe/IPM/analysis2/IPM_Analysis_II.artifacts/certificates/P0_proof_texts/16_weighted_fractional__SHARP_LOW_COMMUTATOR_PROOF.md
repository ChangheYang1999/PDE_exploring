# Direct weighted negative-order commutators

Status: independently audited, V080. Constants are sufficient bounds, not sharp optimal constants.

## 1. Statement, notation and scope

Let R>=1, sigma=11/5, w=(1+r2/R2)^(-sigma/2), v0=w and v1=<r>w. Work on the centrally odd homogeneous negative-order space L(h)=||wh||Hdot^-1, with its canonical Fourier realization and compact smooth core. Put J=(1-Delta)^1/2 and0<s<=2^-12. All derivative tensors below are ordered Cartesian tensors; Sigma norms are sums of component supremums. The constants are uniform in R.

For a smooth centrally odd divergence-free vector field u, write

    T_u=[J^s,u.D]J^-s, B_d=[J^s,d]J^-s,
    D1=||Du||Sigma,infinity, D2=||D2u||Sigma,infinity,
    t_u=312 D1+5665 D2, b_u=1370 D2.

Then

    L(T_u h)<=s[(27/5)t_u+(16/5)b_u]L(h).                 (1)

For a smooth centrally even scalar d, put A1=||Dd||Sigma,infinity and A2=||<r>D2d||Sigma,infinity. Then

    L(B_d h)<=1370s[(27/5)A1+A2]L(h).                    (2)

For a rough velocity W=U[k], with k in the N_s^w space of PROOF.md and n=N_s^w(k),

    L(T_W h)<=(700416/5)(n/sqrt(s))L(h).                 (3)

This last operator is defined by density from smooth k. No third derivative of W, or bounded second derivative of W, is assumed. Also

    L(J^-s h)<=6L(h), L(J^-2 h)<=821L(h).                (4)

These statements concern commutator operators and do not say that u.D itself is bounded on L. Proofs below retain the density weight throughout; no factor sup(w/omega0) occurs.

## 2. Polynomially moderate Bessel kernels

For either v=v0 or v1 and z=X-Y,

    v(X)/v(Y)<=(1+|z|)^(16/5)<=(1+|z|)^4=:m(z),
    |v(X)/v(Y)-1|<=m(z)-1.                               (5)

Indeed <X>/<Y><=1+|z| and (R2+|Y|2)^(1/2)/(R2+|X|2)^(1/2)<=1+|z|/R. Applying these inequalities in both directions proves the difference estimate. In addition,

    |r Dlog w|<=sigma, |<r>Dlog w|<=sigma.                (6)

The second bound uses R>=1 and r<r><=R2+r2.

Let kappa_s be the positive fractional kernel and b_s the positive kernel of J^-s. The heat-mixture formulas in PROOF.md and ROUGH_INVERSE_PROOF.md give, with K_j=int |z|^j kappa_s(z)dz,

    K1<=13s, K2=2s, K3<=30s, K4<=16s, K5<=420s.           (7)

The first three were proved earlier. K4=16s(1-s/2). For K5, its exact expression is30sqrt(pi)s Gamma((5-s)/2)/Gamma(1-s/2). The numerator is at most4/9+5/e<7/3 by splitting at1; Gamma(1-s/2)>e^-1, sqrt(pi)<2 and e<3 yield420s. All these bounds hold already for0<s<=1/2.

If M_j=int |z|^j b_s(z)dz, then

    M1<=9s, M2=2s, M3<=36s, M4=16s(1+s/2)<=20s.           (8)

For M1 and M3 use1/Gamma(s/2)<=es/2, Gamma((s+1)/2)<3 and Gamma((s+3)/2)<2, with the same elementary integral splits. Thus

    int m b_s<=1+212s, int(m-1)kappa_s<=200s,
    int |z|m kappa_s<=685s.                              (9)

Because kappa_s is radial decreasing, integration by parts gives

    int |z|^j |Dkappa_s|=(j+1)K_(j-1), j>=2.

The boundary terms vanish at0 since j>1+s, and at infinity by the heat mixture. Consequently

    int |z|2 m |Dkappa_s|<=4295s,
    int |z|(m-1)|Dkappa_s|<=900s.                         (10)

Young's inequality and(5) now show ||vJ^-s f||2<=(1+212s)||vf||2<=2||vf||2.

For the second-order Bessel resolvent q_ij=partial_ij J^-2, its unweighted operator norm is at most1. Its off-origin kernel has absolute moment bounds

    int r^j |q_ij| <=(2pi,10,9pi,112), j=1,2,3,4.

These follow by integrating |partial_ij p_t|<=(r2/(4t2)+1/(2t))p_t against e^-t. The local delta term commutes with v. Hence

    ||v partial_ij J^-2 f||2
       <=[1+4(2pi)+6(10)+4(9pi)+112]||vf||2
       =(173+44pi)||vf||2<312||vf||2.                    (11)

## 3. Weighted L2 commutator bounds

A coefficient difference bounded by A1|z|, together with(9), proves

    ||v B_d f||2<=1370s A1||vf||2.                        (12)

There is also the cross-weight version

    ||<r>w B_d f||2<=1370s||<r>Dd||Sigma,infinity||wf||2. (13)

To check it, integrate Dd along the segment Z between X and Y. The extra ratio <X>/<Z> is at most1+|z|; the remaining weight ratio is w(X)/w(Y)<=(1+|z|)^(11/5). Their product is bounded by m(z), so precisely the same moment685s applies. This estimate uses no translation on Hdot^-1.

Taylor expansion of u(X)-u(X-z) gives the linear term -s sum u_(j,i)(X) partial_ij J^-2. Equation(11) bounds it. Integrating the derivative off the Taylor remainder gives the cost

    2[(4295/2)+685]s D2=5665s D2.

The factor2 is the J^-s bound, and the two summands retain both differentiated-kernel and differentiated-remainder terms. Thus for either v,

    ||v T_u f||2<=s t_u||vf||2.                          (14)

All small-circle boundary terms are O(epsilon^(1-s)).

For the rough W, write A=(2pi)^-1 int |xi||W_hat| and d=||DW||infinity. V077 gives A,d<=2^11 n/sqrt(s). The Fourier multiplier inequality in ROUGH_INVERSE_PROOF.md gives ||[J^s,W.D]f||2<=A||J^s f||2. The relative double commutator has kernel Dkappa_s(z).(W(X)-W(Y))(v(X)-v(Y));(10) gives its norm at most900s d||vf||2. Also(9) gives

    ||J^s(vf)||2<=(1+400s)||vJ^s f||2.

Therefore, for either v,

    ||v T_W f||2<=(1+2200s)A||vf||2<=2A||vf||2.          (15)

The V077 H^s product bound applies to Dg, including DW for g=k. Commuting v at both ends using(9) yields

    ||vJ^s(Dg f)||2
      <=[2^14(1+400s)+400s*2^11](N_s^w(g)/sqrt(s))||vJ^s f||2
      <=2^15(N_s^w(g)/sqrt(s))||vJ^s f||2.               (16)

The final numerical inequality holds for s<=2^-12. Subtracting multiplication by DW gives the deliberately rounded bound

    ||v B_DW f||2<=36864(n/sqrt(s))||vf||2.               (17)

The vector and tensor versions use Euclidean contraction and the same V077 constants, not an extra component count. In the smooth bounds(12)-(14), the Sigma norms already count all entries.

## 4. Negative-order factorization and parity

Given h in the core, let q=D(-Delta)^-1(wh), a=Dlog w and v=w^-1q. Then ||q||2=L(h), q is centrally even, and

    h=-div v-a.v.                                        (18)

For every divergence-free u, differentiation gives the exact operator identity

    [partial_i,T_u]=sum_j partial_j B_(partial_i u_j).    (19)

It remains valid by approximation for W. Applying T to(18) and multiplying by w expresses wTh as a sum of divergences of wTv and wB_Du v, multiplication of these two vector terms by a, and the remaining term -wT(a.v).

Divergences have Hdot^-1 norm at most the vector L2 norm. Every non-divergence remainder is centrally odd, so the parity Hardy estimate ||f||Hdot^-1<=||rf||2 applies to it. Equation(6) therefore gives

    L(Th)<=[(1+sigma)(C_T+C_B)+sigma C_T^+]L(h),          (20)

where C_T,C_B are weighted L2 norms on w, and C_T^+ is the norm on <r>w. Substitution of(12),(14) proves(1). Substitution of(15),(17) gives

    (27/5)*4096+(16/5)*36864=700416/5,

proving(3).

For B_d, use [partial_i,B_d]=B_(partial_i d). The analogous factorization has one divergence term, the multiplication by a, the final -wB_d(a.v), and the cross term wB_Dd v. Estimate that last term by Hardy and(13). This proves(2). For the order-zero radial Bessel operator J^-s the derivative commutator vanishes, so the same argument gives

    L(J^-s h)<=(1+2sigma)(1+212s)L(h)<6L(h).

For J^-2, its m-weighted positive kernel has integral89+20pi<152. Thus its negative-order norm is at most(27/5)*152<821, proving(4).

These identities are initially distributional identities on smooth inputs. The intermediate v need not be unweighted L2, but is in L2(w2); every Bessel and commutator operator used above is bounded on that weighted space by(9)-(17). Polynomially weighted truncation and smoothing therefore justify the integrations. Every scalar Hardy input has the required odd central parity. Density then defines the bounded operators on L, and their distributional action agrees with the displayed formulas. No unbounded translation on weighted Hdot^-1 was assumed.

## 5. Application to the smooth background coupling

For Qh=U[h].D rho, J^s commutes with the canonical U, so

    [J^s,Q]J^-s h=sum_j B_(partial_j rho) U_j[h].          (21)

Use(2), the V067 vector velocity bound13/2 on L, and the sums of coefficient supremums. With the state131 bounds D1<=12,D2<=24, ||D2rho||Sigma<=12 and ||<r>D3rho||Sigma<=256,

    ||T_u||_(L->L) <=(4298088/5)s,
    ||[J^s,Q]J^-s||_(L->L) <=2856724s.                   (22)

The canonical velocity is applied on L before the multiplication commutator; no false weighted L2 bound on U with weight w is used. Finally the dilation commutator sc(I-J^-2) has L norm at most1644s for |c|<=2. These estimates supply the low part of the sharper compatible inverse in SHARP_ROUGH_INVERSE_PROOF.md.
