# An independent source-disc velocity Hessian bound

Status: the analytic identities and conditional enclosure argument below are proved before numerical implementation. The actual interval bound is pending. No global inverse or existence statement follows.

## Statement and exact inputs

Let the normalized trial density be rho=r^3 sum_(j=0)^260 H_j(t) sin((2j+1)theta), t=log r. On each original logarithmic spline span [a,b], each H_j is a polynomial of degree at most seven in t-(a+b)/2, and H_261=0. All exact polynomial coefficients and the canonical density moments at the span endpoints are enclosed by the dyadic balls in the audited topic31 canonical archive. That archive, its normalization and whole-plane boundary conditions are explicit dependencies. No producer N8 derivative, Taylor model or geometric mask is imported.

For n=1,...,261 put m=2n and define

 I_n(t)=exp(-(m+4)t) integral_(-infinity)^t exp((m+4)s) H_(n-1)(s) ds,
 J_n(t)=exp((m-4)t) integral_t^infinity exp((4-m)s) H_n(s) ds.

The trial's prescribed interior and exterior make these integrals converge. The canonical solution of -Delta psi=rho_x, with no added harmonic term, is

 psi(r,theta)=r^4/2 sum_n (J_n(t)-I_n(t)) sin(m theta).                 (1)

For V=c_l X+(-psi_y,psi_x), D^2 V is the ninety-degree rotation of D^3 psi in the output index. Thus ||D^2 V||_F=||D^3 psi||_F. We will bound this norm on the full radial-angular rectangle from topic84: exact radial cells4096 through4108, theta in [0,3/500], with source center p in [4841405518533377/562949953421312,4841405518533711/562949953421312]. The rectangle covers the upper half of B_(99/2000)((p,0)); reflection in y preserves the derivative norm and supplies the lower half. Radial coverage and the strict sine-cap inequality are checked in both engines. The trial is sufficiently differentiable here, including across its C6 spline joins.

## Canonical moment and stream identities

Differentiation gives I'=-(m+4)I+H_(n-1) and J'=(m-4)J-H_n. The sine-m coefficient of rho_x is

 r^2/2 [(D+4-m)H_(n-1)+(D+4+m)H_n], D=d/dt.

This follows from cos(theta)sin(f theta) and sin(theta)cos(f theta) product-to-sum identities applied to rho_r and rho_theta/r. Applying -Delta to (1) uses Delta[r^4 W(t)sin(m theta)]=r^2[((D+4)^2-m^2)W]sin(m theta). The two first-order moment equations then give exactly rho_x. The moment definitions impose the canonical inner and outer Green boundary conditions, so no homogeneous ambiguity is introduced. This proves (1), also obtainable by integrating the radial Green formula by parts.

## The third derivative tensor in an orthonormal polar frame

Differentiate the polar Hessian using partial_theta e_r=e_theta and partial_theta e_theta=-e_r. Its four symmetric tensor entries are

 T_rrr=r^-3(psi_ttt-3psi_tt+2psi_t),
 T_rrtheta=r^-3(psi_tt_theta-3psi_t_theta+2psi_theta),
 T_rthetatheta=r^-3(psi_t_theta_theta+psi_tt-2psi_t-2psi_theta_theta),
 T_thetathetatheta=r^-3(psi_theta_theta_theta+3psi_t_theta-2psi_theta).

For example, the r,r,theta covariant derivative is (partial_theta Hess_rr-2Hess_rtheta)/r, and the r,theta,theta entry is partial_r Hess_thetatheta. These yield the displayed connection terms. Substituting r^4 W sin(m theta)/2 into these entries gives r/2 times four modal sums A,B,C,D, with sine factors on A,C and cosine factors on B,D. Their polynomials in the logarithmic derivative are

 P_A(D)=D^3+9D^2+26D+24,
 P_B(D)=m(D^2+5D+6),
 P_C(D)=D^2+(6-m^2)D+8-2m^2,
 P_D(D)=m(3D+10-m^2).

Each acts on W=J-I. Orthogonal changes of frame preserve the Frobenius norm of a tensor. Symmetry gives multiplicities1,3,3,1, so

 ||D^2 V||_F^2=r^2(A^2+3B^2+3C^2+D^2)/4.                         (2)

A second, independently assembled identity is

 ||D^2 V||_F^2=r^2[3(A+C)^2+3(B+D)^2+(A-3C)^2+(3B-D)^2]/16.       (3)

