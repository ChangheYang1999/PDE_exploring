# A nonzero kinematic field satisfying the frozen-vorticity restrictions

## Exact construction and claim

The construction below independently verifies LIT15. It is a smooth
nonzero divergence-free decaying velocity, but is not an Euler profile
for any c>0 or omega. Its Omega flow has bounded recurrent aperiodic
nonstationary orbits, zero compact invariant entropy, at most linear
derivative growth, square-zero derivatives at zeros, and zero invariant
mean of U.Omega.

Use the toroidal shell 1<r<2 with major radius R=4 and coordinates

    x=((R+r cos theta)cos phi,(R+r cos theta)sin phi,r sin theta).

Its metric is dr^2+r^2 dtheta^2+(R+r cos theta)^2 dphi^2 and its oriented
volume form is -J0 dr wedge dtheta wedge dphi, where
J0=r(R+r cos theta)>0. The orientation sign follows by taking the determinant
of the three displayed coordinate derivatives. Let alpha=sqrt(2) and choose
nonconstant g in C_c^infinity((1,2)). Define the globally smooth compactly
supported one-form A=g(r)(dphi-alpha dtheta), zero outside the shell.
The angle differentials are globally well-defined forms on the shell, even
though the angles themselves are circle-valued. Let V=A^sharp.

Contraction into the volume form gives

    Omega=curl V=(g'/J0)(d_theta+alpha d_phi),

because both i_Omega vol and dA equal
 g' dr wedge dphi-alpha g' dr wedge dtheta. This checks the orientation
and each component without a sign convention ambiguity.

## Dynamics and derivative bound

The radius is invariant. At g'(r)=0 the flow is stationary. Else the
angular ratio dphi/dtheta=alpha is irrational. More explicitly the smooth
change

    Theta=theta+(r/R)sin theta,
    Phi=phi+alpha(r/R)sin theta

has positive angular Jacobian 1+(r/R)cos theta and conjugates the flow to

    r'=0, Theta'=nu(r), Phi'=alpha nu(r), nu=g'/(rR).

It is a global diffeomorphism on each torus, smoothly depending on r.
At every nonstationary radius its flow is an irrational linear torus flow,
so all orbits are dense in that torus, aperiodic and recurrent in both
directions. Their closure is compact and there is no escape.

The exact transformed time-t map has derivative entries bounded by
C(1+|t|), the only unbounded terms being t nu' and alpha t nu'. On a closed
shell containing the support, the coordinate maps and their inverses have
bounded derivatives. Outside a slightly larger shell the vector field is
zero and the flow is the identity. Hence the global derivative norm is
at most C(1+|t|). For any compact invariant set, Euclidean covers at scale
of order epsilon/(1+T) span its orbit metric through time T with at most
C_K(1+T)^3 epsilon^-3 points. The resulting entropy is zero.

At an interior zero, g'=0, so DOmega=w tensor dr with w tangent to the
torus. Since dr(w)=0, its square vanishes. Outside the shell and at its
extension boundary the field vanishes on a neighborhood. Thus DOmega^2=0
at every zero.

## Solenoidal velocity and zero mean action

Let chi be the decaying Newtonian solution of Delta chi=div V:

    chi(x)=-(4pi)^-1 int div V(z)/|x-z| dz,
    U=V-grad chi.

The source is smooth and compactly supported, giving smooth chi and
U, with grad chi=O(|x|^-2), D^2 chi=O(|x|^-3). Thus U decays, DU tends
to zero, div U=0 and curl U=Omega. Nonzero Omega makes U nonzero.
Since A(Omega)=0,

    U.Omega=-Omega.grad chi.

For every compactly supported Omega-invariant probability measure,
differentiating its invariant integral of chi gives zero mean of the
right side. All differentiations occur on a compact set.

Finally Omega belongs to every L^p, p>0, and S tends to zero. The already
confirmed rotating vorticity Liouville theorem in
in the team records would force U constant if the complete
profile equation held for any c>0 and finite omega. This contradicts
nonzero Omega. Thus the example is only a counterexample to an inference
from the listed frozen-vorticity properties and Omega=curl U alone. It
does not satisfy the B/Omega transport relation and does not refute the
main conjecture. Its invariant tori are Omega tori, not B tori.

Audit recorded: 2026-11-02T18:46:07Z
