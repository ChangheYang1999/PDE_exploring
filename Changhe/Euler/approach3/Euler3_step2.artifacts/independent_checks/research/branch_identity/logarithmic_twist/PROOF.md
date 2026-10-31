# Logarithmic twist, rotation convention, and shell alignment

Status: the statements below are exact mathematical identities under their stated hypotheses. Application to saved fields requires numerical evaluation. They do not establish the Euler equation, a common solution family, or a continuum error bound.

## 1. Linear transport and its sign

Fix c in (0,1) and omega in R, and put alpha=(1-c)/c and k=omega/c. Let J(x,y,z)=(-y,x,0). On r=|y|>0 away from the z axis, write a C1 vector field U in the cylindrical orthonormal frame (e_rho(phi),e_phi(phi),e_z), with component vector u(r,theta,phi). Its linear rotating-profile operator is

L[U]=(1-c)U+c(y dot grad)U-omega((Jy dot grad)U-JU).

Then the cylindrical components of L[U] are

(1-c)u+c r partial_r u-omega partial_phi u.

Consequently L[U]=0 if and only if

u(r,theta,phi)=r^(-alpha) F(theta,phi+k log r)

for a C1 periodic angular component function F. An equivalent formula uses log(r/Rstar) for any fixed Rstar>0, after changing F by a constant angular shift. The characteristics of c y-omega Jy obey d phi/d log r=-k. Their invariant is phi+k log r, not phi-k log r.

Proof. Radial differentiation leaves the cylindrical frame fixed. Azimuthal differentiation differentiates each horizontal frame vector by J, so (Jy dot grad)U-JU has components partial_phi u. This proves the displayed operator identity. Set s=log r and v(s,theta,phi)=exp(alpha s)u(exp(s),theta,phi). The equation becomes partial_s v-k partial_phi v=0. Differentiating v(s,theta,xi-k s) gives zero. It follows that v(s,theta,phi)=F(theta,phi+k s). Substitution proves the converse. The vector c y-omega Jy has dr/dt=c r and d phi/dt=-omega, proving the characteristic sign directly.

The nonlinear Euler momentum equation also contains (U dot grad)U and grad P. Discarding these terms is not an identity for a finite-radius Euler field. This section describes the homogeneous linear equation only.

## 2. Producer coefficient rotation has the opposite active angle

Let Q_gamma be the spatial rotation through gamma about the positive z axis and let T_gamma U(y)=Q_gamma U(Q_(-gamma)y). Its cylindrical components are u(r,theta,phi-gamma), as proved in ../axial_rotation/PROOF.md.

For a real harmonic pair a_c cos(m phi)+a_s sin(m phi), the producer transformation

a_c'=a_c cos(m beta)+a_s sin(m beta),
a_s'=-a_c sin(m beta)+a_s cos(m beta)

equals evaluation of the original pair at phi+beta. This follows by expanding the sine and cosine addition formulas and collecting coefficients. Radial multipliers and curls commute with a constant axial rotation. The same transformation on every toroidal, poloidal and correction pair therefore represents T_(-beta) U. The active angle of the independent Fourier calculation is gamma=-beta, modulo the field's period.

This sign is verified at source level by src/equations/fields.py (cosine sign +1, sine sign -1), src/optimization/problem.py:phase_align, and the lead tools/branch_field_rot.py:rotate. These code statements are separate from the exact trigonometric identity. No assertion about numerical residual accuracy follows from them.

## 3. Exact shell-angle law for homogeneous twisted fields

Let F_a,F_b be nonzero real vector functions in L2(S2;R3), understood as cylindrical components, and let alpha_a,alpha_b,k_a,k_b be real constants. Define, almost everywhere on r>0,

u_a(r,theta,phi)=r^(-alpha_a) F_a(theta,phi+k_a log r),
u_b(r,theta,phi)=r^(-alpha_b) F_b(theta,phi+k_b log r).

For a>0 use the normalized volume norm on a<r<2a. Both norms are positive and finite. Let d_a(gamma) be the larger directional relative L2 distance between T_gamma U_a and U_b. Let C(delta) be the real inner product over 1<t<2, with positive weight t^(2-alpha_a-alpha_b) dt dS, of

F_a(theta,phi+k_a log t-delta) and F_b(theta,phi+k_b log t).

The set of minimizing active angles is exactly

argmin_gamma d_a(gamma)=(k_a-k_b) log a + argmax_delta C(delta)

on the angular circle. In particular, if one maximizer class is unique modulo a common period P and is followed consistently across shells, the active minimizing angle changes by (k_a-k_b) log 2 per doubling of a. The producer minimizing angle changes by -(k_a-k_b) log 2. This law does not require F_a=F_b or small aligned distance.

Proof. Put r=a t and shift the azimuthal integration variable to phi+k_b log a. The cross inner product is a positive constant times

a^(-alpha_a-alpha_b) C(gamma-(k_a-k_b)log a).

The two squared norms scale as a^(-2alpha_a) and a^(-2alpha_b) and are independent of gamma. Their relative-distance denominators are also independent of gamma, by rotation invariance. Minimizing the larger directional distance therefore amounts exactly to maximizing this cross inner product. Translation of its argument proves the set identity. The positive scalar factor does not affect its maximizers. For L2 angular functions, translation is continuous in L2, so C is continuous and periodic and attains a maximum. The increments follow by replacing a by 2a. Multiple maximizers permit different selections; a wrapped angle can also jump by a period. These are not failures of the set identity.

## 4. Conditional asymptotic extension and limits

Suppose a sequence of corrected, centered shell correlations C_j(delta), expressed in the co-moving variable delta=gamma-(k_a-k_b)log a_j, converges uniformly to a continuous P-periodic C. Suppose C has a unique maximum modulo P. Then every choice of maximizer delta_j of C_j converges to that maximum modulo P. For a_j=Rstar 2^j, consistently unwrapped consecutive minimizing active angles consequently have increments tending to (k_a-k_b)log 2.

Proof. For any neighborhood of the maximum, compactness and uniqueness give a positive gap eta between the maximum value and the largest value outside that neighborhood. Once sup|C_j-C|<eta/3, a maximizer of C_j cannot lie outside: its value there would be less than its value at the maximum of C. Thus the maximizing arguments converge modulo P. Their consecutive deviations from the common limiting argument tend to zero, giving the claimed increment after adding the co-moving angle. Uniform convergence, uniqueness and a consistent unwrapping are hypotheses, not automatic consequences of a few computed angles.

This explains why the observed asymptotic increment is a check of the represented radial twist. Since section 3 allows arbitrary angular shapes, agreement with that increment alone cannot show that two fields share a shape or lie on one nonlinear Euler family. Aligned distances supply separate shape/amplitude information. An r-dependent rotation is not one of the constant axial symmetries used in the registered branch rule.

Dependencies: elementary cylindrical differentiation and characteristics; trigonometric addition; the active rotation and L2 norm identities in ../axial_rotation/PROOF.md; continuity of translations in L2 and compactness of the angular circle. There is no formal proof-assistant verification in this campaign.
