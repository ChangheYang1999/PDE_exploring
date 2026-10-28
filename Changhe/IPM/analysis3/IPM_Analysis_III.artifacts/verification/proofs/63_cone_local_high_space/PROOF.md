# Lower regularity away from the vertical axis in the nonlinear high space

## Setting and statement

Use the exact spaces from proof 57:

    a=17/4, eta=5/4,
    w=|x|^(-2a) max(1,r)^(2a-eta), R=L2_P(w dX),
    X0=E B direct-sum R, Y=E G direct-sum R,
    Z=E B direct-sum D(V.grad-1 on R), E beta=x^2 y beta(log r).

P is even-x odd-y parity. The actual field V and scalar space B satisfy
the hypotheses of proof 57, including positive axis rate. Let

    1/4<delta<2, gamma<-3/8, s>2, 0<epsilon<1.

Let H_base be the factored H7-cylinder space H_(delta,gamma) of proof 57,
including its scalar cubic coefficient. Choose a fixed smooth positive
radial factor b(t) equal to exp((3+delta)t) for t<=0 and exp(gamma t)
for t>=1. Define the bulk space

    Q_(epsilon,s)={h(X)=b(log r)v(log r,theta):
       v in Hs(R times S1), v has parity P,
       supp v contained in {|cos(theta)|>=epsilon}},
    ||h||_Q=||v||_Hs.

The value at0 is its continuous extension0. Finally set

    H_cone=H_base+Q_(epsilon,s)

with the infimum Hilbert sum norm. Then:

1. H_cone is a Hilbert space continuously embedded in Z. Its cubic
   coefficient J is continuous and classical, in the uniform sense
   h/(x^2 y)=J+O(r^delta) off the axes, with the quotient continuously
   extended where needed.
2. There are finite constants C,C_V, depending on the fixed data, with

       ||W[d].grad h||_Y<=C||d||_X0||h||_Hcone,
       ||D W[h]||_infinity+|c[h]|<=C_V||h||_Hcone,
       W[d]=U[d]+c[d]X/3.

3. The same conclusions hold if Q is restricted further to t<=T, for
   any fixed finite T. This variant keeps the original H7 regularity at
   infinity and lowers regularity only away from the vertical axis in
   a bounded radial region, including the source and the x-axis direction
   at the origin.

For example delta=3/2, gamma=-1/2, s=21/10 is admissible. The mapping
bounds therefore do not require global H7 regularity or H7 regularity
near the sources. No inverse, propagation of variable regularity, or
nonlinear existence result is claimed here.

## Elementary bulk bounds and embedding

For any 0<alpha<min(1,s-2), cylinder Sobolev embedding gives

    ||v||_(C1,alpha)<=C||v||_Hs.

This follows by Fourier Cauchy-Schwarz for first derivatives and their
alpha increments; the required frequency integral converges when
s>2+alpha. In particular v and its first derivatives are uniformly
bounded. On a dyadic physical annulus r~R0 this gives

    |h|<=C b(log R0)||h||_Q,
    |grad h|<=C b(log R0)/R0 ||h||_Q,                       (1)

and the scaled C1,alpha norm obeys the same bound. All constants absorb
the fixed smooth transition of b.

The bulk support stays a fixed angular distance from x=0, so w is
comparable there to r^(-2a) for r<=1 and r^(-eta) for r>=1. Its squared
R norm is bounded by the logarithmic integrals with exponents

    2delta-1/2 at0, 2gamma+3/4 at infinity.                (2)

Both converge. Since V=O(r) globally, (1) gives the same integrals for
V.grad h-h. Thus Q embeds continuously into the maximal remainder
transport domain D_R. These distributional products agree with the
ordinary locally bounded first derivatives away from0; the vanishing
at0 makes their global distributional extensions legitimate. For
example the boundary flux of h on r=r0 is O(r0^(4+delta)), which tends
to0 as r0 tends to0.

Oddness across y=0 and the bounded angular derivative imply
|v(t,theta)|<=C|sin(theta)| ||h||_Q. On the support, |cos(theta)|>=epsilon.
Hence h/(x^2 y)=O(r^delta) near0, uniformly in angle after continuous
extension across y=0; near x=0 the function is identically zero. Thus
J=0 for every bulk element. The known H_base embedding supplies its
classical J. The sum map H_base direct-sum Q -> Z is continuous, so its
kernel is closed. The quotient by this kernel gives precisely the
infimum norm and proves that H_cone is a Hilbert space with an injective
continuous map into Z. Classical J does not depend on a decomposition.
The extra support condition t<=T is closed in Hs and causes no change.

## The bulk product: jet input and the scalar strain

The high-base product is proved in proof 57. It remains to prove the
product for h in Q. It is supported away from the vertical axis, so its
axis row is zero and it suffices to bound it directly in R.

For d=E beta, the explicit two-mode Green formulas of proof 47 and the
B bounds give

    |U[E beta](X)|<=C||beta||_B r, r<=1,
    |U[E beta](X)|<=C||beta||_B r^(-3/8), r>=1.

The full scalar strain is bounded by C||beta||_B r at every radius.
Together with (1) and (2), this proves

    ||W[E beta].grad h||_R<=C||beta||_B||h||_Q.             (3)

For d in R, c is already a bounded functional. Therefore
(c[d]/3)X.grad h has the same bound. It remains to treat U[d].grad h.
The following estimates use the ordinary unweighted L2 multiplier bound
only where the weight is locally comparable. No A2 assertion for w is
used.

## Comparable input and output radii

