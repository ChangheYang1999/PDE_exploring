# A physical Gram matrix and a sharp center-strain norm

Status: CONFIRMED as an analytic norm and finite-dimensional linear-algebra result. The main proof and exact norm controls were written before execution; post-review clarifications and analytic truncation bounds are explicitly recorded in the model adjudication. The theorem concerns a chosen physical norm and finite-dimensional representations. Numerical quadratures and matrices, when available, are data, not proofs of a continuum inverse theorem or a B2 profile.

## 1. Statement and exact hypotheses

Use fixed physical coordinates X=(x,y), r=|X|. Let G be a measurable function even in x and put Omega=xG. For delta>0 and R>0 define

 w_delta,R(r)=(r/R)^delta+(R/r)^delta,
 ||G||_delta,R^2=integral_R2 w_delta,R(r)|G(X)|^2 dX.                 (1)

The value of the weight at r=0 is immaterial for this Lebesgue norm. If(1) is finite, the full-plane mixed center moment is absolutely convergent and

 c(G)=1/pi integral_R2 x^2 y G(X)/r^4 dX,
 |c(G)|<=1/(4 sqrt(delta)) ||G||_delta,R.                          (2)

The constant is sharp on the class of smooth compactly supported x-even functions whose supports avoid0. It is independent of R. For such smooth compact sources, c(G) is exactly Psi_xy(0) for the ordinary logarithmic full-plane solution -Delta Psi=Omega, without a harmonic addition. For noncompact sources the conclusion is about the moment, and identifies the center strain of a specified inverse only when that inverse has this differentiated kernel. The canonical relative inverse in the B2 setting has this kernel when the ordinary mixed moment is convergent and local smoothness holds.

For the native radial spline representation below, take b,L>0, a positive integer K, a degree d>=0, a nondecreasing clamped knot list 0=t_0<=...<=t_N=1 defining linearly independent normalized B-splines B_j, and a nonempty set of their coefficients retained separately in each angular mode. Nondegenerate B-splines are understood as linearly independent modulo equality almost everywhere; empty mode blocks are omitted. Write

 x=r sin(phi), y=-r cos(phi),
 t=1-[1+(r/L)^2]^(-1/(2b)),
 D=(1-t)^(b+1), rho_even=1, rho_odd=r/sqrt(r^2+L^2),
 G_z(r,phi)=D sum_(k=0)^(K-1) rho_k(r) cos(k phi) sum_j z_kj B_j(t). (3)

Only retained coefficients enter the sums; in the tested representation they are j>=floor(k/2). Let z be their mode-major vector. If

 0<delta<min(2,2/b),                                               (4)

every such field has finite norm(1). Its exact Gram matrix H, defined by ||G_z||^2=z^T H z, is positive definite and block diagonal by angular mode. Set a_0=2 and a_k=1 for k>=1. Its k-th block is

 H_k,ij=pi a_k b L^2 integral_0^1 (1-t) rho_k(t)^2
                                      w_delta,R(r(t)) B_i(t) B_j(t)dt. (5)

The same formula with weight1 is the physical unweighted L2 Gram matrix H0. The exact center functional is c(G_z)=q^Tz, with

 q_kj=-bL/4 (1_{k=1}-1_{k=3}) integral_0^1 B_j(t)dt,
 integral_0^1 B_j(t)dt=(t_(j+d+1)-t_j)/(d+1).                     (6)

Terms for absent modes are zero. In particular

 q^T H^(-1)q <=1/(16 delta).                                      (7)

This is an exact inequality for the integral Gram matrix. A rounded matrix satisfying a numerical version of it is only a consistency check.

For any linear map A on the retained coefficient space and a factorization H=C^T C with C invertible, put

 B=C A C^(-1).                                                    (8)

The largest and smallest singular values of B equal the supremum and infimum, respectively, of ||G_(Az)||_delta,R/||G_z||_delta,R over z!=0. They do not depend on the choice of coefficient coordinates for this same space, map and physical norm. They do depend on the chosen physical norm and finite approximation space. No boundedness or invertibility of a continuum operator follows from a single finite matrix.

