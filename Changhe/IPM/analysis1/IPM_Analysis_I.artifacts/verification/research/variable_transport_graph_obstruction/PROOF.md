# Variable transport is not bounded on the frozen saddle graph domain

Date to be bound by evidence/proof_first.json immediately after this file is written. This standalone informal proof precedes its new checkers. Status OPEN until actual-model review and own final adjudication. All norms below are defined explicitly. No existence or nonexistence theorem for the IPM profile is claimed.

The frozen saddle differentiates only one direction at each point. A phase constant along that direction can oscillate arbitrarily rapidly with bounded frozen graph norm. Near the trial's positive source the true transport differentiates that phase with a coefficient bounded away from zero. The order-zero canonical velocity coupling cannot cancel the resulting growth.

## Statement and exact background

Let rho0 be the exactly joined, exactly normalized modal_v2 trial. Its canonical velocity solves -Delta psi0=partial_x rho0, U0=(-partial_y psi0,partial_x psi0), with sublinear velocity at infinity. Set k=1615536043799051/9007199254740992, ell=1/k, A=2/k-1>0, D=4/k-1=2A+1 and V0=ell X+U0. For compact smooth densities let Sigma(h)=partial_xy psi[h](0), J(h) the coefficient of x^2 y at zero, and

 Lh=V0.grad h-h+U[h].grad rho0+(Sigma(h)/3)X.grad rho0.

The accepted background inputs are as follows. There is a source P=(p,0), p>43/5, with V0(P)=0, DV0(P)=diag(A0,mu), 0<A0<51/5 and mu>99/100. On B_R(P), R=99/2000, ||D^2 V0||_F<M=743/2500. The density and velocity are C6 near that closed smaller rectangle used below. These are the moving_source result with its mandatory ADDENDUM and PUBLICATION and the finite-regularity background statement in annular_degree_five_leakage_v2. The canonical_full_radial_linkage result discharges the archive/canonical-moment application premise of the imported local source bounds. This is an application to the canonical joined trial, not the literal discontinuous stored representation. The new checker must bind these inputs and any byte-identical local source substitutions explicitly.

Fix any finite real a and s=153/50=3+3/50. On x>0 define

 F_h(z,y)=exp((1/2-a)z)h(exp z,y),
 ||h||_Y=||F_h||_(H^s(R_z x R_y)),
 T=-A x partial_x+D y partial_y-1,
 D(T)={h in Y:Th in Y distributionally}.

The Sobolev norm uses the unitary Fourier transform and multiplier (1+xi^2+eta^2)^(s/2). The frozen graph norm is ||h||_Y+||Th||_Y. Extend densities evenly across x=0 and oddly across y=0. There are a fixed real smooth compact cutoff chi, supported away from the two axes, and a sequence of real smooth compact densities h_n, also supported away from both axes, such that

 J(h_n)=Sigma(h_n)=0,
 sup_n (||h_n||_Y+||Th_n||_Y)<infinity,
 ||chi Lh_n||_Y -> infinity.                                      (1)

Each h_n globally factors as x^2 y times a smooth function and has zero center factor. Multiplication by chi is bounded on Y. Consequently no bounded map from the full frozen graph domain into Y can agree with L on all these tests. The same conclusion holds for L-T, and such a map cannot be compact. If some Lh_n is not globally in Y, that already prevents such a map; (1) makes no assertion of global membership of the images. Nothing here excludes a realization using the actual transport graph, a stronger domain, different local norms, or a full IPM inverse in some other space.

## A strict transport mismatch on a concrete rectangle

Take e=1/10000, y_-=1/2000, y_+=3/2000 and

 Q={(x,y): |x-p|<e, y_-<y<y_+}.

Its closure is in B_R(P), since e^2+y_+^2<R^2, and is separated from both axes. Write delta=x-p. Taylor's formula with integral remainder and the Frobenius Hessian bound gives, componentwise,

 |V01(x,y)-A0 delta| <= M(delta^2+y^2)/2,
 |V02(x,y)-mu y| <= M(delta^2+y^2)/2.                              (2)

The mixed linear coefficients vanish by parity. In log coordinates put

 Phi(z,y)=D z+A log y, b_V(z,y)=D V01(exp z,y)/exp z+A V02(exp z,y)/y.

Then (-A partial_z+D y partial_y)Phi=0, whereas V0.grad Phi=b_V. If r_*=M(e^2+y_+^2)/2, (2) gives on Q

 b_V >= A(99/100)-D[(51/5)e+r_*]/(43/5-e)-A r_*/y_- =: b_* >10.     (3)

