# Exact energy and recurrence screens without the profile equation

## Statements and scope

Fix 2/5<c<1/2 and any finite omega. Set p=1/c-1 in (1,3/2) and alpha=3-2p in (0,1). There are two smooth divergence-free fields U on R3, zero near the origin, for which

    |U(y)| <= C(1+|y|)^(-p),
    E(R) = integral_{|y|<R}|U|^2 = 8 pi R^alpha/(3 alpha), R>=1.

For every finite q>0, U belongs to Lq exactly when pq>3. Their actual curls are nonzero outside the unit ball and generate complete, volume-preserving conservative flows, with compact-set radius growth at most C_K(1+|t|)^{c/(1+c)}. Almost every point is recurrent in both directions under every fixed nonzero time map. Their rescalings R^p U(Ry) converge weakly to zero on compact annuli with fixed positive L2 norms, so do not converge strongly.

The first field has unbounded derivative and both signed helicity integrals infinite. The second has |DU|<=C(1+r)^(-2), hence a uniform Dini derivative envelope, and nonzero sign-changing helicity in L1 with total integral zero. In cylindrical vector components the second field has exactly the angular support {-1,0,1}.

Neither field solves the rotating profile equation for any pressure. They test the sufficiency of the listed screens; they do not refute a result assuming the full momentum or vorticity equation. In particular they do not refute the profile-specific strong-tail theorem A069.

## A common construction

Choose smooth chi with chi=0 for r<=1/4, chi=1 for r>=1/2 and 0<=chi<=1. Choose nonnegative nonzero smooth eta supported in (1/8,1/4). Put

    A_0=r^(-p)chi,
    I_0=integral_0^1 r^2 A_0^2 dr,
    I_eta=integral_0^1 r^2 eta^2 dr,
    M=((1/alpha-I_0)/I_eta)^(1/2), A=A_0+M eta.

The numerator is positive since I_0 is strictly below integral_0^1 r^{2-2p}dr=1/alpha. Disjointness of the two nonzero supports gives integral_0^1 r^2 A^2=1/alpha. For r>=1, A=r^(-p).

