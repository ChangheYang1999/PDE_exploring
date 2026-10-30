# Acceptance of the two remaining T2 review repairs

## Statements, hypotheses and dependencies

This audit concerns revision 2 of T2's the review of T4-469 and the T2 check of T4-479 (report repair). The first is a corrected review of an already audited theorem; the second checks specified paragraphs of a historical coordinator report. It introduces no candidate integration or new existence hypothesis. T4-475 supplies the full finite-mode theorem and independent examples, and T4-485 supplies the fixed-norm optimum and its nonlinear side conditions. Both results and their exact inputs are dependencies.

The first claim is that beta_min>3/2 is a sufficient condition for the stated rational trial family to have gradient and r Delta in L2, but is not necessary when uncancelled labels are used for a sum. Here r=|X|, t=r^2/(1+r^2), and psi=u(r)sin(3theta). The corrected review gives

 u=r^3(1+r^2)^(-3/2)(1-t)=r^3(1+r^2)^(-5/2).

With d=||grad psi||2^2, a=||A_(Delta psi)-grad psi||2^2 and M2=||A_(-Delta psi)||2^2, it states d/pi=5/12, a/pi=25/432, M2/pi=205/432. It makes no change to T4-469's sufficient hypotheses. Its historical source and test-count disclosures are checked against the frozen review accepted in475.

The second claim is restricted to the saved report excerpt whose SHA256 is68168051a89e41ac8502534f468b5fc3fc9b5657cfb5bce1b01788dd51eb7f83. It states the fixed-norm scalar budget

 eta*=40722836401/193491763200000, r*=201799/149299200,

and compares it with the already accepted lower bound X(F007)>756.5312630768. It does not assert that this number is optimal across different norms or that it is a necessary PDE tolerance. The provenance statement that the excerpt came from a complete report of a given historical hash is retained as the producer's record unless that entire historical file is independently available.

## Complete proof of the trial correction

The identity 1-t=(1+r^2)^(-1) proves the simplification. At the origin r^3 sin(3theta)=3x^2y-y^3, and the radial factor is smooth. At infinity u=O(r^-2), with the same differentiated decay. Thus grad psi and r Delta psi are square integrable there and locally; radial smooth cutoffs converge in the gradient norm. Each of the two terms before cancellation tends to a nonzero constant, respectively1and-1. Its Laplacian has leading coefficient -9u/r^2, and its gradient squared has leading angular contribution9u^2/r^2. Hence each term separately has logarithmically divergent gradient energy and integral r^3(Delta psi)^2dr. Cancellation makes the sum admissible.

For direct exact verification write u=r(1-t)^b P(t), b=3/2, P=t. Define D_bP=(1-2bt)P+2t(1-t)P'. Direct differentiation yields

 D_bP=3t-5t^2, D_b^2P=9t-40t^2+35t^3.

Changing from r to t gives

 d/pi=(1/2)int_0^1(1-t)[(D_bP)^2+9P^2]dt,
 a/pi=(1/2)int_0^1(1-t)[(D_bP)^2+(D_b^2P)^2/9]dt,
 M2/pi=(1/18)int_0^1(1-t)(D_b^2P-9P)^2dt.

Each polynomial integral is evaluated by int_0^1 t^j(1-t)dt=1/((j+1)(j+2)). This gives the three stated rationals and M2=d+a. Consequently the revised sufficient wording is correct, and the earlier necessity claim is false. The original theorem's trial family still requires every beta>3/2, so the example does not contradict that theorem.

## Complete proof of the report arithmetic

At fixed s=1/5184 and weights (2^15,2^20), set mu=201799/648000 and A=576/5. The sufficient scalar budget is e(r)=r(mu-Ar), for 0<r<mu/A. Completing the square gives

 e(r)=mu^2/(4A)-A(r-mu/(2A))^2.

The unique maximizer and maximum are exactly r* and eta* above. T4-485 separately proves that the low contraction and origin-slope conditions hold at this radius. Exact comparisons give eta*>0.00021046 and 0.00135155<=r*<0.00135165. At the registered radius r=1351/10^6,

 e(r)=85237452769/405000000000000>0.00021046.

For X007=7565312630768/10^10, exact division gives X007/eta*>3594606 and X007/(4207/20000000)>3596535.57. The true residual norm exceeds X007, so these are strict failure-factor floors. The printed decimal ratios remain rounded diagnostics. The source excerpt contains the optimum, radius and registered-radius qualification in each of the three claimed blocks. The result is an acceptance of those specified repairs only.

## Verification and scope

The checker freezes both reviews, their scripts and saved outputs, and the report excerpt. It parses producer code without executing it. Exact polynomial arithmetic reconstructs the trial energies; exact fractions establish the radius and factor comparisons. A diff records every change from the old review, and hashes bind the already accepted475/485 results. The initial statement is written before this checker. Verification evidence is under verification, exact parameters under data, and finite Python sources under code. No Lean sources or build are involved. The actual configured Opus5.5 collaborations are the existing T1/T2/coordinator lane records; provider identity is unobservable.
