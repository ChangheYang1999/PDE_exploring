# Exact weak-axis membership range for the canonical trial residual

This standalone proof is written before new validation computations. Its application remains OPEN until the strict scalar enclosure, independent checks, complete actual Claude Opus 5.5 review and later own adjudication. The object is the exactly joined and normalized modal_v2 trial, not an exact stationary profile or the literal unjoined stored field.

## Statement and definitions

Let rho=x^2 y a(x,y) be the canonical modal trial of modal_repair/PROOF.md. The exact binary64 exponent is k=1615536043799051/9007199254740992, so 0<k<1/2. The finite factor a has 260 cosine modes, the exactly recomputed order-six joins and the exact real correction z to the leading exterior coefficient A_(0,0). This correction imposes Sigma(rho)=psi_xy(0)=3/k-1. The stream and velocity are the full-plane canonical ones:

 -Delta psi=partial_x rho, U=(-psi_y,psi_x), U=o(r) at infinity.

Put ell=1/k and epsilon=(ell X+U).grad rho-rho. For a weight parameter b, distinct from the factor a, and s=153/50, define

 T_b f(zeta,y)=exp((1/2-b)zeta)f(exp(zeta),y),
 ||f||Y_(b,s)=||T_b f||H^s(R^2_(zeta,y)).

The H^s norm uses Fourier weight (1+xi^2+eta^2)^s in its squared norm. In particular its zeroth term is integral_(x>0) x^(-2b)|f|^2 dxdy. Then, for every nonnegative real b,

 epsilon|_(x>0) belongs to Y_(b,153/50) if and only if 2k<b<5/2.       (1)

The inclusion is qualitative: no explicit ceiling for this norm is claimed. The upper endpoint uses the accepted nonzero center-axis coefficient Q of canonical_axis_residual. The lower endpoint requires a new independent nonzero enclosure for the exterior sine-3 coefficient derived below. Until that enclosure is accepted, the lower-end necessity is conditional. This is a forcing-space classification for this trial alone. It gives no inverse, range compatibility, error bound for X3, nonlinear closure or decisive PDE endpoint.

## Differentiated center estimates and exact cancellation

The exact inner formula for a is 1 plus finitely many r^(2j) smooth angular factors, 1<=j<=7, and r^bi times log polynomials of degree at most6, with bi>50. Consequently for every Cartesian derivative of order d<=5,

 |D^alpha(a-1)|<=C_alpha r^(2-d) near0.                  (2)

These estimates follow by differentiating the finite formula on the punctured plane. They do not assert that the homogeneous angular terms are Cartesian polynomials or that a is C5 at0.

The canonical Green solution has differentiated expansion

 U=(-c x,c y)+U_rem, c=3/k-1,
 |D^alpha U_rem|<=C_alpha r^(3-d)(1+|log r|^M), d<=5,     (3)

for some finite integer M. Here is a direct justification, without differentiating a qualitative big-O statement. The density's leading term is exactly x^2y, of degree3; all further inner density exponents are at least5. Its finite source modes have powers of degree at least2. In a mode n=2,4,6,... the two Green integrals applied to any power times a log polynomial give a finite combination of powers times log polynomials; a zero integration exponent can add one log power. The particular stream exponents are the density exponents plus1, hence at least4, and the particular velocity exponents at least3. The growing harmonic stream terms have even degrees n>=2, and there is no singular harmonic term at0. The sole degree2 harmonic term is cxy. All remaining harmonic velocities have degree at least3. Differentiation of this finite representation through5 proves(3), with a finite common M. The accepted exact normalization fixes precisely this linear term.

Parity gives U_rem,1=x v1 and U_rem,2=y v2. Their quotient factors satisfy, uniformly up to either axis,

 |D^alpha v_i|<=C_alpha r^(2-d)(1+|log r|^M), d<=4.       (4)

For example when |x|<=|y|, U_rem,1/x=integral_0^1 partial_x U_rem,1(tx,y)dt, including derivatives. Radii along this segment are comparable to r, so(3) applies. In the complementary cone |x|>=r/sqrt2 direct division and the product rule apply. The argument for U_rem,2/y exchanges the axes. This also justifies all quotients at nonzero axis points.

Set A=2/k-1 and D=4/k-1. Then ell X+U=(-Ax,Dy)+U_rem, and -2A+D-1=0 exactly. Direct differentiation therefore gives

 epsilon=x^2 y B_0,
 B_0=-A x a_x+D y a_y+v1(2a+x a_x)+v2(a+y a_y).         (5)

The missing constant multiple of a cancels exactly by the scalar normalization; it is not a small numerical defect. Equations(2),(4) and the product rule show |D^alpha B_0|<=C r^(2-d)(1+|log r|^M) for d<=4. For E_x=x partial_x, all p+q<=4 consequently satisfy

 |E_x^p partial_y^q epsilon|<=C x^2 r^(3-q)(1+|log r|^M). (6)

