# Independent Cartesian-jet audit of point witnesses

## Exact statement

For each exact canonical potential chi and each specified nonzero rational point X, the code encloses F(X), |cX+U(X)| and |grad rho(X)| using an independent Cartesian Taylor expansion, where rho=-chi_xxy-chi_yyy and U=(-chi_xyy,chi_xxy). It then tests

|F(X)| - |cX+U(X)|/240 - (3/100000)(1+|grad rho(X)|) - 1/8000000 > 0.

This note proves the evaluator identity and arithmetic interpretation. The implication for existence balls depends on T4's separate point-witness theorem and its hypotheses; the numerical check alone does not prove that theorem.

## Cartesian Taylor formula

Write H_m(x,y)=Re((x+i y)^(2m)). Each canonical term is

a[j,m,k] H_m(x,y) s^(k-m)(1+s)^(p_j-k), s=x²+y².

All exponents k-m are nonnegative integers, while p_j is rational. This expression equals the original polar term exactly, since H_m=r^(2m)cos(2m theta). Fix a nonzero point (x0,y0), let s0=x0²+y0², and put S=2x0 h+2y0 v+h²+v². The radial factor has Taylor coefficient at S^n

C_n = sum_(i=0)^n binom(k-m,i) s0^(k-m-i)
                         binom(p_j-k,n-i)(1+s0)^(p_j-k-(n-i)).

Its Taylor polynomial through total Cartesian degree four is sum_(n=0)^4 C_n S^n, discarding monomials above degree four. The harmonic factor has coefficient

[h^a v^b] H_m(x0+h,y0+v)
= binom(2m,a+b) binom(a+b,a) Re((x0+i y0)^(2m-a-b) i^b),

with coefficient zero when a+b>2m. Multiplying the two finite jets and summing the exact rational canonical coefficients yields all derivatives of chi through total order four; the derivative at order (a,b) is a!b! times its Taylor coefficient. Terms discarded above degree four cannot contribute to any retained derivative.

The powers with noninteger exponent have positive real bases s0 and 1+s0. Their outward Arb evaluation, together with ball additions and multiplications, encloses the exact coefficients. This uses Cartesian polynomial jets, independently of the radial-Fourier derivative recurrence used by the T4 diagnostic. The two implementations should have overlapping point enclosures when both target the same canonical coefficients.

## Point quantities

The exact differential identities above give rho, U, grad rho and F=(cX+U).grad rho-rho. Euclidean norms are evaluated by sums of squares and square roots in ball arithmetic. A strictly positive lower endpoint for the displayed difference certifies the point inequality. All copied T4 data and canonical input files are hashed; comparisons are made on exact rational coordinates. No finite-point test is described as a global upper bound.

## Re-evaluation for newly specified balls

For any s>0 and ||h||_(H^(2+s))<=R, the S1 correction equation at a point implies

|F| <= C1(s)R |V| + C0(s)R(1+|D rho|) + C0(s)C1(s)R^2,
C0(s)=[4pi(1+s)]^(-1/2), C1(s)=[8pi s(1+s)]^(-1/2).

The constants and this implication have been independently reviewed in T1 R1-001. They depend only on the displayed Sobolev ball, not on the scalar decay rate of a particular inverse theorem. For the rebalanced framework take s=2^-16 and R=3*2^-15, because the scalar Ns norm dominates H^(2+s). For the illustrative graded box take s=1/50000 and R=sqrt(r_P^2+2r_a^2+r_b^2), because the Bessel Fourier identity and omega>=1 give that domination. This latter reduction enlarges the graded box and is valid regardless of its H component.

Substitution of the independently computed Cartesian point fields into the displayed right side yields an interval for the necessary upper bound. A strictly positive lower bound for |F| minus that expression excludes an exact correction in the specified ball. Failure to obtain a positive gap gives no existence conclusion. These are new scalar evaluations, labelled N4-ORIGIN until another lane reproduces them; the underlying field evaluations are already independently confirmed.

## Independent postprocessing of the symmetry-based corollary

T4's new symmetry lemma claims that every positive scalar-gap ball with base rate at most3/10 satisfies, at the selected axis points,

|F| < (87/10000)|V|+(53/1000000)(1+|D rho|)+1/2000000.

Its proof is copied to data/T4_symmetry_PROOF.md and remains subject to independent theory review. The numerical audit here does not assume it is already a team theorem. The displayed right side is linear in the three supplied nonnegative point values. Parsing their decimal interval strings as exact rational endpoints and evaluating the linear expression gives an independent rational check of T4's new gap numbers. Positivity of these gaps is unconditional as an arithmetic statement about the given reference fields; its interpretation as a correction-ball exclusion is conditional on the cited symmetry lemma.

## Application to the T2-R2 parameter box

The same necessary point inequality applies at s=1/8192 and r=43/50000, the sharp box registered as FW-T-TB-sharp-v1. A nonpositive computed gap only means that this particular point test is inconclusive. Separately, the established weighted projection comparison N_s(F)>=(1-34s)E_2(F), valid at this s, and nonnegativity of the H component give

N_s(F)>=(1-34s)[P2(F)^2+2^14 G1(F)^2+2^18 G0(F)^2]^(1/2).

Thus lower enclosures for these three raw-F components suffice for a necessary-threshold comparison without knowing the H component. The comparison is to the fixed sharp-box threshold5289/50000000 and does not assert a lower bound for the actual inverse correction. The projection estimate and all domain hypotheses are those in the independently reviewed T2-R2 and Analysis II framework.

## Finite scans and required correction size

At each nonzero rational point the audited inequality has the form f<=A R+B R^2, with f=|F|, A=C1|V|+C0(1+|grad rho|)>0 and B=C0 C1>0. Its positive root is R_nec=2f/(A+sqrt(A^2+4 B f)). Every exact correction in H^(2+s) must have norm at least R_nec. A maximum over finitely many points is another valid lower bound, without any claim that the spatial maximum has been found. On axis points (0,y), |y|>=1/2, the independently audited S1 symmetry constant C1=[16 pi s(1+s)]^(-1/2) may be used. Elsewhere use C1=[8 pi s(1+s)]^(-1/2).

The scan stores the exact rational point set, enclosed fields, the chosen symmetry rule, and root enclosures. Each maximizing point is independently recomputed using Cartesian jets. The root evaluation is monotone in f and antitone in A,B, but ordinary outward interval evaluation also encloses it and is used here. No negative or inconclusive gap proves the existence of a correction.

## Transfer to stationary-inverse parameter boxes

Suppose the point inequality excludes a box with parameters (s0,R0), with a certified positive gap g. A second box (s,R) is excluded with gap at least g whenever

    R²/(1+s) <= R0²/(1+s0),
    R²/[s(1+s)] <= R0²/[s0(1+s0)].

Indeed these rational inequalities imply R C0(s)<=R0 C0(s0) and R C1(s)<=R0 C1(s0). All factors are nonnegative. They also imply R² C0(s)C1(s)<=R0² C0(s0)C1(s0), so every term of the new necessary upper bound is no larger than the old one. This argument transfers the existing confirmed b6 gap at (1/8192,43/50000) to any parameter pair passing both checks. It uses the same fixed exponent and point, and does not require a new field evaluation or an inverse estimate.
