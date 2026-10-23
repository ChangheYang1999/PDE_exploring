# A positive first-moment endpoint for the one-sided defect

Date: 2026-10-20. Independent reconstruction of the first-moment argument in the lead's QLE1 source, Section2. This is a conditional necessary condition, not a nonexistence theorem for the unrestricted primary class.

## Exact statement and notation

Let ell>1, D=ell-1 and A=2ell-1. Suppose rho is an exact smooth primary profile on R2:

    W.grad rho=rho, W=ell X+U, U=(-psi_y,psi_x), -Delta psi=rho_x.

The density is even in x and odd in y, has a=rho_y(0)!=0, and obeys the sublinear density and gradient growth bound in PROMPT.md. The stream is odd in both coordinates, and its inverse is canonical, U=o(r), r=|X|. The origin relation is psi_xy(0)=-D. Define

    H=y-rho/a, phi=psi+Dxy, v=(-phi_y,phi_x), V=v2,
    W=(Ax,y)+v, B=X.W/r^2.

Assume in addition yH>=0 everywhere. This is q=rho/(ay)<=1, including the smooth extension to y=0. It is not an established property of the unrestricted class. By ../one_sided_flat_exclusion/PROOF.md, H is not flat. Let n>=3 be its first nonzero Taylor degree. Parity makes n odd. Write H_n for the homogeneous degree-n part and

    C_n=int_S1 H_n(omega) omega_y dtheta,
    T_n=(int_S1 omega_x^2 H_n(omega) omega_y dtheta)/C_n.

Then C_n>0, 0<T_n<1, and

    [a-(n-1)(A-1)]*((n+3)T_n-1)=(n-1)^2.             (1)

Consequently either

    a<(n-1)(A-n),

or

    a>(n-1)(A-1)+(n-1)^2/(n+2).                      (2)

Both inequalities are strict. They are necessary conditions only. The first alternative can contain positive a when A>n; neither alternative may be silently discarded.

For every real m with 2<m<(n+3)/2, the following integrals converge absolutely:

    I_m=int_R2 H y r^(-2m),   J_m=int_R2 V y r^(-2m).

Moreover I_m>0, and

    J_m=a/[2(m-2)]*int_R2 H y r^(-2m)*(2m*x^2/r^2-1),             (3)
    J_m=2m*int_R2 H y B r^(-2m)-(2ell+1)I_m
          -int_R2 H W2 r^(-2m).                                  (4)

All statements are invariant under the genuine spatial dilation. H and V scale as lambda times their values at X/lambda; I_m,J_m scale as lambda^(4-2m). The ratio T_n is unchanged because H_n scales as lambda^(1-n). No normalization of a or ell is used.

## Local equations and convergence

Substituting rho=a(y-H) and the origin linear velocity into transport gives

    W.grad H=H+V,    Delta phi=a H_x,    Delta V=a H_xx.            (5)

Smoothness and parity give v=O(r^3) initially. Since H=H_n+O(r^(n+2)), equation(5) gives

    V=(Ax*d_x+y*d_y-1)H_n+O(r^(n+2))=O(r^n).

At infinity H=O(r) and V=U2+Dy=O(r). Also W=O(r), and B is bounded both at zero and infinity. These estimates prove absolute convergence of every integral in(3)-(4): the radial majorants are r^(n+2-2m) near zero and r^(3-2m) at infinity. The first is integrable exactly when m<(n+3)/2, and the second when m>2. There is no assumption of a global bound on higher derivatives of U.

The function yH is nonnegative and nonzero, so I_m>0. Dividing yH(r omega)>=0 by r^(n+1) and taking r to zero gives omega_y H_n(omega)>=0. It is not identically zero, since H_n is a nonzero polynomial. It is positive on an open arc. Therefore C_n>0. Multiplication by omega_x^2, or by1-omega_x^2, preserves strict positivity on some subarc; the isolated axes cannot support a nonzero continuous function. Thus 0<T_n<1.

## The inverse moment, including both boundary terms

Set

    F_m=y*r^(2-2m)/[4(m-1)(m-2)].

Away from zero, direct differentiation gives

    Delta F_m=y*r^(-2m),
    (F_m)_xx=y*r^(-2m)*(2m*x^2/r^2-1)/[2(m-2)].

Use the distribution identity Delta V=a H_xx from(5) with the compactly supported test F_m chi_(epsilon,R), where the cutoff is1 on2epsilon<r<R and0 onr<epsilon orr>2R, and its first and second derivatives have the usual inverse-radius bounds. Integrating derivatives onto the test is legitimate because V,H are locally smooth and the test avoids the origin. The errors containing a derivative of the cutoff are bounded by

    C epsilon^(n+3-2m) + C R^(4-2m).

This follows using only H,V=O(r^n) at zero and O(r) at infinity, together with F_m homogeneous of degree3-2m. Both exponents have the required sign in the stated m interval. Let epsilon decrease to zero and R increase to infinity. Absolute convergence of the non-error terms yields(3). Thus no unproved decay of grad V and no hidden harmonic boundary contribution enter this interchange.