For any smooth unit vector a(r), let n=y/r and U=A(r)a(r) cross n, setting U=0 near zero. Radial derivatives and the antisymmetry of the cross product give div U=0. Direct differentiation gives

    Omega=(A'+A/r)a+A a'
        -[(A'-A/r)(a dot n)+A(a' dot n)]n,              (1)
    Omega dot n=2A(a dot n)/r,                          (2)
    U dot Omega=-A^2 n dot (a cross a').                (3)

One way to check (1) is to put g=A/r in U=g a cross y. Curl differentiation gives rg'[a-(a dot n)n] plus g[2a+r a'-r(a' dot n)n], which is (1). The angular integral of |a cross n|^2 is 8 pi/3, giving the exact energy after the core adjustment. For general q>0 its angular integral is a positive finite constant depending only on q, so the radial power integral gives the precise Lq threshold.

If Omega vanished at r>=1, (2) would give a dot n=0. Taking the dot product of (1) with a would then give A'+A/r=(1-p)r^(-p-1)=0, a contradiction. Thus its exterior zero set is empty.

## Complete conservative vorticity flow

Equation (2) bounds the radial velocity by 2r^(-p-1) for r>=1, uniformly in a'. Consequently the derivative along Omega of the smooth proper function (1+r^2)^((p+2)/2) is globally bounded. Smoothness bounds it on the remaining compact core. No trajectory can escape to infinity in finite time; ODE continuation gives completeness and the stated radius growth with exponent 1/(p+2)=c/(1+c).

A curl has zero divergence, so the complete flow preserves volume. If a positive-volume bounded set wandered under a fixed nonzero time map, its first N disjoint images would all lie in a ball of volume O(N^{3/(p+2)}). Their total volume is proportional to N, impossible since p>1. Intersecting any proposed positive-volume wandering set with a sufficiently large ball reduces to this bounded case. The usual last-return subsets of any finite-volume set would be wandering if recurrence failed on positive measure. Applying this to a countable basis and to the inverse time map gives conservativity and almost-everywhere topological recurrence in both directions.

## First case: rapid planar turning

Choose phi=r^4, a=(cos phi,sin phi,0), b=(-sin phi,cos phi,0). Then a'=phi' b and b'=-phi' a. On the positive z axis U=-A b, so

    |partial_r U|^2=(A')^2+(A phi')^2,

and |DU|>=4r^{3-p} outside. Formula (3) becomes h=-A^2 phi' n_z. Its mean on every centered sphere is zero. Each signed volume integral is a positive constant times integral_1^infinity r^{5-2p}dr, hence infinite.

On a fixed annulus delta<|y|<D, each component of R^p U(Ry) has radial phases exp(plus or minus i R^4 r^4). Pairing against a smooth test field, integrating first in angle and then by parts in r gives O(R^-4), since the phase derivative is bounded below by 4R^4 delta^3. Density of smooth tests and the uniform L2 bound give weak L2 convergence to zero. Direct integration gives the positive constant squared norm

    8 pi (D^alpha-delta^alpha)/(3 alpha).

For the profile screen use the necessary curl residual

    R_Omega=Omega+B dot grad Omega-(Omega dot grad)U+omega J Omega.

At y=r e_z, let C=(1-p)r^(-p-1), D_1=A phi'=4r^{3-p}. Then Omega=C a+D_1 b, U=-A b and Jy=0. The two nonlinear advection terms have zero component along a: horizontal differentiation of U and Omega at this axis contributes only a vertical vector. Differentiating the remaining radial terms gives

    R_Omega(r e_z) dot a
       = C+c r(C'-D_1 phi')-omega D_1
       = -4r^{3-p}(4c r^4+omega),                       (4)

because C+c r C'=0. This is nonzero for all sufficiently large r, for every finite omega.

## Second case: slow spherical turning

Set kappa=p-1 in (0,1/2), phi=r^kappa, and

    a(phi)=(cos phi cos(2phi), cos phi sin(2phi), sin phi).

It is a unit vector with |a_phi|^2=1+4cos^2 phi. Every component is a finite sum of nonconstant phases with frequencies 1 or 3. Since

    |DU| <= C(|A'|+A/r+A|a'|),
    A|a'| <= C r^(-p+kappa-1)=C r^-2,

the uniform derivative envelope has a finite integral against dR/R. Formula (3) and |a cross a'|=|a'| show that the absolute helicity integral on a sphere, including its area factor, is between two positive constant multiples of r^{kappa+1-2p}=r^-p. It is integrable at infinity. Its angular mean is zero and both signs occur, so h is nonzero, belongs to L1 and has total integral zero.

The weak-rescaling argument is the same integration by parts with phases exp(i m R^kappa r^kappa), m in {1,-1,3,-3}; the phase derivative is bounded below by a positive annulus constant times R^kappa. The norm remains the same positive constant, proving failure of strong convergence. For cylindrical components, the a_z e_z term contributes a nonzero angular mean azimuthal field. The two horizontal terms contribute exactly modes plus and minus one; their coefficients are not identically zero. This proves the stated exact support in that component convention.

It remains to exclude the profile equation. Take r_j=(2 pi j)^(1/kappa) and y=r_j e_z. At these radii,

    a=e_x, a_phi=2e_y+e_z, a_phiphi=-5e_x,
    U=-A e_y, Omega=C e_x+2A phi' e_y,

where C=(1-p)r^(-p-1). The e_x component of the radial derivative of Omega is C'-5A(phi')^2. The nonlinear advection terms have no e_x component: horizontal differentiation of U is (A/r)a cross v, and horizontal differentiation of the n term in (1) has only vertical and e_y components when v=U. Since J Omega has e_x component -2A phi',

    R_Omega(r_j e_z) dot e_x
       = -A phi'(5c r_j phi'+2omega).                   (5)

Here c r_j phi'=c kappa r_j^kappa tends to infinity. Thus (5) is nonzero for all sufficiently large j, for every finite omega. A pressure gradient has zero curl and cannot repair (4) or (5).

## Verification evidence

All claims follow from the displayed vector identities, exact radial integration, ODE continuation and a one-dimensional integration by parts. No numerical computation or external existence theorem is used. This independently verifies LIT27 and LIT28, including their explicit failure of the profile equation.