Every y derivative preserves x^2. Expanding E_x^p into x^j partial_x^j preserves the same factor and supplies the needed powers x<=r. The estimates use derivatives of a only through5 and of the velocity through5.

## Differentiated exterior estimates

Let t_b be the exact last log knot and R=exp(t_b). The exterior factor is a finite sum of pure powers r^alpha with smooth cosine coefficients, with ten exponents

 alpha=k-3-j(1-k)-2l,
 (j,l)=(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2),

and an additional r^-bo times log polynomial, bo>120. The leading factor is a_0=r^(k-3)A_0(theta); all other exponents are at most2k-4, except that the much faster r^-bo term may have log factors. Thus for d<=5,

 |D^alpha a|<=C r^(k-3-d),
 |D^alpha(a-a_0)|<=C r^(2k-4-d).                        (7)

No log occurs at either of the two leading pure powers. Finite logarithms at strictly smaller exponents are absorbed by their positive exponent gaps.

The canonical Green formula gives |D^alpha U|<=C r^(k-d), d<=5. Indeed each particular velocity term has the corresponding density exponent, at most k, possibly with finite log factors only at strictly smaller exponents; the homogeneous decaying velocities start with r^-3. There is no resonance at the leading exponent because k+1<2, below every allowed positive even stream frequency. The canonical gauge excludes growing harmonic additions. Division by the odd coordinate, using the two-cone argument above at large radii, gives for w1=U1/x, w2=U2/y,

 |D^alpha w_i|<=C r^(k-1-d), d<=4.                     (8)

The exact exterior factor identity is

 epsilon=x^2y B_infinity,
 B_infinity=(3/k-1)a+(1/k)r partial_r a
                      +w1(2a+x a_x)+w2(a+y a_y).        (9)

The first two terms annihilate a_0 since (3/k-1)+(k-3)/k=0. Equations(7),(8) imply |D^alpha B_infinity|<=C r^(2k-4-d), d<=4, and hence

 |E_x^p partial_y^q epsilon|<=C x^2 r^(2k-3-q), p+q<=4. (10)

Again these are derivatives of exact finite formulas, not formal differentiation of an undifferentiated error term.

## Sobolev sufficiency

Use the smooth radial dyadic partition from weak_axis_compact_mapping: epsilon_j=chi(r/lambda)epsilon, lambda=2^j. On each annulus a is C6 with locally bounded piecewise next derivatives, and the finite Green formula gives the velocity derivatives required above. Exact order-six joins remove interface distributions. Thus the residual is at least C4 there; its global x^2 factor has a C4 quotient on that annulus, including the nonzero axes. Pullback x=exp(zeta) never reaches x=0 at finite zeta.

The Jacobian is dzeta dy=dxdy/x. Differentiation in zeta conjugates to E_x+(1/2-b). The axis integral on a lambda shell is finite for b<5/2 because integral_0^(2lambda) x^(4-2b)dx=(2lambda)^(5-2b)/(5-2b). From(6),(10), including derivatives of chi, for p+q<=4,

 ||partial_zeta^p partial_y^q T_b epsilon_j||L2
 <= C_b lambda^(6-b-q)(1+|log lambda|^M), lambda<=1,
 <= C_b lambda^(2k-b-q), lambda>=1.                     (11)

The Fourier derivative characterization puts each shell in H4. At small lambda its H3 and H4 norms are bounded respectively by C lambda^(3-b) times the log factor and C lambda^(2-b) times that factor. Fourier Holder interpolation with theta=3/50 gives an H^(153/50) bound C lambda^(6-b-s)(1+|log lambda|^M). Since b<5/2, the exponent6-b-s>11/25 is positive. These shell norms sum geometrically despite the finite log powers.

At large lambda the H4 shell norm is at most C lambda^(2k-b), which sums when b>2k. Finitely many intermediate shells have finite H4 norms by the same axis-factor integral and annular regularity. Absolute convergence of the H^s shell norms, completeness and local finiteness of the partition identify their sum with T_b epsilon. This proves sufficiency in(1). There is no claim of an explicit uniform constant as b approaches either endpoint.

## Nonzero leading exterior coefficient and the lower endpoint

Put tau=log(r/R), gamma=2k-1, a_e=k+1, m=2n, and nu_j=2j+1. Expand the two leading density coefficients as

 rho=R^3[e^(k tau) sum_(j=0)^260 d_j sin(nu_j theta)
          +e^(gamma tau) sum_(j=0)^260 d1_j sin(nu_j theta)+lower terms].

