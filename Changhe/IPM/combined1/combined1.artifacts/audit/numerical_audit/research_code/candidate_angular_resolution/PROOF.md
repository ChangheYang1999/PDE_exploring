# Angular resolution for the current quotient and scaled families

## Exact statement and scope

At a fixed radius r>0, let

 chi(r,theta)=sum_(m=0)^M a_m(r) cos(2m theta)

be a smooth potential with arbitrary smooth radial coefficients. Define
rho=-partial_y Delta chi, psi=partial_xy chi, u=(-psi_y,psi_x) and
F=(cX+u).grad rho-rho for any fixed real c. At the ideal quadrant
midpoints theta_i=(i+1/2)pi/(2N), i=0,...,N-1, with weight pi/(2N),
the following angular integrals are exact if 4M+5<2N:

1. The squared Cartesian components D^alpha F, |alpha|<=2, each
   multiplied by any angularly constant weight.
2. The squared Cartesian components D^alpha rho, |alpha|=2.
3. F(r,theta) sin(n theta) for positive odd n with 4M+3+n<4N.

The same is true for sums of the indicated terms. Integration is over
[0,pi/2]; parity gives the corresponding whole-circle integral by a
factor four. This is an exact trigonometric quadrature statement. It
assumes exact ideal nodes, weights and field values, and gives no error
bound for their floating implementations, radial quadrature, omitted
radial regions, coefficient rounding, or any reported continuum norm.

The actual candidate020 shape list and proposed022 shape list both have
M=79. The largest allowed frequencies of F, grad F and D^2 F are thus
319,320,321. N=180 gives 321<360. Every probe with odd n<=47 satisfies
319+n<=366<720. Radius25, radius50 and the proposed higher-angular
radius25 additions do not increase M beyond the old quotient maximum79.
Actual future candidate identity is not implied by its proposed list.

## Bandwidth and parity proof

The radial Laplacian preserves each angular frequency. Cartesian
partial_y shifts it by one, so rho has only odd sine frequencies at
most2M+1. The stream psi is obtained by two Cartesian derivatives and
has only even sine frequencies at most2M+2. In polar coordinates,

 u.grad rho=(psi_r rho_theta-psi_theta rho_r)/r.

Radial and angular differentiation do not increase angular frequency;
a product has maximum frequency at most the sum of its factors. Hence
the nonlinear term has frequency at most4M+3. Radial drift preserves
the density frequencies. F has the density's separate coordinate
parities and therefore only odd sine modes. Cartesian differentiation
has the formulas

 partial_x=cos(theta) partial_r-sin(theta)/r partial_theta,
 partial_y=sin(theta) partial_r+cos(theta)/r partial_theta.

Each raises the maximum frequency by at most one. For a fixed derivative
component the sine/cosine type and the parity of the frequency are fixed
by the coordinate parities. Its square is therefore a cosine polynomial
in frequencies2q, with q no larger than that component's maximum
frequency. Consequently the largest q required by item1 is4M+5.
For item2 it is at most2M+3. For item3 the sine product formula gives
cosine frequencies at most4M+3+n, which are even since both summands
are odd. These statements are bounds on permitted support, and do not
claim every highest frequency occurs for a fitted coefficient vector.

## Exact midpoint sum

For integer q with0<q<2N, the finite trigonometric sum is

 sum_(i=0)^(N-1) cos(q*pi*(i+1/2)/N)
    =sin(q*pi)/(2*sin(q*pi/(2N)))=0.

The denominator is nonzero in the specified range. This identity follows
by taking the real part of the finite geometric series, or by telescoping
2 sin(x/2) cos((i+1/2)x)=sin((i+1)x)-sin(i x), x=q*pi/N.
The exact integral of cos(2q theta) on the quadrant is also zero. The
constant integrates to pi/2 under both rules. Linearity and the bandwidth
bounds prove every assertion above. Positive radial weights can vary
arbitrarily with r without changing this argument at that radius.

## Candidate and source application

The exact checker reads every shape in the immutable020 snapshot and the
hash-bound proposed022 abstract list, and computes both maximum m values.
It binds the accepted020 actual-shape/objective record and its raw input;
its shape equality is an accepted dependency. It binds the new proposed
list without assuming the still open2414-dimensional rank theorem, since
this bandwidth argument only needs the shapes.

Read the frozen optimizer, evaluator and objective sources as text. The
evaluator defines the stated quadrant midpoint formula. The frozen
Problem2 objective has radial weights on the six F derivative squares
through order two, and optional Hessian-rho squares. Its wlog term is
F^2 ds dtheta with no angular factor. Problem3 adds squared finite weak
pairings. Each individual angular pairing has the item3 exactness;
squaring the assembled pairing introduces no additional angular rule.
Candidate020 metadata and completed launcher specify180 nodes. The
proposed022 launch also specifies180, but a future completed run needs
its own metadata binding. No publisher program is executed.

The checker additionally enumerates the products of every allowed sine
or cosine frequency for each derivative parity and verifies that all
nonconstant cosine indices remain below2N. This finite arithmetic checks
the bandwidth application, not floating sine implementations. The
midpoint theorem is the previously independently reviewed theorem in
../angular_resolution/PROOF.md, with the derivative and shape application
proved here in full. There is no condition-number, optimizer-floor,
stationarity, inverse, or existence conclusion.
