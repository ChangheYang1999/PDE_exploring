# The actual first-order end error is not bounded on the normal graph

## Statement

Let V be the exact normalized modal transport field and V_0=(-Ax,Dy) its origin linearization. Let T and T_0 denote V.grad-1 and V_0.grad-1 after conjugation by r^(3+delta), delta=9/5, in the origin cylinder. Use either the exact normal space X_- of proof 131 or the actual smooth-order space X_s on a sufficiently small open horizontal plateau where its order is s_0=41/20. For every sufficiently small end radius R there is a smooth parity-preserving cutoff chi supported in0<r<R such that

 chi(T-T_0):D(T_0,X_-)->X_-

is unbounded when the domain carries ||u||_X_-+||T_0u||_X_-. The same localized statement holds for the actual space, since the support lies in a constant-order plateau and away from the cofactor sector.

In particular, although the coefficient difference tends to zero as r tends to zero, it cannot be treated as a small bounded operator on the normal transport graph. For any lambda in the inverse half-plane of proof 131,

 chi(T-T_0)(T_0-lambda)^(-1):X_-->X_-

is unbounded. This refutes that particular Neumann-series justification for an actual-end estimate. It does not refute the stable energy estimates of topics133 and135 or the possibility of H3.

## Why the actual error has a transverse component

The density has exact leading term x^2y. The velocity is divergence free and has curl

 partial_x U_2-partial_y U_1=Delta psi=-partial_x rho=-2xy+o(r^2).

Its parity makes V_1 odd in x and even in y, and V_2 even in x and odd in y. Local elliptic regularity can here be checked directly from the finite inner Green expansion: after the linear term there is a homogeneous cubic polynomial V_3, followed by o(r^3), with the corresponding derivative remainder. The leading polynomial x^2y has no resonant logarithmic velocity term of degree3; equivalently its differentiated Poisson source is the degree2 polynomial2xy and admits a degree4 polynomial particular solution. Any smooth harmonic contribution through degree4 is polynomial as well. Thus

 div V_3=0, curl V_3=-2xy.                              (1)

Suppose V_3 were pointwise parallel to V_0 on an open angular interval. Their polynomial wedge would vanish on an open set and hence identically. Parity gives V_3,1=x P_2 and V_3,2=y Q_2 for even homogeneous quadratic polynomials. The parallel condition then forces

 V_3=alpha_2 V_0,
 alpha_2=a x^2+b y^2.

Taking divergence and using div V_0=D-A gives

 div(alpha_2 V_0)=(D-3A)a x^2+(3D-A)b y^2.

For the actual rates D-3A=2-2ell is nonzero and3D-A=10ell-2 is nonzero. Hence a=b=0, contradicting the curl in(1). The transverse cubic polynomial is therefore nonzero on some subinterval of every open angular interval. In particular one may choose an angle inside the uniform low-order horizontal plateau, separated from the horizontal axis itself, where the actual V-V_0 is transverse to V_0 at arbitrarily small positive radii. The o(r^3) remainder cannot cancel a nonzero leading value for all sufficiently small radii.

## A characteristic phase and the packets

On the first quadrant choose

 phi(x,y)=D log x+A log y.

Then V_0.grad phi=0 and grad phi is nonzero. Transversality gives a point, and hence a small compact neighborhood O inside the chosen plateau, on which

 b=(V-V_0).grad phi

is bounded away from zero. Choose a nonzero smooth amplitude a supported in O. The neighborhood avoids both axes and the vertical cofactor sector. In cylinder coordinates define

 u_N=N^(-s_0) a exp(iN phi).

Extend by the required even-x, odd-y physical parity to four disjoint reflected neighborhoods. A real sequence can be obtained with cosine in place of the exponential. All functions are smooth, have compact support away from the origin and infinity, vanish near each axis, and therefore satisfy every cofactor trace condition. They are in both maximal transport domains. Multiplication by the fixed physical conjugating factor does not change any estimate on this compact set.

For a compactly supported smooth amplitude and a phase with nonvanishing gradient, the H^s norm of a exp(iN phi) is comparable to N^s. One elementary justification is to integrate its Fourier transform by parts outside a fixed annulus cN<=|xi|<=CN containing the phase gradients. The exterior contributions decay to arbitrary order, while Plancherel preserves the nonzero L2 mass in that annulus. Derivative bounds give the upper estimate, and the annular L2 mass gives the lower estimate. Smooth cutoffs separated from the support give arbitrary-order small tails by the same nonstationary integration. Consequently the variable-order norm here is comparable to the ordinary H^(s_0) norm; its higher-order region is separated from the support and contributes a rapidly decaying tail.

Since V_0.grad phi=0, differentiating u_N with T_0 produces only derivatives of the fixed amplitude and fixed conjugation factor. Therefore

 ||u_N||_X_-+||T_0u_N||_X_-<=C.                         (2)

In contrast,

 (T-T_0)u_N=i N^(1-s_0) b a exp(iN phi)+O_(H^s_0)(1).

The first term has X_- norm bounded below by cN, because ba is nonzero. Choose chi=1 on the amplitude support and supported in the same end plateau, and extend it with the parity symmetries. Then

 ||chi(T-T_0)u_N||_X_->infinity.                        (3)

This proves the unbounded graph map.

## Resolvent consequence and exact scope

For lambda in the half-plane Re lambda>-m_x, let f_N=(T_0-lambda)u_N. Equation(2) makes f_N bounded in X_-. Proof 131 gives the exact inverse on its maximal domain, so (T_0-lambda)^(-1)f_N=u_N. Equation(3) proves the unbounded composition. The cutoff may be supported in an arbitrarily small fixed end neighborhood, but its location is held fixed as N tends to infinity. Thus no fixed coefficient smallness compensates for arbitrarily high transverse frequency.

This is an actual-coefficient counterexample, not just an arbitrary perturbation example. Its inputs are the exact x^2y leading term, incompressibility, parity, the nonresonant cubic local velocity expansion, and the accepted constant-order horizontal plateau. It does not assert that the actual full operator lacks an inverse. It explains why principal first-order coefficient errors must be treated by energy, characteristic changes or a genuine microlocal estimate rather than by a bounded-perturbation claim on the normal graph.
