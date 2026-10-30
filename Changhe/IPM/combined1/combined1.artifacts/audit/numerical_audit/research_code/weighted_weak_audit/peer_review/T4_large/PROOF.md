# Independent audit of finite large-scale weighted weak probes

## Exact claim and dependencies

Let rho, its canonical velocity u, c, F and the S1 weighted space H_a satisfy every hypothesis of the corrected weighted weak-test theorem in ../weighted_weak_probe/PROOF.md. In particular the correction is at fixed c and the velocity constant C_U is a certified bound on H_a. For any finite list of integers k>=0, that theorem gives a necessary lower bound on ||(1+r^2)^(-a/2)h||_2 from each test phi_k=y t^k(1-t)^2, t=r^2/(1+r^2). The maximum of these bounds is again necessary. There is no restriction on how large a finite integer k may be. This statement asserts neither an optimal scale nor an asymptotic localization theorem.

This audit independently evaluates N4-095's list k=0 and k=2^(2j), 0<=j<=24, for the exact state131 background and a=6/5,13/10,7/5,3/2. The velocity constants are those already independently certified in ../s1_velocity_audit/PROOF.md. Acceptance of the numerical comparisons does not replace the separate required analytic review of the original weighted weak theorem.

## Pairing and background integrals

Use the independently derived polar density and stream function from ../weak_probe_audit/PROOF.md. With z=1-t, their exact form is

    rho=r sum z^((j+1)delta/2) R_(j,n)(t) sin(n theta),
    psi=r^2 sum z^((j+1)delta/2) S_(j,m)(t) sin(m theta).

Let T_(b,d)P=(d-2bt)P+2t(1-t)P'. Put ell_k=3c+1+2ckz-4ct and h_k=1+2kz-4t. Integrating the weak equation against phi_k before differentiating the density gives the linear pairing

    -(pi/2) sum_(j,n=1) integral_0^1
      t^(k+1) z^((j+1)delta/2-1) R_(j,1) ell_k dt.

The nonlinear pairing is

    (pi/4) sum_(i,j,|n-m|=1) integral_0^1
      t^(k+1) z^((i+j+2)delta/2-1)
      R_(i,n) [sign(n-m) m S_(j,m) h_k - T_((j+1)delta/2,2) S_(j,m)] dt.

These identities follow from the sine/cosine product formulas and u=(-psi_y,psi_x). In particular the calculation never imports an assembled residual polynomial from the peer. All angular signs are those verified in the preceding localized weak audit.

The three squared upper-bound coefficients A^2,B^2,C^2 and the gradient bound H are exactly (5)-(7) of the weighted weak theorem. Their polar square coefficients are formed from the density and stream function with all cross terms. Then D=A+B+C_U C and the necessary radius is

    2|pairing|/[D+sqrt(D^2+4 C_U H |pairing|)].

Every squared norm and nonzero pairing must be positively separated from zero by its computed interval before use. No floating-point quadrature or fitted residual is substituted.

## Stable evaluation at arbitrary finite k

For any polynomial P and b>-1, expand P(1-z)=sum p_j z^j. The required integral is

    integral_0^1 t^M (1-t)^b P(t) dt
      =sum_j p_j Beta(b+j+1,M+1),  M>=0.

Euler's beta integral proves this identity term by term, since the sum is finite and both exponents exceed -1. The initial positive value is evaluated as

    exp(logGamma(b+1)+logGamma(M+1)-logGamma(b+M+2)),

and consecutive values follow the exact recurrence

    B_(j+1)=B_j (b+j+1)/(b+j+M+2).

All operations use outward ball arithmetic. This differs from the peer's direct gamma quotient and from the earlier integer product over M: it has no loop of length k. Finite cancellation is enclosed by the interval operations. The log-gamma identity holds on the positive real axis, so no branch ambiguity occurs.

The supremum S(j,b)=(j/(j+b))^j(b/(j+b))^b for j>0, and S(0,b)=1, follows by differentiating t^j(1-t)^b on [0,1]. Thus the same exact gradient bound remains valid for every finite k. Combining it with the already proved weak inequality establishes each lower bound.

## Verification scope

The code records source, helper, proof, peer and velocity-certificate hashes, the exact rational exponents and integers, interval components and real elapsed time. Every one of the peer's104 rows is compared componentwise. Passing comparisons confirms this finite computation. It does not prove an infinite-k limit or close the high inverse hypothesis of any existence theorem.