## 2. Sharp weighted center moment

The logarithmic fundamental solution is -log|X-Y|/(2pi). Its mixed derivative at X=0 is xy/(pi r^4). Multiplication by Omega=xG gives the first formula in(2). For a smooth compact source the mixed distributional Hessian has no delta term, since the two derivative indices differ. The displayed integrand is O(1/r) near0 if G is bounded; it is locally area-integrable. More explicitly, the mixed derivative is the distributional principal-value integral, and local absolute integrability turns it into the ordinary Lebesgue integral. This fixes the sign without using any fitted inverse matrix. For the canonical relative inverse, write V(X)=integral[K_v(X-Y)-K_v(-Y)]Omega(Y)dY with K_v(Z)=(Z_y,-Z_x)/(2pi|Z|^2). On the region |Y| greater than twice a fixed small observation radius, the derivative kernels are bounded by a constant times1/|Y|^2. Their products with Omega are bounded by a constant times|G(Y)|/|Y|, whose tail integral is finite by the same weighted Cauchy-Schwarz radial estimate used below. Differentiation of that outer integral is therefore justified by domination. The inner source can be cut off smoothly and uses the preceding smooth compact-source calculation. It follows that -partial_x V_x(0)=partial_y V_y(0)=c(G), with no harmonic addition. This proof requires local smoothness for the inner integral; no classical velocity derivative is asserted for a merely measurable G.

In usual polar coordinates x=r cos(theta), y=r sin(theta), the area kernel is

 K(X)=cos(theta)^2 sin(theta)/(pi r).

Weighted Cauchy-Schwarz gives absolute convergence and the sharp possible constant ||K/sqrt(w)||_2. Its squared value is

 1/pi^2 [integral_0^(2pi) cos(theta)^4 sin(theta)^2 dtheta]
         [integral_0^infinity dr/(r((r/R)^delta+(R/r)^delta))].      (9)

The angular integral is3pi/4-5pi/8=pi/8. Put u=(r/R)^delta in the radial integral; dr/r=du/(delta u), so it is

 (1/delta) integral_0^infinity du/(1+u^2)=pi/(2delta).

Consequently(9)=1/(16delta), proving(2). A nonzero scalar multiple of G_*=K/w saturates Cauchy-Schwarz in the weighted Hilbert space. It is even in x. Its weighted squared norm is the finite quantity in(9), although it need not extend smoothly to0. Multiply G_* by smooth radial cutoffs supported in annuli and tending to1 at every r>0, with values between0 and1. The resulting functions are smooth compact x-even functions supported away from0. Dominated convergence in both the norm and the moment shows that their ratios tend to1/(4sqrt(delta)). Hence the constant is sharp on the stated smooth class. These fields do not purport to satisfy the coupled B2 equations or preserve a normalization.

## 3. The native Gram matrix and exact strain row

Angular orthogonality gives integral cos(k phi)cos(l phi)dphi=pi a_k times the Kronecker delta. Different retained radial coefficients in one mode give the radial products in(5). Differentiating the radial relation in(3) yields

 r dr=b L^2(1-t)^(-2b-1)dt.

Multiplying by D^2=(1-t)^(2b+2) leaves exactly bL^2(1-t)dt. Also

 rho_odd(t)^2=1-(1-t)^(2b).

This proves(5). Near0, each spline is bounded, rho<=1 and G_z is bounded. The singular part r^-delta of the weight is integrable in area for delta<2. At infinity D=O(r^(-1-1/b)), the splines are bounded and rho<=1. The exterior weighted radial majorant is r^(delta-1-2/b), integrable for delta<2/b. This proves the sufficient range(4). It does not assert necessity for all masked coefficients or for fields with vanishing leading tails.

For any nonzero z there is a nonzero radial spline in at least one mode. Standard nondegenerate B-splines are locally linearly independent on the positive-length knot intervals. Thus a nonzero combination is a nonzero polynomial on one such interval and is nonzero on an open subinterval inside(0,1); multiplication by the strictly positive D,rho there preserves this. Orthogonality and the positive weight give z^T H z>0. This proves positive definiteness without a numerical eigentest.

