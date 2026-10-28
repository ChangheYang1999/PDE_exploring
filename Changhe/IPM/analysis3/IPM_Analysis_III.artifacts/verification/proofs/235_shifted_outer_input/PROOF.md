# Shifted outer columns: exact joins, high-domain intersections and input Gram

## Statement and definitions

This result concerns the five shifted outer remainder columns of the numerical S1J1 section. It certifies their input definition and regularity. It does not certify their output Gram, an operator singular value, or a complement inverse.

Interpret the original archive's binary64 value of k and last knot t_+ as exact rationals. Let

 (j_i,l_i)_(i=0,...,9)=((0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)),
 alpha_i=k-3-j_i(1-k)-2l_i,
 t_J=t_++1, P(z)=product_(i=1,...,4)(z-alpha_i).

The pair list is read from the read-only original modal_fit.py; it is not contained in the NPZ. All nine alpha_i for 1<=i<=9 are distinct for the exact stored k. The accompanying rational check verifies this fact and 0<k<1/4.

For q=5,...,9 define

 A_(qi)=product_(1<=j<=4,j!=i) (alpha_q-alpha_j)/(alpha_i-alpha_j), 1<=i<=4,
 b_q(t)=0 for t<t_J,
 b_q(t)=exp(alpha_q(t-t_J))-sum_(i=1,...,4) A_(qi) exp(alpha_i(t-t_J)) for t>=t_J.

Set p(theta)=cos(theta)^2 sin(theta), F(theta)=cos(2theta)+1, and

 h_q(r,theta)=r^3 p(theta) F(theta)b_q(log r)
             =2r^3 cos(theta)^4 sin(theta)b_q(log r).

Let O be their real five-dimensional span. Every h_q is C^3 across r=exp(t_J), with a nonzero fourth radial derivative jump. All belong to the low input and maximal low graph realization used by S1. Their cubic jet at the origin is zero. Here the low input is L^2(w_a dX), where w_a=|cos(theta)|^(-17/2) exp(mu_a(t)), mu_a(t)=-17t/2 for t<=0 and -5t/4 for t>=0, with the angular remainder constraint of that realization.

For the high spaces H_full and D_H(A0) of proof 206, equivalently the precise spaces of topics173 and174, write h=sum_(q=5,...,9) d_q h_q. Define

 J_n(d)=sum_(q=5,...,9) d_q [alpha_q^n-sum_(i=1,...,4)A_(qi)alpha_i^n].

Then

 O intersect H_full={h:J_4(d)=J_5(d)=0}, dimension 3,
 O intersect D_H(A0)={h:J_4(d)=J_5(d)=J_6(d)=0}, dimension 2.       (1)

In particular none of the five individual columns belongs to H_full. A statement that their entire span contains no high input or no high graph direction would also be false.

The exact, unscaled low input Gram is

 G_(qr)=K exp(27t_J/4) sum_(i,j=1,...,9) B_(qi) B_(rj)/[-27/4-alpha_i-alpha_j],
 K=8 Beta(3/2,1/4),
 B_(qq)=1, B_(qi)=-A_(qi) for 1<=i<=4, B_(qi)=0 otherwise.       (2)

All denominators are positive. For arbitrary positive column scales s_q, the Gram is G_(qr)/(s_q s_r). Formula(2) defines the input exactly, including the whole infinite tail. An interval enclosure and a separate rational integration check are supplied alongside this proof. The finite section's metadata scales are interpreted as exact binary64 constants and the two angular partners must have identical scales before its columns can be identified with h_q/s_q.

## Exact joins and linear independence

Lagrange interpolation at the four distinct nodes alpha_1,...,alpha_4 gives

 sum_i A_(qi)alpha_i^n=alpha_q^n, 0<=n<=3.

Consequently the zero extension of b_q has continuous derivatives through order three. For n=4, the monic interpolation error is P(alpha_q), which is nonzero because the nine exponents are distinct. Thus its fourth derivative has exactly that jump. Multiplication by the smooth nonzero radial factors and by a nonzero angular factor on an open sector preserves the first jump order. Changing from t to r preserves it as well. The columns are linearly independent: in a relation between their exponential sums, the coefficient of exp(alpha_q(t-t_J)), for q>=5, is exactly d_q, and exponential functions with distinct real exponents are independent. One proof differentiates a relation through order eight at any positive t-t_J; the resulting Vandermonde determinant is nonzero.

The norms and graph conditions at infinity converge. The largest participating exponent is alpha_1=2k-4. Thus |h|=O(r^(2k-1)), and every fixed cylinder derivative has the same radial order. The old input's radial squared exponent is 27/4+2alpha_1=4k-5/4<0, so it is integrable at infinity. The angular factor after multiplying by the singular weight is a constant times sin(theta)^2 |cos(theta)|^(-1/2), which is integrable. The input vanishes on a full neighborhood of the origin. Its low transport image has the same far leading power. The bounded renormalized remainder coupling C_R gives the core image (T_R+C_R)h in the same remainder target. This is the S1 core realization of topics43,48 and198, including its axis-remainder projection. Therefore it is a conforming low input and graph column. This statement is not an identification of that core image with the full high operator A0 used in(1).

## High membership and the two rank conditions

