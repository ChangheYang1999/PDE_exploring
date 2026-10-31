# Objective recovery does not identify a perturbed field

Status: an exact finite-dimensional statement about what an objective value can establish. It does not determine the distance of any campaign state from its source.

## Statement and hypotheses

Let a > 0. Equip X = R^2 and H = R^2 with the Euclidean norm. Define the smooth residual map r:X -> R^2, the least-squares objective L:X -> R, and the linear field map V:X -> H by

    r(x,y) = (a,x),   L(x,y) = (a^2 + x^2)/2,   V(x,y) = (x,y).

Fix the nonzero reference state z0 = (0,1). For every M >= 0 there is a state zM with

    L(zM) = L(z0) = a^2/2,
    ||V(zM)-V(z0)|| / ||V(z0)|| = M.

Consequently, over smooth least-squares residuals and linear field maps, equality of positive objective values supplies no finite universal upper bound on relative field distance. The same conclusion holds for objective values arbitrarily close to the reference value.

## Proof

Take zM = (0,1+M). Its first coordinate is zero, so substituting in L gives L(zM) = a^2/2 = L(z0). The reference field is (0,1) and has norm one. Their difference is (0,M) and has norm M. This proves the displayed identities. Since M is arbitrary, no finite bound depending only on the two identical objective values can hold over this class. Equal objective values also satisfy every positive tolerance on their difference, proving the last assertion.

## A sufficient additional condition

For a particular reference z0, let A be a set of admissible states. Suppose there is a known C >= 0 for which

    ||V(z)-V(z0)|| <= C ||r(z)-r(z0)||   for all z in A.

Then a measured residual-vector difference gives the stated field-distance bound, and the triangle inequality also gives

    ||V(z)-V(z0)|| <= C (sqrt(2 L(z)) + sqrt(2 L(z0))).

The latter bound is not controlled by the difference L(z)-L(z0). Both conclusions follow by substitution and the triangle inequality. Neither the existence of C nor membership in A follows from a small loss. A quotient by rotations or another declared symmetry needs its own distance and its own bound.

## Application and limits

The F3 producer note at 2026-10-29T23:25:16Z reports an objective decrease from about 1.55e-4 to 2.82e-7 in two accepted steps and describes the perturbation as removed. These objective values support a statement about objective recovery. To establish removal of the field perturbation, compare the saved field at the claimed iteration with the source field on declared common domains, with any allowed rotation specified. The parameter-dependent field map must use each state's actual parameters.

This counterexample is not an Euler representation and does not show that the particular F3 iterate is far from S01. That distance is OPEN until evaluated. No optimizer state is reconstructed from scalar losses, no continuum bound is inferred from a finite quadrature, and no exact solution is asserted.

## Dependencies and evidence

The proof uses only Euclidean norms and direct substitution. The companion perturbation proof establishes how the initial coefficient perturbation is normalized; it gives no estimate for a later optimizer iterate. Numerical evidence and the producer-note binding are in the verification subfolder. No formal proof was run.
