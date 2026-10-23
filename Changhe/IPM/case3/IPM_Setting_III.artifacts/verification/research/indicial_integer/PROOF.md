# The integer-degree distinction in smooth angular local modes

Status: CONFIRMED after independent derivation, exact rational tests of 18 even-degree examples, and a completed Opus 5.5 review. Date: 2026-10-20.

Verification: ../../evidence/opus_review_09/answer.md and verification/exact_examples.json. The actual returned model was claude-opus-5-5. Its clarifications were checked and incorporated below.

## Statement

Use the local linearized system and parities in ../indicial_fourier/PROOF.md, with A>1 and a0 real:

    (A x partial_x+y partial_y-1)eta+a0 chi_x=0,
    -Delta chi=eta_x.

Assume eta and chi are smooth on the punctured plane, homogeneous of degrees d and d+1, respectively, and have the required even-x/odd-y and odd-x/odd-y parities. Here d>1 can be an integer. The equations initially hold on the punctured plane. They also hold as tempered distributions on the full plane: eta and chi are locally integrable homogeneous functions, and any equation defect supported at zero would have degree d or d-1, both greater than -2, whereas a nonzero distribution supported at zero has degree at most -2. The assumption A>1 permits division by A-1 below. Then:

1. If d is not an odd integer, nonzero eta occurs precisely at the lattice

       d=(2m+1)A-2m,
       a0=(A-1)[(2m+1)A+2n+3],  m,n nonnegative integers.

   The real solution space has dimension one. This includes even integer d. Such even-degree eta is not a polynomial at zero and is not smooth there.
2. If d is an odd integer, eta and chi are homogeneous polynomials. This statement does not classify their polynomial solution space or fix the harmonic datum of chi. The fixed-harmonic resonance matrices in ../indicial/PROOF.md remain the separate polynomial problem.

No logarithmic or polyhomogeneous perturbation is classified here. A homogeneous chi is an explicit hypothesis. No nonlinear full-plane conclusion follows.

## Fourier argument for necessity

The Fourier transform F of eta is smooth off zero by the homogeneous Fourier regularity theorem recorded in ../indicial_fourier/PROOF.md. For every real d>1 the same punctured-frequency calculation gives, in each open quadrant,

    F=C xi^mu zeta^nu (xi^2+zeta^2)^(-a0/(2(A-1))),
    mu=(d-A)/(A-1),
    nu=(a0+2-A(d+1))/(A-1).

If F is nonzero on one quadrant, parity and smooth angular matching force mu and nu to be nonnegative integers with mu=2m and nu=2n+1, which give the lattice. If F is zero on the quadrants, its smoothness off zero makes it supported at zero; consequently eta is a polynomial. A nonzero homogeneous polynomial with eta's parities has odd integer degree.

For odd integer d, a nonzero quadrant constant is in fact impossible. To see this, let T be any homogeneous distribution of degree -d-2 with the indicated smooth off-zero value F. Write E=xi partial_xi+zeta partial_zeta. Homogeneity and distributional integration by parts imply

    <T,(E-d)phi>=0

for every compactly supported smooth test function phi. Choose

    phi(xi,zeta)=P_d(xi,zeta) q(r),
    P_d=zeta (xi^2+zeta^2)^((d-1)/2),

where q is a smooth radial cutoff, equal to one near zero and zero for sufficiently large r. Since d is odd, P_d is a homogeneous polynomial of degree d, so phi is a legitimate test function. Then (E-d)phi=P_d r q'(r), supported away from zero. Evaluating the ordinary integral there gives

    0=[integral_0^infinity q'(r) dr]
        integral_0^(2pi) F(cos theta,sin theta) P_d(cos theta,sin theta) dtheta.

The first factor is -1. On the unit circle the second factor is

    C integral_0^(2pi) cos^(2m)(theta) sin^(2n+2)(theta) dtheta,

which is nonzero for C nonzero. This contradiction is independent of any choice of extension at the frequency origin. Thus F vanishes off zero and eta is polynomial. A polynomial Poisson particular solution of degree d+1 exists; subtracting it from chi leaves a smooth angular homogeneous harmonic function of degree d+1, which is a harmonic polynomial. Hence chi is polynomial too.

## Existence and uniqueness off odd integer degrees

If d is not an odd integer, the homogeneous angular Poisson inverse in chi's parity class has no kernel: chi uses only even sine frequencies, and resonance would require d+1 to be an even integer. The matching calculation therefore bounds the solution space by one dimension, provided a nonzero eta is not polynomial, as already shown.

On the lattice set s=d+2m+2n+1 and define

    eta=partial_x^(2m) partial_y^(2n+1) r^s,
    chi=-partial_x^(2m+1) partial_y^(2n+1) r^(s+2)/(s+2)^2.

Here s is not an even nonnegative integer. The Fourier transform of r^s has a finite nonzero homogeneous radial coefficient, so the formula is nonzero and its punctured transform is the matched F above. It satisfies the Poisson equation by direct differentiation. Its transport defect has Fourier support at zero, so that defect is a homogeneous polynomial of degree d. Such a polynomial is absent if d is noninteger, and excluded by even-x/odd-y parity if d is an even integer. Therefore the defect vanishes. This proves sufficiency also at even integer d without asserting uniqueness of homogeneous distribution extensions in an exceptional degree without a parity condition.

At even integer d, eta cannot be polynomial for the same parity reason. It is smooth off zero but has finite regularity at zero. In particular, a lattice point whose d is an odd integer carries no nonpolynomial mode. At odd integer d, a harmonic stream-function datum is available and was deliberately not eliminated in this statement.
