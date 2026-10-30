# Rational-point audits of background derivative and matrix conditions

## Exact statement

Let chi be an exact finite potential as in ../refit_audit/PROOF.md, rho=-chi_xxy-chi_yyy, U=(-chi_xyy,chi_xxy), c>1, and V=cX+U. At any prescribed nonzero rational point X, repeated exact polynomial differentiation and outward ball evaluation enclose every derivative used below. A ball strictly above a required upper cap, or a ball strictly below a required lower cap, disproves that global pointwise condition for this exact reference. No unsampled point is constrained by a point check.

## Derivative tensors

For a+b=d,

partial_x^a partial_y^b rho = -chi_(a+2,b+1)-chi_(a,b+3),
partial_x^a partial_y^b U_1 = -chi_(a+1,b+2),
partial_x^a partial_y^b U_2 = chi_(a+2,b+1).

The squared ordered tensor norm is the sum of component squares with multiplicity binom(d,a), summing both velocity components when appropriate. Thus the quantities checked for the weighted theorem are

S_U = sqrt(1+r^2) |D^3 U|,
S_3 = (1+r^2) |D^3 rho|,
S_4 = (1+r^2) |D^4 rho|.

Their respective required caps are 16, 32 and 512. These definitions agree with the explicit Euclidean ordered-tensor convention in S1_CLOSURE.md, section 7a. The unrelated component-sum convention of hypothesis B9 is not used here.

## Matrices

Let A=[[rho_y,-rho_x/2],[-rho_x/2,0]]. Direct substitution gives

M11=2c+1-2chi22-chi04, M22=2c+1+chi22, M12=chi31.

The unweighted first-derivative matrix I-sym DU+A has entries 1-chi04, 1-chi22, chi13. For the weighted theorem, this matrix acquires the scalar addition

w1=-(c r^2+X.U)/(5(1+r^2)),

because omega1=(1+r^2)^(-1/10). The second weighted matrix (1+c+V.grad log omega2)I-2sym DV+A has entries

M2_11=1-c+w2+chi22-chi04,
M2_22=1-c+w2-2chi22,
M2_12=(3chi13-chi31)/2,

where w2=16(c r^2+X.U)/(5(1+4r^2)) and omega2=(1+4r^2)^(2/5). For a real symmetric matrix [[a,b],[b,d]], its least eigenvalue is (a+d-sqrt((a-d)^2+4b^2))/2. Evaluation of this formula in outward ball arithmetic gives a rigorous interval.

## Method and dependencies

The derivative recurrence and ball evaluator are derived in ../radial_fourier/PROOF.md. Rational input and polynomial arithmetic are exact. Arb evaluation, including square roots and rational powers of positive radii, is outward enclosing. The current audit recomputes known rational-point failures by a different radial Fourier route from the earlier Cartesian Taylor-jet route; it does not execute the earlier code. Agreement of displayed values is a reproduction check. The actual inequality verdict comes from strict ball comparisons with the cap.

## Scope

A violated derivative cap does not prove that no alternative theorem can apply. A failed matrix condition is specific to its given weight and floor. The audit states those conditions explicitly and does not infer all background hypotheses from finite samples.

## Necessary point tests for the signed low-energy hypothesis

For A=[[rho_y,-rho_x/2],[-rho_x/2,0]], its least eigenvalue is

lambda_min(A) = (rho_y-sqrt(rho_y^2+rho_x^2))/2.

Thus theta=sup_X (|D rho(X)|-rho_y(X))/2 is nonnegative and every point supplies a lower bound for it. In the proposed signed low-energy condition c+1-theta-kappa>=2, a point value theta_X with theta_X+kappa>c-1 disproves that sufficient condition for the stated kappa. If kappa is the structured Hilbert-Schmidt upper bound, this is only a failure of that chosen sufficient bound; a sharper treatment of the nonlocal operator could alter the condition.

The scan evaluates exact derivative polynomials in 512-bit Arb at a finite set of rational points. Rational polynomials are shifted exactly to the closer compactification endpoint before ball conversion. This is the same exact field representation established in the radial_fourier topic. The largest scanned value is a lower bound for the global supremum, not an upper bound. A positive failure is checked again using independent Cartesian Taylor jets at that rational point. No conclusion of global success follows when all scanned points pass.
