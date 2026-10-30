# Signed low-energy and unweighted first-derivative matrix certificates

## Statement and status

Fix the exact d2 potential in ../refit_audit/data/d2_canonical.json, with c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma. Put rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and

A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
M1=I-sym Du+A.

The two numerical targets are

A+(2/25)I >=0, and M1 >=(9/10)I                            (1)

on the entire plane. This document proves the reduction and the validity of a completed certificate. It does not assert (1) before every cell passes. A failed interval enclosure is inconclusive. A negative point value, if separately certified, disproves the corresponding target.

The already independently confirmed d2 Hilbert-Schmidt value is

kappa=0.7104111374799075935225...,

with its exact interval in ../background_sobolev/verification/d2.json. If the first target passes, then theta<=2/25, where

theta=ess sup_X (sqrt(rho_x(X)^2+rho_y(X)^2)-rho_y(X))/2.

Consequently c+1-theta-kappa >= c+1-2/25-kappa >2. The last strict comparison must be enclosed in the final numerical record. The second target is the unweighted first-derivative hypothesis of T4-019. Neither target supplies its remaining background or forcing conditions.

## Exact derivative identities

Write chi_ab=partial_x^a partial_y^b chi. Direct differentiation gives

Du=[[-chi22,-chi13],[chi31,chi22]],
rho_x=-chi31-chi13, rho_y=-chi22-chi04.

It follows that

A+tau I=[[tau-chi22-chi04,(chi31+chi13)/2],
         [(chi31+chi13)/2,tau]],                          (2)

M1-(9/10)I=[[1/10-chi04,chi13],
            [chi13,1/10-chi22]].                         (3)

The least eigenvalue of A is (rho_y-sqrt(rho_x^2+rho_y^2))/2. Thus the first inequality in (1) is exactly the global theta bound. Equations (2)-(3) also show why the previously certified matrix with omega1=(1+r^2)^(-1/10) is a different target: it contains an additional scalar V.grad log omega1.

## Full-plane polynomial representation

Use t=r^2/(1+r^2), z=cos(2theta), w=(1-t)^(delta/2). The exact polynomial reconstruction and its independent equality check are in ../global_matrices/data/independent_d2_polynomials.json.gz and ../global_matrices/verification/reconstruction.json. Each fourth derivative is a sum of w^(j+1) times rational polynomials in t,z. The odd angular fields chi31 and chi13 contain the common factor sin(2theta). Therefore (2)-(3) have diagonal polynomials a,b and off-diagonal sin(2theta) q. The domain [0,1] times[-1,1] covers a quadrant and its limits at the origin and infinity. S1 reflections change only the sign of the off-diagonal; eigenvalues are unchanged.

The polynomial arrays used here were independently derived from the exact potential, not inferred from sampled fields. The earlier derivative and matrix-cover proof establishes their limiting values and their complete-plane interpretation.

## Interval positivity and adaptive coverage

On each rational rectangle, enclose a,b,q by either tensor Bernstein convex-hull bounds with the independent w interval, or by the midpoint degree-six Taylor expansion of w powers with its rigorously bounded remainder. The formulas and proof are in ../global_matrices/PROOF.md. Each method is valid on the complete cell. A lower bound from either can certify it.

If a>=a0, b>=b0 and |q|<=q0, set C=q0 sqrt(1-min_cell |z|^2). Then a valid least-eigenvalue lower bound is

(a0+b0-sqrt((a0-b0)^2+4C^2))/2.

Also min(a0,b0)-C is valid. The larger of valid bounds remains valid. A nonnegative outward-rounded result certifies the cell.

The initial partition is an already checked complete binary cover of [0,1] times[-1,1]. If a cell is inconclusive, replace it by its two equal radial or angular halves. Induction shows that accepted plus pending cells still form a complete partition. At every checkpoint verify the finite binary tree, including absence of duplicate or ancestor leaves. A completed certificate has no pending cells and every accepted leaf has a nonnegative bound. This proves (1) including all cell boundaries. Adaptive choices and execution order affect cost, not validity. No area estimate or numerical sampling replaces coverage.

## Dependencies and scope

Dependencies are the exact d2 coefficient file, the independent fourth-derivative reconstruction, the elementary identities (2)-(3), the Bernstein and Taylor enclosure proof, finite binary-tree induction, and outward Arb arithmetic. There is no Lean certificate in this campaign. Every new numerical bound is N4-ORIGIN until another lane reproduces it independently. Even successful matrix targets leave residual smallness and other background estimates to be verified separately.

## Diagnostic rational-point test for the first-derivative target

An inconclusive rectangle is not a counterexample. To distinguish interval overestimation from failure of the target, select its center in compactified coordinates, map it approximately to a Cartesian point, and round each coordinate to a finite decimal. Treat those decimal coordinates as exact rationals. Evaluate chi04, chi22 and chi13 using independent Cartesian Taylor jets and the radial-Fourier recurrence; require overlapping enclosures. At that point the least eigenvalue of M1 is

1-(chi04+chi22)/2-sqrt((chi04-chi22)^2+4chi13^2)/2.

An outward-rounded upper bound strictly below9/10 refutes the global target. A value above9/10, even for every tested point, does not prove the global target. The floating center selection is only a witness-search heuristic and is not used in the final inequality.

## Relative-radius refinement and continuation

The original absolute-coordinate split rule can waste angular subdivisions near t=1: a tiny interval in t can still produce substantial variation in (1-t)^(delta/2). The continuation therefore compares (b-a)/(1-a) to (d-c)/2 when selecting radial or angular bisection on [a,b] times[c,d]. This changes only the search order. Each accepted old cell retains its original enclosure, and each pending old cell is replaced by a complete subtree. The continuation checks the parent certificate and code hashes, carries its accepted leaves, and checks the complete partition after every step. Its output records the parent hash and the new refinement rule. Consequently the coverage proof above is unchanged.
