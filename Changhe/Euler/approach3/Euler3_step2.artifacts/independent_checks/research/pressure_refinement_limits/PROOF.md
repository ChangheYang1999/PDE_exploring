# What two pressure quadratures can establish

Status: proved statements in a normed space. The counterexample concerns inference from numerical differences; it is not an Euler field or an assertion that an observed pressure computation is inaccurate.

## Statement, hypotheses and notation

Let H be a nonzero real normed vector space. For two states X in {A,B}, let F_X in H contain all nonpressure residual terms, let P_X in H be the exact pressure gradient, and let P_X^L,P_X^H in H be two approximations. Define R_X^i=F_X+P_X^i for i in {L,H}, R_X=F_X+P_X, delta_X=||P_X^H-P_X^L||, and D_i=||R_A^i||-||R_B^i||. All terms for one state must use the same points, weights and norm.

Then |D_H-D_L| <= delta_A+delta_B. In particular, if D_H > delta_A+delta_B then D_L>0. Thus a large computed gap compared with the observed refinement changes establishes stability between these two approximations.

Without another hypothesis relating either approximation to P_X, there is no finite upper bound on ||P_X^H-P_X|| from delta_X alone. Even an arbitrarily large ratio D_H/(delta_A+delta_B) cannot establish that the exact residual norms differ.

If separate error bounds ||P_X^H-P_X|| <= E_X are available, then |D_H-(||R_A||-||R_B||)| <= E_A+E_B. Consequently D_H>E_A+E_B implies ||R_A||>||R_B||. The quantities delta_X cannot replace E_X without a proved error relation.

## Complete argument

The reverse triangle inequality gives | ||R_X^H||-||R_X^L|| | <= ||R_X^H-R_X^L||=delta_X. Subtract the two norm differences and apply the scalar triangle inequality to obtain the first bound. Its sign consequence follows by D_L >= D_H-delta_A-delta_B.

Choose u in H with ||u||=1. For any epsilon>0 and B>0, set P_X=0, P_X^L=B u and P_X^H=(B+epsilon)u. The refinement difference is epsilon, while the high-order error is B+epsilon, which is unbounded as B increases. An identically zero refinement difference also permits arbitrary B by taking P_X^L=P_X^H=B u.

For the two-state conclusion, set F_A=F_B=P_A=P_B=0. Take P_A^L=u, P_A^H=(1+epsilon)u, P_B^L=0 and P_B^H=epsilon u. Then the exact residual norms are both zero, D_H=D_L=1, and delta_A+delta_B=2epsilon. Choosing epsilon<1/(2M) gives a gap/refinement ratio greater than any prescribed M>0. Both approximations at A share an error that their difference does not measure.

Finally apply the same reverse triangle inequality with R_X in place of R_X^L and add the two error bounds. This proves the conditional bound and sign consequence.

## Dependencies and scope

Only the triangle inequality and positive homogeneity of a norm are used. For a finite positive-weight quadrature, H is the Euclidean space of weighted arrays, as in ../holdout_quadrature/PROOF.md. A changing denominator requires a separate sensitivity argument for normalized residual ratios. These statements neither certify nor refute convergence of the campaign's Green quadrature. They identify which conclusion follows from two evaluated pressure approximations alone.