It follows by expanding 3(a+c)^2+(a-3c)^2=4a^2+12c^2 and its b,d counterpart. The first engine bounds the four entries before (2); the second directly forms the four trace and trace-free polynomials before (3). No agreement or overlap criterion replaces either upper bound.

## Independent canonical moment propagation to a subcell center

Fix t_c in [a,b]. With lambda_I=-(m+4) and lambda_J=m-4, exact variation of constants gives

 I(t_c)=exp(lambda_I(t_c-a))I(a)+integral_0^(t_c-a) exp(lambda_I u)H_(n-1)(t_c-u)du,
 J(t_c)=exp(-lambda_J(b-t_c))J(b)+integral_0^(b-t_c) exp(-lambda_J u)H_n(t_c+u)du.

The first method expands each complete polynomial at t_c and integrates its monomials using the absolutely convergent exponential series. For h>=0,

 integral_0^h u^j exp(lambda u)du=h^(j+1) sum_(k=0)^infinity (lambda h)^k/[k!(j+k+1)].

After degree N, the absolute tail is at most

 h^(j+1) |lambda h|^(N+1)/[(N+1)!(j+N+2)] / [1-|lambda h|/(N+2)],

provided |lambda h|<N+2. This follows because successive absolute terms have ratio at most |lambda h|/(N+2) in the tail. The checker verifies the inequality and retains this remainder for every moment.

The second method uses the complete polynomial antiderivative. For lambda nonzero and p(u)=sum c_j u^j, choose q(u)=sum_l [sum_(j>=l) (-1)^(j-l) j! c_j/(l! lambda^(j-l+1))]u^l. Then q'+lambda q=p, so the integral is exp(lambda h)q(h)-q(0). For lambda=0 integrate p term by term exactly. This is finite algebra with no truncation. Arbitrary cancellation is covered by the interval arithmetic.

## Whole-subcell Taylor models with a proved residual bound

Let t=t_c+h u, -1<=u<=1, where h is half the exact subcell width. For y'=lambda y+sH, s=+1 or -1, put ell=lambda h and H(t_c+h u)=sum_(j=0)^7 g_j u^j. Use c_0=y(t_c), and

 c_(k+1)=[ell c_k+s h g_k]/(k+1), with g_k=0 for k>7.

For Q>=7, p(u)=sum_(k=0)^Q c_k u^k has residual p'-ell p-s h H=-ell c_Q u^Q. Variation of constants in either direction from zero gives

 |y(t_c+h u)-p(u)| <= |ell c_Q| exp(|ell|)/(Q+1).                  (4)

If c_0 and g_j are interval enclosures, the recurrence encloses the exact polynomial for every admissible input and (4), using their upper magnitudes, remains valid. Endpoint-moment uncertainty is retained. No derivative of an unspecified remainder is taken.

For any polynomial P(D)=sum_(k=0)^d a_k D^k, repeated use of the first-order equation gives

 P(D)y=P(lambda)y+s sum_(k=1)^d a_k sum_(j=0)^(k-1) lambda^(k-1-j) H^(j).

This identity transforms each tensor polynomial into the moment model plus complete density polynomials. Therefore its remainder is bounded by |P(lambda_J)| times the J remainder plus |P(lambda_I)| times the I remainder. The forcing terms have no truncation. All coefficients, both moments, every finite mode and all remainders are retained.

## Range and final norm bounds

The first engine ranges each complete degree-Q tensor polynomial by converting its exact rational-coordinate interval [-1,1] to Bernstein form; nonnegative Bernstein basis functions sum to one, so the coefficient hull contains the polynomial. It adds the proved remainder (4). The second engine uses interval Horner on [-1,1] and independently adds its own remainder. Trigonometric factors are enclosed over every closed exact angular subinterval. Modal sums are formed before squaring. A finite upper endpoint for each square sum, multiplied by a directed upper enclosure of exp(2t_right), bounds every point of the box. Nonfinite results are rejected. The maximum over all boxes in both methods is rounded to a rational upper bound only after an exact strict square comparison.

The accepted conclusion, if all computations pass, will be a numerical upper bound for M_V on this source disc, conditional on the audited canonical archive and stated bracket. Combining it with topic84's M_rho may certify the coefficient hypothesis in topics77/78, subject to the sign convention correction in topic80 and their other hypotheses. It would not establish global invertibility, matching, the rank-one denominator, nonlinear closure or an endpoint.
