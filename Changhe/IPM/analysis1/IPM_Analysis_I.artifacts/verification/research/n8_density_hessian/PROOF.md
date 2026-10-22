# An independent source-disc density Hessian bound

Status: analytic identities proved here; actual interval computation pending. This is a density-only result. It does not certify the velocity derivatives or the full local source estimate.

## Statement, representation and dependencies

The exact normalized trial density is represented on each logarithmic spline span by

 rho(r,theta)=r^3 sum_(j=0)^260 H_j(t) sin(f_j theta), t=log r, f_j=2j+1.

Each H_j is a polynomial of degree at most seven on the span. Its coefficients, enclosed as exact dyadic balls in the canonical archive of topic31, refer to the stated exact span center. The archive is tied to the exact binary64 trial by the existing partition and knot audit. Those audits are explicit dependencies. No Green anchor is needed for the density Hessian.

Let P=(p,0), with p in the exact source bracket used in topic82. Take delta=33/2000. The N8 fine radial cells 4096 through4108 and their angular cap cover B_(3delta)(P), as checked independently in topic83. For this independent calculation enlarge the angular cap to the exact rational 3/500. Its sine will be compared directly with (3delta)/p_min in both engines. This topic bounds the density Hessian on the full enclosing radial-angular rectangle, using all angular cells and no geometric exclusion filter. Reflection in y extends the bound to the lower half-disc. The rectangle may include points outside the disc, which is harmless for an upper bound.

For any real interval enclosures of the three sums below on every selected cell, the stated formulas give a rigorous upper bound on sup ||D^2 rho||_F. Every finite mode is retained, and the exact polynomial is evaluated rather than truncated. The numerical conclusion is pending and must name its certified upper bound once both independent methods pass.

## Orthonormal polar Hessian

For a C^2 scalar field, in the orthonormal frame e_r,e_theta its Hessian is

 H_rr=rho_rr,
 H_rtheta=r^(-1) rho_rtheta-r^(-2)rho_theta,
 H_thetatheta=r^(-1)rho_r+r^(-2)rho_thetatheta.

These follow by differentiating grad rho=e_r rho_r+e_theta rho_theta/r and using partial_theta e_r=e_theta and partial_theta e_theta=-e_r. Since t=log r, partial_r=r^(-1)partial_t. Substitution of the finite trial expansion gives

 H_rr=e^t sum_j (H_j''+5H_j'+6H_j) sin(f_j theta)=e^t A,
 H_rtheta=e^t sum_j f_j(H_j'+2H_j) cos(f_j theta)=e^t B,
 H_thetatheta=e^t sum_j (H_j'+(3-f_j^2)H_j) sin(f_j theta)=e^t C.

Orthogonal changes of frame preserve the Frobenius norm, because tr((Q^T H Q)^T(Q^T H Q))=tr(H^T H). Thus

 ||D^2 rho||_F^2=e^(2t)(A^2+2B^2+C^2).                 (1)

The factor two on the mixed component counts both symmetric entries. Bounding each sum before squaring preserves cancellations between modes and avoids the producer's repeated Cartesian derivative recursion.

## An independent trace and traceless formula

The Laplacian is the trace of the Hessian, and the two-dimensional traceless part has squared norm ((H_rr-H_thetatheta)^2+4H_rtheta^2)/2. Define

 L=sum_j (H_j''+6H_j'+(9-f_j^2)H_j) sin(f_j theta),
 T=sum_j (H_j''+4H_j'+(3+f_j^2)H_j) sin(f_j theta).

Then L=A+C and T=A-C. The elementary identity (A+C)^2+(A-C)^2=2A^2+2C^2 gives

 ||D^2 rho||_F^2=e^(2t)(L^2+T^2+4B^2)/2.             (2)

Method1 evaluates (1) with Arb polynomial ranges. Method2 evaluates (2) with mpmath.iv and a different polynomial-range algorithm. The resulting interval upper bounds need not coincide. Each is independently sufficient if the exact input-polynomial and coverage hypotheses are satisfied. Their maximum is a conservative common certificate; an overlap of output intervals by itself is not proof.

## Polynomial ranges and exact source data

Let p(z)=sum_(i=0)^d c_i z^i, d<=7. On z=a+h u, 0<=u<=1, expand

 p(a+h u)=sum_(l=0)^d v_l u^l,
 v_l=h^l sum_(i=l)^d binom(i,l)c_i a^(i-l).

Its Bernstein coefficients of degree d are

 b_k=sum_(l=0)^k [binom(k,l)/binom(d,l)]v_l.

Indeed u^l=sum_(k=l)^d [binom(k,l)/binom(d,l)] binom(d,k)u^k(1-u)^(d-k), by factoring out u^l and applying the binomial theorem. The Bernstein basis is nonnegative and sums to one, so p(z) lies between the least coefficient lower bound and greatest coefficient upper bound. This argument holds for interval coefficients containing the exact coefficients. The first method uses this range enclosure.

The second method shifts the polynomial to the exact midpoint of its evaluation interval and evaluates the complete polynomial by interval Horner on a symmetric interval. The binomial shift is exact algebra and interval arithmetic preserves enclosure. No truncation remainder is needed. Derivative polynomials are formed exactly from coefficient balls by multiplying by their integer degree, then combining the displayed integer coefficients. Every trigonometric factor is evaluated on an interval covering its full angular cell.

The archive spans are matched against the exact selected radial cells. If one geometric cell crosses an original spline knot, it must be split there before either polynomial is used. All resulting intervals are closed; shared endpoints are covered by both adjacent formulas. The density is C6 across these joins, so its Hessian is unambiguous. Extending a polynomial past a span is not used as a claim about the trial.

## Scope

This calculation accepts no velocity derivative, source inverse, residual or nonlinear bound. A Hessian bound may be inserted as M_rho in topic77 only with its canonical correction in topic80 and the remaining independently proved hypotheses. The current exact trial and its finite regularity remain as specified in PROMPT. There is no decisive endpoint from a density Hessian bound alone.
