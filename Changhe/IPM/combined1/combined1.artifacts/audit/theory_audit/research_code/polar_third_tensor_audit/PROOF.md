# Audit of the complete polar third-derivative formula

Status: independent T4 audit of the N4 polar Q3 method. The analytic
identities below are checked before the local symbolic computation.
The numerical value of a particular full-plane norm still depends on
its complete source and arithmetic records.

## Statement and notation

Let F be a smooth real scalar on R2 with a finite expansion

    F(r,theta)=sum_(n>0) H_n(r) sin(n theta),

where each H_n is a finite sum r v^d P(t), t=r^2/(1+r^2), v=1-t,
d is rational and P is a rational polynomial. Distinct branches within
one frequency are summed before squaring. Put

    Q3^2=int_R2 (1+4r^2)^(4/5) |D^3 F|^2 dX,

where the full ordered Cartesian tensor has squared norm
F_xxx^2+3F_xxy^2+3F_xyy^2+F_yyy^2. This audit confirms the polar tensor
formula and its whole-plane integration rule under the endpoint
conditions stated below. It does not assert an inverse or existence.

## 1. An independent complex-derivative identity

Write Dplus=partial_x+i partial_y and Dminus=partial_x-i partial_y.
The two derivatives divided by sqrt(2) form a unitary change of basis
on the complexified cotangent space. Applying this change on all three
indices preserves the ordered tensor norm. For real F the two conjugate
pairs give the pointwise identity

    |D^3 F|^2=(|Dplus^3 F|^2+3|Dplus Delta F|^2)/4.       (1)

Define R_m h=h'-m h/r. In polar coordinates

    Dplus[h(r) exp(i m theta)]
      =exp(i(m+1)theta) R_m h.

For one positive sine mode H sin(n theta), angular orthogonality therefore
gives

    int_0^(2pi) |D^3 F|^2 dtheta
      =pi/8 [Aplus^2+Aminus^2+3Bplus^2+3Bminus^2],      (2)

where

    Aplus=R_(n+2) R_(n+1) R_n H,
    Aminus=R_(-n+2) R_(-n+1) R_(-n) H,
    J=H''+H'/r-n^2 H/r^2,
    Bplus=R_n J, Bminus=R_(-n) J.

The two angular frequencies in each complex derivative are distinct
because n>0. Formula (2) provides an audit path that does not use the
polar connection identities in N4's implementation.

## 2. Polar connection components

The radial and angular orthonormal frame gives the Hessian components

    Hrr=H'' sin(n theta),
    Hrtheta=n(H'/r-H/r^2) cos(n theta),
    Hthetatheta=(H'/r-n^2 H/r^2) sin(n theta).

Taking its covariant derivative gives the four symmetric third-tensor
amplitudes

    A=H''',
    B=n(H''/r-2H'/r^2+2H/r^3),
    C=H''/r-(1+n^2)H'/r^2+2n^2 H/r^3,
    D=3n H'/r^2-n(n^2+2)H/r^3.                        (3)

Their angular factors are respectively sin, cos, sin, cos. For example
C is the radial derivative of Hthetatheta, and D contains the two
connection terms 2Hrtheta/r. Thus the angular integral is

    pi (A^2+3B^2+3C^2+D^2).                          (4)

Expansion of the four raising-operator expressions in (2) yields exactly
(4). The local symbolic check treats H,H',H'',H''' and n as arbitrary
symbols, so it checks every radial function, not just selected fixtures.

## 3. Rational compactification

For one radial branch H=r v^d P(t), define

    T_d P=(1-2dt)P+2t(1-t)P'.

Direct differentiation gives H'=v^d T_d P. The Hessian amplitudes are
r v^(d+1) times

    a=-2d T_d P+2v(T_d P)',
    b=n(-2d P+2vP'),
    c=(T_d P-n^2P)/t.

The quotient must be a polynomial; the implementation checks its exact
zero remainder. The third amplitudes are v^(d+1) times

    T_(d+1)a, T_(d+1)b, T_(d+1)c, n c+2b.             (5)

Tensor symmetry gives the additional exact identities

    T_(d+1)b=n a-2b,
    T_(d+1)c=a-c-n b.

These verify the derivative and connection paths agree. No polynomial
coefficient is divided approximately. If a candidate fails these checks,
the calculation must stop.

For each nonzero polynomial E from (5), extract E(1-v)=v^q Q(v) exactly.
For two branches with d=ell delta/2 and d'=ell' delta/2 the weighted
radial product is, apart from pi/2 and tensor/cross multiplicities,

    v^b Q(v) Q'(v) (4-3v)^(4/5) dv,
    b=d+d'+q+q'-4/5.                                (6)

This follows from r dr= -dv/(2v^2). In particular there is no factor
1-v left. Require 2d+2q-4/5>-1 for each nonzero diagonal branch.
Every cross exponent is the average of the corresponding diagonal
exponents, so all cross products are absolutely integrable. This is a
sufficient branchwise test. Failure alone does not prove divergence,
since cancellations could improve a grouped endpoint.

## 4. Weight and signed-coefficient integration

Let W_N be the degree N Taylor polynomial of (1-3v/4)^(4/5). All its
nonconstant coefficients are negative. For k>=1 the absolute coefficient
ratio to the next is (3/4)(k-4/5)/(k+1)<3/4. Thus, if epsilon is four
times the magnitude of the first omitted coefficient,

    W_N-epsilon <= (1-3v/4)^(4/5) <= W_N, 0<=v<=1.

The original mode integrand before this factor is a sum of squared
real tensor amplitudes, with multiplicities 1,3,3,1, hence nonnegative.
Let S be its integral and T its integral after multiplication by W_N.
Then the mode energy belongs to

    [(pi/2)4^(4/5)(T-epsilon S), (pi/2)4^(4/5)T].     (7)

All polynomial terms integrate by
int_0^1 v^(b+j)dv=1/(b+j+1), with positive rational denominator.
Mixed signs of expanded coefficients do not invalidate (7): the weight
comparison is applied before expansion. Arithmetic must keep outward
balls throughout polynomial multiplication, summation and division.

## 5. Audit scope and retained evidence

N4's code preserves all branches within each frequency, counts cross
pairs twice, uses 1,3,3,1 tensor multiplicities, checks every endpoint,
and verifies both exact tensor identities. Its degree112 weight bound
matches Section4. The complete-mode manifest and per-mode hashes prevent
an unfinished positive partial sum from being called a full upper bound.

The local checker proves (2)=(4) symbolically, independently reconstructs
the binomial bound, verifies all 160 completed candidate007 mode hashes,
rechecks their rational endpoint exponents, and adds their outward energy
balls. It compares the resulting interval with the frozen independent
N3 Cartesian result on the same canonical data. This is a theorem/code
and retained-record audit, not a third full regeneration of all 1360
residual polynomials. The two full arithmetic paths are N3 Cartesian and
N4 polar. The record says so explicitly.

Dependencies: elementary flat tensor differentiation, finite Fourier
orthogonality, finite power integrals, outward ball arithmetic, and the
already verified exact residual assembly of the same candidate. No
external operator theorem or computer proof assistant is used.
