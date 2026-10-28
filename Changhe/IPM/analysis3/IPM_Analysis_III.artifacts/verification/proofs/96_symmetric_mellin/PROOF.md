# Second-order real-energy comparison for the full regular Mellin family

## Operators and hypotheses

Use the regular torus, Fourier lattice, principal velocity U_pr and matrix B of topics81 and94. The radial frequency is xi and the angular index is n. The homogeneous family U_sigma is defined by

 Aplus=(sigma+i xi-n)/(sigma+i xi+n+2),
 Aminus=(sigma+i xi+n)/(sigma+i xi-n+2),
 U_sigma,1=(e^(2i theta)Aplus(D)-e^(-2i theta)Aminus(D))/(4i),
 U_sigma,2=-(e^(2i theta)Aplus(D)+2I+e^(-2i theta)Aminus(D))/4.

Assume the low-frequency denominators do not vanish and define the principal family to be zero on the zero input frequency. This includes the actual radial lines sigma=13/4 and sigma=-3/8. Only high frequencies will enter the estimates below. Finite changes in the zero-mode convention have no effect once the cutoff satisfies the displayed strict inequality.

Let g1,g2 be real bounded scalar functions with finite first Fourier moments S1(g_j). Let B and b_eta have the second Fourier moments of proof 94. Put

 a=sigma+1, b=sigma+2, K=max(|a|,1),
 Lambda>2+|b|,
 R=Lambda-2-|b|, L=Lambda-1,
 E0=a^2/(L^2-a^2)+1/(L^2-1),
 G0=||g1||_infinity+||g2||_infinity,
 G1=S1(g1)+S1(g2).

Then for u=Q_Lambda u,

 Re<sum_j g_j U_sigma,j u,u>
 <= integral bplus |u|^2+E_sigma ||u||^2,                 (1)

where the entirely explicit sufficient error is

 E_sigma=eta/2+[S2mat(B)+S2(b_eta)]/(2 Lambda^2)
                        +G0 E0+6 K G1/R^2.               (2)

Thus the regular Mellin real-energy error also has second-order cutoff decay when the fixed coefficient moments are finite. Formula (2) replaces the crude first-order vector operator norm only in the quadratic form. It is not an L2 norm improvement of U_sigma-U_pr, which remains an operator of order minus one.

As in topics81 and94, this family does not itself specify the actual full-plane canonical inverse, harmonic additions at finite boundaries, the singular angular weight, localization errors, or the jet row. Those remain separate for an actual inverse certificate.

## Symmetric part of the constant-coefficient velocity error

Put R_j=U_sigma,j-U_pr,j. Consider a shift from angular mode n to n+2, with midpoint N=n+1, z=N+i xi. In the self-adjoint part of U_sigma the scalar coefficient multiplying 1/(4i) in component1 or -1/4 in component2 is

 Fa=[Aplus(sigma+i xi,n)+conjugate(Aminus(sigma+i xi,n+2))]/2
   =(a^2+N^2+xi^2)/(a^2-z^2).                            (3)

For the principal family the corresponding coefficient is

 Fpr=[f(N-1)+f(N+1)]/2, f(v)=(i xi-v)/(i xi+v).

Exact rational subtraction gives

 Fa-f(N)=2a^2 N/[z(a^2-z^2)],
 f(N)-Fpr=-2i xi/[z(z^2-1)].                             (4)

The negative shift has the conjugate, index-shifted coefficients, with the same bounds. For input frequency |p|>=Lambda, |z|>=Lambda-1=L. The assumptions ensure L>|a| and L>1. Consequently

 |Fa-Fpr|<=2a^2/(L^2-a^2)+2/(L^2-1)=2E0.

There are two shifts, each with coefficient magnitude 1/4. Each shift is an L2 isometry. Therefore

 ||sym(R_j) Q_Lambda||<=E0, j=1,2.                        (5)

The common central term in component2 cancels, and the zero-mode convention is outside these high-frequency input/output interactions. This proves the constant-coefficient part without a pseudodifferential expansion.

## The commutator with the variable coefficients

The exact multiplier differences before the two shifts are

 Dplus=2[(sigma+1)n-i xi]/[(sigma+i xi+n+2)(i xi+n)],
 Dminus=-2[(sigma+1)n+i xi]/[(sigma+i xi-n+2)(i xi-n)].      (6)

If r=|(xi,n)|>|b|, direct differentiation of these rational functions gives the sufficient bounds

 |Dplus|,|Dminus|<=2K/(r-|b|),
 ||grad Dplus||,||grad Dminus||<=6K/(r-|b|)^2.             (7)

For completeness, the numerator has modulus at most 2Kr and differential norm at most 2K. The two denominator factors have moduli at least r-|b| and r, and differential norms at most one. The product rule bounds the derivative by

 4K/[r(r-|b|)]+2K/(r-|b|)^2<=6K/(r-|b|)^2.

Each of R_j* is a sum of two shifts by s=(0,2) or (0,-2), with a coefficient symbol equal to one quarter of a conjugate Dplus or Dminus evaluated at p+s. Let this symbol be d_s(p). The Fourier entry of [R_j*,g] from p to k has, for each such shift, the factor

 ghat(k-p-s)[d_s(k-s)-d_s(p)].                            (8)

Both input and output are restricted to |p|,|k|>=Lambda. The underlying arguments p+s and k therefore have lengths at least Lambda-2. Set q=k-p-s. If |q|<=R/2, every point on the joining segment has r-|b|>=R/2. Equations (7) and the factor 1/4 give

 |d_s(k-s)-d_s(p)|<=6K |q|/R^2.

If |q|>R/2, the endpoint bound in (7) gives at most K/R, which is at most 2K|q|/R^2. Thus the former bound holds in both cases. Sum the two shifts and apply Young's inequality to (8):

 ||Q_Lambda [R_j*,g] Q_Lambda||<=12K S1(g)/R^2.            (9)

No bound on the symbol along a segment passing through the origin is used in the large-q case. This avoids a common invalid commutator argument. All low-frequency poles are excluded by the family hypothesis and, in the displayed estimates, by the high-frequency separation.

## Assembly

There is an exact identity

 sym(M_g R_j)=M_g sym(R_j)+[R_j*,M_g]/2.                  (10)

Although the two terms on its right need not separately be self-adjoint, their sum is. Pair with u and use (5), (9):

 |Re<M_g R_j u,u>|
 <=[||g||_infinity E0+6K S1(g)/R^2]||u||^2.

Sum over j and apply the principal estimate (2) of proof 94. This proves (1)-(2). The first Fourier moments can be enclosed by the explicit three-derivative bound in proof 78, and the second moments by the four-derivative bound in proof 94. These are finite for smooth periodic regular-patch extensions of the modal coefficients; their actual numerical values are not supplied here.

## Verification and limits

The accompanying symbolic script independently checks (3)-(4), both differences in (6), and the shifted-adjoint convention. It uses exact rational symbolic algebra. The proof above supplies the full infinite-dimensional estimates. This result does not claim an actual global inverse, a certified rank, or an absence of a kernel. Its use is to reduce the conservative regular-region energy error before the remaining finite-rank and tail calculations.
