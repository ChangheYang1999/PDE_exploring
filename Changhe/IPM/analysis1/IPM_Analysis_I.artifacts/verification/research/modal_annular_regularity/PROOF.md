# Annular regularity of the exactly joined finite modal trial

Written 2026-10-21T20:16:21.912596+00:00 before the new verification code.

## Exact statement, notation and scope

Use the exact modal source data in data_exact/modal_v2.json and the definition in topic15, modal_repair/PROOF.md. The260 factor modes have degree7 clamped B-splines with simple interior knots. Let a and b be the first and last distinct knots. Their physical boundaries are exp(a) and exp(b). The stored rmin,R0 and rounded Ei,Eo are provenance, not definitions. At each outer or inner boundary recompute the correction coefficients by the exact matching formula below. At the outer boundary add the exact normalization correction z times B, where z is the finite real number defined in topic15. The regularity conclusion holds for every finite real z with this matching convention.

Let rho be this density, psi its canonical finite-mode stream function, U=(-psi_y,psi_x), c_l the defined constant, and eps=(c_l X+U) dot grad rho-rho. On the punctured plane R^2 without0, rho is C6, psi is C7, U is C6 and eps is C5. Thus every finite odd Fourier mode of eps is C5 in t=log r, including at all spline knots and the two exact radial boundaries. Every mode of eps-eps_t is C4. In particular the finite-mode C2 hypothesis of topic163 holds for eps on an open neighborhood of its closed annulus. The majorant-W premises of that theorem remain unproved here.

This is a regularity theorem for the exact normalized modal trial. It does not assert that the stored rounded joining coefficients are exactly conforming, does not replace physical derivative enclosure checks, and does not concern the original X3 formula. There is no new center, tail-norm, residual-size, inverse, existence or exclusion assertion.

## Complete argument across radial joins

The degree0 B-splines are indicators of consecutive knot intervals. Degree p is defined by the Cox recurrence, with a summand having zero denominator set to zero. At every simple interior knot each degree1 basis function is the continuous piecewise affine hat: its two nonzero pieces take the same value1 at their common knot and zero at their support endpoints. Inductively, the recurrence makes every degree p basis continuous near an interior knot when p>=2. On the adjacent open spans its derivative equals

 N'_(i,p)=p N_(i,p-1)/(k_(i+p)-k_i)-p N_(i+1,p-1)/(k_(i+p+1)-k_(i+1)).

To derive it, differentiate the two affine recurrence factors and insert the derivative identity of degree p-1. Substitution of the degree p-1 recurrences collects the coefficients of N_(i,p-2), N_(i+1,p-2), N_(i+2,p-2). Their denominators agree and the respective numerators reduce to p(t-k_i), p(k_(i+p)-t)-p(t-k_(i+1)), and -p(k_(i+p+1)-t), with the appropriate outer denominator retained. This gives the displayed identity; zero-denominator terms vanish on the neighborhood considered. Equivalently this identity can be checked directly on each polynomial span by the defining recurrence. Its right side is C^(p-2) by induction. A continuous piecewise differentiable function whose one-sided derivatives match this continuous function has that function as its derivative, by integrating on the two adjacent intervals. Repeating gives C^(p-1). Hence every degree7 spline and every finite linear combination is C6 across all simple interior knots. Repeated endpoint knots do not lie in the interior under this assertion.

At either endpoint write tau=t-a or t-b, let J_n be the one-sided spline jets, and let P_n be the jets of the uncorrected exponential sum, n=0,...,6. A correction exp(beta tau) sum_(i=0)^6 E_i tau^i has matching coefficients

 E_i=sum_(j=0)^i (-beta)^(i-j)(J_j-P_j)/((i-j)!j!).

This follows by multiplying the degree6 Taylor jet sum (J_j-P_j)tau^j/j! by exp(-beta tau). The coefficient of E_n in its nth derivative is n!, so the solution is unique. Equivalently it is the triangular solve

 E_n=(J_n-P_n-sum_(i<n) n!/(n-i)! beta^(n-i) E_i)/n!.

The inner correction uses beta=b_i and the outer beta=-b_o. All real exponential polynomials are smooth at finite tau. Matching the seven jets makes the resulting radial function C6 at each join by the same fundamental-theorem-of-calculus argument. The scalar normalization term is

 B(tau)=exp(alpha_0 tau)-exp(-b_o tau) sum_(i=0)^6 ((alpha_0+b_o)tau)^i/i!, tau>=0.

Multiplying by exp(b_o tau), its Taylor coefficients through degree6 vanish. Thus B and its first six derivatives at0 vanish exactly. Adding zB preserves all joins for every real z; an enclosure for z is not substituted for its exact definition.

Multiplication by r^3, by the fixed trigonometric factor, and by finitely many smooth angular modes preserves C6 on every annulus separated from0. The polar descriptions define smooth angular functions across both axes, so this proves rho C6 on the entire punctured plane, not just in quadrants.

## Canonical Green modes and residual regularity

Write rho=r^3 sum_(j=0)^261 H_j(t) sin((2j+1)theta), H_261=0. The finite H_j are linear combinations of the factor modes and hence C6 on R. For1<=n<=261, m=2n, the canonical moments are

 I_n(t)=integral_-infinity^t exp(-(m+4)(t-s)) H_(n-1)(s) ds,
 J_n(t)=integral_t^infinity exp(-(m-4)(s-t)) H_n(s) ds.

These integrals converge: at negative infinity H_j is bounded and the rate m+4 is positive; the finitely many inner correction terms have positive rates b_i and2,...,14. At positive infinity H_n is a sum of finite exponential polynomials with rates alpha_l<-2 or-b_o<-2. Since m>=2, each m-4-alpha_l and m-4+b_o is positive. Polynomial powers do not spoil exponential integrability. The normalization correction has the same rates. Every integral is absolutely convergent even for n=2, when m-4=0.

On a compact t interval the fundamental theorem of calculus and product rule give I'_n=-(m+4)I_n+H_(n-1) and J'_n=(m-4)J_n-H_n. They first give C1 moments; induction using H C6 gives I,J in C7. Their fixed canonical combination psi_n(t)=exp(4t)(J_n-I_n)/(2n) is C7. The finite stream sum is therefore C7 away from0, with U C6. In Cartesian coordinates eps=(c_l X+U) dot grad rho-rho is C5 because grad rho is C5 and U is C6. Fourier coefficients can be differentiated through a finite sum, or under the integral on the compact circle, so eps_N(t) is C5 and eps_N-eps'_N is C4. Classical derivatives equal weak derivatives on compact annuli, with no interface measures. This verifies the stated regularity premise of topic163 independently of the unvalidated W tables or numerical moment archive values.

## Verification plan and dependencies

New exact arithmetic will check the knot multiplicities, coefficient dimensions, exponent signs, endpoint reconstruction by two different methods, the two jet-solving formulas and all scalar-normalization vanishing jets. Method A uses exact binary64/Fraction input with the derivative B-spline endpoint recurrence; method B manually decodes hexadecimal rationals and uses exact fmpq Cox polynomials on the first and last spans. Neither imports the earlier endpoint code. Compare all seven jets of all260 modes at both endpoints and all corresponding corrections. The analytical interior continuity proof applies to all knots once their simple multiplicities are checked. No exhaustive interior jump-table computation is claimed or needed.

The shape and zero-mode algebra will be checked from the fixed finite angular identity already stated in topics99 and156, independently by signed sine scattering. The accepted topic15 definition and topic163 theorem remain hash-pinned dependencies; numerical moment membership and physical derivative models are explicitly not conclusions.
