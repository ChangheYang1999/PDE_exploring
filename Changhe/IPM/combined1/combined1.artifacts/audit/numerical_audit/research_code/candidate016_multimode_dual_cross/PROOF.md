# Candidate016: independent sixteen-mode dual and solenoidal certificates

## Exact statement

Let chi be the exact potential C1-N1-016-legqs25-quot013 with raw SHA256
 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Set c=4076476460239181/2251799813685248, delta=1-1/c,
rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), and
F=(cX+U).grad rho-rho on R2. All integrals use Lebesgue measure. Define

 H(F)=sup{|integral F phi|: phi in C_c^infinity(R2), ||grad phi||2<=1}.

The accepted complete finite sine representation of F has all160 positive
odd frequencies from1 through319. Its accepted rF norm is finite. Define

 M2=pi sum_(all n) n^-2 integral_0^infinity r^3 f_n(r)^2 dr,

where F=sum f_n(r) sin(n theta). The word all is essential.
This topic evaluates exact finite tests only at n=1,3,...,31. It does not
replace M2 by a truncated sum. Every rational coefficient, beta and integer
k of its tests is read from source/N3_full_vectors.json, whose bytes and
original source are bound in source/MANIFEST.json. Set

 psi_n=sum_i x_i r^3(1+r^2)^(-beta_i)
                   (r^2/(1+r^2))^k_i sin(n theta).

The checker requires beta_i>3/2, k_i>=-1 and 3+2k_i-n an even nonnegative
integer. Write d_n=||grad psi_n||2^2, p_n=integral F psi_n,
Z_n=A_(Delta psi_n)-grad psi_n, a_n=||Z_n||2^2 and
b_n=<A_F,Z_n>, where A_G=-e_theta sum_n r g_n cos(n theta)/n.
If each d_n and a_n is positive, then

 H(F)^2 >= sum_(n=1,3,...,31) p_n^2/d_n,
 H(F)^2 <= M2-sum_(n=1,3,...,31) b_n^2/a_n.                  (1)

A successful finite computation certifies the displayed quotients and
improvements. A numerical upper bound additionally requires a separately
accepted complete M2. No basis completeness or solver optimality is assumed.

## Admissibility and proof of the two inequalities

Each trial term is smooth at zero: r^(3+2k)sin(n theta) is a Cartesian
polynomial times an even power of r. At infinity the trial and its first
two logarithmic radial derivatives are O(r^(3-2beta)). The gradient is
square integrable. Smooth radial cutoff errors in the squared gradient
norm are O(R^(6-4beta_min)), tending to zero. The norm error is therefore
O(R^(3-2beta_min)), not the squared error exponent. Thus psi_n is in the
gradient completion of C_c^infinity and r Delta psi_n is in L2.
The absolute endpoint checks below identify its pairing with the ordinary
integral by dominated convergence.

The tangential vector field A_F belongs to L2 and has distributional
divergence F. This identity holds on annuli by angular differentiation,
and extends across the origin because its radial flux is zero and it is
locally integrable. Hence H(F)<=||A_F||2 and the functional is continuous
on the gradient completion. Distinct trial gradients are orthogonal by
sine and cosine orthogonality. Applying this continuous functional to
sum_n (p_n/d_n)psi_n proves the lower inequality in (1).

