# A non-profile passing centered-ball energy, torque and helicity tests

## Statement

Fix 2/5<c<1/2 and finite omega. Put p=1/c-1 in (1,3/2), alpha=3-2p and kappa=p-1. There exist real smooth fields U,P on R3, with div U=0, U zero near zero and U tending to zero at infinity, having all the properties below.

The pressure is the canonical L2 Poisson pressure of U. For every R>=1 the energy is exactly E(R)=8pi R^alpha/(3alpha), and the full centered-ball energy, vertical angular-momentum and helicity flux identities of the rotating profile equation hold with that same pressure. The helicity identity holds at every radius. The derivative is O(r^-2); helicity is integrable, nonzero and sign-changing with zero total integral; the frozen curl flow is complete, volume preserving and conservative, with the natural polynomial radius bound. The angular support is exactly {-1,0,1}.

Nevertheless the velocity is not a profile for any pressure. Its annular rescalings have a nonzero weak homogeneous limit with strictly less energy and cannot converge strongly. This confirms the substantive LIT29 screen, with its last residual coefficient corrected below.

## Construction and exact radial moments

Choose smooth chi equal to zero on r<=1/4 and one on r>=1/2, with 0<=chi<=1. Choose a nonnegative nonzero smooth eta supported in (1/8,1/4). Set

    A0=r^-p chi,
    M^2=(1/alpha-integral_0^1 r^2 A0^2 dr)
           /(integral_0^1 r^2 eta^2 dr),
    A=A0+M eta.

The numerator is positive since integral_0^1 r^(2-2p)dr=1/alpha. The two summands are disjoint on the support of eta. Thus A is zero near zero, is r^-p for r>=1, and integral_0^1 r^2 A^2 dr=1/alpha.

Choose nonnegative nonzero smooth xi supported where eta>0, and define

    K0=integral_0^1 r^3 A xi dr>0,
    D=1/(4-p)-integral_0^1 r^3 A dr.

Choose d>0 with d(1+|D| ||xi||_infinity/K0)<1/2, and put

    zeta=d[1+(D/K0)xi],    phi=r^kappa,
    a=(sqrt(1-zeta^2)cos phi,sqrt(1-zeta^2)sin phi,zeta),
    U(y)=A(r) a(r) cross n,    n=y/r.

Set U(0)=0. This is smooth because it is identically zero near zero; the fractional radial powers cause no singularity there. The unit vector a has vertical component d outside a compact set, and

    integral_0^1 r^3 A zeta dr=d/(4-p).                (1)

## Curl, derivative and pressure

