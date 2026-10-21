# Fifth source endpoint under summable fourth derivatives

Date: 2026-10-20. Status: conditional theorem proved below, and a proved counterexample for transport with constant divergence. Neither is an unconditional theorem for coupled IPM.

## Statement, hypotheses and notation

Translate the source P to (0,0), write s=-r<0, and fix A>1 and q=4/A. Let f,W=(a,b) be C^(2,alpha), 0<alpha<1, in a neighborhood of P, smooth on its left punctured part. Assume

    a f_s+b f_y=f,   a_s+b_y=A+1,
    W(P)=0, DW(P)=diag(A,1), f_y(P)=g_*>0,

with a even and f,b odd in y. The letter a denotes horizontal velocity here, not the density factor at the other equilibrium. Choose a fixed left cone, radii R_n=2^(-n)r_0 and annuli

    A_n={(-r,y): R_n/2<=r<=R_n, |y|<=2 kappa r}.
    d_n=R_n^(q-1) sup_(A_n)(|D^4 f|+|D^4 W|).

D^4 includes every spatial derivative of total order four. If sum_n d_n is finite, then

    r^q f_yyyyy(-r,0) -> 0.

Consequently ell_5=lim G_5/H_5 exists and is zero, where G_5=f_yyyyy/120 and H_5 is any positive homogeneous fifth-order integrating factor, comparable to r^(-q). The theorem is valid for every A>1. Bounded fourth derivatives imply its hypothesis only when A<4; for A>=4 the hypothesis is substantially stronger and is not supplied by the default class.

For R_(N+1)<r<=R_N the following quantitative bounds hold:

    r^q |f_yyyyy(-r,0)| <= C(r^(q-2)+sum_(n>=N-3)d_n), q>2;
    r^q |f_yyyyy(-r,0)| <= C(r^q+sum_(n>=N-3)d_n), 0<q<=2.

## Algebraic cancellation

Set D=a partial_s+b partial_y, h=f_y/a, K=f_yyyy-h a_yyy. On the left cone a=-Ar+O(r^2) is nonzero. Define

    F=(a_y a_yyy/a-a_yyyy)(f_s+b h)
      -4 a_y f_syyy-6 a_yy f_syy-4 a_yyy f_sy
      -6 b_yy f_yyy-4 b_yyy f_yy+(a_s-3 b_y)h a_yyy.

For arbitrary smooth functions and E=Df-f, V=a_s+b_y, product differentiation gives

    (D+4 b_y-1)K-F=E_yyyy-(a_yyy/a)E_y-f_y V_yyy.

One way to verify the highest-order terms is to first differentiate h:

    D h=(1-V)h-(a_y/a)(f_s+b h)+E_y/a.

After expanding E_yyyy, the term b_yyyy f_y combines with a_syyy f_y from D(h a_yyy) to form f_y V_yyy. The other binomial terms give F. Thus the claimed transport equation (D+4b_y-1)K=F uses only transport and divergence. An independent symbolic check of the unrestricted identity accompanies this proof.

## Annular estimates

Use a smaller cone |y|<=kappa r. A ball of radius c r around any of its points lies inside the larger cone and meets at most the annuli with |n-N|<=2, for c fixed small. Put M=C r^(1-q) sum_(|n-N|<=2)d_n. It bounds every fourth derivative on the ball and on the vertical segments to the axis.

If q>2, the uniformly bounded C^2 norm and a one-dimensional Taylor estimate on a segment of length t<=c r give a bound C(t^(-1)+Mt) for each third derivative. Choosing t=min(c r,M^(-1/2)) yields L=C(r^(-1)+sqrt(M)), with L^2<=C(r^(-2)+M).

If 0<q<=2, use the summability directly. Along each ray (-r,eta r), |eta|<=kappa, the integral of a fourth derivative over annulus n is bounded by C R_n^(2-q)d_n. The initial third derivatives are bounded on a fixed compact outer section, uniformly in eta. Therefore all third derivatives on the cone are bounded by C+C sum_n R_n^(2-q)d_n, which is finite since 2-q>=0. In this case take L=C. This argument uses q>0 only later, in the characteristic integral; it does not require q>1.

