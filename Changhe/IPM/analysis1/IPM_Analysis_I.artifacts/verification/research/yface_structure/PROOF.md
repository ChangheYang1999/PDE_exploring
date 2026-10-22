# The y-face local term, edge smoothing and the meaning of traces

2026-10-20. Independent statement and proof written before arithmetic verification. This note audits structural portions of V12. The full N=6 near/far constants and the complete coupling remainder inequality are separate obligations. The pinned lead snapshot is revision2, which already withdraws the classical-trace inference and inserts the product cutoff. Our counterexample below confirms and strengthens that withdrawal.

## Operator identities and normalization

For real h in L2(R2), let U=(-psi_y,psi_x), -Delta psi=h_x, using the canonical Fourier multipliers. With zeta=(xi,eta),

U1hat=xi eta |zeta|^(-2) hhat,
U2hat=-xi^2 |zeta|^(-2) hhat.

Values at the single frequency zero are irrelevant in L2. Put (S h)(x,y)=h(y,x). The first symbol is symmetric and xi^2+eta^2=|zeta|^2, hence

U1=S U1 S, U2+I=-S U2 S.

Thus the nonlocal part U2tilde=U2+h has the exchanged x-face kernel, but the full U2 retains a local subtraction -h. For even-x odd-y h, U1 is odd in x and U2 is even in x. All parity identities hold in L2 and in distributions. Incompressibility gives (l+1)v1,l+1+partial_y v2,l=0 whenever these coefficient maps are defined. We reserve sigma=psi_xy(0) for the raw canonical strain. The accepted center-normalization argument in ../local_geometry/PROOF.md gives c_l[rho]=(1+sigma[rho])/3. Canonical linearity therefore gives D c_l[rho]h=sigma[h]/3. Differentiating F(rho)=(c_l[rho]X+U[rho]) dot grad rho-rho yields the coupling (U[h]+(sigma[h]/3)X) dot grad rho. This justifies the scaling coefficient for an exactly center-normalized background and center-preserving corrections. If the background scaling has an independent nonzero mismatch delta, the additional delta G and delta X dot grad h terms of the local-geometry identity must be restored. U is divergence free; the field U[h]+(sigma[h]/3)X has divergence2sigma[h]/3, and is not asserted to be divergence free.

## Separated edge data

Let phi be real, even, smooth and compactly supported on R, and let e belong to H^s(R), with s any real number. Begin with smooth e and extend by the multiplier estimates below. Put h_e(x,y)=phi(x)e(y) and v_i,l=(partial_x^l U_i[h_e])(0,y)/l!. Partial Fourier transformation in y, with a=|eta|>0, gives

G_a(t)=exp(-a|t|)/(2a),
K0(t)=(a/2)exp(-a|t|),
K1(t)=(i eta/2)sgn(t)exp(-a|t|).

Indeed G_a solves (a^2-partial_x^2)G_a=delta, psi=G_a'*h_e, U1=-i eta psi=K1*h_e, and U2=G_a''*h_e=K0*h_e-h_e. Transfer x derivatives to phi to obtain

m2,l(eta)=integral K0(t)[phi^(l)(t)-phi^(l)(0)]dt/l!,
m1,l(eta)=-(i eta/(2l!)) integral sgn(t)exp(-a|t|)phi^(l)(t)dt.

The first expression is for the FULL U2. Its even-l multipliers are potentially nonzero; the odd-l ones vanish. For U1 only odd l can be nonzero. These are H^s coefficient maps, not an assertion of pointwise y derivatives of arbitrary e.

For even l, Taylor's integral remainder and phi^(l+1)(0)=0 give

|phi^(l)(t)-phi^(l)(0)| <= (t^2/2)||phi^(l+2)||_infty.

The exact Laplace moments are integral K0=1 and integral K0(t)t^2/2 dt=a^(-2). For odd l, phi^(l)(0)=0, so |phi^(l)(t)|<=|t|||phi^(l+1)||_infty and integral |K1(t)||t|dt=a^(-1). Consequently

|m2,l| <= min(||phi^(l)-phi^(l)(0)||_infty, a^(-2)||phi^(l+2)||_infty)/l!,
|m1,l| <= min(||phi^(l)||_infty, a^(-1)||phi^(l+1)||_infty)/l!.

For a<=1, (1+a^2)<=2; for a>=1, (1+a^2)<=2a^2. Multiplication by (1+a^2) for m2,l and by sqrt(1+a^2) for m1,l proves the respective H^s to H^(s+2) and H^s to H^(s+1) bounds, with constants

C2,l=2 max(||phi^(l)-phi^(l)(0)||_infty,||phi^(l+2)||_infty)/l!,
C1,l=sqrt(2) max(||phi^(l)||_infty,||phi^(l+1)||_infty)/l!.

All these inequalities are uniform away from a=0, so the null frequency does not affect Sobolev norms. The low-frequency estimate is essential; the high-frequency decay by itself is not a full inhomogeneous Sobolev bound.

If phi=x^p for |x|<d_e, p=2 or4, then phi^(p)-phi^(p)(0) and phi^(p+1) vanish there. The corresponding m2,p and m1,p+1 are at most their bounded integrand supremum times exp(-a d_e)/l!. This proves arbitrary finite smoothing for these two coefficient maps. In particular the -e term in v2,2 for p=2 cancels with the leading part of U2tilde; retaining it alone would give the wrong order-zero conclusion.

