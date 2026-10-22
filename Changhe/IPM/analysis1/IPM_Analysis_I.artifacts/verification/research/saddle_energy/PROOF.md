# The isotropic saddle energy symbol and its limited implication

Date: 2026-10-20. Status: CONFIRMED for the stated frozen model. The independent exact/Arb/iv scalar calculation passed, and actual Opus 5.5 accepted the source derivation at17:45:34 UTC. Evidence/verdict.json records the executed source and result hashes. This note addresses V9 and the local saddle part of V5. It does not audit the lead's sampled variable-coefficient energy maps or orbit integrals.

## Exact homogeneous energy identity

Let c_l>1, A=2c_l-1>1, D=4c_l-1=2A+1, and

T_0=-A x partial_x+D y partial_y-1.

For real s, work first with Schwartz functions whose Fourier transforms have compact support away from zero. Write xi=(xi_1,xi_2), B=diag(-A,D), and use the unitary Fourier convention. For the homogeneous Sobolev inner product with weight w(xi)=|xi|^(2s),

Re <T_0 f,f>_(dot H^s)=integral S_s(xi)|xi|^(2s)|fhat(xi)|^2 dxi,
S_s(xi)=s[-A xi_1^2+D xi_2^2]/|xi|^2-(1+c_l).

Indeed, Fourier transformation gives

(T_0 f)^hat=-(B^T xi) dot grad_xi fhat-(tr B+1)fhat.

Taking the real part and integrating by parts produces

(1/2)div_xi(w B^T xi)-(tr B+1)w
=[-1-(tr B)/2+s(xi dot B^T xi)/|xi|^2]w.

Here tr B=D-A=2c_l. There are no boundary terms because fhat has compact support away from zero. This proves the exact identity. It extends to any graph-domain element for which the core approximation and the pairing converge, but no such extension is needed for the negative and positive test functions below.

For the inhomogeneous H^s norm, the same calculation with w=(1+|xi|^2)^s gives

S_s^inh(xi)=s[-A xi_1^2+D xi_2^2]/(1+|xi|^2)-(1+c_l).

Therefore the homogeneous expression is the high-frequency angular limit of the inhomogeneous expression; the two are not equal at finite frequency. In particular the value requested in V9 is

S_s(0,1)=sD-(1+c_l),
S_s(1,0)=-sA-(1+c_l).

These are the maximum and minimum over the unit circle, respectively.

## Positive and negative tests

If s>3 and c_l>1, then

S_s(0,1)>3(4c_l-1)-(1+c_l)=11c_l-4>0,
S_s(1,0)<0.

Continuity supplies open angular cones about the vertical and horizontal directions with strict respective signs. Nonzero smooth Fourier functions supported in those cones make the exact dot H^s quadratic form positive or negative. The supports can avoid both axes and be reflected across them. Choose the Fourier amplitude imaginary, even in xi_1 and odd in xi_2; its inverse Fourier transform is real, even in x and odd in y. The reflected cones have the same energy signs. Hence the parity requirement does not restore a sign for this frozen model. For H^s, dilate the Fourier supports to sufficiently large frequency, where the sign approaches the same nonzero limits.

At the nonlinear origin, the factorization rho=x^2 y a with a continuous and rho in C^1 implies grad rho(0)=0. The local leading symbol of U[h] dot grad rho therefore vanishes at the origin. This does not remove the nonlocal scalar strain term or prove that the frozen model captures a particular full operator realization. The verified center normalization in ../local_geometry/PROOF.md is the dependency identifying A and D with c_l for an exact profile or the exactly normalized modal trial.

For a smooth positive scalar spatial weight exp(phi), the transport integration by parts contributes -(1/2)V dot grad phi to the principal energy symbol. At a fixed point with V=0 this contribution is zero. Thus such a finite smooth scalar weight alone does not change these limiting signs at the saddle. This statement concerns the displayed energy pairing, not general pseudodifferential symmetrizers, singular weights or a global resolvent.

## What the sign calculation does not prove

This calculation refutes a positive coercive lower bound Re <T_0 f,f> >= a||f||^2 with a>0 in this pairing, and also a negative one Re <T_0 f,f> <= -a||f||^2. It does not by itself refute an estimate ||f||<=C||T_0 f|| or prove any kernel, cokernel or nonclosed range. The elementary bounded operator diag(1,-1) on R^2 has both energy signs, yet is its own bounded inverse with norm1. Therefore indefiniteness alone cannot justify the general inference that every isotropic inverse estimate fails in either direction. Any such conclusion for this differential operator needs a separate domain and spectral argument.

In particular this result is not a NO endpoint for an IPM profile neighborhood. The lead's sampled variable-coefficient symbol values, orbit costs and their implications remain outside this audit.

## Exact input and numerical verification

The local scalar calculation uses k=1615536043799051/9007199254740992, c_l=1/k, and s=13/4. This k is the exact normalized modal-trial exponent parameter, already audited in ../modal_repair/PROOF.md. All quantities A,D,S_y,S_x are rational. An exact Fraction calculation is compared to an independent direct-k calculation with mpmath.iv and to Arb256. Both interval implementations must contain the exact rational value. This verifies arithmetic and the connection to the pinned input; the all-s>3 sign theorem above is analytic.