The exact d_j and d1_j follow by multiplying each cosine coefficient by cos^2(theta)sin(theta). For cosine mode m0, the four sine frequencies are1+2m0,1-2m0,3+2m0,3-2m0, each with signed weight1/8; negative frequencies change sign. The leading raw cosine coefficient is Aout[m0,0]+z delta_(m0,0), and the second is Aout[m0,1]. Set d_261=d1_261=0.

For n=1,...,261 the leading source coefficient is

 F_n=[(a_e-2n)d_(n-1)+(a_e+2n)d_n]/2.

The radial Poisson equation gives a stream term R^4 e^(a_e tau)F_n/[(2n)^2-a_e^2]. Therefore the leading coefficients of U_r/r and U_theta/r are R^2 e^((k-1)tau) times v_n cos(2n theta) and w_n sin(2n theta), where

 v_n=-2n F_n/[(2n)^2-a_e^2],
 w_n=a_e F_n/[(2n)^2-a_e^2].                            (12)

Every denominator is strictly positive. Equivalently q_plus=F_n/(a_e+2n), q_minus=-F_n/(a_e-2n), v_n=-(q_plus+q_minus)/2, w_n=(q_minus-q_plus)/2, as derived by the two Green integrals.

The linear leading rho term cancels since k/k-1=0. Among the ten density exponents beta=k-j(1-k)-2l and the correction3-bo, only beta=gamma contributes to the remaining linear term at exponent gamma, and only the pair(k,k) contributes to a particular product beta+beta'-1=gamma. Every transient product has exponent beta-2n-2<=k-4<gamma. All other terms have strictly smaller exponents, with finite log-polynomial factors. Thus, uniformly in theta,

 epsilon=e^(gamma tau) Phi(theta)+o(e^(gamma tau)),      (13)

where Phi is the finite sine polynomial

 Phi=R^3(gamma/k-1) sum_j d1_j sin(nu_j theta)
    +R^5[(sum_n v_n cos(2n theta))(sum_j k d_j sin(nu_j theta))
         +(sum_n w_n sin(2n theta))(sum_j nu_j d_j cos(nu_j theta))]. (14)

This derivation retains the full canonical homogeneous terms among the strictly lower exponents, so none is omitted in(13).

Let e_1 be the sine-3 coefficient of Phi. A previous complete exterior computation suggests e_1 is close to -0.0009662164638762; that saved display is diagnostic only. New independent calculations must prove the strict rational window

 -966216463877/10^15 < e_1 < -966216463875/10^15.          (15)

The primary path reads raw NPZ binary64 values as exact Fractions, projects the two density vectors, solves(12) through its Green q_plus/q_minus expressions, and takes an Arb Laurent polynomial convolution. The second path independently decodes integer hexadecimal JSON into exact fmpq values, reconstructs both projections, solves the radial Poisson expression in(12) directly, and sums only the product-to-sum frequency contributions to sine3 using mpmath.iv. Both use the same already audited interval enclosing the exact normalization scalar z; this is an explicit analytic dependency. It is not a free parameter selection or an estimate from the rounded stored joins. Each path must enclose its whole output strictly inside(15), and exact data identities and exponent gaps must agree. The two algorithms do not make two independent analytic proofs of(13).

If(15) is accepted, Fourier orthogonality implies Phi is not identically zero. Its continuity and finite sine representation yield a closed angular interval I strictly inside x>0 and away from both axes on which |Phi|>=c>0. To justify the half-plane choice, Phi inherits even-x, odd-y parity; a nonzero value has a reflected nonzero value with x>0, and continuity supplies a point off the axes. The uniform remainder in(13) then gives |epsilon(r,theta)|>=c' r^gamma on I for all sufficiently large r. Since cos(theta) is bounded above and below by positive constants on I, the zeroth squared norm is bounded below by a positive constant times

 integral_R1^infinity r^(2gamma-2b+1)dr
                  = integral_R1^infinity r^(4k-2b-1)dr. (16)

It diverges exactly when b<=2k, logarithmically at equality. This proves the lower-end necessity without differentiating the asymptotic remainder or approximating angular samples.

## Upper endpoint and scope

The accepted canonical_axis_residual theorem proves epsilon_xx(0,y)/2=Q y^3+o(y^3), with strict6.087210e-6<Q<6.087213e-6. It constructs a fixed positive-y rectangle on which |epsilon|>=c x^2. Thus the zeroth squared norm diverges for b>=5/2, including equality. That exact coefficient uses the origin boundary term in the quartic stream and the exactly normalized joined trial; its full evidence is inherited and rehashed, not recomputed in this result.

Combining this upper obstruction, the new lower obstruction(16) and sufficiency proves(1) for all b>=0. The accepted graph-domain obstruction for the full variable transport in variable_transport_graph_obstruction is unchanged throughout this interval. Membership does not supply a bound for the norm, solvability in the frozen range, a full inverse on a different domain, any nonlinear estimate, or any exclusion of an exact nearby profile. The PDE verdict remains UNRESOLVED.
