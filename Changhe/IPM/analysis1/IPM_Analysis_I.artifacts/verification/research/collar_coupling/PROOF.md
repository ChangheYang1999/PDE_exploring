# Local collar velocity and forcing estimates

Date: 2026-10-20. Independent verifier reconstruction of the lead's revision2, copied to evidence/lead_collar_v2.md. The argument is written before numerical evaluation of its constants. Numerical status, source hashes and reviews belong in evidence/verdict.json. This is a bounded local mapping theorem, not a global inverse or a closing inequality.

## Statement and conventions

Put Q={x>0,y>0}. The density h is real, even in x and odd in y. Fix I=[x1,x2], d>0, x1>2d, 5/2<b<7/2 and 0<g<2. Let I_t=[x1-t,x2+t], N=(I_(2d) union -I_(2d)) times (-2d,2d), N1=(I_d union -I_d) times (-d,d), and N0=I times (-d/2,d/2). Write H_b(S)=L2(S,|y|^(-2b)dxdy). Choose smooth even cutoffs between0 and1: chi_N=chi1(x)chi2(y), equal1 on N1, supported in N; and chi0(y), equal1 on |y|<=d0=d/4 and zero for |y|>=d/2.

On N suppose h=phi_e(y)c_e(x)+h_rem, with phi_e=y chi(y/d_e) smooth compactly supported and odd, c_e even and L2 on the x projection of N, and h_rem in H_b(N). Assume Z=||(1+r)^(-g)h||_(L2(R2 minus N1)) finite. Set h_n=chi_N h_rem, h_e=(chi2 phi_e)(chi1 c_e), h_f=(1-chi_N)h. Thus h=h_n+h_e+h_f, and h_n,h_e are compactly supported L2 densities. The far velocity on N0 is defined by the parity-symmetrized kernel below. It agrees there with the usual full-plane velocity for compact L2 data. For admissible sublinear profiles it agrees with the canonical integral; the present larger weighted class alone is not asserted to satisfy U=o(r) globally.

The velocity is U=(-psi_y,psi_x), -Delta psi=partial_x h. Write u_(i,j)=partial_y^j U_i(x,0)/j! in the Sobolev trace sense specified below, and T3U_i=U_i-sum_(j<3)y^j u_(i,j). Put

sigma_j=b-j-1/2,
c_j=2^(-b-1)sqrt(Gamma(2b+1))/j!,
e_j=sqrt(2(2d)^(2b+1)/(2b+1))/(2j!), M_j=max(c_j,e_j),
J_j=sqrt(2 d0^(2j+1-2b)/(2b-2j-1)).

The constant C=C_(3,b) in the independently proved ../edge_velocity/PROOF.md is an explicit dependency. In this note it equals

C=2^b+sqrt(2^(2b-7)7!/[(7-2b)(3!)^2])+sqrt(2^(-2b-1)/(2b+1))
  +sum_(j=0)^2 {sqrt(2^(-2b-1)(2j+1)!/[(2b-2j-1)(j!)^2])
                 +sqrt(3*2^(2b-1)(2j+1)!/(j!)^2)}.

For the near remainder the estimates are

||u^n_(i,j)||_(H^sigma_j)<=2^(sigma_j/2)M_j ||h_rem||_(H_b(N)),
||u^n_(i,j)||_2<=M_j ||h_rem||_(H_b(N)), j<3,
||R_i^n||_(H_b(R2))<=K_n ||h_rem||_(H_b(N)),
R_i^n=U_i[h_n]-sum_(j<3)chi0 y^j u^n_(i,j), K_n=C+sum_(j<3)J_j M_j.

For the far part let R_B=sqrt(x2^2+d^2/4), R0=2R_B and

J=sqrt((1+1/R0)^(2g)(pi/2)R0^(2g-4)/(4-2g)),
g0=(128/9)R_B, g_m=4(m+1)!2^(m+2)R0^(1-m) for m>=1,
A_m=(m+1)!/(2pi)*(2/d)^(m+2)*sqrt(pi R0^2)*(1+R0)^g+g_m J/(4pi).

Then every partial derivative of order m of either far velocity component is bounded on N0 by A_m Z. Its traces are smooth and ||partial_x^n u^f_(i,j)||_(Linf(I))<=A_(n+j)Z/j!. The fixed-cutoff remainder satisfies

||R_i^f||_(H_b(N0))<=K_f Z,
K_f=A3/6*sqrt(2|I|(d/2)^(7-2b)/(7-2b))+sum_(j<3)(A_j/j!)*sqrt(|I|)J_j.

For phi=chi2 phi_e and e=chi1 c_e, the edge part obeys, whenever e in H^s,

