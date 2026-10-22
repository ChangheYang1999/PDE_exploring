# Fresh finite-antiderivative audit

A third calculation checks selected modes at higher precision and all
saved remainder verdicts by exact comparisons. It does not invoke the
first two calculation functions. For q'=lambda q+sign Z e^(2u)F(u),
if lambda!=2 choose the polynomial Q solving

 Q'+(2-lambda)Q=sign F.

Its coefficients are obtained backwards from the highest degree. Then
q=e^(lambda u)(q(0)-Z Q(0))+Z e^(2u)Q(u), verified by direct
substitution and the initial value. For a monomial F=u^k the coefficients
are Q_v=sign (-1)^(k-v) k!/[v!(2-lambda)^(k-v+1)], 0<=v<=k.
Exact rational summation gives its Taylor coefficient weights; input
symbols are combined before interval evaluation. This construction
uses neither the beta-integral sum nor the affine time recursion.

For lambda=2 instead q=e^(2u)[q(0)+sign Z int_0^u F(v)dv]. The integral
is a degree8 polynomial with coefficient sign F_k/(k+1) at order k+1.
The homogeneous term retains q(0). This handles the n2 plus branch.
For n1 lambda_plus=0, integer zero-power conventions apply as before.

For a polynomial Q of degree d, define
B_N(Q)=sum_k |Q_k| sum_(v=0)^min(N,k) choose(N,v) 2^(N-v)
                       k!/(k-v)! h^(k-v).
Then sup|D^N(e^(2u)Q)|<=exp(2h)B_N(Q). Thus, in the nonresonant case,

 sup|q^(N)|<=|lambda|^N exp(max(lambda,0)h)|q(0)-ZQ(0)|
                            +Z_max exp(2h)B_N(Q).

In the resonant case apply the polynomial bound to
Q_res=q(0)+sign Z int F, keeping the full q(0) and Z input boxes.
All endpoint magnitudes and products are enclosed in Arb1536. Averaging
the plus/minus derivative bounds gives a common P,R degree22 Taylor
remainder. Adding magnitudes of exact coefficient intervals at orders13
through22 gives another rigorous degree12 remainder, by the preceding
refinement proof. This fresh bound is checked against the unchanged
producer budgets for each selected mode, as well as the coefficients.

The artifact audit separately checks every1566 saved engine-mode record
from v3: exact coverage, no duplicate or missing record, no coefficient
failures, finite nonnegative candidate radii, full saved remainder upper
endpoint below the candidate budget, and all file hashes. It checks that
the candidate arrays from v2 and v3 are identical, so the refinement did
not enlarge any budget. The earlier failed tests remain part of the
publication evidence. The finite-antiderivative calculation is a
supplementary spot audit of five named modes in each of three cells,
not a third whole calculation over all261 modes.
