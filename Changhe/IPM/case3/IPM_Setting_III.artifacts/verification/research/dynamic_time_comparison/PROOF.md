# 169. What the first DR time-step table measures

Written 2026-10-21 before independent log parsing. This is an audit of finite diagnostics, not a continuum trajectory theorem. The exact setting, canonical generator G and numerical projection are those in result165; each frozen log is empirical data from a finite coefficient evolution.

Let f(t) be a twice continuously differentiable scalar diagnostic on [a,b]. Its linear interpolant I(t) satisfies f(t)-I(t)=f''(xi)(t-a)(t-b)/2 for an intermediate xi, so |f-I|<=sup|f''|(b-a)^2/8. The formula follows from Rolle's theorem applied to f-I minus its multiple of (t-a)(t-b). No curvature bound for the producer diagnostics is known. Two tables constructed from different log knots compare both trajectory errors and different interpolation errors. A small discrepancy between such interpolated diagnostics is useful empirical agreement; it is not automatically a same-time state error, a rate of time convergence, or a bound on the exact trajectory. Rounded time stamps and diagnostic columns contribute additional errors.

One refinement pair cannot establish an observed convergence order without additional information. For every integer p>0, the scalar approximation f_h=f+K h^p has discrepancy |K|h^p(1-2^-p) between h and h/2. By choosing K the same one-pair discrepancy occurs for every p. An asymptotic error model or more refinements are needed to identify p. Even zero discrepancy of selected diagnostics does not bound an unobserved field component: trajectories (0,h) and (0,2h) have identical first-coordinate diagnostics but different states. These examples do not invalidate measured agreement; they delimit its inference.

An independent issue is that linear interpolation need not preserve a nonlinear relation among diagnostics. For endpoint values c0,A0,c1,A1 and lambda in[0,1], write cbar=(1-lambda)c0+lambda c1 and Abar=(1-lambda)A0+lambda A1. Direct multiplication gives

    cbar Abar-[(1-lambda)c0A0+lambda c1A1]
      =-lambda(1-lambda)(c1-c0)(A1-A0).

In variantA with C=3, canonical slope gauge gives c=-2cw and normalized slope A=a/cw, hence cA=-2a. If a is preserved, separately interpolating c and A generally violates this identity even when each endpoint is exact. The independently parsed table records this interpolation term, so such a violation is not misidentified as physical slope drift.

For a numerical report, retain actual step values, log brackets and interpolation weights. Compare state snapshots or dense outputs at the same requested times when claiming state convergence. A changed step that is close to half should be stated as its actual ratio. Large-region spatial convergence, finite projector accuracy, and time integration are separate issues. The unprojected G printed under a rho_tau label is subject to result167 and is not renamed a time derivative here.

The protocol freezes the full-step and requested smaller-step C3 N64 logs, parses their printed real values without importing producer code, and independently reconstructs the specified linear interpolants at0,5,10,15,20. It records both absolute and relative diagnostic discrepancies and brackets, plus the cA interpolation identity. It checks the published rounded table by transcription. This is a reproducibility test of logs, not a rerun or independent verification of the evolved states. No well-posedness, continuum instability, long-time limit or endpoint follows.
