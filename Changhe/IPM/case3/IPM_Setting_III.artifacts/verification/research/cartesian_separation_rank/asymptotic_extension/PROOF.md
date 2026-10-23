# Asymptotically finite Cartesian rank is also excluded

## Statement and hypotheses

Assume an exact primary IPM Setting III profile rho, with p=1/ell in(0,1), and its already established homogeneous far field h(X)=lim_(R->infinity)R^-p rho(RX). The limit is locally Holder of some exponent alpha>p on the punctured plane, has growth |h(X)|<=C|X|^p, and h(0,1)=K!=0. There are no finite N, factors F_j:R->R and G_j:(0,infinity)->R, and error E such that

    rho(x,y)=sum_(j=1)^N F_j(x)G_j(y)+E(x,y)

outside a fixed disk in y>0, with R^-p E(Rx,Ry)->0 for every fixed x in R and y>0. In particular a uniform error o(|X|^p) is impossible. The same exclusion holds if the representation is only required on y>y0 for a fixed y0>0. No regularity of the factors is assumed.

## Proof

The complete finite-dimensional dilation argument in ../PROOF.md proves that such an h has infinite Cartesian separation rank: any finite-dimensional span of its horizontal sections is dilation invariant, has growth exponent p, and has origin Holder exponent alpha>p, so its functions are constant. Homogeneity would then give h(x,y)=K y^p. This violates the Holder bound at a nonzero point of the horizontal axis.

For a contradiction choose arbitrary N+1 horizontal points x_i and N+1 positive vertical points y_j. For large R every grid point (Rx_i,Ry_j) is in the stated exterior or strip domain. The matrix with entries R^-p[rho(Rx_i,Ry_j)-E(Rx_i,Ry_j)] has rank at most N by its product-sum representation. Its entries tend to h(x_i,y_j), hence its zero determinant tends to det[h(x_i,y_j)]. All such determinants vanish. If the horizontal sections of h spanned dimension above N, N+1 independent sections would have N+1 separating evaluations and a nonzero determinant. Thus h has rank at most N, contradicting the preceding rigidity. This proves all domain versions.

If the exact quotient q=rho/(a y) has finite Cartesian separation rank on y>0 or on a stated exterior domain, multiply each vertical factor by a y to give an excluded finite-rank representation of rho. For an approximate quotient representation one must check that its error multiplied by a y satisfies the density error condition above; no arbitrary unweighted quotient error is asserted to suffice.

## Scope and evidence

This is a proved restricted exclusion, not a full-plane NO endpoint. It uses the proved homogeneous limit, nonzero axis amplitude, and Holder exponent gap. It does not assume an all-order far-field limit, or convergence of the factors. Exact determinant algebra was tested in ../verification/exact_checks.json; the new raywise limit passage is an analytic argument, not a numerical test. It independently confirms the stronger error-term part of the lead's frozen Section3.62.