For(4), multiply W.grad H=H+V by y*r^(-2m) and use the same cutoffs. Since div W=2ell,

    div(W*y*r^(-2m))=2ell*y*r^(-2m)+W2*r^(-2m)
                    -2m*y*B*r^(-2m).

The cutoff error has the same endpoint bounds as above: H=O(r^n), W=O(r) near zero and both O(r) at infinity. Passing to the limit and rearranging proves(4), with the additional -I_m accounted for by the right-hand H in transport.

## Passing to the first local divergence

Put delta=n+3-2m and let m increase to(n+3)/2. On a fixed small disk, insert the homogeneous expansion of H and the uniform angular Taylor remainder. Integrating the leading radial power gives

    delta*I_m -> C_n,
    delta*int H y*(x^2/r^2)*r^(-2m) -> C_n T_n.

The terms outside the small disk remain bounded uniformly for m sufficiently close to the endpoint, because the endpoint is strictly larger than2. The remainder inside is integrable uniformly, since its radial power has two additional degrees. The same reasoning applies to the other integrals, using

    B=1+(A-1)omega_x^2+O(r^2),    W2=y+O(r^3).

Consequently(3) gives

    lim J_m/I_m = a/(n-1)*((n+3)T_n-1),

whereas(4) gives

    lim J_m/I_m = n-A+(n+3)(A-1)T_n.

Equating these and rearranging gives(1).

Let z=(n+3)T_n-1, so -1<z<n+2, and lambda=a-(n-1)(A-1). Equation(1) says lambda*z=(n-1)^2>0. If lambda<0, then z<0 and z>-1 force lambda<-(n-1)^2, which is the first alternative in(2). If lambda>0, then z>0 and z<n+2 force lambda>(n-1)^2/(n+2), which is the second. lambda=0 is impossible. This proves the strict dichotomy.

## Scope and independent algebra check

The only imported nontrivial result is the nonflatness theorem under yH>=0; alternatively the statement can explicitly assume a finite first degree n and dispense with that dependency. The canonical inverse enters through the true origin relation and U=o(r), not through an adjustable harmonic strain. The argument is a positive first moment, distinct from the previously audited squared weighted norms.

The accompanying exact checker differentiates the test function, verifies the endpoint algebra, and checks(1) against independently generated homogeneous leading equations for many rational A,a and odd degrees. Such checks support the proof but do not replace the cutoff argument. No numerical candidate is proved to satisfy the extra sign hypothesis.

## Direct leading-equation identity, without a sign hypothesis

Added 2026-10-20 after the lead's request to audit the scope. The identity can be proved locally without taking a global moment limit. Let n>=3, A>1, and let H_n,V_n be homogeneous polynomials of degree n with

    V_n=(A x partial_x+y partial_y-1)H_n,
    Delta V_n=a partial_xx H_n.

Write H(theta)=H_n(cos(theta),sin(theta)), C=int H sin(theta), and M=int H cos(theta)^2 sin(theta), with integrals over one full circle. No sign is imposed. In the polar frame the first equation is

    V_n=[n-1+n(A-1)cos(theta)^2]H
                         -(A-1)cos(theta)sin(theta)H'.

Since (cos(theta)sin(theta)^2)'=3cos(theta)^2 sin(theta)-sin(theta), integration by parts on the circle gives

    int V_n sin(theta)=(n-A)C+(n+3)(A-1)M.                  (14)

For a homogeneous function of degree n, the polar Laplacian is r^(n-2)(n^2 H+H''). Thus

    int (Delta V_n)|_(r=1) sin(theta)=(n^2-1)int V_n sin(theta).

Also

    (partial_xx H_n)|_(r=1)
      =n[(n-1)cos(theta)^2+sin(theta)^2]H
        -2(n-1)cos(theta)sin(theta)H'+sin(theta)^2 H''.

Twice integrating by parts, and using (sin(theta)^3)''=9cos(theta)^2 sin(theta)-3sin(theta), gives

    int (partial_xx H_n)|_(r=1) sin(theta)
                       =(n+1)[(n+3)M-C].

The Poisson equation therefore implies

    (n-1)int V_n sin(theta)=a[(n+3)M-C].                   (15)

Combining (14)-(15) proves the undivided identity

    [a-(n-1)(A-1)]((n+3)M-C)=(n-1)^2 C.                  (16)

It holds even when C=0. When C is nonzero, dividing by C gives the identity with T=M/C in the main theorem. Positivity enters only to obtain C>0 and 0<T<1. The global cutoff argument is still needed to justify the exact-profile moment identities away from the origin; it adds no further coefficient to this local relation.

For n=3, write H_3=B x^2 y+E y^3. Then C=pi(B+3E)/4 and M=pi(B+E)/8. Equation (16) reduces exactly to 6E=(a-2A)B. This is (T1) after H=-h/a. The divided version is equivalent on C!=0; the undivided version also covers C=0.

For the lead's n=7,A=10 example, the prior sign recurrence gives a>=24 and (a-24)(a-42)(a-60)>=0, hence a in[24,42] union[60,infinity). The new strict dichotomy is a<18 or a>58. Its intersection with the prior necessary set is[60,infinity), proving the stated improvement for that degree and that A. This is still a necessary condition in the one-sided subclass.
