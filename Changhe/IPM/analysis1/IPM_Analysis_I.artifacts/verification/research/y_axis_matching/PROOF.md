# Canonical y-axis jets and the diagonal endpoint matching conditions

Status: standalone proof written before code. Statements about the full coupled operator are exact identities under the regularity below. The endpoint inverse and matching results concern the diagonal scalar rows with known forcing. They do not prove an inverse or a cokernel dimension for the coupled IPM equation.

## Hypotheses and notation

Write X=(x,y), r=|X| and E=x partial_x+y partial_y. Initially let h be smooth, compactly supported, even in x and odd in y, with h(0,y)=0. Use the canonical full-plane inverse -Delta psi[h]=partial_x h, U[h]=(-psi_y,psi_x). Write ell[h]=psi[h]_{xy}(0) and delta c_l[h]=ell[h]/3. Thus ell is the strain, not the prompt's scaling functional. We use Taylor coefficients, not unnormalized derivatives:

h=x^2 a_2(y)+x^4 a_4(y)+O(x^6),
U_1[h]=x u_1(y)+x^3 u_3(y)+x^5 u_5(y)+O(x^7),
U_2[h]=u_0(y)+x^2 u_2(y)+x^4 u_4(y)+O(x^6).

These local identities also hold for noncompact h when the canonical velocity exists, is sufficiently differentiable, and the displayed expansions are justified. No such extension is inferred merely from a conormal completion.

Let the background be even in x and odd in y, and smooth near the relevant axis, with

rho=x^2 r_2(y)+x^4 r_4(y)+O(x^6),
V_1=x u(y)+x^3 w(y)+O(x^5),
V_2=v(y)+x^2 z(y)+O(x^4),
V=c_l X+U[rho]. In particular u=c_l+partial_x U1[rho](0,y) and v=c_l y+U2[rho](0,y).

The normalized linearization is Lh=(V dot grad-1)h+U[h] dot grad rho+(ell[h]/3)E rho. For the center identity assume rho and h are C3 locally, rho=J x^2y+o(r^3), h=b x^2y+o(r^3), both velocities C1, and 3c_l-ell[rho]=1. The scalar J may be any real number; normalization of rho sets J=1.

For the separate diagonal endpoint result, let c_l>1, k=1/c_l, A=2c_l-1 and D=4c_l-1=2A+1. Assume u is even smooth near0, v odd smooth near0 and v>0 on(0,infinity). Require

v=Dy+O(y^3), u=-A+O(y^2) near0,
v=c_l y+O(y^k), u=c_l+O(y^(k-1)) at infinity,

with the derivatives needed for each asserted smooth expansion. Define

T_j a=v a'+(2j u-1)a, j=1,2,
p_j=(2j A+1)/D, p_1=1, p_2=2-1/D in(5/3,2).

Fix 1<gamma<1+k. The far jet space has squared norm integral_R^infinity y^(4j+1-2gamma)|a(y)|^2 dy. Forcing F is smooth and odd near0, locally smooth on(0,infinity), and has finite far norm of this same order. The forcing can in particular be smooth and compactly supported.

## Reconstructing the nonlocal trace and its Taylor coefficients

Fourier transform in y only with convention exp(-i eta y). Put kappa=|eta|>0 and R_kappa=(kappa^2-partial_x^2)^(-1), whose Green kernel is exp(-kappa|x-z|)/(2kappa). Directly from the Poisson equation,

psi_hat=partial_x R_kappa h_hat,
U2_hat=partial_x^2 R_kappa h_hat=-h_hat+kappa^2 R_kappa h_hat,
U1_hat=-i eta partial_x R_kappa h_hat.

Because h is even in x and h(0,y)=0, the axis trace B(y)=U2[h](0,y) satisfies

B_hat(eta)=kappa integral_0^infinity exp(-kappa z)h_hat(z,eta) dz.  (1)

For compact smooth h the limit at eta=0 is0, consistent with the formula by continuity. This is a nonlocal moment; it is not determined by the local density Taylor coefficients.

Apply Delta U2=-partial_x^2 h and div U=0. Equating powers of x gives

u_0=B,
u_2=-a_2-B''/2,
u_4=-a_4+a_2''/12+B''''/24,
u_1=-B',
u_3=a_2'/3+B'''/6,
u_5=-u_4'/5,
ell[h]=B'(0).  (2)

