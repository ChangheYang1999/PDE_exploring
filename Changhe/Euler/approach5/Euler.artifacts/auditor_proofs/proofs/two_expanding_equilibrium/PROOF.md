# A vortical Euler equilibrium with two expanding backward directions

## Exact statement

Let 0<c<1/2, a=1-2c, kappa=1+c, and let omega be any nonzero finite real number. Choose 0<epsilon<a/2 and put L=a-epsilon. There is a smooth affine velocity U and quadratic pressure P on R3 solving

    div U=0,
    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0,
    J(x1,x2,x3)=(-x2,x1,0),

whose carrier B=(cI-omega J)y+U has an equilibrium at0 with nonzero actual vorticity Omega=curl U. The backward carrier derivative there has Lyapunov exponents

    L, epsilon, -kappa.

For the Dirac invariant probability at0, entropy is0. For each finite r>1, one can choose epsilon so that

    0 >= epsilon-(L-epsilon)/(r-1).

Thus this particular finite-regularity entropy lower bound is compatible with an atomic vortical equilibrium and a selected positive exponent that is not the largest. The example does not decay and has no positive-volume trapped basin. It is a local compatibility test, not a counterexample to any existence or coverage theorem.

## Construction and verification

Let

    D=diag(-L-c,-epsilon-c,1),
    E=diag(-L,-epsilon,kappa),
    U(y)=Dy+omega Jy, B(y)=Ey.

The identity L+epsilon=a makes trace D=0 and trace E=3c. Thus div U=0 and the carrier has the desired form. Its vorticity is the constant vector Omega=2omega e3, which is nonzero. Since E e3=kappa e3,

    [B,Omega]=-E Omega=-kappa Omega.

This is the actual vorticity, not an independent field.

The non-pressure part of the profile equation is the linear vector field S y with

    S=D(I+D)+omega J(I+2D)+omega^2 J^2.

To check this expression, insert DU=D+omega J, B=Ey and E=D+cI into (1-c)U+DU B+omega JU. The diagonal terms combine into D(I+D), and the terms linear in omega combine into omega J(I+2D). The matrix S is symmetric: D1+D2=-1, so the two off-diagonal entries of J(I+2D) both equal epsilon-L. The remaining two matrices are diagonal. Set P(y)=-(1/2)y.Sy. Then grad P=-Sy, and the profile equation holds globally. All derivatives and the single-valued pressure are explicit.

The backward flow is Psi_t(y)=(exp(Lt)y1,exp(epsilon t)y2,exp(-kappa t)y3), so its exponents at0 are exactly those stated. Their sum is -3c, consistent with volume contraction. The time-one map fixes0; the Dirac probability has entropy0. There is no zero flow exponent at an equilibrium. Using a zero flow exponent there would be the precise spectral error.

## The finite-r entropy comparison

For the projective direction e2 the selected exponent is epsilon and the largest exponent is L. The indicated defect expression is

    epsilon-(L-epsilon)/(r-1)
       =((r+1)epsilon-a)/(r-1).

Taking epsilon=a/(2(r+1)) puts it strictly below zero. The entropy0 atom is therefore not excluded by that inequality at the chosen finite r. This observation does not show that an actual empirical-measure construction places mass on the atom. For a fixed epsilon the inequality would become positive for sufficiently large r; the example does not establish an obstruction uniform as r tends to infinity.

## Relevance to the older curve-entropy source

The manuscript arXiv:2111.06651v2, Section5.3, excludes a second positive selected exponent using a surface-specific fact about invariant measures with two positive exponents. That step does not transfer to a three-dimensional flow equilibrium. Its geometric-time lower bound is tau_p=log(10)/p, with p selected after r in Proposition5. Merely increasing r does not, without further estimates, give an r-independent positive selected exponent for the resulting measures. These source facts are recorded as limitations of the proposed adaptation, not flaws in the surface theorem.

A regular ergodic three-dimensional flow component of negative constant divergence has a zero flow exponent; if one exponent is positive, there is exactly one positive exponent. Its selected positive exponent is therefore the largest, and this particular defect vanishes. The equilibrium component needs a separate argument. In the conditional LIT41 construction, an arclength-absolutely-continuous mixture of nonconstant exponentially incoming curves gives zero mass to equilibria directly. Obtaining that mixture is precisely one of the premises under audit.

## Scope and dependencies

The velocity grows linearly, so it violates the prompt's uniform decay and the compact backward trapping used elsewhere. For omega=0 the same formula is an irrotational exact profile, but its actual vorticity vanishes. No assertion about the full older-source construction in dimension3 is made. The proof is direct matrix algebra and exact linear flow; no numerical or formal computation is used.
