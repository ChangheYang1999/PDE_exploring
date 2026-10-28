# A uniform inverse for the exact origin normal operator

## Space and theorem

Let k,ell,A,D,Sigma,delta,s_0,sigma and p(theta) have the exact values of proof 129. Let s_-(theta) be smooth, reflection invariant, nondecreasing on the first quadrant, equal to s_0=41/20 near the horizontal directions and to sigma=25/4 on a fixed open vertical sector. The limiting order of proof 130 satisfies these requirements.

On C=R_t times S^1 define the closed Hilbert space X_- of bulk functions v with the physical parity, with

 v in H^{s_-(theta)}(C),
 chi_y v/p in H^sigma(C),
 (v/p)|_(vertical axis)=0,

where the sector cutoff chi_y equals1 near the vertical directions and its support and transition lie in the constant-order region. The cofactor is even in its normal coordinate. The sum of the bulk and cofactor norm squares is used. A fixed equivalent dyadic norm is also allowed. Its constants are independent of translation in t. The ambient functions are v=h/r^(3+delta); the physical factor is a convention defining this normal space, not the actual far-field weight.

Let

 T_0=q_0 partial_t+vartheta_0 partial_theta+(3+delta)q_0-1,
 q_0=-A cos^2(theta)+D sin^2(theta),
 vartheta_0=Sigma sin(theta)cos(theta),
 D_0={v in X_-:T_0 v in X_- in distributions}.

Put m_x=(3ell-7)/10>0. For every compact subset K of the complex half-plane Re lambda>-m_x there is a finite C_K such that

 ||v||_(X_-)<=C_K||(T_0-lambda)v||_(X_-), lambda in K,   (1)

and T_0-lambda:D_0->X_- is bijective. Its inverse also maps boundedly into D_0 with its graph norm, locally uniformly in lambda.

Fourier transformation in t gives the exact family N_(xi,lambda) of proof 129. If H_xi denotes the fiber norm obtained by transforming the displayed cylinder norm, then

 sup_(xi real, lambda in K) ||N_(xi,lambda)^(-1)||_(H_xi->H_xi)<infinity. (2)

The norm H_xi uses (1+xi^2+eta^2) in the cofactor Sobolev factor and the corresponding variable-order bulk reduction. It is not the unweighted angular norm with a constant presumed independent of xi. No numerical value for C_K is claimed. This result concerns the exact origin normal operator only.

## Finite-time transport on the normal space

The normal transport is the exact physical linear field V_0=(-Ax,Dy), with scalar operator V_0.grad-1. Its conjugation to the bulk variable is T_0. The cofactor identity of proof 129 gives the uncut cofactor equation

 partial_tau u=q_0 partial_t u+vartheta_0 partial_theta u+delta q_0 u.

The coefficients are smooth with uniformly bounded cylinder derivatives. Their parity and axis tangency preserve the even cofactor and its zero trace. Since vartheta_0 s_-'(theta)>=0, the finite-time energy argument of proof 126 applies without an additional geometric assumption: for the normal transport group S_tau, tau>=0,

 ||S_tau||_(X_-->X_-)<=exp(omega tau)                     (3)

in a fixed equivalent dyadic norm, for a finite omega. Only the finite-time bound is used here, not its large-lambda inverse theorem.

To specify this use, differentiate the dyadic bulk square. Its order derivative contributes exactly

 -2 j log(2) integral vartheta_0 s_-' |2^(j s_-)Delta_j v|^2,

which is nonpositive. The bounded-coefficient commutator estimate and the constant-order cofactor chart give an upper bound by a constant times the total square norm, including the cutoff-overlap term. All coefficients here have arbitrarily many bounded derivatives, so the finite-regularity proof of proof 126 applies in particular. A dense core is formed by smooth functions with compact t support and exact cofactor trace correction. The flow preserves the trace and finite-time bounds; density gives (3) and strong continuity. No embedding of this normal space in the actual global physical remainder space is assumed. The ordinary unweighted bulk L2 space suffices as an ambient space to identify its distributional transport group.

For a solution of (T_0-lambda)v=f in X_- one has, for any finite T>=0,

 v=exp(-lambda T)S_T v-integral_0^T exp(-lambda a)S_a f da. (4)

This follows first on the core by differentiation along the flow. It also holds for the maximal domain, either by the ambient L2 generator identity or by approximation of the smooth transport equation. Since the lowest order is greater than2 in dimension2, one can alternatively integrate the C1 representative when v and f are already in X_-.

## Uniform control on a vertical sector

On y>0 set tau=log y and z=x/y. Write

 h=x^2 y^(1+delta) w(tau,z).