In (2), u_j are the coefficients in the opening display. In particular u_4 is absent from the x^4 coupling equation below, since rho_y begins at x^2. The coefficients a_2'' and B'''' do not appear in that row. Formula (1) is useful for fixed smooth compact extensions of a_j; it is not by itself a global estimate for variable-width extensions or nonsmooth completions.

## Exact coupled rows and the cubic compatibility identity

Multiplication of the displayed series gives, for f=Lh,

f_2=v a_2'+(2u-1)a_2+2r_2 u_1+r_2' u_0+(ell[h]/3)(2r_2+y r_2'),  (3)

f_4=v a_4'+(4u-1)a_4+2w a_2+z a_2'
       +4r_4 u_1+2r_2 u_3+r_4' u_0+r_2' u_2
       +(ell[h]/3)(4r_4+y r_4').  (4)

The zeroth density jet is zero because V1=U1[h]=0 at x=0, while h and rho vanish identically on that axis with their tangential derivatives. The remainder with zero a_2 and a_4 is not invariant: its nonlocal B can generate the right side of (3) and (4).

At the origin the parity and canonical strain give

DU[rho](0)=diag(-ell[rho],ell[rho]),
DU[h](0)=diag(-ell[h],ell[h]).

C3 Taylor remainder control for rho,h and C1 expansions for the velocities imply

[x^2y]Lh=b(3c_l-ell[rho]-1)+J(3 delta c_l[h]-ell[h])=0.  (5)

Indeed V dot grad(x^2y)=(3c_l-ell[rho])x^2y to leading order, U[h] dot grad(Jx^2y)=-J ell[h]x^2y, and delta c_l[h]E(Jx^2y)=3J delta c_l[h]x^2y. The remainders are o(r^3). No derivative of order four is needed. If Lh=f, its cubic coefficient must vanish under these hypotheses even when b is allowed to be nonzero. This identity imposes a range condition; it does not remove the independent normalization b=0 when that condition is required of h.

For the normalized background J=1, in the smooth coefficient notation r_2=y+O(y^3) and B=ell[h]y+O(y^3). The three coupling terms in (3) have y coefficients -2ell[h],ell[h],ell[h], whose sum is0. Thus the known diagonal forcing

F_2=f_2+2r_2 B'-r_2' B-(ell[h]/3)(2r_2+y r_2')

satisfies F_2'(0)=f_2'(0). The dependence of B on the entire perturbation remains; a formula for a_2 in terms of known F_2 does not invert this coupled equation. In the full problem F_2 and the analogous F_4 depend on h through B and its derivatives. Conditions on these F_j are conditions on a putative coupled solution, not cokernel functionals of the supplied f alone. No smoothness or far-norm bound for B[h] in a general far jet completion is inferred here.

## Positive homogeneous solutions and the far endpoint

There is a unique positive homogeneous solution H_j normalized by H_j/y^p_j ->1 at0. Explicitly it solves

H_j'/H_j=(1-2j u)/v.

Near0 the right side is p_j/y+O(y), with smooth odd error. Thus H_j=y^p_j times a smooth positive even factor equal to1 at0. At infinity the right side equals(k-2j)/y+O(y^(k-2)). The error is integrable because k<1. Hence H_j/y^(k-2j) tends to a positive finite constant. In particular, for sufficiently large R there are m_H,M_H,v_0>0 with

m_H<=H_j(y)y^(2j-k)<=M_H, v(y)>=v_0 y, y>=R.  (6)

The far norm of H_j diverges: its square integrand is comparable to y^(2k+1-2gamma), whose exponent is greater than-1 because gamma<1+k. A difference C H_j can therefore lie in the far space only for C=0.

Cauchy-Schwarz and (6) give convergence of the integral from y to infinity of F/(vH_j). For its tail,

integral_R^infinity |F|/(vH_j) dy
 <= ||F||_far R^(gamma-1-k)/(v_0 m_H sqrt(2(1+k-gamma))).  (7)

Every solution in the far space must therefore equal

a_infinity(y)=-H_j(y) integral_y^infinity F(z)/(v(z)H_j(z)) dz.  (8)

To see existence in the far space, set t=log y, lambda=1+k-gamma>0 and multiply a and F by exp((2j+1-gamma)t). Using (6), the transformed kernel is bounded in absolute value by (M_H/(v_0 m_H))exp(-lambda(s-t)) for s>=t. Minkowski and the L1 norm1/lambda of this kernel prove

||a_infinity||_far <= M_H/(v_0 m_H lambda)||F||_far  (9)

on y>=R. This gives uniqueness in the far space on[R,infinity); the assumed smoothness of F on(0,infinity) and v>0 continue the solution uniquely to every positive y. Differentiation on compact subintervals verifies T_j a=F. Any other solution differs by C H_j and is excluded by the far norm. No assertion that the full coupled operator is onto follows.

## Local matching: second-order density jet

For j=1, H_1=y times a smooth even factor, and vH_1=D y^2 times such a factor. If F'(0)!=0, the integral in (8) produces the nonzero term (F'(0)/D)y log y. Thus it fails C1 at the center. If F'(0)=0, odd smoothness gives F=O(y^3), and F/(vH_1)=O(y). The integral converges also at0 and

a_infinity=-I_1 H_1+H_1 integral_0^y F/(vH_1),
I_1=integral_0^infinity F/(vH_1).  (10)

It follows that a_infinity=-I_1 y+O(y^3) with a smooth odd extension. One can check smoothness by changing variables z=y tau in the local integral; the even smooth coefficients have integrable tau weights. If the y coefficient is free, there is no further local matching condition. If the original cubic normalization of h requires a_2'(0)=0, there is the additional condition I_1=0. The fact that a scaling vector is absent from some far space does not remove this condition.

## Local matching: fourth-order density jet and required subtraction

For j=2 let p=p_2, so1<p<2. The unregularized integral from0 of F/(vH_2) generally diverges even for smooth admissible data. For example a=y chi_0(y), with an even compact smooth chi_0 equal to1 near0, is smooth and has compact support. Yet F=T_2a=D(1-p)y+O(y^3), and F/(vH_2) is a nonzero constant times y^(-p) to leading order.

For a general smooth odd F choose this same kind of cutoff, put

b_F=F'(0)/(D(1-p)), S_F=b_F y chi_0(y),
G_F=F-T_2S_F,
ell_4^0(F)=integral_0^infinity G_F/(vH_2).  (11)

The numerator is O(y^3); near0 the quotient is O(y^(2-p)), hence integrable. The far tail is integrable by (7). If two cutoffs are used, their difference S has compact support and vanishes near0, and

(T_2 S)/(vH_2)=(S/H_2)'.

The two boundary values are0, so ell_4^0 does not depend on the cutoff. Subtracting T_2S_F from (8) gives

a_infinity=S_F-ell_4^0(F)H_2+H_2 integral_0^y G_F/(vH_2).  (12)

The last term is smooth odd and O(y^3): the substitution z=y tau factors it as y^3 times a smooth even function, with integrable weight tau^(2-p). Thus ell_4^0(F)=0 is necessary and sufficient for a smooth odd local extension of the far-selected solution. If it is nonzero, the term -ell_4^0(F) sgn(y)|y|^p times a smooth even positive factor is not C2 at0. In particular it is not in local H^s for s>5/2, including153/50.

The sharper exclusion is H^s nonmembership for s>=p+1/2. Here p>5/3, so the second derivative has leading nonzero coefficient sgn(y)|y|^(p-2), with exponent alpha=p-2 in(-1/3,0). For0<sigma<1 its fractional Gagliardo seminorm has, on0<x<delta and2x<y<3x, a lower bound by a constant times integral_0^delta x^(2alpha-2sigma) dx. This diverges for sigma>=alpha+1/2. The smoother terms cannot cancel the leading power; choose delta small to preserve the lower bound. Set s=2+sigma, then use Sobolev nesting for larger s. This proves the exclusion including the logarithmic divergence at s=p+1/2.

For a quantitative local contribution, if |G_F(y)|<=M y^3, v(y)>=v_c y and H_2(y)>=h_c y^p on0<y<=d, then

integral_0^d |G_F|/(vH_2) <= M d^(3-p)/(v_c h_c(3-p)).  (13)

Together with (7), this bounds the matching functional in the explicit sum of sup_{0<y<=d}|G_F(y)|/y^3, integral_d^R |G_F|/(vH_2) dy, and ||F||_far, with the displayed fixed positive coefficient bounds and a cutoff supported below R. No continuity in a weaker unspecified norm is claimed.

## Diagonal homogeneous Sobolev rate

For the homogeneous local model T_j^0=D y partial_y-Dp_j, take a Schwartz test function whose Fourier transform is smooth and compactly supported away from0. Direct Fourier transformation gives

(T_j^0 a)_hat=-D eta partial_eta a_hat-D(1+p_j)a_hat.

Integration by parts, with no frequency boundary terms, yields

Re <T_j^0 a,a>_{dot H^s}=D(s-1/2-p_j)||a||_{dot H^s}^2.  (14)

This is the homogeneous diagonal rate only. A positive value does not estimate lower-order terms, the nonlocal B, the variable coefficients, cutoffs, matching constants or an inhomogeneous global norm. The degree-four row changes sign at s=p_2+1/2. A low local regularity at P and a tangential jet regularity at the y-axis are distinct design choices.

## Independent finite trace integral and a manufactured endpoint example

For a separate numerical test of (1), use p(x)=x^2(1-x^2)^8 on|x|<=1 and zero outside. This compact C7 function is even, has p(0)=0, and suffices for the trace integral; it is not being called C-infinity. Its multiplier is M(kappa)=kappa integral_0^1 exp(-kappa z)z^2(1-z^2)^8 dz. It lies strictly between0 and2/kappa^2, by comparison with the integral of exp(-kappa z)z^2 on the positive half-line.

One exact method expands (1-z^2)^8 and uses

J_n=integral_0^1 exp(-kappa z)z^n dz
   =n! kappa^(-n-1)[1-exp(-kappa)sum_{q=0}^n kappa^q/q!].  (15)

An independent method expands exp(kappa(1-z)) and (1+z)^8, both positively, after writing (1-z^2)^8=(1-z)^8(1+z)^8. It gives

M=kappa exp(-kappa) sum_{q=0}^infinity [kappa^q/q!] sum_{m=0}^8 binom(8,m) B(3+m,9+q).  (16)

All terms are positive. The ratio of successive terms in q is at most kappa/(q+1), because the Beta factor ratio is (q+9)/(q+m+12)<1. Thus the tail after N is at most the next term divided by1-kappa/(N+2), when N+2>kappa. These formulas test finite trace values, not a norm of a full extension operator.

For an endpoint example with explicit homogeneous solutions, take

v=y(D+c_l y^2)/(1+y^2), u=(-A+c_l y^2)/(1+y^2),
H_j=y^p_j[1+(c_l/D)y^2]^((k-2j-p_j)/2).  (17)

Direct logarithmic differentiation verifies T_j H_j=0. The field has v>0 and the stated endpoint asymptotics. The smooth odd function a=y/(1+y^2)^3 lies in each far jet space for the displayed gamma=1129/1000. For F=T_2a,

integral_d^infinity F/(vH_2)=-a(d)/H_2(d),
d^(p_2-1) integral_d^infinity F/(vH_2)
 =-(1+d^2)^(-3)[1+(c_l/D)d^2]^((p_2-k+4)/2) ->-1.  (18)

This gives explicit divergent bare integrals as d decreases, despite a smooth far-admissible solution. The regularized condition (11) is zero for this solution by the proved boundary identity. No claim of compact support for this rational example is made.

## Verification plan and scope

Independent symbolic series multiplication will check (2)-(5) and the scalar integrating-factor identities. For illustration only use k=1615536043799051/9007199254740992 and c_l=1/k. Exact rational arithmetic and two interval libraries will check this illustrative modal c_l, the two p_j, far Hardy margin and rates at s=153/50. A rational model with interpolated positive v,u will check the local/far asymptotic powers and a manufactured compact solution exposing the divergent bare fourth-jet integral. Higher precision output auditing will check the recorded interval outputs. An actual Claude Opus5.5 exchange is retained as review provenance; it is not a replacement for the mathematical argument or executed checks. The final local manifest binds the reviewed files and the executed outputs.

The hypotheses v>0 on the whole axis and sufficient background smoothness are explicit and not established here for the numerical trial. Compactness, Fredholmness and a dimension for the full coupled cokernel remain open. These are identities and conditional diagonal results, not an a posteriori theorem or a profile exclusion.
