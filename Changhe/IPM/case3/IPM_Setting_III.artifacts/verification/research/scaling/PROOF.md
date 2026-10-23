# The y-axis and a global reporting scale

Status: independent analytic verification of SPEC v0 Sections 5.1--5.4. The statement is conditional on an exact primary profile. It does not show that one exists.

## Statement

Assume all hypotheses of ../origin/PROOF.md. Let G(y)=rho(0,y), v(y)=c_l y+U2(0,y), and p=1/c_l. Then for every y>0,

    v(y)>0,  G(y)/a0>0,  G'(y)/a0>0.

There is a finite nonzero K, of the sign of a0, such that

    G(y)=K y^p(1+O(y^(gamma-1))) as y->infinity.

In particular p<=gamma. The length

    L=(K/a0)^(1/(1-p))

is positive and finite for every primary profile. Under the genuine residual scaling rho_lambda(X)=lambda rho(X/lambda), it transforms as L_lambda=lambda L. Hence each scaling orbit has a unique representative with L=1, with no exceptional profiles in the primary class.

## The y-axis argument

The y-axis is invariant by parity. On it the profile equation is vG'=G. The center identity gives v(y)=y+O(y^3), while G(y)=a0 y+O(y^3). Thus v>0 and G has sign a0 for sufficiently small y>0.

If v had a first positive zero y*, choose 0<delta<y* where G(delta)!=0. On [delta,y*) the linear equation gives

    G(y)=G(delta) exp(integral_delta^y 1/v(s)ds).

Its absolute value is at least |G(delta)| because v is positive there. Continuity would give |G(y*)|>=|G(delta)|>0. But v(y*)G'(y*)=G(y*) and finite G'(y*) give G(y*)=0, a contradiction. Thus v has no positive zero. The same formula now holds on every compact interval in (0,infinity) and proves the two sign statements for G and G'.

The canonical bound proved in ../inverse/PROOF.md gives v(y)=c_l y+O(y^gamma). Therefore, for large y,

    1/v(y)-p/y=O(y^(gamma-2)).

This is integrable at infinity. Integrating the logarithmic derivative of G/y^p proves convergence to a finite nonzero K, with the same sign as a0. The tail integral is O(y^(gamma-1)), giving the displayed relative error. Comparing |G(y)| with the assumed O(y^gamma) bound gives p<=gamma.

## Scaling and its exact action

For A,B>0, set rho_new(X)=A rho(BX), psi_new(X)=(A/B)psi(BX), and U_new(X)=A U(BX). Poisson follows by the chain rule. If the original transport RHS is c_rho rho, the transformed equation has c_l,new=AB c_l and c_rho,new=AB c_rho. Indeed its left side is A^2 B times the original left side at BX. Uniqueness of the canonical inverse shows that the transformed velocity is exactly the canonical one; it preserves parity and sublinear growth.

Keeping c_rho=1 forces AB=1. With lambda=A=1/B, c_l and a0 are invariant. More generally

    D^m rho_lambda(X)=lambda^(1-m) D^m rho(X/lambda),
    D^m U_lambda(X)=lambda^(1-m) D^m U(X/lambda),
    D^m psi_lambda(X)=lambda^(2-m) D^m psi(X/lambda).

A density coefficient homogeneous of degree d scales by lambda^(1-d). Thus a coefficient of degree 2j+1 scales by lambda^(-2j), and a far-field coefficient of r^s scales by lambda^(1-s). Whenever the corresponding homogeneous weighted L^q norm is finite,

    || |X|^a D^m rho_lambda ||_q
       =lambda^(a+1-m+2/q) || |X|^a D^m rho ||_q,

with 2/q=0 for q=infinity. For psi replace 1-m by 2-m. Inhomogeneous weights 1+|X| do not have that exact formula, but finiteness of the admissible growth bound is preserved with a changed constant.

In particular K_lambda=lambda^(1-p)K and L_lambda=lambda L. The choice lambda=1/L is unique and attainable for every profile. No assumption about the sign of the density off the y-axis is needed.

The action is free. If a nonzero profile is fixed by some lambda!=1, iterating toward zero and using differentiability gives rho(X)=a0 y for every X. This contradicts sublinear growth with a0!=0. Thus no nontrivial stabilizer is hidden in the representative construction.

For a candidate which need not solve transport exactly, R_lambda(X)=lambda R(X/lambda). Both prompt denominators Nf and Nv transform in the same way. Pointwise residual ratios are invariant at matched points. Homogeneous norm statements follow from the same change of variables.

## Limits of this normalization

This proves a reporting representative for exact primary profiles. An approximate candidate may fail to have a nonzero K or satisfy the axis ODE; those failures must be reported. The exponent 1/(1-p) tends to infinity as c_l decreases to 1, so small relative errors in K/a0 can produce large errors in L. A well-defined analytic normalization can be numerically ill-conditioned.

Fixing a0 or c_l is not justified by this symmetry. A condition on an angular mean at infinity is not the same as the y-axis K condition: the present argument does not prove that such a mean is nonzero for every profile. A local numerical slice must demonstrate transversality and state its coverage.

The orthogonal coordinate symmetries compatible with the fixed vertical coupling are axis reflections with the corresponding density sign for vertical reflection; these act trivially on this parity class. No complete classification of all nonlinear or Lie point transformations is claimed. The absence of further transformations remains OPEN.

## Dependencies

The proof uses the canonical O(r^gamma) velocity estimate, the origin normalization, an elementary scalar ODE, and the chain rule. It does not require a sign condition away from the y-axis, global basin topology, analytic regularity, or numerical evidence.