Parity and C^2 bounds give |a| comparable to r, |a_y|+|f_s|+|b|<=C|y|, and bounded f_y,a_yy,f_sy. The odd derivatives a_yyy,f_syy are bounded by C|y|M. Also |b_yy|+|f_yy|<=C|y|L and |b_yyy|+|f_yyy|<=CL. Substitution in F gives

    |F|<=C|y|(M/r+L^2).

For example the first and last groups cost C|y|M/r. The three middle a-products cost C|y|M; the two b-products cost C|y|L^2. The term a_y a_yyy/a times f_s+b h costs C|y|^3 M/r^2<=C|y|M. No M^2 term is required. Directly from K on one annulus,

    |K(-r,y)|<=C r^(1-q)d_N.

## Characteristic exit and transverse limit

Start at (-r,y), 0<|y|<kappa r, and follow the characteristic (-R(t),Y(t)) backward to its first cone exit |Y(T)|=kappa R(T). The C^2 hypothesis and parity give, uniformly inside the cone,

    d log R/dt=A+O(R),  d log|Y|/dt=1+O(R), b_y=1+O(R).

After reducing r_0, backward motion decreases R and increases |Y|/R at a rate bounded away from zero. Thus T is finite; as y->0 with r fixed, T->-infinity and R(T)->0. The radius never reaches zero in finite time. Define J(t)=exp(int_0^t(4b_y-1)dt). Because Aq=4,

    d/dt log(J(t)|Y(t)|/|y| * (r/R(t))^q)=O(R(t)).

The integral of R(t) over [T,0] is at most 2r/A. The resulting bound J(t)|Y(t)|/|y|<=C(R(t)/r)^q is uniform in T.

Integrating the equation for K gives

    K(-r,y)=J(T)K(-R(T),Y(T))+int_T^0 J(t)F(-R(t),Y(t))dt.

After division by |y| the boundary term is at most C r^(-q)d_(n(T)), which tends to zero. The forcing integrand is at most C r^(-q) times

    sum_(|n-n(t)|<=2)d_n + R(t)^(q-2), if q>2;
    sum_(|n-n(t)|<=2)d_n + R(t)^q, if 0<q<=2.

Each annulus is visited once and takes bounded time. The first part integrates to the tail sum in the theorem. The two powers have finite integrals bounded respectively by C r^(q-2) and C r^q. Finally |h a_yyy|/|y|<=C r^(-q)d_N. Smoothness at the fixed point (-r,0) and oddness of f_yyyy allow passage to f_yyyyy there. This proves both estimates and the endpoint.

The first axis equation and divergence give w g'=(w'-A)g and b_y=A+1-w', where w=a(s,0), g=f_y(s,0). Hence H_5=C g^(5+q)(-w)^(-q) solves the homogeneous fifth equation and is comparable to r^(-q). This proves the stated normalized consequence without assuming beforehand that ell_5 exists.

## Sharp distinction between summability and convergence to zero

Fix 1<A<4, so 1<q<4. Take c smooth and nondecreasing, c=0 on (-infinity,4], c=1 on [5,infinity), with c' nonzero somewhere. Let l=log r and t=log|v|/l, and put

    F(s,v)=r^(1-q)v^5 c(t)/(q-1), s=-r<0,
    u=s+F_v, y=v+F_s, f(s,y)=v.

At v=0 use c=1. Extend F by zero for s>=0. For each r, F is supported in |v|<=r^4 and has polynomial core |v|<=r^5. It is smooth off (0,0), including across s=0 away from v=0. Let J=1+F_sv. Since F_sv=O(r^(16-q)), J>=1/2 in a small neighborhood. The coordinate change preserves area, since du wedge dv=J ds wedge dv=ds wedge dy. Pull back (Au,v):

    a=(A(s+F_v)-v F_vv)/J,  b=a F_ss+v J.

Transport and divergence hold exactly; the parities follow from F odd in v. An independent symbolic calculation, using Aq=4, gives

    a-As = r^(1-q)v^4/((q-1)J) *
       [5(At-1)c'(t)/l + ((At-1)c''(t)+A c'(t))/l^2].

For i+j<=4, repeated differentiation gives

    |partial_s^i partial_y^j(a-As)|<=C r^(1-q-i)|v|^(4-j)/|l|,
    |partial_s^i partial_y^j(f-y)|+|partial_s^i partial_y^j(b-y)|
       <=C r^(-q-i)|v|^(5-j).

