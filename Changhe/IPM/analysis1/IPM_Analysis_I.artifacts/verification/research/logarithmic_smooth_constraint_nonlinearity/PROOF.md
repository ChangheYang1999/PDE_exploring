# Smooth finite constraints and quadratic discontinuity

This informal proof is written before the new checks. Its status is OPEN until independent verification, actual Claude Opus 5.5 review and a later adjudication. It extends result211 from linear constraints to regular finite nonlinear constraints. It asserts no decisive PDE endpoint.

## Statement and notation

Use the exactly joined and canonically normalized modal_v2 density rho, ell=1/k, V=ell X+U[rho], and the canonical full-plane sublinear velocity. Write

 Lh=V.grad h-h+U[h].grad rho+(Sigma(h)/3)X.grad rho,
 Q(h)=U[h].grad h+(Sigma(h)/3)X.grad h,
 Sigma(h)=psi[h]_xy(0),  -Delta psi[h]=partial_x h.

For fixed real b and finite s>=0 let Y have norm

 ||h||Y=||exp((1/2-b)z)h(exp z,y)||H^s(R^2_(z,y)),
 ||h||G=||h||Y+||Lh||Y.

The Fourier H^s convention is unitary, with multiplier (1+|xi|^2)^(s/2). Let K be the fixed four reflected open disks of209, whose closures avoid both axes and lie in the smooth punctured inner representation. Put

 E=D_cp={-Delta f: f in C_c^infty(K), f even in x and odd in y}.

Equip this real vector space with ||.||G. It need not be complete and L need not have a closed realization. Each h in E has compact canonical velocity U[h]=(-f_xy,f_xx), all center jets zero and Sigma(h)=0. Thus h,Lh,Q(h) are in Y and supported in K. Containment refers to the potential support, which can exceed the density support. The canonical center normalization J and all far coefficients are zero on E.

Let Omega be a graph-norm open neighborhood of0 in E. Let F:Omega->R^m be continuously Frechet differentiable with respect to ||.||G, F(0)=0, and suppose Lambda=DF(0):E->R^m is surjective. Then there exist z_n^+,z_n^- in Omega, with F(z_n^+)=F(z_n^-)=0, such that

 max(||z_n^+||G,||z_n^-||G)->0,
 liminf max(||Q(z_n^+)||Y,||Q(z_n^-)||Y)>0.          (1)

Consequently Q and h->Lh+Q(h) are discontinuous at0 on this zero set, in its inherited graph topology. On its intersection with every graph ball about0 there is no finite quadratic-bound constant. Constants and sequences may depend on b,s,F and m. No uniformity, stronger domain norm, weaker target, infinite constraint family or singular nonlinear constraint is covered. The case m=0 is included. No inverse or profile existence/nonexistence statement follows.

## Constrained tangent packets and one derivative estimate

Apply211 to the linear map Lambda. Its proof gives g,k_n in kerLambda intersect E with bounded graph norms and

 ||C_g k_n||Y>=c n-C,  c>0,
 C_u v=U[u].grad v+U[v].grad u.                    (2)

More specifically, k_n is a linear combination of finitely many fixed-patch waves h_(i,n), with coefficients of absolute value at most1. Their potentials are n^(-s-2)a_i cos(n phi) on the positive patch and their prescribed parity reflections. The phase satisfies V.grad phi=0 and phi_y>1/2 there. Every amplitude is smooth compact and independent of n.

We need the additional upper estimates

 ||U[k_n]||Y<=C,
 ||partial_x k_n||Y+||partial_y k_n||Y<=C n.        (3)

Here the vector norm can be the sum of its component norms. To check (3), direct differentiation of each potential gives the density

 h_(i,n)=n^(-s)a_i|grad phi|^2 cos(n phi)
   +n^(-s-1)(2grad a_i.grad phi+a_i Delta phi)sin(n phi)
   -n^(-s-2)Delta a_i cos(n phi).

The two velocity components have the same three powers n^(-s-j), j=0,1,2, with fixed smooth compact amplitudes, as explicitly calculated in209 and211 REVIEW_RESPONSE.md. Differentiating either density component in x or y yields fixed amplitudes at powers n^(1-s), n^(-s), n^(-s-1), n^(-s-2). The fixed-chart modulation estimate of209 bounds the Y norm of an amplitude times sin(n phi) or cos(n phi) by C n^s for n>=1. The reflected patches satisfy the same estimate. The triangle inequality and the bounded coefficients of k_n prove (3). This uses no spatial differentiation of the coefficients, which are constants for each n, and no fractional-order orthogonality of different supports.

For every fixed q in E, multiplication by U[q] and by grad q is bounded on Y for functions supported in K: in logarithmic coordinates these are fixed smooth compact coefficients. Consequently (3) implies

 ||C_(k_n) q||Y<=C_q n.                            (4)

This estimate does not assert a bounded bilinear map on all of E. The other argument q is fixed and smooth. For finitely many fixed q_j, a common constant works. All products have compact potential-derived supports, so no nonlocal tail estimate is involved.

## Correcting a tangent point in finitely many directions

Assume first m>=1. Surjectivity supplies q_1,...,q_m in E with Lambda(q_j)=e_j. Define the bounded linear map R:R^m->E by R a=sum_j a_j q_j, so Lambda R=I. Its boundedness follows from the triangle inequality and the fixed finite norms of the q_j, not from a Banach-space inverse theorem.

