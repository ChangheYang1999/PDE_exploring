# Binding clarifications after independent audit

Recorded 2026-10-28T17:06:40.768170+00:00. The independent audit used actual model a separate model instance. Its verdict is PASS WITH REMARKS; no essential gap was found. The verifier read the full audit and replay code and checked all seven findings. The submitted PROOF.md is unchanged. These clarifications form part of its interpretation.

1. Canonical velocity. The proposed stream function psi=v_x is Schwartz, odd in x and odd in y, and solves -Delta psi=partial_x d. It lies in the canonical odd-odd subquadratic class, so uniqueness identifies it with the prescribed stream function. Directly, the far kernel subtraction constants vanish by parity on centered annuli; therefore its kernel and multiplier velocities agree. The strain sign is c=-partial_x U1(0)=partial_y U2(0)=psi_xy(0)=1.

2. The cofactor in the definition of X_s is chi h/(b p), with the fixed near-vertical angular cutoff chi. The uncropped smooth quotient for this particular d has every Sobolev order, so multiplication by chi gives exactly the required membership.

3. Global transport regularity. Write v_c=d/b and u_c=d/(b p). Proof 126 gives the exact identities

       T(b v_c)/b = W.grad v_c + c2 v_c,
       T(b p u_c)/(b p) = W.grad u_c + c1 u_c,
       c1 = 2V1/x + V2/y + q a'/a -1,
       c2 = q(3+a'/a)-1.

The actual coefficients W,c1,c2 belong to W^(7,infinity) on the whole cylinder with the uniform end bounds established in proof 126. Both v_c and u_c lie in H^8 and decay at both ends as proved in PROOF.md. The right-hand sides and the angular-cutoff commutator consequently lie in global H^7. This implies every required order up to sigma=25/4, including the variable bulk order. The cofactor trace remains zero because u_c has a cos^2(theta) factor and W is tangent to the axes. No assumption of C7 across the modal joins is made.

4. The domain of the high moving-tail realization in topics165/167/171 is B_H direct-sum {u in X_s:T u in X_s}. For this d the scalar component is zero. Thus the verified statement T d in X_s is precisely the required maximal high-domain membership. The normalized coupling and m0 are in Y_H by topics123 and167, in the same cutoff convention.

5. The constants in the necessary test have eta_*=eta_H because f_0=F0 at n(ell0)=0, and N4=-n(4). Both tests require the conjunction(I),(S). No high-norm upper estimate, failure of(I) or(S), or inverse is proved.

6. The exact symbolic check is completed. In its historical JSON, J=0 and zero_vertical_cofactor_trace=true are labelled logical consequences, not separate numerical tests: the code directly asserts exact x^4 y divisibility, even quotient powers and minimum physical degree at least5. These identities prove the zero trace and J. The independent audit additionally verifies them by direct symbolic substitutions. No rerun or modification of the accepted certificate is necessary.

7. The independent auditor's exact polynomial and Laurent-mode strain calculation agree with the verifier's polynomial derivative recurrence and Gamma/Beta integration. Its floating quadrature is a consistency observation only and is not used to certify c=1. Both exact routes prove c=1.
