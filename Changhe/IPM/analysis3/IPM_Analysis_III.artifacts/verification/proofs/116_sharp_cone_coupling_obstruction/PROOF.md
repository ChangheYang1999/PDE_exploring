# A sharp spatial change of Sobolev order fails for the coupling

## Statement

Use the actual normalized modal background rho and the remainder coupling C_R of proof 44. Fix 0<epsilon_0<1 and the space R_H=R_base+Q of proof 115, with sigma=25/4 and s=41/20. Here R_base consists of p a u, where u belongs to the cylinder H^sigma, is even under both coordinate reflections and has zero vertical-axis trace. The summand Q consists of r^3 a v with v in cylinder H^s, of the density parity, supported in the closed cone |cos(theta)|>=epsilon_0. The norm is the infimum Hilbert sum norm. All radial weights are smooth and strictly positive away from the origin.

Then the actual coupling is not a bounded map

 C_R:R_H -> R_H.                                           (1)

The stronger estimate with one transport graph derivative also fails:

 ||C_R h||_(R_H) <= C (||h||_(R_H)+||T_R h||_(R_H)).          (2)

The counterexamples are smooth, compactly supported away from all axes, the origin, all radial joins and infinity. They have J=0 and no tail coordinate. Thus the problem is the sharp spatial boundary between orders, rather than an endpoint or normalization issue.

This does not refute the jet-block mappings of proof 115, whose lower-block images lie in R_base and whose row compactness only needs a sector graph embedding. It refutes H1 for the direct choice X_H=Y_H=R_H, and also for X_H given its single-transport-derivative graph norm. A smooth variable-order construction or a different transition space remains a separate possibility.

## A regular point on the cone boundary

In the first quadrant let theta_0=arccos(epsilon_0). Choose r_0>0 sufficiently small that the actual inner modal expansion is analytic near

 X_0=r_0(cos(theta_0),sin(theta_0)).

The expansion rho=x^2 y+O(r^5), with differentiated cofactor bounds, gives

 g_0=grad rho(X_0)=(2x_0y_0,x_0^2)+O(r_0^4) != 0.

The cone boundary is a straight ray. Let n be its unit normal pointing from the low-order cone toward the vertical axis. In a fixed neighborhood of X_0 the low-order side is n.(X-X_0)<=0 and the high-order side is n.(X-X_0)>0. The four reflected neighborhoods are disjoint and avoid all axes.

For an open ball B lying on the high-order side, any decomposition f=p a u+q with q in Q gives u=f/(p a) on B. On the fixed neighborhood, p a is smooth and nonzero and physical and cylinder coordinates are smoothly equivalent. Consequently there is a fixed C_0, independent of the radius of B, such that

 ||f||_(R_H) >= C_0^(-1) ||D_v^6(f/(p a))||_(L2(B))        (3)

for each fixed vector v. Indeed the H^sigma norm of u controls all local physical derivatives of order at most6, and restriction to B only decreases the L2 norm. Taking the infimum over decompositions proves (3). If f is not in R_H, interpret its norm as infinity.

## A nonzero exterior kernel derivative

Away from the diagonal the canonical IPM velocity has the kernel

 K_1(Z)=-z_1 z_2/(pi |Z|^4),
 K_2(Z)=(z_1^2-z_2^2)/(2pi |Z|^4).                       (4)

The local identity term in U_2 is irrelevant when output and input supports are disjoint. The frozen coupling kernel is

 K_g(Z)=g_0.K(Z)
       =[g_{0,2}(z_1^2-z_2^2)-2g_{0,1}z_1z_2]/(2pi |Z|^4). (5)

It is a nonzero real-analytic function on the punctured plane because g_0!=0. It is homogeneous of degree -2. Choose w_0 on the low-order side and z_0 on the high-order side so that K_g(v)!=0 for v=z_0-w_0; this is possible since a nonzero quadratic numerator cannot vanish on an open set of such differences. Homogeneity gives

 D_v^6 K_g(v)=7! K_g(v) != 0.                             (6)

Choose a nonnegative smooth bump phi of integral1 supported in a sufficiently small ball about w_0, strictly on the low-order side. By continuity the sixth derivative of K_g*phi in direction v is nonzero at z_0. Shrink a ball B_+ about z_0, strictly on the high-order side, so that

 ||D_v^6(K_g*phi)||_(L2(B_+))>0.                           (7)

This construction uses only separated smooth kernels. No principal-value limit occurs in (7).

## The scaled sequence

For 0<tau sufficiently small set

 h_tau(X)=tau^s phi((X-X_0)/tau)

on the first-quadrant patch, and add its three reflected copies with even-x, odd-y signs. Its support is contained in the low-order cone. The usual Fourier change of variables in dimension2 gives

 ||h_tau||_(H^s) <= C tau,
 ||grad h_tau||_(H^s) <= C.                               (8)

The constants are independent of tau. The same estimates hold in cylinder coordinates on the fixed patches, and after division by r^3 a. Since the actual transport coefficients are smooth with bounded derivatives on these patches, multiplication and Leibniz estimates give

 ||h_tau||_(R_H)+||T_R h_tau||_(R_H)<=C.                   (9)

Both functions may be represented entirely in Q. Every member lies in the maximal low transport domain as well.

## The output on the high-order side

Put X=X_0+tau z with z in B_+. For the first patch, the degree -2 homogeneity of (4), including the Jacobian tau^2, gives the exact separated-support identity

 U[h_tau](X_0+tau z)=tau^s (K*phi)(z)

before the reflected patches are added. The other three patches are a fixed positive distance away; their contributions and every fixed number of physical derivatives are O(tau^(s+2)). Therefore, on B_+, in the C6 norm in z,

 tau^(-s) U[h_tau](X_0+tau z).grad rho(X_0+tau z)
       -> K_g*phi.                                      (10)

The normalized strain term and subtraction of the axis row do not change this limit. For the strain, its kernel is smooth on the four input patches, so c[h_tau]=O(tau^(s+2)). For the axis row, the output axis stays a fixed positive distance from these patches. All of its derivatives on the fixed radial interval are O(tau^(s+2)) by differentiation under the separated kernel integral. Multiplication by p and the analytic background coefficients preserves these estimates. The radial normalization cutoff is fixed and smooth. Thus (10) holds with C_R h_tau in place of the raw coupling.

Since (p a)(X_0)!=0, (7) and (10) imply, for a fixed c_0>0 and all sufficiently small tau,

 ||D_v^6((C_R h_tau)/(p a))||_(L2(X_0+tau B_+))
       >= c_0 tau^(s+1-6).                              (11)

There is one factor tau from the square root of the two-dimensional Jacobian and six inverse factors from differentiation. Here

 s+1-6=-59/20<0.

Combining (3), (9) and (11) proves that the right side of (2) stays bounded while the left side diverges. This proves both assertions.

## Dependencies and scope

The proof uses only the actual inner analytic expansion, the exact IPM kernel, the definition of the sharp cone sum and elementary scaling. It does not use a conjectured inverse, numerical smallness or a high-frequency approximation to the kernel. The obstruction applies for every fixed cone boundary away from the axes. It leaves the finite-angular jet images and the separate scalar graph theorem unchanged.
