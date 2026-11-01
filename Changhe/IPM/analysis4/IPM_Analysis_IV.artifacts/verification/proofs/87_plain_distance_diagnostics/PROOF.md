# Finite plain-norm curvature and distance partitions

Status: finite interval diagnostics only. No asymptotic growth model is assumed.

## Definitions and exact identities

For the canonical delta=2/3, c=3, sin(theta) sequence write H_n=sum h_(n,q,m)t^q sin(m theta). Define the plain coefficient norm M_n=sum_(q,m)|h_(n,q,m)| and L_n=log10 M_n. The second-difference statistic at lag h is

\[
 \widehat\sigma_{n,h}=
 \frac{L_n-2L_{n-h}+L_{n-2h}}
 {\log_{10}(n!)-2\log_{10}((n-h)!)+\log_{10}((n-2h)!)}.
\]

For n>2h the denominator is positive, since its exponential is the product of (n-j)/(n-h-j)>1 for j=0,...,h-1. If M_n=C A^n(n!)^sigma holds at the three specified indices, cancellation of the constant and linear terms gives exactly sigma. Without this hypothesis, the statistic is only a finite diagnostic. Lag30 is a multiple of the residue period3.

For order290, the weighted mass of column q is W_q=q!12^q sum_m|h_(q,m)|. We partition each column by distance d from the specified center: near d<=q/4, middle q/4<d<=q, far d>q; at q0 near means d<=2 and the middle band is empty. Two centers are computed explicitly: |P_n| for both fields, and |P_n+1| for density with |P_n| for stream. Here P_n=2-2n/3. These are distinct diagnostics and must not be confused.

Within a fixed column, the factor q!12^q cancels from the band fractions. The share of a column in the full weighted norm is W_q/sum_v W_v, so a column can be entirely near while contributing an arbitrarily small part of the full norm. Global band fractions and fractions conditional on q>=40 are formed by summing the weighted masses before dividing.

All boundaries are tested by multiplying distances by3, and then by4 when needed. Thus no rounded boundary classification occurs. The triangle inequality supplies the nonnegative masses. Arb interval addition, multiplication, logarithms and division enclose the derived quantities, and each claimed strict maximum is checked by strict interval comparisons against every other column or mode.

## Evidence and scope

The inputs are the frozen N290 checkpoint's already verified plain column norms and its exact packed interval coefficients. Both source hashes and the original checkpoint hash are retained. The script reconstructs weighted mass directly from coefficient intervals, independently of the numerical experiments' diagnostic code. None of the results establishes an infinite growth rate, a bounded nonlinear product loss, or a convergent or divergent exterior series.

## Later extension: stream shift shares and finite slope statistics

The stream-shift audit groups each coefficient at frequency m=2j by the exact rational quantity min(|P_n+m|,|P_n-m|), and also retains the sign of the minimizing factor. It sums interval absolute values over all log columns, then divides by the interval plain stream norm. Density near-band mass uses ||P_n|-(2j+1)|<=4/3. Every comparison with a peer floating result is only a finite rounded comparison.

For L_n=log10||H_n||_plain, the three-step slope is v_n=(L_n-L_(n-3))/3. A reported finite-window mean, sample standard deviation, or least-squares slope is evaluated by its defining finite sum in intervals. The regression standard error is the algebraic quantity sqrt(SSE/((N-2)Sxx)); no random model is assumed. It is a descriptive statistic and does not provide an asymptotic test or probabilistic confidence statement for this deterministic sequence.
