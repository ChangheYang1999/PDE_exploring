# Adding the cubic coefficient to a nonclosable graph norm

## Exact spaces and conclusion

Fix the strict scaled Holder space Z=Z_(alpha,beta,gamma) and actual closed operator A0:D_Z->Z of proof 222, with 0<alpha<1, 2k-1<beta<k and gamma>4k. Define

 S={h in C_c^infinity: h is even in x, odd in y,
                         h(0,y)=0 for all y, c[h]=0}.

All elements of S belong to D_Z. Give S the actual graph norm ||h||G=||h||Z+||A0h||Z. Let G_sm be its closure in D_Z with this norm. This is a Banach space of functions. No assertion G_sm=D_Z intersect ker c is made.

On S let J(h) be the coefficient of x^2y at0. Define the stronger norm

 ||h||G,J=||h||G+|J(h)|.

The abstract Banach completion of S in this norm is isometrically G_sm direct-sum R with its sum norm, under the map h -> (h,J(h)). The natural projection of that completion to functions in G_sm has kernel exactly {0} direct-sum R. In particular it is not an injective realization as functions.

The bounded extension of h -> A0h from this stronger completion to Z is (g,j) -> A0g. It has the entire one-dimensional scalar factor in its kernel. Thus merely adding |J| to the nonclosable graph norm and completing cannot create a stronger Banach function domain with a genuine cubic coefficient, or produce an injective inverse problem with the same target. This concerns this particular completion construction, not every stronger norm controlling an actual local trace.

The completion of S intersect ker J in the original graph norm is G_sm. Requiring the scalar coordinate j=0 in the augmented completion likewise projects onto all of G_sm. Neither operation imposes the physical jet J(g)=0 on every function that results. Indeed it includes smooth g whose actual cubic coefficient is1.

## Domain membership and the small normalization packets

A compact smooth parity-compatible h vanishing on x=0 factors smoothly as x^2 times a smooth function, and also vanishes on y=0. Its E2 norm is finite. The compact annular and weighted factors of Z are finite. The actual field V is C1 with sufficient local Holder derivatives, is odd in x in its first component and odd in y in its second, and its quotient V1/x is locally Holder. Therefore

 (V.grad h)/x^2=(V1/x)(h_x/x)+V2(h_y/x^2)

has the required compact divided vertical Holder regularity. The ordinary horizontal estimate follows by the product rule and the actual local coefficient regularity. Thus Th is compact with finite Z norm. Boundedness of C0 proves h in D_Z and complete image membership. In particular S is a vector subspace of the actual maximal domain.

Topics204/222 give an explicit sequence k_epsilon in S with

 J(k_epsilon)=1,
 ||k_epsilon||Z+||A0 k_epsilon||Z ->0.             (1)

For completeness, take H(X)=x^2y chi(X) with chi radial smooth compact and1 near0, and h_epsilon(X)=epsilon^3 H(X/epsilon). The weighted vertical seminorm scales as epsilon^(1-alpha), the horizontal seminorm as epsilon^(3-alpha), and the supremum as epsilon^3. The actual transport applied to h_epsilon has the same bounded rescaled cofactor and hence graph-small order epsilon^(1-alpha). Its support is compact. Since c[h_epsilon]=epsilon^2 c[H], subtract epsilon^2 c[H]q, where q is a fixed compact smooth annular input with J(q)=0,c[q]=1. The result is k_epsilon. Its strain is zero and its cubic coefficient is1 exactly. Boundedness of the complete C0 on Z gives (1), including the nonlocal images. This is a sequence in S, not only a formal jet assignment.

Because A0 is closed, a Cauchy sequence in its graph has a unique limiting function and image. Thus G_sm is a closed subspace of the actual graph, hence Banach. The bounded strain remains zero there. This does not use density in the larger maximal graph; proof 211 separately shows why such a density assertion would be false in the earlier large Holder realization.

## Completion as a product and its kernel

