# A strict improvement inside the projection pairing

## Statement and scope

Use the real homogeneous Holder seminorm and kernel conventions of
../../../01_setup/PROOF.md. The projection operator P_R, the number A_alpha,
and the positive measure Q_R are defined in ../PROOF.md. For every
0<alpha<1 define the integer and positive numbers

    n = ceil(10625/alpha),
    epsilon = alpha/(150000 n),
    delta_alpha = alpha^2 epsilon^2/12500.

Then, for every R>0, every real f with finite homogeneous alpha-Holder
seminorm, and every z in R^2,

    |P_R f(z)| <= (A_alpha/alpha - delta_alpha) R^alpha [f]_alpha.   (1)

In particular the pointwise projection bound A_alpha R^alpha/alpha is
strictly larger than the norm of P_R for every exponent. This statement
concerns P_R alone. No subtraction from a bound using only a retained
part of this plan is asserted without checking which edges remain.
The constants are conservative. They do not change any displayed decimal
in the final numerical table.

Put Atilde_alpha=A_alpha-alpha delta_alpha. The unchanged decomposition
N_R=P_R+I/pi-Q_R and the far derivative estimate imply the explicit bound

    D_alpha <= 2 Atilde_alpha / (alpha(1-alpha))
               * ((1-alpha) B_alpha/(2 Atilde_alpha))^alpha + 1/2,  (2)

which is strictly smaller than G_proj from ../PROOF.md. Here D_alpha is
the R_1^2 norm, B_alpha is from ../../../02_upper_bounds/PROOF.md, and
Atilde_alpha>0. This is a supplemental improvement of the original
projection bound, not a claim that (2) is the best bound in the report.

## The projection map and the source measure

Set R=1 and work in the positive half-lobe 0<v<u. For p=(u,v) write

    a(p) = (2uv^2/(u^2+v^2), 2u^2v/(u^2+v^2)).

Reflection in the adjacent zero ray sends (u,v) to (v,u), and the
projection factor is 2uv/(u^2+v^2). Thus a is exactly the target of P_1.
The source measure has density

    K(p) = (u^2-v^2)/(2 pi (u^2+v^2)^2).

The original edge length is

    s(p)=|p-a(p)|=(u^2-v^2)/sqrt(u^2+v^2).

The original total cost over all four positive half-lobes is
A_alpha/alpha. Although the source measure has infinite total mass near
the origin, its alpha-cost is finite. All modifications below take place
in a compact region away from the origin and have finite mass.

The projection map is 2-Lipschitz on the first-quadrant half-lobe. Indeed,
in polar coordinates its radial derivative has length |sin(2theta)|,
and its unit angular derivative has squared length
4 cos^2(2theta)+sin^2(2theta). Their scalar product need not vanish, so
these two length bounds alone do not prove the assertion. Instead observe
that a(p)=p-s(p)e(p), or compute its Jacobian directly: in radial and
angular orthonormal bases the matrix is

    [[sin(2theta), 2 cos(2theta)], [0, -sin(2theta)]].

Its operator norm is 1+|cos(2theta)|, at most 2. The convexity of the
half-lobe then gives the Lipschitz bound by integration along segments.

## A positive circulation

Let H=[2/5,4/5] x [1/10,1/5], oriented counterclockwise, and define

    g(p) = grad_p |p-a|^alpha evaluated at a=a(p)
         = alpha (u^2-v^2)^(alpha-1) (u^2+v^2)^(-alpha/2) (u,-v).

The gradient here differentiates the first argument of the cost while
holding its second argument fixed. A direct differentiation gives

    curl(g) = partial_u g_2 - partial_v g_1
            = 2 alpha^2 u v (u^2-v^2)^(alpha-1)
                (u^2+v^2)^(-1-alpha/2).

On H, uv>=1/25, 0<u^2-v^2<1, and u^2+v^2<1. Consequently
curl(g)>=2alpha^2/25. The area of H is 1/25, so Green's theorem gives

    integral_boundary(H) g dot dp >= 2alpha^2/625.                 (3)

## From the circulation to a finite cycle