Then r=y sqrt(1+z^2), t=tau+(1/2)log(1+z^2), and w=(1+z^2)^(delta/2) v/p. A direct chain rule, using (V_0.grad-1)(x^2 y)=0, gives exactly

 (V_0.grad-1-lambda)h
   =x^2 y^(1+delta)[D partial_tau-Sigma z partial_z+delta D-lambda]w. (5)

On each bounded z strip this coordinate change and its smooth multipliers are bounded isomorphisms of isotropic H^sigma spaces, with constants independent of the tau frequency. This is a fixed smooth diffeomorphism with bounded derivatives and bounded inverse derivatives. Its constants are not taken to be1.

Choose z_0>0 so that |z|<=2z_0 stays in the fixed cofactor sector. Transform the cofactor forcing there and multiply by an even smooth cutoff equal to1 on |z|<=z_0 and supported inside |z|<2z_0. Call its zero extension F_y. It belongs to H^sigma(R^2), is even in z and has zero value at z=0, with norm at most C||f||_(X_-). It also belongs to the low space

 H_y=L2(|z|^(-9/2) d tau dz).

Here is an elementary membership check. Evenness and H^sigma regularity give zero first derivative trace. Thus F_y(tau,z)=integral_0^z(z-a)partial_z^2 F_y(tau,a)da. The H^1_z embedding bounds the supremum in z of the second derivative in L2_tau by C||F_y||_H^3. Consequently the weighted integral near0 is bounded by C integral_0^(2z_0) z^(-1/2)dz times ||F_y||_H^3 squared. Away from0 the compact z support is harmless. This proves low membership and its norm bound, rather than imposing it as an independent condition on the data.

Put nu=Re lambda. The two gaps required by the selected vertical inverse of proof 102 are

 kappa_y=(7/4)Sigma-delta D+nu,
 kappa_2=(3/2)Sigma-delta D+nu.

They are positive whenever nu>-m_x, because

 (3/2)Sigma-delta D-m_x=(s_0-delta)Sigma=Sigma/4,
 kappa_y=kappa_2+Sigma/4.                                (6)

Thus the maximal low inverse is

 w_y=-integral_0^infinity exp((delta D-lambda)a)
                       F_y(tau+D a,exp(-Sigma a)z)da.   (7)

It converges in H_y. Proof 102 proves w_y in H^sigma on every fixed bounded strip, with

 ||w_y||_(H^sigma(|z|<z_0))<=C_K||F_y||_H^sigma.         (8)

Its proof differentiates twice in z, obtaining contraction with rate kappa_2, removes both affine integration constants by the low weight, then recovers tangential regularity from D!=0. This is an isotropic estimate in(tau,z), so it already includes every radial frequency. Replacing the real zeroth-order constant in that proof by delta D-lambda changes the semigroup norm only through nu; the tangential bootstrap uses the bounded number |delta D-lambda|. Hence its constants are uniform for lambda in K. The same proof also shows w_y is even and has zero value and first derivative at z=0.

For |z|<=z_0, formula(7) samples F_y only at smaller |z|. Its restriction is therefore independent of the extension outside the original sector. At each fixed tau frequency, its difference from the solution of proof 129 is a homogeneous vertical cofactor solution. The latter has exponent alpha=((delta+i xi)D-lambda)/Sigma with Re alpha<2. It cannot be even, have zero value and belong to H^sigma unless its coefficient is zero, as proved in proof 129. Thus (8) bounds the actual normal-family solution on this sector, not an unrelated chosen local solution.

This comparison can initially be made for data whose t Fourier transform has bounded support. The fixed-frequency theorem gives an X_- solution for such data, with a finite support-dependent bound. The two coordinate changes preserve the radial Fourier support because their coefficients are independent of tau. Fourier transformation of (7), or the preceding homogeneous uniqueness, identifies the two solutions almost everywhere. Therefore

 ||chi_v v||_(X_-)<=C_K||f||_(X_-)                      (9)

for a smaller fixed vertical cutoff chi_v. Here division by p and the chart transition are included in the left norm.

## Propagation across the finite angular region

Let theta_a>0 be small enough that the horizontal-order plateau contains0<=theta<=2theta_a. Choose an angular cutoff chi_x supported in that plateau and equal to1 on a still smaller neighborhood of each horizontal direction. Put chi_i=1-chi_x. On each first-quadrant component of supp chi_i the angular coordinate is bounded below by a positive number. The exact normal angular flow satisfies

 tan(theta(a))=exp(Sigma a)tan(theta(0)).                 (10)

Consequently there is a finite common T for which the forward image of supp chi_i is contained in the region where chi_v=1. The other quadrants follow by the parity reflections. Choose the vertical cutoff in (9) large enough to contain these images while remaining in its valid sector.

