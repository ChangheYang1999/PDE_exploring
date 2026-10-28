# High input and graph intersections of the complete shifted-junction section

## Exact statement

Let B_i, 0<=i<38, be the radial functions of proof 239 in the fixed S1J1 metadata order, and s_i their exact positive binary column scales. Put

 h_i=2r^3 cos(theta)^4 sin(theta) B_i(log r)/s_i,
 S=span_R{h_i:0<=i<38}.

The original knot vector, k and all matching conventions are exactly those of topics198,235 and239. In particular t_minus<t_plus<t_J=t_plus+1, there are34 degree-seven coarse splines, and every interior coarse knot is simple. Use the high correction and target spaces of topics173 and174, with sigma=25/4:

 H_full=E B_H direct-sum X_s, Y_H=E Gamma_H direct-sum X_s,
 E beta=r^3 p(theta) beta(t), p=cos(theta)^2 sin(theta),
 B_H=R chi_0+a_H H^(29/4)(R), Gamma_H=a_H H^sigma(R),
 b_H=r^3 a_H=r^(24/5) near0 and r^(-1/2) at infinity.

The remainder X_s measures h/b_H in the variable order41/20<=s(t,theta)<=sigma and chi h/(b_H p) in fixed H^sigma on vertical sectors, with zero vertical cofactor trace. All weight interpolations and cutoffs are smooth and fixed as in proof 173. Let A0 be the complete moving-tail normalized operator on

 D_H(A0)={h in H_full:A0h belongs to Y_H distributionally}.

For a coefficient vector d in R^38 write B_d=sum_i d_i B_i/s_i and define the three jump functionals

 J_(minus,n)(d)=B_d^(n)(t_minus+)-B_d^(n)(t_minus-),
 J_(plus,n)(d)=B_d^(n)(t_plus+)-B_d^(n)(t_plus-),
 J_(outer,n)(d)=B_d^(n)(t_J+)-B_d^(n)(t_J-).

These are exact real linear forms; after multiplication by the rational scales their coefficients are rational. The full section obeys

 S intersect H_full
   ={sum_i d_i h_i: J_(v,4)(d)=J_(v,5)(d)=0 for v=minus,plus,outer},
 dim(S intersect H_full)=32,                                      (1)

 S intersect D_H(A0)
   ={sum_i d_i h_i: J_(v,4)(d)=J_(v,5)(d)=J_(v,6)(d)=0
                                      for v=minus,plus,outer},
 dim(S intersect D_H(A0))=29.                                    (2)

The entire section has J=0 and zero vertical cofactor trace. Neither(1) nor(2) is a high-norm operator estimate. In particular a singular value computed after restricting a low-norm matrix to the29-dimensional subspace would still use that low norm and an uncertified output matrix.

## Local and end membership

Proof 239 proves independence of all38 columns and their C3 matching at the three exceptional joins. Every other join is C6. The common angular factor has physical parity and vertical cofactor factor2 cos(theta)^2, so its trace on both vertical axes is zero. The unique scalar coordinate of any high input in S is therefore zero. Consequently local high membership is determined by the fixed H^(25/4) cofactor sector, not by the H^(29/4) scalar input norm.

Near the origin every B_i is a finite combination of exp(2j(t-t_minus)), j>=1, or zero. Thus h_i is a finite polynomial combination of x^4 y (x^2+y^2)^(j-1), supported by the fixed inner region. It is smooth there, has physical order at least5 and cubic coefficient J=0. Dividing by b_H gives order r^(5-24/5)=r^(1/5). Every fixed cylinder derivative has the same strict end exponent, so the high input norm and all orders needed in the transport image are finite at the inner end. Its cofactor division merely replaces the fixed smooth angular factor by2 cos(theta)^2 and changes no radial exponent.

At infinity the five outer columns have order r^(2k-1), with every fixed cylinder derivative. Their quotient by b_H has exponent2k-1/2<0, since the exact stored k<1/4. Therefore all fixed high cylinder norms converge at that end. All other columns vanish beyond t_plus. The intermediate intervals are finite. There are consequently no further input end constraints beyond the three finite jump conditions.

For a piecewise smooth scalar function, a first nonzero derivative jump of order n is compatible with local H^s exactly for s<n+1/2. Proof 206 proves this by the fractional difference integral across the jump and tensor-product testing on a nonzero angular sector. Smooth positive radial weights preserve the first nonzero jump order. On a smaller open vertical sector the factor2 cos(theta)^2 is nonzero. Thus high membership requires zero fourth and fifth jumps at each exceptional join. Conversely these conditions make the input C5 at those joins, with piecewise smooth sixth derivatives, hence locally H^s for every s<13/2, including25/4. The C6 interior joins are more regular. Global fixed H^sigma controls the variable-order norm since s<=sigma. With the strict end bounds already proved, this establishes the equivalence in(1).

