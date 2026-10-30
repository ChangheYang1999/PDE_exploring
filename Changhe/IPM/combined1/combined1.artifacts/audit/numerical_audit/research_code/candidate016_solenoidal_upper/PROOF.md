# Candidate016: finite divergence-free improvements to the full Hardy upper bound

## Statement and exact inputs

Let rho be the real S1 reference C1-N1-016-legqs25-quot013, with raw
SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Use the canonical IPM velocity and its complete residual
F=(cX+U[rho]).grad rho-rho, c=4076476460239181/2251799813685248.
All norms and integrals below are with Lebesgue measure on R2. Define

 H(F)=sup {|integral F phi|: phi in C_c^infinity(R2), ||grad phi||2<=1}.

Write the complete residual as sum of its 160 positive odd sine modes,
F=sum_n f_n(r) sin(n theta). Its accepted complete rF norm is finite.
Let

 M2=pi sum_n n^-2 integral_0^infinity r^3 f_n(r)^2 dr.

The sum is over every nonzero mode, including modes not used below.
Let psi_1 and psi_3 be precisely the two exact rational tests frozen
and independently reconstructed in ../candidate016_dual_lower, with
all coefficients retained in its source/N3_exact_vectors.json. Define
A_F=-e_theta r sum_n f_n cos(n theta)/n and

 Z_n=A_(Delta psi_n)-grad psi_n,
 a_n=||Z_n||2^2, b_n=<A_F,Z_n>.

Then a_1,a_3>0 and

 H(F)^2 <= M2-b_1^2/a_1-b_3^2/a_3.                       (1)

The checker first evaluates a_n and b_n independently from the complete
exact source. A numerical upper value from (1) is accepted only after
the complete M2 upper certificate has passed a separate check. The
initial cross-term result alone is not a bound on H. The existing dual
lower certificate remains independent of (1). No finite-basis
completeness or solver optimality assumption is used.

## Domain, identity and orthogonality

The divergence of A_F equals F: integrate in theta on annuli, where
the tangential field has zero radial flux. Finite ||rF||2 implies
A_F in L2. Passing to the plane against compact smooth tests proves
the distribution identity. Cauchy-Schwarz proves H<=||A_F||2.

Each trial term is x r^3(1+r^2)^(-beta) t^k sin(n theta), where
x and beta are exact rationals, t=r^2/(1+r^2), beta>3/2, k>=-1,
and 3+2k-n is an even nonnegative integer. It is smooth at the origin
because r^(3+2k)sin(n theta) is a polynomial in the Cartesian
coordinates. At infinity its size and its first two logarithmic
radial derivatives are O(r^(3-2beta)). Its gradient is square
integrable, and the gradient norm of the error from a smooth radial
cutoff at R is O(R^(3-2beta_min)), tending to zero. Thus psi_n is
in the gradient completion of C_c^infinity. Also r Delta psi_n is
in L2. These facts hold for the finite exact sum without a bound on
its coefficient sizes. Its source label and nonzero value are checked.

The same construction gives div A_(Delta psi_n)=Delta psi_n, hence
Z_n is divergence free. Therefore A_F+t_1 Z_1+t_3 Z_3 is an L2
vector field with divergence F for every pair of real t_i. Its
squared norm bounds H(F)^2. Radial and angular components of Z_1
and Z_3 have distinct sine and cosine frequencies, so their cross
inner product vanishes. Expanding this squared norm and completing
the two squares proves (1) at t_i=-b_i/a_i.

## Positive exact formula for a_n and signed formula for b_n

