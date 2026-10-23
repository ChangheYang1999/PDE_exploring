# Independent audit of five resolved-map hydrostatic trial states

Written before running this audit. This is result 227. The computational domain is the
whole plane for the auxiliary positive-sign hydrostatic problem, not the full IPM
problem of PROMPT.md. All numerical conclusions below will concern the five frozen
trial densities, not exact profiles, uniform bounds or limiting solutions.

## Statement, hypotheses and notation

For a fixed smooth density g, even in x and odd in y, with sublinear power-law tails,
define on x,y >= 0

    V1(x,y) = - integral_y^infinity g_x(x,t) dt,
    V2(x,y) = integral_0^y t g_xx(x,t) dt
              + y integral_y^infinity g_xx(x,t) dt,
    Phi(x,y) = integral_0^y t g_x(x,t) dt
               + y integral_y^infinity g_x(x,t) dt.

Continue by the vector and stream-function parities. Then V=(-Phi_y,Phi_x),
-Phi_yy=g_x and div V=0. No homogeneous vertical stream or velocity is added.
The tested transport equation is (cX+V).grad g=g, with c=3 for these inputs.
It is not the isotropic Poisson equation -Delta psi=rho_x required by Setting III.

The five numeric checkpoints are hsG_c3.0_N64_log, hsG_c3.0_N96_log,
hsG_c3.0_N128_log, hsG_c3.0_N64_fine_log, hsG_c3.0_N96_fine_log.
They are producer outputs with revised quadrature maps. The producer's evaluation
and differentiation code will not be run or imported. The independently written
reader reconstructs exactly the saved binary64 coefficients and stored radial nodes.
No value of a0, c, a Taylor coefficient or center integral is repaired in the data.

Write P>1 for the stored radial-map exponent and p=1-1/P. The compactified map is
r=L sqrt((1+t)/2)/(1-t)^P, or r=C sqrt(1-w) w^(-P), w=(1-t)/2, C=L/2^P.
The density is represented by

    g = r sin(theta) w sum_k ((1+t)/2)^k q_k(t) cos(2k theta).

Here q_k is the Chebyshev polynomial obtained from the numeric checkpoint's local
basis by exact rational affine conversion. This formula is smooth at every finite
Cartesian point: the map variable s=(1+t)/2 is an analytic function of r^2 near
zero, s/r^2 has a positive finite limit, and r sin(theta)=y. Each angular term
s^k cos(2k theta) is therefore a smooth radial factor times a Cartesian polynomial.
At finite nonzero r the inverse map is smooth and its derivative does not vanish.
The formula gives g=O(r^p), grad g=O(r^(p-1)), with p in (0,1), and all higher
Cartesian derivatives have the corresponding differentiated bounds at infinity.
The leading angular function can vanish; these are upper bounds, not an assertion
of a nonzero leading term in every direction.

## Full-plane inverse and numerical quadrature

The displayed integrals converge, since g_x=O(t^(p-1)) is not by itself integrable,
but for each fixed x the even-x symmetry and smooth angular expansion improve it
to O(x t^(p-2)); g_xx=O(t^(p-2)) is integrable because p<1. Weighted integration
is only over the finite interval [0,y]. Differentiating the integrals gives exactly
Phi_y=int_y^infinity g_x, Phi_yy=-g_x and Phi_x=V2. Differentiation in x is allowed
by the differentiated tail bounds. The parities determine zero values on the axes;
there is no wall condition. This is the hydrostatic canonical inverse used here.
The polynomial density has uniform angular derivative bounds, which give
|V|=O(r^p) for large r by splitting the integrals at t comparable to r, and hence
fix the homogeneous freedom: a stream difference has the form y A(x)+B(x),
parity forces B=0 and A odd, and sublinear velocity as y tends to infinity at
fixed x forces A'(x)=0. Thus A=0. No arbitrary x-dependent homogeneous field remains.

Finite intervals are split geometrically with inner scale 1/8 and integrated by
Gauss-Legendre quadrature. On [R,infinity) use t=R/u^P, 0<u<1, including the
Jacobian P R u^(-P-1). This evaluates the entire prescribed tail, with no finite-box
boundary closure. The exact substitution preserves both integrals and turns their
leading t^(p-2) behavior into a constant at u=0. Higher terms are resolved by
ordinary Gauss-Legendre rules. Three full-grid settings are (finite order, tail
order, split multiplier)=(32,96,16),(48,160,64),(64,192,128). A fourth setting
(88,256,512) tests the union of the sampled maximizers and fixed probes. Quadrature
agreement is empirical; no rigorous quadrature error bound is claimed.

## Center coefficients and exact integral

Let q_k(t)=sum_j a_kj T_j(t), where each a_kj is an exact rational reconstructed
from the input. Put

    a=sum_j (-1)^j a_0j,
    d=sum_j (-1)^(j+1) j^2 a_0j,
    b1=sum_j (-1)^j a_1j.

Expanding s=2^(2P) r^2/L^2+O(r^4) at zero yields

    g(x,y)=a y+b x^2 y+e y^3+O(r^5),
    b=(2d-a+b1) 2^(2P)/L^2,
    e=(2d-a-b1) 2^(2P)/L^2.

