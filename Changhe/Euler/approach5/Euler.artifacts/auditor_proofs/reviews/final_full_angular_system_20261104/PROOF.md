# Final recheck of the full angular system

Status: CONFIRMED in A3257 at the exact existing angular-system scope below, after the complete reconstruction postread and complete existing C comparison. No new theorem direction or unconditional nonexistence result.

## 1. Exact class and claims

Let J(y1,y2,y3)=(-y2,y1,0), c>0 and omega be a finite real number. Let U in C^2(R^3;R^3), P in C^1(R^3) solve

    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0,
    div U=0.

The local infinite-mode identities below do not require decay. For the angular support and linear-kernel conclusions assume additionally that U tends uniformly to zero at infinity. For the pressure-torque integral assume 0<c<1/2 and bounded U; uniform sublinearity, meaning sup_(|y|>=R)|U(y)|/|y|->0 as R->infinity, suffices by the same radial argument. No symmetry or finite Fourier support is assumed.

This audit rechecks the statements of A032-A034, the linear-kernel part of A046, and A073-A074. It does not recertify the other statements of in the team records or any numerical experiment. Its proof dependencies are elementary Fourier theory, the whole-space Poincare lemma, harmonic Liouville, and, only for the canonical pressure-mode statement, the separately audited pressure normalization A031.

## 2. Moving frame and the complete system

Write r=(y1^2+y2^2)^(1/2)>0, z=y3 and U=R(theta)u in the orthonormal cylindrical frame, where R(theta)=exp(theta J). Differentiating gives

    ((Jy).grad)U-JU=R(theta) partial_theta u,
    ((U.grad)U)_cyl
       =u_r partial_r u+(u_theta/r)partial_theta u+u_z partial_z u
          +(u_theta/r)(-u_theta,u_r,0).

Thus the rotation contribution is exactly -omega partial_theta u. Let (a_m,b_m,w_m) and p_m be the angular Fourier coefficients of (u_r,u_theta,u_z) and P, with phases exp(im theta). Put D=r partial_r+z partial_z and

    T_(k,l)f=a_k partial_r f+(il/r)b_k f+w_k partial_z f.

For every integer m, the equations are

    (1-c-im omega)a_m+cD a_m+partial_r p_m
       +sum_(k+l=m)(T_(k,l)a_l-b_k b_l/r)=0,
    (1-c-im omega)b_m+cD b_m+(im/r)p_m
       +sum_(k+l=m)(T_(k,l)b_l+a_k b_l/r)=0,
    (1-c-im omega)w_m+cD w_m+partial_z p_m
       +sum_(k+l=m)T_(k,l)w_l=0,
    partial_r(r a_m)/r+(im/r)b_m+partial_z w_m=0.

These follow by taking coefficients of the full-field equations. On compact subsets of r>0, two angular derivatives of u are bounded, hence u_m=O((1+|m|)^-2) uniformly. Each first spatial derivative is square integrable in the angle. For each fixed output m, the product coefficient is an absolutely convergent convolution by Cauchy-Schwarz of its two square-summable coefficient sequences. Local uniform bounds also hold. There is no truncation, no exchange with an unproved sum of second derivatives, and no assumption that a largest occupied mode exists. Reality gives u_(-m)=conjugate(u_m).

The equation gives grad P in C^1, so P is C^2. In the moving frame the coefficient matrix of DU is

    G_m = [[partial_r a_m, (im a_m-b_m)/r, partial_z a_m],
           [partial_r b_m, (im b_m+a_m)/r, partial_z b_m],
           [partial_r w_m, im w_m/r,       partial_z w_m]].

Taking divergence of the original equation cancels the two rotation terms and gives -Delta P=tr((DU)^2). Consequently

    (partial_r^2+r^(-1)partial_r-m^2/r^2+partial_z^2)p_m
       =-sum_(k+l=m)tr(G_k G_l).

The same convolution argument applies. The curl coefficients are

    Omega_(r,m)=(im/r)w_m-partial_z b_m,
    Omega_(theta,m)=partial_z a_m-partial_r w_m,
    Omega_(z,m)=partial_r(r b_m)/r-(im/r)a_m.

