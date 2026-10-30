# Independent coefficient-rounding audit

## Statement and exact objects

Fix c=4076476460239181/2251799813685248. Let chi be the exact potential of C1-N1-007-d2w-j7-e2bal, with its published rational coefficients a_i and its exact single-scale generators. Define b_i to be the exact rational value of binary64 rounding of a_i. Define chi_b using the same exact generators and c with coefficients b_i. This is a precisely defined second mathematical function. It does not include floating-point errors in generator evaluation or a change to c.

The check below certifies the number and maximum size of coefficient changes, their origin-jet effects, the first nonzero far-field residual sector, and two pointwise residual differences. If the certified first nonzero sector of F_b has exponent greater than or equal to -1, then F_b is not in full-plane L2. The exact rational candidate is unaffected by that conclusion.

## Generator conversion and polar identities

Set delta=1-1/c, gamma=1/c, t=r^2/(1+r^2), and u=1-t. A mono generator of indices (j,m,k) has radial polynomial t^(m+k). A Legendre generator (j,m,w,n) has polynomial

    t^(m+w) sum_(k=0)^n (-1)^(n+k) binom(n,k) binom(n+k,k) t^k.

Its potential is (1+r^2)^((3+gamma-j delta)/2) times that polynomial times cos(2m theta). This is the finite Rodrigues expansion, so summing it with a_i or b_i is an exact canonical conversion. Both conversions are compared coefficient by coefficient to independently constructed canonical data.

The previously audited polar differentiation gives finite polynomials R_jn and S_jm such that

    rho = r sum_(j,n) u^((j+1)delta/2) R_jn(t) sin(n theta),
    psi = r^2 sum_(j,m) u^((j+1)delta/2) S_jm(t) sin(m theta),
    u_r = -(1/r) partial_theta psi,   u_theta = partial_r psi.

Here psi=chi_xy and the velocity is (-psi_y,psi_x); rho=-partial_y Delta chi. Every division by t in the derivation is checked exactly. For T_(a,k)P=(k-2at)P+2t(1-t)P', r partial_r of r^k u^a P is r^k u^a T_(a,k)P. These formulas evaluate all point fields by finite rational-polynomial operations and outward real powers.

At the origin smoothness and angular order imply

    rho_y(0)=sum_j R_j1(0),
    partial_y u_2(0)=2 sum_j S_j2(0).

The second identity follows from psi=2(sum S_j2(0))xy+O(r^4). It is the strain normalization used in this campaign. Both identities are checked against the exact canonical metadata before their differences are used.

## Leading far-field coefficient

Write e_j=gamma-j delta. The q=0 homogeneous coefficients of rho and psi are R_jn(1)r^e_j sin(n theta) and S_jm(1)r^(1+e_j) sin(m theta). In F=(cX+u).grad rho-rho, the linear part at index h has coefficient (c e_h-1)R_hn(1). A density index i and stream index j contribute to h=i+j+1. Their angular coefficients are

    sin((n+m)theta): R_in(1) S_jm(1) [-m e_i+n(1+e_j)]/2,
    sin((n-m)theta): R_in(1) S_jm(1) [-m e_i-n(1+e_j)]/2.

Negative sine frequencies are folded with their sign; frequency zero vanishes. This is direct multiplication of the polar velocity and gradient. In particular h=0 vanishes identically because c gamma-1=0. The first possible nonlinear sector is h=1, exponent 2/c-1. Terms with q>=1 have exponent at most gamma-2, strictly below 2/c-1. Thus a nonzero h=1 coefficient is necessarily the leading residual term.

If its sine coefficients are A_n, its full-circle norm is sqrt(pi sum A_n^2). The finite family has a convergent expansion in r^-2 for r>1, with only finitely many j and angular modes. Therefore the remaining terms are o(r^(2/c-1)) uniformly in angle. A nonzero leading coefficient gives an eventual angular L2 lower bound by half this norm times r^(2/c-1). The radial L2 integral diverges because 2/c-1>-1. This establishes nonmembership without treating small coefficients as zero.

## Pointwise conversion error and scope

Let e=rho_b-rho and v=u_b-u. Exact multiplication gives

    F_b-F=(cX+u).grad e+v.grad rho+v.grad e-e.

Evaluate the two exact functions and this identity at (0,1/4) and (100,200), with sufficient outward precision to resolve their differences. Compare each field with the independent Cartesian evaluator. No finite-point test establishes a global error norm. The theorem concerns coefficient rounding only and does not assert which executable used that realization.

## Dependencies and verification

The polar generator identities are independently verified in ../new_candidate_witness/PROOF.md and ../multiscale_generator_audit/PROOF.md. Exact inputs and independent comparison data are in data/ and source/. Code and actual execution evidence are in code/ and verification/. The present proof is an independent audit of the frozen N4 proof, not a new existence theorem.
