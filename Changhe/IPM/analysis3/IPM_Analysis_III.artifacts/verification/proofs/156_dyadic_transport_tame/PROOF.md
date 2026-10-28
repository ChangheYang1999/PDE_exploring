# A tame dyadic transport commutator

## Statement

Let C=R times S1. Let s and Lambda be real bounded smooth functions with all derivatives bounded, 0<s_-<=s(X)<=s_+<infinity, and let N be fixed. Choose a smooth inhomogeneous dyadic Fourier resolution Delta_k, k>=0. Define

 w_j(X)=exp(N Lambda(X)) 2^(j s(X)).

For j>=1 let Q_j=Op(q_j(X,xi)), where q_j vanishes outside c 2^j<=<xi><=C 2^j for fixed positive c,C. For j=0 use a fixed bounded frequency ball. Assume the scaled symbol estimates

 |partial_X^alpha partial_xi^beta q_j(X,xi)|
                      <=C_(alpha,beta) 2^(-j|beta|)              (1)

uniformly in j. Left quantization is used. Only finitely many seminorms enter the conclusion. If B is a vector field in H^{s(.)}(C) with bounded first derivatives, and v is in H^{s(.)}(C) with bounded first derivatives, then

 (sum_j ||w_j sum_l [Q_j,B_l] partial_l v||_2^2)^(1/2)
 <=C [||DB||infinity ||v||H^s
                         +||B||H^s ||Dv||infinity].             (2)

The norm H^{s(.)} is the dyadic norm of proof 123, with its fixed inhomogeneous low-frequency convention. Equation(2) is a square-function coefficient commutator. It is not the false unmodified bound for [Op(<xi>^s),B.grad] refuted in proof 151, and it does not by itself prove a bound for the sum over j of these commutators.

An important allowed family is

 q_j(X,xi)=(<xi>/2^j)^s(X) psi_j(xi),
 A_j=w_j Q_j=Op(exp(N Lambda(X))<xi>^s(X) psi_j(xi)),      (3)

where the real smooth dyadic functions psi_j have the above supports and sum_j psi_j^2=1. On the support of psi_j the ratio <xi>/2^j is bounded above and below, so (1) follows even after X derivatives. For this family (2) estimates sum_l[A_j,B_l]partial_l v.

If B=c E+Z, where E is a fixed smooth bounded field with all derivatives bounded and Z belongs to H^{s(.)} with bounded first derivatives, the right side may be replaced by

 C_E |c| ||v||H^s
 +C [||DZ||infinity ||v||H^s+||Z||H^s ||Dv||infinity].     (4)

In particular, proof 155 and s_->2 give a bound C||g||G ||v||H^s for the normalized IPM perturbation field. Constants are qualitative.

## Moderate weights and kernels

There are fixed M and C such that

 w_j(X)/w_j(Y)<=C(1+2^j d(X,Y))^M,                       (5)

where d is cylinder distance. To verify this, bounded Lambda contributes a constant. If d<=2^(-j/2), the logarithm of the remaining ratio is at most j log(2)||Ds||infinity 2^(-j/2), uniformly bounded. If 2^(-j/2)<d<=1, log_2(1+2^j d)>=j/2, which bounds j|s(X)-s(Y)| after increasing M. If d>=1, use the bounded oscillation of s and log_2(1+2^j d)>=j. Low j changes only the constant.

For k>=j-C_0 it follows that

 w_j(X)/w_k(Y)
 <=C 2^(-(k-j)s_-)(1+2^j d(X,Y))^M,                     (6)

with the fixed negative values of k-j absorbed into C. We use (6) only with k>=j-C_0.

Frequency integration by parts in (1) gives, for arbitrary sufficiently large L,

 |K_j(X,Y)|<=C_L 2^(2j)(1+2^j d(X,Y))^(-L),             (7)

and the same estimate after a scaled input derivative. The periodic coordinate is obtained by summing the Euclidean kernels over its translates; the bounds are summable. Equations(5)-(7) and Schur's test give the usual weighted convolution bounds. In particular, for |k-j|<=C_0,

 ||w_j [Q_j,F] partial_l Delta_k v||_2
 <=C ||DF||infinity ||w_k Delta_k v||_2.                (8)

Indeed the commutator kernel is K_j(X,Y)(F(Y)-F(X)), so it gains d(X,Y), hence 2^(-j). Move the weight with (5), and use the weighted Bernstein estimate for Delta_k to supply 2^k. That Bernstein estimate follows from the same kernel argument applied to a larger dyadic cutoff. This proves (8).

Another consequence used below is, for k>=j-C_0 and bounded f_k,

 ||w_j Q_j((Delta_k B) f_k)||_2
 <=C 2^(-(k-j)s_-) ||w_k Delta_k B||_2 ||f_k||infinity.   (9)

