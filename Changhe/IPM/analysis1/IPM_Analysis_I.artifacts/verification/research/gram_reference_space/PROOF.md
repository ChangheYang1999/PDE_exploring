# The H1m reference functions and the central coefficient

## Statement, notation and scope

Fix L>0 and 0<k<1. Put r=(x^2+y^2)^(1/2), p(x,y)=x^2 y,
u=r/L, m(r)=u^3(1+u^2)^((k-3)/2), and
w(r)=m(r)^(-2)(1+r^2/L^2)^(-3/2) for r>0.
Let X consist of functions with weak first derivatives on every compact
annulus and finite norm

    ||h||_X^2 = integral_R2 [h^2+r^2|grad h|^2] w(r) dx dy.

The derivatives are distributional weak derivatives, not derivatives
computed separately on pieces. This is the H1m expression in the numerics
lane's current src/c2_gram.py. The following claims hold.

1. For each R>0, J_R=p 1_{r<R} is not in X. Its finite piecewise-gradient
   energy is not its X-norm. Consequently a global X-angle with J_R,
   and a global X-orthogonal projection onto span{J_R}, are undefined.
2. The source definitions J_code=J_exp(t0) and
   J_inner=J_exp(tmin) have this defect. It occurs also for the unweighted
   H1 variant. It does not occur for the derivative-free L2y expression
   solely because these references have a jump.
3. On the subspace of X of functions h=p a with a continuous near the
   origin, the linear central coefficient a(0) is unbounded in ||.||_X.
   Explicitly, for 0<epsilon<=L let

       h_epsilon = p (1-r^2/epsilon^2)_+^6.

   Then h_epsilon is C^5 and compactly supported, its central coefficient
   is1, and ||h_epsilon||_X^2 < L^6 epsilon^2. In particular these norms
   tend to zero as epsilon tends to zero.

These assertions concern the diagnostic H1m space. They make no claim
against a stronger space used in a final inverse theorem. They do not
reject a finite Gram form restricted to genuinely continuous combinations,
nor the derivative-free L2y diagnostics. The C2 matrices and spectra have
not been independently recomputed here.

## Proof of the jump obstruction

On a compact annulus containing r=R the functions w and r^2w are positive,
continuous and bounded above and below by positive constants. Thus an
X-function has ordinary locally square-integrable weak gradient there.
For any smooth vector test function F supported in that annulus, integration
by parts on the disk gives

    <grad J_R,F>
      = integral_{r<R} grad p . F dxdy
        - integral_{r=R} p F . nu dS,               (1)

where nu=(x,y)/R is the outward normal. This proves the distributional
identity grad J_R=1_{r<R} grad p-p nu delta_{r=R}.
The second term is nonzero. Here is a direct proof that it is not an L2
function, avoiding any informal treatment of the delta term.

Choose a nonnegative smooth angular function phi, not identically zero,
supported in (pi/6,pi/3), and a smooth function eta supported in (-1,1)
with eta(0)=1. For 0<d<R/4 define

    F_d(r,theta)=nu(theta) phi(theta) eta((r-R)/d).

Its support has area O(d), and its L2 norm is O(d^(1/2)). The first term
in (1) is O(d), because grad p is bounded on the fixed annulus. The
second term is independent of d and equals

    -R^4 integral cos(theta)^2 sin(theta) phi(theta) dtheta < 0.

If grad J_R were locally L2, its pairing with F_d would tend to zero by
Cauchy-Schwarz. Equation (1) instead tends to this strictly negative
constant. This contradiction proves claim1. The same local argument
applies when the positive continuous factor m^(-2) is omitted.

The current source has radial coefficient1 on (-infinity,t0) for its
J column and zero afterwards, with a redundant split at tmin; its added
J_inner reference has coefficient1 only on (-infinity,tmin). Each has
angular coefficient1 in the m=0 mode, so multiplying by x^2y gives the
specified J_R. Values assigned exactly on a circle do not change this
argument. The Gram routine evaluates the classical derivative on each
piece and integrates those values. That omits the circle term of (1).
A zero jump of an actual linear combination cancels the circle term,
which explains why this reference objection by itself says nothing
adverse about the Gram on an exactly continuous constraint subspace.

For comparison, J_R belongs to the stated L2y space: dividing p^2 by
y^2 gives x^4 almost everywhere, and its compact support makes
integral x^4(1+r^2/L^2)^(-1129/1000) dxdy finite. No derivative is used.

## Exact norm computation for a concentrated central coefficient

Write s=r/epsilon, chi(s)=(1-s^2)^6 on 0<=s<=1 and zero afterwards.
This cutoff has a zero of order6 at s=1; multiplying by p gives a C^5
function across r=epsilon. Near zero it is a polynomial in x,y, and its
factor has value1. With Phi(theta)=cos(theta)^2 sin(theta),

    Phi=(sin(theta)+sin(3theta))/4,
    integral_0^{2pi} Phi^2 = pi/8,
    integral_0^{2pi} (Phi')^2 = 5pi/8.             (2)

Since h_epsilon=r^3 chi(r/epsilon) Phi, its radial logarithmic derivative
is r^3(3chi+s chi')Phi and its angular derivative is r^3 chi Phi'.
Substitution in the norm and (2) therefore gives exactly

    ||h_epsilon||_X^2
       = (pi/8)L^6 epsilon^2 integral_0^1
           s(1+(epsilon s/L)^2)^(3/2-k)
           [15chi^2+6s chi chi'+s^2 chi'^2] ds.   (3)

The bracket is 6chi^2+(3chi+s chi')^2 and is nonnegative. Because
0<k<1 and epsilon<=L, the weight in (3) is at most2^(3/2-k)<3.
The following exact polynomial integrals give the remaining constant:

    I0 = integral_0^1 s chi^2 ds = 1/26,
    integral_0^1 s^2 chi chi' ds = -I0,
    I2 = integral_0^1 s^3 chi'^2 ds = 12/143.

The middle identity follows by integrating (chi^2)'/2, whose boundary
term s^2chi^2 vanishes at both endpoints. For the last identity, put
z=s^2 and use chi'=-12s(1-s^2)^5:

    I2 = 72 integral_0^1 z^2(1-z)^10 dz
       = 72 * 2! 10! / 13! = 12/143.

The integral of the bracket times s is thus

    15I0-6I0+I2=9/26+12/143=123/286.

It follows that

    ||h_epsilon||_X^2 <= (369pi/2288)L^6 epsilon^2
                         < L^6 epsilon^2,        (4)

using pi<4 and 1476<2288. This proves finite norm, the claimed convergence,
and the unboundedness of the central coefficient functional. Indeed,
any bound |a(0)|<=C||h||_X would give 1<CL^3 epsilon for every epsilon>0,
an impossibility. The factor a(0) is unique: away from the coordinate
axes it equals h/p, and its continuous extension at0 is determined by
those values.

## Dependencies and what still needs checking

The mathematical proof uses only elementary distributional integration
by parts, Cauchy-Schwarz, polar coordinates, polynomial integration and
trigonometric orthogonality. Source linkage will be checked independently
against frozen read-only snapshots. Two distinct exact arithmetic methods
will check (2) and the polynomial constants in (3)-(4). The raw reported
JSON values, their norm-versus-squared-norm labels and any statements about
row refinement will be treated as floating diagnostics only. Global
invertibility, physical residual bounds, a strict closing inequality and
a meaningful exclusion neighborhood all remain OPEN.
