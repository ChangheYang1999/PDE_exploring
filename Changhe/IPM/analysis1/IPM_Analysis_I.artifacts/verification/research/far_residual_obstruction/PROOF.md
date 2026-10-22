# The modal trial has no stationary correction in unweighted L2

Status: independent informal proof before a new coefficient certificate.
This is a scoped obstruction in an affine unweighted class. It is not a
decisive NO about a meaningful weighted uncertainty neighborhood of X3.

## 1. Objects and claim

Let rho0 be the exact normalized 260-mode trial of modal_repair/PROOF.md,
with 0<k<1/2, c0=1/k and its canonical sublinear velocity U0. Set
beta=2k-1 in (-1,0). Let R=exp(tplus), where tplus is the exact final
logarithmic knot. All stored coefficients have their exact dyadic meaning;
the scalar normalization z has the exact real definition in that proof.

The finite exterior representation and its canonical Green inverse imply,
uniformly in angle and with the indicated radial derivative,

 rho0=r^k Theta(theta)+O(r^beta),
 E rho0=k r^k Theta(theta)+O(r^beta),
 |grad rho0|=O(r^(k-1)), |U0|=O(r^k),
 epsilon0=(c0 X+U0).grad rho0-rho0
         =r^beta Epsilon(theta)+o(r^beta).                         (1)

Here E=X.grad. Both angular functions are finite trigonometric
polynomials, and Theta is nonzero. Let e0 be the coefficient of
sin(theta) in the coefficient of exp(beta tau) in epsilon0, with
tau=log(r/R). A fresh two-engine computation will verify

 -0.0002000282880 < e0 < -0.0002000282879.                          (2)

Its physical homogeneous coefficient is E0=R^(-beta)e0, so E0!=0 and
Epsilon is not zero. An inconclusive calculation would leave this
numerical premise open. No value is invented to close the proof.

Subject to that finite coefficient check, there is no stationary full-plane
canonical profile rho=rho0+h with h in L2(R2), the specified parities and
sublinear canonical velocity, for any finite real scaling c. In particular
no finite unweighted Hs correction, s>=0, can produce an admissible exact
profile. This is stronger than a small-radius exclusion in that affine
class, but does not give an exclusion in a topology permitting tail changes.
The statement is about actual stationary profiles having meaningful local
products, in particular the task's P2 or stronger classes. It does not
assert regularity of every arbitrary L2 perturbation.

## 2. Reconstructing the leading residual coefficient

Write the factor's first two outer cosine rows as A_m0+z delta_m0 and
A_m1, m=0,...,259. Define d_j and b_j by the exact finite sine projections

 cos(theta)^2 sin(theta) sum_m (A_m0+z delta_m0) cos(2m theta)
       =sum_(j=0)^260 d_j sin((2j+1)theta),
 cos(theta)^2 sin(theta) sum_m A_m1 cos(2m theta)
       =sum_(j=0)^260 b_j sin((2j+1)theta).                         (3)

This follows from cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4
and the sine-cosine product identities. Define d_261=0, a=k+1, m=2n and

 F_n=((a-m)d_(n-1)+(a+m)d_n)/2,
 v_n=-m F_n/(m^2-a^2), w_n=a F_n/(m^2-a^2), 1<=n<=261.            (4)

To derive (4), apply partial_x=cos(theta)partial_r-
(sin(theta)/r)partial_theta to r^k sum d_j sin((2j+1)theta).
Its sin(2n theta) source has coefficient F_n r^(k-1). Since
-Delta[r^(k+1)sin(m theta)]=(m^2-(k+1)^2)r^(k-1)sin(m theta),
the particular stream coefficient is F_n/(m^2-a^2). In polar coordinates
U_r=-psi_theta/r and U_theta=psi_r, yielding (4). The denominators are
strictly positive because m>=2 and 1<a<3/2. The R factors below restore
the original exterior coordinate normalization.

The residual coefficient at exp(beta tau) is exactly

 R^3(beta/k-1) sum_j b_j sin((2j+1)theta)
 +R^5[(sum_n v_n cos(2n theta))(sum_j k d_j sin((2j+1)theta))
      +(sum_n w_n sin(2n theta))(sum_j (2j+1)d_j cos((2j+1)theta))].  (5)

The first density power k cancels from the linear part because c0 k=1.
The next power is beta; every other density exponent is strictly smaller.
A particular velocity-density product has exponent beta_i+beta_j-1,
which equals beta only for i=j=0. Canonical homogeneous transient products
have exponents at most k-4<beta. Logarithmic join corrections are strictly
smaller powers. There are finitely many terms, proving the last limit in
(1) uniformly. The other limits follow directly from the same finite
representations, including the angularly differentiated formulas.

Only j=n or j=n-1 can contribute frequency one in (5). Thus

 e0=R^3(beta/k-1)b_0
   +(R^5/2)sum_(n=1)^261
      {k v_n(d_n-d_(n-1))
       +w_n[(2n-1)d_(n-1)-(2n+1)d_n]}.                            (6)

Equivalently, the summand including its factor 1/2 is

 F_n/{2(m^2-a^2)}
   { [m(2k+1)-a]d_(n-1)-[m(2k+1)+a]d_n }.                       (7)

The first method will evaluate this quadratic expression as an exact
rational polynomial in z, then use Arb for the exact-real bracket and
radial exponentials. A second method will form the sine projections by
Laurent multiplication of cos(theta), cos(theta), sin(theta) and the raw
cosine series, then use mpmath.iv and (4),(6). This avoids importing the
first projection or quadratic coefficients. It also compares (2) with the
prior full 522-frequency convolution and independent direct-product audit
in outer_leading_cancellation. Every printed bound must hold separately.

## 3. Identifying the canonical velocity of an L2 difference

