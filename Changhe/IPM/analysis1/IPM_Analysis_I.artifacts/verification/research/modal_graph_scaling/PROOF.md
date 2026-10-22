# The scaling vector of the exact modal trial in the weighted graph domain

2026-10-21. This note concerns the exact, normalized modal trial of research/modal_repair/PROOF.md. It does not concern the literal unjoined floating coefficient formulas or an unknown exact IPM profile.

## Statement and definition of the domain

Let rho be that exact modal trial, with k,L and the finite spline, inner and outer data fixed by data_exact/modal_v2.json and the dependent coefficients defined by the exact join and strain equations. Its canonical velocity is U, its exponent is c_l=1/k, its residual is epsilon=(c_l X+U) dot grad rho-rho, and E=X dot grad. Let X be the weighted weak H1 space defined in research/graph_center_norm/PROOF.md, with this same k,L. Write Sigma(h)=psi[h]_xy(0), and

    Lh=(c_l X+U) dot grad h-h+U[h] dot grad rho+(Sigma(h)/3)E rho.

Define D to consist of the even-x, odd-y perturbations h that are locally C^{2,alpha} for some alpha>0, have a continuous even-even factor h=x^2 y b near zero, satisfy the sublinear density and first-derivative growth condition, possess the specified canonical velocity and finite central strain, and satisfy h,Lh in X. Take the real linear domain formed by these functions. The condition some alpha>0 is stable under finite sums by using the smaller exponent. No completeness, closedness or Fredholm property is claimed for D.

Then the actual trial scaling vector

    K=rho-E rho

belongs to D, with

    J(K)=-2,  Sigma(K)=0,  U[K]=U-E U,
    LK=epsilon-E epsilon.                                 (1)

All quantities in(1) are actual functions for this exact trial. In particular K is a nonzero X class. The bump functions used in graph_center_norm also belong to D. Therefore imposing J=0 on D intersect ker Sigma cannot improve an estimate ||h||_X<=C||Lh||_X, and any such finite C must satisfy

    ||K||_X <= C ||epsilon-E epsilon||_X.                  (2)

If the right-hand image norm were zero, no such estimate could hold. No zero image or numerical value of either norm is asserted here. If the image norm is positive, division gives only a necessary lower bound on C. Equation(1) does not make the trial stationary.

The leading far coefficient of K is (1-k)Theta, where rho=r^k Theta(theta)+O(r^(2k-1)). The actual Theta is nonzero. Thus K does not belong to any perturbation class that fixes the entire leading r^k coefficient, or that requires h=o(r^k) uniformly in angle. This statement does not identify any computed retained numerical vector with K.

## Regularity and end bounds of the modal definition

All joins in this proof are the exact C6 joins of modal_repair. Inside the middle annulus the finite degree-seven B-splines with simple knots are C6. At the inner end the nonconstant core terms in rho have homogeneous degrees5,7,...,17, multiplied by smooth functions on the unit circle. A homogeneous term of degree d with a smooth angular factor is C^{d-1,1} at zero when d is a positive integer: its derivatives through d-1 extend continuously, and the derivatives of order d are bounded away from zero. Integrating along a segment, split at the origin if necessary, proves Lipschitz continuity of derivatives of order d-1. This statement does not assert that the homogeneous term is a polynomial.

The inner logarithmic terms in rho have degree bi+3, with bi>4 and a polynomial of degree at most6 in log r. Their derivatives through order5 are bounded by constants times r^(bi-2)(1+|log r|^6), which tend to zero. Lower derivatives have still larger powers. Thus rho is locally C^{4,alpha} for every alpha<1, with near-center bounds

    rho=x^2 y+O(r^5),
    D^j(rho-x^2 y)=O(r^(5-j)), 0<=j<=3.                 (3)

The logarithmic terms can be absorbed into these particular powers because bi+3>7. The finite angular derivatives enter finite constants. Moreover the center factor a has a=1+O(r^2) and E a=O(r^2), uniformly in angle. Neither assertion requires a to be C2 at the center.

In the exterior region the exact definition is a finite sum of powers and powers times log polynomials. The leading exponent in the density is k. Every other power is strictly smaller than k; the finite exact exponent inequalities give the sharper O(r^(2k-1)) remainder after any fixed number of derivatives. Consequently

    D^j rho=O(r^(k-j)), 0<=j<=3,
    rho=r^k Theta(theta)+O(r^(2k-1)),                    (4)

with differentiated versions of the second expression. The finite input audit checks 0<k<1/2, bi>4, bo>4-2k, alpha_q<=2k-4 for q>0, and simple knots. These give all exponent comparisons used here. The dependent scalar changes only the leading mode-zero coefficient and the exact outer join correction; it does not change an exponent.

## Canonical velocity and its derivatives

The canonical kernel construction in trial_regularities and modal_repair gives the unique sublinear velocity. Local Schauder regularity applied to

    -Delta U1=-rho_xy,  -Delta U2=rho_xx

gives U in C^{4,alpha}_loc from rho in C^{4,alpha}_loc. Only C2 local regularity is needed to evaluate the center derivative in(1).

