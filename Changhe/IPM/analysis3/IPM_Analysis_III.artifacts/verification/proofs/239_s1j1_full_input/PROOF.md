# Exact full input Gram of the shifted-junction section

## Statement and scope

Use the original exact binary knot vector and k of proof 198, and the degree-seven coarse B-splines b_i, 0<=i<34, constructed there. Write t=log r, t_minus and t_plus for the first and last knots, and t_J=t_plus+1. Put e_j=2j for 1<=j<=7. The current result concerns the complete 38-dimensional S1J1 input section, all in angular mode m=1 after removal of the vertical-axis cofactor trace. It supplies exact input norms and strain coefficients, including the infinite inner and outer tails. It does not enclose the output Gram, the finite singular values or an infinite-dimensional inverse.

The columns are h_i(r,theta)=2r^3 cos(theta)^4 sin(theta) B_i(t)/s_i, with positive scales s_i interpreted exactly as the binary64 numbers in the frozen S1J1 metadata. Their radial functions, in metadata order, are:

* i=0,...,3: B_i=b_i on [t_minus,t_plus], and B_i=sum_(j=1)^4 D_(ij) exp(e_j(t-t_minus)) for t<t_minus, zero for t>t_plus. The four D_(ij) match derivatives of b_i through order three at t_minus.
* i=4,...,6: writing q=i+1, B_i=exp(e_q(t-t_minus))-sum_(j=1)^4 L_j(e_q)exp(e_j(t-t_minus)) for t<t_minus, zero otherwise, where L_j(z)=product_(1<=l<=4,l!=j)(z-e_l)/(e_j-e_l).
* i=7,...,32: B_i=b_(i-3), extended by zero, so the spline indices are4,...,29.
* i=33,...,37: the five b_q of proof 235, q=i-28=5,...,9, starting at t_J.

All columns belong to the low remainder input and its maximal S1 core graph domain. They are linearly independent. The exact Gram has a33 by33 block and a5 by5 block with zero cross entries. Define lambda(t)=-1/2 for t<0 and27/4 for t>=0. Its entries and strain row are

 G_(il)=K/(s_i s_l) integral exp(lambda(t)t) B_i(t)B_l(t)dt,
 c[h_i]=(3/8)/s_i integral exp(2t)B_i(t)dt,
 K=8 Beta(3/2,1/4).                                             (1)

The integral notation for lambda(t)t denotes the stated piecewise exponent, with no derivative taken at0. Every integral in(1) is finite. The attached original-data code encloses all1444 Gram entries and38 strain coefficients using exact rational spline reconstruction and Arb exponential and Gamma balls. A separate moment formula at higher precision supplies a consistency replay. No numerics-team radial evaluator, spline coefficients, quadrature nodes or assembled matrix enters the reconstruction. Frozen metadata enters only to declare column labels, pairing and binary scales.

## Inner matching and regularity

Let v_(in)=b_i^(n)(t_minus+), 0<=n<=3, for i=0,...,3. The Vandermonde matrix E_(nj)=e_j^n is invertible since e_1,...,e_4 are distinct. Thus the matching system

 sum_j D_(ij)e_j^n=v_(in), 0<=n<=3                         (2)

has unique rational coefficients: the knots and spline jets are rational. Solve it with exact rational elimination, then check every equation exactly. For q=5,6,7 the Lagrange identities sum_j L_j(e_q)e_j^n=e_q^n, 0<=n<=3, prove that the three additional inner powers have zero matching jets. They are therefore C^3 across the inner sphere. The first four extended splines are C^3 there; all interior coarse joins are C^6. At the outer endpoint these splines and the selected pure splines have zero jets through order three. Proof 235 establishes the C^3 outer joins. These conditions give piecewise classical first derivatives without surface distributions.

Near the origin all inner radial functions are O(r^2), with the same fixed cylinder derivative bounds. Thus h_i=O(r^5). Their physical angular expression is 2x^4 y times a polynomial in r^2 on the inner disk, divided by fixed positive powers exp(e_j t_minus). In particular they are smooth at0, have J=0 and zero vertical cofactor trace. In the low input, the radial integrand near t=-infinity is bounded by C exp((4-1/2)t), hence integrable. The lowest exponent in an inner Gram denominator is e_1+e_1-1/2=7/2>0. Their first transport derivatives obey the same radial integrability and angular order four, since the background velocity is tangent to the parity axes. The bounded low remainder coupling of topics43 and48 proves membership of the S1 core image. At infinity the outer columns obey the already checked exponent2k-1 and proof 235's integrability proof. These statements do not assert membership in the separate high space.