||u^e_(i,j)||_(H^s)<=||phi^(j)||_infty ||e||_(H^s)/j!, 0<=j<=3,
||T3U_i[h_e]||_(H_b(R times (-delta,delta)))
 <=||phi'''||_infty/6 * sqrt(2delta^(7-2b)/(7-2b)) ||e||_2.

The cutoff tail for j<3 is bounded by J_j||phi^(j)||_infty||e||_2/j!. No j=3 assertion on the whole y-line is made. These bounds give a total decomposition U1=chi0(u10+y^2u12)+R1, U2=chi0 y u21+R2 on N0, with u21=-partial_x u10 and all R_i controlled by the three input quantities above.

## Proof of near and edge bounds

Take the Fourier transform in x with inverse normalization1/(2pi). For a=|xi|>0 the fundamental solution of a^2-partial_y^2 is e^(-a|y|)/(2a). Therefore the partial Fourier kernels for U2,U1 are respectively

K2(t)=-(a/2)e^(-a|t|), K1(t)=(i xi/2)sgn(t)e^(-a|t|).

The point xi=0 is null for L2 Fourier integration. For smooth data supported away from y=0, the trace formula has absolute prefactor a^(j+1)/(2j!) and integrand (sgn y')^j e^(-a|y'|)hhat, or the extra sign and unimodular factor in U1. Weighted Cauchy-Schwarz gives the factor

sqrt(integral_R |y'|^(2b)e^(-2a|y'|)dy')=sqrt(2Gamma(2b+1)/(2a)^(2b+1)).

The resulting bound is c_j a^(-sigma_j)||hhat||_(L2(|y|^(-2b))). Because |y'|<=2d, dropping the exponential gives the second bound e_j a^(j+1)||hhat||. For a>=1 use the first; for a<1 use the second. Since sigma_j>0, multiplication by (1+a^2)^(sigma_j/2) costs at most2^(sigma_j/2) in either range. Plancherel proves both near trace bounds. This low-frequency step uses bounded y support and is absent in a pure global homogeneous estimate.

The face theorem bounds T3U by C||h_n||. The difference between a full Taylor polynomial and its fixed-cutoff version is sum_(j<3)(1-chi0)y^j u_j. Its H_b norm is at most J_j||u_j||_2 because the y integral outside d0 equals2d0^(2j+1-2b)/(2b-2j-1). All denominators are positive. This proves K_n.

Approximation by compact smooth densities vanishing near the axis extends the estimates to h_n. Such functions are dense by cutoff and smoothing where the weight is bounded above and below. The compact support also bounds the ordinary L2 norm by the H_b norm; U is an L2 Fourier multiplier of norm at most1. Thus the decomposition passes in L2_loc. A pointwise kernel trace differentiated j times additionally requires b>j+1: its squared weighted kernel is locally integrable precisely when integral_0^1 r^(2b-2j-3)dr converges. Higher traces when this fails are understood in the Sobolev sense, not as pointwise absolutely convergent integrals.

For h_e=phi(y)e(x), derivatives can instead be placed on the smooth phi. Both K_i have L1 norm1 and Linf norm a/2. Hence

|uhat_(i,j)|<=|ehat| min(||phi^(j)||_infty,(a/2)||phi^(j)||_1)/j!.

Multiplication in xi and Plancherel give the claimed H^s estimate. Taylor's integral remainder in y is bounded for each xi by |ehat||y|^3||phi'''||_infty/6. Integrating its square with weight proves the local remainder estimate. The cutoff tail follows from the same J_j integral. For j=3 that integral diverges at infinity since b<7/2. Parity gives u20=u11=u22=0 and incompressibility gives u21=-u10' in distributions.

## Proof of the far estimate and the strain condition

For z=x+iy away from the density support the local term -h e2/2 vanishes and

U2+iU1=(1/(2pi))integral h(W)(z-W)^(-2)dA(W).

Combining four reflected points before integration gives the kernel

G(z,W)=(z-W)^(-2)-(z-conj W)^(-2)+(z+conj W)^(-2)-(z+W)^(-2)
       =4i sum_(n odd)(n+1)z^n Im(W^(-n-2)), |z|<|W|.

This identity follows by four geometric series, with coefficient (1-(-1)^n)(W^(-n-2)-conj(W)^(-n-2)). For |W|>=R0 and z in N0, t=|z|/|W|<=1/2. The odd sum equals2t/(1-t^2)^2, giving |G|<=g0|W|^(-3). For m>=1, enlarge the differentiated odd sum to all n>=m to obtain

|partial_z^m G|<=4|W|^(-m-2)(m+1)!(1-t)^(-m-2)<=g_m|W|^(-3).

The last step uses |W|^(1-m)<=R0^(1-m). Weighted Cauchy-Schwarz over Q outside R0 gives J, because integral_(Q,r>=R0)r^(2g-6)dA=(pi/2)R0^(2g-4)/(4-2g). Also (1+r)^(2g)<=r^(2g)(1+1/R0)^(2g). The quadrant input norm is at most Z/2 by parity. Thus the far contribution to A_m is g_mJ/(4pi).

