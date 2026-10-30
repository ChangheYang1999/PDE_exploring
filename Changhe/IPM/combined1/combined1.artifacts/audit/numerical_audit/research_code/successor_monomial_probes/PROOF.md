# Whole-plane monomial angular probes for successor candidates

## Statement and hypotheses

Let c>1 be rational, gamma=1/c and delta=1-gamma. The reference potential
is a finite exact sum a_(j,m,k) r^(2k)(1+r^2)^((3+gamma-j delta)/2-k)
cos(2m theta), with the origin cancellations of the audited canonical
candidate. Its density is R=-partial_y Delta chi and its canonical velocity
is u=(-chi_xyy,chi_xxy). Set F=(cX+u).grad R-R. Require all forbidden
residual sectors to vanish, the exact source hash to match the audited
candidate, and the complete integrals below to converge.

Let h be an S1-symmetric L2 correction solving the stationary equation at
this c in the distributional sense. Assume its canonical velocity U[h]
is divergence free and satisfies ||U[h]||2<=||h||2. All weak products must
be locally integrable. Let n be a positive odd integer and K an integer
with K>=(n-1)/2. Put t=r^2/(1+r^2), v=1-t and

    phi=r v^2 t^K sin(n theta).

This function is smooth at the origin: r^n sin(n theta) is a homogeneous
Cartesian polynomial, and the remaining factor is
(r^2)^(K-(n-1)/2)/(1+r^2)^(K+2). It decays as r^-3 at infinity.
Define I=integral F phi and let A,B,C,H be the explicit upper bounds below.
Then every such correction obeys

    |I| <= (A+B+C)||h||2+H||h||2^2,
    ||h||2 >= 2|I|/[A+B+C+sqrt((A+B+C)^2+4H|I|)].

Containing balls with a strict rational floor certify a necessary distance.
No sufficient existence condition or unknown actual solution is asserted.
Another trial c requires the separately audited tail-pinning hypotheses.

## Proof of the weak inequality and the bounds

The correction equation tested against phi and integrated by parts gives

    I=integral h[(2c+1)phi+cX.grad phi+u.grad phi]
       -integral phi U[h].grad R+integral h U[h].grad phi,

up to a harmless common sign convention for I. Absolute values and
Cauchy-Schwarz give the stated inequality, with
A=||(2c+1)phi+cX.grad phi||2,
B>=||u.grad phi||2, C>=||phi grad R||2 and H>=||grad phi||infinity.
The cutoff limit follows from R,u=O(r^gamma), gamma<1, the decay of phi,
the checked moment integrability and the assumed L2 correction bounds.

Writing D(v)=-3+(2K+4)v, polar differentiation gives

    partial_r phi=v^2 t^K D(v) sin(n theta),
    r^-1 partial_theta phi=n v^2 t^K cos(n theta).

Thus |grad phi|^2<=v^4 t^(2K)[D(v)^2+n^2]. Since |D(v)| is at most
max(3,2K+1), and n<=2K+1, a sharper pointwise bound on the gradient is
max(3,2K+1) v^2 t^K. The maximum of (1-t)^2 t^K is
4 K^K/(K+2)^(K+2) for K>0, by one differentiation, and is1 for K=0.
Take H to be the corresponding exact rational product.

The reference Cartesian field algebra writes each velocity component as
r sum_j v^((j+1)delta/2) U_j(t) trig(theta), and each density derivative
as sum_j v^((j+1)delta/2) V_j(t) trig(theta). All U_j,V_j are exact rational
polynomials. For each component and angular frequency, square the full
branch sum. Include all diagonal terms and twice each off-diagonal term,
with angular factor pi, or2pi for cosine frequency0. This constructs
polynomials G_b(v) for velocity and Q_b(v) for density derivatives, where
b=5-p_i-p_j and p_j=(3+gamma-j delta)/2. Then

    B^2=(pi/2) sum_b integral_0^1 v^b (1-v)^(2K+1)
                                      G_b(v)[D(v)^2+n^2] dv,
    C^2=(pi/2) sum_b integral_0^1 v^b (1-v)^(2K+1) Q_b(v) dv.

The preceding pointwise inequalities prove these upper bounds without
assuming angular independence. Every input angular mode is retained.
The squared drift norm is exact. With a=2K+2,
l0=3c+1+2cK and l1=2c(K+2), direct sine integration yields

    A^2=pi/[2a(a+1)] [l0^2-2l0l1 a/(a+2)
                         +l1^2 a(a+1)/((a+2)(a+3))].

For the pairing, construct the complete sine-n residual projection by
Cartesian differentiation and exact convolution of every input angular
pair. It has the form r sum_ell v^(ell delta/2) P_ell(t). Therefore

    I=(pi/2) sum_ell integral_0^1
          v^(ell delta/2-1) (1-v)^(K+1) P_ell(1-v) dv.

All integrals are full-plane moments, with no radial or angular truncation.
For a polynomial sum q_j v^j, they are finite sums of
q_j B(b+j+1,M+1). Exact b>-1 is checked. Evaluate the first Beta function
with outward Gamma balls and use
B(b+j+2,M+1)=B(b+j+1,M+1)(b+j+1)/(b+j+M+2).
This recurrence and outward polynomial products enclose every cross term.
Require positive energies, at least150 accuracy bits and a strict rational
radius floor verified against the containing ball.

## Independent calibration and dependencies

Before applying the method to successor013, reproduce the existing007
mode21,K522 result from the new direct residual projection, comparing
I,A,B,C,H and the radius. The earlier calculation used a separately
assembled complete residual cache. This checks projection normalization
without generating a new large cache. A second007 mode7,K131 calibration
can be run with the same code when needed. Candidate hashes and the source
sector audit are prerequisites, not substitutes for these integrals.

Dependencies are the fully audited angular_weak_probes/PROOF.md,
successor_weak_probes/PROOF.md, radial_fourier field recurrence and
localized_weak_probe/BETA_EVALUATION.md. All are in this lane's research
folder. The exact candidate coefficients stay in JSON. This proof was
written before the implementation. Results and peer status are recorded
separately in verification and verdict ledger.
