# A pointwise-gradient certificate for the limiting velocity profile

Status: proposed certificate, written before the checker. No finite
radius follows. The numerical value is asserted only after all cells
of the finite verification below have passed.

## Statement and exact data

Let c=4076476460239181/2251799813685248 and q=1/c-4. For each of
the exact endpoint data sets007,013,014, write f1=A and f2=100000P,
where A and P are their frozen odd sine polynomials. For real z=(z1,z2),
let f_z=z1 f1+z2 f2 and define

 G(z)=sup_theta sqrt(q^2 f_z(theta)^2+f_z'(theta)^2),
 N(z)=sup_theta |V_q[f_z](theta)|.

V_q is the canonical Hessian velocity of
r^(q+2) sum_n (f_z)_n sin(n theta)/((q+2)^2-n^2), evaluated at r=1.
It includes the contact term of the IPM operator. The claim to certify is

 N(z) <= (93/250) G(z) for every real z.                    (1)

Let h be C1 and S1, with finite
H_q=max(sup(1+r)^(-q)|h|,sup(1+r)^(1-q)|grad h|), and suppose
r^(-q)h(r e_theta) tends uniformly to (A+tP)/(4c) for some real t.
The audited theorem402/413 and the pointwise gradient limit then give

 limsup_(r->infinity) sup_theta
 r^(-q)|U[h](r e_theta)+DK(r e_theta)M[h]| <= (93/250) H_q.  (2)

The absolute first moment converges because q<-3. All spaces and
canonical conventions here are those in the frozen402 proof. There
is no assumption of convergence of the rescaled gradients.

## Reduction to two finite angular variables

Both sides of(1) are homogeneous in z. It suffices to take
z=(cos alpha,sin alpha) with -pi/2<=alpha<=pi/2, which covers all
real projective directions. Reflection symmetries of the odd sine
polynomials and their Hessian velocities reduce theta to[0,pi/2].
Define the symmetric2 by2 matrices

 Q_ij(phi)=q^2 f_i(phi)f_j(phi)+f_i'(phi)f_j'(phi),
 F_ij(theta)=V_q[f_i](theta) dot V_q[f_j](theta).

Thus G(z)^2>=z^T Q(phi)z for every selected witness angle phi, and
N(z)^2=sup_theta z^T F(theta)z. The exact F_ij are finite cosine
polynomials sum_n C_ij,n cos(n theta), with only even degrees.
A rigorous cell certificate is

 z(alpha)^T [E^2 Q(phi)-F(theta)] z(alpha)>0              (3)

for all alpha in one closed projective interval I and all theta
in[0,pi/2], with E=93/250 and a witness phi that may depend on I.
If a finite list of I covers[-pi/2,pi/2],(3) proves(1).
Witnesses need not be maximizing angles. A FLOAT search may select
them, but only the exact interval test(3) decides acceptance.

## Interval certificate and its error bounds

Write alpha=pi a, with rational a in a dyadic interval [l,r]. Let
alpha0=pi(l+r)/2 and h=pi(r-l)/2. Divide theta into M equal intervals
of[0,pi/2], with centers theta_j=(j+1/2)pi/(2M) and halfwidth
k=pi/(4M). Use a finite witness list phi_d=d pi/(2D),0<=d<=D.

For a symmetric matrix T, write

 c0=(T11+T22)/2, cc=(T11-T22)/2, cs=T12,
 t(alpha)=z^T Tz=c0+cc cos(2alpha)+cs sin(2alpha).

Since |t''|<=4sqrt(cc^2+cs^2), its value on I is bounded below by

 t(alpha0)-2| -cc sin(2alpha0)+cs cos(2alpha0)|h
             -2sqrt(cc^2+cs^2)h^2.                    (4)

Apply(4) to T=E^2 Q(phi_d)-F(theta_j). To account for theta variation,
subtract from that lower bound

 k U_j(I)+k^2 M2(I)/2,                                 (5)

where U_j(I) bounds |z^T F'(theta_j)z| on I, and

 M2(I)=sum_n n^2 sup_(alpha in I)|z^T C_n z|.

Each supremum in these definitions may use direct interval evaluation
of c0+cc cos(2alpha)+cs sin(2alpha). Taylor's theorem in theta proves
(5). All matrix entries, trigonometric values, square roots and error
terms are enclosed with Arb at the precision in parameters.json.
For each I, a strictly positive lower bound for every j proves(3).
Intervals that fail this sufficient test are bisected. The saved
rational endpoints, witness indices, minimum lower bounds and interval
coverage checks make the complete finite certificate reproducible.
No grid maximum is treated as a continuum maximum without(4)-(5).

## Derivation of(2) and limitations

For z=(1,t/100000), f_z=A+tP. The pointwise gradient-limit inequality
gives G(z)/(4c)<=H_q. The uniform compensated-velocity limit is
V_q[f_z]/(4c), so(1) gives(2). The endpoint equation is needed only
to place the tail in this span; it is not inferred from this estimate.

This is a profile-subspace estimate and does not contradict the
universal weighted-C1 lower coefficient0.7930365. It is asymptotic,
requires the exact frozen endpoint profiles, and supplies neither
an upper bound on H_q nor the finite-radius constants required by
CI351. A failed cell would mean the particular discretized certificate
needs refinement; it would not refute(1).
