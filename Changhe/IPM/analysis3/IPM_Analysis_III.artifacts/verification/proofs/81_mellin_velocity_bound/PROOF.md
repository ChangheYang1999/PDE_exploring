# Exact homogeneous velocity and a regular-cylinder high-frequency bound

## Statement and scope

Use -Delta psi=partial_x h and U[h]=(-partial_y psi,partial_x psi).
For h=r^lambda e^(in theta), n an integer, lambda complex, define

 Aplus=(lambda-n)/(lambda+n+2),
 Aminus=(lambda+n)/(lambda-n+2).

When the displayed denominators are nonzero, a homogeneous particular
velocity is

 Ux[h]=r^lambda/(4i) [Aplus e^(i(n+2)theta)
                              -Aminus e^(i(n-2)theta)],
 Uy[h]=-r^lambda/4 [Aplus e^(i(n+2)theta)+2e^(in theta)
                              +Aminus e^(i(n-2)theta)].        (1)

This is a particular homogeneous solution; it does not independently
specify a canonical global inverse or the harmonic additions at
resonances. The following bound concerns the operator defined by this
Mellin family on the regular cylinder, with unweighted dt dtheta norm.

Fix real sigma. Put lambda=sigma+i xi, p=(xi,n), and replace Aplus and
Aminus in (1) by

 Aplus0=(i xi-n)/(i xi+n),
 Aminus0=(i xi+n)/(i xi-n)

to define U_pr. Let Q_Lambda be the Fourier projection to |p|>=Lambda,
with Lambda>|sigma+2|. Then, with K=max(|sigma+1|,1),

 ||(U_sigma-U_pr)Q_Lambda||_(L2 -> L2(vector))
       <= K/(Lambda-|sigma+2|).                              (2)

In particular the weaker bound with sqrt(2)K in the numerator used in
the theory author's INJ_cap consultation is valid. The improvement in (2) is
an exact cancellation between the two output-component norm squares.
Multiplication by a vector field g to form g.U multiplies the bound
by ||g||_infinity.

## Derivation of the homogeneous solution

Polar differentiation gives

 partial_x(r^lambda e^(in theta))
  =r^(lambda-1)/2 [(lambda-n)e^(i(n+1)theta)
                                  +(lambda+n)e^(i(n-1)theta)],

 Delta(r^mu e^(im theta))=(mu^2-m^2)r^(mu-2)e^(im theta).

Therefore a particular stream function is

 psi=-r^(lambda+1)/2 [e^(i(n+1)theta)/(lambda+n+2)
                              +e^(i(n-1)theta)/(lambda-n+2)].

The cancellation of the factors lambda-n or lambda+n in this formula
is legitimate as a particular solution even when one is zero: that
term is then harmonic and contributes zero to the right-hand side.
The excluded denominators correspond to the genuine resonant formulas.
Using

 partial_y(r^mu e^(im theta))
 =r^(mu-1)/(2i)[(mu-m)e^(i(m+1)theta)
                              -(mu+m)e^(i(m-1)theta)]

and the analogous partial_x identity gives (1), with the stated signs.

## Comparison with the principal family

At p nonzero, exact subtraction gives

 Aplus-Aplus0 =2[(sigma+1)n-i xi]
               /[(sigma+i xi+n+2)(i xi+n)],
 Aminus-Aminus0=-2[(sigma+1)n+i xi]
               /[(sigma+i xi-n+2)(i xi-n)].                   (3)

The numerator modulus is at most2K|p|. By the reverse triangle
inequality, each denominator modulus is at least
|p|(|p|-|sigma+2|). Thus each scalar multiplier difference on the
retained frequencies has operator norm at most

 M=2K/(Lambda-|sigma+2|).

Let Dplus,Dminus be these scalar Fourier multipliers restricted by
Q_Lambda, and let Splus,Sminus multiply by e^(2i theta),e^(-2i theta).
For an input v set a=Splus Dplus v and b=Sminus Dminus v. The difference
of the two velocities has components (a-b)/(4i) and -(a+b)/4.
Consequently the Hilbert-space parallelogram identity gives

 ||(U_sigma-U_pr)Q_Lambda v||^2
  = [||a-b||^2+||a+b||^2]/16
  = [||a||^2+||b||^2]/8
  <= M^2 ||v||^2/4.

Taking square roots proves (2). This argument works on the continuous
radial Fourier line and on any periodic radial frequency lattice.
The shifts need not preserve the high-frequency subspace: they act
after the input projection and are isometries on the full output space.

The principal family can also be checked directly. With
nu_x=(xi cos(theta)-n sin(theta))/|p| and
nu_y=(xi sin(theta)+n cos(theta))/|p|, its two symbols are
nu_x nu_y and -nu_x^2. This agrees with the physical convention and
hence with the coupling symbol g1 nu_x nu_y-g2 nu_x^2.

## Actual radial lines and additional errors

For the remainder weight of proof 76,

 w=|x|^(-17/2)max(1,r)^(29/4),

an exact L2 isometry to cylinder measure is

 (Jh)(t,theta)=exp(-13t/4+(29/8)max(t,0))
                              |cos(theta)|^(-17/4)h(e^t,theta).

Indeed the square of this factor is w times the Jacobian e^(2t).
If only the radial factor is retained, its Mellin lines are sigma=13/4
near0 and sigma=-3/8 near infinity. Formula (2) may be applied to the
regular radial family on either fixed line, with its stated cutoff.
It does not control the singular angular conjugation, the change of
radial line at t=0, cutoffs, Taylor subtraction, harmonic additions,
or jet and normalization terms. Those remain separate bounds for
any actual finite-rank compact-defect certificate.

## Verification dependency

The companion symbolic check verifies (3), the polar stream equations
and the component signs by exact rational symbolic operations. The
norm estimate is the elementary Hilbert-space argument above. No
sampled numerical value is used as a proof and no global inverse
claim is made.
