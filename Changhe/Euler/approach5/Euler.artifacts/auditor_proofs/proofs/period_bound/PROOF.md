# A sharp period lower bound for the similarity flow

## Statement

Suppose c is real with c!=1/2, omega is finite, and a C^2 divergence-free U with a C^1 single-valued pressure solves the rotating profile equation on a neighborhood of a nonconstant periodic orbit Y of B=(cI-omega J)y+U. If Y'=B(Y) and T>0 is a period, then omega is nonzero and T>=2pi/|omega|. Equality implies a horizontal circle, possibly with displaced center, parametrized with angular velocity -omega.

This is LIT09. Only local H0 near the orbit is required. No far-field hypothesis, symmetry or vorticity condition is used.

## Proof

The exact Kelvin law on a closed material curve says its U circulation multiplies by exp((2c-1)s). The periodic orbit is unchanged as an oriented curve by every sufficiently small flow time. Its circulation is therefore zero, since 2c-1 is nonzero. Substituting U(Y)=Y'-cY+omega JY and integrating the derivative of |Y|^2 gives

\[
 E+\omega A=0,\quad
 E=\int_0^T|Y'|^2>0,\quad
 A=\int_0^T JY\cdot Y'.                                \tag{1}
\]

Thus omega cannot be zero. Put Z=Y-average(Y). Then integral JY dot Y'=integral JZ dot Z'. The periodic Wirtinger inequality and Cauchy-Schwarz give

\[
 |A|\le\|JZ\|_2\|Z'\|_2
 \le\|Z\|_2\|Z'\|_2
 \le \frac{T}{2\pi}\|Z'\|_2^2
 =\frac{T}{2\pi}E.
\]

Equation (1) proves the lower bound after division by E. If equality holds, Z has no vertical component, consists only of first Fourier harmonics, and Z'=kJZ for a constant real k. Nonconstancy gives k!=0. Equation (1) becomes k(k+omega) integral|Z|^2=0, hence k=-omega. The radius of Z is constant and nonzero, so the orbit is the stated circle.

## Sharpness and scope

The exact affine profile U=(-cx,-cy,2cz), P=(c-c^2)(x^2+y^2)/2-(c+2c^2)z^2 has B=-omega Jy+3cz e_z. Its circles at z=0 attain the lower bound for every nonzero omega. It grows linearly and is not a decaying counterexample. At c=1/2 the circulation no longer forces (1), so that value is explicitly excluded.
