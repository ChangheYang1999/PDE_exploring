# Two rigid subclasses of complex homogeneous fields

## Statements

Let Z be C1 on R3 minus the origin with values in C3, with globally C1 angular data and homogeneity Z(tx)=t^mu Z(x) for real t>0. Products in differential equations are complex bilinear. Then:

1. If div Z=curl Z=0 and -2<Re mu<-1, then Z=0.
2. If div Z=0, Re mu<0 and Z=Fv for one fixed nonzero v in C3, then Z=0.
3. If Z(R_theta x)=exp(i L theta)R_theta Z(x) for a nonzero integer L, and Z(rn)=r^mu[v(n)+f(n)n] with v tangent to the sphere, then integral f^2=integral v.v=0 on S2. Thus the bilinear homogeneous Beltrami integral identity has no positivity content for this single mode.

These confirm LIT31. They do not exclude a variable-direction, nonzero-curl complex steady field, nor a full Fourier mode whose leading coefficient vanishes.

## Irrotational case

Set h=(x.Z)/(mu+1). The denominator is nonzero. Symmetry of DZ and Euler's homogeneity identity give grad h=Z, hence Delta h=0. Its degree is delta=mu+1. If g=h restricted to S2, then

    -Delta_S2 g=delta(delta+1)g.

Multiply by conjugate(g), integrate and take real parts. Writing delta=A+i B, with -1<A<0,

    integral |grad_S2 g|^2
       =[A(A+1)-B^2] integral |g|^2.

The coefficient is negative, so g=0 and Z=0. All integrations are justified by h in C2. The Hermitian pairing is valid here because this is a linear harmonic equation.

## Fixed complex direction

Write v=A+i B for real vectors A,B. The bound |F(x)|<=C|x|^(Re mu) follows from homogeneity and bounded angular data.

If A,B are dependent, v is a nonzero complex scalar times a real vector w. The divergence condition is w.grad F=0. On each line parallel to w avoiding the origin, F is constant and tends to zero at either infinite end, so it vanishes. Continuity covers the remaining line away from the origin.

If A,B are independent, choose a real N completing them to a basis and write x=sA+tB+zN. Directional differentiation gives

    partial_s F+i partial_t F=0.

For each fixed z!=0 the affine plane avoids the origin; F is an entire holomorphic function of s+i t. The displayed bound makes it bounded and tending to zero at infinity. The complex Liouville theorem gives F=0 there. Continuity covers z=0 away from the origin. The argument does not use v.v and includes null complex directions.

## Bilinear angular cancellation

The transformation rules are f(R_theta n)=exp(i L theta)f(n) and v(R_theta n)=exp(i L theta)R_theta v(n). Each square in statement 3 therefore has angular character 2L. Invariance of sphere area implies I=exp(2i L theta)I for every theta, hence I=0.

For completeness the formal real Beltrami identity extends bilinearly as follows. Write alpha=-mu and U=r^-alpha(v+fn). Divergence gives div_S v=(alpha-2)f. The Beltrami condition U cross curl U=0 makes the full Bernoulli function constant. For nonzero homogeneity it can be gauged to zero, giving the homogeneous pressure p=-(f^2+v.v)/2. The radial momentum equation becomes

    v.grad_S f+(alpha-1)v.v=0.

Integrating by parts yields

    (2-alpha) integral f^2=(1-alpha) integral v.v.

For real 1<alpha<2 the two coefficients have opposite signs and real squares are nonnegative. For complex nonzero angular character both integrals are zero. Replacing these bilinear squares by absolute squares is a different identity and is not licensed by this calculation.

## Half-space example and scope

On x3>0, Z=x3^mu(e1+i e2) has zero divergence and (Z.grad)Z=0, with angular character one. For Re mu<0 it diverges at the equator x3=0 away from the origin. It cannot give globally C1 angular data. The natural leading exponent mu=1-1/c+i L omega/c has real part in (-3/2,-1) when 2/5<c<1/2, so statement 1 applies, but only when irrotationality is separately known.