Direct differentiation gives

    div U=0,
    Omega=(A'+A/r)a+A a'
       -[(A'-A/r)(a.n)+A(a'.n)]n,
    Omega.n=2A(a.n)/r,
    h=U.Omega=-A^2 n.(a cross a').                    (2)

These formulas can be obtained by writing U=(A/r)a cross y and differentiating each factor. The radial derivative part in div U contracts with a vector perpendicular to y. The two dot identities follow from |a|=1 and a.a'=0.

Since |a'|=sqrt(1-d^2) kappa r^(kappa-1) outside the unit ball, (2) gives |DU|=O(r^-2). The spherical integral of |a cross n|^q is a positive constant independent of a. Thus U is in Lq precisely when pq>3, and its exact energy follows from the chosen A moment.

Each U_i U_j is in L2 because 4p>3. Define P=sum R_i R_j(U_i U_j), using the Fourier multipliers of the Riesz transforms. L2 boundedness gives P in L2, and

    -Delta P=partial_i partial_j(U_i U_j)
            =partial_i U_j partial_j U_i.

The right side is smooth locally, so local elliptic regularity gives a smooth representative of P. A harmonic L2 difference must vanish, which gives uniqueness in this normalization. U is odd under y->-y, so P and q=|U|^2/2 are even, Omega is even and h is odd.

## Three centered-ball flux identities

Both U and Jy are tangent to spheres, and B=(cI-omega J)y+U has B.n=cR on S_R. Hence

    integral_S_R (Bq+PU).n=(cR/2) E'(R)
      =(5c/2-1)E(R), R>=1,                           (3)

because c alpha=5c-2. There is no hidden pressure flux: U.n=0 pointwise.

For M_z=(Jy).U, the product identity gives

    M_z=rA[a_z-(a.n)n_z],
    integral_S_R M_z=(8pi/3)R^3 A(R)zeta(R).

By (1), integral_B_R M_z=8pi d R^(4-p)/(3(4-p)) for R>=1. Since c(4-p)=5c-1,

    integral_S_R (B.n)M_z=(5c-1)integral_B_R M_z.     (4)

The integrated pressure torque is zero: partial_theta P=div(P Jy), and Jy is tangent to S_R. Thus (4) retains the complete pressure term of the ball identity.

Finally the helicity identity is

    integral_S_R [Bh-(q-P)Omega].n
        =(4c-2)integral_B_R h.                       (5)

Every term is zero at every positive radius: h is odd, B.n=cR is even, and (q-P) is even while Omega.n is odd. All three identities therefore use the same canonical pressure; none is an assertion about arbitrary domains or translated balls.

## Frozen flow, helicity and weak limit

If Omega=0 at an exterior point, (2) first gives a.n=0 and then a.Omega=A'+A/r=(1-p)r^-p-1, a contradiction. Its radial speed is at most 2r^-p-1. Consequently the derivative of (1+r^2)^((p+2)/2) along Omega is globally bounded. This proper-function bound proves complete flow and radius growth at most C_K(1+|t|)^(1/(p+2)) for compact initial sets.

The flow preserves volume. For any fixed nonzero time step a positive-volume wandering set has a bounded positive-volume subset. Its first N disjoint images would fit into a ball of volume O(N^(3/(p+2))), which is sublinear in N because p>1. This contradicts volume preservation. Applying this to last-return subsets of a countable basis gives recurrence in both directions for almost every point.

Write s=sqrt(1-d^2). Outside the unit ball |a cross a'|=s kappa r^(kappa-1). The sphere integral of |h| is 2pi s kappa r^-p and is integrable in r. Its spherical mean is zero, while it takes both signs. Thus h is in L1 and has total integral zero.

On a fixed annulus the rescaled velocity is

    R^p U(Ry)=|y|^-p[s cos(R^kappa |y|^kappa),
                      s sin(R^kappa |y|^kappa),d] cross n.

Radial integration by parts against smooth test functions makes the oscillatory part O(R^-kappa). Uniform L2 bounds extend this to weak L2 convergence. The weak limit is d|y|^-p e_z cross n. If K_ann is the squared norm of the full field on the annulus, the limit has norm squared d^2 K_ann; the squared norm of the difference is exactly (1-d^2)K_ann. Thus strong convergence fails. The vertical part gives m=0 and the nonzero horizontal part gives m=plus/minus one in the cylindrical frame.

## Corrected exact residual

At r_j=(2pi j)^(1/kappa) on the positive z axis, put C=A'+A/r. Then

    U=-As e_y,
    Omega=Cs e_x+As phi' e_y+(2Ad/r)e_z.

The e_x component of (U.grad)Omega is zero. The e_x component of (Omega.grad)U, however, has TWO contributions. Horizontal differentiation gives

    [(Omega_x partial_x+Omega_y partial_y)U].e_x
       =-d s A^2 phi'/r,

because a cross e_y has e_x component -d. Vertical differentiation gives +2d s A^2 phi'/r. Their sum is +d s A^2 phi'/r. Also

    partial_r Omega.e_x=s[C'-A(phi')^2],
    J Omega.e_x=-As phi'.

Therefore the exact vorticity-profile residual is

    [Omega+B.grad Omega-(Omega.grad)U+omega J Omega].e_x
      =s(C+crC')-s A phi'[cr phi'+omega+d A/r]
      =-s A phi'[cr phi'+omega+d A/r].                (6)

The cancellation C+crC'=0 uses p+1=1/c. The term cr_j phi'=c kappa r_j^kappa tends to infinity. Thus (6) is nonzero for all sufficiently large j at every fixed finite omega. No pressure can repair a nonzero curl residual.

LIT29's original formula had 2d A/r in the bracket and stated that horizontal differentiation contributes no e_x component. Those two statements are false. Their correction leaves the non-profile conclusion and all integral screens intact.

## Scope and dependencies

The proof uses exact differentiation, L2 Riesz boundedness, local elliptic regularity, radial integration and volume packing. It does not assert the carrier-vorticity bracket, balances on all domains, or sufficiency of the checked scalar tests. It does not refute any theorem that assumes the full profile PDE.
