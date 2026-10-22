# Finite stagnation samples and the whole-plane inverse

## Exact statement

Fix beta>0 and a finite set S of nonzero points in R^2. There is a smooth compactly supported x-odd stream function psi, with support disjoint from S, its x-reflection and the vertical axis, such that U=(-psi_y,psi_x), Omega=-Delta psi and W=beta X+U satisfy all of the following. The velocity U is the ordinary whole-plane inverse of Omega. It has U(0)=0, vanishes near S and outside a compact set, and W has an off-axis hyperbolic saddle p and its reflection. Thus q=|W|/(beta|X|)=1 and W.X/(beta|X|^2)=1 at every sample in S, while W has off-grid zeros and local separatrices. This is an inverse/kinematic example, not a B2 solution.

More generally, a smooth compact x-odd perturbation of the stream function can preserve a prescribed smooth x-symmetric transport field and all its derivatives near any finite S and the origin, preserve its far-field tail, and insert a saddle at a chosen off-axis p outside those neighborhoods. This requires the base field to have div W=2 beta and the B2 x-reflection parity. It says nothing about preservation of the nonlinear profile equations away from the samples.

## Proof

Choose p=(a,b), a>0, outside the finite reflected sample set and away from the axis. Choose rho>0 so the closed disks B(p,rho) and its reflection are disjoint from each other, the axis and the sample set. Let chi be a C-infinity cutoff supported in B(p,rho) and equal to1 near p. Given d>0, write xi=x-a, eta=y-b and

    P(x,y)=-beta b xi+beta a eta+(beta+d)xi eta,
    phi=chi P,
    psi(x,y)=phi(x,y)-phi(-x,y).

The reflected summand vanishes near p. There psi_x(p)=-beta b, psi_y(p)=beta a, psi_xx(p)=psi_yy(p)=0 and psi_xy(p)=beta+d. Consequently U(p)=-beta p and

    D W(p)=diag(-d,2 beta+d).

The eigenvalues are nonzero and have opposite signs. The smooth stable-manifold theorem gives local stable and unstable curves through p, tangent respectively to e1 and e2. Reflection gives a second saddle. Compact support and the parity formula give every stated sample, center and far-field property. The divergence of U is zero, so div W=2 beta everywhere.

To verify that this velocity is produced by the inverse rather than an appended harmonic field, let E(X)=-(2pi)^(-1)log|X|, so -Delta E=delta. For compact smooth psi, distributional integration by parts gives E*(-Delta psi)=(-Delta E)*psi=psi. Equivalently, move the two derivatives from psi onto E in the compact-support pairing; no boundary term at infinity occurs. Thus the ordinary logarithmic convolution of Omega=-Delta psi equals psi exactly, and differentiating produces U. This also fixes the decaying-velocity gauge. The perturbation source is compact x-odd and has zero integral.

For the general assertion let J=[[0,-1],[1,0]], so U=J grad psi. At p let M=D W_0(p), tr M=2 beta. Prescribe the perturbation velocity jet delta U(p)=-W_0(p) and derivative B=diag(-d,2 beta+d)-M. Since tr B=0, the matrix H=-J B is symmetric. A quadratic polynomial with gradient -J delta U(p) and Hessian H has exactly the required jet. Multiply by chi and antisymmetrize as above. Then W_0+delta U has the desired zero and saddle derivative. Supports avoid all preserved neighborhoods and all large radii. Its inverse correction is the ordinary inverse of -Delta(delta psi) by the same convolution argument. If the base field is required to belong to a particular canonical inverse class, this assertion additionally assumes that inverse is linear on the base source plus compact perturbations and agrees, in its relative-center gauge, with the ordinary inverse on this compact correction. The chosen disks must lie outside the preserved neighborhoods, so their complement must contain p and a small disk. No arbitrarily small perturbation norm or prescribed finite-dimensional basis is asserted.

## Application and limits of numerical evidence

A grid search with positive W.X and no sampled small q proves those sampled facts, subject to evaluation error. The statement alone cannot exclude an unsampled zero or a separatrix. The construction above obeys the divergence, parity, relative-center and full-plane inverse constraints, and can preserve any finite list of sampled jets of a base field. It does not satisfy the temperature and vorticity equations merely because those kinematic constraints hold. To exclude hidden zeros for a specific stored field one needs further quantitative control, for example a certified interpolation/derivative bound on a covering and separate origin and far-field arguments. No such bound is supplied by a positive sampled minimum alone.

If W has an isolated hyperbolic source at0 with diagonal derivative diag(beta-c,beta+c), its horizontal-ray small-radius q limit is |beta-c|/beta. For the stored states with0<c<beta this is (beta-c)/beta. That limit does not force the minimum over a finite annular grid to occur at the origin or on that ray.

Dependencies: elementary compact-support distribution calculus and the local stable-manifold theorem. The source and inverse construction are fully justified above; the theorem on stable curves is used only for the separatrix statement, not for existence of the explicitly constructed zeros. No formal proof, B2 candidate, or global exclusion is claimed.
