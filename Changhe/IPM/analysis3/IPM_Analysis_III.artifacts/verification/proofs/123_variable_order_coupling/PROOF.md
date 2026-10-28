# The remainder coupling on a smooth variable-order space

## Statement and notation

Let rho be the exact normalized C6-joined modal trial of topics15 and68, let k=1615536043799051/9007199254740992, and let U, c, E and Gamma_C have the meanings and signs verified in topics1,37,109 and113. In particular U=(-R_1 R_2,R_1^2), E beta=x^2 y beta(log r), and

 C_ren h=[U[h]+c[h] chi_0(r) X/3].grad rho,
 C_R h=C_ren h-E Gamma_C[h].                              (1)

The fixed cutoff chi_0 is smooth, equals one for all sufficiently small r and vanishes for all sufficiently large r. Set

 sigma=25/4, s_0=41/20, delta=9/5, gamma=-1/2.

Choose a positive smooth a(t) with a(t)=exp(delta t) for t<=-1 and a(t)=exp((gamma-3)t) for t>=1. Put b(t)=exp(3t)a(t) and p(theta)=cos(theta)^2 sin(theta). Thus x^2 y a(t)=b(t)p(theta).

Let s(t,theta) be a real smooth function on the cylinder C=R x S^1. Assume every derivative of s is bounded, s is invariant under both coordinate reflections, s_0<=s<=sigma, and

 s(t,theta)=sigma when |cos(theta)|<epsilon_2              (2)

for some fixed epsilon_2>0. Choose a smooth reflection-invariant theta cutoff chi equal to one on |cos(theta)|<=epsilon_0 and supported in |cos(theta)|<epsilon_1, where 0<epsilon_0<epsilon_1<epsilon_2. No monotonicity along a flow is needed for this theorem.

Use the usual inhomogeneous variable-order L2 Sobolev space H^{s(.)}(C). One precise realization is an elliptic pseudodifferential order reduction with principal symbol <xi>^{s(t,theta)}, with a lower fixed Sobolev norm added to remove its finite-frequency kernel. An equivalent definition uses a smooth inhomogeneous Littlewood-Paley resolution and the norm

 sum_(j>=0) ||2^{j s(t,theta)} Delta_j v||_2^2.

Fix either realization once and for all. Define X_s to consist of parity-P functions h (even in x and odd in y) for which v=h/b belongs to H^{s(.)}(C), and

 u=chi(theta) h/[b(t)p(theta)] belongs to H^sigma(C),
 u(t,pi/2)=u(t,3pi/2)=0.                                 (3)

The quotient in (3) is defined away from the vertical axis and required to have the indicated Sobolev extension. Give X_s the Hilbert norm squared ||v||_{H^{s(.)}}^2+||u||_{H^sigma}^2. Different allowed cutoffs produce equivalent local descriptions if s=sigma on the region between them. The trace conditions in (3) are closed since sigma>1/2. They are part of the definition, not consequences of parity.

**Theorem.** X_s embeds continuously in R=L2_P(|x|^{-17/2} max(1,r)^{29/4} dX), and C_R extends to a bounded operator X_s -> X_s. The scalar and jet choices of proof 114,

 Gamma_H=a H^sigma(R), B_H={beta in B:A beta in Gamma_H},

satisfy J1, J2 and J3 with remainder target X_s: Err+C_R E maps B_H boundedly into X_s, Gamma_C maps E B_H plus X_s compactly into Gamma_H, and the actual moving-tail variation zeta belongs to E Gamma_H plus X_s.

The theorem is qualitative. Its constants depend on the displayed cutoffs, a, finitely many uniform derivatives of s, the actual modal coefficients and the previously verified axis-row constants. It does not prove H2, H3, a transport inverse, injectivity or nonlinear closure. It does not assert that U by itself preserves X_s.

## Local analytic facts used below

We give the relevant calculus argument to specify the hypotheses. On uniformly sized coordinate patches, a smooth order-zero pseudodifferential operator is bounded on H^{s(.)}. Conjugate it by an elliptic order reduction with symbol <xi>^{s(x)}. The leading symbol has order zero. Every nonleading composition term contains a frequency derivative, while the spatial derivatives of the order weight introduce powers of log<xi>. Thus these terms have order -1+epsilon or lower, for any fixed epsilon in (0,1/2). Symbolic inversion and the ordinary L2 order-zero bound prove the claim. A uniformly smooth family of symbols and order functions gives a uniform operator bound. This is also the scalar case of Krainer and Mendoza, Proposition5.2, after localization to patches of small order oscillation. Their coordinate invariance, Proposition4.12, permits the annular coordinates used here.

