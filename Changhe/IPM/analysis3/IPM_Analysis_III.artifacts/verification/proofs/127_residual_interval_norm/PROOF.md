# Directed residual integration by angular-norm Taylor bounds

## Object and scope

Use the exact normalized original modal trial, its canonical full-plane velocity, and the strong target Y of topics98 and105. This proof describes an integration certificate, not a claimed numerical result. Numerical conclusions require complete coverage and successful output audits. The input data, normalization correction and exact Green boundary enclosures are those independently checked in topics4,15 and68.

Write F/r^3=p(theta)[gamma(t)+cos(theta)^2 Q(t,theta)], with p=cos(theta)^2 sin(theta). The squared Y norm is the integral of

 g(t) N(F/r^3)^2,  N(f)^2=gamma^2+M H(Q),
 g(t)=exp(-t/2) for t<0, exp(27t/4) for t>=0,
 M=2 Beta(1/4,3/2).

Here H is the exact angular probability quadratic form of proof 98. No raw angular truncation is made. Sine indices0 through522 include every residual mode; the final index is zero padding.

## A finite radial interval

Let I=[m-h,m+h] be contained in one analytic branch or one closed spline span, and not cross t=0. Use z=(t-m)/h. The density sine coefficients h_j are polynomials on a spline span and exponential polynomials on an end branch. The velocity coefficients P_n,Q_n have the same exponential-polynomial form. The exact residual coefficients are obtained from

 Lh-P cos(2n theta)(3h+h')+Q sin(2n theta) partial_theta h,
 Lh=ell(3h+h')-h.

Choose polynomial approximants to each coefficient in z. Their products and the angular Laurent products are formed before any interval evaluation. Suppose the resulting residual polynomial is sum_(j=0)^J f_j(theta) z^j and its exact omitted residual has sine coefficient l1 norm at most e_raw throughout I. Let N_max=522 and

 C_N=4 N_max^4(2 N_max+1), E=sqrt(1+M) C_N e_raw.

Proof 107 proves that this constant controls both angular divisions; it also dominates the map to gamma. Thus the omitted residual has N norm at most E. By the triangle and reverse triangle inequalities,

 max(0,N(f_0)-sum_(j=1)^J N(f_j)-E)
 <=N(F/r^3)<=N(f_0)+sum_(j=1)^J N(f_j)+E.               (1)

All terms are bounded by directed arithmetic using the complete angular Gram form. Multiplying the squared bounds in(1) by the exact positive integral of g over I gives lower and upper energy bounds. The use of polynomial coefficient norms is conservative but retains cancellations in each coefficient.

Every residual coefficient f_j is divisible by x^2, because the density is x^2 times a smooth angular polynomial, the radial velocity multiplies that factor, and the angular velocity is a sine polynomial in even frequencies and hence vanishes at the vertical axis. This remains true for independent radial polynomial approximants to the velocity modes. Thus the first angular division is structural. The subsequent axis subtraction is the exact linear quotient map, not a projected least-squares division.

## Exponential-polynomial Taylor remainder

For a term exp(e(t-m)) sum_i p_i(t-m)^i, its degree n Taylor polynomial in z has coefficients

 a_j=sum_(i<=j) p_i h^i (eh)^(j-i)/(j-i)!.

For |z|<=1 the omitted part has modulus at most

 sum_i |p_i| h^i exp(|e|h) (|e|h)^(n-i+1)/(n-i+1)!,       (2)

provided i<=n. This follows by the absolute exponential series remainder and is valid for either sign of e. Sum(2) over the finitely many exponents. Polynomial branches have zero omitted part once their degree is retained.

For approximations A=A_0+dA and B=B_0+dB, the product error obeys

 |AB-A_0B_0| <= e_A ||B_0||_sup+e_B ||A_0||_sup+e_A e_B.

The polynomial coefficient l1 sum bounds its supremum on |z|<=1. Applying this to both nonlinear residual products and adding the scaling-part error proves the e_raw used in(1). Angular products have sine/cosine l1 norm at most the product of their coefficient l1 norms. Derivatives h' are expanded as separate exact exponential polynomials; no derivative of a numerical remainder is inferred.

## Exact local Green reconstruction

At a spline center let H_j be the physical Taylor coefficients of the density mode. The local Green moments solve

 I'+(2n+4)I=h_(n-1),  J'-(2n-4)J=-h_n.

Their center values come from the independently certified left and right Green boundary values and exact exponential moments. Their polynomial particular solutions are computed by backward substitution. If b=2n-4 is zero, use J_part=-integral_0^u h_n(v)dv and retain its free constant separately. Add the exact homogeneous exponentials. Then

 P_n=n exp(2t)(J-I),
 Q_n=exp(2t)[n(J+I)-(h_n+h_(n-1))/2].                    (3)

Equations(3) agree with the independently derived point formulas of proof 105 and define analytic continuations of each spline span. No claim that this continuation equals an adjacent span is needed. Their shared endpoint values are included by continuity.

## Coverage and tails

The accepted finite certificate must partition a closed interval [T_-,20], with every spline knot and t=0 treated as an interval boundary. Its complete lower and upper sums are then added to separately proved inner and outer tail bounds. Proof 122 supplies the full outer tail beyond20. An inner tail bound, when used, must remove the exactly vanishing degree-three residual before estimating its positive exponential powers. Missing intervals, failed quotient checks, nonfinite endpoints or an omitted tail invalidate a full-norm conclusion.

## Dependencies and limitations

Topics4,15,68 certify the exact trial and Green values; topics98,105 certify the angular norm and complete residual formula; proof 107 supplies the angular coefficient l1 comparison; proof 122 supplies the outer tail. This proof neither changes the trial nor supplies inverse bounds or nonlinear closure.

## Inner tail

Let T< t_- and write H=H_0+H_+, where H_0 is the exact constant inner angular profile p. Write P=P_0+P_+, Q=Q_0+Q_+, where only mode n=1 of P_0,Q_0 is nonzero and equals c=3 ell-1. Direct substitution gives

 ell(3H_0)-H_0-P_0 cos(2theta)3H_0+Q_0 sin(2theta)partial_theta H_0=0.

Every exponent in H_+, P_+, Q_+ is at least2. The possible degree-one polynomial at exponent2 arises from the n=2 Green resonance. To include it without assuming a constant coefficient at that rate, use rate nu=3/2. For an exponential polynomial shifted to T, every exponent e>nu obeys, for u=t-T<=0,

 |u|^j exp(e u)<=j!/(e-nu)^j exp(nu u).

This is the elementary inequality v^j exp(-a v)<=j!/a^j for v>=0. It gives a bound for each of H_+, its exact derivative, P_+ and Q_+ at rate nu. The full H and 3H+H' and partial_theta H are bounded at rate0 by the same formula, including their constant terms. Therefore a raw residual bound at rate nu is obtained by summing

 |ell(3H_++H_+')-H_+|_1
 + |c| (|3H_++H_+'|_1+|partial_theta H_+|_1)
 + |P_+|_1 |3H+H'|_1 + |Q_+|_1 |partial_theta H|_1.

Here every factor means its corresponding majorant at T. If this sum is B_T, then the full inner Y energy is bounded by

 (1+M) C_N^2 B_T^2 exp(-T/2)/(2nu-1/2).

The exact constant cancellation is removed algebraically before forming B_T. No division by an interval believed to be small is used. A positive upper bound with lower bound0 suffices for the full norm enclosure.

## Machine coverage convention

The production calculation first forms the exact-rational partition: every nonempty original spline span, split at0 if necessary, together with adjoining inner and outer intervals reaching T=-40 and20. Analytic-end widths grow from1/125 to at most1/2 on the inner branch and1/10 on the outer branch. Each interval may be bisected if its Taylor error is too large. Accepted leaves replace their parent and must preserve its exact endpoints. Every accepted leaf, its index, and both directed energy endpoints are written immediately to a JSON-lines checkpoint. A separate audit reconstructs the partition using rational numbers, verifies the branch and knot constraints, verifies the original-data and code hashes, and sums the saved rational outward endpoints independently. The outer bound is imported only from the already audited proof 122 certificate, with its hash recorded.