The factor is real, so only a,d,b1 and the center integral are rational in general.
Set H(t)=w sum_k (-1)^k s^k q_k(t), so g(0,y)=y H(t(y)). The exact primitive from
result 198 is obtained from

    D(t)=sum_(k>=1) (-1)^k k^2 s^(k-1)
          [(1+2P)+(2P-1)t]/2 q_k(t),
    J(t)=integral_-1^t D(tau) dtau,
    Kpoly(t)=-H(t)+J(t)-J(1).

Differentiating these finite polynomials and the radial map gives
Kpoly(t(y))=int_y^infinity g_xx(0,tau) dtau. Therefore
cH=Kpoly(-1)=-a-J(1), and delta=c+cH-1 is exact rational in the binary data.
No numerical origin row is reused. Cross-check cH by complete vertical quadrature
and by the separately written exact-center formula. The rescaled source relation
is satisfied only if delta=0. For an imperfect trial the coefficient of y^3 in the
axis residual is e(2+3delta)-a b/3; this follows from
V2(0,y)=cH y-(b/3)y^3+O(y^5). Do not replace it by the exact-profile cubic identity.

## Far-field coefficients and core moment

Expand H(1-2w)=h1 w+h2 w^2+..., Kpoly(1-2w)=k1 w+k2 w^2+.... The constant terms
vanish exactly. Inverting y=C sqrt(1-w) w^(-P) gives

    G(y)=K y^p+c2 y^(2p-1)+..., K=h1 C^(1/P),
    c2=C^(2/P)[h2-h1/(2P)], Q=k1 C^(1/P)/P,
    Kpoly(t(y))=Q y^(p-1)/(1-p)+O(y^(2p-2)).

When 1<P<2, hence 0<p<1/2, the finite core moment exists and equals

    m0=lim_(R->infinity)[int_0^R Kpoly(t(y))dy
                         -Q R^p/(p(1-p))]
      =C sum_(j>=1) j kj B(j-P,3/2).

The beta value at j=1 is understood by its finite part. Integration by parts after
subtracting k1 w at w=0 gives the convergent integral

    m0/C = integral_0^1 w^(-P)
                [sqrt(1-w) Kpoly_w(w)-k1]dw - k1/(P-1).

This equality follows by integrating the compactified Jacobian and keeping the
boundary subtraction. Near zero the bracket is O(w), so P<2 proves convergence;
near one the terms are bounded. The beta recurrence or this integral evaluates
m0 without fitting the far field. Exact endpoint derivatives provide independent
checks k1=-2 Kpoly_t(1), k2=2 Kpoly_tt(1), and analogously for H. Working precision
is increased according to the exact coefficients' cancellation size and checked
again at 40 additional decimal digits.

The coefficient of y^(2p-1) in the transport residual is

    r2=[c(2p-1)-1] c2+K Q/(1-p).

There is also a leading term K(cp-1)y^p. The input P is a binary float, so cp-1
may be tiny but not exactly zero; its literal infinite-radius effect must not be
suppressed. The expression y R_h/Nf -> m0/(2c) applies only when K>0, cp=1,
r2=0 and smaller remainders have been justified. In particular m0/6 is a
conditional c=3 diagnostic, not a limit inferred for these trials.

## Residual protocol and interpretation

Use a fixed independent grid of 774 physical points with radii from 1e-5 to 1e4,
exact points on both axes, angles displaced from collocation nodes, and probes in
all quadrants. Report regions r<.01, .01<=r<.1, .1<=r<1, 1<=r<100 and r>=100,
plus three nested physical extents 10,100,10000. At every point record

    R=(c x+V1)g_x+(c y+V2)g_y-g,
    Nf=|(c x+V1)g_x|+|(c y+V2)g_y|+|g|,
    Nv=|g|+|x g_x+y g_y|+|V1 g_x+V2 g_y|.

Undefined 0/0 ratios remain null and are counted. Absolute and normalized maxima
retain their own locations and denominators. Their maximizers need not coincide.
Compare quadrature levels point by point, not just their maxima. Check selected
Cartesian jets by high-precision scalar differentiation of the reconstructed
angular density, a distinct route from the Cartesian analytic-jet evaluator.
Exact center conditions, full inverse residuals, changes of coefficients across
states, and differences in maps are separate diagnostics. Failed solves do not
prove nonexistence. Five finite trial outputs cannot prove a convergence limit or
that quadrature error is irrelevant to every solver. None is a primary Setting III
candidate, since the auxiliary inverse is different.

## Dependencies and verification evidence

The mathematical dependencies are the complete proofs in
../independent_hydrostatic_evaluator/PROOF.md,
../hydrostatic_power_tail_inverse/PROOF.md,
../hydrostatic_axis_primitive/PROOF.md and
../hydrostatic_axis_core_moment/PROOF.md, together with the saved-basis reconstruction
proof ../dynamic_local_reconstruction/PROOF.md. Their current manufactured-test
and source-hash gates are checked before this run. Numeric checkpoints, frozen
producer tables for comparison only, a manifest, exact polynomial JSON certificates,
raw pointwise results, method settings, source hashes, and UTC timings are stored
under verification/. The final verdict will be written only after the computation
and independent summary checks finish.
