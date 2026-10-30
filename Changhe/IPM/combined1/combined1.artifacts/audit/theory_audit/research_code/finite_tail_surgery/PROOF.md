# Finite tail removal and a reference at the dipole endpoint

This independently checks R2 and R3 of the frozen Opus review
the review of T4-324 and applies the result to a third cutoff. It is a finite
reference construction. No infinite iteration or stationary solution
is asserted. The proof is written before its specialization checker.

## 1. Finite-order theorem with explicit expansion assumptions

Fix the campaign numbers

    c=4076476460239181/2251799813685248,
    gamma=1/c, delta=1-gamma=A/B,
    A=1824676646553933, B=4076476460239181.

Let R be a real smooth S1 reference with canonical velocity U_R.
Assume |U_R|<=V r^gamma and |grad R|<=G r^(gamma-1) outside a disk.
Write e(K,L)=1-K delta-2L, with nonnegative integers K,L.
Fix T>=1-2A.

Assume the density R and velocity U_R have asymptotic expansions in
these exponents with finite trigonometric polynomials at each exponent.
Require the expansions and their first derivatives uniformly in angle
through every finite order used below, with remainders and their first
derivatives bounded by the corresponding radial powers. It suffices
instead to have a convergent expansion outside a larger disk with
termwise differentiated convergence there. There is no term of degree
greater than gamma in R or U_R. Assume every nonzero residual sector
of F(R)=cX.grad R-R+U_R.grad R above T has K>=1 and e(K,L)<-1.

Then, for every epsilon>0 and every prescribed disk, there are finitely
many smooth potential cutoffs h_j, each vanishing with its velocity
on that disk, such that

    ||sum_j h_j||_2<epsilon,
    ||F(R+sum_j h_j)-F(R)||_2<epsilon,
    F(R+sum_j h_j)=O(r^T).

The last two norms make sense when F(R) is in L2; even without that
assumption the displayed difference belongs to L2. Every origin jet
and the prescribed leading profile are preserved. If any finite list
of weighted derivative norms has negative dilation exponent for all
the cutoffs used, those correction norms can also be made smaller
than epsilon.

Proof. There are finitely many pairs (K,L) with e(K,L)>T. Since delta
is positive, both K and L are bounded. Exponents can coincide; combine
their finite angular polynomials before each removal.

Suppose the current leading nonzero residual above T is r^q D(theta),
where q=e(K,L)<-1 and K>=1. To apply the finite angular inverse of
T4-324 we need q+3 outside the even integers. If q+3 were even, then
K A/B would be even. Since A,B are coprime and A is odd, K would be
a positive multiple of 2B. But e(K,L)>T>=1-2A implies K A/B<2A,
so K<2B, a contradiction. This proves nonresonance at every step.

Set B_q=D/(1-cq). The explicit triangular inverse in T4-324 gives a
finite even-cosine potential r^(q+3)P_q whose density is r^q B_q.
Cut it off outside a radius larger than twice all previous radii.
The resulting canonical velocity is exactly homogeneous of degree q
outside twice the new radius. Its linear residual is -r^q D.

A product with a reference term of degree e(K',L') has degree
q+e(K',L')-1=e(K+K',L+L'). The reference growth assumption gives
e(K',L')<=gamma, so this is at most q-delta. The self product has
degree 2q-1<q. Its label is (2K,2L). All newly created labels have
positive first coordinate and lower exponent. Products with the
previous cutoffs satisfy exactly the same rules. No removed exponent
is reintroduced. After finitely many steps no residual exponent above
T remains. The uniform remainder assumptions imply O(r^T).

At step j the current reference is already fixed. T4-324 gives

    ||h_j||_2=C_j L_j^(q_j+1),
    ||F(R_j+h_j)-F(R_j)||_2
       <=C_lin,j L_j^(q_j+1)
          +C_mix,j L_j^(q_j+gamma)+C_quad,j L_j^(2q_j).

All powers are negative and the constants are finite. Choose each
radius successively so that both costs are less than epsilon/2^(j+1).
Their sums are less than epsilon. The radius may also enforce the
finite list of other negative-power bounds. Summing the residual
differences is legitimate because the references R_j are successive.
The support and leading-profile assertions follow from each cutoff.
This proves the theorem.

The proof does not give uniform constants as T tends to minus infinity.
It neither defines an infinite sum nor controls an inverse operator.
The astronomical lower bound on T is an arithmetic nonresonance
statement, not a proposal to compute that many sectors.

