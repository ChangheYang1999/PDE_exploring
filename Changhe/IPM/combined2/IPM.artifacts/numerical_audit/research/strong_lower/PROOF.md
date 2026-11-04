# Certified finite-point lower bounds for the registered strong norm

## Exact hypotheses and convention

Use the authoritative exact Candidate 007, the independent Cartesian Taylor construction of ../cartesian_jets/PROOF.md, and the sum convention

\[
S_F(\alpha,\delta,\sigma)=\sum_{j=0}^{k}\|D^j g\|_\infty+[D^kg]_\beta,
\qquad g=\langle X\rangle^\sigma F,
\quad 1+\alpha+\delta=k+\beta,
\]

where k is a nonnegative integer and 0<beta<1. Tensors use the ordered Frobenius norm. The implementation below supports k<=2 and records derivatives through order three. All evaluation points, weights and Holder orders are exact rationals saved in JSON. Distinct point pairs have strictly positive exact squared distance.

## Lower-bound argument

For any finite set of points P_i, define

\[
L_j=\max_i|D^jg(P_i)|_F,
\quad
L_H=\max_{i<h}\frac{|D^kg(P_i)-D^kg(P_h)|_F}{|P_i-P_h|^\beta}.
\]

Every point value is bounded by the defining supremum. Every distinct pair is among the pairs in the global Holder seminorm. Therefore

\[
S_F\ge\sum_{j=0}^k L_j+L_H. \tag{1}
\]

The maxima in the different summands need not occur at the same point. This is allowed because the target norm is the sum of independent suprema and the Holder seminorm.

The exact tensor formulas are

\[
|D^jg(P)|_F^2=\sum_{b=0}^{j}\binom jb
 |\partial_x^{j-b}\partial_y^b g(P)|^2
\]

and the same formula applied to component differences gives the pair numerator. The binomial factors count ordered index tuples. Cartesian Taylor coefficients must first be multiplied by (j-b)!b! to obtain derivative values.

Evaluate the potential jet and all subsequent derivatives, products and positive rational powers in outward ball arithmetic. The Cartesian construction through seven potential derivatives supplies the residual derivatives through order three. For each point norm and pair quotient, take its exact lower endpoint, replacing a negative endpoint by zero if necessary. Maxima and addition of these rational lower endpoints then give a rigorous lower bound in (1). There is no claim that the finite maxima exhaust the global ones, and no quadrature or exterior remainder is needed for a lower bound.

## Selection, checks and scope

Point locations are chosen near peaks reported by the numerical team and rounded to rational coordinates. The choice influences the strength of the bound, not its validity. Every selected point is evaluated afresh from the exact candidate by the independent Cartesian code. The producer's floating function values and pair quotients are not inputs.

The own polynomial jet fixtures are run first. A separate exact tensor fixture checks the binomial multiplicities. Every positive norm or quotient must retain the recorded minimum arithmetic accuracy before an endpoint is accepted. Input, canonical representation, point-set JSON and both implementations are bound by hashes.

These are lower bounds for a specified strong norm of the residual. They do not bound the inverse image h0, the inverse constants, the radius of an invariant ball, or the distance to an exact solution. An upper bound or an existence claim requires separate arguments.