Subdivide each of the four sides of H into n equal segments, giving
4n successive points p_i and cyclic indices. Consider the alternative
edges p_i to a(p_(i+1)). Their total saving against the original edges is

    E = sum_i (|p_i-a(p_i)|^alpha-|p_i-a(p_(i+1))|^alpha).

Telescoping the original costs also writes E as

    sum_i (|p_(i+1)-a(p_(i+1))|^alpha
                 -|p_i-a(p_(i+1))|^alpha).

For each side segment this is the integral of the first-argument gradient
with a(p_(i+1)) held fixed. On H, s(p)>=s(2/5,1/5)>1/4.
Each segment has length at most 2/(5n). Since n>=16, the distance from
p to every point between a(p) and a(p_(i+1)) is at least
1/4-4/(5n)>=1/5. The Hessian of the cost |p-a|^alpha in either argument
has norm at most alpha |p-a|^(alpha-2), hence at most 25alpha there.
Together with the 2-Lipschitz bound for a, the error on a segment of
length h is at most 50alpha h^2. The sum of the squared segment lengths
is 17/(50n). Therefore (3) yields

    E >= 2alpha^2/625-17alpha/n >= alpha^2/625.                    (4)

The last step is precisely n>=10625/alpha. No finite numerical search
or optimal-transport existence theorem is used.

## Replacing point edges by positive source mass

For each p_i use the disk p_i+B(0,epsilon). They are disjoint: successive
centers on the shorter sides are 1/(10n) apart, whereas
2epsilon<1/(10n). Every disk lies in the enlarged rectangle
[39/100,81/100] x [9/100,21/100]. Here u^2-v^2>=108/1000 and
u^2+v^2<=7002/10000<71/100. It follows that K(p)>=1/(40pi).
Extract from every disk the same uniform density 1/(40pi), a submeasure
of the original source measure. Its mass per disk is epsilon^2/40.

For each common offset w in B(0,epsilon), replace the 4n original edges

    p_i+w -> a(p_i+w)

by

    p_i+w -> a(p_(i+1)+w).

The source marginals remain identical, and the target submeasures are
merely permuted. The signed operator P_1 is therefore unchanged.

It remains to check the cost uniformly in w. On H all original distances
exceed 1/4 and all new distances exceed 1/5. In fact the latter exceed
1/4-4/(5n), and with n>=10625 this is greater than 0.2499.
The perturbation of either distance is at most 3epsilon, by the
2-Lipschitz bound. Thus the entire interpolation in w has distance
at least 1/5. The cost gradient has norm at most 5alpha. Each of the two
costs in one summand changes by at most 15alpha epsilon, and the total
saving changes by at most 120 n alpha epsilon=alpha^2/1250.
By (4), the saving for every w is at least alpha^2/1250.
Multiplication by the common disk mass gives a cost reduction at least
alpha^2 epsilon^2/50000 in this half-lobe.

Reflect this construction in the two coordinate axes to obtain the
same saving in the other three positive half-lobes. The four compact
source regions are disjoint. The total saving is delta_alpha as stated.
Every unmodified edge still obeys the original Holder cost estimate.
This proves (1) at R=1. Scaling yields R^alpha and translation gives any z.
An unmodified positive-cost region remains, so Atilde_alpha>0.

## Consequence for the diagonal transform

For h=|x-y|, applying (1) at x and y replaces the local contribution
2A_alpha R^alpha/alpha by
2(A_alpha/alpha-delta_alpha)R^alpha. The positive measure Q_R and the
remaining local identity coefficient still have total mass 1/2.
The far term is B_alpha hR^(alpha-1). Minimizing over R/h gives (2).
Since the resulting nonconstant factor is proportional to
Atilde_alpha^(1-alpha), the improvement over G_proj is strict.
The quotient-space interpretation and compact smooth approximation are
unchanged. Complex inputs for the real scalar operator follow by phase
projection.

## Verification and status

The proof is elementary and independent of the floating cycle search.
The source coordinates and a small illustrative cycle are recorded in
verification/cycle_certificate.json. That certificate checks the curl
identity, the Jacobian norm identity, and selected finite-cycle costs;
it is not needed for the general analytic inequality above.

Status at creation: OPEN pending independent lead cross-read.
