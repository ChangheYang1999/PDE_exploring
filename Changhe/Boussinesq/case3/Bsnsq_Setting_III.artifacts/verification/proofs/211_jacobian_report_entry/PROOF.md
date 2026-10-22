# Scope and metric of the saved Jacobian report entry

Written 2026-10-21 before the entry checker. This is an audit of a proposed numerical report paragraph, not an existence proof.

## Statement and definitions

Let z denote the active coefficients of the divided field G=Omega/x at the stored forced state beta=3.0952, lambda=0.989973. The frozen finite array J_h has 1332 rows and columns and was obtained by NUM using forward differences of its fitted inner map with step h=10^(-6). P208 independently evaluated this array and the input metadata. This packet checks that the lead's proposed report entry faithfully states those computations and their limitations.

The coefficient norm is the Euclidean norm of z. The independent physical norm is

 ||z||_H^2 = integral_{R^2} (r^(1/4)+r^(-1/4)) |G_z(X)|^2 dX,
 r=|X|, with the reference length R=1.

It is a norm of G, not Omega, on this finite space. Let H be its Gram matrix and H=C^T C. Both input and output use the same norm. The singular values quoted for the physical metric are the Euclidean singular values of C(J_h-I)C^(-1). Values rounded from the P208 computation are sigma_min=0.034 and condition253 in coefficient space; sigma_min=0.015 and condition2111 in this specified physical norm; spectral radius of J_h=0.43. The calculated mismatch-derivative diagnostics are2.87 in lambda and2.1e-4 in beta. These are measured floating-point array quantities. No singular-value enclosure for an exact derivative is asserted.

## Norm transformation

For any coefficient vector v, ||v||_H=||Cv||_2. Write u=Cv. Then ||(J_h-I)v||_H/||v||_H = ||C(J_h-I)C^(-1)u||_2/||u||_2. Taking its infimum and supremum over nonzero u proves the claimed metric transformation. Changing from G to Omega changes the Gram matrix and generally changes the singular values. The reference length and radial weight must therefore be specified for a reproducible report.

The spectral radius is invariant under this similarity transformation, since det(tI-CJ_hC^(-1))=det(C(tI-J_h)C^(-1))=det(tI-J_h). It does not equal an arbitrary induced operator norm. In particular a matrix can have all eigenvalues inside the unit disk and yet enlarge some vectors in a given norm. Thus the measured spectral radius alone does not certify a contraction in the stated coefficient or physical metric.

## Conditional branch derivative and missing hypotheses

If an exact differentiable map T(z,p) has an exact fixed point z(p), differentiating T(z(p),p)=z(p) gives (I-D_z T)z_p=D_p T. When I-D_z T is invertible, the local implicit-function theorem supplies the corresponding local branch under its hypotheses. If the scalar mismatch is m(z,beta,lambda)=q(beta)^T z+lambda c_f-1-beta/2, its branch derivatives at a fixed source are

 m_lambda=q^T z_lambda+c_f,
 m_beta=(d_beta q)^T z+q^T z_beta-1/2.

Substitution of J_h and sampled parameter columns produces linearized diagnostics. This algebra neither establishes an exact fixed point nor a bound on the exact derivative. It consequently does not establish an exact differentiable branch, a fold, or error bars for m.

A small defect and a small Newton correction are also insufficient without nonlinear control. For epsilon>0, T_epsilon(x)=epsilon+x^2/epsilon has T_epsilon(0)-0=epsilon, T_epsilon'(0)=0 and Newton correction epsilon for T_epsilon(x)-x=0. However the fixed-point equation is (x-epsilon/2)^2+3epsilon^2/4=0 after multiplying by epsilon, and has no real root. This counterexample concerns the inference, not the particular NUM map.

## Dates, dependencies and verdict convention

P208's actual saved-array computation began2026-10-21T21:23:15.081605Z and finished21:23:20.262370Z. Additional sensitivity checks, model exchanges and publication continued through21:32:29Z. Its evaluator existed earlier, while the array was unavailable. An entry saying that the frozen-array audit began21:22 does not match the recorded calculation start and should say21:23. NUM's matrix run18:11-to21:22 is consistent with its saved log, rounded to minutes.

The checker will read the actual versioned candidate, the frozen array metadata and the independent P208 diagnostics. Q1 covers numbers and state description, Q2 the limited inference scope, and Q3 dates. A report paragraph can accurately quote diagnostics without turning them into a theorem. A metric clarification and a corrected audit start do not change any numerical result. The full B2 endpoint remains OPEN.
