# Conditional attribution of a finite-difference discrepancy

## Statement and notation

Let h > 0, and let f be a real function on [-2h, 2h]. Define

D2_h f = (f(h) - f(-h))/(2h),

D4_h f = (-f(2h) + 8f(h) - 8f(-h) + f(-2h))/(12h).

Let d be a proposed value of f'(0). Suppose the saved function values are f_hat(t) = f(t) + e_t at t in {-2h, -h, h, 2h}, with |e_t| <= epsilon. In this statement the subsequent linear combinations and divisions are exact. Errors in that arithmetic must be added separately when the statement is applied to machine calculations.

If f is C^3 and |f'''(t)| <= M3 throughout [-h, h], then

|D2_h f_hat - f'(0)| <= M3 h^2/6 + epsilon/h.

If f is C^5 and |f^(5)(t)| <= M5 throughout [-2h, 2h], then the sufficient, non-sharp bound

|D4_h f_hat - f'(0)| <= M5 h^4/18 + 3 epsilon/(2h)

holds. Consequently

|d - f'(0)| <= |d - D4_h f_hat| + M5 h^4/18 + 3 epsilon/(2h).

A small value of the first term alone is not this bound. It is evidence for accuracy only subject to additional information about the other terms.

For the leading Taylor coefficients, if f is C^5, then

D2_h f = f'(0) + f'''(0) h^2/6 + R2,

where |R2| <= M5 h^4/120. If f is C^7 on [-2h, 2h] and |f^(7)(t)| <= M7, then

D4_h f = f'(0) - f^(5)(0) h^4/30 + R4,

where |R4| <= 17 M7 h^6/3780. The constants M5 and M7 here bound the indicated derivatives on the relevant intervals. A ratio of about 100 or 10000 per decade can be consistent with these leading terms, but the observed ratio by itself does not supply the derivative bounds.

## Proof

Taylor expansion through degree two at h and -h has remainders at most M3 h^3/6. The even terms cancel on subtraction. Division by 2h gives the first truncation bound. The perturbation numerator is e_h - e_-h, of absolute value at most 2 epsilon, giving epsilon/h.

For the five-point formula, Taylor expansion through degree four cancels the constant, quadratic, cubic and quartic terms, and gives coefficient one for f'(0). Each remainder at t is bounded by M5 |t|^5/120. The sum of the absolute weighted remainders, divided by 12h, is at most

M5 h^4 (32 + 8 + 8 + 32)/(120 times 12) = M5 h^4/18.

The absolute stencil coefficients sum to 18, so their perturbation bound is 18 epsilon/(12h). The asserted bound on |d - f'(0)| follows by the triangle inequality.

Expanding the two-point formula through degree four leaves f'''(0) h^2/6. Its two fifth-order remainders give M5 h^4/120. Expanding the five-point formula through degree six leaves the fifth-derivative coefficient (-32 + 8 + 8 - 32)/(120 times 12) = -1/30. Its seventh-order remainders have absolute coefficient (128 + 8 + 8 + 128)/(5040 times 12) = 17/3780. This proves the remaining formulas.

## Exact evaluation of a quadratic cost difference

Let r_plus and r_minus be vectors in R^n, with n a positive integer. Set O(r) = ||r||_2^2/2. Then

O(r_plus) - O(r_minus) = <r_plus + r_minus, r_plus - r_minus>/2.

This follows by expanding the inner product and cancelling the equal cross terms. If the last row of r is a gauge g, let r_m denote the vector of the other n-1 rows and let g0 be the base gauge value. For O_tilde(r,g) = O(r) - (g-g0)^2/2, the same expansion gives

O_tilde(r_plus,g_plus) - O_tilde(r_minus,g_minus)
= <r_m_plus + r_m_minus, r_m_plus - r_m_minus>/2 + g0 (g_plus-g_minus).

Both are exact identities for real input vectors. Applying a high-precision sum to saved floating-point vectors can distinguish cancellation during scalar cost formation from earlier errors in the vectors. It does not bound those earlier errors and does not define a new registered estimator or change any pass rule.

## Dependencies and scope

Dependencies are the Taylor theorem with bounded derivative remainder, the triangle inequality and the Euclidean inner-product identity. No claim about derivative bounds or function-evaluation error for S11 follows from this proof. In particular, finite observations under a qualitative smoothness assumption are not certified numerical bounds. No formal proof or Lean/Lake build is attempted. Verification records are kept alongside this proof in verification/ and in the chronological verification record.

## Why an evaluation-error assumption is necessary

Fix H > 0 and a finite set T contained in [-H,H]. Suppose f is C^5 on that interval and saved values y_t satisfy y_t = f(t) + e_t for every t in T. If no bound on e_t is imposed, these observations do not give any finite bound on f'(0). Indeed, for any real delta define f_delta(t) = f(t) + delta t and e_delta,t = e_t - delta t. Then y_t = f_delta(t) + e_delta,t at each saved point, whereas f_delta'(0) = f'(0) + delta. All derivatives of order at least two are unchanged. Thus even a bound on the third and fifth derivatives, without information about evaluation error, does not resolve this ambiguity. The added term is affine and requires no oscillation between observations.

This is an identifiability statement about incomplete error information. It is not a construction of an error in the Euler implementation and is not evidence that its proposed derivative is wrong. An actual bound on e_t restores the quantitative inequalities above.