For clarity the far derivative bounds can also be read directly from the finite Green modes, without differentiating a mere big-O assertion. Write each exterior density mode as a finite sum c r^p(log r)^j with p<=k. The top exponent p=k has j=0. The source derivative has powers p-1, and a radial stream particular solution has powers p+1 with a finite log polynomial. A resonance with the growing homogeneous mode r^n would require p+1=n. It cannot occur, since p+1<=k+1<2<=n. A resonance with the decaying mode r^(-n) can only introduce one extra log factor at p=-n-1<k. Constants supplied by interior integration multiply the decaying stream mode r^(-n). There are finitely many n, all even and at least2. Termwise differentiation therefore gives

    D^j U=O(r^(k-j)), 0<=j<=3.                            (5)

Any logarithm attached to a strictly smaller power is absorbed in r^k. All source and velocity parity conventions are those of the fixed canonical inverse. No growing homogeneous stream term or affine strain is added.

## Membership and center trace of K

From the factor formula, K=x^2 y(-2a-Ea). The preceding center bounds give a continuous even-even factor with value-2. The local regularity is C^{3,alpha}, since rho is C^{4,alpha}. In particular K has the required C^{2,alpha} regularity. Equations(3)-(4) give

    |K|+r|grad K|+r^2|D2 K|=O(r^3), r<=1,
    |K|+r|grad K|+r^2|D2 K|=O(r^k), r>=1.                (6)

For the first bound the range away from zero is covered by compactness; similarly for the second near r=1. Thus K has sublinear density and first-derivative growth. With w<=C r^(-6) near zero and w<=C r^(-2k-3) at infinity, the integrands for its squared X norm are bounded by constants times r and r^(-2), respectively. Hence K belongs to X and is nonzero by its center factor.

Set psi_K=2psi-E psi. The commutators Delta E=E Delta+2Delta and partial_x E=E partial_x+partial_x imply

    -Delta psi_K=-E partial_x rho=partial_x K.

Its velocity is U-E U. It has the required parity and, by(5), sublinear growth. Canonical uniqueness therefore identifies it with U[K]. Since U is C2 at zero,

    D(U-E U)(0)=0.

In particular Sigma(K)=-partial_x U[K]_1(0)=0. This does not use differentiability of a dilation curve in an unspecified norm.

The near-center velocity U[K] is C1, vanishes at zero, and is O(r), while its first derivatives are bounded. Together with(3), (6), V=O(r) and DV=O(1), the product rule gives

    |LK|+r|grad LK|=O(r^3), r<=1.

At infinity (4)-(6) give V=O(r), DV=O(1), U[K]=O(r^k), DU[K]=O(r^(k-1)) and hence

    |LK|+r|grad LK|=O(r^k), r>=1.

The rank-one term is zero. These bounds show LK in X by the same radial integrals. All products have weak first derivatives equal to the displayed classical ones, since the exact modal joins and the local C^{3,alpha} regularity of K are sufficient. Thus K belongs to D.

## The exact image identity and the normalization consequence

Using K=rho-E rho, U[K]=U-E U and Sigma(K)=0, expand L K. The product rule E grad rho=grad E rho-grad rho gives

    E epsilon=(c_l X+E U) dot grad rho
               +(c_l X+U) dot(grad E rho-grad rho)-E rho.

Subtracting from epsilon yields exactly L K. This proves(1) as a spatial identity. Both sides belong to X by the estimates just proved. No differentiation of a Banach-space curve is required.

The trial background satisfies all hypotheses of graph_center_norm: (3) implies its center derivative bounds for any alpha<1, (4) implies the exterior derivative bounds, and the canonical local velocity is C1 with V(0)=0. Its constants A,B,D exist, but no usable numerical values are claimed. The compact C5 bumps and their linearized images are therefore in X and obey the remaining kinematic requirements of D. Applying FIXED_STRAIN.md to K gives K_delta=K+2b_delta with J(K_delta)=Sigma(K_delta)=0, converging to K in graph norm. Passing to the limit in an assumed inequality proves(2).

Finally E(r^k Theta)=k r^k Theta, so (4) gives K=(1-k)r^k Theta+O(r^(2k-1)). The leading angular factor Theta is nonzero: the exact scalar audit encloses the correction of the stored leading A_00, and their sum is bounded away from zero by exact arithmetic. Multiplication by cos^2(theta)sin(theta) cannot annihilate a nonzero finite cosine polynomial on the whole circle. Since k<1, the leading coefficient of K is nonzero. This excludes K from the stated fixed-leading-coefficient or uniformly smaller-growth classes, without asserting anything about a numerical projection onto such classes.

## Verification and limits

The proof precedes new computation. Recheck the exact scalar, spline and exponent input conditions and inherited file hashes. Independently reconstruct the spatial differential identity and Poisson commutators with symbolic derivatives and exact polynomial-jet algebra. Record the nonzero leading coefficient using both rational decimal and independent hexadecimal input decoding. Request actual Opus5.5 review of membership, center trace, far differentiation and the distinction between the maximal weighted graph domain and fixed-tail domains. No actual kernel, quantitative inverse lower bound, nonlinear closure or PDE endpoint is established.