The local pressure equation permits harmonic summands. Under the separate canonical-pressure theorem, the canonical scalar pressure is the contracted Newton-kernel operator applied to U tensor U, modulo constants; its gradient is unique. Here tensor rotations mean F(y) maps to R F(R^(-1)y) R^T. This contracted tensor-to-scalar operator is rotation covariant. Individual fixed-index Riesz transforms are not scalar operators commuting with every rotation. Thus absent tensor modes imply absent nonzero pressure modes only after canonical normalization; the arbitrary scalar constant remains in mode zero.

## 3. Axis and mean-field checks

For a Cartesian C^k scalar f, its Taylor polynomial in y1,y2 at (0,0,z) of degree k has no angular frequency larger than k. The remainder is o(r^k) locally uniformly in z. Hence f_m=O(r^min(|m|,k)) and f_m=o(r^k) if |m|>k. Applying this to

    U1+iU2=exp(i theta)(u_r+i u_theta),
    U1-iU2=exp(-i theta)(u_r-i u_theta)

gives the shifted indices m+1 and m-1 in the source's axis bounds. These necessary conditions do not characterize Cartesian regularity; in particular C^2 alone does not give r^|m| decay at the axis for arbitrarily large |m|.

Let a,b,w be the mean cylindrical components, u' their fluctuations, and Q_ij=<u'_i u'_j>. By Parseval, Q_ij=sum_(m!=0)(u_i)_m(u_j)_(-m). Divergence-free convection is the divergence of U tensor U. Taking its angular average, including derivatives of the cylindrical frame, gives

    (1-c)a+cDa+(a partial_r+w partial_z)a-b^2/r+partial_r p0
       =-partial_r(rQ_rr)/r-partial_z Q_rz+Q_(theta theta)/r,
    (1-c)b+cDb+(a partial_r+w partial_z)b+ab/r
       =-partial_r(r^2 Q_(r theta))/r^2-partial_z Q_(theta z),
    (1-c)w+cDw+(a partial_r+w partial_z)w+partial_z p0
       =-partial_r(rQ_rz)/r-partial_z Q_zz,
    partial_r(ra)/r+partial_z w=0.

The angular derivative has zero mean; the quadratic fluctuation terms need not vanish. The mean therefore solves a forced axisymmetric system. Applying an unforced nonrotating Liouville theorem to it would drop part of the equation. The explicit factor im omega is imaginary in a mode energy pairing, so it gives no real coercive term by itself. This observation does not rule out another integral argument using additional constraints.

## 4. Complete flows and angular momentum

Put B=(cI-omega J)y+U and Gamma=(Jy).U=r u_theta. Multiplying the theta equation by r and using B r=cr+u_r gives

    (1-2c)Gamma+B.grad Gamma+partial_theta P=0.

If U is bounded by M, B has linear growth and its flow Phi_t is complete. Variation of constants gives

    |Phi_(-t)x|<=exp(-ct)|x|+(1-exp(-ct))M/c,  t>=0.

Thus each backward orbit is compactly contained. For uniform sublinearity the bound B(y).y>=c|y|^2/2 outside a sufficiently large ball supplies the same trapping conclusion, and linear growth supplies completeness. When 0<c<1/2, Gamma and partial_theta P are bounded on that orbit closure and

    Gamma(x)=-integral_(-infinity)^0 exp((1-2c)s)
                     partial_theta P(Phi_s x) ds.

The integral is absolutely convergent; its omitted past boundary term is zero. Axisymmetric pressure therefore gives Gamma=0, including the axis by continuity. This statement alone does not make the other velocity components axisymmetric. The mean version uses the different field cy+Ubar and the Reynolds torque as its source; it does not use the full carrier trajectories.

For omega!=0, let R_t=exp(omega tJ), V(t,y)=R_t U(R_t^(-1)y), Q(t,y)=P(R_t^(-1)y). Direct differentiation gives

    partial_t V+(1-c)V+(cy+V).grad V+grad Q=0.

The period T=2pi/|omega| need not be minimal. A characteristic has the form y(t)=R_t Phi_t x, so its time-T map is exactly Phi_T. A nonstationary orbit of minimal carrier period p consists of periodic points of this map precisely when p/T is rational. Neither periodic coefficients nor this conjugacy implies convergence of almost every backward orbit to a periodic point. That remains the separate Liu Theorem 7.3 premise.

## 5. The linear kernel, support rule and odd transformations

