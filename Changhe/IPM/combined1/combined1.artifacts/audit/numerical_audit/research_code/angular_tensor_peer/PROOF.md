# Exact quadrant integration of residual tensor squares

## Statement, hypotheses and scope

Let M be a nonnegative integer, c a real number, and let
chi(r,theta)=sum_{m=0}^M a_m(r) cos(2m theta) on an open annulus r>0,
where every a_m is C^6. Set psi=partial_x partial_y chi,
rho=-partial_y Delta chi, u=(-partial_y psi,partial_x psi), and
F=(cX+u).grad rho-rho. The derivatives in this statement are classical.
For an integer N>=1, let theta_i=(i+1/2)pi/(2N), 0<=i<N, and
Q_N[g]=(pi/(2N))sum_i g(theta_i). At each fixed radius the following
identities hold, with all function values and nodes evaluated exactly:

  Q_N[g]=int_0^(pi/2) g(theta) dtheta,

for g=F^2, |grad F|^2, |D^2 F|_F^2, and (Delta F)^2 whenever
N>=2M+2. Here |D^2 F|_F^2=F_xx^2+2F_xy^2+F_yy^2 is the ordered
Cartesian tensor square. Multiplication by any finite radial factor
at that radius preserves the identity. For each separate Cartesian
derivative of F of order at most two, its square is integrated exactly
under the sufficient condition N>=2M+3. These are sufficient bounds;
no optimality or realized highest coefficient is claimed.

For the shapes with M=79 in N4-295, the respective sufficient bounds
are N>=160 and N>=161. The adopted N=180 meets both. Application to
an actual candidate still requires its complete shape binding; a
proposed family alone does not bind fitted coefficients. This theorem
controls angular quadrature with ideal arithmetic. It supplies no
binary64 evaluation error, radial quadrature error, origin or far-tail
bound, residual smallness, conditioning, inverse, or existence.

## Frequency bound for F

The polar differential formulas are
partial_x=cos(theta)partial_r-r^-1 sin(theta)partial_theta and
partial_y=sin(theta)partial_r+r^-1 cos(theta)partial_theta.
The Laplacian preserves each angular frequency. Consequently rho is
a finite sum of odd sine modes with largest possible frequency 2M+1.
The field psi is a sum of even sine modes with frequency at most2M+2.
Products to sums and the polar Jacobian identity give

  u.grad rho = r^-1(psi_r rho_theta-psi_theta rho_r).

The right side is an odd sine polynomial with frequency at most
(2M+2)+(2M+1)=4M+3. Also X.grad rho=r rho_r has frequency at most
2M+1. Hence F is a sum of sin(n theta) with positive odd n<=d=4M+3.
Radial derivatives and angular derivatives preserve this upper bound;
an angular derivative changes sine to cosine. No assumption about the
radial shape or the nonzero highest coefficient is used.

## Quadrant midpoint identity

For any integer q with 0<q<2N, put x=q pi/N. Telescoping
2sin(x/2)cos((i+1/2)x)=sin((i+1)x)-sin(i x) gives

  2sin(x/2)sum_{i=0}^{N-1} cos((i+1/2)x)=sin(Nx)=0.

The multiplier is nonzero because 0<x/2<pi. Thus Q_N annihilates
cos(2q theta), whose exact quadrant integral is also zero. It treats
the constant exactly. The square of any odd sine polynomial or odd
cosine polynomial of frequency at most d is a linear combination of
1 and cos(2q theta) with 1<=q<=d. This follows term by term from the
sum and difference product identities. If d<2N, Q_N therefore
integrates that square exactly. With d=4M+3, the integer condition
N>=2M+2 ensures d<2N.

## Gradient and Hessian tensor identities

Write e_r=(cos theta,sin theta), e_theta=(-sin theta,cos theta).
The gradient has orthonormal components F_r and r^-1 F_theta, so

  |grad F|^2=F_r^2+r^-2 F_theta^2.

Differentiating these components and the unit vectors gives the
symmetric Hessian in this frame:

  A=F_rr,
  B=r^-1 F_rtheta-r^-2 F_theta,
  C=r^-1 F_r+r^-2 F_thetatheta.

For completeness, partial_r e_r=partial_r e_theta=0,
partial_theta e_r=e_theta, partial_theta e_theta=-e_r. The radial
column of the derivative of grad F is (F_rr,
r^-1 F_rtheta-r^-2 F_theta). The angular column, with the directional
factor r^-1, is (r^-1 F_rtheta-r^-2 F_theta,
r^-1 F_r+r^-2 F_thetatheta). This proves the displayed Hessian.

Orthogonal change of frame preserves the Frobenius norm and trace.
Therefore

  |D^2 F|_F^2=A^2+2B^2+C^2,
  Delta F=A+C.

At fixed r, A and C have only odd sine modes and B has only odd cosine
modes, all at frequency at most d. The same applies to the two gradient
components. The preceding midpoint identity integrates each square
exactly, including (A+C)^2. The full tensor equality is essential:
individual Cartesian components gain angular frequencies when the
frame rotates, and their cross-component cancellation need not survive
arbitrary separate weights. This proves the full tensor assertions.

## Separate Cartesian components

Each application of partial_x or partial_y shifts angular frequencies
by at most one. By separate coordinate parities of F, each fixed
Cartesian derivative has a single sine or cosine type and frequencies
of one parity. The frequencies are odd for even j and even for odd j;
the zero cosine mode is allowed. A derivative of order j<=2 therefore
has frequency at most d+j<=d+2. Its square has the cosine indices covered by the
midpoint identity if d+2<2N. The integer condition N>=2M+3 implies this.
This also explains why the more conservative N4-295 rule remains
valid after the full tensor improvement.

## Independent review and finite verification

T4-374 section5 is the peer theorem reviewed here. Its full proof was
read before this proof was written. We independently derive the frame
derivatives, tensor identities and midpoint telescoping formula above.
The finite checker verifies both tensor identities by polynomial
arithmetic modulo cos^2(theta)+sin^2(theta)=1. An independent roots of
unity calculation checks exact midpoint cosine sums as real parts in
Q[z]/Phi_(8N)(z) for representative N, including the first alias. It
checks all pairwise cosine indices for M=79 and compares the sufficient
bounds with N4-295 and T4-374. Every retained peer source is hash-bound.
The peer code is inspected, not executed. The general theorem rests
on the complete argument above, not only on finite test values.

The audit accepts section5 only. The other conclusions in T4-374 have
their own dependencies and are not independently re-certified by this
check. No formal source or Lean build is claimed. Exact parameters and
verification evidence belong in data or verification, alongside this
proof. No JavaScript, server, cluster, remote computation or GPU is used.