On an output annulus r~R0, restrict the input to R0/8<|Z|<8R0. The
canonical velocity multipliers have bounded ordinary L2 norm. On the
input annulus the weight has the lower bound C R0^(-2a) near0 or
C R0^(-eta) at infinity. On the bulk output it has a comparable upper
bound, with a constant depending on epsilon. Thus

    ||1_output U[1_input d]||_R<=C_epsilon||1_input d||_R.

Multiplication by (1) costs at most

    C||h||_Q R0^(2+delta) near0,
    C||h||_Q R0^(gamma-1) at infinity.                     (4)

These factors are bounded over all dyadic radii. Output annuli can be
chosen disjoint, while the expanded input annuli overlap only a fixed
finite number of times. Squaring and summing proves the global bound
for this part.

## Smaller input radii

For |Z|<r/4, odd parity in the source y coordinate makes the integral
of d over the radial input region zero. Subtract the kernel value at Z=0.
The derivative of each off-diagonal velocity kernel has size at most
C r^(-3), giving

    |K(X-Z)-K(X)|<=C |Z| r^(-3).

The product kernel is therefore bounded by
C||h||_Q b(log r) r^(-4)|Z| on the bulk output. Its source inverse-weight
integral satisfies

    integral_(|Z|<r/4) |Z|^2 w(Z)^(-1)dZ
       <= C r^(2a+4) for r<=1,
       <= C r^(eta+4) for r>=1.

Its squared weighted Hilbert-Schmidt norm is consequently bounded by
C||h||_Q^2 times

    integral_0^1 r^(3+2delta)dr
                +integral_1^infinity r^(2gamma-3)dr.       (5)

Both integrals converge. Parity subtraction is first justified on
smooth radial truncations and then by these absolute weighted bounds.

## Larger input radii

For |Z|>4r, each velocity at X=0 vanishes after integration against the
parity-P input on this radial region. For U1, the kernel is odd in the
source x coordinate after multiplication by d; for U2 it is odd in the
source y coordinate. Subtract this zero term. The first kernel derivative
gives

    |K(X-Z)-K(-Z)|<=C r |Z|^(-3).

The product kernel is now bounded by
C||h||_Q b(log r)|Z|^(-3). The source integral satisfies

    integral_(|Z|>4r) |Z|^(-6)w(Z)^(-1)dZ
       <= C for r<=1,
       <= C r^(eta-4) for r>=1.                            (6)

At0, convergence follows from 2a-5>-1; at infinity it follows from
eta-5<-1. The squared weighted Hilbert-Schmidt norm is bounded by
C||h||_Q^2 times

    integral_0^1 r^(2delta-3/2)dr
                +integral_1^infinity r^(2gamma-3)dr.       (7)

The first is exactly where delta>1/4 is required. The second converges
because gamma<1, already implied by the stated stronger far condition.
Equations (3)-(7) prove the bulk product estimate. They use only the
bulk first-derivative envelope (1); no bulk C5 bound is needed.

All these estimates extend from smooth parity-preserving truncated
inputs. Low inputs converge in local L2 velocity and in c; high bulk
inputs converge locally with first derivatives and the uniform weighted
envelopes. The limit is the canonical locally integrable product. It
vanishes near each nonzero point of the vertical axis, has no extra
axis distribution, and its global R bound is the one proved above.

## The global velocity derivative bound

The annular C1,alpha bounds give

    |grad h|=O(r^(2+delta)) near0, O(r^(gamma-1)) at infinity,
    [grad h]_(Calpha on r~R0)<=C b(log R0)R0^(-1-alpha)||h||_Q.

These seminorms are uniformly bounded: 2+delta-alpha>0 at0 and
gamma-1-alpha<0 at infinity. Comparing points in widely separated
annuli using their distance and the pointwise bounds proves the global
Calpha estimate. The squared L2 norm of grad h is bounded by the radial
integrals with powers 5+2delta at0 and 2gamma-1 at infinity. They converge.
Thus

    ||grad h||_infinity+[grad h]_Calpha+||grad h||_2
        <= C||h||_Q.

For each component and g=partial_j h, the canonical kernel split gives

    ||U_i[g]||_infinity
      <= (1/2)||g||_infinity+[g]_Calpha/alpha
                                +||g||_2/(2 sqrt(pi)).    (8)

The local difference integral, far Cauchy-Schwarz integral and local
point-mass term establish (8), as in proof 57. Derivatives commute with
the canonical velocity here: the differentiated input is integrable in
the displayed classes, and radial cutoff errors vanish by the origin
and far powers above. Therefore (8), continuity of c, and the existing
H_base estimate prove the second bound in statement2.

## Consequence for the proposed variable-order approach

One may take low order s=21/10 in every cone bounded away from x=0,
including the x-axis segment and source neighborhoods, while retaining
H7-cylinder regularity near x=0. Restricting the bulk component to t<=T
retains H7 at infinity as well. These are exact Hilbert spaces with
continuous classical normalization, a defined image, and a proved
low/high nonlinear product. They satisfy the mapping portion of the
proposed approach with high regularity required only in the specified
regions.

This does not show that the linearized or quasilinear inverse preserves
these spaces. Pointwise frozen thresholds and an escape function do
not supply the missing commutator estimates or compatibility at the
interfaces. No derivative-level energy theorem is inferred here.

## Dependencies and status

Dependencies: proof 57's factored high space and its low/high estimate;
proof 47's explicit jet-input Green formulas; the actual transport
properties of proof 52; the bounded strain functional; the ordinary
unweighted L2 multiplier bound and cylinder Sobolev embedding. All new
bulk estimates and target membership checks are given above.

CONFIRMED under the same positive-axis hypothesis as proof 57. The actual
uniform high inverse and nonlinear closure remain OPEN.
