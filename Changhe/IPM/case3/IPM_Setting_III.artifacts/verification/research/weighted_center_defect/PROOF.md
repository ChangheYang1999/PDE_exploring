# Weighted residual identities with a nonzero center defect

Date: 2026-10-20. Status: complete independent argument; required implementation checks
passed 2026-10-20T20:05:13.445596+00:00. This supplies a stable diagnostic for non-profile
interpolants and verifies the first-derivative weighted inequality WID1(f).

## Definitions and hypotheses

Let rho be smooth, even in x and odd in y, with a=rho_y(0)!=0, and let U be its
canonical smooth full-plane IPM velocity. Assume that rho and U and their
needed derivatives obey sublinear symbol bounds with some exponent p<1.
These bounds hold for the finite smooth Q interpolants being evaluated;
exact primary profiles have them by the earlier regularity results.
Fix any ell>1, without imposing the transport or center equations. Set

    c=psi_xy(0), delta=ell+c-1,
    h=rho-a y, phi=psi-cxy, v=U-(-cx,cy), W=ell X+U,
    R=W.grad rho-rho, F=R-a delta y,
    ||g||_m^2=integral_R2 |g|^2 r^(-2m)dX,
    sigma=sup|sym DU|_op, M=sup_{X!=0}(-X.U/r^2).

All inverses in these definitions use the actual field's c. The subtraction
in phi and v is a change of unknown, not an added harmonic velocity in the
original problem. In general M>=|c| and sigma>=|c|. Only when delta=0 may
one replace |c| with D=ell-1 in these origin lower bounds.

## Scalar identity and the center obstruction

A direct expansion, retaining the center mismatch, gives

    W.grad h-h=-a v2+F.                                  (1)

Indeed W.grad(ay)-ay=a[(ell-1)y+U2]=a delta y+a v2.
Parity and smoothness give h=O(r^3), phi=O(r^4), v=O(r^3),
R=a delta y+O(r^3), and F=O(r^3) at zero. At infinity h,v,F=O(r)
and phi=O(r^2), with corresponding symbol derivative bounds. Thus for
2<m<4 all terms of the following identity are absolutely integrable:

    ((m-1)ell-1)||h||_m^2
      +m integral (X.U/r^2)h^2 r^(-2m)dX
      +a integral v2 h r^(-2m)dX
       = integral F h r^(-2m)dX.                         (2)

To prove it, multiply (1) by h r^(-2m), integrate on circular annuli,
and use divW=2ell. The boundary flux is O(r^(8-2m)) at zero and
O(r^(4-2m)) at infinity, so both vanish. The divergence of the weight
is exactly the one in result57. This proves (2) also when delta!=0.

Let Qsign(m) denote Qminus(m) if a>0 and Qplus(m) if a<0, as in result59.
The same weighted inverse applies to phi,h because -Delta phi=h_x,
independently of the transport equation. Consequently

    ||F||_m/||h||_m
      >= (m-1)ell-1-mM-|a|Qsign(m)
      >= (m-1)ell-1-m sigma-|a|Qsign(m).                  (3)

The second lower bound uses M<=sigma, obtained by integrating DU along
segments. The first denominator is nonzero: h=0 would give rho=ay,
contradicting the sublinear growth and a!=0. A negative right side is merely
an uninformative bound, not an inconsistency.

If delta!=0, the unmodified residual R has infinite weighted norm for
every m>=2. To see this, on any angular sector with |sin(theta)|>=1/2,
R=a delta r sin(theta)+O(r^3). Uniformity of the Taylor remainder makes
|R|>=|a delta|r/4 there for all sufficiently small r. The lower bound on
its squared weighted radial integral is a positive constant times
integral_0^epsilon r^(3-2m)dr, which diverges. Thus subtracting a delta y
is essential to make this particular diagnostic finite. It does not
excuse delta: the center defect must be reported as a separate error.
A tiny nonzero center defect cannot be called a small value of ||R||_m.