The strict final inequality is an exact rational claim to be checked by two separate implementations. In particular no floating point locator or assumed width from continuity is used to select Q.

## Oscillation estimates without a stationary-phase assumption

Choose a nonzero real b in C_c^infinity of the log image of Q. For integers n>=1 define F_n=n^(-s)b exp(i n Phi), first for y>0. Its inverse log transform defines h_n^raw there. Extend evenly in x and oddly in y; the supports of the four reflected pieces are disjoint and separated from the axes. These extensions are smooth and compact.

For a fixed compact C4 amplitude q and smooth phase Phi on a neighborhood of its support, differentiation through order4 gives ||q exp(i n Phi)||_H4<=C n^4 and its L2 norm is ||q||_2. Holder's inequality in Fourier space gives

 ||v||_Hs <= ||v||_2^(1-s/4)||v||_H4^(s/4),

so the H^s upper bound is C n^s. This also applies to the reflected pieces and to fixed physical-coordinate amplitudes after the smooth log substitution.

A lower bound requires only a nonzero L2 amplitude q supported where y>0. Take the Fourier transform only in z. Because partial_z Phi=D,

 F_z[q exp(i n Phi)](xi,y)=exp(i n A log y) qhat_z(xi-nD,y).

The squared L2 mass on |xi|<nD/2 is at most integral_(|zeta|>=nD/2) |qhat_z(zeta,y)|^2 d zeta d y, which tends to zero. Thus the mass on |xi|>=nD/2 tends to ||q||_2^2. The full Fourier H^s norm dominates (nD/2)^s times the square root of that mass, by Plancherel in y. Consequently for sufficiently large n,

 ||q exp(i n Phi)||_Hs >= (nD/2)^s ||q||_2/sqrt(2).                 (4)

No differentiation of q and no asymptotic oscillatory integral is needed for this lower bound.

The log conjugate of T is P0=-A partial_z+D y partial_y+c, c=-A(a-1/2)-1. Since P0 differentiates Phi only through its constant term, exactly

 P0 F_n=n^(-s) exp(i n Phi)[-A b_z+D y b_y+c b].                   (5)

The preceding upper bound proves uniform boundedness of both the Y and T graph norms of h_n^raw.

## The principal output and the nonlocal term

Choose a real smooth cutoff chi_+ supported in the log image of Q and equal to1 on a neighborhood of supp b. Regard it also as a physical cutoff by z=log x, extended by zero outside Q. Its multiplication is bounded on Y. It suffices initially to use this one positive-quadrant cutoff; parity of the image is not required after localization. On that patch the log conjugate of V0.grad applied to h_n^raw is

 i n^(1-s) b b_V exp(i n Phi)
 +n^(-s) exp(i n Phi)[(V01/x)b_z+V02 b_y+(a-1/2)(V01/x)b].          (6)

The amplitude b b_V is nonzero by (3), and is compact C4. Equations (4) and (6) show that the H^s norm of this localized transport output is at least c1 n-C1 for constants c1>0 and C1 independent of n. The term -h_n^raw is bounded in Y.

Here is a direct justification that the localized nonlocal term has uniformly bounded Y norm. On the fixed four compact supports the physical h_n^raw have uniformly bounded H^s(R^2) norm by the H4 interpolation argument already given. The canonical full-plane Fourier symbol of U is

 (xi1 xi2/|xi|^2, -xi1^2/|xi|^2).

Its squared vector length is xi1^2/|xi|^2<=1, so ||U[h_n^raw]||_Hs<=||h_n^raw||_Hs. The value at zero frequency is irrelevant. These compact smooth sources have the decaying canonical velocity; hence the multiplier has no harmonic-strain ambiguity. Multiplication by chi_+ grad rho0, followed by the inverse log coordinate change and the smooth bounded exponential weight on the patch, is bounded H^s to H^s. Only the local C4 derivatives of grad rho0 and a smooth coordinate map on a compact set are needed, and rho0 is C6 there.