## Full operator-domain membership

Use the actual radial transport coefficient

 q(t,theta)=V(X).X/r^2, V=ell0 X+U[rho0].

At each exceptional radius its vertical-axis value is the previously certified coefficient d_axis(t)>=5.5752. Therefore q is nonzero on an open vertical angular sector there. This uses the actual joined normalized background, not a frozen dilation. All local coefficient regularity and axis divisions are those established for proof 206 and its binding audit clarifications.

If an input satisfying(1) has a nonzero sixth jump at a join t0, its transport image has the leading fifth-derivative jump q(t0,theta) times that input jump and the nonzero angular factor. The non-cancellation argument requires Sobolev regularity of the remainder, not merely a C5 assertion. Write

 q(t,theta)=q(t0,theta)+(t-t0)Q(t,theta),

with Q in the local W^(6,infinity) class supplied by the exact coefficient formulas. The product(t-t0)B_d' has its first possible jump at derivative6 and is locally H6. The Q product and the other B_d times coefficient terms are locally H6. The leading term q(t0,theta)B_d' fails H^(11/2) on a smaller sector when the sixth input jump is nonzero. Addition of H6 terms cannot remove that failure. This is the piecewise smooth Hadamard split of proof 206's audit clarification, applied to a linear combination. Since25/4>11/2, the transport image is outside the high target.

For every H_full input in S, the complete normalized nonlocal coupling and fixed moving-tail chart term are in Y_H. The bounded high realization proves this; it can also be checked directly here. The finitely many angular Green modes preserve the local H^sigma radial regularity, and grad rho0 has local H^sigma regularity from its C6 joins. Products are in H^sigma. Axis traces use the same finite radial formulas. Near zero the smooth velocity has c[h](-x,y)+O(r^3); the normalized cubic term cancels exactly, leaving physical order r^5 and divided order r^(1/5). At infinity U[h]=O(r^(2k-1)) for these exact sublinear finite-power tails, while grad rho0=O(r^(k-1)); their product divided by b_H has order r^(3k-3/2), which decays. The fixed target-valued chart column has divided order r^(2k-1/2)(1+log r), which also decays. The compact chart pieces are harmless. These bounds include the axis coordinate and both ends.

Thus addition of the high-target coupling cannot repair a non-H^sigma transport image. This proves necessity of all three sixth-jump constraints in(2). Conversely zero jumps through order6 give a globally piecewise C6 radial input at all finite joins. Its first derivative is locally H^s for s<13/2, including sigma, and multiplication by the stated transport coefficients preserves that regularity. The strict inner and outer powers are unchanged by cylinder transport. The normalized coupling just checked completes A0 membership. This proves the equivalence in(2), on the exact maximal domain with no density or smooth-core assumption.

## Exact ranks and dimensions

The jump constraints at the three separated radii are independent. At t_minus use the pure splines b_4,b_5,b_6, which have exact first nonzero left endpoint derivatives of orders4,5,6, respectively. They vanish near t_plus and t_J. Their columns occur in S at indices7,8,9. The first two minus rows evaluated on b_4,b_5 form a triangular2 by2 matrix with nonzero diagonal. The first three minus rows evaluated on b_4,b_5,b_6 form such a3 by3 matrix. The positive scales do not change rank.

At t_plus use b_29,b_28,b_27, whose exact first nonzero right endpoint orders are4,5,6. They vanish near t_minus and t_J. Their columns occur at indices32,31,30. The same triangular argument proves independent plus rows, jointly independent of all minus rows.

The five outer columns vanish near both spline endpoints. Proof 235 proves that their fourth and fifth jump rows have rank2, and their fourth through sixth rows have rank3, by a Vandermonde matrix at five distinct outer exponents times nonzero interpolation errors. Conversely all nonouter columns vanish near t_J. Therefore the combined six-row input constraint matrix has rank2+2+2=6, and the combined nine-row graph matrix has rank3+3+3=9. The ambient dimension38 gives32 and29.

The attached rational computation independently reconstructs both endpoint jets through order7 from the original knot vector, forms all scaled jump rows using proof 239's exact matching coefficients, verifies their ranks by rational elimination, and exports exact rational nullspace bases. It checks the named triangular minors, every nullspace identity and the rank of the exported nullspaces. These are exact finite algebraic checks, not numerical singular-value tests. The original source and all dependency hashes are recorded.

## Scope and verification status

This result classifies this precise38-column S1J1 span only. It does not classify the169-column joined section, establish a bounded inverse, assert that a low input Gram is a high Gram, or remove the output-division and complement gaps. The norm, coefficient and jump-regularity inputs are topics173,174,206 with its audit clarifications,235 with its audit clarifications, and239. The analytic derivation precedes computation. Exact ranks and nullspace exports remain pending until the attached original-data run passes; an independent review is requested before adoption of the new whole-section theorem.