To prove independence, restrict a linear relation to(t_minus,t_plus). Its only surviving terms are b_0,...,b_29. These thirty B-splines are independent as a subset of the full coarse basis, forcing coefficients of the first four and the26 pure columns to zero. On t<t_minus the remaining three inner exponential sums have respective unique exponents e_5,e_6,e_7; independence of exponentials forces their coefficients to zero. On t>t_J proof 235 forces the five outer coefficients to zero. The weight is positive almost everywhere, so the full input Gram is positive definite. There is no unproved inference from rounded eigenvalues in this argument.

## Exact block formulas

Let D_i be the seven-component vector of inner exponential coefficients for i=0,...,6, padding the first four with zeros and using coefficient1 at e_(i+1) for i=4,5,6. Set D_i=0 for other indices. On t<t_minus,

 R_inner(i,l)=exp(-t_minus/2) sum_(j,q=1)^7 D_(ij)D_(lq)/(e_j+e_q-1/2),
 C_inner(i)=exp(2t_minus) sum_(j=1)^7 D_(ij)/(2+e_j).          (3)

The substitutions u=t-t_minus and direct integration on(-infinity,0) prove(3), term by term in a finite sum of integrable exponentials. Every denominator is strictly positive. Cancellation is retained exactly in the rational sums.

On the finite interval the spline index is i for i=0,...,3 and i-3 for i=7,...,32. The three pure inner columns have no finite-interval contribution. Cox-de Boor recursion gives exact polynomials of degree seven on each of27 nonzero coarse spans. An independent unit-column de Boor recurrence checks every active polynomial and partition of unity. Split the unique span crossing0. Products have degree at most14 and the moments are precisely those of proof 198:

 M_j(z)=integral_0^1 x^j exp(zx)dx.

At512 bits use the160-term Taylor enclosure with error exp(|z|)|z|^160/(160!(160+j+1)). At640 bits use M_0=(exp(z)-1)/z and M_j=exp(z)/z-j M_(j-1)/z. The exact z values on all pieces are nonzero. Both are rigorous enclosures; the second formula is an algebraic check using the same original inputs, not an independent data source. The lambda=2 moments similarly compute strain. All zero compact-support entries remain exact zeros.

The outer5 by5 block and its strain row are exactly proof 235(2), with no finite truncation at infinity. They may be independently rebuilt from the original k and pair list, and checked against the saved235 enclosure. Since t_J>t_plus, every outer B_i has disjoint support from the other33 functions, proving every off-block Gram entry is exactly zero. Formula(1) follows from the polar area element and the exact angular quotient2 sin(theta), as derived in topics185,198 and235.

## Reproducibility and numerical comparisons

The code checks the original trial hash, the literal pair source, both frozen producer hashes, the complete metadata cell list, all38 labels and angular modes, and equality of scales between the m=0 and m=1 partners. Every scale is then an exact positive rational. The original knot vector reconstructs the spline polynomials independently of the numerics producer. Source files are copied into this topic's evidence; neither originals nor other teams are modified. All calculations run one thread and write only in this team.

If the completed floating input matrix G_float becomes available, apply proof 198's exact-binary whitening test. For an exactly interpreted invertible matrix T, verify interval row-sum bounds e>=||T^T G T-I||_2<1 and d>=||T^T(G_float-G)T||_2. Then

 |v^T(G_float-G)v|<=d/(1-e) v^T G v

for every real v. This compares the declared input norms only. A floating output matrix and accumulation-only error model cannot supply an exact finite operator inverse. Output angular division, radial integration, angular truncation, off-basis residuals and the continuum complement each retain their separate verification requirements.

## Acceptance status

The statement and exact derivation precede computation. Numerical results remain pending until the attached original-data run and replay pass. Dependencies: topics04,43,48,185,198 and235, with235's audit clarifications. No new high-space dimension is claimed here. The five outer high-space dimensions remain exactly those verified in235 and V263.
