# Independent radial localization of the background Hessian energy

## Exact statement

Let rho be the density of the exact rational candidate C1-N1-007-d2w-j7-e2bal at c=4076476460239181/2251799813685248. For a measurable radial region A set

    E_x(A)=integral_A (rho_xx^2+rho_xy^2),
    E_y(A)=integral_A (rho_yy^2+rho_xy^2),
    K(A)=[(log 2-1/2)E_x(A)+(3 log 2-2)E_y(A)]/(16 pi).

The audited structured Hilbert-Schmidt bound has square K(R^2). The two coefficients are positive. We compute the exact contributions from r<1/50, from 1/50<=r<=R, and from r>R, where R is the exact rational binary64 value of the launch argument 8356.474846731926. These three contributions sum to the whole-plane value. All comparisons refer to the exact rational candidate.

The purpose is to check the independent N4 radial computation and quantify the omitted nonnegative mass. A floating finite-domain value is not promoted to a certificate by its agreement with the exact middle-domain value.

## Independent Cartesian differentiation through polar modes

Put delta=1-1/c, t=r^2/(1+r^2), v=1-t. The independently derived density is

    rho=r sum_(j,n) v^((j+1)delta/2) P_jn(t) sin(n theta).

Define T_(a,k)P=(k-2at)P+2t(1-t)P'. For r^k v^a P times sin(n theta), its x derivative is r^(k-1)v^a times

    (T_(a,k)P-nP) sin((n+1)theta)/2
      +(T_(a,k)P+nP) sin((n-1)theta)/2,

and its y derivative is r^(k-1)v^a times

    (nP-T_(a,k)P) cos((n+1)theta)/2
      +(nP+T_(a,k)P) cos((n-1)theta)/2.

For a cosine input the x derivative has the same two coefficients with cosines. The y derivative has coefficients (T_(a,k)P-nP)/2 at sin(n+1) and -(T_(a,k)P+nP)/2 at sin(n-1). These follow directly from the Cartesian-polar chain rule and angle addition identities. Negative sine modes change sign; negative cosine modes do not. The two contributions to a zero cosine mode are added, not discarded.

Apply these rules first with k=1 and then k=0. Each resulting second derivative is r^-1 v^a Q(t) times a trigonometric mode. Exact divisibility by t is checked component by component. Since r^-1 v^a t=r v^(a+1), this becomes

    D^alpha rho = r sum_(j,n) v^(1+(j+1)delta/2) L_(alpha,j,n)(t) T_n(theta).

Independently computing rho_xy and rho_yx gives an exact polynomial identity check. No integration-by-parts identity is used on a restricted region.

## Complete finite antiderivatives

For each derivative, square all equal-frequency contributions including off-diagonal multiplicity two. Angular orthogonality gives factor pi for a nonzero mode and2pi for the constant cosine mode. The radial Jacobian gives

    r^3 v^(2+(j+k+2)delta/2) dr
       = -(1/2)(1-v)v^((j+k+2)delta/2-1) dv.

Consequently each E_x or E_y is pi/2 times a finite sum of integrals v^e H_e(v), with exact rational polynomials H_e. All j,k are nonnegative and delta>0, so e=(j+k+2)delta/2-1>-1 before any additional endpoint cancellation. Every term is integrable separately. The exterior mass at radius R is

    (pi/2) sum_(e,l) H_(e,l) V^(e+l+1)/(e+l+1),
    V=(1+R^2)^-1.

This is obtained by integrating each monomial from0 toV. At R=0 it is an exact rational times pi/2. Those complete rational energies are compared with the separately verified whole-plane values obtained by integration by parts in T4-111. Thus the pointwise-square and whole-plane-integral methods independently meet in exact rational data.

The origin and middle masses are obtained by subtraction of complete exterior masses. Outward precision must suffice for positive enclosures and the additive identity. Signed polynomial coefficients are all retained. The exact endpoint R and all input hashes are stored with the result.

## Scope and dependencies

The generator and polar field identities are proved in ../new_candidate_witness/PROOF.md. The structured commutator formula was independently audited in T4-016. Whole-plane background data were confirmed in T4-111. The present audit rederives the pointwise second derivatives and regional integrals, then compares with the frozen N4 calculation. It is a numerical and analytic reproduction, not an existence theorem or a replacement for a global signed-matrix certificate.
