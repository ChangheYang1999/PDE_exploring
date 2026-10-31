# Shell distance under an axial rotation

Status: the identities and finite-search inequalities below are proved in exact arithmetic. Their numerical use in this campaign is empirical; no interval arithmetic or certified quadrature error is supplied.

## 1. A rotation becomes a shift of cylindrical components

Let Q_gamma be rotation by gamma about the z axis, and let T_gamma U(y)=Q_gamma U(Q_{-gamma}y). For cylindrical radius rho>0 write y=(rho cos(phi),rho sin(phi),z), e_rho(phi)=(cos(phi),sin(phi),0), e_phi(phi)=(-sin(phi),cos(phi),0), and e_z=(0,0,1). Suppose a measurable field U has cylindrical component vector u(rho,z,phi) in this orthonormal frame. Then T_gamma U has cylindrical components u(rho,z,phi-gamma). Indeed Q_gamma sends each frame vector at phi-gamma to the corresponding frame vector at phi. Expanding U(Q_{-gamma}y) in that frame proves the assertion. The axis has zero three-dimensional measure and does not affect shell L2 norms.

This T_gamma equals T_{-gamma} in ../../rotation_generator/PROOF.md. This identity fixes the sign convention: positive gamma actively rotates the field counterclockwise when viewed from the positive z axis. It is not a shift of Cartesian components alone.

## 2. Exact Fourier formula for the shell distance

Let J be a finite nonempty set. For each j let (X_j,nu_j) be a probability space of meridional coordinates. Let M be a nonnegative integer. Suppose u_j and v_j are real vector functions on X_j times the azimuthal circle with finite Fourier representations

u_j(x,phi) = sum_{m=-M}^M a_{jm}(x) exp(i m phi),
v_j(x,phi) = sum_{m=-M}^M b_{jm}(x) exp(i m phi),

where each a_{jm},b_{jm} belongs to L2(nu_j;C3), a_{j,-m}=conj(a_{jm}), and b_{j,-m}=conj(b_{jm}). In the remainder write these two functions simply as u and v on shell j. Use the product norm with measure dnu_j dphi/(2pi). Set

A_j = ||u||_j^2 > 0,   B_j = ||v||_j^2 > 0,
c_{jm} = integral_{X_j} a_{jm}(x) dot conj(b_{jm}(x)) dnu_j(x),
q_j = min(A_j,B_j).

Then, for every real gamma,

f_j(gamma) := ||u(x,phi-gamma)-v(x,phi)||_j^2 / q_j
 = (A_j+B_j-2c_{j0}-4 Re sum_{m=1}^M c_{jm} exp(-i m gamma))/q_j.

In particular c_{j0} is real. If the squared symmetric field distance across the shells is F(gamma)=max_{j in J} f_j(gamma), then F is nonnegative, continuous, and 2pi-periodic. The unsquared distance is sqrt(F).

Proof. Expand the squared difference as A_j+B_j minus twice the real inner product. The integral of exp(i(m-n)phi) against dphi/(2pi) is one when m=n and zero otherwise. Thus the inner product equals sum_m c_{jm} exp(-im gamma). Conjugate symmetry pairs the m and -m terms, giving c_{j0}+2 Re sum_{m=1}^M c_{jm} exp(-im gamma). Azimuthal shifts preserve A_j. Dividing by the smaller squared norm gives the larger of the two squared directional distances. A finite maximum of continuous nonnegative periodic functions has the stated properties.

For actual shells a_j<r<b_j, take x=(r,mu), mu=cos(theta), with probability measure 3r^2 dr dmu/[2(b_j^3-a_j^3)]. For a finite meridional quadrature use its positive normalized weights instead. The same proof applies exactly to that discrete measure. It does not prove that this measure approximates the continuum integral.

## 3. A complete finite search with a stated margin

Define

L_j = 4 sum_{m=1}^M m |c_{jm}| / q_j,   L=max_j L_j.

Let P>0 be a common period of all f_j, let K be a positive integer, h=P/K, and gamma_k=k h for 0<=k<K. Define

lower = min_{0<=k<K} max_{j in J} [f_j(gamma_k)-L_j h/2],
upper = min_{0<=k<K} F(gamma_k).

Then

max(0,lower) <= min_{gamma in R} F(gamma) <= upper,

and also lower >= upper-Lh/2. Any further angle evaluation can lower upper without altering the lower bound.

Proof. Differentiate the finite sum in section 2 and bound its absolute value term by term to obtain |f_j'(gamma)|<=L_j. Integrating this bound gives |f_j(s)-f_j(t)|<=L_j|s-t|. Every point of the circle of circumference P lies within circular distance h/2 of a grid point gamma_k. Periodicity then gives f_j(gamma)>=f_j(gamma_k)-L_jh/2 simultaneously for every j. Taking the maximum over j and the minimum over possible k proves the lower bound. Nonnegativity allows replacement by max(0,lower). Evaluation on a subset gives the upper bound. Finally max_j(f_j(gamma_k)-L_jh/2)>=F(gamma_k)-Lh/2, and taking minima proves the last inequality. Compactness of one period supplies the minimum.

When every nonzero frequency m is divisible by a positive integer g, P=2pi/g is a common period. No assertion that this is the smallest period is needed.

## 4. Exact recovery from azimuthal samples

For N>2M and any real offset delta, let phi_k=delta+2pi k/N. The discrete coefficient

(1/N) sum_{k=0}^{N-1} u(x,phi_k) exp(-im phi_k)

equals a_{jm}(x) for |m|<=M. To prove this, substitute the finite series. For each frequency difference n-m between -2M and 2M, the finite geometric sum of exp(2pi i(n-m)k/N) vanishes unless n=m, since the only multiple of N in that interval is zero. The surviving offset factor is one. The same cancellation proves exact azimuthal trapezoidal integration of each squared norm and cross product. Floating-point implementation of this identity remains subject to rounding.

## 5. Representation hypotheses and scope

For the campaign's finite toroidal and poloidal potentials, each spherical harmonic has one azimuthal frequency. The radial envelopes, Chebyshev factors and smooth radial twist multiply its sine/cosine pair by factors independent of phi. Curl in spherical components uses radial and polar derivatives and azimuthal differentiation, with coefficients independent of phi. Starting from the radial vector potential Ty or Sy, one or two curls therefore preserve the finite frequency set. Converting spherical components to cylindrical components mixes only the polar angle. This explains why the stated finite-frequency hypothesis applies to the exact finite representation, including its retained correction channels. The cutoff M is the largest retained azimuthal frequency of all channels, not merely the main degree six.

Dependencies: cylindrical orthonormal frames, the finite Fourier geometric-sum identity proved above, the L2 inner product, and the elementary derivative bound. The shell normalization and symmetric distance agree with ../PROOF.md. Norm-only rotation lower bounds are established separately in ../rotation_norm_bound/PROOF.md.

A floating-point lower value from section 3 is not a rigorous lower bound for the continuum field without bounds on coefficient rounding and meridional quadrature error. An observed rotating-field distance is a diagnostic about two saved fields; it proves neither that either solves Euler nor that two Euler solution branches exist. The campaign's registered comparison uses the saved phase gauges and is not changed by this supplementary minimization.
