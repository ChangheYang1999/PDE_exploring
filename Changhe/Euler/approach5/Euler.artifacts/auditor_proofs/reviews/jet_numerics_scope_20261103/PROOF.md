# Scope of the unconstrained and constrained jet searches

Status: the searched exact polynomial systems remain OPEN at the numerical candidates. The exact branch results already confirmed as A429 are unchanged.

## 1. Objects and claims

The reviewed objects are the numerical addenda of the Lagrangian agent's in the team records, its team notes and the final available refinement and constrained-continuation logs. The relevant searches use c=0.45 and omega=1. The unconstrained seed21 search does not impose the necessary global helicity-free first-jet condition A428. The seed31 search does impose it.

The unconstrained degree7 refinement log ends with residuals

    7.427e-4, 2.432e-4, 7.413e-5, 1.641e-5, 6.887e-6.

The constrained log records residuals1.54e-14,3.38e-14,7.70e-12 at degrees3,4,5, and3.84e-3 after800 evaluations at degree6. These are reported floating-point residual norms, not exact identities or certified root enclosures. No check here reproduces the solver, recomputes its residual or changes those logs. The final log text is retained as an observation with its source hash.

The source correctly labels the searches numerical and explains that stalling is not an inconsistency proof. However, its phrases "formal solutions EXIST", "exactly", "PASS: formal helicity-free jets exist", and "final confirmation needs the residual to reach ~1e-9" need to be replaced by descriptions of approximate candidates and a numerical acceptance tolerance. No positive residual threshold gives mathematical confirmation by itself. Its heading suggesting no universal degree7 obstruction is likewise not an established conclusion.

## 2. Complete elementary obstruction to the inference

For every tolerance tau>0, consider the one-variable polynomial

    F_tau(x)=x^2+tau/2.

It has no real zero because F_tau(x)>=tau/2>0. Nonetheless the sequence

    x_n=sqrt(tau/2) 2^-n

has strictly decreasing positive residuals

    |F_tau(x_n)|=(tau/2)(1+4^-n),

which are below tau for every n>=1 and whose excess over their limit decreases geometrically. Thus a positive tolerance, or a finite history of decreasing residuals, cannot establish existence of a zero even for a polynomial system. Arbitrarily small tau does not change this logical fact. Conversely, failure of one optimization run to locate a zero proves no nonexistence, since the polynomial x^2 has a zero even if the tested sequence stays near1.

This argument refutes only the general inference from optimization residual to proof. It says nothing about whether the specific Euler jet system has a real or complex zero. Such existence remains OPEN until an exact reconstruction, a valid root certificate or an independent existence theorem is supplied. The rank and consistency requirements of an overdetermined jet system must be checked in any such certificate.

## 3. Relation to the exact research question

A429 already proves a degree6 extension and a degree7 obstruction for its specified exact quadratic jet. The unconstrained numerical candidates can suggest a different branch to study but do not refute A429 or prove a universal degree7 obstruction false. Their omission of A428 also prevents them from representing the global helicity-free witness class without an additional check.

Even an exact solution of one finite-degree jet system would only establish that finite-order compatibility. It would not establish a compatible sequence through every order, convergence of a formal series, a local C2 Euler field, or an entire decaying profile. The exact analytic Cauchy construction in LIT116 is a separate type of existence result and explicitly fails Euler; it cannot bridge this gap.

The constrained search's degree6 residual is equally inconclusive in the opposite direction. Its current failure to converge neither excludes exact constrained jets nor proves a local theorem against a global carrier equilibrium. The appropriate next mathematical question is an exact consistency analysis with A428 imposed. This audit launches no computation and makes no inference from hardware runtime or iteration count.

## 4. Verdict and report wording

Report the observed residuals as approximate candidates, record the pass/fail threshold as a numerical criterion only, and keep the exact systems and the degree7 all-data existence question OPEN. A proposed sentence is: "The unconstrained numerical refinement reduced the degree7 residual to6.887e-6. The A428-constrained run reached residual3.84e-3 at degree6. Neither run certifies existence or nonexistence; the exact branch-specific A429 result remains the only applicable proof cited here."

The source labels already prevent these observations from being used as PROVED in the theorem ledger. The wording repairs prevent the surrounding prose from contradicting that policy.
