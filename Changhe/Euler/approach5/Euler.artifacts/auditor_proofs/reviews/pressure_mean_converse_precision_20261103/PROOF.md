# Positive pressure means do not invert the Poisson sign test

## 1. Exact issue

The Theory Agent C note of19:17Z describes the remaining rotating alternative T=tr((DV)^2)<=0 near a common flat point as equivalent to positive means of P on all small spheres. C60 proves the implication from T<=0 to strictly positive means under its full structural hypotheses. It does not prove the converse. The following explicit countertest refutes a converse deduced from the scalar Poisson mean identity alone. It is not a counterexample to the full reduced Euler system.

## 2. Smooth flat scalar countertest

On0<r=|x|<1/2 let F(r)=exp(-1/r^2), e=x3/r and

    P(x)=F(r)(1+2e),  P(0)=0,  T(x)=-Delta P(x).

Every derivative of the punctured formula is a finite sum of a power of r times F times a smooth angular function. Since F decays faster than every power, P and T extend smoothly and flatly through0. Their spherical mean is M(r)=F(r)>0, because the mean of e is zero.

Direct differentiation gives F''+2F'/r=(4r^-6-2r^-4)F and the spherical Laplacian of e is -2e. Thus

    Delta P=F[(4r^-6-2r^-4)(1+2e)-4r^-2 e].

On the positive axis e=1 this is F r^-6(12-6r^2-4r^4)>0 for0<r<1/2, so T<0. On the negative axis e=-1 it is F r^-6(-4+2r^2+4r^4)<0, so T>0. Both signs occur arbitrarily close to0 despite strictly positive means on every small sphere. The identity M'(r)=-(4pi r^2)^-1 integral_(B_r)T still holds; it controls an integral, not the pointwise sign.

## 3. Verdict and the structural boundary

The proposed converse from the Poisson mean identity alone is REFUTED. In the complete C60 local class, a converse is OPEN unless an additional argument is supplied. The countertest does not provide V, does not impose T=tr((DV)^2), and does not vanish on a full orbit arc. None of the confirmed C60 theorem parts A2127-A2132 is contradicted.

The note should say that T<=0 implies positive means, and that the T<=0 alternative remains open. Positive means form the only mean-trichotomy case in which the theorem does not itself force positive values of T nearby; this does not identify that case with T<=0. No new computation or external input is needed.