The linear map

 i:S -> G_sm direct-sum R, i(h)=(h,J(h))

is an isometry for ||.||G,J. It suffices to show its image is dense in the displayed product. Given g in G_sm and j in R, choose h_n in S with ||h_n-g||G ->0. For each n use (1) to select a packet k_n with

 J(k_n)=1,
 ||k_n||G <=1/[n(1+|j-J(h_n)|)].

No bound on J(h_n) is needed. Set

 v_n=h_n+(j-J(h_n))k_n.

Then v_n belongs to S, J(v_n)=j exactly, and ||v_n-g||G <=||h_n-g||G+1/n ->0. Hence i(v_n) tends to (g,j) in the sum norm. This proves density and identifies the abstract completion isometrically with the entire product.

The natural map to functions is the first projection (g,j) -> g, whose kernel is exactly (0,R). In particular k_epsilon, viewed in the stronger completion, tends to the nonzero element (0,1), even though the underlying functions and their actual operator images tend to0. This is the precise obstruction to treating the completion as an injective stronger function space.

On S the map h -> A0h is bounded by the graph norm. Its extension on the product is (g,j) -> A0g: this follows from graph convergence in the construction above and uniqueness of the continuous extension. Every (0,j) is in its kernel. Adding a scalar target condition j=j0 would determine that abstract label, but it would not prove that the function g has cubic coefficient j0.

Taking j=0 in the same approximation shows S intersect ker J is graph-dense in G_sm. In particular fix k_* in S with J(k_*)=1. The sequence k_*-k_epsilon belongs to S intersect ker J and tends to k_* in graph norm. Its limiting function has actual cubic coefficient1. The failure is therefore concrete even on a smooth limiting function.

## The exact image cubic coefficient supplies no missing scalar equation

One might instead try to recover the label from the cubic coefficient of the operator image. For every smooth compact physical-parity input h vanishing on x=0, including those with nonzero c[h], the actual full expression has a cubic jet and

 J(A0h)=0.                                             (2)

Here the ordinary jet exists because rho0 is C^(4,1) near0, the canonical velocity of a compact smooth input is smooth, and the actual columns have the corresponding divided origin expansion. The background has J(rho0)=1 and exact 3ell-c[rho0]=1. Its transport linear part is diag(ell-c[rho0],ell+c[rho0]). Consequently

 J(Th)=(3ell-c[rho0]-1)J(h)=0.

The canonical velocity has linear part c[h](-x,y). Acting on the leading x^2y of rho0 gives -c[h]x^2y, so

 J(U[h].grad rho0)=-c[h].

The exact moving-tail column has J(M0)=1. To see its scalar normalization directly, zeta vanishes near0, so only U[zeta].grad rho0 contributes to J(Lfix zeta), with coefficient -c[zeta]. Since n'_0=3-c[zeta] and M0=(X.grad rho0+Lfix zeta)/n'_0,

 J(M0)=(3-c[zeta])/n'_0=1.

The two coupling coefficients therefore cancel exactly. This proves (2), independent of J(h). On the zero-strain core S each coupling term already has zero cubic coefficient. Appending the ordinary image jet where it is defined consequently gives no estimate controlling J(h) and does not remove the invisible scalar in the completion above.

## Scope

This result formalizes the graph-norm repair obstruction rather than asserting failure of the unaugmented A0 inverse on Z. It does not exclude norms controlling additional actual derivatives, divided cofactors, a genuine jet remainder or a Sobolev trace. It does not claim smooth density in the full maximal graph, and it does not identify the abstract completion's extra scalar with an additional physical density degree of freedom. A valid normalized function-space theorem must supply an injective domain and a closed, physically defined normalization, not only a labelled completion.

Dependencies: topics01/217 for the exact normalization identity and moving-tail column; topics204/222 for the actual graph-small exact zero-strain packets; proof 33 for origin regularity. The completion, domain-membership, image-jet and kernel arguments are proved above. No computation, numerical claim or global inverse conclusion is used.