We also need multiplication by coefficients that have the actual finite regularity. A compactly supported coefficient q in H^{sigma+epsilon} on a two-dimensional patch, with epsilon>0, acts boundedly on H^{s(.)} when 1<s_0<=s<=sigma. To see the needed estimate, split the product into low-q/high-v, high-q/low-v and comparable-frequency terms. The first term uses the uniform L-infinity norm of the low-frequency q and the frequency-local moderate weight 2^{j s(x)}. In the second term use 2^{j s(x)}<=2^{j sigma}, the L-infinity bound for v from H^{s_0}, and the H^{sigma+epsilon} square sum of q. The comparable-frequency terms are summed using s_0>1 and the same positive epsilon. Smooth bounded s makes 2^{j s(x)} moderate on the scale 2^{-j}, so the convolution kernels used in these three estimates retain arbitrarily summable spatial decay. This proves the bound, with the finite-frequency terms controlled by L2. The same reasoning at constant order is the usual H^sigma algebra estimate.

For the actual modal trial, every annularly normalized coefficient of grad rho used below is uniformly H^{sigma+epsilon} for, for example, epsilon=1/8. At a spline join rho is C6 and piecewise analytic, so grad rho is C5 with a continuous fifth derivative whose next weak derivative is piecewise smooth with finitely many jumps. A compactly localized such coefficient is H^q for q<13/2, and sigma+1/8=51/8<13/2. The finite number of joins and finite angular bandwidth make the constants uniform. At the two ends the explicit exponential-polynomial expansions give the same uniform bounds after removing their stated powers. This regularity assertion concerns coefficients, not an extra derivative of the unknown.

Finally, an odd function f in H^{q+1}(R^2) has f/x in H^q locally, with a bounded norm for every q>=0. For integers this follows from

 partial_x^j(f/x)=integral_0^1 tau^j partial_x^{j+1}f(tau x,y) d tau

and the integrability of tau^{j-1/2}; tangential derivatives commute with this formula. Interpolation gives the fractional orders. Cutoffs supply the local version.

## Embeddings and the already verified jet blocks

Away from the vertical axis, the R weight divided by b^{-2} contributes the bounded radial factors r^{2delta-1/2} at the origin and r^{2gamma+3/4} at infinity. Both are bounded in their corresponding ends. Near the vertical axis use (3), the evenness of u in the normal variable and its zero axis trace. The angular Hardy estimate of proof 111, of order9/4 with weight |cos(theta)|^{-9/2}, gives the R bound. The same estimate after four t derivatives proves X_s -> R_(4,sector), with the sector cutoff supported where chi=1.

Every element b p w with w in H^sigma and zero axis trace belongs to X_s: multiplication by p and chi is bounded and H^sigma embeds into H^{s(.)}. Thus the full high base used in proof 115 embeds in X_s. J1 and J3 therefore follow from their proved images in that base. The remainder part of J2 follows from X_s -> R_(4,sector) and proof 113 with the stronger endpoint weights of proof 115. Its free-jet part is unchanged. In particular

 ||Gamma_C[h]/a||_{H^sigma} <= C ||h||_{X_s},              (4)

and this map is compact. We will also use boundedness of c on R, already proved in proof 91.

## Same-scale coupling and the vertical factor

Use a smooth radial partition of unity in t with uniformly bounded overlap, preserving parity. Let h_n be one annular input and first restrict the output to a comparable annulus. Rescale its radius to one. The localized U is a smooth order-zero pseudodifferential operator plus a smooth kernel. Away from the vertical axis, the preceding calculus and multiplication estimates apply directly to C_ren h divided by b. Its operator norm has the scale factor O(r^2) at the inner end and O(r^{k-1}) at the outer end. Both are bounded.

Near the vertical axis, input from the smaller fixed vertical sector is of the form x^2 times an H^sigma function in rescaled coordinates. The missing smooth radial and y factors are nonzero and have bounded derivatives there. Input outside a slightly larger sector is separated from the output, so its kernel is smooth. For the former input use the exact commutator identity

 U_1[x^2 w]/x = x U_1[w]+2[U_1,x]w+x^{-1}[[U_1,x],x]w.   (5)

After smooth localization the single and double commutators have orders -1 and -2. The double commutator output is odd in x. The preceding division estimate shows that its quotient by x lies in H^{sigma+1}, hence in H^sigma. The low-frequency smooth part obeys the same parity argument. Thus U_1[x^2 w]/x is bounded in H^sigma. Also U_2[x^2 w] is bounded in H^sigma. Since rho=x^2 f locally,

 (U[h].grad rho)/x^2=(2f+x f_x) U_1[h]/x+f_y U_2[h].      (6)

The coefficients in (6) have the regularity just established. This proves the required same-scale estimate for the factored output, without losing derivatives of w. The strain term is a smooth annular coefficient times c[h_n] and obeys the same bound at comparable scales.

## Separated radial scales and the origin cancellation

