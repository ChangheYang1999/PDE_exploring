# A common analytic axis domain for the formal endpoint hierarchy

Prepared 2026-10-22T08:57:50.422178+00:00 before controls. The mathematical conclusion is conditional on the exact all-order residue and base compatibility identities proved in P321, P303 and P306. It strengthens the domain statement for those coefficients; it supplies no convergence in the transverse variable and no B2 solution on an open subset of the plane.

## Statement and notation
Fix real C,k with Ck nonzero, beta=2, and use the inward coordinate s. Put

B(s)=s+ks^2-(Ck/260)s^13, H=-k^7/231,
R=min(1,1/(4|k|),(65/|Ck|)^(1/12)), D={s in C: |s|<R}.

Let t=s^10 exp(tau) and Y=s^6 exp(upsilon), with tau(0)=upsilon(0)=0, solve t'/t=(8+2B')/B and Y'/Y=(5+B')/B. Let J(0)=0 and J'=t/(B Y). Initialize theta_1=Ct/2, omega_0=Y(H-CJ), v_0=B, and

v_(j+1)=-(omega_j+v_j''/(2j+1))/(2j+2).

Use the exact Cartesian transport recurrences, with derivatives in s,

B theta_l'-(8l+2lB')theta_l = sum_(a=1)^(l-1) [2(l-a)v_a' theta_(l-a)/(2a+1)-v_a theta_(l-a)'],
B omega_j'-[((2j+1)(4+B')+1)]omega_j = -2(j+1)theta_(j+1) + sum_(a=1)^j [(2(j-a)+1)v_a' omega_(j-a)/(2a+1)-v_a omega_(j-a)'].

There exists a unique formal coefficient sequence fixed by the successive compatibility choices of P321. Every coefficient theta_l, omega_j and v_j in this sequence extends holomorphically to the SAME disk D, is real on its real diameter, and satisfies its exact coefficient identities on D. Uniqueness is within this specified initial axis family, with the normalization of t,Y,J and the compatibility sequence of P321. There is no bound here on the coefficients as l,j grow. No convergence of the resulting x series is asserted.

## A uniform disk for the fixed factors
Write B=s b, where b=1+ks-(Ck/260)s^12. For |s|<R,

|b-1| <= |k||s|+|Ck||s|^12/260 < 1/2.

Consequently b has no zero on D and its reciprocal is holomorphic there. Direct algebra gives

tau'=(-6k-(4Ck/65)s^11)/b,
upsilon'=(-4k-(7Ck/260)s^11)/b.

These holomorphic functions have unique primitives with value zero at the origin because D is a disk. Thus exp(tau) and exp(upsilon) are holomorphic nonzero functions throughout D. The only zeros of t and Y on D are the stated orders10 and6 at s=0. The quotient t/(B Y)=s^3 exp(tau-upsilon)/b is holomorphic on D and has the unique primitive J with J(0)=0. Hence theta_1,omega_0,v_0,v_1 are holomorphic on D and real on its real diameter.

## A scalar continuation lemma
Let z=s^m u on D, with m a nonnegative integer and u holomorphic and nowhere zero. Let B=s b as above, and suppose z solves the homogeneous equation B z'-h z=0 with h holomorphic on D. Then B f'-h f=g, for holomorphic g on D, has a holomorphic solution if and only if the meromorphic function g/(B z) has zero residue at0. Every such solution is

f=z(P+c),

where P is a meromorphic primitive of g/(B z) with its constant coefficient set to zero and c is a scalar.

Indeed g/(B z) is holomorphic on D minus0 and has a pole at0 of order at most m+1. Split its Laurent expansion into its finite principal part and a function holomorphic on D. A single-valued meromorphic primitive exists precisely when the coefficient of s^-1 vanishes. Integrate every other principal-part monomial, and take a holomorphic primitive of the holomorphic remainder on D. The resulting P has a pole of order at most m. Multiplication by z removes that pole, so f is holomorphic on ALL of D. Conversely the derivative (f/z)' cannot contain an s^-1 coefficient. If two holomorphic solutions exist, their difference divided by z has derivative zero on the connected punctured disk, hence is a constant. Reality is preserved when all inputs and c are real. The word primitive here is a single-valued function on D minus0, not a branch of a logarithm.

