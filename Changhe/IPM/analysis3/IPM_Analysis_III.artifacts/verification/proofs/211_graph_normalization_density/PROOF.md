# The exact density statement for cubic normalization

## Statement

Fix 0<alpha<1 and either normalized origin extension L_delta of proof 203, for the joined normalized modal background and a sufficiently small fixed delta. Let

 E2={bounded continuous even-x, odd-y h: h(0,y)=0,
       ||h||E2=||h||infinity+[h]_x+[h]_(y,2)<infinity},
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2)=sup |h(x,y)-h(x,y')|/(|x|^2 |y-y'|^alpha),
 G=D(L_delta), ||h||G=||h||E2+||L_delta h||E2,
 S=C_c^infinity(R2) intersect E2, with both stated parities.

The graph domain is the maximal distributional domain. The exact central strain c is bounded on E2. Define J:S->R by

 J(s)=(1/2) partial_x^2 partial_y s(0).

Then

 closure_G(S intersect ker c intersect ker J)
             =closure_G(S intersect ker c).                       (1)

Thus the cubic constraint gives no additional closed restriction on this particular smooth-domain closure. Equation(1) does not identify that closure with G intersect ker c. In fact, for either of the stated operators there is an h in G intersect ker c and a constant b>0 such that

 inf_(s in S) ||h-s||G >= b.                                      (2)

Consequently the unqualified claim that the smooth cubic kernel is dense in the entire graph intersected with ker c is false. Density in the entire graph is already excluded by continuity and nonvanishing of c. Nonclosability of J on S intersect ker c, proved in proof 204, remains true. No density assertion is needed for that conclusion.

## The exact smooth domain

For a smooth even-x function, h(0,y)=0 implies h=x^2 a with a smooth, by Taylor's integral formula in x. Compactness then makes its weighted y Holder seminorm finite; ordinary compact smooth differences give the remaining E2 norm. Conversely membership in E2 includes h(0,y)=0, so parity alone is insufficient: y chi(r) has the parities but does not belong to E2.

The transport of either origin extension is

 V_delta=(-x A_delta,y D_delta),
 L_delta=V_delta.grad-1+B_delta,

where A_delta,D_delta are bounded C2 coefficients and B_delta is bounded E2->E2 by proof 203. Differentiating x^2 a under this transport preserves the factor x^2 and gives a compact C1 quotient. Hence S lies in G. The graph is Banach because L_delta is closed, and c is continuous for the graph norm because it is continuous on E2.

## Relative density and nonclosability

Proof 204 supplies k_epsilon in S with

 J(k_epsilon)=1, c[k_epsilon]=0,
 ||k_epsilon||G<=C epsilon^(1-alpha)->0.

These properties were established there by exact scaling of x^2 y chi(X/epsilon), the complete transport image and a smooth zero-strain correction. For any fixed s in S intersect ker c, put

 s_epsilon=s-J(s) k_epsilon.

Then s_epsilon lies in S intersect ker c intersect ker J and converges to s in G. This proves that the left-hand set in(1) contains S intersect ker c. Taking closures gives one inclusion, and the reverse follows from containment. This proof gives precisely(1), regardless of whether S is dense in G. The same packets make the closure of the graph of J contain(0,1), which proves nonclosability on its stated domain.

## A graph element that cannot be approximated by smooth inputs

Choose Q=(x0,y0) in the first quadrant, strictly inside B_(delta/4), away from the axes and in the innermost analytic region of the modal state. Such a point exists. In that region the modal functions are finite sums of powers, logarithms and angular functions, hence smooth away from0. The actual transport has V_delta,1=-A0 x+O(r^3), A0>0, so choose Q with V_delta,1(Q) nonzero. The frozen transport plainly has the same property. A small box about Q and its three reflected boxes are disjoint and stay in the smooth region.

Use the local map

 F(s,z)=Flow_s^(V_delta)(x0,y0+z).

Its derivative at(0,0) has columns V_delta(Q) and(0,1), so its determinant is V_delta,1(Q), which is nonzero. Shrinking gives smooth coordinates with

 V_delta.grad s=1, V_delta.grad z=0,
 F(0,z)=(x0,y0+z).                                             (3)

Choose smooth compact cutoffs eta(s),theta(z), both equal1 near0, with support strictly inside this coordinate box. Define there

 u(F(s,z))=eta(s)theta(z)|z|^alpha,

extend by0, and reflect evenly in x and oddly in y into the other three boxes. Since the cutoffs vanish near the coordinate boundary, the global u is compact C^alpha. In distributions, (3) gives exactly

 V_delta.grad u(F(s,z))=eta'(s)theta(z)|z|^alpha.                 (4)

One can verify(4) directly in these coordinates by testing and integration by parts in s; the transverse cusp has no s derivative. The right side is compact C^alpha. The supports are separated from x=0, so both u and the expression(4) belong to E2: for weighted y differences, either the function vanishes on the entire vertical line or |x|^{-2} is bounded by a fixed constant. Ordinary C^alpha bounds handle the other differences and the cutoff boundary.

Boundedness of B_delta on the full E2 space now implies L_delta u belongs to E2. This checks the complete nonlocal image, rather than assuming it stays in the four boxes. Thus u lies in the actual maximal graph G.

The strain integral of u exists, since its compact support is separated from0. Choose a smooth compact q in S, with support disjoint from a neighborhood of Q and c[q]=1. For example take q_raw=x^2 y beta(r), beta a nonzero nonnegative smooth function supported in an annulus of sufficiently small radius, then divide by

 c[q_raw]=(1/4) integral r beta(r)dr>0.

The annulus avoids0 and may be chosen below the radial distance of the four boxes. It is disjoint from Q, and q has finite graph norm by the smooth-domain argument. Set

 h=u-c[u]q.

Then h lies in G, c[h]=0, and h vanishes near0. In particular its classical origin derivatives and cubic coefficient exist and equal0, even though h is not smooth at Q. On a sufficiently short vertical segment through Q the correction q is zero and (3) gives exactly

 h(x0,y0+r)-h(x0,y0)=|r|^alpha.                                (5)

For each s in S, smoothness at Q gives

 s(x0,y0+r)-s(x0,y0)=O_s(|r|).

Subtract this identity from(5), divide by x0^2 |r|^alpha and let r tend to0. Since alpha<1, the limit is 1/x0^2. Therefore

 ||h-s||G >= ||h-s||E2 >= [h-s]_(y,2) >= 1/x0^2

for every s in S. This proves(2) with b=1/x0^2. The estimate already holds for the input norm, so changing the graph image by its bounded coupling cannot fix the density failure.

## Dependencies and scope

Proof 203 provides bounded coupling and the closed maximal graphs; proof 204 provides the exact J=1,c=0 packets; the canonical strain formula is proof 201. The local smooth region and the exact flow coordinates are independently checked above as in proof 207. No smooth approximation in the large Holder norm is assumed. All density statements specify the ambient closure. There is no numerical calculation and no new profile-existence conclusion.