## Edge coupling coefficients and local compactness

Let a background rho be even in x, vanish on x=0 and belong to W^(7,infty) on a neighborhood of a compact y interval J. Define p2=rho_xx(0,y)/2 and p4=rho_xxxx(0,y)/24. For a smooth edge perturbation, direct multiplication of the Taylor expansions of rho_x and rho_y gives the coefficients

q2=2p2(v1,1+sigma/3)+p2'(v2,0+sigma y/3),
q4=4p4(v1,1+sigma/3)+2p2 v1,3+p4'(v2,0+sigma y/3)+p2'v2,2.

These are algebraic coefficient identities. This section asserts the edge contribution only, not a bound for the full remainder. After a compact y cutoff, p2 and p4 have enough bounded derivatives for multiplication on H1. One may prove this directly by the product rule for functions with a bounded weak first derivative. For this physical parity corollary take the localized L2 edge inputs e2,e4 to be odd and compactly supported; the multiplier estimates themselves require neither condition and impose no additional low-frequency constraint. The products p2 v1,1, p4 v1,1 and p2 v1,3 use the H1 velocity bounds. The products p2' v2,0, p4' v2,0 and p2' v2,2 use the H2 velocity bounds, followed by inclusion in H1. Each background coefficient is in W^(1,infty). The edge multipliers just proved therefore map these L2 edge data into H1(J) for both q2 and q4. The scalar strain term is separate; if its functional is bounded on the chosen input space, its range is finite-dimensional.

The inclusion H1(J) into L2(J) is compact. An elementary proof partitions J into subintervals of length at most delta and replaces a function by its average on each subinterval. The fundamental theorem of calculus and Cauchy-Schwarz bound the L2 error by delta times the L2 derivative norm. On a bounded H1 set this error is uniform, while the vectors of finitely many averages form a bounded finite-dimensional set. Finite-dimensional compactness and then delta tending to zero prove precompactness. Hence the fixed bounded-collar edge maps above are compact from L2 input into L2 output. The near and far parts are not claimed compact here. This makes no statement about unbounded collars, a global direct sum, the transport domain, or the whole IPM coupling operator.

For the local decomposition h=phi2 e2+phi4 e4+h_rem given only on a near region N, the actual compact edge input is chi_N times these terms. If chi_N=chi_x(x)chi_y(y), the multiplier lemma must be applied to phi=chi_x phi_p and e=chi_y e_p. Derivative constants involve this product cutoff. The pure monomial property survives on the inner collar when both cutoffs equal1 there. Omitting these cutoff derivatives is not justified by a decomposition known only on N.

## Weighted L2 does not supply classical density jets

For every a>0, a compactly supported even-x odd-y density can lie in L2(|x|^(-2a)dxdy) and have no continuous representative across x=0, even though it is a weighted-norm limit of smooth functions vanishing near x=0. Thus revision1's inference of classical zero jets from that approximation is false without additional regularity. Revision2 already withdraws that inference; the present counterexample strengthens the withdrawal to failure of continuity itself.

Choose a smooth even bump eta supported in (-1,1), 0<=eta<=1 and eta(0)=1. Choose a smooth odd psi(y) supported in two compact intervals away from y=0, with psi(y_*)=1 at some positive y_*. Set b_j=2^(-j), epsilon_j=b_j^(2a+2)/16, for j>=1, and

h(x,y)=psi(y) sum_(j>=1)[eta((x-b_j)/epsilon_j)+eta((x+b_j)/epsilon_j)],

assigning h(0,y)=0. Since epsilon_j<b_j/8, all x supports are disjoint, and every nonzero term has |x|>=b_j/2. Its weighted squared norm is at most

4*2^(2a)||psi||_2^2 sum_j epsilon_j b_j^(-2a)
 = (2^(2a)/4)||psi||_2^2 sum_j b_j^2 < infinity.

The finite partial sums are smooth and vanish near x=0; the same tail bound proves convergence in the weighted norm. But h(b_j,y_*)=1 and h is zero in the gaps between successive supports. A continuous representative cannot repair this discrepancy on null sets: each bump and gap has nonempty open neighborhoods with these separated values. Hence continuity fails at (0,y_*). The far weight and absolute strain integral are finite since the density is bounded, compactly supported and stays away from the origin.

Correct interpretation: coefficients of the weighted decomposition can be defined by its unique asymptotic polynomial class and the velocity coefficient maps by their Sobolev limits. If a polynomial sum_(l<6)x^l e_l(y) also belongs locally to L2(|x|^(-2a)) with 5.5<a<6.5, then each coefficient is zero: pair against smooth y tests to obtain a scalar polynomial, whose smallest nonzero degree l<=5 makes integral_0 x^(2l-2a)dx diverge. The coefficients are thus unique in this decomposition sense. Classical density traces, and their derivatives, require an added regularity hypothesis.

## Scope

This proves the swap, edge multiplier smoothing, local edge compactness and the trace counterexample. It does not certify the lead's numerical N=6 near/far constants, the complete coupling remainder estimate, a global Fredholm realization, source transition, inverse, existence or exclusion. The trace issue is a scope repair and is not by itself a counterexample to the near/far L2 estimates.