For completeness that fractional-order mapping bound can be checked without assuming a global log diffeomorphism. Write s=3+alpha, alpha=3/50. The Fourier H^s norm is equivalent to the sum of L2 norms of derivatives through3 and the alpha Gagliardo seminorms of derivatives of order3. The equivalence follows from Plancherel and the positive finite integral integral_R2 |exp(i xi.h)-1|^2 |h|^(-2-2alpha) dh = C_alpha |xi|^(2alpha). Finiteness follows from min(4,|xi|^2|h|^2), and positivity follows for xi nonzero. Products differentiated three times contain bounded Lipschitz coefficient factors. In their fractional seminorm, split each product difference into the coefficient difference and the function difference. The coefficient difference contributes at most C|X-Y| times the function, whose squared near-diagonal kernel is integrable because alpha<1; the far-diagonal contribution is bounded by L2. Lower function derivatives also have H^alpha norm bounded by H^s. The log coordinate map and its inverse have bounded derivatives through4 and are bi-Lipschitz on a slightly larger fixed patch. The same difference estimates and change of variables compare the local fractional integrals; a cutoff supported strictly inside that larger patch controls all pairs with one point outside it by their positive separation or the ordinary global cutoff estimate. This proves the needed boundedness. Constants may depend on a, the fixed supports and background. No uniformity in a or a quantitative inverse bound is claimed.

It follows that ||chi_+ U[h_n^raw].grad rho0||_Y<=C. This order-zero term cannot cancel the linear growth in (6).

## Exact strain and normalization correction

For parity-compatible compact smooth h supported away from zero, the canonical strain is

 Sigma(h)=(1/pi) integral_R2 h(X) sin(3 theta)/r^3 dX.              (7)

To recover its sign and factor, write F_l(r)=(1/pi)integral_0^(2pi)h(r,theta)sin(l theta)d theta. The sin2theta coefficient of partial_x h is (F3'+3F3/r+F1'-F1/r)/2. Green's formula gives the r^2 sin2theta coefficient of psi as one quarter of its r^(-1) integral. Integrating by parts, the F1 terms cancel, and this coefficient is (1/2)integral F3/r^2 dr. Since r^2 sin2theta=2xy, differentiation yields (7). All endpoints vanish because the support is compact and separated from zero.

After changing x to z on each reflected patch, the kernel and Jacobian in (7) are smooth on a fixed compact set. Integration by parts N times in z, using partial_z Phi=D>0 and zero boundary terms, gives for every integer N>=0

 |Sigma(h_n^raw)|<=C_N n^(-s-N).                                  (8)

Choose a fixed real h0 in C_c^infinity, parity-compatible, supported in 1<r<2 away from both axes, with Sigma(h0)=1 and J(h0)=0. Such a function exists explicitly: take eta>=0, nonzero and smooth in (1,2), and a nonnegative smooth angular phi invariant under both coordinate reflections, supported away from the axes, with phi sin^2(3theta) not identically zero. Then eta(r)phi(theta)sin(3theta) has the density parity and positive strain by (7). Divide it by that positive real integral. It has the required global factorization. Its local L image near Q has finite H^s norm: the source is smooth compact, its canonical velocity is smooth, and the background on Q has the finite regularity just used.

Set h_n=h_n^raw-Sigma(h_n^raw)h0. Then J(h_n)=Sigma(h_n)=0 exactly, so the rank-one term of Lh_n vanishes. The corrections have bounded frozen graph norm and, by (8), change the localized L output by a term tending to zero. Equivalently one can bound the raw rank-one term first by (8), since its fixed localized background coefficient is C4. Thus (1) holds for the complex sequence.

Finally L, T, J and Sigma have real coefficients. Real and imaginary parts of h_n obey the same homogeneous constraints and have bounded input norms. The squared complex output norm is the sum of the two squared real output norms. For each n select the part with larger output norm. Its output is at least 1/sqrt(2) of the complex output and tends to infinity. This yields a real sequence. If a parity-compatible cutoff is desired, sum the reflected copies of chi_+; bounded multiplication by chi_+ recovers the positive patch and hence the same divergence.

The result follows. A compact map on the frozen graph space would be bounded, and subtraction of T changes the localized estimate by a bounded term. No assertion about the spectrum or invertibility of the full IPM linearization follows.

## Verification scope

The analytic phase construction, Sobolev bounds, strain correction and domain argument require mathematical review. Exact algebra alone cannot certify them. New code will reconstruct the two conjugations and phase mismatch, derive the strain integration coefficients, verify the complete imported source dependencies, and check (3) by NPZ/Fraction/Arb and separate integer-hex/fmpq/mpmath.iv calculations. Actual Opus5.5 must receive the full proof and executed evidence, with all substantive objections resolved by a later own adjudication. Any changed foreign input is replaced only by an already pinned byte-identical local snapshot, with both identities recorded. No heavy computation is added while the derivative-norm queue is active.