## First derivative identity

Put g=grad h. Differentiating (1) gives the exact vector equation

    W.grad g+(ell-1)g+(DU)^T g=-a grad v2+grad F.

For 1<mu<3, g,grad v2,grad F=O(r^2) at zero and O(1) at infinity.
Their weighted norms are finite, with boundary flux O(r^(6-2mu)) at
zero and O(r^(2-2mu)) at infinity. Pairing with g r^(-2mu) gives

    (mu ell-1)||g||_mu^2
     +mu integral (X.U/r^2)|g|^2 r^(-2mu)dX
     +integral g^T S g r^(-2mu)dX
       =-a integral grad v2.g r^(-2mu)dX
          +integral grad F.g r^(-2mu)dX, S=sym DU.       (4)

The coefficient mu ell-1 includes both the integration-by-parts drift
and the differentiated linear term. Skew DU contributes zero to the
quadratic form. No maximum principle for a weighted Riesz transform
has been used.

For each j=x,y the potential phi_j satisfies

    -Delta phi_j=partial_x h_j.

It is O(r^3) at zero, O(r) at infinity, and odd under X->-X. Set on the
log-radius cylinder G_j=r^(-mu)phi_j and H_j=r^(1-mu)h_j. The polar
Poisson equation is

    -[(partial_s+mu)^2+partial_theta^2]G_j
      =(partial_s+mu)(cos(theta)H_j)
                      +partial_theta(-sin(theta)H_j).

Both G_j and the vector on the right have only odd angular frequencies.
At frequency (xi,n), the norm of the corresponding rank-one derivative
map is at most

    (xi^2+mu^2+n^2)/sqrt((xi^2+(n-mu)^2)(xi^2+(n+mu)^2)).

This expression is largest at xi=0. Among odd integers it is largest at
|n|=1 or3 when1<mu<3, giving

    Nodd_mu=max((mu^2+1)/(mu^2-1),(mu^2+9)/(9-mu^2)).

There is no multiplier zero in the stated range, so L2 uniqueness on the
cylinder identifies the actual derivative potentials. Summing the two
squared estimates proves

    ||Dv||_mu <= Nodd_mu ||grad h||_mu.                  (5)

Here ||Dv|| uses the full Frobenius tensor. In particular it bounds the
smaller norm ||grad v2||. Using S>=-sigma I, X.U/r^2>=-sigma, (5) and
Cauchy-Schwarz in (4) yields

    mu ell-1 <= (mu+1)sigma+Nodd_mu |a|
                        +||grad F||_mu/||grad h||_mu.   (6)

The denominator is again nonzero, since a constant h is forced to zero
by parity and would contradict sublinear rho. An exact profile has
delta=0 and F=0, proving WID1(f) for every1<mu<3; atmu2 the coefficient
is13/5. For a non-profile grad R alone has infinite weighted norm when
delta!=0 and mu>=1, by the same center argument applied to its constant
leading vector a delta e_y. Equation (6) uses the corrected F throughout.

## Scaling, numerical scope and dependencies

For rho_lambda=lambda rho(X/lambda), the quantities ell,a,c,delta,sigma,M
are unchanged. The weighted norms in (2) scale by lambda^(2-m), and
the derivative norms in (4) scale by lambda^(1-mu). All ratios and
inequalities above therefore respect the unresolved spatial dilation.

The only inverse input is the explicit weighted multiplier already
proved for even stream modes in57/59; its odd-mode derivative version
is derived above. The rest is exact differentiation, Taylor expansion
and justified annular integration. Implementation checks use a Gaussian
canonical stream with an arbitrary nonzero center defect, exact angular
integration and separate radial quadrature. Candidate norms, if later
reported, need both radial convergence and full-plane tail control.
Sampled values of M or sigma are lower estimates and cannot supply the
upper bound needed to make the right side of (3) a valid numerical
exclusion. The original center and transport equations remain separate
requirements. No existence or full-class nonexistence claim follows.