Multiply (4) by chi_i. Since chi_v=1 at every sampled point in its first term,

 chi_i v=exp(-lambda T)chi_i S_T(chi_v v)
          -chi_i integral_0^T exp(-lambda a)S_a f da.

Smooth multiplication is bounded on X_-. Estimates(3) and(9) therefore give

 ||chi_i v||_(X_-)<=C_K||f||_(X_-).                     (11)

This proves the variable-order estimate on the entire intervening angular region. It does not replace a full isotropic norm by an angular or tangential seminorm, and it loses no boundary trace half derivative: it propagates a solution on an open sector for a fixed finite time. Monotonicity of the order is used in(3).

## The horizontal endpoint

On x>0 use tau=log x, z=y/x and h=x^(3+delta)w. The exact transformed operator is

 P_x=-A partial_tau+Sigma z partial_z-c-lambda,
 c=1+A(3+delta)=Sigma+delta A.                           (12)

Apply this to chi_x h. Its forcing is chi_x f+(W_0.grad chi_x)v in bulk notation. The commutator is supported in the region controlled by(11). The cutoff support is entirely in the constant s_0 plateau. After the smooth bounded chart transformation, its forcing F_x is compactly supported in z and belongs to H^s_0(R^2), with norm at most C_K||f||_(X_-).

The localized unknown w_x is in ordinary L2(d tau dz) for bounded-frequency data, because its angular support is compact and the fixed-frequency theorem gives the original bulk norm. It solves P_x w_x=F_x in distributions after zero extension outside the cutoff support; the smooth cutoff has introduced precisely the displayed commutator. The selected inverse of proof 101 with low t weight0 applies. Its low gap is c+nu+Sigma/2>0. Its high gap is exactly

 c+nu+Sigma/2-s_0 Sigma=m_x+nu>0.                        (13)

The high regularization argument there, with the factor exp(-lambda a) added to the semigroup, gives

 ||w_x||_H^s_0<=||F_x||_H^s_0/(m_x+nu).

The imaginary part of lambda is a constant unitary multiplier in this integral and does not affect this bound. Returning to the polar cylinder and reflecting at the other horizontal direction proves

 ||chi_x v||_(X_-)<=C_K||f||_(X_-).                     (14)

The cofactor cutoff is absent on this support. Combining(11) and(14) proves (1), uniformly for bounded-frequency data, with a constant independent of that frequency bound.

## Full domain, surjectivity and uniform fibers

The cylinder norm is invariant under translations in t. Its Fourier decomposition gives the Hilbert direct integral of its angular fiber norms H_xi: for the dyadic norm this follows directly by Plancherel, since the position weights depend only on theta and the Fourier cutoffs become Delta_j(xi,D_theta). The cofactor norm decomposes in the same way. Fiber norms on bounded xi intervals are equivalent to the fixed-parameter norm in proof 129.

For data with bounded radial Fourier support, construct the fiber solution by proof 129. It is measurable and locally bounded in xi and lambda: the explicit integral and endpoint estimates show this, or one can use the resolvent identity since N changes by a bounded smooth multiplier when either parameter changes. This gives the solution to which the preceding estimates were applied.

Now truncate the radial Fourier transform of an arbitrary f in X_-. The solutions form a Cauchy sequence in X_- by(1), uniformly for lambda in K. Their distributional limits satisfy (T_0-lambda)v=f. Therefore v belongs to the stated maximal domain, and T_0 v=f+lambda v gives the graph bound. The maximal domain is closed because T_0 is continuous from X_- to distributions. If (T_0-lambda)v=0, its radial transform satisfies the homogeneous fiber equation almost everywhere; proof 129 forces it to vanish. Thus the inverse is both left and right on the exact maximal domain.

The uniform cylinder bound gives the fiber bound(2) for almost every xi. It holds for every xi because the fixed-frequency inverse depends continuously on xi on a neighborhood of each fixed value. One can prove that continuity in a common angular norm by the resolvent identity for the bounded perturbation i(xi-xi_0)q_0, then use continuity of the fiber norm. A failure at one xi would persist on an interval of positive measure and contradict the direct-integral bound. This completes the theorem.

## Scope and a remaining derivative issue

This proves the uniform normal inverse required in item2 of the theory author H3 outline. It uses exact linear-coordinate identities, two selected frozen low inverses, finite-time propagation in a monotone variable order and the exact maximal-domain fixed-frequency theorem. It does not assume an all-covector vertical energy estimate.

The difference between the actual operator and this normal operator contains small coefficients multiplying first derivatives. Their coefficient decay alone does not make that difference small from X_- to X_-, or from the normal transport graph to X_-. An actual end estimate must control its principal part in the appropriate microlocal or flow realization. No global H3, compact-error estimate, low injectivity or nonlinear existence is proved here.