Define Lambda V=(1-c)V+((cI-omega J)y).grad V+omega JV. Suppose a decaying C^2 divergence-free V satisfies Lambda V+grad p=0 for p in C^1(R^3). Taking curl gives, with W=curl V,

    W+((cI-omega J)y).grad W+omega JW=0.

Along y(s)=exp(cs)exp(-omega sJ)y, the vector exp(s)exp(omega sJ)W(y(s)) is constant. As s tends to minus infinity, y(s) tends to zero and W remains bounded there, so that constant is zero. Hence W=0. Since div V=0, every component is entire harmonic; boundedness and decay give V=0. Real and imaginary parts extend the argument to complex V. This is a kernel statement, with no assertion of a bounded inverse or a spectral gap.

For the full nonlinear U use the global rotation projection

    V_m(y)=(2pi)^(-1) integral_0^(2pi) exp(im theta)
                       R_theta U(R_theta^(-1)y) dtheta.

These fields are globally C^2, divergence-free and decaying, including at the axis. Rotation covariance gives

    Lambda V_m+grad P_m+N_m=0,
    N_m=sum_(k+l=m)(V_k.grad)V_l.

At each fixed Cartesian point the convolution is absolutely convergent by the Cauchy-Schwarz argument in Section 2. N_m is C^1 by its original integral definition, without differentiating the series. If curl N_m=0, the whole-space Poincare lemma gives N_m=grad phi_m. The preceding kernel result then forces V_m=0. Thus every occupied mode has nongradient quadratic forcing and S subset S+S, where S={m:V_m is not identically zero}. The inclusion is automatic if 0 belongs to S. For every positive integer L, it excludes nonempty supports contained in L(2Z+1), but does not exclude every finite support.

Finally let sigma be orthogonal, commute with J, and satisfy T_sigma U=-U, where T_sigma U(y)=sigma U(sigma^(-1)y). The linear and pressure terms commute with this transformation while N(T_sigma U)=N(U). Subtracting the transformed equation from the original leaves

    2 Lambda U+grad(P-T_sigma P)=0.

The kernel result gives U=0. No finite-order property of sigma is used, and the argument permits determinant minus one. These are conditional symmetry exclusions, not a symmetry assumption on every profile.

## 6. Final comparison, dependencies and scope

The complete earlier independent reconstruction, 144 lines, has been freshly read. Its mathematical Sections 1-5 are reproduced above, with two explicit precisions: the odd frequency lattice uses a positive integer L, and tensor modes use the tensor rotation action. The complete179-line FOURIER_SYSTEM source and105-line ANGULAR_SUPPORT source have also been freshly read. The complete54-line existing C comparison of 2026-11-04T06:34:32Z was read and its six mathematical items checked again. This is file collaboration with the existing configured model agent; actual provider execution is independently unattested. No new model client is used.

The three restricted readings in that comparison remain necessary. First, individual fixed-index Riesz transforms are not scalar rotation-invariant operators; the contracted tensor operator is covariant, and local Poisson equations alone leave harmonic freedom. Second, a largest occupied mode does not by itself settle the full coupled system. For example the finite set {-2,-1,1,2} satisfies S subset S+S, so the support inclusion alone cannot exclude every finite support; this set is only a combinatorial test, not a realized Euler field. Third, the scalar radial calculation is not a bounded-inverse or spectral-gap theorem for the full constrained vector operator. No higher-order Lyapunov statement is recertified by this recheck.

No diagnostic log or script is a premise of the present proof or has been freshly inspected or run here. In particular, the old diagnostic labels and selected polynomial examples are not substitutes for the chain-rule and covariance derivations above. The final pressure-mode statement uses the actual canonical-pressure theorem only under its stated uniform velocity decay; all other displayed mode equations are local identities independent of pressure normalization. The torque integral uses compact containment of each actual backward orbit and 1-2c>0, so its boundary term is justified without a global pressure bound.

The equations include every integer angular mode and retain every quadratic convolution. C2 regularity gives the stated local convergence and finite-order axis conditions, not arbitrarily high-order vanishing. No symmetry, finite angular support, small omega, rational-angle condition or commensurate period is imposed on the general profile. Odd-transformation exclusions and axisymmetric-pressure consequences remain explicitly conditional. The zero angular mean of the rotation term does not remove Reynolds stresses. None of these results proves unconditional nonexistence for 2/5<c<1/2 and arbitrary omega.
