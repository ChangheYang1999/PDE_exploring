# Smooth angular matching for noninteger local indicial modes

Status: CONFIRMED by independent derivation, checked Opus 5.5 review 07, and 24 exact rational differentiation tests with nonzero negative controls. Date: 2026-10-20.

## Exact statement

Fix A>1, a0 real, and a noninteger real degree d>1. Let eta=r^d Theta(theta), where Theta is a real C-infinity function on the circle, with eta even in x and odd in y. Define chi to be the unique function homogeneous of degree d+1, smooth off zero and odd in both coordinates, satisfying

    -Delta chi=eta_x.

Uniqueness follows from the absence of noninteger-degree smooth angular harmonic functions. Then the local homogeneous linearization

    (A x partial_x+y partial_y-1)eta+a0 chi_x=0         (1)

has a nonzero solution if and only if there are nonnegative integers m,n with

    d=(2m+1)A-2m,
    a0=(A-1)[(2m+1)A+2n+3].                          (2)

For fixed A,a0,d the real solution space is one-dimensional when (2) holds and zero otherwise. The pair (A,d) determines m, and a0 then determines n. The noninteger-degree restriction means (2m+1)A is not an integer. In particular there are no modes in this class if A is an integer. Every mode has d>=A and a0>0. An explicit spanning function is

    eta=partial_x^(2m) partial_y^(2n+1) r^s,
    s=d+2m+2n+1.

It has a finite angular Fourier expansion. The equation and classification are local homogeneous statements. A nonzero term with noninteger d cannot belong to a smooth Taylor expansion at zero. This theorem does not claim that such a term occurs in any nonlinear profile, nor that its absence selects c_l.

## Fourier transform facts used

Use the tempered-distribution transform with kernel exp(-i X.xi). A homogeneous distribution of degree d has transform of degree -d-2. A homogeneous distribution which is smooth off zero has Fourier transform smooth off zero. The latter regularity statement is Corollary 3.2.6 and its concluding paragraph on page 141 of Carlos Lemoine, *Fourier transforms of homogeneous distribution*, Annali della Scuola Normale Superiore di Pisa, series 3, volume 26 (1972), pages 117-149.

A smooth function homogeneous of degree lambda off zero has a unique homogeneous distributional extension if lambda is not -2,-3,... . See R. T. Seeley, *Homogeneous Distributions*, report TW 88, Mathematisch Centrum (1962), Corollary 2 following Theorem 1, pages 9-10. The source metadata and precise use are recorded in sources/SOURCES.json. The uniqueness can also be seen directly: a distribution supported at zero is a finite sum of derivatives of the Dirac distribution, of degrees -2-j.

Only these structural Fourier facts are taken from the references. The transport calculation, endpoint matching, parameter relations and explicit spanning functions below are independently derived.

## Equation away from the Fourier origin

Since d>1, eta and chi are locally integrable and have polynomial growth. Their homogeneous extensions are ordinary functions at zero. The smooth angular Poisson equation is invertible: in even sine modes its eigenvalues are (d+1)^2-k^2, none of which vanish for noninteger d. In particular chi exists and is smooth off zero. The distributional Poisson equation holds on the whole plane. There is no point-supported defect, either by homogeneity or by vanishing of the small-circle boundary terms for these positive degrees.

Write Fourier coordinates as (xi,zeta), and F=hat eta. On the punctured Fourier plane,

    hat chi=i xi F/(xi^2+zeta^2),
    hat chi_x=-xi^2 F/(xi^2+zeta^2).

Also the transform of A x eta_x+y eta_y-eta is

    -[A xi partial_xi+zeta partial_zeta+A+2]F.

Therefore (1) implies

    (A xi partial_xi+zeta partial_zeta)F
      =-[A+2+a0 xi^2/(xi^2+zeta^2)]F.                (3)

By the Fourier regularity theorem, F is a smooth function on the punctured plane, homogeneous of degree -d-2. In the open quadrant xi,zeta>0 write

    F(xi,zeta)=zeta^(-d-2) f(xi/zeta).

Substitution into (3), with q=xi/zeta, gives

    (A-1)q f'=[d-A-a0 q^2/(1+q^2)]f.

Every nonzero solution on this quadrant is a constant times

    q^mu (1+q^2)^(-a0/(2(A-1))),
    mu=(d-A)/(A-1).

In the original Fourier coordinates it is

    F=C xi^mu zeta^nu (xi^2+zeta^2)^(-a0/(2(A-1))),
    nu=(a0+2-A(d+1))/(A-1).                         (4)

