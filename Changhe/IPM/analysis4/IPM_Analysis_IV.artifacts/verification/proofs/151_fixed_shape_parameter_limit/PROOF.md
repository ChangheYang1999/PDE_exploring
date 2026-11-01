# The fixed-shape irrational family can be singular at a tuned rational profile

Status: PROVED finite-order fixed-shape pole obstruction. Both nonzero residues are certified in V293; the theory part independently rederived the analytic limit and residue at11:34Z, recorded in V299.

## Statement and notation

Let delta0=2/3, c0=3, and fix one exact real root b of the sextic compatibility polynomial in119. Hold the leading shape f_1=sin(theta)+b sin(3theta) fixed while varying delta. At every nonresonant delta, define f_n(delta),g_n(delta) by the unique pure Fourier recurrence with no free harmonics. Let H6_star be the free sin(2theta) stream coefficient selected by the compatible tuned solution at delta0. Write a_1(delta) and a_3(delta) for the sin(theta) and sin(3theta) coefficients of f_6(delta).

All orders preceding6 are analytic in delta near delta0. Since a_1(delta0)=0, the apparent singularity in the sin(2theta) coefficient of g_6 is removable. Its limiting value is

    H6_lim = a_1'(delta0)/12 + a_3(delta0)/8.                (1)

Let sigma_2 be the nonzero response from H6 to the next obstruction, the sin(3theta) coefficient of f_9. If H6_lim differs from H6_star, then the sin(4theta) coefficient of g_9(delta) has a nonzero simple pole at delta0, with residue

    Res = sigma_2(H6_lim-H6_star)/18.                       (2)

Consequently the fixed-shape nonresonant coefficients do not converge coefficientwise to the tuned rational coefficients. This does not contradict convergence at each fixed admissible irrational parameter or at the tuned rational parameter. It excludes uniform coefficientwise continuity across that rational parameter for this fixed shape.

## Proof

The only positive stream resonance at or below6 is order6, frequency2. Every earlier coefficient is therefore analytic by the finite rational recurrence. The relevant Fourier coefficient is

    g_(6,2)(delta) = [(P_6-2)a_1+(P_6+2)a_3]
                       /[2(4-P_6^2)],
    P_6=2-6delta.

At delta0, P_6=-2 and a_1=0. Differentiating numerator and denominator gives -4a_1'-6a_3 and -48, respectively. The denominator has a simple zero, so analytic division gives(1). Every other coefficient at order6 is analytic there. Hence f_7,g_7,f_8,g_8,f_9 also have finite analytic continuations to delta0.

At that limit all preceding coefficients agree with the delta0 recurrence using H6=H6_lim. The next obstruction is affine in H6. It vanishes at H6_star and has slope sigma_2, so its value is sigma_2(H6_lim-H6_star). For order9 and frequency4, the numerator at delta0 is -8 times this obstruction. The derivative of the denominator2(16-P_9^2) is -144. A nonzero obstruction therefore produces the simple-pole residue in(2).

To certify the nonzero comparison, compute the finite recurrence and its delta derivative by interval automatic differentiation, with an exact isolating interval for b. This encloses a_1'(delta0), a_3(delta0) and H6_lim. Independently compute H6_star and sigma_2 by the two-continuation Cartesian construction. A residue interval separated from zero proves the stated conclusion for that exact root.

## Scope and dependencies

The exact root and first compatibility identity are119. The tuned series exists by the independently proved theorem119. This argument concerns a finite coefficient and a fixed leading shape. It makes no claim that suitably varying the leading profile cannot regularize the limit, nor does it imply divergence at any fixed irrational delta.

## Certified values

The1024-bit Cartesian derivative calculation finished at2026-10-31T11:27:41Z in0.3171247891150415 actual seconds. For the smaller root, H6_lim=1.1662746920385938e-7 and H6_star=1.3068216859598592e-6, while the pole residue is positive and enclosed by[1.8474368363007068551148226575027306241701978353944461732328272927e-11 +/-3.97e-76]. For the larger root, H6_lim=-1.6977871809304368e-5 and H6_star=7.3903733314084222e-5, while the residue is enclosed by[-5.2286526585704989273983171140004163832285725966030495278754920939e-8 +/-2.49e-73].

Every density coefficient through6 overlaps the separate tuned Cartesian implementation. Replacing its order6 harmonic by H6_lim and recomputing orders7 through9 reproduces the affine obstruction formula for each root. The exact root intervals, derivative values and full residue intervals are in verification/checks.json.