Recall the exact high realization: sigma=25/4,

 H_full=E B_H direct-sum X_s,
 B_H=R chi_0+a_H H^(29/4)(R), E beta=r^3 p beta,
 Y_H=E Gamma_H direct-sum X_s, Gamma_H=a_H H^sigma(R),
 D_H(A0)={h in H_full:A0h in Y_H distributionally}.

The remainder has zero vertical cofactor trace and is measured by the squared sum of the variable-order norm of h/(r^3 a_H) and the fixed H^sigma norm of its divided cofactor on vertical sectors. The variable order is at most sigma. At infinity r^3 a_H=r^(-1/2); all weights and divisions are smooth positive radial factors on a compact annulus. These are the same spaces and trace convention used in proof 206. Since F vanishes at the vertical axis, the scalar trace coordinate of every h in O is zero.

For a piecewise smooth function with its first nonzero derivative jump of order n, local H^s membership holds for s<n+1/2 and fails at s=n+1/2. The proof is the local fractional difference integral of its n-th derivative across the jump; at exponent 1/2 it contains a nonzero multiple of integral_0^epsilon integral_0^epsilon(u+v)^(-2)du dv, which diverges. A nonzero smooth angular factor preserves the conclusion on an open sector by tensor-product estimates and testing in the angular variable. This establishes the criterion without making any claim about the value exactly on the axis.

All combinations already have jumps zero through order three. Membership in H^(25/4) is therefore equivalent to zero jumps of orders four and five: if they vanish the function is C^5 and lies in every local H^s with s<13/2; if either does not vanish it fails local H^(11/2), or already H^(9/2). The tail divided by r^3 a_H is O(r^(2k-1/2)), strictly decaying because k<1/4. All cylinder derivatives preserve this strict power. Thus the local criterion is also the global high input criterion.

The background is analytic at t_J, which lies strictly beyond its last join. The radial transport coefficient q_0=V.X/r^2 is nonzero on an open vertical sector there: its axis value is the previously verified positive d(t)>=5.5752. If the input first has a sixth derivative jump, q_0 partial_t h has a nonzero fifth derivative jump on a smaller open sector. All other transport terms have greater regularity there. The bounded high coupling and target chart column lie in Y_H for every H_full input and cannot cancel a term outside Y_H. Hence the high graph requires J_6=0. Conversely zero jumps through order six make the input C^6; its first derivative lies in local H^s for every s<15/2-1=13/2, which includes sigma. The smooth transport coefficients and the strictly decaying far tail give global Y_H membership. The bounded high coupling completes A0 membership. This proves the equivalences in(1).

To compute the dimensions, set e_1=sum_(i=1,...,4)alpha_i and h_2=sum_(1<=i<=j<=4)alpha_i alpha_j. Polynomial division by P gives

 J_4(d)=sum_q d_q P(alpha_q),
 J_5(d)=sum_q d_q P(alpha_q)(alpha_q+e_1),
 J_6(d)=sum_q d_q P(alpha_q)(alpha_q^2+e_1 alpha_q+h_2).

After subtracting multiples of earlier rows, the first two or three constraints form respectively two or three rows of a Vandermonde matrix at five distinct nodes, multiplied by the nonzero P(alpha_q). Their ranks are exactly two and three. The corresponding kernel dimensions are three and two. This also rules out an accidental loss of rank for the stored exponents.

## Exact Gram and independent arithmetic check

In polar coordinates dX=r dr dtheta=exp(2t)dt dtheta. The square of h contributes exp(6t), and t>=t_J>0 gives the radial weight exp(-5t/4). Therefore the radial density is exp(27t/4)b_q b_r. The angular factor integrates to

 4 integral_0^(2pi)sin(theta)^2|cos(theta)|^(-1/2)dtheta
 =16 integral_0^(pi/2)sin(theta)^2cos(theta)^(-1/2)dtheta
 =8 Beta(3/2,1/4).

Expanding the two finite exponential sums and integrating each term on u=t-t_J>=0 proves(2). All exponents 27/4+alpha_i+alpha_j are negative since their maximum is 4k-5/4<0. Termwise integration is legitimate because the sum is finite and every term is integrable. The resulting Gram is positive definite because the columns are linearly independent and the weight is positive almost everywhere.

The arithmetic check reads k and t_+ from the read-only NPZ and extracts the literal pair list by Python AST from the original modal_fit.py without executing that file. It computes the Lagrange weights with fractions, verifies all zero jets and ranks by a separately implemented rational elimination, and forms the radial integrals as exact rationals. A separate rational identity checks the Laplace transform of b_q: its numerator is P(alpha_q) and its denominator is the product of the five factors s-alpha_1,...,s-alpha_4,s-alpha_q. This identity follows by residues at each simple pole, and independently checks each interpolation coefficient. Exact rational LDL elimination checks positive definiteness of the radial Gram. Two outward rounding checks use Arb at512 and640 bits, with fixed one-thread execution. The original coefficient values, exact rational joins, Gram balls, metadata and producer hashes are retained in evidence. No finite output data are used to obtain(2).

## Dependencies and scope

Read proof 198 for the exact low norm and the angular remainder construction, proof 206 for the high spaces and Sobolev jump criterion, and topics173,174 for the high mapping and graph realization. The source pair list and NPZ are immutable originals. The frozen S1J1 producer identifies the actual shifted basis and its scales; it is inspected, not executed. The source normalization repair changes the background but does not change the k or tail-exponent data used here. Formula(2) is independent of any output quadrature. Nothing here closes the global injectivity or complement-inverse problem.
