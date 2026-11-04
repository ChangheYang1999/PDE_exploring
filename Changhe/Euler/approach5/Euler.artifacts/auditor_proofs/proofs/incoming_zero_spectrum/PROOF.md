# Spectrum of a vortical zero approached from a compact vortical set

## Statement

Let 0<c<1/2, omega finite, and let U in C2, P in C1 solve the full rotating profile equation near a compact full B-invariant set K, where B=(cI-omega J)y+U and Omega=curl U. Assume Omega is nowhere zero on K. If p in K is a zero of B and some x in K with B(x)!=0 satisfies Phi_-t x->p as t->infinity, then

    spec DB(p)={1+c,lambda_2,lambda_3},
    lambda_3<0<=lambda_2,    lambda_2+lambda_3=2c-1.   (1)

In particular the eigenvalues are real. This confirms the spectral assertion B19. It does not imply lambda_2<1+c and does not establish an attracting set.

## Proof

A130 gives two elementary facts. First, no regular point of K has B parallel to Omega: if Omega(x)=lambda B(x), Cauchy transport gives Omega(Phi_s x)=lambda exp(-(1+c)s)B(Phi_s x), contradicting the positive lower bound of |Omega| on K as s->infinity. Second, the vortex line through p satisfies

    B(gamma(tau))=(1+c)tau Omega(gamma(tau)),

and therefore meets K only at p.

The curl equation at p gives DB(p)Omega(p)=(1+c)Omega(p). The other two eigenvalues have sum 2c-1<0. Suppose both had negative real parts. Then p would be a hyperbolic equilibrium of the backward flow with a one-dimensional stable eigenspace R Omega(p). The local vortex line is invariant and contracts to p in backward time, since its parameter is multiplied by exp(-(1+c)t). Uniqueness in the hyperbolic stable-manifold theorem makes it the local stable manifold. Every point converging to p in backward time eventually lies on this local curve. Applied to x, invariance of K contradicts the preceding nonintersection property.

Thus at least one of the other eigenvalues has nonnegative real part. A nonreal conjugate pair would have both real parts equal to (2c-1)/2<0, so the pair is real. Label its nonnegative member lambda_2; its other member is lambda_3=2c-1-lambda_2<0. This proves (1).

## Zero-eigenvalue qualification

No stable-manifold dimension formula at a nonhyperbolic equilibrium was used. If lambda_2=0, one may place a sufficiently late converging orbit in a local two-dimensional center-stable manifold for the backward flow. The actual set of converging points need not itself be that whole manifold, and should not be identified with it merely by counting center directions. The original draft's casual dimension statement requires this qualification.

The last sentence that such an equilibrium can occur in K only via forward-converging orbits is not needed for (1). A separate accumulation argument, recorded in the non-Lorenz proposal, is required before speaking about arbitrary accumulation rather than convergence.