## Induction on the hierarchy
The thermal homogeneous factor at index l is t^l, with zero order10l. The vorticity factor at index j is t^j Y, with zero order10j+6: their logarithmic derivatives match the displayed scalar equations. Every forcing term in either recurrence is a finite sum of products and derivatives of already constructed holomorphic coefficients. It is therefore holomorphic on D. Differentiation and the Poisson update preserve holomorphy on D without any reduction of domain; bounds on derivatives on the boundary are not being asserted.

For the base construction at l=2,j=1, P303 and P306 verify the vanishing residues for the chosen curvature and H. The scalar lemma yields theta_2 and omega_1 holomorphic on D, initially with zero homogeneous constants. Suppose the hierarchy through theta_n,omega_(n-1),v_n has been obtained on D, with the new constants at that stage still free. P321 proves that the next two residues depend affinely on E,F with matrix

[12Ck/[5(2n+1)], 0; -k^8(2n+5)/[385(2n+1)], -9Ck/(10n)], n>=2.

Its determinant is -54C^2 k^2/[25n(2n+1)], nonzero. There is therefore a unique real pair E,F making both residues vanish. Before thermal compatibility, the convention in P321 subtracts the residue monomial before taking a meromorphic primitive in the definition of the second residue; this is legitimate on the same D. The changes to the existing coefficients are E t^n and -2nE t^(n-1)YJ+F t^(n-1)Y. They are holomorphic on D. Updating v_n by Poisson also preserves that domain. At the solved pair the next thermal forcing has a genuine meromorphic primitive, hence theta_(n+1) is holomorphic on D. The next vorticity forcing then has zero residue and yields omega_n on D. The new Poisson coefficient v_(n+1) is holomorphic on D. This closes the induction without shrinking D.

Every fixed coefficient is final after its compatibility step because later steps change only higher indices. The scalar lemma gives only the stated homogeneous freedoms, and the nonsingular residue matrix fixes them uniquely over the complex numbers as well. Since the data are real, the unique solution is real. The t,Y,J normalizations agree with P321. Zero-constant primitives are a convenient origin for the two free coordinates: replacing them by another analytic particular pair translates the affine residue offsets and the coordinates E,F, but leaves the final compatible coefficients unchanged. Indeed replacing an initial pair by the variation associated with a vector c changes r to r+M c, so the solving coordinate changes from -M^(-1)r to -M^(-1)r-c. Thus the compatible formal sequence is unique in the specified family, on the common disk D. The identities hold as holomorphic identities throughout D because they hold by construction, not merely to a finite Taylor order.

## Scope and non-implication
The result is about formal power series in x with coefficients in the algebra of holomorphic functions on D. This algebra imposes no uniform bound as the coefficient index grows. For example sum_(n>=0) n! x^(2n), whose coefficients are constant holomorphic functions on every D, diverges at every nonzero x: the ratio of successive term magnitudes is (n+1)|x|^2 and the terms fail to tend to zero. This is an illustration of the missing inference, not a solution of the coefficient PDE. Proving convergence of the actual compatible series still requires estimates for its growth in n, possibly on a smaller s disk. The full-plane inverse, attachment to the moving center, sublinear velocity, far-field conditions and global B2 existence remain OPEN. No early endpoint follows.

## Dependencies and restrictions
P321 supplies the generic residue matrix and stable compatibility induction, with its explicit base dependencies P303/P306. This proof supplies the uniform analytic continuation domain by an elementary scalar lemma; it does not silently assume a bound from finite jets. No JavaScript/TypeScript, servers/listeners, RLScience cluster or Lean/Lake builds. Writes only in verification.