The first bound is supported only in the transition. To justify physical differentiation, partial_y=J^(-1)partial_v and partial_s=-partial_r-F_ss J^(-1)partial_v. Each r derivative costs r^(-1), each v derivative |v|^(-1), and the extra term has the same cost times the small factor r^(-q)v^4. Derivatives of c introduce inverse logarithms. This proves the bounds by product differentiation, including mixed derivatives and inverse powers of J.

Since |v|<=r^4, third derivatives of a-As are O(r^(5-q)/|l|), and those of f-y,b-y are O(r^(8-q)). All tend to zero. The corresponding lower derivative estimates give a C^3 extension with baseline source jet. Fourth derivatives obey |D^4a|<=C r^(1-q)/|l| and |D^4f|+|D^4b|<=C r^(4-q). Thus d_n<=C((1+n)^(-1)+R_n^3). Conversely choose t_0 in (4,5) with c'(t_0)>0, v=r^t_0. Four transverse derivatives of the horizontal correction give

    a_yyyy = r^(1-q)/(q-1) *
       [120(At_0-1)c'(t_0)/log r+O(|log r|^(-2))
        +O(r^(16-q)/|log r|)].

These points lie in every fixed left cone for small r. The nonzero leading coefficient proves d_n comparable to (1+n)^(-1). In particular d_n->0 but its sum diverges.

In the core, y=v+r^(-q)v^5 and W=(As,y) exactly. Inversion gives G_3=0,G_5=-r^(-q) and ell_5=-1 with H_5=r^(-q). Curl fails there: b_s-a_y=0 but f_s=-q r^(-q-1)v^5/(1+5r^(-q)v^4) is nonzero off the axis. This is a counterexample for transport and constant divergence, not for coupled IPM.

## Application and limits of the audit

For the R12 axis data on B_3=0, the independent calculation in ../fifth-order/PROOF.md gives B_5<0 for 1<A<4 except the resonance A=2. In particular for 1<A<2, the axis third endpoint vanishes under class regularity and the fifth finite part is fixed by those axis data. Center smoothness requires ell_5+B_5=0. The additional summability theorem forces ell_5=0, so these R12 data cannot extend to a smooth-center coupled profile with the summability hypothesis. This excludes the stated axis family under an extra source hypothesis; it is not NO_inf for the full class. At A=2 one must instead use the logarithmic center condition.

This proof audits the lead's proposed o26 D9 v2, D9x, and resulting R12 consequence. D8 v3 changes only wording and cross-references already checked in ../source-estimates/PROOF.md. D10's power and logarithmic primitive constructions were independently established in ../transport-source/PROOF.md. Those constructions remain explicitly uncoupled. No assertion that the IPM velocity law supplies summability is proved here.

## Further regularity and the R12 consequence for 2<A<4

For the logarithmic-cutoff example set m=5-q, so 1<m<4. Every third derivative h of a-As has |h|<=C r^m and |grad h|<=C r^(m-4), using the stronger inverse-log bounds proved above. The two-point argument with threshold d=R^4/2 proves exponent m/4: above the threshold use amplitudes, below it integrate the gradient along a segment with comparable depths. The third derivatives of f-y and b-y are Lipschitz since their fourth derivatives are O(r^(4-q)), hence bounded. Therefore the pair is C^(3,(5-q)/4). This is an upper regularity assertion only; no sharpness at that exponent is needed. The polynomial core is |v|<=r^5, and the support is |v|<=r^4. These two sets must not be interchanged.

For 2<A<4, the summability theorem gives bounded third derivatives of f and W on the left cone and ell5=0. Since H3 is asymptotic to a positive constant times r^(-2/A), bounded G3 gives ell3=0. The third trace is consequently the source-selected solution in the R12 computation. At L^2=S_A its B3 vanishes but its B5 is strictly negative, as proved in ../fifth-order/PROOF.md. Here 11<p5=10+4/A<12 is nonresonant. Smoothness and even parity at the other equilibrium require ell5+B5=0, contradicted by ell5=0 and B5<0. Thus the R12 data are excluded in this range under the summable hypothesis as well. At A=2 the fifth exponent is the even integer12 and the logarithmic condition replaces this argument; no B5=0 inference is made there.
