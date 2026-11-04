# Localization of backward limit sets and corrections to the bad-set claims

## Valid statements

Assume H0 and H1-prime, 0<c<1/2 and arbitrary finite omega. Write a=1-2c, X=cy+U, M=Jy dot U, B=X-omega Jy. Define

    Q={|X|^2-omega M<0},
    Q0={|X|^2-omega M<=0},
    Q1={a|X|^2+omega partial_theta P<=0}.

Q0 is closed and bounded: at infinity, |X|^2=c^2|y|^2+o(|y|^2) while omega M=o(|y|^2). It meets the rotation axis only where X=0. Q is disjoint from the axis. At a point of Q, writing rho=|y_h|, one has

    0< M/(omega rho^2)<1    when omega!=0,
    dtheta/ds=M/rho^2-omega.

Thus for omega>0 this angular speed lies strictly between -omega and zero; the signs reverse for omega<0. This is only a statement on Q, not every recurrent point.

Every alpha-limit set meets Q0 and Q1. Indeed, if it avoided Q0, continuity and compactness would make X dot B uniformly positive on a neighborhood of that set. The backward orbit eventually remains there, and

    d/dt H(Phi_-t x)=a X dot B

would force the bounded function H on the trapped orbit to grow without bound. The same argument with H+omega M, whose backward derivative is a|X|^2+omega partial_theta P, proves intersection with Q1. Q1 need not be bounded by the argument given here.

For every compactly supported B-invariant probability mu and C^1 f,

    integral B dot grad f dmu=0,
    omega integral partial_theta f dmu=integral X dot grad f dmu.

Using f=H,M,|y|^2/2,q gives the confirmed identities

    integral (|X|^2-omega M) dmu=0,
    a integral M dmu=-integral partial_theta P dmu,
    integral |X|^2 dmu=-(omega/a) integral partial_theta P dmu,
    integral (c|y|^2+y dot U) dmu=0,
    integral ((1-c)|U|^2+U dot grad P) dmu=0.        (1)

The last identity uses B dot grad q=U dot (DU B), whose invariant mean vanishes. It must not be justified by replacing U dot (DU B) with U dot (S B). Those quantities are different in general.

Combining the null point/cycle basins with these facts gives Theory Agent B  Corollary 6.3 in its precise form: almost every vortical initial point has a nonpoint, noncycle compact connected backward limit, meeting Q0, Q1 and {lambda_max(S)>=1}. Such a set carries an invariant probability. The exact nonstationary vortical measure spectrum applies only to measures actually giving full mass to both {B!=0} and {Omega!=0}.

## Refuted boundary assertion

The equality X dot B=0 at every B-zero proves N subset Q0. It does not prove N subset closure(Q), still less N subset boundary(Q). Take U=0, P constant, any c>0 and any nonzero omega. This is a decaying smooth exact profile. Then

    X=cy, B=(cI-omega J)y, X dot B=c^2|y|^2,
    N={0}, Q=empty, Q0={0}.

Thus N is not contained in the boundary or closure of Q. This directly refutes B05's boundary assertion under the full target class. Statements about alpha-limits should use Q0, not silently identify it with closure(Q).

A compact invariant set with X nonzero need not be shown to meet Q merely by integrating a nonnegative function. That calculation only produces zeros of the function, which may belong to Q0 minus closure(Q). No claim stronger than the Q0 localization is certified here.

## Other limits of the submitted discussion

Vorticity need not be globally bounded because U tends to zero; completeness uses the distinct proof A048. The exact contraction of a vortex segment puts it in an exponentially stable set, but does not identify the whole strong stable manifold without a spectral splitting. The conjectural Lorenz-model construction does not yet establish that the complete kinematic relaxation has such an attractor. Finally, the two-form transport plus Omega=curl U is already the curl of the full momentum equation, so it is not logically independent of all pressure coupling on simply connected R^3.

Audit recorded: 2026-11-02T18:56:51Z
