# A local affine-coordinate obstruction to flat detachment

Date:2026-10-20. Status: CONFIRMED by direct calculation. This excludes a local ansatz, not a B2 profile class.

## Exact statement

Let D>0 and let f,g be C3 functions on an interval containing[0,delta), with f(0)=f'(0)=0. On a Cartesian rectangle with x in(0,delta), consider

    W(x,y)=(f(x),(D-f'(x))y+g(x)),
    Omega=partial_y W1-partial_x W2.

Assume the vorticity transport identity

    W.grad Omega+Omega=0

holds throughout that rectangle. There is no such field with f(x) nonzero for every0<x<delta. Consequently this Cartesian ansatz cannot model an immediate smooth detachment from a segment of equilibria by a flat one-sided horizontal velocity. The same conclusion holds with C3 only in the open interval and C2 up to0.

For beta2, this is the vorticity equation in a region of constant temperature. For a general beta with D=2beta it applies in a zero-temperature region. It uses neither a global inverse nor the B2 center jet.

## Complete proof

Direct differentiation gives div W=D and

    Omega=f''(x)y-g'(x).

Therefore

    W.grad Omega+Omega
      =[f f'''+(D+1-f')f'']y-f g''+g f''-g'.

Since this expression is zero on an open y interval, its coefficient of y vanishes:

    f f'''+(D+1-f')f''=0.                         (1)

The derivative of f f''-(f')^2+(D+1)f' is the left side of(1). Thus that expression is constant on(0,delta). By C2 continuity and f(0)=f'(0)=0, the constant is0:

    f f''-(f')^2+(D+1)f'=0.                      (2)

By the nonvanishing hypothesis, division by f^2 is allowed on the entire open interval. Equation(2) says

    (f'/f)'=-(D+1) f'/f^2=(D+1)(1/f)'.

Hence f'/f-(D+1)/f=k for a finite real constant k, so

    f'=D+1+k f.                                 (3)

Let x tend to0 from above. Continuity of f and f' in(3) gives f'(0)=D+1, contradicting f'(0)=0 and D>0. This proves the statement.

The argument permits either sign of f; it never takes log f. The function g cannot remove the obstruction because it enters only the constant coefficient in y. The additional equation for g is f g''-g f''+g'=0, but is not needed for the contradiction.

For comparison, the nonflat solution f(x)=(D+1)x,g=0 gives W=((D+1)x,-y), Omega=0 and div W=D. Its equilibrium has a stable eigenvalue-1. This confirms that the obstruction is to the flat or zero-slope detachment, rather than to every nonzero f.

## Why this does not settle the flat-endpoint problem

A smooth B2 field at a beta2 flat endpoint has div W=4, but need not have W1 independent of the Cartesian coordinate y or W2 affine in y. Straightening the flow or its equilibrium curve by a nonlinear coordinate change does not preserve the Euclidean curl formula used above. Even if a coordinate change preserves area and divergence, the pulled-back velocity one-form contains the metric DX^T DX; its curl is not the formula f''y-g' in arbitrary coordinates. Thus(1) cannot be imposed on a general straightened B2 field.

If this ansatz were instead imposed globally with sublinear V=W-beta X, it would already fail the B2 center strain: at fixed x and |y| tending to infinity, V2/y=beta-f'(x) must tend to0. It follows that f'=beta everywhere, hence the horizontal strain at the marked center is0. The local lemma is recorded only to test a proposed local counterexample construction. It is not a new broad nonexistence theorem, and it supplies no unique continuation theorem for the true flat-endpoint geometry.

## Dependencies and verification

Only Cartesian differentiation, comparison of polynomial coefficients and integration of an ordinary derivative are used. The informal proof was written before the symbolic verification. The exact symbolic checks are recorded in verification/; no formal proof assistant is used. A separate actual Claude Opus5.5 request76 asks about this ODE and the finite-time analyticity scope issue. Its result must be recorded independently and is not presumed here.
