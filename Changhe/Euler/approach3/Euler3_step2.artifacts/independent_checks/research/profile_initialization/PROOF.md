# Lowest initial objective does not imply the best finite-budget profile value

Status: proved exact elementary statement and counterexample. This does not oppose the registered initialization heuristic. It limits the conclusion that can be drawn from it.

## Statement

Let A be a nonempty coefficient set. For each fixed parameter p, let F_p:A -> [0,infinity) be an objective, and define the ideal profile value I(p)=inf_{a in A} F_p(a). Every feasible computed coefficient a gives I(p)<=F_p(a). Suppose a finite collection of initial candidates a_1,...,a_k is nonempty, choose a_star to minimize their initial objective values, and apply any descent procedure producing a feasible output b with F_p(b)<=F_p(a_star). Then

I(p)<=F_p(b)<=min_i F_p(a_i).

This inequality does not imply F_p(b)<=F_p(b_i) for outputs b_i obtained by applying the same procedure for the same budget from the other initial candidates. It does not establish the ideal profile minimum or quantify the optimization error F_p(b)-I(p).

## Proof and explicit least-squares counterexample

The first inequality is the definition of infimum. The second is the assumed descent property and the definition of a_star.

For the non-implication take A=R, one fixed parameter, residual r(a)=a^2-1 and objective F(a)=r(a)^2/2. Perform one damped linearized least-squares step with damping lambda=1: choose delta minimizing (r(a)+r'(a)delta)^2+delta^2, then output a+delta. Differentiation of this strictly convex quadratic gives the unique delta=-r'(a)r(a)/(r'(a)^2+1).

At a_1=0, F(a_1)=1/2, r'(a_1)=0 and delta=0, so b_1=0 and F(b_1)=1/2. At a_2=2, F(a_2)=9/2, r'(a_2)=4 and delta=-12/17. Thus b_2=22/17 and

F(b_2)=( (22/17)^2-1 )^2/2 = 38025/167042 < 1/2.

Both starts receive exactly one step of the same positive-damping procedure, and both outputs satisfy nonincrease. Selecting the lowest initial objective chooses a_1 and misses the better output b_2. The global profile infimum is zero, attained at a=1 and a=-1. This example does not need a difference in evaluation cost, step acceptance or numerical arithmetic.

## Campaign interpretation and scope

Choosing the best available iteration-0 candidate among kept, offline-refit and linear-response coefficients is a reproducible initialization heuristic. Reporting all candidate initial values makes the choice inspectable. If the subsequent worker is monotone, it controls the final value by that lowest initial value. It does not make the finite-budget profile bound the tightest attainable among other starting basins. Different parameter points can retain different optimization errors; even equal nominal budgets do not identify a profile minimum. This is a methodological limitation, not a demand to run every start or change the lead's registered budget.

The statement requires all compared values at one fixed parameter to use the same objective, constraint set, gauge convention and evaluation settings. A value after a coefficient projection or a parameter change belongs to the corresponding actual feasible point and must be evaluated there. Values produced before and after a gauge projection cannot silently be treated as identical initial states.

Dependencies: definition of infimum, finite minimum, elementary differentiation of a strictly convex scalar quadratic and rational arithmetic. No formal proof has been built.