For the strain, in the angular convention(3),

 c(G)=-1/pi integral_0^infinity integral_0^(2pi)
                                  sin(phi)^2 cos(phi) G(r,phi)dphi dr.

The identity sin(phi)^2 cos(phi)=(cos(phi)-cos(3phi))/4 selects only k=1,3, with angular integrals pi/4 and-pi/4. Further,

 D rho_odd dr=bL dt.

One obtains c=-bL/4 integral(S_1-S_3)dt. The normalized B-spline integral is the knot span divided by d+1, yielding(6). This standard integral identity also follows by integrating the derivative recurrence for a degree d+1 B-spline, summing successive recurrences and using clamped endpoint values. It remains valid for repeated clamped endpoint knots. For arbitrary knots we assume a valid nondegenerate B-spline basis and omit zero support basis functions; no division by a zero support length is used.

Finally set z=H^-1 q. Then q^Tz=z^THz. If q=0,(7) is immediate. Otherwise applying(2) and dividing by sqrt(q^TH^-1q) gives(7). Equivalently sqrt(q^TH^-1q) is the exact dual norm of the strain row restricted to this finite span, and cannot exceed its full weighted-space dual norm.

The finite-span inequality(7) is strict. Equality for a nonzero strain would force G_z proportional to K/w. Its mode1 amplitude divided by D rho_odd behaves as a nonzero constant times r^(delta-2) near0. This is unbounded under(4), whereas every radial spline is bounded. If q=0, the strict inequality0<1/(16delta) already holds.

## 3a. Independent integral controls

For an unmasked mode0 with every coefficient1, partition of unity gives G=D. Its unweighted squared norm is pi bL^2. The corresponding mode1 field G=D rho cos(phi) has unweighted squared norm pi b^2 L^2/[2(b+1)]. Its strain is -bL/4. These follow either from(5) or directly from u=(r/L)^2 in physical area.

For the weight(1), the two direct physical integrals are, respectively,

 pi L^2 [(L/R)^delta Beta(1+delta/2,1/b-delta/2)
           +(R/L)^delta Beta(1-delta/2,1/b+delta/2)],
 pi L^2/2 [(L/R)^delta Beta(2+delta/2,1/b-delta/2)
           +(R/L)^delta Beta(2-delta/2,1/b+delta/2)].

Here Beta(p,q)=integral_0^infinity u^(p-1)(1+u)^(-p-q)du for p,q>0. In the second case rho^2=u/(1+u) and the angular integral is pi instead of2pi, giving the extra factor1/2. The parameter restrictions(4) give all four positive beta-function arguments. These are exact analytic norm controls, independent of the spline-knot quadrature. The unweighted norms above use weight identically1; they are not the delta-to0 limits of(1). Since w_delta,R tends to2, the displayed weighted norms tend to twice the unweighted values. At every fixed R the weight is even in delta. Inverting L/R at fixed L does not generally preserve these norms.

## 4. Basis invariance, projections and Jacobian interpretation

The norm ratio in the statement equals ||C A z||_2/||C z||_2. Let y=Cz; varying z!=0 varies y!=0, proving the singular-value characterization(8). If z=P eta is any invertible coordinate change, then H_eta=P^T H P and A_eta=P^-1 A P. Their norm ratios are identical; hence their extreme values and all generalized singular values coincide. If Cprime is another factor, Cprime C^-1 is orthogonal, so the two transformed matrices are orthogonally similar. Equivalently the squared singular values are the eigenvalues of H^-1 A^T H A; the Cholesky formulation is preferable for numerical evaluation. A factor C need not be symmetric. A Cholesky factor H=L_c L_c^T gives C=L_c^T. Choosing C=L_c instead would generally give the wrong conjugation.

For a differentiable finite iteration T at an actual fixed point z_*, write J=DT(z_*) and A=J-I. A neutral direction for T is Jv=v, exactly Av=0. The condition ||Av||/||v||=1 alone does not imply neutrality. Also T may include a strain projection onto q^T z=c_*; its differential in the Euclidean coefficient metric is

 P_E=I-q q^T/(q^Tq).

