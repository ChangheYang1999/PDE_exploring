# Audit of the updated finite-spectrum submission C18

## Exact scope

Let U in C2(R3;R3), P in C1 solve the full rotating profile equation, div U=0, U tending to zero, c>0 and finite omega. Assume its covariant angular support S is finite, nonempty and has L=max S>=1. Proposition 1.1 is read for nonempty symmetric finite S; the empty set satisfies S subset S+S trivially and has no maximum. No finite-spectrum assumption is imposed on the main conjecture.

A137-A140 already verify the support test, pressure support, highest-mode equation and conditional leading-tail compatibility. They also exhibit smooth decaying complex highest-mode steady fields which are not profiles. The current C18 retains those conclusions. The introductory exclusion of L=0 from nonrotating Liouville applies for 0<c<1/2, not for every c>0 in the section's setting.

## The three homogeneous statements

Let Z in C2(R3 minus {0};C3) be homogeneous of complex degree mu, divergence free and of covariant angular character L>=1. Assume globally regular angular data.

Put F=(Z dot grad)Z. It is homogeneous of degree 2mu-1. If curl F=0, then

    partial_i(y dot F)=F_i+y_j partial_i F_j
                        =F_i+y_j partial_j F_i=2mu F_i.

For mu!=0, q=-(y dot F)/(2mu) therefore satisfies F+grad q=0. The potential has degree 2mu and scalar angular character 2L, as claimed. The converse follows by taking curl. This argument uses complex bilinear products, not Hermitian products.

If curl Z=0, choose the angular-character-L scalar potential h. One direct formula, valid also at mu=-1, is

    h=(Z dot Jy)/(iL).

Cartan's formula for the closed one-form Z dot dy and its Lie derivative under rotation gives grad h=Z. It has degree delta=mu+1 and character L; div Z=0 gives Delta h=0. Its spherical restriction g therefore satisfies

    -Delta_S2 g=delta(delta+1)g.

The spectrum of the sphere, restricted to scalar character L, is ell(ell+1) for integers ell>=L. Thus a nonzero field requires delta=ell or delta=-ell-1, equivalently mu=ell-1 or mu=-ell-2. The zero field must be allowed separately. The reverse constructions are gradients of the corresponding solid or exterior spherical harmonics. Their steady pressure is -Z dot Z/2. In particular a nonzero critical tail with Im mu=L omega/c nonzero cannot be irrotational.

Finally suppose curl Z=(kappa/r)Z for a nonzero constant kappa. Taking divergence and using div Z=0 gives Z dot grad(1/r)=0, hence the radial component vanishes. On each sphere the radial curl equation makes the tangential one-form closed, and the divergence equation makes it co-closed. There are no nonzero harmonic one-forms on S2, also after complexification. Therefore Z=0. This excludes only the stated coefficient kappa/r. It does not exclude a variable angular coefficient or a general complex steady field.

## Numerical and formal limits

The spherical-component equations in section 4.1(a) agree term by term with divergence and convective acceleration in spherical coordinates. Their shooting experiments, pole-germ dimension count and analytic continuation are not part of this confirmation. A small numerical residual, even at increasing truncation, is not an existence theorem. Conversely failure to find the target degree is not a nonexistence theorem. The pressure-resonance and higher-order tail discussion remains formal with the qualifications in A139.
