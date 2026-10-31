# Reverse-over-reverse directions require a differentiable pullback

## Statement and hypotheses

Let F: R^n -> R^m be continuously differentiable at x, and let v in R^n. A reverse-mode pullback evaluated at an auxiliary cotangent g in R^m is B_x(g) = DF(x)^T g. If the software representation of B_x retains its differentiable dependence on g, the derivative with respect to g of the scalar v^T B_x(g) is DF(x)v. If instead a custom backward implementation returns a detached numerical evaluation of B_x(g), this second differentiation cannot recover that contribution. A system that treats disconnected derivatives as zero returns zero for the detached contribution, even if the first pullback values themselves are correct.

## Argument

Write A = DF(x). Then v^T B_x(g) = v^T A^T g = (Av)^T g. Its derivative with respect to g is Av. Detaching B_x(g) replaces its represented dependence on g by a constant vector b, so the represented scalar is v^T b and has derivative zero with respect to g. This is a statement about the represented computation and does not assert that the mathematical derivative of F is zero. For a sum H(x) + F(x), a retained pullback of H and detached pullback of F yield only DH(x)v on the second reverse pass.

No second derivative of the original mathematical function is needed: the second pass differentiates the pullback with respect to the auxiliary cotangent. It nevertheless requires a graph for that dependence. The first-order reverse derivative of a scalar loss can remain correct without that graph.

## Application under examination

The frozen source wrappers `_SourceDD.backward` and `_SolveDD.backward` invoke `torch.autograd.grad` without `create_graph=True`. The supplementary verifier uses `torch.autograd.functional.jvp`, a reverse-over-reverse construction in the installed environment. The exact source methods will be exercised on small analytic fixtures to test whether the missing cotangent graph removes their contribution. These fixtures do not validate the full Euler model, its pressure accuracy, or any complete-gradient numerical value. The actual worker uses separate forward-mode and closure derivative constructions and must be judged by its own recorded tests.

## Dependencies and scope

The algebra above uses only finite-dimensional differentiation and the stated graph semantics. Evidence for the behavior of the installed software belongs in `verification/`. No formal proof assistant source is claimed. The failed full-grid S01 supplementary result is retained separately; a fixture can diagnose its derivative construction without turning its failed comparisons into passing comparisons.

## Checked software behavior

The 2026-10-29T10:40:34Z fixture record confirms the disconnection on both exact frozen custom wrappers: ten controls pass, first reverse derivatives and true forward rules agree with the analytic fixtures, and reverse-over-reverse returns zero. The full-grid S01 supplementary failure is retained as V253. It is an invalid checker construction, not an independently established production derivative defect.