Here and in the projection formulas assume q!=0. A physical change of norm does not replace this implemented projection by the different H-orthogonal projection

 P_H=I-H^-1 q q^T/(q^T H^-1q).

The latter minimizes the change of physical norm, but it defines a different computational map unless the two projections happen to agree. Transform the actual A as in(8) if merely reporting a different norm. Likewise a norm on a constraint tangent space needs the actual map to preserve that space or an explicitly specified output projection; it cannot be silently inferred from the input normalization.

No matrix has been assumed to be a derivative merely because it was formed by differences. In the intended numerical audit, A may be the stored difference matrix minus identity, the base point may have a nonzero iteration defect, and quadrature may only approximate H. In that case all singular values are diagnostics of those finite stored arrays in an approximated physical norm. A derivative-error bound, an actual root, uniform approximation in a complete function space and an invertibility estimate remain separate tasks. Metric error is a separate issue: if an independently established Loewner bracket(1-eta)H<=H_tilde<=(1+eta)H holds with0<=eta<1, every norm ratio changes by factors between sqrt((1-eta)/(1+eta)) and its reciprocal. Taking the singular-value min-max over subspaces proves the same multiplicative bracket for every singular value of the same A in the two metrics. Quadrature refinement alone does not establish this bracket relative to the unknown exact integral H.

For any established matrix perturbation bound ||B-B_true||_2<=epsilon, elementary norm inequalities give sigma_min(B_true)>=sigma_min(B)-epsilon, but no such epsilon is invented from a step comparison.

## 5. Scale, dependencies and computational protocol

R is a fixed physical reference radius, distinct from the representation map scale L. Changing L while representing the same field does not change norm(1); changing R generally does. Under the B2 divided-field dilation G_l(X)=l^-1G(X/l), norm_(delta,lR)(G_l)=norm_(delta,R)(G). With R held fixed the two positive radial weight terms scale by l^delta and l^-delta, so the norm need not be invariant. The sharp strain bound itself is independent of R. This metric controls the strain moment, not every inverse quantity; in particular no claim is made that it bounds the far-field constant C2 considered in P189.

Dependencies: the full-plane mixed kernel proved here and in P191; angular orthogonality; positive integrals and Cauchy-Schwarz; standard normalized B-spline definitions; and finite-dimensional linear algebra. No numerics-lane code will be imported or run. The independent reader is allowed to read its serialized scalar geometry and coefficients. Independent weighted quadrature must resolve both physical endpoints and will retain convergence differences, source hashes and endpoint transformations. An unweighted polynomial control, physical-space polar integration, the exact strain row and the dual inequality are independent checks. Actual Opus5.5 exchange and every availability limitation will be recorded. No formalization or Lean/Lake execution is claimed.

## 6. Analytic bounds for truncated physical norm checks

Suppose the normalized splines are nonnegative and sum to1, with absent coefficients set to0. Set M=sum_k max_j |z_kj|. Then |G_z|<=M D since |cos|,rho<=1. For0<r<=r_lo, D<=1, so the omitted inner squared norm is at most

 2pi M^2 [R^-delta r_lo^(2+delta)/(2+delta)
             +R^delta r_lo^(2-delta)/(2-delta)].

For r>=r_hi, D^2=(1+r^2/L^2)^(-1-1/b)<=L^(2+2/b)r^(-2-2/b). Direct integration gives the omitted outer squared norm at most

 2pi M^2 L^(2+2/b) [R^-delta r_hi^(delta-2/b)/(2/b-delta)
                       +R^delta r_hi^(-delta-2/b)/(delta+2/b)].

All denominators are positive by(4). The corresponding omitted strain is bounded by1/(4sqrt(delta)) times the square root of the relevant bound, by applying(2) to the field restricted to that omitted region. These are analytic truncation bounds; floating evaluations of them and adaptive quadrature error estimates are not interval certificates. They do not bound quadrature or matrix rounding errors.

Publication UTC: 2026-10-21T20:40:44.496558+00:00.