Inside |W|<R0 use the ordinary full-plane integral: support of h_f is at distance at least d/2 from N0, so the m-th derivative of the kernel is bounded by (m+1)!(2/d)^(m+2). The integral of |h_f| over this disk is at most Z(1+R0)^g sqrt(pi R0^2). This is the first contribution to A_m. The bounds justify differentiation under the integral and holomorphy. Taylor's theorem in y and the same cutoff integrals prove K_f. All full-plane and quadrant factors have been retained.

The condition g<2 cannot simply be weakened to g<=2 for this data class. With a radial cutoff for large r, h=r sin(3theta)/log r has the prescribed parity and finite weighted L2 norm for g=2, since integral dr/(r log^2r) converges. The first reflected moment at any real z=x>0 is a nonzero multiple of integral dr/(r log r), which diverges; higher terms are integrable. Thus even the symmetrized velocity may diverge.

Write sigma[h]=psi_xy[h](0), reserving c_e for the independent edge coefficient. Whenever N_sigma=(1/pi)integral_R2 |h|r^(-3)dA is finite, the differentiated parity kernel gives

sigma[h]=(4/pi)integral_Q h sin(3theta)r^(-3)dA, |sigma[h]|<=N_sigma.

This is the raw strain; the perturbation scaling functional is sigma[h]/3. Near/far collar hypotheses alone do not make N_sigma finite: h=eta(r)r sin(3theta), supported near0 disjoint from N, satisfies them but its strain integral diverges as integral dr/r. A separate finite-strain hypothesis is necessary for the coupled forcing statement.

## Coupling with a finite-regularity background

Assume rho is odd in y and C6 on a neighbourhood of the closure of N, and N_sigma finite. Set r1=rho_y(x,0), r3=rho_yyy(x,0)/6,

S1=||partial_x partial_y^5 rho||_(Linf(N0))/120,
S2=||partial_y^5 rho||_(Linf(N0))/24,
A=rho_x-y r1'-y^3r3', B=rho_y-r1-3y^2r3.

Taylor's integral theorem and parity give |A|<=S1|y|^5, |B|<=S2|y|^4. With W=U+(sigma/3)(x,y), put

q=(u10+(sigma/3)x)r1'+(u21+sigma/3)r1.

Direct substitution, without differentiation of h, yields W dot grad rho=chi0 y q+R, where

R=chi0 y^3(u10 r3'+u12 r1'+3u21 r3)
  +chi0[u10 A+y^2u12(rho_x-y r1')+y u21 B]+R1rho_x+R2rho_y
  +(sigma/3)[(1-chi0)y(x r1'+r1)+y^3(x r3'+3r3)+xA+yB].

For p=3,5 define k_p=sqrt(2(d/2)^(2p+1-2b)/(2p+1-2b)). The H_b(N0) norm of chi0 y^p f(x) is bounded by k_p||f||_(L2(I)). Consequently

||R||<=k3(||r3'||_infty||u10||+||r1'||_infty||u12||+3||r3||_infty||u21||)
 +k5[S1||u10||+(||r3'||_infty+S1(d/2)^2)||u12||+S2||u21||]
 +||rho_x||_infty||R1||+||rho_y||_infty||R2||+(|sigma|/3)C_rho,

C_rho=J1||x r1'+r1||+k3||x r3'+3r3||+k5(S1||x||+S2sqrt(|I|)).

Here coefficient norms are L2(I) and remainder norms H_b(N0). Every displayed term follows from the exact identity: in particular y^2u12(rho_x-y r1')=y^5u12r3'+y^2u12 A. Thus no hidden derivative or cutoff contribution is omitted.

Let s=b-3/2 in (1,2). Extend r1 to a compactly supported C5 function rtilde, using the given neighbourhood and a smooth cutoff. For the near part, q_n=rtilde'u10^n-rtilde(u10^n)' satisfies

||q_n||_(H^s)<=[mu_s(rtilde')+mu_s(rtilde)]2^((b-1/2)/2)M0||h_rem||_(H_b(N)).

Here mu_s(f) is the bounded multiplication norm on H^s. It is finite for these coefficients: a C2 bounded multiplier is bounded on L2 and H2 by the product rule, hence on intermediate H^s by interpolation. The input trace has order s+1, so differentiation costs exactly one order. For the edge part,

||q_e||_(H^s)<=[mu_s(rtilde')||phi||_infty+mu_s(rtilde)||phi'||_infty]||chi1 c_e||_(H^s).

This requires chi1 c_e in H^s. It does not follow from L2 edge data. Indeed for phi(y)=y near0, the U2 normal-trace multiplier tends to -1 as |xi| tends to infinity; the correction decays exponentially because phi'-1 vanishes near0 and is bounded elsewhere. Thus no positive high-frequency regularity is gained from that trace. The far part is C4, from the product rule with r1 in C5 and the far bounds A_m; the strain part is (sigma/3)(x r1'+r1). These conclusions establish the claimed local forcing decomposition.

No assertion about the corner, source-to-face transition, conic summation, y-face local term, derivative mapping, Fredholm index or nonlinear contraction follows from this local theorem. Large derivative majorant upper bounds likewise imply no lower bound for the actual derivative norm.
