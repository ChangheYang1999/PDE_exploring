# Original-data point enclosures for the strong residual norm

## Statement and scope

Let rho be the exactly normalized, C6-joined modal trial defined in topics04 and15 from the original file with SHA-256

 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.

It is the analysis1 modal trial attached to the current case1 state, not the raw X3 array. Let ell=1/k, V=ell X+U[rho], F=V.grad rho-rho, p=x^2 y and t=log r. Use the exact target Y=E G direct-sum R and its Hilbert norm from proof 98. There are uniquely defined functions gamma(t) and Q(t,theta) such that

 F(X)=p(X)[gamma(t)+cos(theta)^2 Q(t,theta)].

Q is a finite cosine polynomial. Put

 e_J(t)=omega(t) gamma(t)^2,
 e_R(t)=omega(t) integral_0^(2pi) |cos(theta)|^(-1/2) sin(theta)^2 Q(t,theta)^2 dtheta,

where omega(t)=exp(-t/2) for t<0 and exp(27t/4) for t>=0. Then ||F||_Y^2=int_R(e_J+e_R)dt. The following pointwise enclosures hold. A notation [a,b]10^q means the interval [a 10^q,b 10^q].

| t | e_J(t) | e_R(t) |
|---|---|---|
| -40 | [5.8561103632,5.8561103633]10^-72 | [2.0285703509,2.0285703510]10^-70 |
| -10 | [2.3286357062,2.3286357063]10^-26 | [8.0836830870,8.0836830871]10^-25 |
| 0 | [1.0638622903,1.0638622904]10^-15 | [1.4354108071,1.4354108072]10^-8 |
| 4 | [0.00010352357242,0.00010352357243] | [171275.298892,171275.298893] |
| 10 | [8.1268733611,8.1268733612] | [11779542.042748,11779542.042750] |
| 30 | [0.0034358320362,0.0034358320363] | [527.2295047104,527.2295047105] |

These are six pointwise energy densities. They are not an integral enclosure, a bound for eta, an existence obstruction, or a proof that an entire inner half-line contributes any particular amount. In particular, no positive integral lower bound follows from a single point without additional continuity control. The numerical magnitude of the far energy density is real for this norm, despite a separate floating-point instability in the numerics team's initial inner-tail computation.

## Exact residual construction

The source has 260 cofactor modes m=0,...,259. Multiplication by cos(theta)^2 sin(theta) gives density sine modes j=0,...,260. For uniform indexing the implementation carries j=261 with an exactly zero coefficient. Write

 rho/r^3=sum_j h_j(t) sin((2j+1)theta),
 V_r/r=ell-sum_(n=1)^261 P_n(t) cos(2n theta),
 V_theta/r=sum_(n=1)^261 Q_n(t) sin(2n theta).