Put psi_n=u(r)sin(n theta), y=log r and v(y)=u(exp y). Direct polar
differentiation gives

 Z_n=-u'(r)sin(n theta)e_r
       -(r u''(r)+u'(r))cos(n theta)e_theta/n.

Consequently

 a_n=pi integral_R [v'(y)^2+v''(y)^2/n^2]dy,              (2)
 b_n=(pi/n^2) integral_0^infinity
                r f_n(r)[r^2u''(r)+r u'(r)]dr.          (3)

This derivation checks the sign without subtracting pairings. Formula
(2) is strictly positive for a nonzero decaying trial: zero would
force v' identically zero and v constant; its decay forces v=0.
Its nonzero polynomial data is also checked algebraically.

Write w=1-t and group b=beta-1>1/2:

 u(r)=r sum_b w^b P_b(t), P_b=sum_k x_(beta,k)t^(k+1),
 D_b P=(1-2bt)P+2t(1-t)P'.

Logarithmic differentiation gives u_y=r sum_b w^b D_bP_b and
u_yy=r sum_b w^b D_b(D_bP_b). The notation D_b^2 below means
operator composition. Since dy=dt/(2tw), (2) becomes

 a_n/pi=(1/2) sum_(b,c) integral_0^1 w^(b+c-2)
             [(D_bP_b)(D_cP_c)+(D_b^2P_b)(D_c^2P_c)/n^2]dt. (4)

Every ordered pair is included. Since b+c-2>-1, integrating the
finite polynomial after t=1-w gives exact rational values using
integral_0^1 w^q dw=1/(q+1). Individual coefficients may have either
sign; the exact completed sum must be strictly positive.

The independent Cartesian projection writes the complete mode as

 f_n=r sum_ell w^(ell delta/2) A_(ell,n)(t),
 delta=1824676646553933/4076476460239181.

Here A are exact rational functions, with denominators composed of
positive factors 1+s w. This includes the multiscale reference and
does not assume that A are polynomials. Substitution into (3) gives

 b_n=(pi/(2n^2)) sum_(ell,b) integral_0^1
              w^(ell delta/2+b-3) t A_(ell,n)(t) D_b^2P_b(t)dt. (5)

Group equal exponents and combine whole rational functions before
integration. Extract the exact numerator vanishing order q at w=0.
Require ell delta/2+b-3+q>-1 for each nonzero completed group.
Its denominator is positive on [0,1], and its numerator is polynomial
there. These checks prove absolute convergence and justify all finite
regrouping and integrations. No divergent piece is assigned an
analytic continuation. The own accepted positive-pole moment module
checks its exact partial fraction reconstruction and encloses each
ordinary integral in Arb balls. Formula (5) retains its sign.

## Directed bounds and numerical acceptance

Record exact a_n/pi, a ball for b_n, and a containing ball for
c_n=b_n^2/a_n. If a b_n ball crosses zero, use zero as its conservative
squared lower value. A strict rational lower floor l_n for c_n, with
l_n>=0, can be subtracted from any accepted full M2 upper U:

 H(F)^2 <= U-l_1-l_3.

Require the right side positive before taking its square root. A
containing interval for M2-c_1-c_3 gives a range for this particular
improved upper-bound expression, not a two-sided range for H(F).
Only a separately accepted dual lower bound gives the latter.

As independent normalization checks, the checker reconstructs the
old exact gradient energies and raw vector labels, reprojects the
complete residual and compares its hashes with N4-355 and N4-396,
and compares its energy records with N4-396. It validates D twice
against direct differentiation on manufactured rational tests of
modes 1 and 3. Source identities are checked before and after.
Large coefficients remain in exact JSON. Peer scripts are never run.

## Dependencies, reviews and limitations

The analytic idea and formulas are T4-469, whose full proof has been
read and frozen. The domain also uses the independently reviewed
T4-466 dual argument and the cutoff clarification in
../candidate016_dual_lower/CUTOFF_CLARIFICATION_v01.md. Their exact
source hashes and existing Opus reviews are recorded separately.
Consult the existing theory lanes configured for Opus5.5. Their
provider response identity is not observable locally; no substitute
model or remote client is used. Before the final upper acceptance,
read any returned independent analytic review and resolve material
objections. The finite cross-integral computation is useful even
while that review is pending.

The accepted complete-field differentiation and positive-pole moment
soundness are explicit dependencies. This proof gives neither a
stationary linear inverse nor an existence theorem. It does not
claim exact H from two tests, completeness of a beta basis, a sharp
Hardy constant for the reference, correction-distance ordering or
any conclusion for other candidates. The optional same-definition
E2 assembly must use its independently accepted G0,G1,P2 components.