Move w_k from the input to the output with (6) and apply Schur. Also Q_j maps bounded functions to bounded functions with uniform norm, by (7).

## The low-coefficient and high-input terms

Choose a fixed large integer C_0 in the Bony decomposition, so the product of an input at frequency 2^k and a coefficient below 2^(k-C_0) remains in an annulus comparable to 2^k. For a scalar component B_l, write this part as

 sum_k (S_(k-C_0) B_l) partial_l Delta_k v.

After applying Q_j, only |k-j|<=C_1 can occur because Q_j has input-frequency support in its j-th annulus. This remains exact when its symbol depends on X: its integral over input frequencies is still restricted to that annulus. Subtract the corresponding low-coefficient part of B_l Q_j partial_l v. The kernel commutators are bounded by (8), since

 ||D S_(k-C_0) B_l||infinity<=C||DB||infinity.

Differences between the low cutoffs with indices k and j have only finitely many blocks at frequency comparable to 2^j. Their suprema are at most C 2^(-j)||DB||infinity; the derivative on v supplies 2^j, and the weights w_j,w_k are comparable. The square sum of this entire part is bounded by C||DB||infinity ||v||H^s.

## The terms containing a high coefficient frequency

The remaining part of Q_j(B_l partial_l v) is a sum of two types:

 Q_j((Delta_k B_l) S_(k-C_0) partial_l v), |k-j|<=C_1,
 Q_j((Delta_k B_l) partial_l Delta_m v), |m-k|<=C_1, k>=j-C_1.

Low-frequency cutoffs and dyadic blocks are bounded on L-infinity, so every displayed factor involving Dv is at most C||Dv||infinity. The first type follows from (9) with a bounded difference k-j. The second follows from (9) and the summability of

 a_n=2^(-n s_-), n>=-C_1.

Young's inequality for convolution in the integer index therefore bounds their square sum by C||B||H^s ||Dv||infinity. This is why a strictly positive lower order is required. In particular the high-high-to-low contribution is not summed with an unjustified l1 bound.

The remaining subtraction terms B_l Q_j partial_l v contain coefficient blocks Delta_k B_l with k>=j-C_1. At each X,

 w_j(X)|Delta_k B_l(X)|
             <=C 2^(-(k-j)s_-) w_k(X)|Delta_k B_l(X)|.

The uniform L-infinity bound for Q_j and the same sequence convolution bound give C||B||H^s ||Dv||infinity. Combining the three estimates proves (2). A finite smooth approximation proves the formula first without convergence issues. The bounds pass to the stated spaces by density and distributional convergence. Equivalently, the estimates show that all of the Bony sums converge in the target square-sum space.

## A fixed smooth nondecaying field

For a fixed E, the low-coefficient argument uses ||DE||infinity. Its high blocks satisfy ||Delta_k E||infinity<=C_R 2^(-kR) for every fixed R, including after finitely many derivatives. In the high-coefficient terms one now estimates the v factor in weighted L2 instead of its supremum. If its input frequency is m<=k+C_1, the ratio w_j(X)/w_m(X) costs at most C 2^(max(j-m,0)s_+), and its derivative costs 2^m. Moving the output weight through Q_j uses (5) and an integrable kernel. In all of these terms k>=max(j,m)-C_1. After summing 2^(-kR) over these k, the resulting matrix in j,m is bounded by C 2^(-(R-s_+-1)max(j,m)). This matrix has bounded row and column sums when R>s_++3. This overestimate also covers the comparable-frequency and high-high-to-low terms. For the subtraction (Delta_k E) Q_j Dv, k>=j-C_1, the input frequency m is comparable to j; its bound is C 2^j 2^(-kR)||w_j Delta_m v||_2 and is summable. The finitely many low blocks are covered by (8). Thus the square sum is bounded by C_E||v||H^s, proving (4).

## Exact logarithmic term and limitation

For the family(3), differentiating the left symbol gives the exact identity

 A_j(B.grad v)
 =B.grad(A_j v)-N(B.grad Lambda) A_j v
 -(B.grad s) A_j log<D>v
 +sum_l[A_j,B_l]partial_l v.                            (10)

The third term is not included in (2). The robust fixed order of proof 152 makes its total coefficient nonnegative for small perturbations; proof 153 supplies the positive-form bound at C^(1,alpha) regularity. Those facts suggest an energy argument using the family A_j. To obtain the full high estimate one must still check that the summed dyadic energy has the same background principal matrix and compact remainders as the single-operator energy, and then pass to the exact maximal domain. Those steps are not asserted by this proposition.