Thus the exact residual sine polynomial is

 F/r^3=(ell-sum P_n cos(2n theta)) sum_j(3h_j+h_j')sin((2j+1)theta)
       +(sum Q_n sin(2n theta))sum_j(2j+1)h_j cos((2j+1)theta)
       -sum_j h_j sin((2j+1)theta).                         (1)

The largest possible odd frequency is1043, with sine index521. The implementation safely carries index522, which is structurally zero. Formula(1) is evaluated by Laurent polynomial multiplication in directed Arb arithmetic. A sine polynomial is represented by coefficients s_k at z^k and -s_k at z^-k, so that it is 2i times the physical sine polynomial. Cosine polynomials use half their coefficient at each nonzero signed frequency. Every product in(1) has exactly one sine factor; this representation gives the correct physical sine coefficients with no missing factor2 or sign.

The Green coefficients P_n and Q_n are reconstructed by the independently checked formulas of topics15 and68. On spline cells, their polynomial-exponential representation is evaluated by the local analytic series at a point. On each half-line, the exact endpoint exponential polynomials are evaluated directly. The special resonant primitive in the inner J_n is a polynomial antiderivative; it is not divided by a zero exponent. At n=1 the constant homogeneous strain coefficient is set to the exact normalization value 3/k-1. This substitution is justified by the normalization identity proved in proof 04; the independently propagated enclosure is also checked to overlap that value. It is not justified merely by this overlap.

The Green boundary cache records exact-input hashes, original knot values and directed endpoint balls. These are all checked on loading. Consequently every coefficient used in(1) encloses its value for the same exact original trial. No teammate matrix, FFT, numerical pseudoinverse or truncated background is used.

## Exact axis factors and norm evaluation

Since rho=p a with a even in both coordinates, V has first component odd in x and even in y, and second component even in x and odd in y. Hence V.grad rho-rho is divisible by p at every positive radius. This proves the necessary factor structurally before any division. If s_j are the sine coefficients of(1), define

 A_0=sum_j s_j,
 A_m=2 sum_(j>=m) s_j for m>=1.

The identity sin((2j+1)theta)/sin(theta)=1+2 sum_(m=1)^j cos(2m theta) gives F/(r^3 sin(theta))=sum A_m cos(2m theta). Its value at the vertical axis is exactly zero by the proved x^2 factor. Applying proof 98's exact cosine quotient to A therefore gives the cofactor B=F/p. Applying it again to B-B(axis) gives Q. The directed axis ball is checked to contain zero, but the exact structural argument, rather than that check, is what permits the first division.

Proof 98 then gives

 e_J=omega B(axis)^2,
 e_R=omega 2 Beta(1/4,3/2) H(q),
 H(q)=sum_(j,l)q_j q_l(m_(j+l)+m_|j-l|)/2.

The moments m_n are the exact rational beta-weight moments of proof 98. The finite quadratic form is evaluated by an Arb polynomial square. There is no angular sampling error or omitted Fourier tail.

## Independent internal checks

Let alpha(t)=a(t,pi/2), d(t)=V_2(0,e^t)/e^t and D=4ell-1. The sine representation gives

 alpha=-1/2 sum_j(-1)^j(2j+1)^2 h_j,
 d=ell-sum_n(-1)^n P_n.

The independently derived axis identity of proof 41 gives

 gamma=d alpha'+(D-d-2d')alpha.                            (2)

The implementation checks the difference between(2) and the polynomial-quotient gamma in directed arithmetic at all six points. It also evaluates(1) directly at theta=pi/7 and checks equality with cos(theta)^2 sin(theta) B(t,theta). All differences contain zero at384-bit precision, with radii far below the displayed enclosures. These checks complement the algebra above; they do not replace it.

The final JSON stores exact dyadic lower and upper endpoints, the original-data hash, the code hash, precision and actual run time. The table is rounded outward from those endpoints. The separate audit verifies each displayed enclosure using rational comparisons and verifies the exact zero top input mode.

## Relation to the initial floating estimate

The initial eta2 script evaluates(1) in binary64, extracts800 residual sine modes by FFT, and divides a noisy mode vector by cos(theta)^4 with a numerical pseudoinverse. Modes522 through800 are identically zero for this trial. Axis extraction multiplies mode errors by (2j+1)^2; division by a function with a fourth-order zero at the axis is still more sensitive. A small unweighted residual of that division does not bound the strong weighted quotient norm.

The confirmed point values here show both the tiny exact inner residual and the large exact far weighted density. They do not certify or refute a future stabilized radial integral. Such an integral must enclose the radial quadrature, the endpoint tails and any angular coefficient errors in the actual target norm.

## Dependencies and evidence

Dependencies: topics04 and15 for the exact trial and normalization; proof 68 for the independent Green reconstruction; proof 98 for exact angular quotients and norm. Evidence: code/check_points.py, evidence/points_384.json, and the rational audit. All source reads are from the read-only original or the team's verified cache. No result in this note concerns the raw X3 realization or a continuum inverse.