Suppose rho is a hypothetical admissible stationary profile with
h=rho-rho0 in L2. Its Fourier velocity is the L2 multiplier

 uhat=(xi1 xi2,-xi1^2)/|xi|^2 hhat,

with any definition at xi=0, a set of measure zero. Its squared multiplier
norm is xi1^2/|xi|^2<=1. Hence u is in L2, ||u||2<=||h||2,
div u=0 and curl u=-partial_x h, distributionally. It has the same
velocity parities as the difference of the two canonical velocities.

Let W=U[rho]-U0-u. Its divergence and curl vanish, so each component is
harmonic in distributions. The sublinear growth of the two canonical
velocities and u in L2 give ||W||_{L2(B_R(x))}=o(R^2) for each fixed x.
This conclusion does not assume the Fourier velocity decays pointwise.
Mollify W by a compactly supported radial smooth approximate identity.
The mollified field is smooth harmonic, preserves parities, and has the
same large-ball o(R^2) estimate, by the local convolution L2 inequality.
For a smooth harmonic function H and a radial smooth averaging kernel
eta_R supported in B_R with integral one, the mean-value property gives
H(x)=integral H(y)eta_R(y-x)dy. Differentiation and Cauchy-Schwarz give

 |grad H(x)|<=||H||_{L2(B_R(x))} ||grad eta_R||2
             =C R^(-2)||H||_{L2(B_R(x))}.

Let R tend to infinity. Every mollified component is constant; its odd
coordinate parity forces the constant to be zero. Passing to the
approximate-identity limit yields W=0 in distributions. Thus the actual
canonical velocity difference is exactly u, with no harmonic strain.

## 4. Annular weak tests exclude every L2 correction

Write delta=c-c0 and V_delta=(c0+delta)X+U0. Subtract the trial equation
from the hypothetical stationary equation. In distributions this is

 0=epsilon0+delta E rho0+V_delta.grad h-h
                 +u.grad rho0+div(h u).                           (8)

The last form uses div u=0. It is meaningful because h u is in L1 by
Cauchy-Schwarz; no derivative of h is assumed or estimated.

Fix phi smooth with compact support in 1<|Y|<2 and set
phi_R(X)=R^(-1)phi(X/R), with annulus A_R={R<|X|<2R}. Then
||phi_R||2=||phi||2, ||grad phi_R||2=R^(-1)||grad phi||2 and
||grad phi_R||infinity=R^(-2)||grad phi||infinity. Also
|V_delta|<=C_delta R on A_R and div V_delta=2(c0+delta).
Integration by parts therefore bounds all h-dependent terms of (8) by

 C_(phi,delta)||h||_{L2(A_R)}
 +C_phi R^(k-1)||u||_{L2(A_R)}
 +C_phi R^(-2)||h||_{L2(A_R)}||u||_{L2(A_R)}=o(1).                 (9)

The second term uses |grad rho0|<=C R^(k-1). Both L2 annular norms tend
to zero. This controls arbitrarily oscillatory corrections without any
assumed pointwise tail expansion for h or its derivatives.

For any continuous angular A and fixed exponent q, uniform angular
asymptotics r^q A+o(r^q) imply

 <r^q A+o(r^q),phi_R>
  =R^(q+1) integral |Y|^q A(arg Y)phi(Y)dY+o(R^(q+1)).             (10)

Choose a nonnegative nonzero smooth radial g supported in (1,2) and first
take phi(Y)=g(|Y|)Theta(arg Y). The coefficient of delta R^(k+1) in
(8),(10) is k integral_1^2 g(s)s^(k+1)ds integral Theta^2 dtheta>0.
All residual terms are O(R^(beta+1)), with beta<k, and (9) is o(1).
Dividing by R^(k+1) and taking the limit forces delta=0.

Now take phi(Y)=g(|Y|)sin(arg Y). Orthogonality of the finite sine modes
and E0!=0 give

 <epsilon0,phi_R>
   =pi E0 R^(beta+1) integral_1^2 g(s)s^(beta+1)ds
                   +o(R^(beta+1)).                              (11)

Since beta+1=2k>0, this grows in magnitude. It cannot equal the negative
of the o(1) terms in (9). This contradiction proves the claim in Section1.

The same nonzero angular coefficient and the uniform limit imply
 epsilon0 in L2(R2,(1+r^2)^(-gamma)dX) iff gamma>2k.                (12)
For divergence choose an angular interval on which Epsilon stays nonzero
and integrate r^(2beta+1-2gamma); equality gives logarithmic divergence.
For convergence use the O(r^beta) far bound and local boundedness of the
trial residual. Near zero the exact trial density is C2 with bounded
canonical velocity; away from zero its finite pieces and joins are C6.
Thus epsilon0 itself is not in unweighted L2 despite tending to zero.

## 5. Why this is not a decisive branch exclusion

The affine class rho0+L2 fixes every non-L2 tail direction. Topic103 shows
that even X3 is outside this class. More generally, let chi be smooth,
zero near zero and one for sufficiently large r. For any nonzero eta,

 h_eta=eta chi(r)r^beta cos(theta)^2 sin(theta)

is not in L2, since beta+1=2k>0. It preserves parity and the local center
normalization. Its weighted factor norm from modal_repair tends to zero
linearly with |eta|: divide h_eta by x^2y and then by
W=(1+(r/L)^2)^((k-3)/2); at infinity the ratio is O(|eta|r^(k-1)).
It is bounded on the intervening compact annulus. Hence arbitrarily
small admissible tail perturbations in that topology leave the affine
L2 class. The obstruction does not exclude a neighborhood permitting
such corrections. In particular, no meaningful numerical-uncertainty
ball about X3 is claimed contained in the excluded class. Global
invertibility in an appropriate weighted realization and all decisive
endpoints remain open.
