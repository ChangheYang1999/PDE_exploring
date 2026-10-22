# Coherent derivative cells and the effect of rounded left endpoints

Written 2026-10-21 before the new computation. This is a conditional geometry and weight theorem. The saved derivative majorants have not been independently proved for the physical trial on all these cells.

## Statement

Fix L>0 and 0<k<1. Let b_-=the exact first distinct knot and b_+=the exact last distinct knot of the normalized modal_v2 trial. Its exact middle partition consists of 7809 closed intervals [t_i,t_(i+1)] obtained by rational equal subdivision of each knot span. Use the exact JSON partition of the accepted middle-residual construction. Add the inner partition

 s_i=b_- -5+5i/2632, 0<=i<=2632,

and the outer partition

 z_i=b_+ +17i/8948, 0<=i<=8948.

All these are rational numbers. Their union is the single closed interval [b_- -5,b_+ +17]. The end of the inner partition equals the start of the middle partition, and the end of the middle equals the start of the outer.

For every cell, let a_i be its exact left endpoint and d_i its exact positive length. Let ahat_i and h_i be the exact binary64 values stored as t_a,h in the matching saved derivative row. Let the source midpoint-radius boxes for the base, tau or middle endpoint be interpreted as closed real intervals with exact binary64 midpoint and radius.

The finite geometric obligations are these:

1. Every a_i is in the corresponding producer input start box and every d_i is at most h_i. Source h_i must equal the actual midpoint-radius subtraction/magnitude calculation at the frozen source values. For the outer and inner regions ahat_i must equal the frozen Arb128 start-box addition followed by midpoint conversion; in the middle it must equal the saved tb midpoint. This is current-source reproduction, not historical runtime authentication.
2. Source base endpoints agree exactly with b_-,b_+. Every rational tau endpoint is in its exported tau box. The middle rational endpoints are in their tb boxes. The coordinates are ordered and do not cross a middle knot span.
3. Set delta=max_i |a_i-ahat_i|. The exact data audit must prove a stated rational upper bound on delta. No floating endpoint union is substituted for this coherent partition.

Assume, separately, that each saved W_pq,i is a valid majorant of sum_N (2N+1)^q |partial_t^p f_N(t)| throughout its coherent true cell, for (p,q)=(0,0),(1,0),(2,0),(0,1),(1,1). Assume the Fourier expansion and derivatives meet the weighted square-integrability hypotheses below. Define

 A_i=W00_i^2+W10_i^2+W01_i^2,
 B_i=(W00_i+W10_i)^2+(W10_i+W20_i)^2+(W01_i+W11_i)^2,
 v(t)=L^2 (exp(t)/L)^(-4) (1+(exp(t)/L)^2)^(3/2-k).

Then on E=[exp(b_- -5),exp(b_+ +17)],

 ||f||_(X(E))^2 <= pi exp(4delta) sum_i h_i v(ahat_i) A_i,
 ||f-partial_t f||_(X(E))^2 <= pi exp(4delta) sum_i h_i v(ahat_i) B_i,          (1)

where ||g||_(X(E))^2 is the integral over r in E and 0<=theta<=2pi of [g^2+r^2|grad g|^2] m(r)^(-2)(1+r^2/L^2)^(-3/2) r dr dtheta and m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2).

These conclusions retain the physical-majorant hypothesis. They do not prove it by inspecting interval coordinates.

## Proof of the coverage and interval-parameter implication

The inner and outer nodes are increasing arithmetic progressions with the stated shared endpoints. The middle JSON must be checked to be a contiguous rational subdivision from b_- to b_+. Finite closed intervals with consecutive common endpoints cover the full interval between their first and last endpoints. This proves coverage and makes no claim about the different union defined by the rounded ahat_i.

At a true cell start a_i choose the actual base and tau and all actual density/Green input values. If these values lie in their respective source boxes, then they form an admitted, possibly correlated tuple in the product of those boxes. A whole-input-box enclosure for the producer's local variable sigma in [0,h_i] applies to this tuple. Because every t in the true cell has sigma=t-a_i in [0,d_i] and d_i<=h_i, it applies to the whole true cell. Interval independence is only an enlargement of admissible tuples. It is not a requirement that the physical inputs vary independently.

Conversely, this argument is unavailable if the derivative routine encloses only midpoint input data, if a needed physical input is outside its source box, if a model remainder is unproved, or if it treats the wrong local variable. The present result leaves all those physical enclosure and execution issues explicit. It only verifies the geometry necessary to apply such an enclosure. A polynomial model may be used on its small artificial overhang beyond d_i without interpreting it as the neighboring physical spline there.

## Proof of the weight and norm bounds

Differentiation gives

 (log v)'=-4+(3-2k)u^2/(1+u^2), u=exp(t)/L.

Since 0<k<1, this derivative lies strictly between -4 and 0. Thus v is decreasing, and integration of its logarithmic derivative gives v(a_i)<=exp(4|a_i-ahat_i|)v(ahat_i). For t in the true cell, v(t)<=v(a_i). The source h_i upper bound therefore implies

 integral_cell v(t)dt <= d_i v(a_i) <= h_i exp(4delta)v(ahat_i).

Full-circle sine/cosine orthogonality gives the X norm identity with integrand pi v(t) sum_N [f_N^2+(partial_t f_N)^2+(2N+1)^2f_N^2]. The inequality sum b_N^2<=(sum |b_N|)^2 bounds its three sums by A_i. Applied to f-partial_t f, the triangle inequality bounds them by B_i. Integrating cell by cell proves (1). Finite Fourier sums require no limiting argument. For infinite sums assume convergence in the indicated weighted first-derivative square integrals and apply the finite identity followed by that convergence.

This proof establishes a global bound on the displayed finite annulus if its hypotheses hold. It supplies no contribution for r<exp(b_- -5) or r>exp(b_+ +17). It gives no inverse constant, lower bound on ||K||, norm estimate near X3, existence or exclusion endpoint.

## Data and independent checks

The first method uses NumPy only to read the original NPZ small geometry members, exact Fraction arithmetic for coherent nodes and interval inclusion, frozen MR source reproduction for h, and Arb128 to reproduce source start rounding. It independently checks the returned h against the exact true length. The second method reads the same original NPY members directly from ZIP without NumPy, decodes every IEEE754 entry with integer shifts, reconstructs all rational nodes by a separate span traversal and checks the containments with flint fmpq. It checks the binary64 rounding cells of all source JSON t_a,h tokens against their decimal rational values. The engines must compare every exact discrepancy and every actual row, not just maxima.

The frozen source files, exact extracted geometry JSON, source hashes, both actual outputs and an actual completed Claude Opus5.5 review will be preserved. Accepted topics152 and153 remain immutable: topic153's literal exported union still has its proved gaps. This new coherent interpretation concerns other intervals and does not contradict that result. The current proof is OPEN until the indicated checks and independent adjudication complete.