We show that every sufficiently small y in kerLambda has a correction w(y)=R a(y) satisfying

 F(y+w(y))=0,  |a(y)|<=2|F(y)|=o(||y||G).           (5)

By differentiability at0, F(y)=Lambda y+o(||y||G)=o(||y||G) uniformly as such y tends to0. Continuity of DF at0 gives a radius r>0 such that the graph ball of radius r lies in Omega and

 ||DF(x)R-I||_(R^m->R^m)<=1/2  whenever ||x||G<r.

For small y, all x=y+Ra with |a|<=2|F(y)| are in this ball. On that Euclidean closed ball define

 T_y(a)=a-F(y+Ra).

The derivative of T_y in a has norm at most1/2. Integrating this derivative along line segments in the Euclidean ball gives the same Lipschitz constant. Also |T_y(0)|=|F(y)|. Hence T_y maps the ball of radius2|F(y)| into itself. Iteration starting at0 has successive differences at most2^(-j)|F(y)|; it is Cauchy in the finite-dimensional ball and converges to a fixed point a(y). If F(y)=0, the radius-zero ball gives a(y)=0 directly. The fixed-point equation proves (5). Only a finite-dimensional completeness argument was used. No completeness of E, implicit-function theorem on an incomplete space, or regularity of y->a(y) is needed.

## Size of the nonlinear correction

Let t_n=n^(-1/2), and put y_n^+=t_n(g+k_n), y_n^-=t_n(g-k_n). Both lie in kerLambda and have graph norm O(t_n). Apply (5) to both for sufficiently large n, obtaining coefficient vectors a_n^+,a_n^- with |a_n^+|+|a_n^-|=o(t_n). This follows uniformly from the Frechet remainder, including indices where one y_n is zero. Define

 w_n^+=R a_n^+,  w_n^-=R a_n^-,
 z_n^+=y_n^++w_n^+,  z_n^-=y_n^-+w_n^-.

These belong to Omega intersect E, satisfy the constraints exactly and tend to0 in graph norm. On E, Sigma=0 and U is linear, so

 Q(y+w)-Q(y)=C_y w+Q(w).                            (6)

For a finite combination w=Ra, the fixed products U[q_i].grad q_j give ||Q(w)||Y<=C|a|^2. Equations (4) and the fixed smooth g give

 ||C_(y_n^+) R a||Y+||C_(y_n^-) R a||Y
 <=C t_n n |a|.                                   (7)

The constant absorbs n>=1. With a=a_n^+ or a_n^- as appropriate, (6)-(7) therefore give

 ||Q(z_n^+)-Q(y_n^+)||Y+||Q(z_n^-)-Q(y_n^-)||Y
 <=C t_n n (|a_n^+|+|a_n^-|)
   +C(|a_n^+|^2+|a_n^-|^2)=o(1),                  (8)

because t_n^2 n=1 and a_n^+/t_n,a_n^-/t_n tend to0. Continuous differentiability suffices; no C^2 or quantitative Holder modulus is assumed.

By (2) and polarization, the lower limit of max(||Q(y_n^+)||Y,||Q(y_n^-)||Y) is at least c>0. Equation (8) preserves that lower limit for z_n^+,z_n^-, proving (1) for sufficiently large n. Reindexing the tail supplies a sequence indexed by all positive integers if desired. Only the maximum is bounded below. Since ||Lz_n^+||Y+||Lz_n^-||Y tends to0, the same conclusion holds for Lh+Q(h), the normalized residual difference. Every graph ball contains the sequences eventually, which disproves the stated local quadratic bound.

When m=0, use z_n^+=y_n^+,z_n^-=y_n^- directly from211. There is no finite correction to construct.

## Why the derivative hypothesis matters

Surjectivity cannot be dropped from a general theorem of this form. The map

 F_*(h)=||h||Y^2+||Lh||Y^2 : E->R

is a continuous real quadratic polynomial in the graph norm. Indeed its associated inner product is bounded by ||h||G||v||G, so DF_*(h)v=2(<h,v>Y+<Lh,Lv>Y), its second derivative is constant and every higher derivative is zero. It is thus C^infty, with DF_*(0)=0, but its zero set is exactly {0}. Q is continuous on that zero set. This example proves only that an arbitrary singular nonlinear constraint need not preserve the obstruction; it does not classify singular constraints.

The theorem concerns graph-smooth finite constraints whose derivative at zero is onto. It does not apply merely because a constraint is described as a normalization or a phase condition. Graph differentiability and surjectivity must be proved in each proposed application. The canonical center and far conditions already hold identically on E, and are not being assumed graph-continuous on a larger space.

## Dependencies and verification

The canonical background, compact-potential gauge and fixed-chart all-order Sobolev estimates are those proved in209, including its mandatory addendum, and used in211. Result211 supplies the constrained tangent packets and their bounded coefficients. Equations (3)-(8) and the finite-dimensional contraction are the new argument. Inherited file pins will be freshly rehashed. Two exact algebra methods will reconstruct the quadratic perturbation identities and selected correction/scaling examples. These finite checks cannot prove a statement about every Frechet differentiable map; that statement is established by the argument above. No new interval enclosure, modal norm ceiling or numerical constant is proposed. Actual proof and executed-evidence reviews, resolution of objections and a later own adjudication are required before FINAL.