The powers add to total degree -d-2, as required.

## Matching at both Fourier axes

The density parities make F even in xi and odd in zeta. Reality of eta makes F purely imaginary. If the quadrant constant in (4) were zero, the same parities would make F zero on every open quadrant. Its smoothness off zero then makes it zero everywhere off zero. Such an F is supported at zero, so eta is a polynomial. A nonzero polynomial cannot have noninteger homogeneous degree. Thus the quadrant constant is nonzero.

Near xi=0 at any fixed zeta>0, the radial factor in (4) is smooth, even and strictly nonzero. Smooth even extension of the remaining power |xi|^mu is possible exactly when mu is an even nonnegative integer, say mu=2m. Near zeta=0 at any fixed xi>0, odd matching similarly requires sign(zeta)|zeta|^nu to be smooth, which occurs exactly when nu is an odd positive integer, say nu=2n+1. Negative powers are unbounded; noninteger powers lose a finite derivative; integers of the wrong parity also lose smoothness on the reflected axis.

Solving these two equations gives exactly (2). The constants on all quadrants are determined by parity, and any additional point-supported part is forbidden by the noninteger homogeneous degree -d-2. Thus the dimension is at most one.

## Construction and sufficiency

Suppose (2) holds. On the punctured Fourier plane choose

    F=i xi^(2m) zeta^(2n+1) (xi^2+zeta^2)^(-a0/(2(A-1))).

This is nonzero, smooth off zero, has the required parities, and is homogeneous of noninteger degree -d-2. Its unique homogeneous distributional extension exists. Let eta be its inverse transform. The inverse Fourier transform is the forward transform composed with reflection, up to a constant, so the same Fourier regularity theorem gives smoothness off zero. Homogeneity gives eta=r^d Theta with smooth Theta; since d>-2, this locally integrable function is the unique homogeneous extension. Its imaginary and parity properties give real eta, even in x and odd in y.

Define chi by the homogeneous angular Poisson inverse. Equation (3) holds pointwise off the Fourier origin. Both x partial_x and y partial_y commute with isotropic dilations, so the left side of (1) is homogeneous of degree d despite the anisotropic transport coefficients. Its Fourier transform is consequently supported at zero and has homogeneous degree -d-2. Since this degree is noninteger, that distribution must be zero. This proves (1) on the whole plane and establishes sufficiency without an arbitrary product of singular distributions at the Fourier origin.

For the explicit expression, s=a0/(A-1)-2=d+2m+2n+1 is noninteger. The Fourier transform of r^s is a nonzero constant times the homogeneous extension of |xi|^(-s-2), by the same homogeneous transform formula (Seeley, equation (13), page 8). Differentiating 2m times in x and 2n+1 times in y produces (4), up to a nonzero imaginary constant. Multiplication of the radial homogeneous extension by the corresponding polynomial agrees with the homogeneous extension of the product, by uniqueness at its noninteger resulting degree. Thus the stated eta spans the solution space. Its angular expansion is finite because finitely many derivatives of a radial power give a finite polynomial in direction cosines times a radial power.

A corresponding stream function is explicitly

    chi=-partial_x^(2m+1) partial_y^(2n+1) r^(s+2)/(s+2)^2,

since Delta r^(s+2)=(s+2)^2 r^s in two dimensions.

## Lowest example and limits of the result

For m=n=0 the conditions are d=A and a0=(A-1)(A+3). Up to a constant,

    eta=y r^(A-1),   chi=-x y r^(A-1)/(A+3).

Direct differentiation gives -Delta chi=eta_x and

    (D-1)eta=(A-1)y r^(A-3)(A x^2+y^2),
    chi_x=-y r^(A-3)(A x^2+y^2)/(A+3),

which cancel under the stated a0 relation. This is a useful independent sign check.

The classification does not include integer d, where polynomial terms and frequency-origin distributions matter. It does not include angular functions with only finite regularity, where noninteger axis powers in (4) are permitted as distributions. It does not apply the canonical sublinear full-plane inverse to a global superlinear density. In a cutoff local perturbation, smooth harmonic jets generated by the exterior still require separate treatment as explained in ../indicial/PROOF.md.

## Verification evidence

The independent script independent_code/check_indicial_fourier.py differentiates monomials with rational powers using exact fractions, then expands to a common radial power. It verifies both equations for 24 choices of rational A and (m,n), and verifies that changing a0 by 1 makes the transport defect nonzero. Results are in verification/exact_examples.json. The actual model, timings and review are saved in evidence/opus_review_07/. The theorem is confined to the stated even-x, odd-y parity class.