## 2. The third campaign sector

For the exact references 007, 013 and 014, the already verified leading
residual sectors are

    q1=e(4,1)=-1-4delta,
    q2=e(9,0)=1-9delta,
    q3=e(5,1)=-1-5delta,
    qstar=e(1,2)=gamma-4.

The original finite algebraic formulas have convergent expansions
in r^-2 outside a disk, with the stated differentiated remainders
and finite angular coefficients at every exponent. Their density and
velocity leading degree is gamma. They therefore supply the expansion
and growth assumptions used here.

After the first cutoff, let A3 be the (5,1) residual coefficient.
It is computed from the original sector maps by setting the density
and stream (4,1) coefficients to zero and evaluating the complete
quadratic residual convolution. By T4-334 this equals the coefficient
after the global algebraic repair. The first cutoff changes A3 from
its original value. The second does not: its mixed terms have degree
at most q2-delta=e(10,0)<qstar, and its self term is lower still.

Consequently the twice-repaired reference R2 has

    F(R2)=r^q3 A3+r^qstar Astar+O(r^(qstar-epsilon0)),

for some epsilon0>0, where Astar is the original (1,2) coefficient.
This is R2 of the Opus review, now with the remainder assumption
and the distinction between the two cutoffs made explicit.
The forced-tail theorem T4-317 applies to a new correction k of R2,
provided H_q3(k)<infinity. It forces the angular coefficient
A3/(1-cq3). It does not constrain arbitrary L2 corrections.

Solve the same finite angular inverse with q=q3 and
B3=A3/(1-cq3), then use a third potential cutoff h3 with radius
larger than twice the second. Here -2<q3+3<0, so nonresonance holds
for every finite angular support. The linear residual removes A3.
All its mixed terms have degree at most q3-delta<qstar, and its
self term has degree 2q3-1<qstar. Thus

    R3=R+h1+h2+h3,
    F(R3)=r^qstar Astar+O(r^(qstar-epsilon1))                  (1)

for some epsilon1>0. The leading density profile Theta is unchanged.
The three corrections and their residual changes can simultaneously
have arbitrarily small L2 norms and vanish on any prescribed disk.
In particular they preserve a strict existing distance exclusion
when their total norm is smaller than its margin.

This proves that a reference meeting the asymptotic hypotheses of
the moment-resolved endpoint theorem can be constructed. The constants
V,G,E_F,E_R and its starting radius are finite but not numerically
certified here; (1) is an exact asymptotic statement.

## 3. Conditional endpoint consequence

T4-335 remains OPEN independent review. Conditional on its validity,
apply it to R3. For any real S1 C1 stationary correction k with
H_qstar(k)<infinity and m=integral y k,

    k=r^qstar [Astar+(m/pi)P]/(4c)+o(r^qstar),
    P=gamma cos(2theta)Theta+sin(2theta)Theta'.

The differentiated expansion of grad R3 required by that theorem
follows from the original expansion and the three lower-degree
homogeneous cutoffs. The original exact Astar and Theta, hence P,
are unchanged. T4-305 and the exact checks of T4-335 show
Astar is not in span(P) for 007, 013 and 014. Therefore, conditional
on T4-335, no correction of R3 with H_qprime finite for qprime<qstar
can be stationary. The limiting circle coefficient has lower bounds
85017, 85018 and 85016 respectively.

These are angular coefficient bounds. They are not whole-plane L2
distance estimates. Removing the endpoint itself by a fourth cutoff
is permitted by section1, so there is no obstruction to all finite
reference design. That fourth cutoff would change Astar and the
present endpoint conclusion would have to be recomputed.

## 4. Verification and scope

The checker reads copied exact sector maps for all three references,
sets the (4,1) density and stream to zero, and recomputes A3 by the
complete residual convolution. It compares every available original
sector with the same convolution before changing any coefficients.
It verifies the original endpoint data and its preservation, computes
the unique third potential by exact rational arithmetic, and applies
the direct density formula back to that potential. Large coefficients
are stored only in JSON.

The checker also verifies every relevant exponent comparison and the
coprimality and parity used in section1. Directed Arb arithmetic is
used only for the finite angular norms. Numerical values of cutoff
radii quoted in the peer review remain FLOAT and are not used here.
The finite-order and third-cutoff assertions are an independent audit
of Opus R3, while section3 retains the OPEN dependency on T4-335.
