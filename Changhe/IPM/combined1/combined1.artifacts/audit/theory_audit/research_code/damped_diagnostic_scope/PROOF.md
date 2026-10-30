# What damped least-squares diagnostics certify

## Statement and setting

Let H be a real Hilbert space, f in H, and J:R^d -> H a bounded linear map on an already admissible tangent space. The unregularized linearized residual floor is m=inf_z ||f+Jz||_H. Let G be any positive definite coefficient metric. For lambda>0 the damped step z_lambda minimizes ||f+Jz||_H^2+lambda z^T G z. A finite list of computed damped residuals gives upper bounds on m if they are evaluated rigorously in H. It does not itself give a positive lower bound on m, a certified bracket for an undamped step, or a conclusion about optimization in every basis. Floating or mesh-only diagnostics do not become rigorous Hilbert-space bounds.

## Exact counterexamples

For H=R, f=-1, Jz=z and G=1, the damped minimizer is z_lambda=1/(1+lambda), obtained by differentiating the strictly convex quadratic. The undamped solution is z_0=1. For any two positive damping parameters both damped steps are strictly below1, so their interval does not bracket the undamped solution. Their positive residuals lambda/(1+lambda) likewise fail to bracket the exact residual floor0. This refutes the unrestricted claim that two damping parameters bracket the answer.

The same scalar example with Jz=epsilon z has

    z_lambda=epsilon/(epsilon^2+lambda),
    ||f+Jz_lambda||=lambda/(epsilon^2+lambda),
    m=0,
    |J^T f|=epsilon.

For any finite set of fixed positive lambda, all residuals tend to1 and the reduced gradient tends to zero as epsilon tends to zero, although the attainable residual floor remains0. Thus a plateau and a small gradient alone do not establish a positive floor. These examples make a logical point about available evidence; they do not determine the actual minimum for candidate007.

For every computed z, the elementary inequality m<=||f+Jz|| gives the direction of inference. A candidate yielding residual0.338 supplies an upper estimate for a minimum, not a lower estimate of0.338. With unverified quadrature it supplies a floating diagnostic only. A lower bound on the norm of an exact Newton solution Jz=-f is a different assertion: that equation has residual0, whereas a damped residual0.338 is nonzero. A theorem requiring Jz=-f cannot be applied as an equation to the damped step.

## Certificates that could establish a lower bound

If y in H is nonzero and J^*y=0, then for every z,

    ||f+Jz||_H >= |<f,y>|/||y||_H.

This follows by taking the inner product with y and applying Cauchy-Schwarz. If instead z^T G z<=R^2, the exact identity

    <f+Jz,y>=<f,y>+z^T J^*y

and the G-weighted Cauchy-Schwarz inequality give

    ||f+Jz||_H >= (|<f,y>|-R ||G^(-1/2)J^*y||)_+ / ||y||_H.

These are explicit useful alternatives to a plateau inference. For an unbounded coefficient domain, a merely small J^*y is not enough, since its pairing with z can grow without bound. For an affine tangent z=z_part+Kq, replace f by f+Jz_part and J by JK; use a positive metric on q or work on the quotient where it is positive.

To use these certificates for whole-plane IPM, H and all inner products must be the chosen continuous residual space, with every origin and far-field term included. A normal matrix computed on a finite mesh certifies neither the continuous null condition nor the continuous norm. A dual witness made from the already audited weak probes is one possible route for a bounded physical-radius assertion. This is a suggested check, not a claim that such a witness has been computed.

## Application to numerics_v07

Section2 calls the sampled0.338 residual a floor of the whole007 span, says the obstruction is the span rather than the objective, and says two Euclidean damping values bracket the floating answer. None of these universal or bracketing inferences follows from the displayed steps. Section4 correctly leaves a conditioning stall unresolved; section2 and the summary should use the same qualification. The stated near-null physical spectrum is also floating evidence, as that section acknowledges.

The existing exact weak-distance theorem independently gives a norm lower bound for every exact Newton correction, regardless of basis. It already excludes the registered small exact-Newton balls. This conclusion does not require calling0.338 a certified residual minimum, and it says nothing about whether the current generator span can achieve a smaller nonzero residual with a larger correction. The current failed optimizer does not prove that the inner functions cannot affect any field beyond r=20. The design experiments and genuine held-out checks should be reported as such.

Dependencies: elementary finite-dimensional quadratic minimization, Hilbert-space Cauchy-Schwarz, and the frozen numerical report for the statements under review. The argument introduces no numerical proof of a candidate property.