The same distribution identity for A_(Delta psi_n) shows that Z_n is
divergence free. Distinct Z_n are orthogonal: in polar components their
frequencies are distinct. The vector field A_F+sum t_n Z_n has divergence
F and squared norm M2+sum(2t_n b_n+t_n^2 a_n). Completing each square at
t_n=-b_n/a_n proves the upper inequality in (1). The formula

 Z_n=-u_n'(r)sin(n theta)e_r
       -(r u_n''(r)+u_n'(r))cos(n theta)e_theta/n

also proves a_n>0 for every nonzero decaying trial: zero norm forces u_n
to be constant, and its decay forces that constant to be zero. The exact
polynomial data must separately pass the nonzero check.

## Exact formulas used in the independent computation

Let t=r^2/(1+r^2), w=1-t and group the trials as
u_n=r sum_b w^b P_b(t), with b=beta-1>1/2 and
P_b=sum_(i:beta_i-1=b) x_i t^(k_i+1). Define

 D_b P=(1-2bt)P+2t(1-t)P'.

Then u_y=r sum_b w^b D_b P_b and u_yy=r sum_b w^b D_b^2 P_b,
where y=log r and D_b^2 means composition. Polar integration gives

 d_n/pi=(1/2)sum_(b,c) integral_0^1 w^(b+c-2)
               [(D_bP_b)(D_cP_c)+n^2 P_b P_c]dt,
 a_n/pi=(1/2)sum_(b,c) integral_0^1 w^(b+c-2)
               [(D_bP_b)(D_cP_c)+(D_b^2P_b)(D_c^2P_c)/n^2]dt.

Every ordered pair is retained. Substitute t=1-w and integrate each
monomial as 1/(exponent+1). Since b+c-2>-1 these are ordinary convergent
integrals, and the results are exact rational numbers. The first must
equal the peer's saved exact d_n/pi, without rounding or tolerance.

Reconstruct each complete f_n directly from the raw potential using the
own weak projection algorithm:

 f_n=r sum_ell w^(ell delta/2) A_(ell,n)(t).

Every contributing angular product is included. The rational functions
have only positive denominator factors1+s w. The new projection is bound
to the accepted complete Cartesian-checked F representation, component
by component. To compare different rational representations, raise or
exactly lower denominator powers to the reference powers. Lowering requires
exact polynomial divisibility with zero remainder. The resulting numerator
degree and its coefficient-by-coefficient hash must agree. This is an
exact rational-function identity, not agreement at selected sample points.

The pairing formulas are

 p_n=(pi/2)sum_(ell,b) integral_0^1
                  w^(ell delta/2+b-3) t A_(ell,n) P_b dt,
 b_n=(pi/(2n^2))sum_(ell,b) integral_0^1
                  w^(ell delta/2+b-3) t A_(ell,n) D_b^2 P_b dt.

The second sign follows directly from the polar formula for Z_n. Combine
all terms with the same exponent as complete rational functions before
integration. Extract their exact numerator zero order q at w=0 and require
ell delta/2+b-3+q>-1. The denominator is positive on[0,1]. These checks
establish absolute convergence, with no analytic continuation or omitted
sector. The own positive-pole moment checker verifies its exact partial
fraction identity and evaluates containing Arb intervals.

## Replay, directed bounds and energy assembly

Export every group integral as a containing650digit ball. Reparse the
saved JSON and add those intervals independently. Require their accumulated
absolute radius below10^-200 and final pairings with more than600 bits of
relative accuracy. Require containment of the unformatted full-precision
sum in that replay. These are checked inequalities, not assumptions based
on digit count. The source-bound computation remains incomplete if any
required check fails. Candidate pairings and quotients must lie strictly
inside the peer's containing displays; historical long endpoint strings
are not treated as containing balls.

For each n take strict nonnegative rational floors l_n<|p_n|/sqrt(d_n)
and j_n<b_n^2/a_n. Then H(F)^2>sum l_n^2 and
H(F)^2<M2-sum j_n. A lower bound for H requires no M2 evaluation. The
sum of the full-precision quotients is also compared to the peer's total
containing ball. If the separately accepted deeper tests in modes1 and3
give larger floors, one may take the larger floor separately in each of
those two modes. One must never add both same-mode floors. The same rule
holds independently for solenoidal improvements, since a single better
trial can be selected in each frequency. The checker reports both the
exact peer-vector sum and this optional improved selection distinctly.

With separately accepted G0=||F||2, G1=||grad F||2 and
P2=||(1+4r^2)^(2/5)D2F||2, define exactly

 E2(F)^2=P2^2+2^14G1^2+2^18G0^2+(20/21)2^18H(F)^2.

Monotone substitution of accepted directed component bounds and (1)
gives directed energy bounds. Upper energy assembly remains separate
until the complete M2 result and independent analytic review are read
and accepted. The independently accepted007 E2 upper may be used for
same-definition energy ordering only after a strict directed comparison.

## Dependencies and scope

The proof uses the complete-field soundness and endpoint-moment proofs,
../candidate016_dual_lower/PROOF.md and its cutoff clarification,
../candidate016_solenoidal_upper/PROOF.md and the independent T4/Opus
analytic reviews. Its code imports only own implementations and treats
peer code as text. Freeze all dependency hashes before arithmetic and
recheck them afterward. Do not copy or execute the large peer F cache.
The finite trial coefficients are proposed exact data, not proof by
import. No optimization, quadrature, finite-radius truncation or sampled
angular transform occurs. Nothing here proves basis completeness, exact
H, a correction distance, a linear inverse, nonlinear closure, or profile
existence. All numerical claims remain OPEN until their checks finish.