The following estimates also hold for the output Sobolev norms just used. For separated annuli the kernel is smooth; any fixed number of rescaled output derivatives obeys the same scale powers. Multiplication by the background uses its H^{51/8} coefficient bounds. The angular factor at the vertical axis follows from parity and (6). Constants absorb the fixed annular widths. Let r be the output radius, s the input radius, and let e_s be the input normalized annular X_s norm.

The input amplitude is b(s)e_s. Its integral vanishes by oddness in y. Its first absolute moment is bounded by C s^3 b(s)e_s. Its strain satisfies |c[h_s]|<=C b(s)e_s/s. The degree-minus-two U kernel and parity therefore give

 |U[h_s](X)| <= C r^{-3} s^3 b(s)e_s,        s much smaller than r,
 U[h_s](X)=c[h_s](-x,y)+O(r^3 b(s)e_s/s^3), r much smaller than s. (7)

The second formula has no constant or quadratic term by parity. At small output radii the normalized linear strain c(-2x/3,4y/3) annihilates x^2 y exactly. Since rho=x^2 y+O(r^5), its contribution to C_ren is O(r^5 |c[h_s]|). This cancellation must be performed before summing the input annuli.

Combining (7), the strain term and grad rho=O(r^2) inside, O(r^{k-1}) outside, gives the following matrix bounds for C_ren/b and, near the vertical axis, C_ren/(b p):

 0<s<=r<=1: C r^2 (s/r)^{delta+2} e_s,
 0<r<=s<=1: C r^{2-delta} s^delta e_s,
 1<=s<=r:   C r^{k-1} (s/r)^{gamma+3} e_s,
 1<=r<=s:   C r^{k-1} (s/r)^{gamma-1} e_s,
 0<r<=1<=s: C r^{2-delta} s^{gamma-1} e_s,
 0<s<=1<=r: C r^{k-4-gamma} s^{delta+2} e_s.              (8)

For the first line, the velocity term alone has the stronger power delta+6; delta+2 also includes the normalization strain. For the last line, the velocity term has s^{delta+6}; the strain cutoff is supported in a fixed output annulus and can be bounded by the displayed weaker power with a fixed constant. Modifying finitely many annuli covers the transition regions of a, chi_0 and the expansions.

The six matrices in (8) have uniformly bounded row and column sums on logarithmically spaced annuli. For the only potentially growing ratio, r<=s<=1, sum r^{2-delta}s^delta first in s or first in r; both sums converge because 0<delta<2. The other inner sums use delta+2>0. The outer sums use gamma<1, gamma+3>0, k<1 and k-4-gamma<0. These inequalities all hold for the exact displayed parameters. The two mixed-end sums are products of convergent geometric series. Schur's test and the finite overlap prove

 ||C_ren h/b||_{H^{s(.)}} + ||chi C_ren h/(b p)||_{H^sigma}
 <= C ||h||_{X_s}.                                      (9)

The parity-preserving annular sums converge in these spaces. They agree with the previously defined full-plane operator by their kernel convergence on every compact annulus and then by continuity. Thus the calculation has not introduced a different realization of U.

## Axis subtraction and closedness

By (4), E Gamma_C/b=p Gamma_C/a belongs to H^sigma(C), and chi E Gamma_C/(b p)=chi Gamma_C/a belongs to H^sigma(C). Consequently subtracting E Gamma_C preserves both norms in (9). The exact axis identity of topics109 and113 identifies the trace of C_ren h/(b p) with Gamma_C[h]/a. The trace of C_R h/(b p) is therefore zero. This proves C_R h in X_s with the stated bound.

The definition of X_s is a closed graph intersection of Hilbert spaces with two continuous zero-trace conditions, hence is complete. Equation(9) and the convergent kernel construction define the bounded operator directly on this closed intersection, so no density assertion for a special normalized smooth core is needed. No unclosed pointwise normalization has been used.

## Dependencies and limitations

The local smooth calculus is the scalar specialization of Thomas Krainer and Gerardo A. Mendoza, *Elliptic systems of variable order*, arXiv:1301.5820v2, Proposition4.12 and Proposition5.2. Andre Unterberger, *Sobolev spaces of variable order and problems of convexity for partial differential operators with constant coefficients*, Asterisque2-3 (1973),325-341, gives the scalar definition and local square-function equivalence in Section1. The present proof supplies the singular axis factor, limited coefficient regularity, global end estimates and normalization cancellation; those do not follow just from a local order-zero calculus.

Internal dependencies: topics15,68 and84 for the actual modal background and coefficient regularity; proof 91 for c; topics109,111,113,114 and115 for the exact axis row, Hardy estimate and compatible jet blocks. No theorem about the existence of a smooth Lyapunov order function is assumed beyond the explicit conditions (2). No numerical bound for the operator constant is claimed.
